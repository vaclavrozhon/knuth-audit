#!/usr/bin/env python3
"""Exact finite certificates for TAOCP 4.1-30(d) and its additional example."""
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def decode(n, period):
    original = n
    digits = []
    for k in range(1000):
        if n == 0:
            assert sum(bit * (1 << j) * period[j % len(period)]
                       for j, bit in enumerate(digits)) == original
            return digits
        bit = n % 2
        digits.append(bit)
        n = (n - bit * period[k % len(period)]) // 2
    raise AssertionError(('termination', original, period))


def grouped(n, period):
    for d in period:
        n = (n - (n % 2) * d) // 2
    return n


def certify(period, expected_offsets, lo, hi):
    modulus = 1 << len(period)
    offsets = [grouped(r, period) for r in range(modulus)]
    assert offsets == expected_offsets
    errors = [Fraction(offsets[r]) - Fraction(r, modulus)
              for r in range(modulus)]
    lower, upper = min(errors), max(errors)
    # For n >= hi+1: lo <= F(n) < n. For n <= lo-1: n < F(n) <= hi.
    assert Fraction(hi + 1, modulus) + upper < hi + 1
    assert Fraction(hi + 1, modulus) + lower >= lo
    assert Fraction(lo - 1, modulus) + lower > lo - 1
    assert Fraction(lo - 1, modulus) + upper <= hi
    paths = {}
    for start in range(lo, hi + 1):
        n = start
        path = [n]
        while n:
            n = grouped(n, period)
            assert lo <= n <= hi
            assert n not in path, (period, start, path, n)
            path.append(n)
        paths[str(start)] = path
    translations = 0
    for q in range(-100, 101):
        for r in range(modulus):
            assert grouped(modulus * q + r, period) == q + offsets[r]
            translations += 1
    lengths = [len(decode(n, period)) for n in range(-10000, 10001)]
    # Independent subset-sum enumeration: values must be distinct; division
    # must recover precisely the chosen finite subset, up to leading zeros.
    seen = set()
    for mask in range(1 << 14):
        chosen = [i for i in range(14) if mask >> i & 1]
        value = sum((1 << i) * period[i % len(period)] for i in chosen)
        assert value not in seen
        seen.add(value)
        bits = decode(value, period)
        recovered = sum(bit << i for i, bit in enumerate(bits))
        assert recovered == mask
    return {'period': period, 'group_modulus': modulus, 'offsets': offsets,
            'affine_error_bounds': [str(lower), str(upper)],
            'invariant_interval': [lo, hi], 'paths': paths,
            'group_translation_checks': translations,
            'integer_reconstructions': len(lengths),
            'max_reconstruction_length': max(lengths),
            'distinct_subset_sums_and_recoveries': len(seen)}


def main():
    target = ROOT / 'results/binary-bases.json'
    if target.exists():
        raise SystemExit('Refusing to overwrite a completed certificate.')
    result = {'scope': 'Finite termination certificates plus independent subset sums; general proofs in notes/generalized-bases.md.',
              'examples': []}
    for period, offsets, lo, hi in [([7, -13], [0, 5, 7, -1], -2, 8),
                                  ([5, -3, 3], [0, -2, 1, -1, -1, 0, 0, 1], -2, 2)]:
        result['examples'].append(certify(period, offsets, lo, hi))
        print('PASS', period, flush=True)
    exponents = [0, 1, 2, 3, 5, 9, 10]
    terms = [(1 << k) * [7, -13][k % 2] for k in exponents]
    assert sum(terms) == 1
    assert decode(1, [7, -13]) == [int(k in exponents) for k in range(11)]
    result['printed_one'] = {'exponents': exponents, 'terms': terms, 'sum': sum(terms)}
    result['status'] = 'passed'
    target.write_text(json.dumps(result, indent=2) + '\n')
    print('PASS printed representation of 1', flush=True)


if __name__ == '__main__':
    main()
