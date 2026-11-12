#!/usr/bin/env python3
"""Exact checks of both bounds and the construction in TAOCP 4.5.3-38."""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json, os, time
from flint import arb, ctx

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/euclid-maximum.json'
# A pair (a,b) denotes a+b*phi; phi^2=phi+1.
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y):
    a,b=x;c,d=y
    return (a*c+b*d,a*d+b*c+b*d)
def scale(x,c): return (c*x[0],c*x[1])
def sign(x):
    # 2(a+b*phi)=(2a+b)+b*sqrt(5); compare by exact squares.
    a,b=x;p=2*a+b;q=b
    if q==0:return (p>0)-(p<0)
    if p==0:return (q>0)-(q<0)
    if p>0 and q>0:return 1
    if p<0 and q<0:return -1
    delta=p*p-5*q*q
    assert delta!=0
    return ((delta>0)-(delta<0))*((p>0)-(p<0))

FIB=[0,1]
for _ in range(420):FIB.append(sum(FIB[-2:]))
POS=[(1,0)];NEG=[(1,0)]
for _ in range(420):
    POS.append(mul(POS[-1],(0,1)))
    NEG.append(mul(NEG[-1],(-1,1)))

def divisions(a,b,trace=False):
    steps=0;rows=[]
    while b:
        q,r=divmod(a,b)
        if trace:rows.append([a,b,q,r])
        a,b=b,r;steps+=1
    return steps,rows

def exhaustive_maxima():
    rows=[];pairs=0;printed_failures=0
    for n in range(1,2049):
        vals=[divisions(r,n)[0] for r in range(n)]
        pairs+=n;L=max(vals);r=vals.index(L)
        assert n>=FIB[L+1]
        rad=(1-n,2*n)  # sqrt(5)*n+1
        assert sign(add(rad,neg(POS[L+1])))>0
        assert sign(add(POS[2*L+2],neg(rad)))>0
        if sign(add(POS[L+2],neg(rad)))>0:printed_failures+=1
        if n<=32 or n in (100,1000,2048):
            rows.append({'n':n,'L':L,'attaining_m':r if r else n})
    return {'n_max':2048,'residue_pairs':pairs,'selected_maxima':rows,
            'printed_bound_failures':printed_failures,
            'scope':'All positive m covered through all residues modulo n.'}

def lower_construction():
    count=0;hist={};large=[]
    inputs=list(range(3,8193))
    inputs += sorted(set(FIB[j]+d for j in range(25,201,7) for d in (-1,0,1)))
    for n in inputs:
        m=(isqrt(5*n*n)-n)//2+1
        assert 0<m<n
        eps=(Fraction(m,n)+1,Fraction(-1))
        assert sign(eps)>0 and sign(add((Fraction(1,n),0),neg(eps)))>0
        a,b=n,m;qs=[];z=None;k=None
        while b:
            q,r=divmod(a,b);qs.append(q)
            if q>=2 and k is None:k=len(qs);z=Fraction(a,b)
            a,b=b,r
        assert k>=2 and k%2==0 and z>=2
        numerator=add(NEG[k-1],scale(eps,FIB[k-1]))
        denominator=add(NEG[k],neg(scale(eps,FIB[k])))
        assert sign(denominator)>0
        assert add(numerator,neg(scale(denominator,z)))==(0,0)
        # The exact algebraic inequality (B7), then its strict consequence.
        rhs=mul(POS[k],scale(eps,FIB[k+2]))
        assert sign(add(rhs,neg((2,-1))))>=0
        assert sign(add(POS[2*k+4],neg((1-n,2*n))))>0
        T=divisions(m,n)[0]
        assert T==len(qs)+1 and T>=k+1
        assert sign(add(POS[2*T+2],neg((1-n,2*n))))>0
        count+=1;hist[k]=hist.get(k,0)+1
        if n>8192 and len(large)<8:large.append({'n':n,'m':m,'k':k,'T':T})
    return {'inputs':count,'initial_range':'3..8192',
            'additional_inputs':'F_j-1,F_j,F_j+1 for j=25,32,...,200',
            'first_nonunit_index_histogram':hist,'selected_large_examples':large}

def upper_sharpness():
    count=0
    for s in range(1,201):
        n=FIB[s+1];m=FIB[s+2]
        T,_=divisions(m,n)
        assert T==s and n<FIB[s+2]
        rad=(1-n,2*n)
        assert sign(add(rad,neg(POS[s+1])))>0
        assert sign(add(POS[s+2],neg(rad)))>0
        count+=1
    ctx.dps=70;phi=(1+arb(5).sqrt())/2
    rows=[]
    for m,n in ((1,1),(5,3),(8,5)):
        T,trace=divisions(m,n,True)
        B=(arb(5).sqrt()*n+1).log()/phi.log()-2
        assert B<arb(T)
        rows.append({'m':m,'n':n,'T':T,'trace':trace,'printed_rhs_ball':str(B)})
    return {'Fibonacci_families':count,'s_range':'1..200','counterexamples':rows}

def main():
    t=time.time();out={'pid':os.getpid(),'status':'running','checkpoints':{}}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print('PID',os.getpid(),flush=True)
    for name,fn in [('complete_maxima',exhaustive_maxima),('lower_construction',lower_construction),('upper_sharpness',upper_sharpness)]:
        out['checkpoints'][name]=fn();OUT.write_text(json.dumps(out,indent=2)+'\n')
        print(name,'PASS',flush=True)
    out['status']='passed';out['elapsed_seconds']=time.time()-t
    OUT.write_text(json.dumps(out,indent=2)+'\n');print('PASS',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
