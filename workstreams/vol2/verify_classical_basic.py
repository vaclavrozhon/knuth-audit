#!/usr/bin/env python3
"""Exact arithmetic and MIX checks of TAOCP 4.3.1 A/S/M, exercises 2-16.

Finite checks supplement the general proofs in notes/classical-basic.md.
Completed blocks are checkpoints; --resume does not rerun them.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse, json, random, time
from mix_float_machine import Machine, Word, word

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/classical-basic.json'
SOURCE=ROOT/'sources/classical-basic.mix'


def digits(u,b,n):
    assert 0<=u<b**n
    return [(u//b**i)%b for i in range(n)]


def value(u,b):return sum(x*b**i for i,x in enumerate(u))


def add(u,v,b):
    k=0;w=[];K=0
    for j,(x,y) in enumerate(zip(u,v)):
        assert value(u[:j],b)+value(v[:j],b)==value(w,b)+k*b**j
        k,z=divmod(x+y+k,b);w.append(z);K+=k
        assert k in (0,1)
    return w+[k],K


def subtract(u,v,b):
    k=0;w=[]
    for j,(x,y) in enumerate(zip(u,v)):
        assert value(u[:j],b)-value(v[:j],b)==value(w,b)+k*b**j
        k,z=divmod(x-y+k,b);w.append(z);assert k in (0,-1)
    return w,k


def left_add(u,v,b):
    n=len(u);w=[None]*n+[0];counts=Counter()
    for j in range(n-1,-1,-1):
        t=u[j]+v[j];w[j]=t%b;i=j;k=0
        while t>=b:
            i+=1;assert i<=n
            t=w[i]+1;w[i]=t%b;k+=1
        if k:counts[k]+=1
    return w,counts


def stream_add(u,v,b):
    n=len(u);i=n;r=0;written={};order=[]
    def emit(k,x):
        assert k not in written and 0<=x<b
        written[k]=x;order.append(k)
    for j in range(n-1,-1,-1):
        assert 0<=r<=b-2
        t=u[j]+v[j]
        if t>=b:
            emit(i,r+1)
            for k in range(i-1,j,-1):emit(k,0)
            i=j;r=t%b
        elif t<b-1:
            emit(i,r)
            for k in range(i-1,j,-1):emit(k,b-1)
            i=j;r=t
    emit(i,r)
    for k in range(i-1,-1,-1):emit(k,b-1)
    assert order==list(range(n,-1,-1))
    return [written[k] for k in range(n+1)]


def multiply(u,v,b,initial=0):
    m,n=len(u),len(v);w=digits(initial,b,m)+[None]*n;trace=[]
    for j in range(n):
        if v[j]==0:
            w[j+m]=0;continue
        k=0
        for i in range(m):
            assert value(w[:j+m],b)+k*b**(i+j)==initial+value(u,b)*value(v[:j],b)+value(u[:i],b)*v[j]*b**j
            t=u[i]*v[j]+w[i+j]+k;assert 0<=t<b*b
            k,w[i+j]=divmod(t,b);assert 0<=k<b
            trace.append({'step':'M5','i':i,'j':j,'t':t,'w':w.copy()})
        w[j+m]=k
        trace.append({'step':'M6','i':m,'j':j,'t':t,'w':w.copy()})
    assert value(w,b)==value(u,b)*value(v,b)+initial
    return w,trace


def short_divide(u,v,b):
    assert 0<v<b
    r=0;w=[0]*len(u)
    for j in range(len(u)-1,-1,-1):
        w[j],r=divmod(r*b+u[j],v)
        assert 0<=w[j]<b and 0<=r<v
        assert value(u[j:],b)==value(w[j:],b)*v+r
    return w,r


class ClassicalMachine(Machine):
    def __init__(self,beta,n,m=1):
        super().__init__(beta,source=SOURCE)
        self.symbols.update(N=n,M=m,MN=m*n,U=1000,V=1500,W=2000)
        self.external=set();self.writes=set()
    def put(self,name,ds):
        a=self.symbols[name]
        for i,x in enumerate(ds):self.memory[a+i]=word(x);self.external.add(a+i)
    def store(self,addr,field,w):
        if addr>=len(self.rows):
            assert addr in self.external and field==(0,5),(addr,field)
            self.memory[addr]=w;self.writes.add(addr)
        else:super().store(addr,field,w)
    def run(self,entry,outlen):
        self.put('W',[17]*outlen)
        self.ret=self.symbols[entry+'_END']
        self.execute(entry)
        return [self.memory[self.symbols['W']+i].val for i in range(outlen)]


def radix_block():
    count=0;distribution=[]
    for b,n in [(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(3,4),(4,3),(5,3),(10,2)]:
        total=Counter();Ksum=0
        for U in range(b**n):
            u=digits(U,b,n)
            for V in range(b**n):
                v=digits(V,b,n);w,K=add(u,v,b)
                assert value(w,b)==U+V
                wl,cs=left_add(u,v,b)
                assert wl==w==stream_add(u,v,b)
                assert sum(k*c for k,c in cs.items())==K
                total.update(cs);Ksum+=K
                ws,borrow=subtract(u,v,b)
                assert value(ws,b)==(U-V)%(b**n) and borrow==-(U<V)
                if borrow:
                    comp,borrow2=subtract([0]*n,ws,b)
                    assert value(comp,b)==V-U and borrow2==-1
                for d in range(1,b):
                    q,r=short_divide(u,d,b)
                    assert (value(q,b),r)==divmod(U,d)
                # Comparison of reversed digit lists is the printed lexical rule.
                assert (u[::-1]>v[::-1])-(u[::-1]<v[::-1])==(U>V)-(U<V)
                count+=1
        pairs=b**(2*n)
        for k in range(1,n+1):
            mk=F(b-1,2*b**k)*((n+1-k)*F(b-1,b)+F(1,b))
            assert F(total[k],pairs)==mk
        expected=F(1,2)*(n-F(1,b-1)*(1-F(1,b**n)))
        assert F(Ksum,pairs)==expected
        distribution.append({'b':b,'n':n,'pairs':pairs,'carry_counts':dict(total),'E_K':str(expected)})
    rng=random.Random(43109)
    for _ in range(2000):
        bases=[rng.randrange(2,21) for _ in range(rng.randrange(1,9))]
        u=[rng.randrange(b) for b in bases];v=[rng.randrange(b) for b in bases]
        k=0;U=V=W=0;weight=1
        for b,x,y in zip(bases,u,v):
            k,z=divmod(x+y+k,b);U+=x*weight;V+=y*weight;W+=z*weight;weight*=b
        assert U+V==W+k*weight
    return {'pairs':count,'carry_distributions':distribution,'mixed_radix_cases':2000}


def multiplication_block():
    count=0;rng=random.Random(43114)
    for b in range(2,7):
        for m,n in product(range(1,4),repeat=2):
            if b**(m+n)>5000:continue
            for U,V in product(range(b**m),range(b**n)):
                w,_=multiply(digits(U,b,m),digits(V,b,n),b)
                assert value(w,b)==U*V;count+=1
    for _ in range(3000):
        b=rng.randrange(2,101);m=rng.randrange(1,9);n=rng.randrange(1,9)
        U=rng.randrange(b**m);V=rng.randrange(b**n);initial=rng.randrange(b**m)
        multiply(digits(U,b,m),digits(V,b,n),b,initial)
    w,trace=multiply([4,1,9],[4,8],10)
    assert w==[6,7,7,6,7]
    expected=[('M5',0,0,16,[6,0,0,None,None]),('M5',1,0,5,[6,5,0,None,None]),
              ('M5',2,0,36,[6,5,6,None,None]),('M6',3,0,36,[6,5,6,3,None]),
              ('M5',0,1,37,[6,7,6,3,None]),('M5',1,1,17,[6,7,7,3,None]),
              ('M5',2,1,76,[6,7,7,6,None]),('M6',3,1,76,[6,7,7,6,7])]
    assert [(t['step'],t['i'],t['j'],t['t'],t['w']) for t in trace]==expected
    return {'exhaustive_products':count,'multiply_add_cases':3000,'table1':trace}


def mix_block():
    rng=random.Random(4310313);counts=Counter();examples={}
    for beta in [64,100,256]:
        B=beta**5
        for n in [1,2,4,8]:
            for case in range(40):
                def sample(length):
                    pool=[0,1,B-1,B-2,B//2]
                    return [rng.choice(pool) if case<20 else rng.randrange(B) for _ in range(length)]
                u,v=sample(n),sample(n);U,V=value(u,B),value(v,B)
                for entry in ['A','C8','S','C13']:
                    mm=ClassicalMachine(beta,n);uu,vv=(v,u) if entry=='S' and U<V else (u,v)
                    mm.put('U',uu);mm.put('V',vv)
                    want=(value(uu,B)-value(vv,B)) if entry=='S' else U*v[0] if entry=='C13' else U+V
                    length=n if entry=='S' else n+1
                    before={a:w for a,w in mm.memory.items() if a in mm.external}
                    out=mm.run(entry,length)
                    assert mm.halt is None and all(0<=x<B for x in out)
                    assert value(out,B)==want
                    assert all(mm.memory[a]==w for a,w in before.items())
                    if entry=='A':assert mm.time==10*n+6
                    if entry=='S':assert mm.time==12*n+3
                    if entry=='C8':assert mm.time==9*n+mm.visits['CL808']+7*mm.visits['CL809']+4
                    if entry=='C13':assert mm.time==23*n+mm.visits['CL1310']+5
                    counts[entry]+=1
                # Exchange the arithmetic instructions, keeping branch labels at their addresses.
                mm=ClassicalMachine(beta,n);uu,vv=(v,u) if U<V else (u,v)
                mm.put('U',uu);mm.put('V',vv)
                a=next(i for i,r in enumerate(mm.rows) if r[0]=='CLS05');c=a+1
                mm.rows[a][2:],mm.rows[c][2:]=mm.rows[c][2:],mm.rows[a][2:]
                out=mm.run('S',n)
                assert mm.halt is None and all(0<=x<B for x in out) and value(out,B)==abs(U-V)
                counts['S_swap05_06']+=1
                m=1+case%6;columns=[sample(n) for _ in range(m)]
                mm=ClassicalMachine(beta,n,m);mm.put('U',[x for c in columns for x in c])
                out=mm.run('C3',n+1)
                assert value(out,B)==sum(value(c,B) for c in columns)
                assert mm.time==5*m*n+7*n+mm.visits['CL310']+5
                counts['C3']+=1
        for m,n in product(range(1,7),repeat=2):
            for case in range(10):
                u=[rng.randrange(B) for _ in range(m)]
                v=[0 if rng.random()<.35 else rng.randrange(B) for _ in range(n)]
                if case==0:u=[B-1]*m;v=[B-1]*n
                if case==1:v=[0]*n
                mm=ClassicalMachine(beta,n,m);mm.put('U',u);mm.put('V',v)
                out=mm.run('PM',m+n)
                assert all(0<=x<B for x in out) and value(out,B)==value(u,B)*value(v,B)
                Z=v.count(0);K=mm.visits['CLM18'];Kp=mm.visits['CLM21']
                assert mm.time==27*m*(n-Z)+4*m+10*n+3-3*Z+K+Kp
                counts['M']+=1
    beta=64;B=beta**5
    for entry,m,n,uu,vv in [('C3',2,1,[B-1,1],[]),('C8',1,1,[B-1],[1])]:
        mm=ClassicalMachine(beta,n,m);mm.put('U',uu);mm.put('V',vv);out=mm.run(entry,n+1)
        examples[entry]={'byte_radix':beta,'word_radix':B,'M':m,'N':n,'u':uu,'v':vv,'w':out,'cycles':mm.time,'visits':dict(mm.visits),'trace':mm.trace}
    assert examples['C3']['cycles']==23 and examples['C8']['cycles']==21
    mm=ClassicalMachine(64,2);mm.put('U',[0,1]);mm.put('V',[1,0])
    a=next(i for i,r in enumerate(mm.rows) if r[0]=='CLS06');c=a+1
    mm.rows[a][2:],mm.rows[c][2:]=mm.rows[c][2:],mm.rows[a][2:]
    bad=mm.run('S',2);assert bad==[-1,1]
    examples['S_swap06_07']={'u':[0,1],'v':[1,0],'invalid_digits':bad,'expected_digits':[B-1,0]}
    return {'cases':dict(counts),'witnesses':examples,'semantics':'MIX byte radix beta; arithmetic digit radix B=beta^5; overflow initially clear; full-word stores cost2'}


def truncation_block():
    count=0;small=[]
    for b in range(2,31):
        for n in range(1,31):
            direct=sum((F((b-1)**2,b**(i+j)) for i in range(1,n+1) for j in range(1,n+1) if i+j>n+2),F(0))
            exact=F(n-2,b**(n+1))-F(n-1,b**(n+2))+F(1,b**(2*n))
            assert direct==exact
            if n>=3:assert 0<exact<F(n-2,b**(n+1))
            else:
                assert exact==0
                if b==10:small.append({'b':b,'n':n,'error':str(exact),'printed_strict_bound':str(F(n-2,b**(n+1)))})
            count+=1
    # Independent direct product minus the retained triangular sum, all digit pairs.
    enumerated=0
    for b,n in [(2,1),(2,2),(2,3),(3,3),(2,4)]:
        best=F(0)
        for U,V in product(range(b**n),repeat=2):
            u=digits(U,b,n)[::-1];v=digits(V,b,n)[::-1]
            kept=sum((F(x*y,b**(i+j+2)) for i,x in enumerate(u) for j,y in enumerate(v) if i+j+2<=n+2),F(0))
            error=F(U*V,b**(2*n))-kept
            assert error>=0;best=max(best,error);enumerated+=1
        exact=F(n-2,b**(n+1))-F(n-1,b**(n+2))+F(1,b**(2*n))
        assert best==exact
    return {'closed_form_cases':count,'exhaustive_pairs':enumerated,'boundary_witnesses':small,'scope':'omitted products before final rounding'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'scope':'4.3.1 A/S/M and2-16','blocks':{}}
    if OUT.exists() and not args.resume:raise SystemExit('Use --resume to preserve existing successful blocks')
    for name,fn in [('radix',radix_block),('multiplication',multiplication_block),('MIX',mix_block),('truncation',truncation_block)]:
        if name in data['blocks']:continue
        start=time.monotonic();result=fn();result['elapsed_seconds']=time.monotonic()-start
        data['blocks'][name]=result;OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,'PASS',flush=True)
    print('ALL CHECKPOINTS COMPLETE',flush=True)
if __name__=='__main__':main()
