"""Exact checks of integer polynomial lifting, reconstruction and bounds.

Arithmetic helpers from earlier blocks are imported without running their tests.
Independent oracles: exhaustive lift enumeration, SymPy factorization/gcd and
resultants, bounded fractions, and direct subset enumeration.
"""
from collections import Counter
from fractions import Fraction
from itertools import product, combinations
from math import comb, gcd, isqrt, lcm
from pathlib import Path
import argparse
import datetime
import json
import os
import random
import time
import warnings

import sympy as sp
from sympy.utilities.exceptions import SymPyDeprecationWarning
from verify_berlekamp import Field
from verify_euclid_reconstruction import stopped

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / 'results/integer-factorization.json'
STATS = Counter()
X = sp.Symbol('x')
Z = Field(None)
BOOK = (-5, 2, 8, -3, -3, 0, 1, 0, 1)


def zp(a):
    a = tuple(a)
    assert all(Fraction(v).denominator == 1 for v in a)
    return tuple(int(v) for v in Z.poly(a))


def add(a, b):
    return zp(Z.add(a, b))


def sub(a, b):
    return zp(Z.sub(a, b))


def mul(a, b):
    return zp(Z.mul(a, b))


def scale(a, c):
    return zp(c*v for v in a)


def pp(a):
    a = zp(a)
    if not a:
        return a
    content = gcd(*a)
    if a[-1] < 0:
        content = -content
    return tuple(v//content for v in a)


def exact_div(a, b):
    q, r = Z.div(a, b)
    return zp(q) if not r and all(v.denominator == 1 for v in q) else None


def centered(a, modulus):
    return zp((v+modulus//2) % modulus-modulus//2 for v in a)


def polynomial(a, p=None):
    return sp.Poly.from_list(list(reversed(a)), X, **({'modulus':p} if p else {'domain':sp.ZZ}))


def modular_gcd(a, b, p):
    f = Field(p)
    return f.gcd(f.poly(a), f.poly(b))


def oracle_factors(a, p=None):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', SymPyDeprecationWarning)
        unit, qs = sp.factor_list(polynomial(a, p))
    result = []
    for q, e in qs:
        coeff = tuple(int(c) for c in reversed(q.all_coeffs()))
        if p:
            coeff = Field(p).poly(coeff)
        result.extend([coeff]*e)
    return int(unit), result


def bezout(v, w, modulus):
    f = Field(modulus)
    a, b, c, d = (1,), (), (), (1,)
    r, s = f.poly(v), f.poly(w)
    while s:
        q, t = f.div(r, s)
        r, s = s, t
        a, c = c, f.sub(a, f.mul(q, c))
        b, d = d, f.sub(b, f.mul(q, d))
    assert len(r) == 1
    inverse = pow(r[0], -1, modulus)
    return f.poly(inverse*x for x in a), f.poly(inverse*x for x in b)


def correction(v, w, a, b, error, modulus):
    f = Field(modulus)
    v, w = f.poly(v), f.poly(w)
    quotient, dv = f.div(f.mul(b, error), v)
    dw = f.add(f.mul(a, error), f.mul(quotient, w))
    assert len(dv) < len(v)
    # w can have a vanishing leading coefficient modulo modulus.
    assert f.sub(f.add(f.mul(w, dv), f.mul(v, dw)), error) == ()
    return dv, dw


def lift_pair(u, v, w, a, b, q, r):
    assert q % r == 0
    difference = sub(u, mul(v, w))
    assert all(c % q == 0 for c in difference)
    error = Field(r).poly(c//q for c in difference)
    dv, dw = correction(v, w, a, b, error, r)
    V, W = add(v, scale(dv, q)), add(w, scale(dw, q))
    assert V[-1] == 1 and len(V) == len(v) and len(W) == len(w)
    assert not Field(q*r).poly(sub(u, mul(V, W)))
    return V, W


def hensel():
    rng = random.Random(45022)
    for p in [2, 3]:
        f = Field(p)
        for m in [1, 2]:
            for k in [0, 1, 2]:
                for trial in range(5):
                    while True:
                        v = tuple(rng.randrange(p) for _ in range(m))+(1,)
                        w = tuple(rng.randrange(p) for _ in range(k))+(rng.randrange(1,p),)
                        if f.gcd(v, w) == (1,):
                            break
                    a, b = bezout(v, w, p)
                    q = p**(1+trial % 2)
                    error = tuple(rng.randrange(-3,4) for _ in range(m+k+1))
                    u = add(mul(v, w), scale(error, q))
                    got = lift_pair(u, v, w, a, b, q, p)
                    solutions = []
                    for digits in product(range(p), repeat=m+k+1):
                        V = add(v, scale(zp(digits[:m]), q))
                        W = add(w, scale(zp(digits[m:]), q))
                        if not Field(q*p).poly(sub(u, mul(V, W))):
                            solutions.append((V,W))
                        STATS['enumerated_lift_candidates'] += 1
                    assert solutions == [got]
                    STATS['unique_lifts'] += 1
    # Squaring the modulus, including simultaneous Bezout lifting.
    for p in [2,3,5]:
        for _ in range(12):
            while True:
                V = tuple(rng.randrange(-5,6) for _ in range(rng.randrange(1,4)))+(1,)
                W = tuple(rng.randrange(-5,6) for _ in range(rng.randrange(1,4)))+(rng.randrange(1,6),)
                if W[-1] % p and modular_gcd(V,W,p)==(1,):
                    break
            u=mul(V,W);q=p;v=Field(p).poly(V);w=Field(p).poly(W);a,b=bezout(v,w,p)
            for _ in range(3):
                v,w=lift_pair(u,v,w,a,b,q,q)
                error=scale(sub((1,),add(mul(a,v),mul(b,w))),Fraction(1,q))
                db,da=correction(v,w,a,b,Field(q).poly(error),q)
                a,b=add(a,scale(da,q)),add(b,scale(db,q))
                q*=q
                assert not Field(q).poly(sub(add(mul(a,v),mul(b,w)),(1,)))
                assert not Field(q).poly(sub(v,V)) and not Field(q).poly(sub(w,W))
                STATS['doubling_lifts']+=1
    return {'scope':'Exhaustive uniqueness and three successive modulus squarings, with Bezout updates.'}


def hensel_book():
    # Printed binary lift and its exact uniqueness inside coefficient bounds.
    v=(1,1,1);w=(1,1,0,0,1,1,1);a,b=bezout(v,w,2);q=2
    for _ in range(3):
        v,w=lift_pair(BOOK,v,w,a,b,q,2);q*=2;v=centered(v,q);w=centered(w,q)
    assert v==(-1,3,1) and w==(5,-3,4,-4,-5,-3,1)
    assert exact_div(BOOK,v) is None
    assert [c for c in range(-11,12) if c % 16 == 3]==[3]
    assert [c for c in range(-10,11) if c % 16 == 15]==[-1]
    return {'binary_lift_mod16':[v,w]}


def lift_many(u, factors, p, target):
    factors=[Field(p).poly(v) for v in factors]
    inverses=[]
    for i,v in enumerate(factors):
        w=(1,)
        for j,t in enumerate(factors):
            if i!=j:w=mul(w,t)
        _,b=bezout(v,w,p)
        inverses.append(b)
    q=p
    while q<target:
        modulus=q*p
        lead=u[-1];f=Field(modulus)
        normalized=f.poly(c*pow(lead,-1,modulus) for c in u)
        old=(1,)
        for v in factors:old=mul(old,v)
        difference=sub(normalized,old)
        assert all(c % q==0 for c in difference)
        error=Field(p).poly(c//q for c in difference)
        new=[]
        for v,b in zip(factors,inverses):
            dv=Field(p).rem(Field(p).mul(b,error),Field(p).poly(v))
            new.append(centered(add(v,scale(dv,q)),modulus))
        factors=new;q=modulus
        check=(lead,)
        for v in factors:check=mul(check,v)
        assert not Field(q).poly(sub(check,u))
        STATS['multifactor_lifts']+=1
    return q,factors


def recombine_full(u, factors, modulus):
    answer=[];d=1;factors=list(factors)
    while d<=len(factors)//2:
        found=False;r=len(factors)
        for indices in combinations(range(r),d):
            if 2*d==r and indices[0]!=0:
                continue
            v=(1,)
            for i in indices:v=mul(v,factors[i])
            v=centered(scale(v,u[-1]),modulus)
            STATS['recombination_trials']+=1
            if exact_div(scale(u,u[-1]),v) is None:
                continue
            factor=pp(v)
            quotient=exact_div(u,factor)
            assert quotient is not None
            answer.append(factor);u=quotient
            factors=[v for i,v in enumerate(factors) if i not in indices]
            found=True
            break
        if not found:
            d+=1
    if len(u)>1:
        answer.append(pp(u))
    return sorted(answer)


def recombine():
    rng=random.Random(452)
    inputs=[BOOK,(2,1,1,0,1,1),(1,101,2,1)]
    for _ in range(42):
        u=(1,)
        for _ in range(rng.randrange(2,5)):
            v=pp(tuple(rng.randrange(-4,5) for _ in range(rng.randrange(1,3)))+(rng.randrange(1,5),))
            u=mul(u,v)
        if len(u)>1 and polynomial(u).sqf_part().degree()==len(u)-1:
            inputs.append(u)
    for u in inputs:
        a=u[-1];bound=(2**(len(u)-1))*abs(a)*(isqrt(sum(c*c for c in u))+1)
        for p in [2,3,5,7,11,13,17]:
            if a % p and modular_gcd(u,Field(p).derivative(u),p)==(1,):
                break
        else:
            raise AssertionError('No test prime')
        _,factors=oracle_factors(u,p)
        modulus,lifts=lift_many(u,factors,p,2*bound+1)
        _,expected=oracle_factors(u)
        assert recombine_full(u,lifts,modulus)==sorted(expected)
        STATS['integer_factorizations']+=1
    q,lifts=lift_many(BOOK,[(3,1),(12,4,8,1),(6,4,3,2,1)],13,169)
    assert q==169 and lifts==[(-36,1),(-66,82,-18,1),(84,69,-10,54,1)]
    assert all(exact_div(BOOK,v) is None for v in [lifts[0],lifts[1],centered(mul(lifts[0],lifts[1]),169)])
    expected71=[(12,1),(25,1),(-7,-13,1),(-12,31,-16,-24,1)]
    out=(1,)
    for v in expected71:out=mul(out,v)
    assert not Field(71).poly(sub(out,BOOK))
    assert all((12*c) % 71 not in [1,5,66,70] for c in [25,-7,-12])
    # Weak bound: a rejected large factor has a valid small complementary factor.
    u=(100,101,2,1);p=41;B=20
    large=(18,1,1);small=(1,1)
    assert p>2*B and exact_div(u,small)==(100,1,1)
    assert polynomial(large,p).is_irreducible and Field(p).gcd(large,small)==(1,)
    assert not Field(p).poly(sub(mul(large,small),u))
    assert u[0] % large[0] != 0 and u[0] % small[0] == 0
    return {'lift_mod169':lifts,'weak_bound_filter_counterexample':{'u':u,'p':p,'B':B,'ordered_factors':[large,small],'rejected_constant':18,'actual_factor':small}}


def bounds():
    rng=random.Random(45720)
    for _ in range(800):
        v=tuple(rng.randrange(-5,6) for _ in range(rng.randrange(1,5)))+(rng.randrange(1,5),)
        w=tuple(rng.randrange(-5,6) for _ in range(rng.randrange(1,5)))+(rng.randrange(1,5),)
        u=mul(v,w);m=len(v)-1;norm2=sum(c*c for c in u)
        for j,c in enumerate(v):
            b1=comb(m-1,j) if j<=m-1 else 0
            b2=comb(m-1,j-1) if j>=1 else 0
            residual=abs(c)-b2*abs(u[-1])
            assert residual<=0 or residual*residual<=b1*b1*norm2
            STATS['exact_coefficient_bounds']+=1
    # Reflection norm identity for nonreal Gaussian-rational coefficients.
    for _ in range(50):
        alpha=sp.Rational(rng.randrange(-5,6),3)+sp.I*sp.Rational(rng.randrange(-5,6),2)
        w=sum((sp.Rational(rng.randrange(-3,4),2)+sp.I*sp.Rational(rng.randrange(-3,4),3))*X**j for j in range(4))
        u=sp.Poly(sp.expand((X-alpha)*w),X);v=sp.Poly(sp.expand((sp.conjugate(alpha)*X-1)*w),X)
        norm=lambda f:sp.expand(sum(c*sp.conjugate(c) for c in f.all_coeffs()))
        assert sp.simplify(norm(u)-norm(v))==0
        STATS['complex_reflection_identities']+=1
    return {'scope':'800 exact coefficient-bound inputs and50 complex reflection identities.'}


def graeffe():
    import mpmath as mp
    mp.mp.dps=80
    u=BOOK;values=[]
    for t in range(8):
        value=mp.power(sum(c*c for c in u),mp.mpf(1)/(2**(t+1)))
        values.append(mp.nstr(value,45))
        even=u[::2];odd=u[1::2]
        u=sub(mul(even,even),(0,)+mul(odd,odd))
    expected=['10.63','12.42','6.85','6.64','6.65','6.6228','6.62246','6.62246']
    for t,(value,rounded) in enumerate(zip(values,expected)):
        error=abs(mp.mpf(value)-mp.mpf(rounded))
        unit=mp.power(10,-len(rounded.split('.')[1]))
        if t==5:
            # Printed last digit is not nearest rounding. Keep as a precision
            # candidate, since no explicit rounding convention is stated.
            assert mp.floor(mp.mpf(value)*10000+mp.mpf('.5'))==66227
            assert unit/2 < error < unit
        else:
            assert error < unit/2
    # 2x-1 -> 1-4x -> 1-16x -> ... ; normalized limit is -x.
    u=(-1,2)
    for t in range(1,9):
        u=sub(mul(u[::2],u[::2]),(0,)+mul(u[1::2],u[1::2]))
        assert u==(1,-2**(2**t))
        STATS['graeffe_sign_counterexample_steps']+=1
    return {'graeffe_norm_upper_bounds':values,'printed_roundings':expected,
            'precision_candidate':'t=5: nearest rounding6.6227, printed6.6228; absolute error0.000052308438..., less than one unit in last place. No explicit rounding convention.',
            'graeffe_limit_counterexample':'u=2x-1; normalized t-th iterate=(1-2^(2^t)x)/sqrt(1+2^(2^(t+1))) -> -x.'}


def modular():
    # The discriminant is independently obtained by a resultant determinant.
    u=polynomial(BOOK);disc=int(sp.discriminant(u.as_expr(),X))
    coeff=list(reversed(BOOK));derivative=[i*BOOK[i] for i in range(1,len(BOOK))][::-1]
    n=len(BOOK)-1
    sylvester=[]
    for i in range(n-1):sylvester.append([0]*i+coeff+[0]*(n-2-i))
    for i in range(n):sylvester.append([0]*i+derivative+[0]*(n-1-i))
    assert disc==int(sp.det(sp.Matrix(sylvester)))
    primes=sorted(map(int,sp.factorint(abs(disc))))
    assert primes==[3,23,233,121702457]
    assert all(sp.isprime(p) and len(modular_gcd(BOOK,Field(p).derivative(BOOK),p))>1 for p in primes)
    v=(1,2,2)
    assert sp.discriminant(polynomial(v).as_expr(),X)==-4
    assert Field(2).poly(v)==(1,) and modular_gcd(v,Field(2).derivative(v),2)==(1,)
    v=(1,1,2,2)
    assert sp.discriminant(polynomial(v).as_expr(),X)==-72
    assert Field(2).poly(v)==(1,1) and modular_gcd(v,Field(2).derivative(v),2)==(1,)
    rng=random.Random(454)
    for _ in range(100):
        d=pp(tuple(rng.randrange(-4,5) for _ in range(rng.randrange(1,4)))+(rng.randrange(1,5),))
        a=pp(tuple(rng.randrange(-4,5) for _ in range(3))+(1,))
        b=pp(tuple(rng.randrange(-4,5) for _ in range(3))+(1,))
        u,v=mul(d,a),mul(d,b)
        expected=tuple(int(c) for c in reversed(sp.gcd(polynomial(u),polynomial(v)).all_coeffs()))
        lead=gcd(u[-1],v[-1]);degree=100;residues=();M=1;success=False
        for p in list(sp.primerange(2,102)):
            if lead % p==0:continue
            f=Field(p);q=modular_gcd(u,v,p);k=len(q)-1
            assert k>=len(expected)-1
            if k>degree:continue
            if k<degree:degree=k;residues=(0,)*(k+1);M=1;STATS['crt_degree_resets']+=1
            target=[lead*(q[j] if j<len(q) else 0) % p for j in range(k+1)]
            residues=tuple(residues[j]+M*((target[j]-residues[j])*pow(M,-1,p)%p) for j in range(k+1))
            M*=p;candidate=pp(centered(residues,M))
            STATS['modular_gcd_primes']+=1
            if candidate and exact_div(u,candidate) is not None and exact_div(v,candidate) is not None:
                assert candidate==expected;success=True;break
        assert success
        STATS['modular_gcd_inputs']+=1
    return {'book_discriminant':str(disc),'bad_primes':primes,'discriminant_degree_drop_examples':[[1,2,2],[1,1,2,2]]}


def basic():
    u=(-1,2,-3,6);n=len(u)-1;a=u[-1]
    transformed=tuple(u[j]*a**(n-1-j) for j in range(n))+(1,)
    assert transformed==(-36,12,-3,1)
    _,fs=oracle_factors(transformed);restored=(1,)
    for v in fs:
        w=pp(tuple(c*a**j for j,c in enumerate(v)));restored=mul(restored,w)
        m=len(v)-1
        assert all(v[j] % a**(m-1-j)==0 for j in range(m))
    assert restored==u
    q=(2,1,1,0,1,1)
    assert mul((1,1,1),(2,-1,0,1))==q
    assert polynomial((1,1,1)).is_irreducible and polynomial((2,-1,0,1)).is_irreducible
    for r in range(1,8):
        for ds in product(range(1,4),repeat=r):
            n=sum(ds);mask=(1<<(n//2+1))-1;bits=1
            for d in ds:bits=(bits | bits<<d)&mask
            got={i for i in range(n//2+1) if bits>>i&1}
            got|={n-i for i in got}
            expected={sum(ds[j] for j in range(r) if subset>>j&1) for subset in range(1<<r)}
            assert got==expected
            STATS['subset_degree_vectors']+=1
    # Wang reconstruction uses the already proved stopped Euclid helper.
    rng=random.Random(46040)
    for _ in range(120):
        v=pp(tuple(rng.randrange(-12,13) for _ in range(rng.randrange(1,6)))+(rng.randrange(1,13),))
        B=max(map(abs,v));p=2
        while v[-1]%p==0:p=int(sp.nextprime(p))
        M=p
        while M<=2*B*B:M*=p
        reconstructed=[]
        for c in v:
            residue=c*pow(v[-1],-1,M)%M
            if residue in [0,1]:
                value=Fraction(residue)
            else:
                pair,_=stopped(residue,M,B,B)
                assert pair is not None
                value=Fraction(pair[1],pair[0])
            assert value==Fraction(c,v[-1]);reconstructed.append(value)
            STATS['reconstructed_coefficients']+=1
        den=lcm(*(c.denominator for c in reconstructed))
        assert pp(tuple(c*den for c in reconstructed))==v
        STATS['reconstructed_polynomial_factors']+=1
    return {'exercise18_transformed':transformed,'exercise25_factors':[(1,1,1),(2,-1,0,1)]}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('block',choices=['hensel','hensel_book','recombine','bounds','graeffe','modular','basic'])
    args=parser.parse_args()
    data=json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert args.block not in data['blocks'],'Do not repeat successful checkpoints'
    started=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic()
    extra=globals()[args.block]()
    data['blocks'][args.block]=dict(status='passed',started_at_utc=started,pid=os.getpid(),
        elapsed_seconds=time.monotonic()-t,stats=dict(STATS),**extra)
    RESULT.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data['blocks'][args.block]))


if __name__=='__main__':main()
