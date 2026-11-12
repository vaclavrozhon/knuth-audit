"""Independent sparse-polynomial oracle versus literal MIX instructions.

The oracle uses dictionaries, never follows the simulated list links. In
addition to coefficients it checks ordering, sentinels, ownership, register
contracts, exact published timings, and switch restoration.
"""
import sys
sys.dont_write_bytecode = True
import itertools, json, random
from pathlib import Path
from collections import Counter
from programs import assembly, symbols, Machine, number, Word, field, Undefined

HERE=Path(__file__).resolve().parent


def add(p,q):
    d=dict(q)
    for e,c in p.items():
        d[e]=d.get(e,0)+c
        if not d[e]: del d[e]
    return d


def mul(p,m):
    d={}
    for e,c in p.items():
        for f,dv in m.items():
            d[e+f]=d.get(e+f,0)+c*dv
    return {e:c for e,c in d.items() if c}


def stats(p,q):
    common=p.keys()&q.keys()
    cancel=sum(p[e]+q[e]==0 for e in common)
    return cancel,len(common)-cancel,len(p.keys()-q.keys()),len(q.keys()-p.keys())


def timeadd(p,q):
    c,n,pi,qi=stats(p,q)
    return 27*c+18*n+27*pi+8*qi+13


def timemult(p,q,m):
    sums=[0]*4
    for e in sorted(m,reverse=True):
        term={f+e:c*m[e] for f,c in p.items()}
        sums=[x+y for x,y in zip(sums,stats(term,q))]
        q=add(term,q)
    c,n,pi,qi=sums
    return 21*len(p)*len(m)+38*len(m)+29+27*c+18*n+27*pi+8*qi,sums


class Fixture:
    def __init__(self,b=64,overflow='halt',pool_count=100,extra=()):
        self.a=assembly(b,overflow,extra);self.s=symbols(self.a)
        self.m=Machine(b);self.a.load(self.m);self.b=b
        self.nodes=[];self.cursor=1000
        self.pool=list(range(2500,2500+2*pool_count,2))
        random.Random(987).shuffle(self.pool)
        self.chain(self.pool)
        self.m.mem[50]=number(self.pool[0] if self.pool else 0,b)
        # Distinct negative-zero and arbitrary register initializations detect
        # accidental dependence on scratch registers without violating entries.
        for i in range(8):self.m.reg[i]=number(-7*i,b,-1)
        self.m.overflow=True;self.m.comparison=-1

    def chain(self,nodes):
        for i,addr in enumerate(nodes):
            nxt=nodes[i+1] if i+1<len(nodes) else 0
            self.m.mem[addr]=number(-51,self.b)
            # Garbage ABC bits are deliberately nonzero; allocators overwrite.
            self.m.mem[addr+1]=number(7*self.b**2+nxt,self.b)

    def polynomial(self,p,zero_sign=1):
        n=len(p)+1
        ns=list(range(self.cursor,self.cursor+2*n,2));self.cursor+=2*n+8
        random.Random(self.cursor).shuffle(ns)
        self.nodes+=ns
        for i,(e,c) in enumerate([(-1,0)]+sorted(p.items(),reverse=True)):
            a=ns[i];nxt=ns[(i+1)%n]
            self.m.mem[a]=number(c,self.b,zero_sign)
            # The sign belongs to ABC, not the address of the next node.
            self.m.mem[a+1]=number((-1 if e<0 else 1)*(abs(e)*self.b**2+nxt),self.b)
        return ns[0]

    def read(self,head):
        p={};ns=[];a=head
        while a not in ns:
            assert a and a+1<4000,(a,ns)
            ns.append(a)
            w=self.m.mem[a+1];e=field(w,3).value(self.b)
            c=self.m.mem[a].value(self.b)
            if a==head:assert e==-1 and c==0,(a,e,c)
            else:
                assert e>=0 and c!=0 and e not in p,(a,e,c,p)
                assert not p or e<min(p),(a,e,p)
                p[e]=c
            a=field(w,37).value(self.b)
        assert a==head,(a,head)
        return p,ns

    def free(self):
        ns=[];a=self.m.mem[50].value(self.b)
        while a:
            assert a not in ns and a+1<4000,(a,ns)
            ns.append(a);a=field(self.m.mem[a+1],37).value(self.b)
        return ns

    def call(self,name,regs=(),limit=100000,trace=False):
        for r,v in regs:self.m.reg[r]=number(v,self.b)
        self.m.j=900;self.m.pc=self.s[name];self.m.halted=False
        start=self.m.time;counts=Counter();events=[]
        for _ in range(limit):
            if self.m.pc==900 or self.m.halted:break
            counts[self.m.pc]+=1
            if trace and self.m.pc in {self.s[x] for x in ['ANEXT','AINIT','ACOMP','ARETURN','AINSERT','MNEXT','MCYCLE']}:
                events.append({'pc':self.m.pc,'regs':[w.value(self.b) for w in self.m.reg],'avail':self.m.mem[50].value(self.b)})
            self.m.step()
        else:raise RuntimeError('finite budget exhausted, not a nontermination proof')
        return self.m.time-start,counts,events

    def partition(self,heads):
        used=[]
        for h in heads:used+=self.read(h)[1]
        free=self.free()
        assert len(set(used+free))==len(used+free)
        assert set(used+free)==set(self.nodes+self.pool),(used,free,self.nodes,self.pool)


def check_add(b,p,q,same=False):
    f=Fixture(b);ph=f.polynomial(p);qh=ph if same else f.polynomial(q)
    before={a:f.m.mem[a] for a in f.read(ph)[1] for a in (a,a+1)}
    t,ct,_=f.call('ADD',[(1,ph),(2,qh)])
    assert not f.m.halted
    assert f.read(qh)[0]==add(p,q)
    assert f.m.reg[1].value(b)==ph and f.m.reg[2].value(b)==qh
    assert t==timeadd(p,q),(p,q,t,timeadd(p,q))
    if not same:assert all(f.m.mem[a]==v for a,v in before.items())
    c,n,pi,qi=stats(p,q);m=c+n;pp=len(p);x=1+m+pi+qi
    # Every line count from the original listing is verified, not just sum.
    expected=[1,1+n,1+n,1+pp,1+pp,x,x,pi+qi,qi,qi,qi,m+1,
              m,m,m,m,c,c,c,c,c,c,c,pi,pi,pi,pi,pi,pi,pi,pi,pi,pi,pi]
    assert [ct[f.s['ADD']+k] for k in range(34)]==expected
    f.partition([ph] if same else [ph,qh])
    return t


def check_mult(b,p,q,m,same_pm=False):
    f=Fixture(b);ph=f.polynomial(p);qh=f.polynomial(q);mh=ph if same_pm else f.polynomial(m)
    initial=f.m.mem[:]
    t,ct,_=f.call('MULT',[(1,ph),(2,qh),(4,mh)])
    assert not f.m.halted
    assert f.read(qh)[0]==add(q,mul(p,m))
    assert [f.m.reg[i].value(b) for i in [1,2,4]]==[ph,qh,mh]
    for h in set([ph,mh]):
        for a in f.read(h)[1]:assert f.m.mem[a:a+2]==initial[a:a+2]
    assert t==timemult(p,q,m)[0],(p,q,m,t,timemult(p,q,m))
    for sw in ['SW1','SW2','SW3']:assert f.m.mem[f.s[sw]]==initial[f.s[sw]]
    f.partition(list(dict.fromkeys([ph,qh,mh])))
    return t


def check_util(b,p):
    f=Fixture(b);ph=f.polynomial(p,zero_sign=-1)
    initial=f.m.mem[:]
    t,_,_=f.call('COPY',[(1,ph)])
    qh=f.m.reg[2].value(b)
    assert t==21*len(p)+31 and f.m.reg[1].value(b)==ph
    assert f.read(qh)[0]==p
    for a in f.read(ph)[1]:assert f.m.mem[a:a+2]==initial[a:a+2]
    f.partition([ph,qh])
    t,_,_=f.call('ERASE',[(1,qh)])
    assert t==11;f.partition([ph])
    t,_,_=f.call('ZERO')
    zh=f.m.reg[2].value(b);assert t==18 and f.read(zh)[0]=={}
    f.partition([ph,zh])


def check_overflow(b):
    count=0
    for op in ['ADD','COPY','ZERO','MULT']:
        f=Fixture(b,pool_count=0);ph=f.polynomial({1:2});qh=f.polynomial({});mh=f.polynomial({1:3})
        f.call(op,[(1,ph),(2,qh),(4,mh)])
        assert f.m.halted and f.m.pc==f.s['OVERFLOW']+1
        count+=1
        f=Fixture(b,overflow='refill',pool_count=0);ph=f.polynomial({1:2});qh=f.polynomial({});mh=f.polynomial({1:3})
        f.pool=[3000,3002,3004,3006];f.chain(f.pool);f.m.mem[51]=number(3000,b)
        f.call(op,[(1,ph),(2,qh),(4,mh)])
        assert not f.m.halted and f.m.mem[51].value(b)==0
        if op=='ADD':assert f.read(qh)[0]=={1:2};f.partition([ph,qh,mh])
        elif op=='MULT':assert f.read(qh)[0]=={2:6};f.partition([ph,qh,mh])
        else:
            new=f.m.reg[2].value(b)
            assert f.read(new)[0]==({1:2} if op=='COPY' else {})
            f.partition([ph,qh,mh,new])
        count+=1
    return count


def run():
    counts=Counter();rng=random.Random(20261101)
    small=[{e:c for e,c in enumerate(cs) if c} for cs in itertools.product([-1,0,1],repeat=2)]
    for b in range(64,101):
        for p,q in itertools.product(small,repeat=2):
            check_add(b,p,q);counts['add_exhaustive']+=1
        for p in small:
            check_add(b,p,p,True);counts['add_alias']+=1
            check_util(b,p);counts['copy_erase_zero']+=3
        for _ in range(100):
            polys=[{e:rng.choice([-3,-2,-1,1,2,3]) for e in rng.sample(range(12),rng.randrange(6))} for _ in range(3)]
            check_add(b,*polys[:2]);counts['add_random']+=1
            check_mult(b,*polys);counts['mult_random']+=1
        for p,q in itertools.product(small,repeat=2):
            check_mult(b,p,q,p,True);counts['mult_pm_alias']+=1
        # Largest valid packed exponent and coefficient; no arithmetic overflow.
        check_add(b,{b**3-1:b**5-1},{0:-1});counts['boundaries']+=1
        check_add(b,{0:-(b**5-1)},{0:b**5-1});counts['boundaries']+=1
        check_mult(b,{b**3-2:b**5-1},{},{1:1});counts['boundaries']+=1
        check_util(b,{b**3-1:-(b**5-1)});counts['boundaries']+=3
        counts['overflow_halt_refill']+=check_overflow(b)
    # Printed example and exercises 6/10, interpreted as exponent in packed x.
    b=64
    p={(4-i)*b*b+i*b:i+1 for i in range(5)}
    m={2*b*b:1,b*b+b:-2,2*b:1}
    assert mul(p,m)=={6*b*b:1,b*b+5*b:-6,6*b:5}
    check_mult(b,p,{},m);counts['printed_product']+=1
    check_add(b,{b*b:1,b:1,1:1},{2*b*b:1,b:-2,1:-1});counts['printed_addition']+=1
    result={'counts':dict(counts),'total_subroutine_checks':sum(counts.values()),
            'radices':list(range(64,101)),
            'oracle':'independent sparse dictionaries; all graph ownership and contracts checked',
            'limits':'Valid input nodes are distinct except the explicit alias tests. All arithmetic intermediates fit. Fixed code/data locations; overflow recovery preserves live registers as required in 2.2.3-4.'}
    (HERE/'results'/'mix.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':run()
