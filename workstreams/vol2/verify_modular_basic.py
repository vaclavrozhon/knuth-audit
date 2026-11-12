#!/usr/bin/env python3
"""Exact independent checks for TAOCP2 4.3.2, text and exercises1–13.

General proofs are in notes/modular-basic.md. Checkpoints avoid repeating
successful blocks. No historical timings or floating FFT are tested here.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import gcd, lcm, prod
from pathlib import Path
import argparse, json, random, time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/modular-basic.json'


def balanced(x, m):
    h = (m - 1) // 2
    return (x + h) % m - h


def garner(res, mods, symmetric=False, compressed=False):
    v = []
    for j, (u, m) in enumerate(zip(res, mods)):
        if compressed:
            prefix = 0
            for i in range(j - 1, -1, -1):
                prefix = (prefix * mods[i] + v[i]) % m
            z = (u - prefix) * pow(prod(mods[:j]), -1, m)
        else:
            z = u
            for i in range(j):
                z = (z - v[i]) * pow(mods[i], -1, m) % m
        v.append(balanced(z, m) if symmetric else z % m)
    return v


def expand(v, mods):
    x = 0
    for j in range(len(v) - 1, -1, -1):
        x = x * mods[j] + v[j]
    return x


def backward_inplace(v, mods):
    v = v[:]
    for j in range(len(v) - 1, -1, -1):
        z = v[j]
        for i in range(j - 1, -1, -1):
            z = (z * mods[i] + v[i]) % mods[j]
        v[j] = z % mods[j]
    return v


def merge(res, mods):
    """General CRT, merged via independent two-modulus Bezout inverses."""
    x, M = 0, 1
    for u, m in zip(res, mods):
        d = gcd(M, m)
        if (u - x) % d:
            return None
        h = m // d
        t = ((u - x) // d * pow(M // d, -1, h)) % h
        x += M * t
        M *= h
        assert 0 <= x < M
    return x, M


def totient(m):
    return sum(gcd(i, m) == 1 for i in range(1, m + 1))


def crt():
    cases = tuples = balanced_cases = 0
    for mods in product(range(1, 10), repeat=3):
        if any(gcd(a, b) != 1 for a, b in combinations(mods, 2)):
            continue
        M = prod(mods)
        basis = [pow(M // m, totient(m), M) for m in mods]
        cases += 1
        for x in range(M):
            # Oracle: reduce an explicitly enumerated original integer.
            res = [x % m for m in mods]
            lifted = [u + (-2 if j % 2 else 3) * m
                      for j, (u, m) in enumerate(zip(res, mods))]
            v = garner(lifted, mods)
            assert v == garner(lifted, mods, compressed=True)
            assert expand(v, mods) == x
            assert sum(a * b for a, b in zip(lifted, basis)) % M == x
            assert backward_inplace(v, mods) == res
            # Parallel triangular form(24), with snapshots at every time j.
            work = res[:]
            for j in range(len(mods) - 1):
                pivot = work[j]
                work[j + 1:] = [(work[k] - pivot) * pow(mods[j], -1, mods[k]) % mods[k]
                                for k in range(j + 1, len(mods))]
            assert work == v
            if all(m % 2 for m in mods):
                sv = garner(lifted, mods, symmetric=True)
                assert expand(sv, mods) == balanced(x, M)
                assert sv == garner(lifted, mods, symmetric=True, compressed=True)
                balanced_cases += 1
            tuples += 1
    assert garner([1, 6, 5], [7, 11, 13]) == [1, 7, 6]
    assert expand([1, 7, 6], [7, 11, 13]) == 512
    generalized = compatible = 0
    for mods in product(range(1, 8), repeat=3):
        M = lcm(*mods)
        # Complete table of actual residues; no CRT routine in this oracle.
        table = {tuple(x % m for m in mods): x for x in range(M)}
        for res in product(*(range(m) for m in mods)):
            ok = all((res[i] - res[j]) % gcd(mods[i], mods[j]) == 0
                     for i, j in combinations(range(3), 2))
            got = merge(res, mods)
            assert ok == (res in table) == (got is not None)
            if ok:
                compatible += 1
                assert got == (table[res], M)
                for a in [-M - 2, 0, M + 3]:
                    u = a + (got[0] - a) % M
                    assert a <= u < a + M
                    assert all((u - t) % m == 0 for t, m in zip(res, mods))
            generalized += 1
    real_cases = 0
    for mods in [(1, 1), (2, 3), (3, 5, 7)]:
        M = prod(mods)
        for f in [F(0), F(1, 2), F(2, 3), F(7, 11)]:
            for a in [F(-17, 9), F(0), F(7, 4)]:
                for x in range(M):
                    residues = [F(x % m) + f for m in mods]
                    integer = merge([int(t - f) for t in residues], mods)[0]
                    u = a + (integer + f - a) % M
                    assert a <= u < a + M
                    assert all((u - t) % m == 0 for t, m in zip(residues, mods))
                    real_cases += 1
    return dict(pairwise_modulus_tuples=cases, complete_integer_inputs=tuples,
                balanced_inputs=balanced_cases, general_residue_tuples=generalized,
                compatible_general_tuples=compatible, rational_cases=real_cases,
                exercise1=dict(moduli=[7, 11, 13], residues=[1, 6, 5], digits=[1, 7, 6], answer=512))


def mod0(x, m):
    return x % m if m else x


def mersenne():
    operations = 0
    for e in range(1, 9):
        B = 1 << e
        M = B - 1
        add = lambda x, y: (x + y) % B + (x + y >= B)
        for x, y in product(range(B), repeat=2):
            vals = [add(x, y), (x - y) % B - (x < y),
                    add(x * y % B, x * y // B), x - y + M * (x < y)]
            targets = [x + y, x - y, x * y, x - y]
            assert all(0 <= a <= M and a % M == b % M for a, b in zip(vals, targets))
            operations += 4
    identities = 0
    for e, f in product(range(65), repeat=2):
        assert gcd((1 << e) - 1, (1 << f) - 1) == (1 << gcd(e, f)) - 1
        assert mod0((1 << e) - 1, (1 << f) - 1) == (1 << mod0(e, f)) - 1
        identities += 2
        for g in range(17):
            assert (mod0((1 << e) - (1 << f), (1 << g) - 1) == 0) == (mod0(e - f, g) == 0)
            identities += 1
    inverses = 0
    for e, f in product(range(1, 50), range(2, 50)):
        if gcd(e, f) != 1:
            continue
        d, c = e % f, pow(e, -1, f)
        v = sum(1 << (i * d) for i in range(c))
        assert v * ((1 << e) - 1) % ((1 << f) - 1) == 1
        inverses += 1
    assert mod0((1 << 1) - 1, 0) == 1  # f0 permits only ce1; e=c1.
    return dict(word_operations=operations, exponent_identities=identities,
                inverse_formulas=inverses,
                five_moduli_range=prod((1 << e) - 1 for e in [32, 31, 29, 27, 25]),
                five_moduli_lower_bound=1 << 143)


def primes(limit):
    return [p for p in range(2, limit + 1) if all(p % d for d in range(2, int(p**0.5) + 1))]


def choice():
    chosen = []
    for m in range(99, 1, -2):
        if all(gcd(m, n) == 1 for n in chosen):
            chosen.append(m)
    assert chosen == [99, 97, 95, 91, 89, 83, 79, 73, 71, 67, 61, 59, 53,
                      47, 43, 41, 37, 31, 29, 23, 17]
    def powers(limit, odd):
        out = []
        for p in primes(limit):
            if odd and p == 2:
                continue
            q = p
            while q * p <= limit:
                q *= p
            out.append(q)
        return out
    optimal = powers(99, True)
    assert prod(optimal) == 315 * prod(chosen)
    eight = powers(256, False)
    assert all(gcd(a, b) == 1 for a, b in combinations(eight, 2))
    assert prod(eight) == lcm(*range(1, 257))
    M = prod(eight)
    assert 1665 * 10**106 <= M < 1675 * 10**106
    assert prod((1 << e) - 1 for e in [32, 31, 29, 27, 25]) > (1 << 143)
    return dict(greedy_moduli=chosen, greedy_product=prod(chosen),
                optimal_odd_moduli=optimal, optimal_odd_product=prod(optimal),
                ratio=315, optimal_eight_bit_moduli=eight, optimal_eight_bit_product=M,
                interpretation='8-bit residues allow modulus256, although256 itself takes9 bits')


def szabo():
    collision_pairs = threshold_cases = transformed = 0
    for a in range(2, 10):
        for b in range(a + 1, 31):
            if gcd(a, b) != 1:
                continue
            M = a * b
            for p, q in combinations(range(a), 2):
                # Enumerate all actual colliding pairs, independently of proof.
                pairs = []
                for u in range(M):
                    if u % a not in (p, q):
                        continue
                    for v in range(u + b, M, b):
                        if v % a in (p, q):
                            pairs.append((u, v))
                u, v = min(pairs)
                assert u < a
                collision_pairs += 1
                for twice_L in range(2 * a, 2 * (M - a) + 1):
                    L = F(twice_L, 2)
                    U, V = (u, v) if v >= L else (v - a, u + M - a)
                    transformed += (v < L)
                    assert 0 <= U < L <= V < M
                    assert {U % a, V % a} == {p, q} and U % b == V % b
                    threshold_cases += 1
    return dict(merged_residue_pairs=collision_pairs, threshold_cases=threshold_cases,
                transformed_pairs=transformed,
                scope='Every noninjective g has a colliding pair; enumerate all such pairs for a2..9,b>a through30.')


def arithmetic():
    pairs = halvings = 0
    for mods in [(1, 1), (3, 5), (3, 5, 7), (5, 7, 9)]:
        M = prod(mods)
        for u, v in product(range(M), repeat=2):
            s = (u + v) % M
            assert (u + v >= M) == (s < u)
            digits = garner([s % m for m in mods], mods)
            assert (u + v >= M) == ((u % 2 + v % 2 - sum(digits)) % 2 != 0)
            a, b = balanced(u, M), balanced(v, M)
            h = (M - 1) // 2
            for t in [a + b, a - b]:
                assert t - M * (t > h) + M * (t < -h) == balanced(t, M)
            va = garner([a % m for m in mods], mods, symmetric=True)
            vb = garner([b % m for m in mods], mods, symmetric=True)
            assert (va[::-1] < vb[::-1]) == (a < b)
            pairs += 1
        for u in range(0, M, 2):
            residues = [(u % m) * ((m + 1) // 2) % m for m in mods]
            assert expand(garner(residues, mods), mods) == u // 2
            halvings += 1
    roots = []
    for n in range(1, 33):
        M, a, b = 10**n, 2**n, 5**n
        x = b * pow(b, -1, a) % M
        y = (1 - x) % M
        assert x > 1 and y > 1 and x + y == M + 1
        assert x*x % M == x and y*y % M == y
        for z in [x, y]:
            lift = (3*z*z - 2*z*z*z) % (M*M)
            oracle = (b*b * pow(b*b, -1, a*a)) % (M*M)
            if z == y:
                oracle = (1 - oracle) % (M*M)
            assert lift == oracle and lift % M == z
        if n <= 5:
            assert [z for z in range(M) if z*z % M == z] == sorted([0, 1, x, y])
        roots.append(dict(n=n, roots=[x, y]))
    inverse_lifts = 0
    for y in range(1, 60):
        for x in range(-60, 61):
            if gcd(x, y) != 1:
                continue
            c0 = pow(x, -1, y)
            for c in [c0 - 2*y, c0, c0 + 3*y]:
                new = 3*c*c - 2*c*c*c*x
                assert (new*x*x - 1) % (y*y) == 0
                inverse_lifts += 1
    return dict(overflow_and_balanced_pairs=pairs, even_halvings=halvings,
                automorphs=roots, inverse_square_lifts=inverse_lifts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    result = json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}
    for name, function in [('crt', crt), ('mersenne', mersenne), ('choice', choice),
                           ('szabo', szabo), ('arithmetic', arithmetic)]:
        if name in result:
            continue
        start = time.monotonic()
        result[name] = function()
        result[name]['elapsed_seconds'] = round(time.monotonic() - start, 3)
        OUT.write_text(json.dumps(result, indent=2) + '\n')
        print(name, 'PASS', result[name]['elapsed_seconds'], flush=True)
    print('ALL FIVE CHECKPOINTS PASS', flush=True)


if __name__ == '__main__':
    main()
