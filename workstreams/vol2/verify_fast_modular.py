#!/usr/bin/env python3
"""4.3.3B: special inverse products, six-modulus multiplication, exercises 6/7.
Independent oracles: Python modular inverse and ordinary integer multiplication.
"""
from pathlib import Path
from math import gcd, prod
from itertools import combinations
import json, random, time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/fast-modular.json'

def reduce_mersenne(x,f):
    assert x>=0 and f>=1
    M=(1<<f)-1
    while x.bit_length()>f:x=(x&M)+(x>>f)
    return 0 if x==M else x

def rotate(x,a,f):
    assert 0<=x<=(1<<f)-1 and 0<=a<f
    M=(1<<f)-1
    z=((x<<a)&M)+(x>>(f-a))
    assert z<=M
    return 0 if z==M else z

def special_product(u,e,f,normalize=True,check=False):
    assert 0<e<f and gcd(e,f)==1 and 0<=u<1<<f
    M=(1<<f)-1;b=pow(e,-1,f)
    a=e;d=(b&1)*e;uk=reduce_mersenne(u,f) if normalize else u;v=(b&1)*uk
    initial=u
    def invariant(k):
        B=b% (1<<(k+1))
        c1=sum(pow(2,j*e,M) for j in range(1<<k))%M
        c2=sum(pow(2,j*e,M) for j in range(B))%M
        assert a==((1<<k)*e)%f and d==(B*e)%f
        assert uk==c1*initial%M and v==c2*initial%M
    if check:invariant(0)
    for k in range(1,b.bit_length()):
        bit=(b>>k)&1
        newa=2*a%f;newd=(d+bit*newa)%f
        newu=reduce_mersenne(uk+rotate(uk,a,f),f)
        newv=reduce_mersenne(v+bit*rotate(newu,d,f),f)
        a,d,uk,v=newa,newd,newu,newv
        if check:invariant(k)
    return v

def inverse_tests():
    small=0;failures=[];invariants=0
    for f in range(2,13):
        M=(1<<f)-1
        for e in range(1,f):
            if gcd(e,f)>1:continue
            inverse=pow((1<<e)-1,-1,M)
            for u in range(1<<f):
                want=u*inverse%M
                old=special_product(u,e,f,normalize=False)
                if old!=want:failures.append(dict(e=e,f=f,u=u,returned=old,expected=want))
                check=u in [0,1,M//2,M-1,M]
                got=special_product(u,e,f,check=check);assert got==want
                invariants+=check;small+=1
    assert failures==[dict(e=1,f=f,u=(1<<f)-1,returned=(1<<f)-1,expected=0) for f in range(2,13)]
    rng=random.Random(43332);large=0
    for f in [31,32,63,64,127,256,1024,4096,16384]:
        for j in range(12):
            e=rng.randrange(1,f)
            while gcd(e,f)>1:e=rng.randrange(1,f)
            u=(1<<f)-1 if j%3==0 else rng.getrandbits(f)
            got=special_product(u,e,f)
            assert got==u*pow((1<<e)-1,-1,(1<<f)-1)%((1<<f)-1)
            large+=1
    return dict(small_cases=small,full_invariant_checks=invariants,large_cases=large,
                max_f=16384,original_counterexamples=failures,seed=43332)

def reconstruct(residues,es):
    assert len(residues)==len(es) and es==sorted(es)
    ms=[(1<<e)-1 for e in es];digits=[]
    for j,(w,f) in enumerate(zip(residues,es)):
        assert 0<=w<ms[j]
        for i in range(j):
            w=special_product((w-digits[i])%ms[j],es[i],f)
        assert 0<=w<ms[j];digits.append(w)
    w=digits[-1]
    for i in range(len(es)-2,-1,-1):w=(w<<es[i])-w+digits[i]
    assert 0<=w<prod(ms)
    return w

def exponents(q):return [6*q+d for d in [-1,1,2,3,5,7]]

def parameter_tests():
    q=1;rows=[]
    for k in range(15):
        p=18*q+8;es=exponents(q)
        assert q==(3**k+1)//2 and p==3**(k+2)+17 and q%5!=3
        assert all(gcd(a,b)==1 for a,b in combinations(es,2))
        # Avoid constructing millions of bits for the asymptotic check.
        assert sum(es)==2*p+1 and min(es)>=5
        if k<=7:assert prod((1<<e)-1 for e in es)>1<<(2*p)
        if k:assert max(es)==18*previous_q+1<previous_p
        rows.append(dict(k=k,q=q,p=p,exponents=es))
        previous_q,previous_p=q,p;q=3*q-1
    # Exact rational comparison: log_3(6)<1.631, but not <1.63.
    assert 6**1000<3**1631 and 6**100>3**163
    return dict(levels=rows,mod5_cycle=[1,2,0,4],rounding_erratum_verified=True)

def crt_tests():
    cases=0;rng=random.Random(43328)
    for es in [[1,2],[1,2,3],[2,3,5],[3,4,5],[5,7,8]]:
        M=prod((1<<e)-1 for e in es)
        values=range(M) if M<10000 else [0,1,M-1]+[rng.randrange(M) for _ in range(300)]
        for w in values:
            residues=[w%((1<<e)-1) for e in es]
            assert reconstruct(residues,es)==w;cases+=1
    for q in [1,2,5,14,41,122,365]:
        es=exponents(q);M=prod((1<<e)-1 for e in es)
        for w in [0,1,M-1]+[rng.randrange(M) for _ in range(10)]:
            assert reconstruct([w%((1<<e)-1) for e in es],es)==w;cases+=1
    return dict(cases=cases,seed=43328,largest_q=365)

def multiply(u,v,k,qs,stats):
    p=18*qs[k]+8;assert 0<=u<1<<p and 0<=v<1<<p
    if k==0:
        stats['leaves']+=1;return u*v
    es=exponents(qs[k]);residues=[]
    for e in es:
        a=reduce_mersenne(u,e);b=reduce_mersenne(v,e)
        w=multiply(a,b,k-1,qs,stats)
        residues.append(reduce_mersenne(w,e))
    w=reconstruct(residues,es);stats['conversions']+=1
    return w

def multiplication_tests():
    qs=[(3**k+1)//2 for k in range(7)];rng=random.Random(4336)
    rows=[]
    for k,q in enumerate(qs):
        p=18*q+8;mask=(1<<p)-1
        pairs=[(0,mask),(1,mask),(mask,mask),(1<<(p-1),1<<(p-1))]
        pairs += [(rng.getrandbits(p),rng.getrandbits(p)) for _ in range(8 if k<5 else 2)]
        stats=dict(leaves=0,conversions=0)
        for u,v in pairs:assert multiply(u,v,k,qs,stats)==u*v
        assert stats['leaves']==len(pairs)*6**k
        rows.append(dict(k=k,p=p,cases=len(pairs),**stats))
    return dict(rows=rows,seed=4336,note='All intermediate inversions use (32), not a generic long multiplication.')

def main():
    d=json.loads(OUT.read_text()) if OUT.exists() else {}
    for name,fn in [('inverse',inverse_tests),('parameters',parameter_tests),('crt',crt_tests),('multiplication',multiplication_tests)]:
        if name in d:continue
        start=time.monotonic();result=fn();result['seconds']=round(time.monotonic()-start,3)
        d[name]=result;OUT.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'block':name,**result}),flush=True)
if __name__=='__main__':main()
