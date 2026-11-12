#!/usr/bin/env python3
"""New checks for 4.6.1-25/27; successful blocks are not rerun."""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import argparse
import json
import random
import time
from verify_polynomial_division import mul, pseudo, trim, primitive
from verify_subresultants import sequence

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/polynomial-c-extensions.json'


def brown_sequence(a,b):
    c = gcd(a[-1],b[-1])
    u, g, h = [a,b], c, F(0)
    hs=[]
    while True:
        delta=len(a)-len(b)
        r=pseudo(a,b)[1]
        if not r:
            break
        factor = g if h==0 else g*h**delta
        r=[F(x)/factor for x in r]
        assert all(x.denominator==1 for x in r)
        r=[x.numerator for x in r]
        h = F(b[-1])**delta/g if h==0 else h**(1-delta)*b[-1]**delta
        g=b[-1]
        hs.append(str(h))
        u.append(r)
        a,b=b,r
    return u,hs


def brown():
    rng=random.Random(2026110407)
    for _ in range(150):
        n=rng.randrange(1,6);m=rng.randrange(n+1,9);c=rng.randrange(2,6)
        a=[1]+[rng.randrange(-3,4) for _ in range(m-1)]+[2*c]
        b=[1]+[rng.randrange(-3,4) for _ in range(n-1)]+[3*c]
        ordinary=sequence(a,b)[0][1:]
        changed,hs=brown_sequence(a,b)
        assert changed[:2]==ordinary[:2]
        assert changed[2:]==[[x//c for x in v] for v in ordinary[2:]]
        assert all(x%c==0 for v in ordinary[2:] for x in v)
        assert all('/' not in x for x in hs)
    a,b=[1,1,0,2],[1,0,1,2]
    assert primitive(a)[0]==primitive(b)[0]==1
    q,r=pseudo(a,b)
    changed,hs=brown_sequence(a,b)
    assert q==[2] and r==[0,2,-2]
    assert changed[2]==[0,1,-1] and hs[0]=='1/2'
    return {'strict_degree_cases':150,'C0199':{'u':a,'v':b,'q':q,'r':r,
            'first_normalized_remainder':changed[2],'first_h':hs[0]}}


def promised_division(u,v,two_ends=False):
    shift=next(i for i,x in enumerate(v) if x)
    assert not any(u[:shift])
    u,v=u[shift:],v[shift:]
    n,d=len(v)-1,len(u)-len(v)
    q=[F(0)]*(d+1);products=0
    split=(d+2)//2 if two_ends else d+1
    for k in range(split):
        total=F(u[k])
        for i in range(1,min(n,k)+1):
            total-=v[i]*q[k-i];products+=1
        q[k]=total/v[0]
    for k in range(d,split-1,-1):
        total=F(u[n+k])
        for j in range(k+1,min(d,n+k)+1):
            total-=q[j]*v[n+k-j];products+=1
        q[k]=total/v[n]
    return trim(q),products


def exact_division():
    rng=random.Random(2026110408)
    cases=0
    for n in range(0,12):
        for d in range(0,15):
            shift=rng.randrange(0,4)
            v=[0]*shift+[rng.choice([-2,1,3])]+[rng.randrange(-4,5) for _ in range(n)]
            v[-1]=rng.choice([-3,1,2])
            q=[rng.randrange(-5,6) for _ in range(d)]+[rng.choice([-2,1,3])]
            u=mul(q,v)
            ql,cl=promised_division(u,v)
            qt,ct=promised_division(u,v,True)
            assert ql==qt==q
            assert cl==sum(min(n,k) for k in range(d+1))
            split=(d+2)//2
            assert ct==sum(min(n,k) for k in range(split))+sum(min(n,k) for k in range(d+1-split))
            assert ct<=cl
            cases+=1
    return {'constructed_exact_divisions':cases,'methods':'Low coefficients and independent two-ended triangular solves; compare with prescribed quotient.'}


def eval_mod(a,x,p):
    r=0
    for v in reversed(a):r=(r*x+v)%p
    return r


def transform_division():
    p,L,omega=257,16,pow(3,16,257)
    assert pow(omega,L,p)==1 and pow(omega,L//2,p)!=1
    rng=random.Random(2026110409);shifted=0
    for case in range(60):
        v=[rng.randrange(p) for _ in range(rng.randrange(1,8))]+[1]
        if case==0:v=[p-1,1] # The untwisted transform contains v(1)=0.
        q=[rng.randrange(p) for _ in range(rng.randrange(1,8))]+[1]
        u=mul(v,q,p)
        alpha=next(a for a in range(1,p) if all(eval_mod(v,a*pow(omega,j,p)%p,p) for j in range(L)))
        shifted+=alpha!=1
        values=[eval_mod(u,alpha*pow(omega,j,p)%p,p)*pow(eval_mod(v,alpha*pow(omega,j,p)%p,p),-1,p)%p for j in range(L)]
        got=[sum(values[j]*pow(omega,(-i*j)%(p-1),p) for j in range(L))*pow(L,-1,p)*pow(alpha,(-i)%(p-1),p)%p for i in range(L)]
        assert trim(got,p)==q
    return {'finite_field_transforms':60,'modulus':p,'length':L,'needed_nontrivial_twist':shifted}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'blocks':{}}
    for name,fn in [('brown',brown),('exact_division',exact_division),('transform_division',transform_division)]:
        if name in data['blocks']:print('REUSE',name,flush=True);continue
        start=time.perf_counter();result=fn();result['seconds']=time.perf_counter()-start
        data['blocks'][name]=result;OUT.write_text(json.dumps(data,indent=2)+'\n');print('PASS',name,result['seconds'],flush=True)
    data['status']='passed';OUT.write_text(json.dumps(data,indent=2)+'\n')


if __name__=='__main__':main()
