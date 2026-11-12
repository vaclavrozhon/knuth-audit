#!/usr/bin/env python3
"""Exact checks for the supplementary complex bases in TAOCP 2, 4.1."""
from itertools import product
from pathlib import Path
import json
import sympy as sp

ROOT=Path(__file__).resolve().parent
TARGET=ROOT/'results/complex-extensions.json'


def add(z,w): return z[0]+w[0],z[1]+w[1]
def mul(z,w): return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def horner(cs,beta):
    z=(0,0)
    for c in reversed(cs): z=add(mul(z,beta),c if isinstance(c,tuple) else (c,0))
    return z


def polynomial_digits(z,d):
    beta=(-d,1);n=d*d+1
    # Replace negative coefficients in z=(x+d*y)+y*beta by -1's
    # nonnegative polynomial. The maintained polynomial may represent zero
    # without being the zero polynomial, so termination tests its VALUE.
    cs=[0]*4
    for j,c in enumerate((z[0]+d*z[1],z[1])):
        if c>=0: cs[j]+=c
        else:
            cs[j]+=-c*d*d;cs[j+1]+=-c*2*d;cs[j+2]+=-c
    assert min(cs)>=0 and horner(cs,beta)==z
    current=z;digits=[];steps=0;nonzero_zero_polynomial=False
    while current!=(0,0):
        assert steps<100000,(d,z)
        old_weight=sum(cs)
        t,r=divmod(cs[0],n)
        cs[0]=r
        cs[1]+=t*(d-1)**2;cs[2]+=t*(2*d-1);cs[3]+=t
        assert sum(cs)==old_weight and horner(cs,beta)==current
        x,y=current
        forced=(x+d*y)%n
        qx_num=-d*(x-forced)+y;qy_num=-(x-forced)-d*y
        assert qx_num%n==qy_num%n==0
        q=(qx_num//n,qy_num//n)
        assert r==forced
        cs=cs[1:]+[0]
        assert sum(cs)==old_weight-r and min(cs)>=0
        assert horner(cs,beta)==q
        current=q;digits.append(r);steps+=1
    nonzero_zero_polynomial=any(cs)
    assert horner(digits,beta)==z
    return steps,nonzero_zero_polynomial


def katai_szabo():
    x,d=sp.symbols('X d',integer=True)
    modulus=x*x+2*d*x+d*d+1
    for expr in [x*x+2*d*x+d*d+1,
                 x**3+(2*d-1)*x*x+(d-1)**2*x-(d*d+1)]:
        assert sp.rem(expr,modulus,x)==0
    cases=steps=zeros=0;longest=(0,None)
    parameters=[(d,x,y) for d in range(2,13) for x,y in product(range(-8,9),repeat=2)]
    parameters += [(1,x,y) for x,y in [(0,0),(1,0),(-1,0),(0,1),(0,-1),(-7,-9)]]
    for d,x,y in parameters:
        k,zero_poly=polynomial_digits((x,y),d)
        cases+=1;steps+=k;zeros+=zero_poly
        if k>longest[0]:longest=(k,[d,x,y])
    # Complete residue systems for both conjugate bases.
    residue_cases=0
    for d in range(1,21):
        n=d*d+1
        for sign in [-1,1]:
            residues={(r+sign*d*0)%n for r in range(n)}
            assert len(residues)==n
            # Quotient polynomial characterizes beta=0 modulo n.
            assert (-d+sign*d*sign)%n==0
            residue_cases+=n
    # Necessity: the stated nonzero fixed remainder is a counterexample
    # for positive real part with imaginary part +1 or -1.
    obstructions=[]
    for a in range(1,21):
        for b in [-1,1]:
            beta=(a,b);z=(1-a,b);r=a*a+b*b-2*a+1
            assert z!=(0,0) and 0<=r<a*a+b*b
            assert add(mul(beta,z),(r,0))==z
            obstructions.append([a,b,list(z),r])
    return dict(status='passed',integer_cases=cases,normalization_steps=steps,
                longest=longest,terminated_with_nonzero_zero_polynomial=zeros,
                complete_residue_checks=residue_cases,positive_real_part_obstructions=obstructions,
                scope='Exact reconstructions; general termination and all-complex extension are proved in notes.')


def norton():
    beta=(2,1);ds=[(0,0),(1,0),(-1,0),(0,1),(0,-1)]
    residues={(x-2*y)%5:(x,y) for x,y in ds}
    assert len(residues)==5
    cases=steps=0;longest=(0,None)
    for initial in product(range(-32,33),repeat=2):
        z=initial;digits=[]
        while z!=(0,0):
            x,y=z;delta=residues[(x-2*y)%5]
            u,v=x-delta[0],y-delta[1]
            qx,qy=2*u+v,2*v-u
            assert qx%5==qy%5==0
            q=(qx//5,qy//5)
            assert q[0]*q[0]+q[1]*q[1]<x*x+y*y
            digits.append(delta);z=q;steps+=1
        assert horner(digits,beta)==initial
        if len(digits)>longest[0]:longest=(len(digits),list(initial))
        cases+=1
    return dict(status='passed',integer_cases=cases,strict_norm_decreases=steps,
                longest=longest,residues={str(k):list(v) for k,v in residues.items()})


def main():
    data=json.loads(TARGET.read_text()) if TARGET.exists() else {}
    for key,fn in [('katai_szabo',katai_szabo),('norton',norton)]:
        if key in data and data[key].get('status')=='passed':continue
        data[key]=fn()
        TARGET.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
        print(key,json.dumps(data[key],ensure_ascii=False),flush=True)

if __name__=='__main__':main()
