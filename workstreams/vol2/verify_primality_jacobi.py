#!/usr/bin/env python3
"""Exact finite cross-checks for TAOCP2 exercise 4.5.4-23.

Independent models: Euclidean reciprocity algorithm versus sets of squares
modulo trial-certified prime factors; direct exponentiation versus CRT counts.
The general proofs are in notes/primality-jacobi.md.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import gcd, prod
from pathlib import Path
import csv
import hashlib
import json
import time

from verify_primality_probabilistic import factor, odd_part, algorithm_p

ROOT = Path(__file__).resolve().parent


def jacobi(a, n):
    assert n > 0 and n % 2
    a %= n
    sign = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                sign = -sign
        if a % 4 == n % 4 == 3:
            sign = -sign
        a, n = n % a, a
    return sign if n == 1 else 0


@lru_cache(None)
def quadratic_residues(p):
    assert p > 2 and factor(p) == [(p, 1)]
    squares = {x*x % p for x in range(1, p)}
    assert len(squares) == (p-1)//2
    return squares


def factored_symbol(a, fs):
    result = 1
    for p, e in fs:
        if a % p == 0:
            return 0
        if e % 2 and a % p not in quadratic_residues(p):
            result = -result
    return result


def predicted_counts(n, fs):
    k, q = odd_part(n-1)
    ss = [odd_part(p-1)[0] for p, e in fs]
    m = min(ss)
    assert m <= k
    pi = prod(gcd((n-1)//2, p-1) for p, e in fs)
    if m == k:
        return pi, pi, 'two'
    if any(s < k and e % 2 for s, (p, e) in zip(ss, fs)):
        assert pi % 2 == 0
        return pi//2, 0, 'half'
    return pi, 0, 'one'


def main():
    start = time.monotonic()
    rows = []
    branches = Counter()
    total = primes = composites = inclusions = strict_separations = 0
    special_numbers = []
    largest = (Fraction(0), 0)
    examples = {}
    for n in range(3, 4096, 2):
        fs = factor(n)
        assert prod(p**e for p, e in fs) == n
        phi = prod((p-1)*p**(e-1) for p, e in fs)
        k, q = odd_part(n-1)
        plus = minus = strong_count = 0
        for x in range(n):
            symbol = jacobi(x, n)
            assert symbol == factored_symbol(x, fs)
            assert (symbol == 0) == (gcd(x, n) != 1)
            euler = symbol != 0 and pow(x, (n-1)//2, n) == symbol % n
            strong = algorithm_p(n, x, k, q)
            assert not strong or euler
            inclusions += strong
            strict_separations += euler and not strong
            strong_count += strong
            plus += euler and symbol == 1
            minus += euler and symbol == -1
            total += 1
        pp, pm, branch = predicted_counts(n, fs)
        assert (plus, minus) == (pp, pm)
        branches[branch] += 1
        b = plus+minus
        prime = fs == [(n, 1)]
        carmichael = not prime and all(e == 1 and (n-1) % (p-1) == 0 for p, e in fs)
        special = carmichael and max(odd_part(p-1)[0] for p, e in fs) < k
        if prime:
            primes += 1
            assert b == strong_count == n-1
        else:
            composites += 1
            assert 2*b <= phi
            if not special:
                assert 4*b <= n-1
            else:
                assert 2*b == phi
                special_numbers.append(n)
            largest = max(largest, (Fraction(b, n-1), n))
        rows.append([n, k, branch, phi, plus, minus, strong_count, int(special)])
        if n in (9, 27, 45, 81, 341, 561, 1729):
            examples[str(n)] = dict(factors=fs, k=k, delta=branch, phi=phi,
                                    euler_plus=plus, euler_minus=minus,
                                    strong=strong_count,
                                    error=None if prime else str(Fraction(b, n-1)))
    path = ROOT/'results/primality-jacobi-counts.csv'
    with path.open('w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['n', 'k', 'delta', 'phi', 'euler_plus', 'euler_minus', 'strong', 'special_carmichael'])
        writer.writerows(rows)
    # Historical Lebesgue examples; negative numerators use the natural
    # periodic extension, explicitly outside Knuth's stated nonnegative domain.
    historical = [(a, n, jacobi(a, n)) for a, n in [(-3778, 773), (3785, 2933)]]
    assert [v for a, n, v in historical] == [1, 1]
    for a, n, v in historical:
        assert v == factored_symbol(a, factor(n))
    result = dict(status='passed', elapsed_seconds=time.monotonic()-start,
                  odd_inputs=len(rows), prime_inputs=primes, composite_inputs=composites,
                  all_residue_cases=total, delta_branches=dict(branches),
                  strong_passes=inclusions, euler_only_passes=strict_separations,
                  special_carmichael_inputs=special_numbers,
                  maximum_composite_error=dict(n=largest[1], value=str(largest[0])),
                  examples=examples, historical_examples=historical,
                  csv_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    (ROOT/'results/primality-jacobi.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
