"""Independent word-level execution and combinatorial checks for TAOCP 2.2.2.
No third-party packages; deterministic finite checks supplement notes' proofs.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from fractions import Fraction as F
from itertools import product
from math import comb
import json, random, time
from pathlib import Path

class Full(Exception): pass
class Empty(Exception): pass

@dataclass
class Stacks:
    cap: list[int]
    scheme: str = "simple"
    b: list[int] = field(init=False)
    t: list[int] = field(init=False)
    old: list[int] = field(init=False)
    mem: list = field(init=False)
    ref: list = field(init=False)
    moves: int = 0
    overflows: int = 0
    insertions: int = 0
    repack_intervals: list = field(default_factory=list)
    last_n: int = 0
    since: int = 0
    def __post_init__(self):
        self.n=len(self.cap); self.M=sum(self.cap)
        self.b=[0]
        for x in self.cap:self.b.append(self.b[-1]+x)
        self.t=self.b[:-1].copy();self.old=self.t.copy()
        self.mem=[None]*(self.M+1);self.ref=[[] for _ in self.cap]
    def check(self):
        assert self.b[0]==0 and self.b[-1]==self.M
        for i in range(self.n):
            assert self.b[i]<=self.t[i]<=self.b[i+1]
            assert self.mem[self.b[i]+1:self.t[i]+1]==self.ref[i],(i,self.b,self.t,self.mem,self.ref)
    def shift(self,j,new):
        delta=new-self.b[j]
        inds=range(self.b[j]+1,self.t[j]+1)
        if delta>0:inds=reversed(inds)
        if delta:
            for p in inds:self.mem[p+delta]=self.mem[p];self.moves+=1
        self.b[j]=new;self.t[j]+=delta
    def relocate(self,new):
        for j in range(1,self.n):
            if new[j]<self.b[j]:self.shift(j,new[j])
        for j in range(self.n-1,0,-1):
            if new[j]>self.b[j]:self.shift(j,new[j])
    def push(self,i,value,verify=True):
        self.insertions+=1;self.since+=1
        self.t[i]+=1
        overflow=self.t[i]>self.b[i+1]
        if overflow:
            self.overflows+=1
            if sum(self.t[j]-self.b[j] for j in range(self.n))>self.M:
                self.t[i]-=1
                raise Full
            if self.scheme=="simple":
                right=next((j for j in range(i+1,self.n) if self.t[j]<self.b[j+1]),None)
                if right is not None:
                    for p in range(self.t[right],self.b[i+1],-1):self.mem[p+1]=self.mem[p];self.moves+=1
                    for j in range(i+1,right+1):self.b[j]+=1;self.t[j]+=1
                else:
                    left=max(j for j in range(i) if self.t[j]<self.b[j+1])
                    # Corrected strict upper bound; TOP[i] is provisional.
                    for p in range(self.b[left+1]+1,self.t[i]):self.mem[p-1]=self.mem[p];self.moves+=1
                    for j in range(left+1,i+1):self.b[j]-=1;self.t[j]-=1
            else:
                sizes=[self.t[j]-self.b[j] for j in range(self.n)]
                S=self.M-sum(sizes);D=[max(self.t[j]-self.old[j],0) for j in range(self.n)]
                inc=sum(D);assert inc>0
                alpha=F(S,10*self.n);beta=F(9*S,10*inc)
                new=[self.b[0]];sigma=F(0)
                for j in range(1,self.n):
                    tau=sigma+alpha+D[j-1]*beta
                    new.append(new[-1]+sizes[j-1]+tau.numerator//tau.denominator-sigma.numerator//sigma.denominator)
                    sigma=tau
                if self.repack_intervals:
                    assert self.since>F(self.M-self.last_n,10*self.n)
                self.repack_intervals.append({'insertions':self.since,'old_N':self.last_n,'new_N':sum(sizes),'free':S})
                self.last_n=sum(sizes);self.since=0
                self.t[i]-=1;self.relocate(new);self.t[i]+=1;self.old=self.t.copy()
        self.mem[self.t[i]]=value;self.ref[i].append(value)
        if verify:self.check()
        return overflow
    def pop(self,i,verify=True):
        if self.t[i]==self.b[i]:raise Empty
        value=self.mem[self.t[i]];self.t[i]-=1
        assert value==self.ref[i].pop()
        if verify:self.check()
        return value

def compositions(m,n):
    if n==1:yield (m,);return
    for x in range(m+1):
        for rest in compositions(m-x,n-1):yield (x,)+rest

def check_simple_example():
    s=Stacks([0,0,0,20]);flags=[]
    for serial,(op,i) in enumerate([(1,0),(1,0),(1,3),(1,1),(-1,0),(1,2),(1,0),(1,0),(1,1),(1,3),(-1,1),(-1,0)]):
        if op==1:flags.append((serial+1,s.push(i,serial)))
        else:s.pop(i)
    assert s.b==[0,3,5,6,20] and s.t==[2,4,6,8]
    assert [a for a,b in flags if b]==[1,2,4,6,8,9]
    return {'bases':s.b,'tops':s.t,'overflow_operations':[a for a,b in flags if b]}

def check_overflow_comparison():
    count=0; hint_failures=[]; bound_failures=[]
    for n,M,length in [(2,3,7),(3,3,6)]:
        for caps in compositions(M,n):
            for seq in product(range(2*n),repeat=length):
                a=Stacks([0]*(n-1)+[M]);b=Stacks(list(caps));records=[0]*n
                for serial,op in enumerate(seq):
                    i=op//2
                    if op%2:
                        if not a.ref[i]:break
                        a.pop(i);b.pop(i)
                    else:
                        if sum(map(len,a.ref))==M:break
                        x=a.push(i,serial);y=b.push(i,serial)
                        size=len(a.ref[i])
                        if x and not y:
                            if not (size>records[i] and size<=caps[i]) and len(hint_failures)<5:
                                hint_failures.append({"capacities":caps,"sequence":seq,"stack":i+1,"size":size,"previous_max":records[i]})
                        records[i]=max(records[i],size)
                    assert all(x<=y for x,y in zip(a.b,b.b))
                    if a.overflows>b.overflows+M and len(bound_failures)<5:
                        bound_failures.append({"capacities":caps,"sequence":seq[:serial+1],"overflows0":a.overflows,"overflows1":b.overflows,"M":M})
                    count+=1
    return {"prefixes":count,"printed_hint_failures":hint_failures,"printed_bound_failures":bound_failures}

def check_expectations():
    count=0;example={}
    for n in range(1,5):
        for m in range(0,7):
            totals=[0]*4
            for seq in product(range(n),repeat=m):
                s=Stacks([0]*(n-1)+[m]);occ=[0]*n
                for k,i in enumerate(seq):
                    prev=sum(a>i for a in seq[:k]);s.push(i,k)
                    for t in range(4):
                        if occ[i]>=t:totals[t]+=prev
                    occ[i]+=1
                assert s.moves==sum(seq[j]>seq[k] for k in range(m) for j in range(k))
                count+=1
            assert F(totals[0],n**m)==F((n-1)*m*(m-1),4*n)
            for t in range(4):
                e=F(n*(n-1),2*n**m)*sum(comb(m,k)*(n-1)**(m-k)*(comb(k,2)-comb(t+1,2)) for k in range(t+1,m+1))
                assert F(totals[t],n**m)==e,(m,n,t,totals[t],e)
            if n==2 and m:
                exact=F(sum(comb(m,k)*max(k,m-k) for k in range(m+1)),2**m)
                assert exact==F(m,2)+F(m*comb(m-1,m//2),2**m)
    seq=(0,0,3,1,2,0,1,3,1,0)
    for t in [0,2]:
        occ=[0]*4;a=[]
        for k,i in enumerate(seq):
            a.append(sum(j>i for j in seq[:k]) if occ[i]>=t else 0);occ[i]+=1
        example[t]=a
    assert example[0]==[0,0,0,1,1,3,2,0,3,6]
    assert example[2]==[0,0,0,0,0,3,0,0,3,6]
    return {'sequences':count,'printed_examples':example}

def check_relocation():
    count=0
    for n,M in [(2,5),(3,5),(4,4)]:
        for sizes in product(range(M+1),repeat=n):
            if sum(sizes)>M:continue
            for gaps in compositions(M-sum(sizes),n):
                s=Stacks([a+b for a,b in zip(sizes,gaps)])
                for i,k in enumerate(sizes):
                    for j in range(k):s.push(i,(i,j))
                for newgaps in compositions(M-sum(sizes),n):
                    b=[0]
                    for a,g in zip(sizes,newgaps):b.append(b[-1]+a+g)
                    # Each legal new layout is also the starting layout for the next case.
                    s.relocate(b);s.check();count+=1
    return count

def experiment(seed=20261101):
    rng=random.Random(seed);records=[];checks=0
    for n,M in [(2,40),(5,200),(10,1000)]:
        for distribution in ['uniform','skewed','changing']:
            for target in [.5,.9,.99]:
                for replicate in range(3):
                    a=Stacks([0]*(n-1)+[M]);b=Stacks([0]*(n-1)+[M],"garwick")
                    size=0;steps=3000
                    for k in range(steps):
                        p=[1]*n if distribution=='uniform' else [10 if i==((k//500)%n if distribution=='changing' else 0) else 1 for i in range(n)]
                        i=rng.choices(range(n),weights=p)[0]
                        insertion=(size==0 or (size<M and rng.random()<(0.8 if size<M*target else .2)))
                        if insertion:a.push(i,k);b.push(i,k);size+=1
                        else:
                            if not a.ref[i]:continue
                            a.pop(i);b.pop(i);size-=1
                        assert a.ref==b.ref;checks+=1
                    records.append({'n':n,'M':M,'distribution':distribution,'target':target,'replicate':replicate,'operations':steps,'simple_moves':a.moves,'garwick_moves':b.moves,'simple_overflows':a.overflows,'garwick_repackings':b.overflows})
    return {'seed':seed,'verified_operations':checks,'runs':records}

def main():
    start=time.monotonic()
    result={'figure4':check_simple_example(),'insertion_models':check_expectations(),'relocations':check_relocation(),'comparison17_prefixes':check_overflow_comparison(),'monte_carlo':experiment()}
    result['elapsed_seconds']=time.monotonic()-start
    p=Path(__file__).parent/'results/sequential-allocation.json';p.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='monte_carlo'},indent=2));print('Monte Carlo runs',len(result['monte_carlo']['runs']),'operations',result['monte_carlo']['verified_operations'])
if __name__=='__main__':main()
