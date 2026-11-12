#!/usr/bin/env python3
"""Exact finite cross-checks for TAOCP 4.5.4-30/31 and Dixon's algorithm.

The general proofs are in notes/factoring-dixon.md. No random experiment is
used here: residues, exponent pairs, and binomial probabilities are exhaustive.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb, factorial, gcd, prod
from pathlib import Path
import json
import os
import time

BASE = Path(__file__).resolve().parent
OUT = BASE / 'results/factoring-dixon.json'
BASES = [(2,), (2, 3), (2, 3, 5), (2, 3, 5, 7),
         (2, 3, 5, 7, 11), (3, 7), (5, 11, 13), (17, 19)]


def factor(n):
    fs = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            a = 0
            while n % p == 0:
                n //= p
                a += 1
            fs.append((p, a))
        p += 1
    if n > 1:
        fs.append((n, 1))
    return fs


def smooth(n, ps):
    if n == 0:
        return None
    es = []
    for p in ps:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        es.append(e)
    return tuple(es) if n == 1 else None


@lru_cache(None)
def vectors(m, s):
    if m == 0:
        return ((),)
    return tuple((a,) + es for a in range(s + 1)
                 for es in vectors(m - 1, s - a))


def smooth_squares():
    cases = residues = exponent_pairs = roots_checked = 0
    minimum_margin = None
    for n in range(3, 1024, 2):
        fs = factor(n)
        qrs = [{x * x % q for x in range(1, q)} for q, a in fs]
        for ps in BASES:
            if any(n % p == 0 for p in ps):
                continue
            m = len(ps)
            fibers = defaultdict(list)
            for x in range(1, n):
                y = x * x % n
                if smooth(y, ps) is not None:
                    fibers[y].append(x)
            residues += n - 1
            count = sum(map(len, fibers.values()))
            for r in range(0, n.bit_length() + 1, 2):
                if ps[-1] ** r > n:
                    break
                s = r // 2
                halves = vectors(m, s)
                assert len(halves) == comb(m + s, s)
                labels = {}
                counts = Counter()
                for es in halves:
                    h = prod(p ** e for p, e in zip(ps, es))
                    a = tuple(h % q in qr for (q, _), qr in zip(fs, qrs))
                    labels[es] = a
                    counts[a] += 1
                multiplicities = Counter()
                for es, et in product(halves, repeat=2):
                    exponent_pairs += 1
                    if labels[es] == labels[et]:
                        multiplicities[tuple(e + f for e, f in zip(es, et))] += 1
                assert sum(multiplicities.values()) == sum(a * a for a in counts.values())
                assert max(multiplicities.values()) <= comb(r, s)
                for es in multiplicities:
                    h = prod(p ** e for p, e in zip(ps, es))
                    assert 1 <= h < n
                    assert len(fibers[h]) == 2 ** len(fs)
                    roots_checked += len(fibers[h])
                # Independent direct count versus the complete combinatorial chain.
                ss = sum(a * a for a in counts.values())
                assert count * comb(r, s) >= 2 ** len(fs) * ss
                assert 2 ** len(fs) * ss >= len(halves) ** 2
                assert len(halves) * factorial(s) >= m ** s
                assert count * factorial(r) >= m ** r
                margin = Fraction(count * factorial(r), m ** r)
                minimum_margin = margin if minimum_margin is None else min(margin, minimum_margin)
                cases += 1
    return dict(cases=cases, direct_residues=residues,
                exponent_pairs=exponent_pairs, crt_roots_checked=roots_checked,
                smallest_direct_to_claimed_count_ratio=str(minimum_margin),
                n_range='all odd 3..1023', bases=BASES)


def normalized_elimination():
    instances = fibers_checked = roots_checked = merges = nontrivial = 0
    for n in range(15, 512, 2):
        d = len(factor(n))
        if d < 2:
            continue
        for ps in BASES:
            if any(n % p == 0 for p in ps):
                continue
            inv = [pow(p, -1, n) for p in ps]
            fibers = defaultdict(list)
            exponents = {}
            for x in range(1, n):
                v = x * x % n
                es = smooth(v, ps)
                if es is not None:
                    fibers[v].append(x)
                    exponents[v] = es
            table = {}

            def norm(x, es):
                z = x * prod(pow(p, e // 2, n) for p, e in zip(inv, es)) % n
                bits = sum((e % 2) << i for i, e in enumerate(es))
                return z, bits

            def reduce(z, bits):
                nonlocal merges
                while bits:
                    j = bits.bit_length() - 1
                    if j not in table:
                        break
                    w, other = table[j]
                    overlap = bits & other
                    z = z * w * prod(inv[i] for i in range(len(ps)) if overlap >> i & 1) % n
                    bits ^= other
                    merges += 1
                    assert z * z % n == prod(ps[i] for i in range(len(ps)) if bits >> i & 1) % n
                return z, bits

            # Fixed deterministic history spanning the parity vectors present.
            for v in sorted(fibers):
                z, bits = reduce(*norm(fibers[v][0], exponents[v]))
                if bits:
                    table[bits.bit_length() - 1] = z, bits
            for v, xs in fibers.items():
                zs = []
                for x in xs:
                    z, bits = reduce(*norm(x, exponents[v]))
                    assert bits == 0 and z * z % n == 1
                    zs.append(z)
                    if z not in (1, n - 1):
                        g = gcd(z - 1, n)
                        assert 1 < g < n and n % g == 0
                        nontrivial += 1
                assert len(zs) == len(set(zs)) == 2 ** d
                assert sum(z in (1, n - 1) for z in zs) == 2
                fibers_checked += 1
                roots_checked += len(zs)
            instances += 1
    return dict(instances=instances, conditional_fibers=fibers_checked,
                roots=roots_checked, row_merges=merges,
                nontrivial_gcds=nontrivial,
                scope='Fixed complete parity histories; all fresh roots per square, no Monte Carlo.')


def binomial_tails():
    cases = 0
    maximum_ratio = Fraction(0)
    for m in range(1, 25):
        for M in (4 * m, 4 * m + 1, 6 * m, 8 * m + 3):
            for j in range(5):
                p = Fraction(4 * m, M) + Fraction(j, 4) * (1 - Fraction(4 * m, M))
                assert M * p >= 4 * m
                tail = sum(Fraction(comb(M, k)) * p ** k * (1 - p) ** (M - k)
                           for k in range(2 * m + 1))
                # Markov applied to 2^-Y, entirely rational; no floating-point exp.
                mgf = 4 ** m * (1 - p / 2) ** M
                assert tail <= mgf
                # 3/5 < exp(-1/2); this is an additional finite check, not the proof.
                assert tail <= Fraction(3, 5) ** m
                maximum_ratio = max(maximum_ratio, tail / mgf)
                cases += 1
    return dict(cases=cases, m_range=[1, 24], exact_rational=True,
                largest_tail_to_markov_ratio=str(maximum_ratio))


def main():
    data = json.loads(OUT.read_text()) if OUT.exists() else {
        'scope': 'Independent finite checks; general proofs in notes/factoring-dixon.md',
        'pid': os.getpid(), 'checkpoints': {}}
    for name, fn in [('smooth_squares', smooth_squares),
                     ('normalized_elimination', normalized_elimination),
                     ('binomial_tails', binomial_tails)]:
        if name in data['checkpoints']:
            print('REUSE', name, flush=True)
            continue
        started = time.monotonic()
        result = fn()
        result.update(passed=True, seconds=time.monotonic() - started)
        data['checkpoints'][name] = result
        OUT.write_text(json.dumps(data, indent=2) + '\n')
        print(name, json.dumps(result), flush=True)
    data['passed'] = True
    OUT.write_text(json.dumps(data, indent=2) + '\n')
    print('ALL PASSED', flush=True)


if __name__ == '__main__':
    main()
