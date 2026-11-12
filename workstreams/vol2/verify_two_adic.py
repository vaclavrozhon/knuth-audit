#!/usr/bin/env python3
"""Independent modular checks for TAOCP 4.1-31, including algorithm H."""
from pathlib import Path
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / 'results/two-adic.json'


def quotient_bits(u, v, bits):
    assert v % 2
    w = u % 2
    for n in range(1, bits):
        modulus = 1 << (n + 1)
        discrepancy = ((u % modulus) - (v % modulus) * w) % modulus
        assert discrepancy in [0, 1 << n]
        w += discrepancy
        assert (u-v*w) % modulus == 0
    return w


def root_h(n, bits):
    assert n % 8 == 1
    m, k, v = (n-1)//8, 2, 1
    while k < bits:
        assert v*v == n - (1 << (k+1))*m
        if m % 2:
            m = (m-v-(1 << (k-1)))//2
            v += 1 << k
        else:
            m //= 2
        k += 1
        assert v*v == n - (1 << (k+1))*m
    return v


def classify(n):
    if n == 0:
        return True
    k = 0
    while n % 2 == 0:
        k += 1
        n //= 2
    return k % 2 == 0 and n % 8 == 1


def main():
    out = json.loads(TARGET.read_text()) if TARGET.exists() else {}
    if out.get('status') == 'passed':
        raise SystemExit('Refusing to repeat completed checks.')
    if 'division_comparisons' not in out:
        cases = 0
        # Algorithm's bit-by-bit lift compared with Euclidean modular inversion.
        for bits in range(1, 10):
            modulus = 1 << bits
            for v in range(1, modulus, 2):
                inverse = pow(v, -1, modulus)
                for u in range(-17, 18):
                    assert quotient_bits(u, v, bits) == u * inverse % modulus
                    cases += 1
        out['division_comparisons'] = cases
        print('PASS division', cases, flush=True)
        TARGET.write_text(json.dumps(out, indent=2)+'\n')
    if 'algorithm_h_64_bit_roots' not in out:
        # Exhaustive squares modulo a larger power certify the complete criterion
        # for this bounded input interval: all nonzero n have valuation <= 12.
        modulus = 1 << 15
        residues = {v*v % modulus for v in range(modulus)}
        cases = 0
        for n in range(-4096, 4097):
            assert classify(n) == (n % modulus in residues), n
            cases += 1
        out['criterion_comparisons'] = cases
        out['criterion_modulus'] = modulus
        checks = 0
        for n in range(-4095, 4098, 8):
            v = root_h(n, 64)
            assert v % 4 == 1
            assert (v*v-n) % (1 << 65) == 0
            checks += 1
        out['algorithm_h_64_bit_roots'] = checks
        # Independent enumeration at a small modulus: each odd root branch modulo
        # 2^m is +/-v or +/-v+2^(m-1). Modulo 2^(m+1), H selects the extending bit.
        bits, modulus = 10, 1 << 10
        roots = {}
        for v in range(modulus):
            roots.setdefault(v*v % modulus, set()).add(v)
        for n in range(1, modulus, 8):
            v = root_h(n, bits)
            expected = {(v+s) % modulus for s in [0, modulus//2]}
            expected |= {(-v+s) % modulus for s in [0, modulus//2]}
            assert roots[n] == expected
        out['independent_odd_root_sets_mod_1024'] = 128
        print('PASS square criterion and algorithm H', flush=True)
        TARGET.write_text(json.dumps(out, indent=2)+'\n')
    if 'rational_periods_count' not in out:
        periods = []
        for d in range(3, 202, 2):
            k = 1
            while pow(2, k, d) != 1:
                k += 1
            m = ((1 << k)-1)//d
            assert Fraction(m, (1 << k)-1) == Fraction(1, d)
            for repeats in [1, 2, 3]:
                word = m * ((1 << (k*repeats))-1)//((1 << k)-1)
                assert (d*word+1) % (1 << (k*repeats)) == 0
            periods.append([d, k, m])
        out['rational_periods'] = periods
        out['rational_periods_count'] = len(periods)
        TARGET.write_text(json.dumps(out, indent=2)+'\n')
    # Printed suffixes transcribed from page 213. Each value is the residue
    # after shifting the displayed radix point to the right edge.
    printed = [(7,1,'000000000000111',0),(-7,1,'111111111111001',0),
               (7,4,'00000000000000111',2),(1,7,'110110110110111',0),
               (-1,7,'001001001001001',0),(1,10,'1100110011001101',1)]
    for numerator, denominator, word, shift in printed:
        scaled = Fraction(numerator,denominator)*(1 << shift)
        assert scaled.denominator % 2
        mod = 1 << len(word)
        assert int(word,2) == scaled.numerator*pow(scaled.denominator,-1,mod) % mod
    square_words = ['100000010110101','011111101001011']
    mod = 1 << len(square_words[0])
    v = root_h(-7, len(square_words[0]))
    assert int(square_words[0],2) == v
    assert int(square_words[1],2) == (-v) % mod
    assert (int(square_words[0],2)+int(square_words[1],2)) % mod == 0
    out['printed_rational_suffixes'] = printed
    out['printed_square_root_suffixes'] = square_words
    out['zero_exception'] = {'square_root':0, 'reason':'0 mod 2^(2k+3) is 0, never 2^(2k), for every k >= 0.'}
    out['status'] = 'passed'
    TARGET.write_text(json.dumps(out,indent=2)+'\n')
    print('PASS periodic rational identities and all eight printed suffixes', flush=True)


if __name__ == '__main__':
    main()
