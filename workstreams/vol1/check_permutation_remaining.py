"""Independent finite checks for the general proofs in1.3.3-28–38.

This does not settle the uniform tail in31 or implement the MIX routine in36.
"""
from itertools import permutations,product
from math import gcd
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parent
checks=0;start=time.monotonic()
def check(x,detail=None):
    global checks
    assert x,detail
    checks+=1

def identity(n):return tuple(range(n))
def compose(a,b):return tuple(b[x] for x in a)
def inverse(a):
    out=[0]*len(a)
    for i,x in enumerate(a):out[x]=i
    return tuple(out)
def cyc(n,c):
    a=list(range(n))
    for x,y in zip(c,c[1:]+c[:1]):a[x]=y
    return tuple(a)
def power(a,k):
    out=identity(len(a))
    while k:
        if k%2:out=compose(out,a)
        a=compose(a,a);k//=2
    return out

def cycles(a):
    unseen=set(range(len(a)));out=[]
    while unseen:
        x=min(unseen);c=[]
        while x in unseen:c.append(x);unseen.remove(x);x=a[x]
        assert x==c[0];out.append(c)
    return out

def josephus(n,m):
    living=list(range(n));rank=[0]*n;order=[];i=0
    for k in range(1,n+1):
        i=(i+m-1)%len(living);x=living.pop(i);rank[x]=k;order.append(x+1)
    return rank,order

def inverse_formula(n,m,k):
    x=k*m;iterations=0
    while x>n:
        x=(m*(x-n)-1)//(m-1);iterations+=1
    return x,iterations

for n in range(1,51):
 for m in range(1,26):
    rank,order=josephus(n,m);p=identity(n)
    for first in range(n-1):p=compose(p,power(cyc(n,list(range(n-1,first-1,-1))),m-1))
    check(tuple(x-1 for x in rank)==p,('28',n,m))
    if m>1:
        for k,x in enumerate(order,1):check(inverse_formula(n,m,k)[0]==x,('31 recurrence',n,m,k))
for n in range(1,201):
    rank,order=josephus(n,2);L=2*n+1
    s=tuple((2*(i+1))%L-1 for i in range(2*n));ret=list(range(n))
    for c in cycles(s):
        c=[x for x in c if x<n]
        for x,y in zip(c,c[1:]+c[:1]):ret[x]=y
    check(inverse(tuple(ret))==tuple(x-1 for x in rank),('29',n))
    for k,x in enumerate(order,1):
        d=L-2*k;r=(2*n//d).bit_length()-1
        check(L-d*2**r==x,('Shams formula',n,k))
    fixed={x for x,v in enumerate(rank,1) if x==v};expected=set()
    for r in range(1,L.bit_length()):
        den=2**(r+1)-1;num=(2**r-1)*L
        if num%den==0:expected.add(num//den)
    check(fixed==expected,('30',n,fixed,expected))

for n in range(1,8):
 for rho in permutations(range(n)):
    p=identity(n);current=rho
    for left in [*range(1,n-1,2),*range(0,n-1,2)]:
        labels={x:k for k,c in enumerate(cycles(current)) for x in c}
        if labels[left]!=labels[left+1]:
            swap=cyc(n,[left,left+1]);p=compose(p,swap);current=compose(current,swap)
    check(len(cycles(current))==1,('32b',rho,p))
    check(all(abs(p[k]-k)<=2 for k in range(n)),('32a',p))

E=identity(5);C=cyc(5,[0,1,2,3,4]);P=compose(cyc(5,[0,3]),cyc(5,[1,2]));Q=compose(cyc(5,[0,4]),cyc(5,[1,3]))
S=compose(cyc(5,[1,2]),cyc(5,[3,4]));T=cyc(5,[2,3,4])
def conj(a,g):return compose(compose(inverse(g),a),g)
def interleave(a,b):
    out=E
    for x,y in zip(a,b):out=compose(compose(out,x),y)
    return out
check(compose(P,Q)==C,('33 base',P,Q,compose(P,Q)))
check(compose(compose(compose(conj(C,S),conj(C,T)),conj(inverse(C),S)),conj(inverse(C),T))==C)
a=[[P,Q],[E,E]];b=[[E,E],[P,Q]]
for level in range(3):
    m=2**(2**level);length=2**(2*level+1)
    check(len(a)==len(b)==m);check(all(len(x)==length for x in a+b))
    check(all(compose(x,x)==E for seq in a+b for x in seq))
    for i,j in product(range(m),repeat=2):check(interleave(a[i],b[j])==(C if i==j else E),('33',level,i,j))
    if level<2:
        na=[];nb=[]
        for i,j in product(range(m),repeat=2):
            na.append([conj(x,S) for x in a[i]]+[conj(x,T) for x in a[j]]+[conj(x,S) for x in reversed(b[i])]+[conj(x,T) for x in reversed(b[j])])
            nb.append([conj(x,S) for x in b[i]]+[conj(x,T) for x in b[j]]+[conj(x,S) for x in reversed(a[i])]+[conj(x,T) for x in reversed(a[j])])
        a,b=na,nb

for l,m,n in product(range(13),repeat=3):
    size=l+m+n
    if not size:continue
    virtual=l+2*m+n;shift=l+m
    def following(k):
        k=(k+shift)%virtual
        if k>=size:k=(k+shift)%virtual
        return k
    p=tuple(following(k) for k in range(size))
    expected=tuple([*range(l+m,size),*range(l,l+m),*range(l)])
    check(p==expected,('35',l,m,n))
    d=gcd(l+m,m+n);check(len(cycles(p))==d)
    data=list(range(size))
    for j in range(d):
        saved=data[j];k=j;h=following(k)
        while h!=j:data[k]=data[h];k=h;h=following(k)
        data[k]=saved
    check(tuple(data)==expected)
for m,n in product(range(1,40),repeat=2):
    N=m+n;d=gcd(m,n);p=tuple((x+m)%N for x in range(N));cs=cycles(p)
    check(len(cs)==d and all(len(c)==N//d for c in cs))
    check(all(len([x for x in c if x<d])==1 for c in cs))

def two_long_cycles(p):
    n=len(p)
    if n<=2:return (cyc(n,list(range(n))),)*2
    a=next(x for x in range(n-1) if p[x]<n-1);b=p[a]
    sa=cyc(n,[n-1,a]);sb=cyc(n,[b,n-1]);rho=compose(compose(sa,p),sb)
    assert rho[-1]==n-1
    aa,bb=two_long_cycles(rho[:-1]);aa=aa+(n-1,);bb=bb+(n-1,)
    return compose(sa,aa),compose(bb,sb)
for n in range(1,8):
 for p in permutations(range(n)):
    even=(n-len(cycles(p)))%2==0
    if even:
        a,b=two_long_cycles(p)
        check(compose(a,b)==p and len(cycles(a))==len(cycles(b))==1,('37',p,a,b))
p=compose(compose(cyc(8,[0,1,2]),cyc(8,[3,4])),cyc(8,[5,6,7]));target=inverse(p)
solutions=[t for t in permutations(range(8)) if conj(p,t)==target]
check(len(solutions)==36)
for cs in [[[0,7],[1,6],[2,5],[3,4]],[[1,2],[6,7]],[[0,5,1,7,2,6]]]:
    t=identity(8)
    for c in cs:t=compose(t,cyc(8,c))
    check(t in solutions)
result=dict(checks=checks,elapsed_seconds=time.monotonic()-start,
            scope='28–30,31 recurrence only,32,33 orthogonality,34–35,37–38 selected identities',
            pending=['31 uniform tail','33 less-than construction','36 actual MIX and timing','primary references'])
(ROOT/'results/permutation-remaining.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
