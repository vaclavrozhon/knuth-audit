#!/usr/bin/env python3
"""Exact counterexamples and corrected weighted Euclidean inequality."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import json,os,time
ROOT=Path(__file__).resolve().parent

def sequence(u,v):
    a=[];s,t=u,v
    while t:q,r=divmod(s,t);a.append(q);s,t=t,r
    if len(a)%2:a[-1:]=[a[-1]-1,1]
    T=[(1,0,u),(0,1,v)]
    for q in a:T.append(tuple(x-q*y for x,y in zip(T[-2],T[-1])))
    assert len(a)%2==0 and T[-1]==(-v//gcd(u,v),u//gcd(u,v),0)
    assert all(x*u+y*v==z for x,y,z in T)
    return a,T

def K(a):
    s,t=1,0
    for x in a:s,t=x*s+t,s
    return s

def holds(T,weight,theta_squared,zscale=F(1)):
    for j,(x,y,z) in enumerate(T[1:],1):
        S=weight*x+z*zscale
        if j%2 and S*S<=theta_squared:return True
        if j%2==0 and S>=0 and S*S<=4*theta_squared:return True
    return False

def main():
    start=time.monotonic();print('pid',os.getpid(),flush=True)
    weights=list(map(F,['1/16','1/4','1/2','1','3/2','2','9/4','3','4','8','16']))
    pairs=products=checks=raw_fails=0
    for u in range(1,97):
        for v in range(1,97):
            d=gcd(u,v);a,T=sequence(u,v)
            for k in range(1,len(a)+1):
                actual=abs(T[k+1][0]*T[k][2]);formula=d*K(a[1:k])*K(a[k:])
                assert actual==formula<=v;products+=1
            for w in weights:
                assert holds(T,w,w*v),(u,v,w)
                assert holds(T,w,w*F(v,d),F(1,d)),(u,v,w,'normalized')
                if not holds(T,w,w*F(v,d)):raw_fails+=1
                checks+=1
            pairs+=1
    family=0
    for d in range(2,129):
        a,T=sequence(2*d,d);assert a==[1,1]
        vals=[abs(F(9,4)*x+z-(F(3,2) if j%2==0 else 0)) for j,(x,y,z) in enumerate(T[1:],1)]
        assert min(vals)>F(3,2);family+=1
    out={'status':'passed','pid':os.getpid(),'pairs':pairs,'product_certificates':products,'weighted_inputs':checks,'original_failures':raw_fails,'counterexample_family':family,'example':{'u':4,'v':2,'quotients':[1,1],'lambda':'9/4','mu':1,'theta':'3/2','absolute_residuals':['2','11/4','9/4']},'seconds':time.monotonic()-start,'scope':'Exact rational squared inequalities. Corrected theta=sqrt(lambda*mu*v) and alternatively normalized z_j/d. General proof in C0141 note.'}
    (ROOT/'results/euclid-weighted.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
