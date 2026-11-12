"""Exact independent checks for TAOCP 4.6.2-21.

Sparse coefficient sums are compared with symbolic polynomial products and
real Gaussian moments. Numerical gamma values are illustrations only; the
general inequalities are proved in notes/bombieri.md.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from math import factorial, comb, prod
from pathlib import Path
import argparse
import datetime
import json
import os
import random
import time

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / 'results/bombieri.json'
STATS = Counter()


def fact(a):
    return prod(factorial(x) for x in a)


def indices(t, n):
    if t == 1:
        return [(n,)]
    return [(j,)+q for j in range(n+1) for q in indices(t-1, n-j)]


def convolution(a, b):
    out = defaultdict(lambda: sp.S.Zero)
    for j, v in a.items():
        for k, w in b.items():
            key = tuple(x+y for x, y in zip(j, k))
            out[key] += v*w
    return {j: sp.expand(v) for j, v in out.items() if sp.expand(v) != 0}


def B(a):
    return sp.expand(sum(fact(j)*v*sp.conjugate(v) for j, v in a.items()))


def norm2(a, n):
    return B(a)/factorial(n)


def expression(a, xs):
    return sp.expand(sum(v*prod(x**k for x, k in zip(xs, j)) for j, v in a.items()))


def random_poly(rng, t, n, complex_coefficients=False):
    a = {j: sp.Integer(rng.randrange(-3, 4)) +
         (sp.I*rng.randrange(-2, 3) if complex_coefficients else 0)
         for j in indices(t, n)}
    if not any(a.values()):
        a[next(iter(a))] = sp.S.One
    return {j: v for j, v in a.items() if v != 0}


def inner_sums(a, b):
    out = defaultdict(lambda: sp.S.Zero)
    for p, av in a.items():
        for q, bv in b.items():
            for j in product(*(range(x+1) for x in p)):
                k = tuple(y-x+z for x, y, z in zip(p, q, j))
                if min(k) < 0:
                    continue
                diff = tuple(x-z for x, z in zip(p, j))
                out[j, k] += av*bv*(fact(p)*fact(q)//fact(diff))
    return out


def identity():
    # Independent monomial coefficient computation, including zero coefficients.
    for p, q, r, s in product(range(7), repeat=4):
        left = Fraction(0)
        for j in range(min(p, r)+1):
            k = q-p+j
            if k >= 0 and r-j == s-k:
                left += Fraction(factorial(p)*factorial(q)*factorial(r)*factorial(s),
                                 factorial(j)*factorial(k)*factorial(p-j)*factorial(r-j))
        right = factorial(p+s) if p+s == q+r else 0
        assert left == right, (p, q, r, s)
        STATS['monomial_coefficients'] += 1
    rng = random.Random(45821)
    for t in [1, 2, 3]:
        for _ in range(12):
            # Nonhomogeneous, real signed inputs test all four independent arrays.
            polys = []
            for k in range(4):
                a = {}
                for n in range(3):
                    a.update(random_poly(rng, t, n))
                polys.append(a)
            a, b, c, d = polys
            ab, cd = inner_sums(a, b), inner_sums(c, d)
            left = sum(v*cd.get((j,k), 0)/sp.Integer(fact(j)*fact(k))
                       for (j,k), v in ab.items())
            ad, bc = convolution(a, d), convolution(b, c)
            right = sum(fact(j)*v*bc.get(j, 0) for j,v in ad.items())
            assert sp.expand(left-right) == 0
            STATS['four_polynomial_identities'] += 1
    return {}


def norms():
    rng = random.Random(68321)
    for t in [1, 2, 3]:
        xs = sp.symbols('z:'+str(t))
        for m in range(4):
            for n in range(4):
                a = random_poly(rng, t, m, True)
                b = random_poly(rng, t, n, True)
                c = convolution(a, b)
                assert expression(c,xs) == sp.expand(expression(a,xs)*expression(b,xs))
                assert B(c) >= B(a)*B(b)
                assert norm2(c,m+n) <= norm2(a,m)*norm2(b,n)
                # The full nonnegative expansion proves the lower inequality.
                terms = inner_sums(a, {j:sp.conjugate(v) for j,v in b.items()})
                total = sum(sp.expand(v*sp.conjugate(v))/sp.Integer(fact(j)*fact(k))
                            for (j,k),v in terms.items())
                assert sp.expand(total-B(c)) == 0
                STATS['complex_product_inequalities'] += 1
    assert norm2({(3,0):sp.Integer(4),(1,2):sp.Integer(1),(0,3):sp.Integer(-2)},3)==sp.Rational(61,3)
    assert norm2({(1,3,0,0):sp.Integer(3),(0,0,2,2):sp.Integer(-1)},4)==sp.Rational(29,12)
    for n in range(1,81):
        left = sum(Fraction(comb(n,k)**2,comb(2*n,2*k)) for k in range(n+1))
        assert left == Fraction(4**n,comb(2*n,n))
        assert sum(comb(n,k) for k in range(n+1)) == 2**n
        STATS['central_binomial_norms'] += 1
    return {'printed_norm_squares':['61/3','29/12'],
            'known_2005_correction':'[(x-1)^n]^2=[(x+1)^n]^2=2^n'}


def gaussian():
    rng = random.Random(68421)
    for t in [1,2,3]:
        xs = sp.symbols('x:'+str(t), real=True)
        ys = sp.symbols('y:'+str(t), real=True)
        for n in range(4):
            a = random_poly(rng,t,n,True)
            u = expression(a,[x+sp.I*y for x,y in zip(xs,ys)])
            integrand = sp.Poly(sp.expand(u*sp.conjugate(u)),*xs,*ys)
            # Independent Cartesian moments, divided by pi^t.
            integral = sp.S.Zero
            for powers, coefficient in integrand.terms():
                if any(k%2 for k in powers):
                    continue
                moment = prod(sp.Rational(factorial(k),4**(k//2)*factorial(k//2)) for k in powers)
                integral += coefficient*moment
            assert sp.expand(integral-B(a)) == 0
            STATS['cartesian_gaussian_integrals'] += 1
            # Explicit words give a second model of the normalized norm.
            words = sum(sp.expand(a.get(tuple(w.count(i) for i in range(t)),0)*
                         sp.conjugate(a.get(tuple(w.count(i) for i in range(t)),0)))*
                        sp.Rational(fact(tuple(w.count(i) for i in range(t))),factorial(n))**2
                        for w in product(range(t),repeat=n))
            assert sp.expand(words-norm2(a,n)) == 0
            STATS['noncommutative_word_norms'] += 1
    # u(z)=z^2 in one complex variable: integral=2*pi, [u]^2=1.
    assert sp.integrate(2*sp.pi*sp.Symbol('r',nonnegative=True)**5*
                        sp.exp(-sp.Symbol('r',nonnegative=True)**2),
                        (sp.Symbol('r',nonnegative=True),0,sp.oo)) == 2*sp.pi
    return {'counterexample':{'variables':1,'degree':2,'polynomial':'z^2',
                             'integral':'2*pi','norm_squared':'1','printed_rhs':'1/pi'}}


def bounds():
    rng = random.Random(458214)
    for t in [1,2,3,4]:
        for n in range(13):
            q,r = divmod(n,t)
            beta = factorial(q)**(t-r)*factorial(q+1)**r
            assert beta == min(fact(j) for j in indices(t,n))
            STATS['minimum_factorial_products'] += 1
        for m in range(1,4):
            for k in range(1,4):
                a,b = random_poly(rng,t,m),random_poly(rng,t,k)
                c=convolution(a,b)
                betaa=min(fact(j) for j in indices(t,m))
                betab=min(fact(j) for j in indices(t,k))
                ha,hb=max(abs(v) for v in a.values()),max(abs(v) for v in b.values())
                assert min(ha,hb)**4*betaa*betab <= B(c)
                STATS['factor_height_bounds'] += 1
    for n in range(1,13):
        for _ in range(5):
            a={(0,):sp.Integer(rng.choice([1,2,-3]))}
            ma2=abs(next(iter(a.values())))**2
            for j in range(n):
                root=sp.Integer(rng.randrange(-2,3))+sp.I*rng.randrange(-2,3)
                a=convolution(a,{(0,):-root,(1,):sp.S.One})
                ma2*=max(1,sp.expand(root*sp.conjugate(root)))
            aa={(j[0],n-j[0]):v for j,v in a.items()}
            b=norm2(aa,n)
            assert ma2 <= 2**n*b and b <= 2**n*ma2
            STATS['mahler_comparisons'] += 1
    mp.mp.dps=60
    ct=2**(mp.mpf(1)/8)*mp.pi**(-mp.mpf(3)/8)*2**mp.mpf('0.5')
    ratios=[]
    for n in [100,1000,10000]:
        exact=mp.factorial(n)**mp.mpf('.25')/mp.gamma(1+mp.mpf(n)/4)
        leading=ct*2**(mp.mpf(n)/2)*mp.mpf(n)**(-mp.mpf(3)/8)
        ratios.append({'n':n,'ratio':mp.nstr(exact/leading,35)})
    return {'c2':mp.nstr(ct,40),'stirling_ratio_illustrations':ratios}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('block',choices=['identity','norms','gaussian','bounds'])
    args=parser.parse_args();data=json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert args.block not in data['blocks'], 'Do not repeat successful checkpoints'
    start=datetime.datetime.now(datetime.timezone.utc).isoformat();tic=time.monotonic()
    extra=globals()[args.block]()
    data['blocks'][args.block]=dict(status='passed',started_at_utc=start,pid=os.getpid(),
                                  elapsed_seconds=time.monotonic()-tic,stats=dict(STATS),**extra)
    RESULT.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data['blocks'][args.block]))


if __name__=='__main__':main()
