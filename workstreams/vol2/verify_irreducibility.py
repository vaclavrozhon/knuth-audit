"""Exact certificates for 4.6.2-38/39 and finite height-ratio examples for41.

Numerical embeddings only guide the search for t. Acceptance always uses exact
integer matrices, resultants, divisibility and Perron's integer inequalities.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import argparse
import datetime
import json
import os
import random
import time

import sympy as sp
from verify_berlekamp import Field

ROOT=Path(__file__).resolve().parent
RESULT=ROOT/'results/irreducibility.json'
X,Y=sp.symbols('x y')
STATS=Counter()


def perron_type(poly):
    a=poly.all_coeffs()
    if a[0]!=1 or a[-1]==0:return 0
    if abs(a[1])>1+sum(abs(c) for c in a[2:]):return 1
    if len(a)>=3 and a[1]==0 and a[2]>1+sum(abs(c) for c in a[3:]):return 2
    return 0


def perron():
    rng=random.Random(46038)
    for n in range(2,11):
        for kind in [1,2]:
            for j in range(12):
                tail=[rng.randrange(-4,5) for _ in range(n-kind)]
                if tail and not tail[-1]:tail[-1]=1
                dominant=2+sum(abs(c) for c in tail)+rng.randrange(4)
                if kind==1 and j%2:dominant=-dominant
                coeffs=[1]+([dominant] if kind==1 else [0,dominant])+tail
                u=sp.Poly.from_list(coeffs,X)
                assert perron_type(u)==kind and u.is_irreducible
                STATS['perron_polynomials']+=1
    r=Fraction(-1,2)
    actual=abs(1+4*r*r+r**3)
    printed=1+4*r*r-r**3
    corrected=1+4*r*r-abs(r)**3
    assert (actual,printed,corrected)==(Fraction(15,8),Fraction(17,8),Fraction(15,8))
    assert actual<printed
    return {'C0219':{'u':'x^3+4x+1','r':'-1/2','actual':str(actual),'printed_lower_bound':str(printed),'corrected_lower_bound':str(corrected)}}


def matrix_image(u,t):
    n=u.degree();columns=[]
    for j in range(n):
        rem=sp.rem(t*X**j,u.as_expr(),X)
        columns.append([sp.expand(rem).coeff(X,i) for i in range(n)])
    return sp.Matrix(n,n,lambda i,j:columns[j][i])


def transformed(u,t):
    matrix=matrix_image(u,t)
    v=sp.Poly(matrix.charpoly(Y).as_expr(),Y,domain=sp.ZZ)
    sylvester=sp.Poly(sp.resultant(u.as_expr(),Y-t,X),Y,domain=sp.ZZ)
    assert v==sylvester
    assert sp.rem(v.as_expr().subs(Y,t),u.as_expr(),X)==0
    STATS['exact_resultant_certificates']+=1
    return v


def find_certificate(u):
    n=u.degree()
    roots=[complex(a) for a in sp.nroots(u,maxsteps=300)]
    real=sorted([a.real for a in roots if abs(a.imag)<1e-10])
    upper=sorted([a for a in roots if a.imag>1e-10],key=lambda a:(a.real,a.imag))
    assert len(real)+2*len(upper)==n
    forms=[lambda i,a=a:a**i for a in real]
    forms += [lambda i,a=a:(a**i).real for a in upper]
    forms += [lambda i,a=a:(a**i).imag for a in upper]
    forms=forms[:-1]
    for scale in [10**5,10**8,10**11]:
        lattice=sp.Matrix([[int(i==j) for j in range(n)]+[round(scale*f(i)) for f in forms] for i in range(n)])
        reduced=lattice.lll()
        for row in reduced.tolist():
            t=sum(row[i]*X**i for i in range(n))
            if not t:continue
            v=transformed(u,t)
            if perron_type(v):
                return {'u':str(u.as_expr()),'t_coefficients':[int(row[i]) for i in range(n)],
                        'v_coefficients':[int(c) for c in v.all_coeffs()],
                        'perron_type':perron_type(v),'heuristic_scale':scale}
    raise AssertionError('Bounded heuristic certificate search found none')


def certificates():
    examples=[X**3-2,X**3-X-1,X**4+X+1,X**4-10*X**2+1,
              X**4+1,X**5-X-1,X**6+3*X+1]
    rows=[]
    for expression in examples:
        u=sp.Poly(expression,X,domain=sp.ZZ);assert u.is_irreducible
        rows.append(find_certificate(u));STATS['accepted_certificates']+=1
    # The general resultant formula also has a leading coefficient factor.
    for a in [2,3,-2]:
        u=sp.Poly(a*X**3+X+1,X);t=X**2+2*X+1
        res=sp.Poly(sp.resultant(u.as_expr(),Y-t,X),Y)
        assert res.LC()==a**sp.degree(t,X)
        STATS['nonmonic_resultants']+=1
    return {'certificates':rows}


def modular_irreducibility(poly):
    n=poly.degree()
    for p in list(sp.primerange(2,300)):
        if int(poly.LC())%p==0:continue
        f=Field(p);u=f.poly(reversed([int(c) for c in poly.all_coeffs()]))
        u=f.poly(f.ratio(c,u[-1]) for c in u)
        x=f.poly((0,1));h=x;good=True;checks=[]
        for i in range(1,n+1):
            h=f.power(h,p,u)
            if i in [n//q for q in sp.factorint(n)]:
                d=f.gcd(f.sub(h,x),u);checks.append(i)
                if d!=f.one:good=False;break
        if good and f.sub(h,x)==():
            return {'prime':p,'degree':n,'gcd_indices':checks,'frobenius_identity':True}
    return None


def height(poly):return max(abs(int(c)) for c in poly.all_coeffs())


def factor_height():
    boyd=sp.Poly(2*X**4+4*X**3+5*X**2+4*X+2,X)
    abbotts=[
        [1,1,0,-1,-1,-1,0,2,3,2,1],
        [1,2,3,2,0,-1,-1,-1,0,1,1],
        [29,175,543,1119,1683,1921,1683,1119,543,175,29],
        [6,33,93,175,243,249,158,-26,-248,-427,-495,-427,-248,-26,158,249,243,175,93,33,6]
    ]
    rows=[]
    for g in [boyd]+[sp.Poly.from_list(a,X,domain=sp.ZZ) for a in abbotts]:
        partner=sp.Poly(sp.expand(X**g.degree()*g.as_expr().subs(X,-1/X)),X);product=g*partner
        assert g.is_irreducible and partner.is_irreducible
        cert=modular_irreducibility(g)
        # Some number-field Galois groups have no full cycle: a single prime
        # certificate need not exist; exact factor_list remains the oracle.
        ratio=Fraction(height(g),height(product))
        rows.append({'g_coefficients':[int(c) for c in g.all_coeffs()],
                     'product_coefficients':[int(c) for c in product.all_coeffs()],
                     'ratio':str(ratio),'modular_certificate':cert})
        STATS['irreducible_pairs']+=1
        if cert:STATS['independent_modular_certificates']+=1
    assert rows[0]['ratio']=='5/4'
    assert sp.expand(boyd.as_expr()*boyd.as_expr().subs(X,-X))==4*X**8+4*X**6+X**4+4*X**2+4
    assert rows[1]['ratio']=='3' and rows[2]['ratio']=='3'
    assert rows[4]['ratio']=='55/4'
    return {'examples':rows,'unbounded_irreducible_ratio_proved':False}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('block',choices=['perron','certificates','factor_height'])
    args=parser.parse_args();data=json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert args.block not in data['blocks'],'Do not repeat successful checkpoints'
    start=datetime.datetime.now(datetime.timezone.utc).isoformat();tic=time.monotonic();extra=globals()[args.block]()
    data['blocks'][args.block]=dict(status='passed',started_at_utc=start,pid=os.getpid(),elapsed_seconds=time.monotonic()-tic,stats=dict(STATS),**extra)
    RESULT.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data['blocks'][args.block]))


if __name__=='__main__':main()
