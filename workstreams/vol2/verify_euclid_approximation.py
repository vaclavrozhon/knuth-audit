#!/usr/bin/env python3
"""Independent exact models for TAOCP 4.5.3-42,43,44."""
from bisect import bisect_left
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json
import os
import time

ROOT = Path(__file__).resolve().parent


def cf(x):
    a, b = x.numerator, x.denominator
    out = []
    while b:
        q, r = divmod(a, b)
        out.append(q)
        a, b = b, r
    return out


def convergents(x):
    p0, p1, q0, q1 = 0, 1, 1, 0
    for a in cf(x):
        p0, p1, q0, q1 = p1, a * p1 + p0, q1, a * q1 + q0
        yield p1, q1


def cf_round(x, fits):
    previous = (1, 0)
    for pair in convergents(x):
        if not fits(pair):
            return previous
        previous = pair
    return previous


def all_representables(fits, bound):
    return sorted({F(p, q) for p in range(bound) for q in range(1, bound)
                   if gcd(p, q) == 1 and fits((p, q))})


def oracle(x, values):
    j = bisect_left(values, x)
    if j < len(values) and values[j] == x:
        return x.numerator, x.denominator
    assert j > 0
    lo = values[j - 1]
    hi = values[j] if j < len(values) else None
    left = (lo.numerator, lo.denominator)
    right = (hi.numerator, hi.denominator) if hi is not None else (1, 0)
    med = F(left[0] + right[0], left[1] + right[1])
    if x < med:
        return left
    if x > med:
        return right
    return min((left, right), key=lambda a: (a[1], a[0]))


def main():
    start = time.monotonic()
    print('pid', os.getpid(), flush=True)
    best_cases = basis_cases = 0
    for denominator in range(2, 129):
        for numerator in range(1, denominator):
            if gcd(numerator, denominator) != 1:
                continue
            cs = list(convergents(F(numerator, denominator)))
            for (pp, qp), (pn, qn) in zip(cs, cs[1:]):
                error_prev = min((qp * numerator) % denominator,
                                 (-qp * numerator) % denominator)
                det = qp * pn - qn * pp
                assert abs(det) == 1
                for q in range(1, qn):
                    # Independent nearest-integer rounding, with either tie valid.
                    p = (2 * q * numerator + denominator) // (2 * denominator)
                    error = abs(q * numerator - p * denominator)
                    assert error >= error_prev
                    u = (q * pn - p * qn) // det
                    v = (qp * p - pp * q) // det
                    assert q == u * qp + v * qn and p == u * pp + v * pn
                    assert u != 0 and (v == 0 or u * v < 0)
                    e1 = qp * numerator - pp * denominator
                    e2 = qn * numerator - pn * denominator
                    assert e1 * e2 <= 0
                    assert error == abs(u) * abs(e1) + abs(v) * abs(e2)
                    best_cases += 1
                    basis_cases += 1
    print('best-approximation pairs', best_cases, flush=True)

    formats = []
    for M in range(2, 11):
        for N in range(2, 11):
            formats.append((f'rectangle-{M}-{N}', lambda x, M=M, N=N: x[0] < M and x[1] < N,
                            max(M, N)))
    for bits in range(1, 11):
        formats.append((f'floating-{bits}', lambda x, bits=bits: x[0].bit_length() + x[1].bit_length() <= bits,
                        max(2, 1 << (bits - 1))))
    format_results = []
    total = ties = overflows = 0
    for name, fits, bound in formats:
        values = all_representables(fits, bound)
        samples = {v for v in values if v > 0}
        for lo, hi in zip(values, values[1:]):
            med = F(lo.numerator + hi.numerator, lo.denominator + hi.denominator)
            samples.update([(lo + med) / 2, med, (med + hi) / 2])
            assert cf_round(med, fits) == oracle(med, values)
            ties += 1
        last = values[-1]
        threshold = F(last.numerator + 1, last.denominator)
        samples.update([(last + threshold) / 2, threshold, threshold + F(1, 3), threshold + 10])
        ties += 1
        # More values whose CF lengths are independent of the format boundaries.
        samples.update(F(i * i + 1, 3 * i + 2) for i in range(1, 81))
        for x in samples:
            expected = oracle(x, values)
            assert cf_round(x, fits) == expected, (name, x, cf(x), expected)
            total += 1
            overflows += expected[1] == 0
        format_results.append(dict(name=name, representables=len(values), inputs=len(samples)))
    print('rounding samples', total, 'ties', ties, flush=True)

    families = []
    for k in [3, 4, 5, 7, 11, 17, 23, 33, 47, 67]:
        M = N = 3 * k + 1
        fits = lambda x: x[0] < M and x[1] < N
        values = all_representables(fits, N)
        u, v = F(1, 3), F(2 * k + 1, 3 * k)
        first = oracle(u + v, values)
        assert first == (1, 1) == cf_round(u + v, fits)
        second = oracle(F(*first) - v, values)
        assert F(*second) == F(k - 1, 3 * k) != u
        assert 9 < N
        families.append(dict(k=k, M=M, N=N, u=str(u), v=str(v), result=str(F(*second))))
    assert families[7]['M'] == 100 and families[7]['result'] == '32/99'
    result = dict(status='passed', pid=os.getpid(), best_approximation_cases=best_cases,
                  basis_cases=basis_cases, format_count=len(formats), rounding_inputs=total,
                  exact_mediant_ties=ties, overflow_results=overflows, formats=format_results,
                  inverse_addition_family=families, seconds=time.monotonic() - start,
                  scope='Finite exact comparisons with direct enumeration; general mathematical proofs are in notes/euclid-approximation.md.')
    (ROOT / 'results/euclid-approximation.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'formats'}, indent=2), flush=True)


if __name__ == '__main__':
    main()
