#!/usr/bin/env python3
"""DLX14: exact arithmetic for the finite menage identity on p418.

The independent counting oracle is a subset DP that seats one husband at a
time. It does not use the printed recurrence, inclusion-exclusion, or DLX.
This checks formulas and counts, not the historical citations or mem figures.
"""
from datetime import datetime, timezone
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations
from math import comb, factorial, prod
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def falling(n, k):
    return prod(range(n-k+1, n+1))


def t(n):
    assert n >= 0
    return sum((Q((-2)**k, factorial(k)) for k in range(n+1)), Q())


def touchard(n):
    assert n >= 2
    return sum(((-1)**k * Q(2*n, 2*n-k) * comb(2*n-k, k) * factorial(n-k)
                for k in range(n+1)), Q())


def expanded(n, index_step):
    return sum((Q((-1)**j, factorial(j)*falling(n-1, j)) * t(n-index_step*j)
                for j in range(n//2+1)), Q())


def seat_dp(n):
    @lru_cache(None)
    def count(mask):
        husband = mask.bit_count()
        if husband == n:
            return 1
        return sum(count(mask | (1 << seat)) for seat in range(n)
                   if not mask >> seat & 1 and seat not in (husband, (husband+1) % n))
    return count(0)


def main():
    exact = {n: touchard(n) for n in range(2, 81)}
    term_checks = 0
    for n, value in exact.items():
        assert value.denominator == 1
        assert expanded(n, 2) == value / factorial(n)
        # The preceding "kth term" identity is also correct, term by term.
        for k in range(n+1):
            observed = factorial(n) * sum((Q((-1)**(j+k) * 2**(k-2*j),
                factorial(k-2*j)*factorial(j)*falling(n-1, j))
                for j in range(k//2+1)), Q())
            expected = (-1)**k * Q(2*n, 2*n-k)*comb(2*n-k, k)*factorial(n-k)
            assert observed == expected, (n, k)
            term_checks += 1
    recurrence = [1, -1, 0]
    for n in range(2, 80):
        numerator = (n*n-1)*recurrence[n]+(n+1)*recurrence[n-1]+4*(-1)**n
        assert numerator % (n-1) == 0
        recurrence.append(numerator//(n-1))
    assert all(recurrence[n] == value for n, value in exact.items())
    dp = {n: seat_dp(n) for n in range(2, 17)}
    assert all(value == exact[n] for n, value in dp.items())
    enumeration = {}
    for n in range(2, 10):
        enumeration[n] = sum(all(seat not in (k, (k+1) % n)
                                 for k, seat in enumerate(order))
                             for order in permutations(range(n)))
        assert enumeration[n] == dp[n]
    assert [dp[n] for n in range(3, 11)] == [1, 2, 13, 80, 579, 4738, 43387, 439792]
    # Expand the printed ordinary generating function as formal rational
    # power series: (1-z)/(1+z) * sum_m m! (z/(1+z)^2)^m.
    ogf = []
    for n in range(51):
        coefficient = sum(factorial(m)*((-1)**(n-m)*comb(n+m, n-m)
            - ((-1)**(n-m-1)*comb(n+m-1, n-m-1) if n>m else 0))
            for m in range(n+1))
        assert coefficient == recurrence[n]
        ogf.append(coefficient)
    witnesses = []
    for n in (2, 3, 4, 5):
        wrong, right = expanded(n, 1), expanded(n, 2)
        assert wrong != right
        witnesses.append(dict(n=n, solutions=dp[n], u_over_factorial=str(right),
                              printed_expansion=str(wrong),
                              corrected_expansion=str(right)))
    out = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        scope='Finite identities, recurrence, formal OGF, and counts. History, asymptotic proof, and mem claims remain separate.',
        exact_n_range=[2,80], preceding_term_checks=term_checks,
        subset_dp=dp, exhaustive_permutations=enumeration,
        ogf_coefficients=ogf, counterexamples=witnesses,
        correction='In the explicit expansion, T_(n-j) must be T_(n-2j). The compact sum immediately to its left is already correct.')
    destination=ROOT/'results/menage'
    destination.mkdir(exist_ok=True)
    (destination/'finite-identity.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','preceding_term_checks','subset_dp','counterexamples']},indent=2))


if __name__ == '__main__':
    main()
