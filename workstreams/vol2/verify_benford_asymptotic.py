#!/usr/bin/env python3
"""Direct Cesaro arrays versus the new asymptotic; exact rational prefix checks.

The asymptotic proof is in notes/benford-asymptotic.md. Finite values corroborate
it; no finite convergence experiment is a proof of an asymptotic statement.
"""
import json
import math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import mpmath as mp
from verify_benford_math import coeffs,sm,count_formula

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/benford-asymptotic.json'
mp.mp.dps=65
L=mp.log(10)

def delta(r,j):
    y=r*10**j
    return -((-y.numerator)//y.denominator)-y

def gm(r,m,T):
    rr=mp.mpf(r.numerator)/r.denominator
    alpha=mp.log10(rr); mu=alpha-(rr-1)/9
    n=int(mp.floor(T/L))
    v=mu*T**(m-1)
    for j in range(n+1):
        d=delta(r,j); d=mp.mpf(d.numerator)/d.denominator
        v+=d*((1-alpha)*max(0,T-j*L)**(m-1)+alpha*max(0,T-(j+1)*L)**(m-1))
    return v/math.factorial(m-1)

def block(r):
    rr=mp.mpf(r.numerator)/r.denominator
    alpha=mp.log10(rr); c=(rr-1)/9; cs=coeffs(rr,6)
    Nmax=10**6
    ks=np.arange(1,Nmax+1,dtype=np.int64)
    powers=np.empty(Nmax,dtype=np.int64)
    for j in range(7):
        lo=10**j;hi=min(Nmax,10**(j+1)-1)
        if lo<=hi:powers[lo-1:hi]=lo
    p0=(ks*r.denominator < powers*r.numerator).astype(np.int64)
    exact_prefix=np.cumsum(p0)
    Ns=sorted(set(int(10**n*s) for n in range(1,6) for s in [1,1.7,2,3.1,7,10]))
    exact_checks=0
    for N in Ns:
        j=len(str(N))-1; s=F(N,10**j)
        s1=1+(r-10)/(9*s) if s<=r else 10*(r-1)/(9*s)
        true=F(int(exact_prefix[N-1]))-N*s1
        d=delta(r,j)
        formula=sum(delta(r,h) for h in range(j))-(r-1)/9+d+(1-d)*int(p0[N-1])
        assert true==formula
        assert int(exact_prefix[N-1])==count_formula(N,r)
        exact_checks+=2
    # Formula(1) against integration of the independently built step a_j.
    integral_checks=0
    for m in range(2,7):
        for n,s in [(0,mp.mpf('1.7')),(2,mp.mpf(2)),(5,mp.mpf('3.1'))]:
            T=n*L+mp.log(s); integral=mp.mpf(0);D=F(0)
            for j in range(n+1):
                d=delta(r,j)
                aj=mp.mpf(D.numerator)/D.denominator+(1-alpha)*mp.mpf(d.numerator)/d.denominator+alpha-c
                lo=j*L;hi=min(T,(j+1)*L)
                integral+=aj*((T-lo)**(m-1)-(T-hi)**(m-1))/math.factorial(m-1)
                D+=d
            assert abs(integral-gm(r,m,T))<mp.mpf('1e-54')
            integral_checks+=1
    rows=[]; a=p0.astype(np.float64)
    for m in range(1,7):
        a=np.cumsum(a)/ks
        if m==1:continue
        vals=[]
        for N in Ns:
            j=len(str(N))-1;s=mp.mpf(N)/10**j;T=mp.log(N)
            actual=mp.mpf(N)*(float(a[N-1])-sm(rr,m,s,cs))
            G=gm(r,m,T);rem=actual-G
            u=2.0**-53;gamma=N*u/(1-N*u)
            # Conservative accumulated binary64 sum/division absolute error,
            # expressed in d_m=N(Pm-Sm) units. Evaluating Sm uses65 decimals.
            fp_bound=2*m*gamma*N+1e-8
            if m==2:assert abs(rem)<20+fp_bound
            vals.append({'N':N,'actual_d_m':mp.nstr(actual,19),
                         'G_m':mp.nstr(G,19),
                         'remainder_over_log_to_m_minus_2':mp.nstr(rem/T**(m-2),19),
                         'binary64_absolute_error_bound_d_m':fp_bound,
                         'actual_over_G':mp.nstr(actual/G,19)})
        rows.append({'m':m,'samples':vals})
    return {'r':str(r),'Nmax':Nmax,'exact_rational_comparisons':exact_checks,
            'step_integral_comparisons':integral_checks,'rows':rows,
            'note':'Measured ratios and remainders are corroboration; the uniform general result is proved in notes.'}

if __name__=='__main__':
    state=json.loads(OUT.read_text()) if OUT.exists() else {'blocks':{}}
    for r in [F(2),F(6,5),F(4,3),F(314159,100000),F(999,100)]:
        if str(r) in state['blocks']:continue
        state['blocks'][str(r)]=block(r)
        OUT.write_text(json.dumps(state,indent=2)+'\n')
        print(str(r),'PASS',flush=True)
