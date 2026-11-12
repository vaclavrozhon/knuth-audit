#!/usr/bin/env python3
"""Exact scalar CF oracles and symbolic folding-word validation for 4.5.3-41."""
from fractions import Fraction
from itertools import product
from math import factorial
from pathlib import Path
from random import Random
import argparse,json,os,time
ROOT=Path(__file__).resolve().parent
DEST=ROOT/'results/euclid-folding.json'

def K(w):
    a,b=1,0
    for x in w:a,b=x*a+b,a
    return a

def value(w):
    # Forward convergent recurrence, independent of word folding.
    p0,p1,q0,q1=1,0,0,1
    for x in w:p0,p1,q0,q1=p1,x*p1+p0,q1,x*q1+q0
    return Fraction(p1,q1)

def even_cf(x):
    a,b=x.numerator,x.denominator
    assert 0<x<1
    w=[]
    a,b=b,a
    while b:
        t,r=divmod(a,b);w.append(t);a,b=b,r
    if len(w)%2:w[-1:]=[w[-1]-1,1]
    return w

def normalize(w):
    w=list(w)
    while 0 in w:
        i=w.index(0);assert 0<i<len(w)-1
        w[i-1:i+2]=[w[i-1]+w[i+1]]
    assert all(not isinstance(x,int) or x>0 for x in w)
    return w

def fold(w,r):return normalize(w+[r-1,1,w[-1]-1]+w[-2::-1])
def tag(k):return ('E',k)
def fold_tag(w,k,l):return normalize(w+[l*l-1 if k==2 else tag(k),1,w[-1]-1]+w[-2::-1])
def nu(n):assert n>0;return (n&-n).bit_length()-1

def dragon(n):
    if not n:return 1
    return ((n>>nu(n))%4)//2

def first(n):
    q,r=divmod(n-1,20)
    if r in (3,16):return 2
    if r in (8,11):return 1+(q+r)%2
    if r==1:return 2-dragon(q)
    if r==18:return 1+dragon(q+1)
    return 1

def liouville(n,l,symbolic=False):
    def E(k):return (l*l-1 if k==2 else tag(k)) if symbolic else l**(factorial(k)*(k-1))-1
    r=n%4
    if r==1:return l-2+dragon(n-1)+(n//2)%4
    if r==2:return l+2-dragon(n+2)-(n//2)%4
    if r==0:return 1 if dragon(n)==0 else E(nu(n))
    return E(nu(n+1)) if dragon(n+1)==0 else 1

def binary(n,symbolic=False):
    def E(k):return tag(k) if symbolic else (1<<(factorial(k)*(k-1)))-1
    q,r=divmod(n-1,12)
    if r==0:return E(nu(q)+4) if q and dragon(q)==0 else 1
    if r==1:return 4-dragon(q)
    if r in (2,9):return 3
    if r in (3,8):return 1
    if r==4:return 2+q%2
    if r==5:return E(3) if q%2 else 1
    if r==6:return 1 if q%2 else E(3)
    if r==7:return 3-q%2
    if r==10:return 3+dragon(q+1)
    return E(nu(q+1)+4) if dragon(q+1) else 1

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    out=json.loads(DEST.read_text()) if args.resume and DEST.exists() else {}
    print('pid',os.getpid(),flush=True)
    def save(name,data):out[name]=data;DEST.write_text(json.dumps(out,indent=2)+'\n');print(name,json.dumps(data),flush=True)
    if 'identities' not in out:
        start=time.monotonic();rng=Random(45341);ct=0
        for _ in range(4096):
            m,n=rng.randrange(1,9),rng.randrange(1,9)
            x=[rng.randrange(-4,5) for _ in range(m)];y=[rng.randrange(-4,5) for _ in range(n)]
            left=K(x[:-1]+[x[-1]-1,1,y[-1]-1]+y[-2::-1])
            right=x[-1]*K(x[:-1])*K(y[::-1])+(-1)**n*K(x[:-1]+[0]+[-t for t in y[::-1]])
            assert left==right;ct+=1
        folds=0
        for n in range(1,7):
            for w in product(range(1,4),repeat=n):
                w=list(w);v=value(w);q=K(w)
                for r in range(1,6):
                    raw=w+[r-1,1,w[-1]-1]+w[-2::-1]
                    assert value(raw)==v+Fraction((-1)**n,q*q*r);folds+=1
        save('identities',dict(continuants=ct,folds=folds,seconds=time.monotonic()-start))
    if 'first_number' not in out:
        start=time.monotonic();w=[1,1];s=Fraction(1,2);exact=coeffs=0
        for k in range(1,14):
            assert w==even_cf(s);assert s.denominator==1<<((1<<k)-1)
            assert w==[first(n) for n in range(1,len(w)+1)]
            exact+=1;coeffs+=len(w)
            if k<13:w=fold(w,2);s+=Fraction(1,1<<((1<<(k+1))-1))
        while len(w)<81920:w=fold(w,2)
        assert w==[first(n) for n in range(1,len(w)+1)]
        save('first_number',dict(exact_partial_sums=exact,exact_coefficients=coeffs,symbolic_coefficients=len(w),seconds=time.monotonic()-start))
    if 'liouville_exact' not in out:
        start=time.monotonic();ct=coeffs=0
        for l in range(2,11):
            w=[l-1,l+1];s=Fraction(1,l)+Fraction(1,l*l)
            for m in range(2,8):
                assert w==even_cf(s);assert s.denominator==l**factorial(m)
                expected=[binary(n) if l==2 else liouville(n,l) for n in range(1,len(w)+1)]
                assert w==expected,(l,m)
                ct+=1;coeffs+=len(w)
                if m<7:w=fold(w,l**(factorial(m)*(m-1)));s+=Fraction(1,l**factorial(m+1))
        save('liouville_exact',dict(partial_sums=ct,coefficients=coeffs,bases=list(range(2,11)),max_factorial=7,seconds=time.monotonic()-start))
    if 'liouville_symbolic' not in out:
        start=time.monotonic();ct=0;zero_normalized=0
        for l in (2,3,4,17):
            w=[l-1,l+1]
            for m in range(2,17):
                expected=[binary(n,True) if l==2 else liouville(n,l,True) for n in range(1,len(w)+1)]
                assert w==expected,(l,m,next((i for i,(a,b) in enumerate(zip(w,expected)) if a!=b),None))
                if l==2 and m>=3:
                    raw=[liouville(n,2,True) for n in range(1,(1<<m)-1)]
                    assert normalize(raw)==w;zero_normalized+=len(raw)
                ct+=len(w)
                if m<16:w=fold_tag(w,m,l)
        save('liouville_symbolic',dict(coefficients=ct,raw_binary_coefficients=zero_normalized,max_stage=16,scope='Huge powers represented by exponent-stage tokens; these are exact symbolic comparisons, not enormous integer construction.',seconds=time.monotonic()-start))
    if 'dragon' not in out:
        ct=0
        for h in range(1,16):
            Q=1<<h
            assert dragon(Q)==0
            for t in range(1,Q):
                assert dragon(Q+t)+dragon(Q-t)==1
                assert nu(Q+t)==nu(Q-t);ct+=1
        for n in range(1,10001,2):assert 1-2*dragon(n)==(-1)**((n-1)//2)
        save('dragon',dict(reflections=ct,odd_jacobi=5000))
    out['status']='passed';out['final_pid']=os.getpid();out['scope']='General proofs are in euclid-folding.md; finite checks independently use Euclidean CF extraction and exact series sums.';DEST.write_text(json.dumps(out,indent=2)+'\n')
    print('passed',flush=True)
if __name__=='__main__':main()
