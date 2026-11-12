#!/usr/bin/env python3
"""Exact finite checks of the congruence-only AKS statement after fixing z/a.

No perfect-power or small-factor precheck is applied. These finite checks do
not prove that the omitted hypotheses are redundant. Arb certifies rounding;
FLINT polynomial powers are cross-checked by independent integer models.
"""
from pathlib import Path
from math import comb, gcd, isqrt, lcm
from collections import Counter
import argparse
import csv
import hashlib
import json
import time
from flint import arb, ctx, nmod_poly

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/primality-aks.json'


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def log_floors(n, r=None):
    for precision in [64, 128, 256, 512]:
        ctx.prec = precision
        lg = arb(n.bit_length()-1) if n & (n-1) == 0 else arb(n).log()/arb(2).log()
        x = lg*lg if r is None else arb(r).sqrt()*lg
        z = x.floor().unique_fmpz()
        if z is not None:
            return int(z)
    raise ArithmeticError(('ambiguous logarithmic floor', n, r))


def parameters(n):
    limit = log_floors(n)
    r = limit+2  # ord_r(n) <= phi(r) <= r-1.
    while True:
        if gcd(n, r) == 1:
            z = 1
            for j in range(1, limit+1):
                z = z*n % r
                if z == 1:
                    break
            else:
                # Complete order, independently certifying the chosen inequality.
                z = n % r
                order = 1
                while z != 1:
                    z = z*n % r
                    order += 1
                assert order > limit and order < r
                return r, log_floors(n, r), order
        r += 1


def vector(poly, r):
    return [int(poly[i]) for i in range(r)]


def direct_binomial(n, r, a):
    out = [0]*r
    coefficient = 1
    # Expand (a+x)^n with exact integer binomial coefficients.
    for j in range(n+1):
        out[j % r] = (out[j % r]+coefficient*pow(a, n-j, n)) % n
        if j < n:
            coefficient = coefficient*(n-j)//(j+1)
    return out


def cyclic_multiply(u, v, n):
    r = len(u)
    out = [0]*r
    for i, x in enumerate(u):
        if x:
            for j, y in enumerate(v):
                out[(i+j) % r] += x*y
    return [x % n for x in out]


def cyclic_power(n, r, a):
    result = [1]+[0]*(r-1)
    # Left-to-right powering, as opposed to FLINT's implementation.
    for bit in bin(n)[2:]:
        result = cyclic_multiply(result, result, n)
        if bit == '1':
            # Multiplication by x+a is linear in r.
            result = [(a*result[i]+result[(i-1) % r]) % n for i in range(r)]
    return result


def check_number(n, binomial=False, independent=False):
    r, amax, order = parameters(n)
    modulus = nmod_poly([-1]+[0]*(r-1)+[1], n)
    checks = 0
    for a in range(1, amax+1):
        actual = vector(nmod_poly([a, 1], n).pow_mod(n, modulus), r)
        expected = [0]*r
        expected[0] = a % n
        expected[n % r] = (expected[n % r]+1) % n
        if binomial:
            assert actual == direct_binomial(n, r, a)
        if independent:
            assert actual == cyclic_power(n, r, a)
        checks += 1
        if actual != expected:
            i = next(i for i in range(r) if actual[i] != expected[i])
            return [n, r, amax, order, a, i, actual[i], expected[i]], checks
    return [n, r, amax, order, 0, -1, 0, 0], checks


def consecutive():
    rows = []; counts = Counter(); failures = []; checks = independent = 0
    for n in range(2, 2049):
        row, c = check_number(n, binomial=n <= 127)
        rows.append(row); checks += c
        if n <= 127:
            independent += c
        accepted = row[4] == 0
        truth = prime(n)
        if accepted != truth:
            failures.append(row)
        counts['prime' if truth else 'composite'] += 1
    path = ROOT/'results/primality-aks-consecutive.csv'
    with path.open('w') as f:
        w = csv.writer(f, lineterminator='\n'); w.writerow(['n','r','amax','order','first_reject_a','coefficient','actual','expected']);w.writerows(rows)
    return dict(inputs=len(rows), classifications=dict(counts), congruences=checks,
                independent_binomial_congruences=independent,
                counterexamples=failures, maximum_r=max(row[1] for row in rows),
                csv_sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def prime_squares():
    rows = []; checks = 0
    # Smaller prime squares are already covered by the first checkpoint.
    for p in range(47, 10001, 2):
        if not prime(p):
            continue
        row, c = check_number(p*p, independent=p in [1093, 3511])
        rows.append(row); checks += c
    path = ROOT/'results/primality-aks-squares.csv'
    with path.open('w') as f:
        w = csv.writer(f, lineterminator='\n'); w.writerow(['n','r','amax','order','first_reject_a','coefficient','actual','expected']);w.writerows(rows)
    return dict(prime_squares=len(rows), congruences=checks,
                counterexamples=[row for row in rows if row[4] == 0],
                independent_cyclic_inputs=[1093**2, 3511**2],
                csv_sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def lcm_lemma():
    checked = 0
    for m in range(2, 258):
        row = [comb(m-1, j) for j in range(m)]
        d = lcm(*range(1, m+1))
        assert m*lcm(*row) == d
        assert sum(row) == 2**(m-1) <= d
        checked += len(row)
    for p in [1093, 3511]:
        assert pow(2, p-1, p*p) == 1
        assert pow(2, p*p, p*p) == 2
    return dict(integer_limits=256, binomial_coefficients=checked,
                wieferich_integer_checks=[1093, 3511], counterexamples=[])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--resume', action='store_true')
    ap.add_argument('--only', nargs='*')
    args = ap.parse_args()
    data = json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'checks': {}}
    for name, fn in [('consecutive', consecutive), ('prime_squares', prime_squares),
                     ('lcm_lemma', lcm_lemma)]:
        if (args.only and name not in args.only) or name in data['checks']:
            continue
        start = time.monotonic(); result = fn()
        data['checks'][name] = dict(status='counterexample_found' if result['counterexamples'] else 'finite_check_passed',
                                   seconds=time.monotonic()-start, result=result)
        OUT.write_text(json.dumps(data, indent=2)+'\n')
        print(name, data['checks'][name]['status'], flush=True)


if __name__ == '__main__':
    main()
