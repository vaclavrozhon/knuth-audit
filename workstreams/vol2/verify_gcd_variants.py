#!/usr/bin/env python3
"""Exact invariants for TAOCP4.5.2-38--40, independent of timing claims."""
from collections import Counter
from math import gcd, log2, sqrt
from pathlib import Path
import json, random, sys, time

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/gcd-variants.json'


def penk(u,v,counts,old=False):
    original = u,v
    k = 0
    while u%2 == v%2 == 0: u//=2;v//=2;k+=1
    x=(1,0,u);y=(v,1-u,v)
    t=(0,-1,-v) if u%2 else (1,0,u)

    def check(stage):
        for z in [x,y,t]:
            assert z[0]*u+z[1]*v == z[2]
            if old and not (0<=z[0]<=v and -u<=z[1]<=0):
                return dict(input=original,stage=stage,offending=z)
            assert 0<=z[0]<=v and -u<=z[1]<=0,(original,stage,z)
        assert 0<x[2]<=u and 0<y[2]<=v

    check('Y2')
    while True:
        while t[2]%2 == 0:
            assert t[2]
            both=t[0]%2==t[1]%2==0
            if u%2: assert both==(t[1]%2==0)
            if v%2: assert both==(t[0]%2==0)
            if both: t=tuple(z//2 for z in t);counts['even_coeff_halves']+=1
            else:
                assert (t[0]+v)%2==(t[1]-u)%2==0
                t=((t[0]+v)//2,(t[1]-u)//2,t[2]//2)
                counts['adjusted_halves']+=1
            err=check('Y3')
            if err:return err
        if t[2]>0:x=t
        else:y=(v-t[0],-u-t[1],-t[2])
        check('Y5')
        t=tuple(x[i]-y[i] for i in range(3))
        if t[0]<0 or (t[0]==0 and not old):
            if t[0]==0:counts['zero_first_coefficient_corrections']+=1
            t=(t[0]+v,t[1]-u,t[2])
        err=check('Y6')
        if err:return err
        if not t[2]:
            answer=(x[0],x[1],x[2]*2**k)
            assert answer[0]*original[0]+answer[1]*original[1]==answer[2]==gcd(*original)
            return answer


def penk_checks():
    counts=Counter();pairs=0
    for u in range(1,257):
        for v in range(1,257):penk(u,v,counts);pairs+=1
    rng=random.Random(45239)
    for _ in range(250):
        bits=rng.choice([32,64,127,256,512,1024])
        penk(rng.randrange(1,2**bits),rng.randrange(1,2**bits),counts);pairs+=1
    old=penk(3,1,Counter(),old=True)
    assert old['stage']=='Y6' and old['offending']==(0,2,2)
    return dict(input_pairs=pairs,counts=counts,known_1998_failure=old)


def kung(u,v,trace=None):
    assert u%2
    origin=u,v;M=max(abs(u),abs(v));c=s=t=0

    def bounds():
        # Square inequalities avoid nonintegral exponents and floating point.
        for value,e in [(u,s-c),(v,s+c)]:
            assert (value*value << max(e,0)) <= (M*M << max(-e,0)),(origin,u,v,s,c)
        assert u%2 and gcd(u,v)==gcd(*origin)

    while True:
        t+=1;bounds()
        if trace is not None:trace.append(dict(u=u,v=v,c=c,s=s,K2=t))
        if v==0:
            assert t<=s+2 and 2**s<=M*M
            return abs(u),s,t
        while v%2==0:
            v//=2;c+=1;s+=1;bounds()
        if c>0:u,v=v,u;c=-c
        bounds()
        w=(u+v)//2
        v=w if w%2==0 else w-v
        assert v%2==0 and c<=0
        bounds()


def kung_checks():
    pairs=0;maxratio=(0,None)
    for u in range(-63,64,2):
        for v in range(-64,65):
            d,s,t=kung(u,v)
            assert d==gcd(u,v)
            pairs+=1
    rng=random.Random(45240)
    for _ in range(250):
        bits=rng.choice([32,64,128,256,512])
        u=rng.randrange(-2**bits,2**bits)|1;v=rng.randrange(-2**bits,2**bits)
        kung(u,v);pairs+=1
    trace=[]
    assert kung(1,11,trace)==(1,4,6)
    family=0
    for k in range(2,301):
        d,s,t=kung(1,3*2**k-1)
        assert d==1 and s==2*k and t==k+4
        assert 2**(k+1)<3*2**k-1<2**(k+2)
        family+=1
    previous,current=3,1;records=[];direct=0
    for j in range(1,20001):
        if j<=100 or j in [256,512,1024]:
            d,s,t=kung(current,2*previous)
            assert d==1 and s==2*j+2 and t==2*j+3
            direct+=1
        new=min(abs(3*current-16*previous),abs(5*current-16*previous))
        # Verify the two-round induction prefix for every j, including signs.
        x,y,c=current,new,-1
        w=(x+y)//2;y=w if w%2==0 else w-y
        assert y%4==2
        y//=2;c+=1
        w=(x+y)//2;y=w if w%2==0 else w-y
        assert (x,y,c)==(current,2*previous,0)
        if j in [10,100,1000,10000,20000]:
            records.append(dict(j=j,bits=max(current,2*previous).bit_length(),
                                log2_max_over_j=log2(max(current,2*previous))/j))
        previous,current=current,new
    return dict(signed_input_pairs=pairs,first_family_cases=family,
                recurrence_direct_runs=direct,recurrence_prefixes=20000,
                empirical_ratios=records,phi=(1+sqrt(5))/2,small_trace=trace)


def gosper_batch(u,v,bits,counts):
    W=2**bits;mask=W-1
    shift=max(0,max(u.bit_length(),v.bit_length())-bits)
    h,j=u>>shift,v>>shift;lu,lv=u&mask,v&mask
    A=(1,0);B=(0,1);s=0
    while s<bits:
        # Low input words determine parity up to the allowed number of shifts.
        pu=((A[0]*lu+A[1]*lv)>>s)&1
        pv=((B[0]*lu+B[1]*lv)>>s)&1
        if not pu:
            C=A;D=(2*B[0],2*B[1]);mode='halve_u'
        elif not pv:
            C=(2*A[0],2*A[1]);D=B;mode='halve_v'
        else:
            a,b=A[0]-B[0],A[1]-B[1]
            lower=a*h+b*j+min(a,0)+min(b,0)
            upper=a*h+b*j+max(a,0)+max(b,0)
            if lower>0:
                C=(a,b);D=(2*B[0],2*B[1]);mode='subtract_u'
            elif upper<0:
                C=(2*A[0],2*A[1]);D=(-a,-b);mode='subtract_v'
            else:
                counts['uncertain_sign_stops']+=1;break
        if max(abs(z) for z in C+D)>=W:
            counts['coefficient_stops']+=1;break
        # Full integers below are a validation oracle, not simulation decisions.
        x=(A[0]*u+A[1]*v)>>s;y=(B[0]*u+B[1]*v)>>s
        assert (x%2,y%2)==(pu,pv)
        if mode=='subtract_u':assert x>y
        if mode=='subtract_v':assert y>x
        A,B=C,D;s+=1
        au=A[0]*u+A[1]*v;bv=B[0]*u+B[1]*v
        assert au%2**s==bv%2**s==0
        nx,ny=au>>s,bv>>s
        assert nx>0 and ny>0 and nx+ny<x+y and gcd(nx,ny)==gcd(u,v)
        assert A[0]>0 and A[1]<=0 and B[0]<=0 and B[1]>0
        assert A[0]*B[1]-A[1]*B[0]==2**s
        counts[mode]+=1
    if s:
        counts['batches']+=1;counts['full_word_batches']+=s==bits
        return (A[0]*u+A[1]*v)>>s,(B[0]*u+B[1]*v)>>s
    counts['fallbacks']+=1
    if u%2==0:return u//2,v
    if v%2==0:return u,v//2
    if u>v:return (u-v)//2,v
    return u,(v-u)//2


def gosper(u,v,bits,counts):
    origin=u,v;k=0
    while u%2==v%2==0:u//=2;v//=2;k+=1
    while u!=v:u,v=gosper_batch(u,v,bits,counts)
    assert u*2**k==gcd(*origin)


def gosper_checks():
    counts=Counter();pairs=0;rng=random.Random(45238)
    for bits in [2,3,4,8]:
        for u in range(1,129):
            for v in range(1,129):gosper(u,v,bits,counts);pairs+=1
        for _ in range(80):
            n=rng.choice([32,64,127,256,512,1024])
            gosper(rng.randrange(1,2**n),rng.randrange(1,2**n),bits,counts);pairs+=1
    assert counts['full_word_batches'] and counts['coefficient_stops'] and counts['uncertain_sign_stops']
    # Boundary of the coefficient bound: a complete three-shift batch need not fit.
    u,v,W=463,65,8
    assert u-(W-1)*v==W and gcd(u,v)==1
    assert not any(a*u+b*v==W*v for a in range(1-W,W) for b in range(1-W,W))
    return dict(input_pairs=pairs,word_bits=[2,3,4,8],counts=counts,
                guard_example=dict(u=u,v=v,W=W,matrix=[[1,-7],[0,8]]))


def arithmetic_checks():
    from sympy import Matrix, mobius, totient
    repunits=0;matrices=0;column_entries=0;rng=random.Random(45242)
    for a in [1,2,3,5,10,16,256]:
        for m in range(33):
            for n in range(33):
                assert gcd(a**m-1,a**n-1)==a**gcd(m,n)-1
                repunits+=1
    for n in range(1,17):
        families=[list(range(n+1)),[1]*(n+1),[0]*(n+1),[rng.randrange(-9,10) for _ in range(n+1)]]
        for f in families:
            g=[0]+[sum(int(mobius(k//d))*f[d] for d in range(1,k+1) if k%d==0) for k in range(1,n+1)]
            A=Matrix(n,n,lambda i,j:f[gcd(i+1,j+1)])
            product=1
            for k in range(1,n+1):product*=g[k]
            assert A.det(method='bareiss')==product
            C=A.copy()
            for k in range(1,n+1):
                for j in range(2*k,n+1,k):C[:,j-1]=C[:,j-1]-C[:,k-1]
            for i in range(1,n+1):
                for j in range(1,n+1):
                    assert C[i-1,j-1]==(g[j] if i%j==0 else 0)
                    column_entries+=1
            if f==list(range(n+1)):
                assert g[1:]==[int(totient(k)) for k in range(1,n+1)]
            matrices+=1
    return dict(repunit_pairs=repunits,bases=[1,2,3,5,10,16,256],
                matrices=matrices,largest_dimension=16,column_entries=column_entries)


if __name__=='__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('penk',penk_checks),('kung',kung_checks),('gosper',gosper_checks),('arithmetic',arithmetic_checks)]:
        if name in data:continue
        start=time.monotonic();value=fn()
        data[name]=dict(status='passed',seconds=time.monotonic()-start,result=value)
        OUT.write_text(json.dumps(data,indent=2)+'\n')
        print(name,'passed',round(data[name]['seconds'],3),flush=True)
