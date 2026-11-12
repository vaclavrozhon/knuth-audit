#!/usr/bin/env python3
"""Exact checks of the Mersenne list and digit counts, not new large-prime proofs."""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import hashlib
import json
import time

BASE = Path(__file__).resolve().parent
OUT = BASE / 'results/mersenne-context.json'


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def logarithm_interval(t, terms):
    # log((1+t)/(1-t)) = 2 sum t^(2j+1)/(2j+1).
    lower = 2*sum((t**(2*j+1)/Fraction(2*j+1)
                   for j in range(terms)), Fraction(0))
    tail = 2*t**(2*terms+1)/((2*terms+1)*(1-t*t))
    return lower, lower+tail


def power(a, e, n):
    r = 1
    for bit in bin(e)[2:]:
        r = r*r % n
        if bit == '1':
            r = r*a % n
    return r


def main():
    started = time.monotonic()
    rows = json.loads((BASE/'sources/mersenne-listed-2026-11-03.json').read_text())['rows']
    original = [2,3,5,7,13,17,19,31,61,89,107,127,521,607,1279,2203,
                2281,3217,4253,4423,9689,9941,11213,19937,21701,23209,
                44497,86243,110503,132049,216091,756839,859433,1257787,
                1398269,2976221]
    old_additions = [3021377,6972593,13466917,20996011,24036583,25964951,
                     30402457,32582657,37156667,42643801,43112609]
    corrected_new_additions = [57885161,74207281,77232917,82589933,136279841]
    exponents = [r['exponent'] for r in rows]
    assert exponents == original+old_additions+corrected_new_additions
    assert len(exponents) == 52 and exponents == sorted(set(exponents))
    assert all(prime(p) for p in exponents)  # Only the exponents, not M_p.
    ln2lo, ln2hi = logarithm_interval(Fraction(1,3), 64)
    ln5lo, ln5hi = logarithm_interval(Fraction(2,3), 64)
    lo = ln2lo/(ln2hi+ln5hi)
    hi = ln2hi/(ln2lo+ln5lo)
    assert 0 < hi-lo < Fraction(1, 10**23)
    digits, direct = [], 0
    for row in rows:
        p = row['exponent']
        a, b = (p*lo).__floor__()+1, (p*hi).__floor__()+1
        assert a == b == row['digits']
        if p <= 11213:
            assert len(str((1 << p)-1)) == a
            direct += 1
        digits.append(dict(exponent=p, digits=a))
    wrong = 77232017
    assert wrong == 19*29*140167 and all(prime(p) for p in [19,29,140167])
    factor = 2**19-1
    assert prime(factor)
    assert pow(2, wrong, factor) == power(2, wrong, factor) == 1
    assert wrong//19 == 4064843 and wrong not in exponents
    # A proper factor suffices to refute primality of M_8191.
    f = 338193759479
    M = (1 << 8191)-1
    quotient, remainder = divmod(M, f)
    assert prime(8191) and 1 < f < M and quotient > 1 and remainder == 0
    assert pow(2, 8191, f) == power(2, 8191, f) == 1
    result = dict(
        passed=True, seconds=time.monotonic()-started,
        original_entries=len(original), old_additions=len(old_additions),
        new_additions_with_C0163_repair=len(corrected_new_additions),
        exponent_primality_checks=len(exponents), digit_count_checks=len(digits),
        direct_integer_digit_count_checks=direct,
        log10_2_interval=dict(lower=str(lo), upper=str(hi), terms_per_log=64),
        digit_counts=digits,
        C0163=dict(wrong_exponent=wrong, exponent_factorization=[19,29,140167],
                   proper_divisor_of_M= factor, exponent_quotient=wrong//19,
                   corrected_exponent=77232917),
        M8191=dict(proper_factor=f, division_remainder=0,
                   cofactor_bits=quotient.bit_length(),
                   cofactor_sha256=hashlib.sha256(quotient.to_bytes(
                       (quotient.bit_length()+7)//8,'big')).hexdigest()),
        scope='52 prime exponents and exact digit counts. Primality of large M_p relies on identified external verification records; earlier local Lucas checks through exponent11213 are not rerun.')
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()
                      if k not in ['log10_2_interval','digit_counts']},indent=2))


if __name__ == '__main__':
    main()
