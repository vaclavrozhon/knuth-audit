#!/usr/bin/env python3
"""Numerical, not interval-certified, fixed point of the binary-gcd tail operator.

Uses a uniform grid in z=sqrt(-log(x)), local degree15 interpolation,
and independent formulas for constants. Follows the documented Brent grid
idea; all arithmetic and convergence diagnostics are reproduced locally.
"""
from pathlib import Path
import json,sys,time
import numpy as np
import mpmath as mp
from math import comb

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/gcd-distribution.json'
ld=np.longdouble


def stencil(t,N):
    base=np.floor(t).astype(np.int64)-7
    ix=base[...,None]+np.arange(16)
    delta=t[...,None]-ix
    exact=delta==0
    weights=np.array([(-1)**j*comb(15,j) for j in range(16)],dtype=ld)
    weights=weights/np.where(exact,ld(1),delta)
    weights/=weights.sum(axis=-1)[...,None]
    hit=exact.any(axis=-1)
    weights=np.where(hit[...,None],exact.astype(ld),weights)
    # H(z)=G(exp(-z²)) is even at zero. Its far tail is one to negligible error.
    ix=np.minimum(np.abs(ix),N).astype(np.int32)
    tail=t>N
    return ix,weights,tail


def evaluate(H,prepared):
    ix,w,tail=prepared
    return np.where(tail,ld(1),(H[ix]*w).sum(axis=-1))


def calculate(N):
    start=time.monotonic();zmax=ld(8);h=zmax/N
    z=np.arange(N+1,dtype=ld)*h;ln2=np.log(ld(2));zs=z*z
    terms=[]
    for k in range(1,81):
        # For a=x/(x+2^k), b=1/(1+2^k*x), use stable logarithms.
        za=np.sqrt(np.logaddexp(ld(0),zs+k*ln2))/h
        zb=np.sqrt(np.logaddexp(ld(0),k*ln2-zs))/h
        terms.append((ld(2)**(-k),stencil(za,N),stencil(zb,N)))
    H=-np.expm1(-zs);diagnostics=[]
    for it in range(1,46):
        nxt=np.zeros(N+1,dtype=ld)
        for weight,sa,sb in terms:
            nxt+=weight*(evaluate(H,sa)-evaluate(H,sb))
        residual=np.max(np.abs(nxt-H));H=nxt
        if it in [1,2,5,10,15,20,25,30,35,40,45]:
            diagnostics.append(dict(iteration=it,max_change=str(residual)))
            print('grid',N,'iteration',it,'change',str(residual),flush=True)
    assert H[0]==0 and np.min(H)>=-ld('1e-16') and np.max(H)<=1+ld('1e-16')
    assert np.min(np.diff(H))>=-ld('1e-16')
    # Seven Richardson steps for an even-power trapezoidal error expansion.
    integrand=np.zeros(N+1,dtype=ld)
    integrand[1:]=2*z[1:]*H[1:]/np.expm1(zs[1:])
    integrals=[]
    for j in range(7,-1,-1):
        stride=2**j;values=integrand[::stride]
        integrals.append(h*stride*(values.sum()-(values[0]+values[-1])/2))
    romberg=integrals[:]
    for j in range(1,8):
        romberg=[(ld(4)**j*romberg[i+1]-romberg[i])/(ld(4)**j-1) for i in range(len(romberg)-1)]
    b=2+romberg[0]/ln2;K=2/b
    # At z=0, H(z)/z²=lambda1+lambda3*z^4+lambda5*z^8+... .
    lambdas=[H[j]/(j*h)**2 for j in [8,4,2,1]]
    for r in range(1,4):
        lambdas=[(ld(16)**r*lambdas[i+1]-lambdas[i])/(ld(16)**r-1) for i in range(len(lambdas)-1)]
    lam=lambdas[0]
    k=np.arange(1,81,dtype=ld)
    sample=evaluate(H,stencil(np.sqrt(np.logaddexp(ld(0),k*ln2))/h,N))
    S1=np.sum(ld(2)**(-k)*sample)
    # Polynomial in t=y² for G(exp(-y))/y. Chebyshev nodes avoid clustering
    # errors in the input samples; the solve itself uses80 decimal digits.
    mp.mp.dps=80;degree=16;L=ld('2.25')
    nodes=L*(1+np.cos((2*np.arange(degree+1,dtype=ld)+1)*np.arccos(ld(-1))/(2*(degree+1))))/2
    ys=np.sqrt(nodes);vals=evaluate(H,stencil(np.sqrt(ys)/h,N))/ys
    m_nodes=[mp.mpf(str(t)) for t in nodes];m_vals=mp.matrix([mp.mpf(str(t)) for t in vals])
    mat=mp.matrix([[t**j for j in range(degree+1)] for t in m_nodes])
    coef=mp.lu_solve(mat,m_vals)
    return dict(grid=N,zmax=str(zmax),tail_terms=80,iterations=45,
                floating_mantissa_bits=int(np.finfo(ld).nmant),seconds=time.monotonic()-start,
                diagnostics=diagnostics,b=str(b),two_over_b=str(K),lambda_from_boundary=str(lam),
                S1=str(S1),odd_coefficients={str(2*j+1):mp.nstr(coef[j],30) for j in range(4)},
                vallee_ratio=str(lam/b),vallee_ratio_target=str(2*ln2/np.arccos(ld(-1))**2),
                bounds_note='Floating-point interpolation and extrapolation diagnostics; not a rigorous interval certificate.')


if __name__=='__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for N in [2048,4096]:
        if str(N) in data:continue
        result=calculate(N);data[str(N)]=result
        OUT.write_text(json.dumps(data,indent=2)+'\n')
        print('grid',N,'complete',result['two_over_b'],result['S1'],flush=True)
