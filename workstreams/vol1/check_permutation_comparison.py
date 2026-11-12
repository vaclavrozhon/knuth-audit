"""Explicit less-than programs for the additional claim in1.3.3 answer33."""
from itertools import product
from pathlib import Path
import json,random,time
ROOT=Path(__file__).resolve().parent
E=tuple(range(5));checks=0;started=time.monotonic()
def check(x):
    global checks
    assert x;checks+=1

def mul(a,b):return tuple(b[x] for x in a)
def inv(a):return tuple(a.index(x) for x in E)
def cyc(c):
    a=list(E)
    for x,y in zip(c,c[1:]+c[:1]):a[x]=y
    return tuple(a)
def conj(a,g):return mul(mul(inv(g),a),g)
def transform(seq,g):return [conj(x,g) for x in seq]
def result(a,b):
    r=E
    for x,y in zip(a,b):r=mul(mul(r,x),y)
    return r
C=cyc([0,1,2,3,4]);P=mul(cyc([0,3]),cyc([1,2]));Q=mul(cyc([0,4]),cyc([1,3]))
S=mul(cyc([1,2]),cyc([3,4]));T=cyc([2,3,4]);D=(0,4,3,2,1);R=(0,3,1,4,2)
check(conj(C,D)==inv(C));check(conj(mul(C,C),R)==C)
ea=[[P,Q],[E,E]];eb=[[E,E],[P,Q]]
a=[[conj(P,R)]*2,[E,E]];b=[[E,E],[conj(Q,R)]*2]
levels=[];rng=random.Random(13333)
for level in range(4):
    m=2**(2**level);short=4**(level+1)-2*3**level;printed=6**(level+1)-4**(level+1)
    check(len(a)==len(b)==m);check(all(len(x)==short for x in a+b));check(short<=printed)
    check(all(mul(x,x)==E for seq in a+b for x in seq))
    pairs=list(product(range(m),repeat=2)) if level<3 else [(rng.randrange(m),rng.randrange(m)) for _ in range(100)]+[(k,k) for k in [0,1,127,255]]
    for i,j in pairs:
        check(result(a[i]+[E]*(printed-short),b[j]+[E]*(printed-short))==(C if i<j else E))
    levels.append(dict(level=level,alphabet=m,constructed_length=short,printed_padded_length=printed,pairs_checked=len(pairs)))
    if level==3:break
    na=[];nb=[];nea=[];neb=[]
    for i,j in product(range(m),repeat=2):
        # High-digit less-than OR (high-digit equality AND low-digit less-than).
        na.append(a[i]+transform(ea[i],S)+transform(a[j],T)+transform(ea[i],mul(D,S))+transform(a[j],mul(D,T)))
        nb.append(b[i]+transform(eb[i],S)+transform(b[j],T)+transform(eb[i],mul(D,S))+transform(b[j],mul(D,T)))
        # Equality is needed at the next inductive level.
        nea.append(transform(ea[i],S)+transform(ea[j],T)+transform(ea[i],mul(D,S))+transform(ea[j],mul(D,T)))
        neb.append(transform(eb[i],S)+transform(eb[j],T)+transform(eb[i],mul(D,S))+transform(eb[j],mul(D,T)))
    a,b,ea,eb=na,nb,nea,neb
out=dict(checks=checks,elapsed_seconds=time.monotonic()-started,levels=levels)
(ROOT/'results/permutation-comparison.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
