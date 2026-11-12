#!/usr/bin/env python3
"""Exact checks of TAOCP2 Algorithm P and exercise 4.5.4-22.

The exhaustive algorithm runs independently of the CRT counting formula.
All mathematical bounds use integer or rational arithmetic.
"""
from pathlib import Path
from math import gcd, isqrt, prod
from fractions import Fraction
from decimal import Decimal, localcontext
import argparse
import json
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/primality-probabilistic.json'


def factor(n):
    fs = []
    p = 2
    while p*p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            fs.append((p, e))
        p = 3 if p == 2 else p+2
    if n > 1:
        fs.append((n, 1))
    return fs


def odd_part(n):
    s = 0
    while n % 2 == 0:
        s += 1
        n //= 2
    return s, n


def algorithm_p(n, x, k, q):
    j = 0
    y = pow(x, q, n)
    while True:
        if (j == 0 and y == 1) or y == n-1:
            return True
        if j > 0 and y == 1:
            return False
        j += 1
        if j == k:
            return False
        y = y*y % n


def liar_count(n, fs):
    k, q = odd_part(n-1)
    sd = [odd_part(p-1) for p, e in fs]
    m = min(s for s, d in sd)
    assert k >= m
    t = len(fs)
    g = prod(gcd(q, d) for s, d in sd)
    b = g * (1 + sum(2**(j*t) for j in range(m)))
    phi = prod((p-1)*p**(e-1) for p, e in fs)
    exceptional = False
    if all(e == 1 for p, e in fs):
        if t == 2:
            exceptional = sorted(s for s, d in sd) == [1, 2] and sd[0][1] == sd[1][1]
        elif t == 3:
            exceptional = all(s == 1 for s, d in sd) and all((n-1) % (p-1) == 0 for p, e in fs)
    return b, phi, exceptional


def exhaustive():
    cases = primes = composites = exceptional_count = 0
    largest = (Fraction(0), 0)
    for n in range(3, 4096, 2):
        fs = factor(n)
        assert prod(p**e for p, e in fs) == n
        k, q = odd_part(n-1)
        counted = 1  # Base 1 always passes but is excluded from P1.
        for x in range(2, n):
            accepted = algorithm_p(n, x, k, q)
            counted += accepted
            cases += 1
            if accepted:
                assert gcd(x, n) == 1
        b, phi, exceptional = liar_count(n, fs)
        assert counted == b
        if len(fs) == 1 and fs[0][1] == 1:
            assert b == n-1
            primes += 1
        else:
            composites += 1
            assert 4*b <= n-1
            probability = Fraction(b-1, n-2)
            assert 4*(b-1) < n-2
            largest = max(largest, (probability, n))
            if not exceptional:
                assert 9*(b-1) <= 2*(n-2)
            else:
                exceptional_count += 1
                assert 4*b == phi
    assert cases == 2047**2 == 4190209
    return dict(odd_inputs=2047, prime_inputs=primes, composite_inputs=composites,
                base_cases=cases, exceptional_composites=exceptional_count,
                maximum_error=dict(n=largest[1], numerator=largest[0].numerator,
                                   denominator=largest[0].denominator))


def printed_numbers():
    rows = []
    for ps, expected in [([49939, 99877], '0.24999'),
                         ([1667, 2143, 4523], '0.24968')]:
        # Elementary primality proofs by all possible trial divisors.
        assert all(all(p % d for d in range(2, isqrt(p)+1)) for p in ps)
        n = prod(ps)
        fs = [(p, 1) for p in ps]
        b, phi, exceptional = liar_count(n, fs)
        assert exceptional and 4*b == phi
        probability = Fraction(b-1, n-2)
        with localcontext() as ctx:
            ctx.prec = 60
            decimal = Decimal(probability.numerator) / Decimal(probability.denominator)
            assert str(decimal.quantize(Decimal('.00001'))) == expected
        rows.append(dict(n=n, prime_factors=ps, b=b, phi=phi,
                         numerator=probability.numerator,
                         denominator=probability.denominator,
                         decimal=str(decimal)))
    per_input = Fraction(1, 4**25)
    total_expectation = 10**9 * per_input
    assert per_input < Fraction(1, 10**15)
    assert total_expectation < Fraction(1, 10**6)
    return dict(examples=rows, repetitions=25,
                error_upper_bound_denominator=per_input.denominator,
                billion_inputs_expectation=dict(numerator=total_expectation.numerator,
                                                denominator=total_expectation.denominator))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--resume', action='store_true')
    ap.add_argument('--only', nargs='*')
    args = ap.parse_args()
    data = json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'checks': {}}
    for name, fn in [('exhaustive', exhaustive), ('printed_numbers', printed_numbers)]:
        if (args.only and name not in args.only) or name in data['checks']:
            continue
        start = time.monotonic()
        result = fn()
        data['checks'][name] = dict(status='passed', seconds=time.monotonic()-start, result=result)
        OUT.write_text(json.dumps(data, indent=2)+'\n')
        print(name, 'PASSED', flush=True)


if __name__ == '__main__':
    main()
