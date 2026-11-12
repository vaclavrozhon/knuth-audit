"""Exact checks of TAOCP 4.6.2-15, with explicit randomness conventions.

Small instances use exhaustive square tables as the independent root oracle.
The shift test also compares polynomial gcd with evaluation at the two roots.
Successful blocks are saved separately and must not be repeated.
"""
from collections import Counter
from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse
import datetime
import json
import os
import time

import sympy as sp
from verify_berlekamp import Field

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / 'results/sqrt-mod-prime.json'
STATS = Counter()


def chi(a, p):
    t = pow(a % p, (p-1)//2, p)
    return -1 if t == p-1 else t


def shifts():
    examples = []
    for p in map(int, sp.primerange(3, 102)):
        f = Field(p)
        squares = {a*a % p for a in range(1, p)}
        for u in sorted(squares):
            a = next(a for a in range(1, p) if a*a % p == u)
            poly = f.poly([-u, 0, 1])
            count = 0
            for s in range(p):
                g = f.gcd(poly, f.sub(f.power((s, 1), (p-1)//2, poly), (1,)))
                expected_degree = int((s+a) % p in squares)+int((s-a) % p in squares)
                assert len(g)-1 == expected_degree
                count += len(g) == 2
                STATS['shift_gcds'] += 1
            expected = (p+1+chi(2*a, p)+chi(-2*a, p))//2
            assert count == expected
            assert count in {(p-1)//2, (p+1)//2, (p+3)//2}
            if p == 5:
                examples.append({'p':p,'u':u,'successes':count,'total':p})
            STATS['shift_distributions'] += 1
    # The 2001 erratum writes s*x+t, but its following count is for x+s.
    affine = []
    for p, u, t in [(5, 1, 0), (7, 1, 3)]:
        f = Field(p)
        poly = f.poly([-u, 0, 1])
        success = []
        for s in range(p):
            g = f.gcd(poly, f.sub(f.power(f.poly([t, s]), (p-1)//2, poly), (1,)))
            if len(g) == 2:
                success.append(s)
        assert len(success) < (p-1)//2
        affine.append({'p':p,'u':u,'t':t,'successful_s':success})
    f = Field(5)
    assert f.gcd((4, 0, 1), f.sub(f.power((0, 1), 2, (4, 0, 1)), (1,))) == (4, 0, 1)
    return {'shift_examples':examples,'erratum_affine_counterexamples':affine,
            'first_gcd_counterexample':{'p':5,'u':1,'gcd':[4,0,1]}}


def shanks(u, p, nonresidue):
    q, e = p-1, 0
    while q % 2 == 0:
        q //= 2
        e += 1
    assert q % 2 and chi(nonresidue, p) == -1
    y, r = pow(nonresidue, q, p), e
    x = pow(u, (q-1)//2, p)
    v, w = u*x % p, u*x*x % p
    cost, first = 0, True
    while True:
        assert u*w % p == v*v % p
        assert pow(y, 2**(r-1), p) == p-1
        assert pow(w, 2**r, p) == 1
        strong = pow(w, 2**(r-1), p) == 1
        assert strong == (chi(u, p) == 1) if first else strong
        STATS['shanks_invariant_states'] += 1
        if w == 1:
            return v, cost
        start = cost
        k, t = 0, w
        while t != 1:
            t = t*t % p
            k += 1
            cost += 1
        if k == r:
            assert first and chi(u, p) == -1
            return None, cost
        b = y
        for _ in range(r-k-1):
            b = b*b % p
            cost += 1
        v = v*b % p
        y = b*b % p
        w = w*y % p
        cost += 3
        assert cost-start == r+2
        r = k
        first = False


def algorithms():
    for p in map(int, sp.primerange(3, 1000)):
        roots = {}
        for a in range(p):
            roots.setdefault(a*a % p, set()).add(a)
        for u in range(1, p):
            if p % 4 == 3 and u in roots:
                a = pow(u, (p+1)//4, p)
                assert a in roots[u]
                STATS['direct_3_mod_4'] += 1
            if p % 8 == 5 and u in roots:
                v = pow(2*u, (p-5)//8, p)
                i = 2*u*v*v % p
                a = u*v*(i-1) % p
                assert i*i % p == p-1 and a in roots[u]
                STATS['atkin_5_mod_8'] += 1
            if p % 8 == 1:
                ns = [a for a in range(2, p) if a not in roots]
                for nr in (ns if p < 100 else ns[:2]):
                    a, cost = shanks(u, p, nr)
                    assert (a in roots.get(u, set())) if a is not None else (u not in roots)
                    e = (p-1 & -(p-1)).bit_length()-1
                    assert cost < comb(e+3, 2)
                    STATS['shanks_instances'] += 1
        nr_count = sum(a not in roots for a in range(2, p))
        assert nr_count == (p-1)//2
        assert F(p-2, nr_count) == 2-F(2, p-1) < 2
        STATS['nonresidue_trial_means'] += 1
    assert pow(3, 8, 17) == 16  # printed stronger invariant fails initially.


def cipolla():
    for p in map(int, sp.primerange(3, 102)):
        squares = {a*a % p for a in range(1, p)}
        for u in sorted(squares):
            good = [a for a in range(p) if (a*a-u) % p not in squares | {0}]
            assert len(good) == (p-1)//2
            for a in good:
                d = (a*a-u) % p
                # Independent pair arithmetic: (A+B*t), where t^2=d.
                def mul(v, w):
                    return ((v[0]*w[0]+d*v[1]*w[1]) % p,
                            (v[0]*w[1]+v[1]*w[0]) % p)
                v, base, exponent = (1, 0), (a, 1), (p+1)//2
                while exponent:
                    if exponent & 1:
                        v = mul(v, base)
                    base = mul(base, base)
                    exponent //= 2
                assert v[1] == 0 and v[0]*v[0] % p == u
                STATS['cipolla_instances'] += 1
            STATS['cipolla_trial_distributions'] += 1


def average():
    # Separate cyclic-group model: exponents replace modular multiplication.
    # z is fixed of order 2^e; initial w=z^(2a), a uniform modulo 2^(e-1).
    results = []
    for e in range(2, 15):
        costs = []
        for a in range(2**(e-1)):
            r, b, cost = e, 2*a, 0
            while b:
                k = r-(b & -b).bit_length()+1
                assert 1 <= k < r
                cost += r+2
                b = (b//2**(r-k)+1) % (2**k)
                r = k
            costs.append(cost)
        mean = F(sum(costs), len(costs))
        assert mean == F(e*e+7*e-12, 4)+F(1, 2**(e-1))
        assert max(costs) == F(e*e+5*e-6, 2)
        assert mean < F(comb(e+4, 2), 2)
        results.append({'e':e,'inputs':len(costs),'max':max(costs),'mean':str(mean)})
        STATS['cyclic_states'] += len(costs)
    return {'exact_cost_distributions':results}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('block', choices=['shifts','algorithms','cipolla','average'])
    args = parser.parse_args()
    old = json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert args.block not in old['blocks'], 'Successful block already stored.'
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    start = time.monotonic()
    extra = globals()[args.block]() or {}
    result = {'status':'passed','started_at_utc':started,'pid':os.getpid(),
              'elapsed_seconds':time.monotonic()-start,'stats':dict(STATS),**extra}
    old['blocks'][args.block] = result
    RESULT.write_text(json.dumps(old,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='exact_cost_distributions'}),flush=True)


if __name__ == '__main__':
    main()
