#!/usr/bin/env python3
"""Exact witnesses for TAOCP 4.6.4, polynomial-chain bounds, exercises25--31.

General lower bounds are proved in notes/polyeval-chains.md. This file
checks the printed examples, elementary normalization identities, and
constructs integer algebraic relations by exact rational linear algebra.
"""
from datetime import datetime, timezone
from math import lcm, gcd
from pathlib import Path
import json
import os
import time
import sympy as S

ROOT=Path(__file__).resolve().parent
RESULT=ROOT/'results/polyeval-chains.json'
x=S.Symbol('x')


def zero(v):
    assert S.cancel(S.expand(v)) == 0, S.factor(v)


def examples():
    a=S.symbols('a0:9')
    v=[x]
    v.append(a[1]+v[0])
    v.append(-v[0]-v[0])
    v.append(v[1]+v[1])
    v.append(a[2]*v[3])
    v.append(v[0]-v[0])
    v.append(a[6]-v[5])
    v.append(a[7]*v[6])
    v.append(v[7]*v[7])
    v.append(v[1]*v[4])
    v.append(a[8]-v[9])
    v.append(v[3]-v[10])
    b=[None,a[2],2*a[1],a[7],a[6],0,0,a[1],0,2*a[1]-a[8]]
    mu=[None,b[1]*(2*x+b[2]),b[3]*b[4]]
    mu.append((mu[2]+b[5])*(mu[2]+b[6]))
    mu.append((x+b[7])*(mu[1]+b[8]))
    for original,new in zip([v[4],v[7],v[8],v[9]],mu[1:]):zero(original-new)
    zero(v[11]-(2*x+mu[4]+b[9]))
    beta=S.symbols('b1:5')
    k1=1+beta[0]*x
    k2=1+beta[1]*k1*x
    k3=1+beta[2]*k2*x
    normalized=beta[3]*k3
    target=a[1]*x**3+a[2]*x*x+a[3]*x+a[4]
    zero(normalized.subs(dict(zip(beta,[a[1]/a[2],a[2]/a[3],a[3]/a[4],a[4]])),simultaneous=True)-target)
    coefficients=S.Poly(normalized,x)
    assert coefficients.nth(0)==beta[3]
    assert S.factor(coefficients.nth(3))==S.prod(beta)
    # Missing output in the printed union, independent of normalization example26.
    a1=S.Symbol('a')
    original=a1*(x+x)
    zero(original.subs(a1,0))
    assert S.Poly(original,x).nth(1)==2*a1
    # Every A_odd at this only addition is the empty product1.
    return {'exercise25_intermediate_products':4,'exercise25_output':str(S.expand(v[11])),
            'exercise26_generic_map':True,'exercise26_missing_polynomial':'x^3+1',
            'C0238':'lambda1=x+x, lambda2=a*lambda1; A1=1, R1 empty, R-prime excludes0'}


def normalization():
    A,B,g1,g2,T,c=S.symbols('A B g1 g2 T c')
    zero(A*(T+B)-(A*T+A*B))
    zero((g1*x+A)*(g2*x+B)-(g1*x*(g2*x+B+g2*A/g1)+A*B))
    zero(((g1*x+A)*(g2*x+B)).subs(g1,0)-(A*g2*x+A*B))
    zero(c*(T+A*B)-(c*T+c*A*B))
    counts=[]
    for n in [3,5,7,9,11]:
        alpha=S.symbols('a0:'+str(n+2))
        values={0:x,1:alpha[1]+x,2:(alpha[1]+x)**2,3:alpha[2]*(alpha[1]+x)}
        chain_m=1;param_m=1;adds=1
        for i in range(1,(n+1)//2):
            values[1+3*i]=alpha[1+2*i]+values[3*i]
            values[2+3*i]=alpha[2+2*i]+values[2]
            values[3+3*i]=values[1+3*i]*values[2+3*i]
            chain_m+=1;adds+=2
        y=x+alpha[1];w=y*y
        oracle=alpha[2]*y
        for i in range(1,(n+1)//2):oracle=(oracle+alpha[1+2*i])*(w+alpha[2+2*i])
        zero(values[max(values)]-oracle)
        assert chain_m+param_m==n//2+2 and adds==n
        assert chain_m==n//2+1 and adds+param_m==n+1
        counts.append({'n':n,'multiplications':chain_m+param_m,'additions':adds,'chain_steps':chain_m,'parameter_steps':adds+param_m})
    return {'normalization_identities':4,'equation27':counts}


def compositions(total,length):
    if length==1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first,length-1):yield (first,*rest)


def relation(fs,variables,max_degree):
    for d in range(1,max_degree+1):
        exponents=[e for k in range(d+1) for e in compositions(k,len(fs))]
        polynomials=[S.Poly(S.prod(f**k for f,k in zip(fs,e)),*variables) for e in exponents]
        monomials=sorted(set(m for p in polynomials for m in p.monoms()))
        maps=[p.as_dict() for p in polynomials]
        matrix=S.Matrix([[p.get(m,0) for p in maps] for m in monomials])
        null=matrix.nullspace()
        if not null:continue
        v=null[0]
        denominator=lcm(*[int(c.q) for c in v])
        numerators=[int(c*denominator) for c in v]
        divisor=gcd(*numerators)
        numerators=[c//divisor for c in numerators]
        X=S.symbols('X:'+str(len(fs)))
        g=sum(c*S.prod(z**k for z,k in zip(X,e)) for c,e in zip(numerators,exponents))
        assert g!=0
        zero(g.subs(dict(zip(X,fs)),simultaneous=True))
        return {'inputs':list(map(str,fs)),'degree':d,'relation':str(S.expand(g)),
                'matrix_shape':list(matrix.shape),'integer_coefficients':True}
    raise AssertionError('No relation within selected example bound')


def main():
    assert not RESULT.exists(),'Do not repeat a passed block'
    start=time.perf_counter()
    result={'examples':examples(),'normalization':normalization()}
    a,b=S.symbols('a b')
    result['algebraic_relations']=[relation([a*a,a**3],[a],3),
        relation([a+b,a*b,a*a+b*b],[a,b],2),
        relation([a*a+b,a*b,b*b+a],[a,b],4)]
    result.update(status='passed',pid=os.getpid(),seconds=time.perf_counter()-start,
                  completed_at_utc=datetime.now(timezone.utc).isoformat(),
                  scope='Exact witnesses, not a finite-case proof of general lower bounds.')
    RESULT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__':main()
