"""Executable audit of the complete two-word threaded MIX differentiator.

AST nodes are ('c', integer), ('v', name), or (operator, children...).
The oracle below has no pointers, register operations, or MIX arithmetic.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import collections, json, math, random
from programs import assemble,Machine,Word,number,field

HERE=Path(__file__).resolve().parent
C=lambda n:('c',n)
V=lambda s='X':('v',s)
TYPES={'c':0,'v':1,'ln':2,'neg':3,'+':4,'-':5,'*':6,'/':7,'^':8}
LABELS={'ln':'LOG','neg':'NEGOP','+':'PLUS','-':'MINUS','*':'TIMES','/':'SLASH','^':'UPARROW'}
CODE=' ABCDEFGHIΔJKLMNOPQRΣΠSTUVWXYZ0123456789.,()+-*/=$<>@;:\u2019'
# MIX characters for names are taken from the assembler's explicitly published table.
from mixal import CHARACTERS as CHARS

def info_name(s):
    return Word(1,tuple(CHARS.index(c) for c in s.ljust(5)))

def count(t):
    return 1+sum(map(count,t[1:])) if t[0] not in ('c','v') else 1

def iszero(t): return t==C(0)
def mult(u,v): return v if u==C(1) else u if v==C(1) else ('*',u,v)
def plus(u,v): return v if iszero(u) else u if iszero(v) else ('+',u,v)
def minus(u,v): return u if iszero(v) else ('neg',v) if iszero(u) else ('-',u,v)

def derivative(t):
    op=t[0]
    if op=='c': return C(0)
    if op=='v': return C(int(t[1]=='X'))
    u=t[1]; du=derivative(u)
    if op=='ln': return C(0) if iszero(du) else ('/',du,u)
    if op=='neg': return C(0) if iszero(du) else ('neg',du)
    v=t[2]; dv=derivative(v)
    if op=='+': return plus(du,dv)
    if op=='-': return minus(du,dv)
    if op=='*': return plus(C(0) if iszero(du) else mult(du,v),C(0) if iszero(dv) else mult(u,dv))
    if op=='/': return minus(C(0) if iszero(du) else ('/',du,v),C(0) if iszero(dv) else ('/',mult(u,dv),('^',v,C(2))))
    assert op=='^'
    first=C(0)
    if not iszero(du):
        r=u if v==C(2) else ('^',u,C(v[1]-1) if v[0]=='c' else ('-',v,C(1)))
        first=mult(du,mult(v,r))
    second=C(0) if iszero(dv) else ('*',mult(('ln',u),dv),('^',u,v))
    return plus(first,second)

class Fixture:
    def __init__(self,t,b=64,repair=False,shuffle=0,pool_end=3998,own=False):
        if own:
            from own_programs import rows,REDIRECT
            self.a=assemble(b,True,rows(),REDIRECT)
        else:self.a=assemble(b,repair)
        self.m=Machine(b); self.a.load(self.m); self.b=b
        self.available=list(range(2000 if own else 1000,pool_end+1,2))
        if shuffle: random.Random(shuffle).shuffle(self.available)
        for p,q in zip(self.available,self.available[1:]+[0]):
            self.m.mem[p]=self.word(q,0,0,False)
            self.m.mem[p+1]=number(777,b)
        self.m.mem[24]=number(self.available[0] if self.available else 0,b)
        self.input_nodes=[]
        slots=list(range(1000,1500,2)) if own else list(range(500,1000,2))
        if shuffle: random.Random(shuffle+1).shuffle(slots)
        def build(t):
            p=slots.pop(0); self.input_nodes.append(p)
            children=[] if t[0] in ('c','v') else [build(c) for c in t[1:]]
            self.m.mem[p]=self.word(children[0] if children else 0,0,TYPES[t[0]],False)
            self.m.mem[p+1]=number(t[1],b) if t[0]=='c' else info_name(t[1]) if t[0]=='v' else self.m.mem[self.sym(LABELS[t[0]])+1]
            for child,nextchild in zip(children,children[1:]+[p]):
                w=self.m.mem[child]
                self.m.mem[child]=self.word(self.left(child),nextchild,w.digits[2],nextchild==p)
            return p
        self.root=build(t)
        w=self.m.mem[self.root]
        self.m.mem[self.root]=self.word(self.left(self.root),20,w.digits[2],True)
        self.m.mem[20]=self.word(self.root,20,0,False)
        self.m.mem[22]=self.word(0,22,0,False)
        self.original={p:self.m.mem[p] for n in self.input_nodes for p in (n,n+1)}
        self.visits=collections.Counter()

    def sym(self,s): return self.a.symbols[s].value(self.b)
    def word(self,left,right,typ,tag):
        return Word(-1 if tag else 1,(right//self.b,right%self.b,typ,left//self.b,left%self.b))
    def left(self,p): return field(self.m.mem[p],37).value(self.b)
    def right(self,p): return field(self.m.mem[p],10).value(self.b)
    def decode(self,p,seen=None):
        if seen is None: seen=set()
        assert p and p not in seen,('cycle/alias',p)
        seen.add(p)
        w=self.m.mem[p]; op=next(op for op,k in TYPES.items() if k==w.digits[2])
        if op=='c':
            assert self.left(p)==0
            return C(self.m.mem[p+1].value(self.b))
        if op=='v':
            assert self.left(p)==0
            return V(''.join(CHARS[d] for d in self.m.mem[p+1].digits).rstrip())
        kids=[]; q=self.left(p)
        assert q
        while True:
            kids.append(self.decode(q,seen))
            if self.m.mem[q].sign<0:
                assert self.right(q)==p,('bad parent thread',q,p,self.right(q))
                break
            q=self.right(q)
        assert len(kids)==(1 if op in ('ln','neg') else 2)
        return (op,*kids)
    def call(self,label,registers=(),limit=200000):
        self.m.pc=self.sym(label);self.m.j=50
        for r,v in registers: self.m.reg[r]=number(v,self.b)
        start=self.m.time
        while self.m.pc!=50 and not self.m.halted:
            assert self.m.steps<limit,('step limit',self.m.pc)
            self.visits[self.m.pc]+=1
            self.m.step()
        assert not self.m.halted,('OVERFLOW',self.m.pc,len(self.available))
        return self.m.time-start
    def assert_original(self):
        assert all(self.m.mem[p]==w for p,w in self.original.items()),'input not restored'
    def partition(self,result):
        out=set(); self.decode(result,out)
        free=set();p=self.m.mem[24].value(self.b)
        while p:
            assert p not in free and p in self.available,('bad free list',p)
            free.add(p);p=self.left(p)
        assert not out.intersection(free)
        assert out.union(free)==set(self.available),('leak',len(out),len(free),len(self.available))
        return len(out),len(free)
    def differentiate(self):
        time=self.call('D1');p=self.left(22);out=self.decode(p)
        assert self.m.mem[p].sign<0 and self.right(p)==22
        self.assert_original();self.partition(p)
        return out,time

def smoke():
    cases=[C(0),C(2),V(),V('A'),('ln',V()),('neg',V()),('+',V(),V()),('-',V('A'),V()),('*',V(),V()),('/',V(),V()),('^',V(),C(2)),('^',V(),C(3)),('^',V(),V()),('-',('*',C(3),('ln',('+',V(),C(1)))),('/',V('A'),('^',V(),C(2))))]
    out=[]
    for t in cases:
        f=Fixture(t); actual,time=f.differentiate()
        assert actual==derivative(t),(t,actual,derivative(t))
        out.append({'input':t,'result':actual,'time':time,'steps':f.m.steps})
    copies=[]
    for t in cases:
        f=Fixture(t);time=f.call('COPY',[(1,f.root),(2,77),(3,88)])
        p=f.m.reg[1].value(f.b)
        assert f.decode(p)==t;f.assert_original();f.partition(p)
        assert f.m.reg[2].value(f.b)==77 and f.m.reg[3].value(f.b)==88
        copies.append({'n':count(t),'time':time,'printed':36*count(t)+22,'visits':{n:f.visits[a] for n,a in f.a.line_addresses.items() if 63<=int(n)<=104}})
    bounds=[]
    for b in range(64,101):
        B=b**5
        for t,kind in [(('*',C(-(B-1)),V()),'MULT-negative-bound'),(('^',V(),C(-(B-2))),'PWR-intermediate-bound')]:
            old=Fixture(t,b);bad,time=old.differentiate()
            new=Fixture(t,b,True);good,newtime=new.differentiate()
            assert bad!=derivative(t) and good==derivative(t)
            bounds.append({'b':b,'kind':kind,'input':t,'expected':good,'actual':bad,'overflow':old.m.overflow,'repair_overflow':new.m.overflow,'time':time,'repair_time':newtime})
    return {'smoke':out,'copy_timing':copies,'boundary_failures':bounds}

if __name__=='__main__':
    result=smoke()
    (HERE/'results'/'mix-smoke.json').write_text(json.dumps(result,indent=2)+'\n')
    print('complete differentiator',len(result['smoke']),'COPY',len(result['copy_timing']),'boundary cases',len(result['boundary_failures']))
    print('COPY singleton time',result['copy_timing'][0]['time'])
