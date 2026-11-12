#!/usr/bin/env python3
"""Exact finite checks for TAOCP4.7-29, added2024; proof is in the note."""
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import permutations, product
from math import factorial
from pathlib import Path
import json,time

BASE=Path(__file__).resolve().parent
RESULT=BASE/'results/series-determinant.json'

def determinant(a):
    n=len(a)
    if n<=4:
        result=F(0)
        for perm in permutations(range(n)):
            term=F((-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n)))
            for i in range(n):term*=a[i][perm[i]]
            result+=term
        return result
    a=[[F(x) for x in row] for row in a];answer=F(1)
    for i in range(n):
        pivot=next((j for j in range(i,n) if a[j][i]),None)
        if pivot is None:return F(0)
        if pivot!=i:a[pivot],a[i]=a[i],a[pivot];answer=-answer
        x=a[i][i];answer*=x
        for j in range(i+1,n):
            scale=a[j][i]/x
            for k in range(i+1,n):a[j][k]-=scale*a[i][k]
    return answer

def mul(a,b,n):
    c=[F(0)]*n
    for i,x in enumerate(a[:n]):
        for j,y in enumerate(b[:n-i]):c[i+j]+=x*y
    return c

def coefficients(a,p,q,r,s):
    n=len(a);rp=[F(1)]+[F(0)]*(n-1);sp=rp[:];left=[];right=[]
    for k in range(n):
        left.append([F(0)]*k+mul(p,rp,n-k))
        right.append([F(0)]*k+mul(q,sp,n-k))
        rp=mul(rp,r,n);sp=mul(sp,s,n)
    return [[sum(a[i][j]*left[i][m]*right[j][l] for i in range(n) for j in range(n))
             for l in range(n)] for m in range(n)]

def main():
    assert not RESULT.exists(),'Do not repeat a completed block'
    start=time.perf_counter();checks=0;zero_constants=0
    for constants in product([-2,0,1,2],repeat=4):
        p0,q0,r0,s0=constants
        for n in range(1,5):
            a=[[F((i+2)*(j+3)%7-2)+F(i==j) for j in range(n)] for i in range(n)]
            p=[p0,1,-2,3];q=[q0,-2,3,1];r=[r0,2,1,-1];s=[s0,1,-1,2]
            t=coefficients(a,p,q,r,s)
            expected=p0**n*q0**n*r0**(n*(n-1)//2)*s0**(n*(n-1)//2)*determinant(a)
            assert determinant(t)==expected,(constants,n)
            checks+=1;zero_constants+=int(0 in constants)
    assert determinant([[1]])==1
    counterexample={'n':1,'A':'1','p':1,'q':1,'r':2,'s':2,'actual_det':1,'printed_rhs':4,'corrected_rhs':1}
    # Compute b) directly from (exp(-w)+exp(-z)-1)*A=1.
    # This uses neither the logarithmic substitution nor triangular factors.
    size=12;a=[[F(0) for _ in range(size)] for _ in range(size)];a[0][0]=F(1)
    for m in range(size):
        for n in range(size):
            if m==n==0:continue
            a[m][n]=-sum(F((-1)**i,factorial(i))*a[m-i][n] for i in range(1,m+1))-sum(F((-1)**j,factorial(j))*a[m][n-j] for j in range(1,n+1))
    dets=[]
    for n in range(1,size+1):
        d=determinant([row[:n] for row in a[:n]]);assert d==1;dets.append(str(d))
    result={'status':'passed','seconds':time.perf_counter()-start,'transformation_cases':checks,'cases_with_zero_constant':zero_constants,'sizes':[1,2,3,4],'counterexample':counterexample,'part_b_direct_coefficient_determinants':dets,'part_b_first4matrix':[[str(x) for x in row[:4]] for row in a[:4]],'scope':'Finite exact checks supplement the general triangular-factor proof; b coefficients derived independently from denominator recurrence.','completed_at_utc':datetime.now(timezone.utc).isoformat()}
    RESULT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result),flush=True)

if __name__=='__main__':main()
