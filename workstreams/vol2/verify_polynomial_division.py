#!/usr/bin/env python3
"""Exact validation for TAOCP 2, 4.6.1 D/R/E and exercises 1--10.

Coefficient arrays start with the constant coefficient; [] means zero.
Each completed block is checkpointed and is not rerun by --resume.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd
from pathlib import Path
import argparse
import json
import random
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/polynomial-division.json'


def trim(a, p=None):
    a = [x % p for x in a] if p else list(a)
    while a and not a[-1]:
        a.pop()
    return a


def degree(a):
    return len(a)-1 if a else float('-inf')


def add(a, b, p=None):
    c = [0]*max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return trim(c, p)


def scale(a, c, p=None):
    return trim([x*c for x in a], p)


def mul(a, b, p=None):
    if not a or not b:
        return []
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c, p)


def divide(a, b, p=None):
    assert b
    r = list(a)
    q = [0]*max(0, len(a)-len(b)+1)
    inv = pow(b[-1], -1, p) if p else F(1, b[-1])
    while r and len(r) >= len(b):
        k = len(r)-len(b)
        c = r[-1]*inv
        q[k] = c % p if p else c
        r = add(r, [0]*k+scale(b, -c, p), p)
    return trim(q, p), r


def pseudo(a, b, p=None, optimized=False):
    assert a and b and len(a) >= len(b)
    m, n, leading = len(a)-1, len(b)-1, b[-1]
    r, q = list(a), [0]*(m-n+1)
    if optimized:
        for t in range(m-n):
            r[t] *= leading**(m-n-t)
            if p:
                r[t] %= p
    for k in range(m-n, -1, -1):
        top = r[n+k]
        q[k] = top*leading**k
        for j in range(n+k-1, -1, -1):
            if not optimized or j >= k:
                r[j] = leading*r[j] - (top*b[j-k] if j >= k else 0)
                if p:
                    r[j] %= p
        r[n+k] = 0
    return trim(q, p), trim(r[:n], p)


def primitive(a):
    if not a:
        return 0, []
    c = 0
    for x in a:
        c = gcd(c, x)
    if a[-1] < 0:
        c = -c
    return c, [x//c for x in a]


def generalized_gcd(a, b):
    ca, a = primitive(a)
    cb, b = primitive(b)
    c = gcd(ca, cb)
    if len(a) < len(b):
        a, b = b, a
    while b:
        r = pseudo(a, b)[1]
        a, b = b, primitive(r)[1]
    return scale(a, c)


def extended(a, b, p=None):
    r0, r1 = a, b
    s0, s1, t0, t1 = [1], [], [], [1]
    sequence = [r0, r1]
    while r1:
        q, r = divide(r0, r1, p)
        r0, r1 = r1, r
        s0, s1 = s1, add(s0, scale(mul(q, s1, p), -1, p), p)
        t0, t1 = t1, add(t0, scale(mul(q, t1, p), -1, p), p)
        sequence.append(r)
    inv = pow(r0[-1], -1, p) if p else F(1, r0[-1])
    return scale(r0, inv, p), scale(s0, inv, p), scale(t0, inv, p), sequence


def core():
    rng = random.Random(20261104)
    cases = Counter()
    for modulus in [None, 2, 3, 4, 6, 8, 10, 13]:
        for _ in range(160):
            n = rng.randrange(0, 6)
            m = rng.randrange(n, 9)
            if modulus:
                a = [rng.randrange(modulus) for _ in range(m)]+[rng.randrange(1, modulus)]
                b = [rng.randrange(modulus) for _ in range(n)]+[rng.randrange(1, modulus)]
            else:
                a = [rng.randrange(-9, 10) for _ in range(m)]+[rng.choice([-3, -1, 1, 2, 5])]
                b = [rng.randrange(-9, 10) for _ in range(n)]+[rng.choice([-3, -1, 1, 2, 5])]
            q, r = pseudo(a, b, modulus)
            assert add(mul(q, b, modulus), r, modulus) == scale(a, b[-1]**(m-n+1), modulus)
            assert degree(r) < n
            assert pseudo(a, b, modulus, optimized=True) == (q, r)
            cases[str(modulus)] += 1
            if modulus in [None, 2, 3, 13]:
                qd, rd = divide(a, b, modulus)
                assert add(mul(qd, b, modulus), rd, modulus) == a
                assert degree(rd) < n
            if modulus is None:
                g = generalized_gcd(a, b)
                assert not divide(a, g)[1] and not divide(b, g)[1]
                gr, s, t, _ = extended(a, b)
                assert add(mul(s, a), mul(t, b)) == gr
                assert scale(g, F(1, g[-1])) == gr
    return {'pseudo_cases_by_modulus': dict(cases), 'integer_gcd_cases': 160,
            'methods': 'Pseudo-division identity, rational or field long division, optimized pseudo-division, normalized Bezout gcd certificate.'}


def printed_examples():
    a = [-5, 2, 8, -3, -3, 0, 1, 0, 1]
    b = [21, -9, -4, 0, 5, 0, 3]
    assert pseudo(a, b) == ([-6, 0, 9], [-9, 0, 3, 0, -15])
    expected = [[-9, 0, 3, 0, -15], [2205, -1125, -585], [307500, -233150], [143193869]]
    u, v = a, b
    for wanted in expected:
        r = pseudo(u, v)[1]
        assert r == wanted
        u, v = v, primitive(r)[1]
    rat = extended(a, b)[3]
    wanted_rat = [[F(-1, 3), 0, F(1, 9), 0, F(-5, 9)],
                  [F(441, 25), -9, F(-117, 25)],
                  [F(-102500, 6591), F(233150, 19773)],
                  [F(-1288744821, 543589225)], []]
    assert rat[2:] == wanted_rat
    u, v = trim(a, 13), trim(b, 13)
    expected_mod = [([7, 0, 9], [4, 0, 3, 0, 11]),
                    ([5, 0, 5], [1, 4]), ([5, 6, 5, 6], [12]), ([12, 9], [])]
    for q, r in expected_mod:
        assert divide(u, v, 13) == (q, r)
        u, v = v, r
    a1, b1 = [2, -1, 3, 2, -1, 1, 1], [3, -1, 2, 2]
    assert pseudo(a1, b1) == ([8, -4, 0, 8], [8, 4, 28])
    a2 = [2, 4, 3, 4, 4, 1, 3]
    g, s, t, seq = extended(a2, a2[::-1], 7)
    # Both the printed prose and sequence have 3*x^2. C0192 was a misreading.
    assert g == [6, 4, 3, 1]
    assert divide(a2, g, 7)[1] == []
    assert divide(a2[::-1], g, 7)[1] == []
    assert add(mul(s, a2, 7), mul(t, a2[::-1], 7), 7) == g
    normalized = [scale(r, pow(r[-1], -1, 7), 7)[::-1] if r else [] for r in seq]
    assert normalized == [[1, 5, 6, 6, 1, 6, 3], [1, 2, 5, 2, 2, 4, 5],
                          [1, 5, 6, 2, 3, 4], [1, 3, 4, 6], []]
    a3, b3 = [-1]+[0]*20+[1], [-1]+[0]*12+[1]
    g, v3, u3, _ = extended(a3, b3)
    assert g == [-1, 1]
    assert v3 == [int(i in [0, 3, 6, 8, 11]) for i in range(12)]
    assert u3 == [-int(i in [1, 3, 6, 8, 11, 14, 16, 19]) for i in range(20)]
    assert add(mul(a3, v3), mul(u3, b3)) == [-1, 1]
    # The printed divisibility exception in answer 3 has U,V interchanged.
    assert add(mul([0, 0, 1], [1]), mul([], [0, 1])) != [0, 1]
    g, v, u, _ = extended([0, 0, 1], [0, 1])
    assert (g, u, v) == ([0, 1], [1], [])
    return {'integer_table_rows': 4, 'rational_remainders': 4,
            'mod13_divisions': 4, 'exercises': [1, 2, 3],
            'exercise2': {'correct_gcd': [6, 4, 3, 1], 'printed_gcd': [6, 4, 3, 1],
                          'remainder_first_input_by_printed_gcd': [],
                          'source_review': 'C0192 dismissed: the original already prints coefficient 3.'},
            'bezout_21_13': {'g': [-1, 1], 'U': list(map(int, u3)), 'V': list(map(int, v3))},
            'printed_degenerate_UV_counterexample': {'u': [0, 0, 1], 'v': [0, 1], 'correct_U': [1], 'correct_V': []}}


def statistics():
    rows = []
    count = degree_checks = 0
    for p, max_m in [(2, 5), (3, 4)]:
        polys = {m: [list(c)+[1] for c in product(range(p), repeat=m)] for m in range(max_m+1)}
        for m in range(max_m+1):
            for n in range(m+1):
                paths = Counter()
                totals = [0, 0, 0]
                coprime = 0
                for a in polys[m]:
                    for b in polys[n]:
                        g, v, u, seq = extended(a, b, p)
                        assert add(mul(a, v, p), mul(u, b, p), p) == g
                        ds = tuple(len(r)-1 for r in seq[2:] if r)
                        paths[ds] += 1
                        totals[0] += len(ds)
                        totals[1] += sum(ds)
                        totals[2] += sum((prev-j)*j for prev, j in zip((n,)+ds, ds))
                        coprime += len(g) == 1
                        if m > degree(g) and n > degree(g):
                            d1 = degree(seq[-3])
                            assert degree(u) == m-d1 and degree(v) == n-d1
                            degree_checks += 1
                        count += 1
                size = p**(m+n)
                assert all(c == p**m*(p-1)**len(ds) for ds, c in paths.items())
                expected = [F(n*(p-1), p), F(n*(n-1)*(p-1), 2*p),
                            F(n*(n+1), 2)-F((n+1)*p, p-1)+F(p*p, (p-1)**2)*(1-F(1, p**(n+1)))]
                assert [F(t, size) for t in totals] == expected
                if m == n:
                    assert F(coprime, size) == (F(p-1, p) if n else 1)
                rows.append({'p': p, 'm': m, 'n': n, 'pairs': size,
                             'means': list(map(str, expected)), 'paths': len(paths)})
    return {'pairs': count, 'bezout_degree_checks': degree_checks, 'rows': rows}


def reverse_division():
    rng = random.Random(1701)
    cases = 0
    witness = None
    for _ in range(100):
        n = rng.randrange(1, 7)
        m = rng.randrange(n, 10)
        a = [rng.randrange(1, 10)]+[rng.randrange(-9, 10) for _ in range(m-1)]+[rng.randrange(1, 10)]
        b = [rng.randrange(1, 10)]+[rng.randrange(-9, 10) for _ in range(n-1)]+[rng.randrange(1, 10)]
        qs, rs = divide(a[::-1], b[::-1])
        q = trim((qs+[0]*(m-n+1-len(qs)))[::-1])
        r = trim((rs+[0]*(n-len(rs)))[::-1])
        assert add(mul(b, q), [0]*(m-n+1)+r) == a
        assert degree(r) < n
        cases += 1
    a, b = [1, 1], [1, 2]
    qs, rs = divide(a[::-1], b[::-1])
    assert qs == [1] and rs == [-1]
    assert add(mul(b, qs), [0]+rs) == a
    assert add(mul(b, qs), rs) != a
    witness = {'u': a, 'v': b, 'q': [1], 'r': [-1], 'correct_shift': 1, 'printed_shift': 0}
    return {'cases': cases, 'shift_counterexample': witness}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    data = json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'status': 'in_progress', 'blocks': {}}
    for name, fun in [('core', core), ('printed_examples', printed_examples),
                      ('statistics', statistics), ('reverse_division', reverse_division)]:
        if name in data['blocks']:
            print('REUSE', name, flush=True)
            continue
        start = time.perf_counter()
        value = fun()
        data['blocks'][name] = {'status': 'passed', 'seconds': time.perf_counter()-start, 'result': value}
        OUT.write_text(json.dumps(data, indent=2)+'\n')
        print('PASS', name, data['blocks'][name]['seconds'], flush=True)
    data['status'] = 'passed'
    OUT.write_text(json.dumps(data, indent=2)+'\n')


if __name__ == '__main__':
    main()
