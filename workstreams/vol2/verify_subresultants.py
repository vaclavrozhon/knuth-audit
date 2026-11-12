#!/usr/bin/env python3
"""Exact checks of TAOCP 2, Algorithm C and exercises 11--16,24.

Ascending coefficient arrays. Polynomial recurrence is checked against determinants
of the original inputs, rational Bezout certificates, and coefficient identities.
Successful blocks are durable and --resume does not execute them again.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import prod
from pathlib import Path
import argparse
import json
import random
import time

from verify_polynomial_division import trim, add, mul, scale, divide, pseudo, primitive, extended

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/subresultants.json'


def exact(x):
    x = F(x)
    assert x.denominator == 1
    return x.numerator


def sequence(a, b):
    assert a and b and len(a) >= len(b)
    u, g, h = [None, a, b], [None, 1], [None, 1]
    raw = []
    i = 1
    while True:
        delta = len(u[i])-len(u[i+1])
        g.append(u[i+1][-1])
        h.append(exact(F(h[i])**(1-delta)*g[i+1]**delta))
        q, r = pseudo(u[i], u[i+1])
        assert add(mul(q, u[i+1]), r) == scale(u[i], g[i+1]**(delta+1))
        raw.append(r)
        if not r:
            break
        u.append([exact(F(x, g[i]*h[i]**delta)) for x in r])
        i += 1
    return u, g, h, raw


def det(a):
    """Independent fraction-free Gaussian determinant, with row pivoting."""
    a = [list(r) for r in a]
    n = len(a)
    assert all(len(r) == n for r in a)
    if not n:
        return 1
    sign, previous = 1, 1
    for k in range(n-1):
        pivot = next((j for j in range(k, n) if a[j][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        v = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                z = a[i][j]*v-a[i][k]*a[k][j]
                assert z % previous == 0
                a[i][j] = z//previous
            a[i][k] = 0
        previous = v
    return sign*a[-1][-1]


def shifted_rows(a, b, na, nb):
    rows = [[0]*s+a for s in range(na, -1, -1)]
    rows += [[0]*s+b for s in range(nb, -1, -1)]
    width = max(map(len, rows), default=0)
    return [list(reversed(r+[0]*(width-len(r)))) for r in rows]


def resultant(a, b):
    return det(shifted_rows(a, b, len(b)-2, len(a)-2))


def validate(a, b):
    u, g, h, raw = sequence(a, b)
    n = [None]+[len(x)-1 for x in u[1:]]
    m, v, k = n[1], n[2], len(u)-1
    count = 0
    for j in range(2, k):
        d = n[j]
        mat = shifted_rows(a, b, v-d, m-d)
        size, maxdeg = len(mat), len(mat[0])-1
        for t in range(d):
            minor = [row[:size-1]+[row[maxdeg-t]] for row in mat]
            expected = u[j+1][t] if t < len(u[j+1]) else 0
            assert abs(det(minor)) == abs(expected), (a, b, j, t)
            count += 1
    for j in range(2, k+1):
        d = n[j]
        mat = shifted_rows(a, b, v-d-1, m-d-1)
        size = len(mat)
        assert abs(det([row[:size] for row in mat])) == abs(h[j])
        count += 1
    common, s, t, _ = extended(a, b)
    assert add(mul(a, s), mul(b, t)) == common
    assert scale(u[-1], F(1, u[-1][-1])) == common
    res = resultant(a, b)
    if n[-1] > 0:
        assert res == 0
    else:
        assert abs(res) == abs(h[-1])
        delta = [None]+[n[i]-n[i+1] for i in range(1, k)]
        e = {j: delta[j-1]*prod(1-delta[i] for i in range(j, k)) for j in range(2, k+1)}
        assert abs(prod(F(g[j])**e[j] for j in e)) == abs(res)
    return count, [u, g, h, raw]


def determinant_block():
    rng = random.Random(2026110401)
    a = [-5, 2, 8, -3, -3, 0, 1, 0, 1]
    b = [21, -9, -4, 0, 5, 0, 3]
    count, data = validate(a, b)
    u, g, h, raw = data
    assert u[3:] == [[-9, 0, 3, 0, -15], [-245, 125, 65], [12300, -9326], [260708]]
    assert g[1:5] == [1, 3, -15, 65] and h[1:5] == [1, 9, 25, 169]
    profiles = Counter()
    for _ in range(240):
        n = rng.randrange(1, 7)
        m = rng.randrange(n, 9)
        a = [rng.randrange(-3, 4) for _ in range(m)]+[rng.choice([1, 2, 3])]
        b = [rng.randrange(-3, 4) for _ in range(n)]+[rng.choice([1, 2, 3])]
        if rng.randrange(4) == 0:
            w = [rng.randrange(-2, 3), rng.choice([1, 2])]
            a, b = mul(a, w), mul(b, w)
        c, data = validate(a, b)
        count += c
        profiles[','.join(str(len(x)-1) for x in data[0][1:])] += 1
    return {'input_pairs': 241, 'original_input_minors': count, 'degree_profiles': dict(profiles),
            'printed_sequence': u[1:], 'printed_g': g[1:], 'printed_h': h[1:],
            'printed_raw_remainders': raw}


def scaling_block():
    rng = random.Random(2026110402)
    for _ in range(120):
        n = rng.randrange(1, 6)
        m = rng.randrange(n, 8)
        a = primitive([rng.randrange(-3, 4) for _ in range(m)]+[rng.choice([1, 2, 3])])[1]
        b = primitive([rng.randrange(-3, 4) for _ in range(n)]+[rng.choice([1, 2, 3])])[1]
        w = [1, rng.randrange(-2, 3), rng.choice([1, 2, 3])]
        u, g, h, _ = sequence(a, b)
        U, G, H, _ = sequence(mul(a, w), mul(b, w))
        ell, m, n = w[-1], len(a)-1, len(b)-1
        assert len(U) == len(u)
        for j in range(2, len(u)):
            pj = m+n-2*(len(u[j])-1)
            assert H[j] == ell**pj*h[j]
            if j+1 < len(u):
                assert U[j+1] == scale(mul(w, u[j+1]), ell**(1+pj))
                assert G[j+1] == ell**(2+pj)*g[j+1]
    a, b, w = [1, 1, 0, 1], [1, 0, 1], [0, 1]
    u = sequence(a, b)[0]
    U = sequence(mul(a, w), mul(b, w))[0]
    assert u[3] == [1] and U[3] == [0, 1]
    assert U[3] != mul(w, u[2])
    return {'scaled_sequences': 120, 'C0193': {'u1': a, 'u2': b, 'w': w,
            'actual_U3': U[3], 'printed_U3': mul(w, u[2])}}


def divisibility_block():
    # Boundary example printed in answer14 and a missing valuation-case split.
    q, r = pseudo([1, 0, 0, 1], [1, 2, 4])
    assert r == [18]
    a, b = [0, 0, 9, 6, 1], [4, 8, 2]
    q, r = pseudo(a, b)
    assert q == [-4, 8, 4] and r == [16]
    assert 4 % 8 != 0  # P=2, j=3, a1=4: p^j does not divide a1.
    rng = random.Random(2026110403)
    witnessed = 0
    for _ in range(600):
        n = rng.randrange(2, 6)
        s = rng.randrange(2, 5)
        b = [rng.randrange(-4, 5) for _ in range(n)]+[rng.choice([2, 3, 4])]
        q0 = [rng.randrange(-3, 4) for _ in range(s)]+[1]
        error = [rng.randrange(-5, 6) for _ in range(rng.randrange(1, n))]
        a = add(mul(b, q0), error)
        r = pseudo(a, b)[1]
        assert all(x % b[-1] == 0 for x in r)
        if r:
            t = n-(len(r)-1)-1
            factor = b[-1]**(s*t)
            assert all((r[-1]**t*x) % factor == 0 for x in r)
            witnessed += 1
    return {'degree_gap_cases': 600, 'nonzero_remainders': witnessed,
            'printed_m_equals_n_plus_1_remainder': [18],
            'valuation_counterexample': {'u': [0,0,9,6,1], 'v': [4,8,2],
                'q': [-4,8,4], 'r': [16], 'p': 2, 'j': 3, 'k': 1, 'a1': 4}}


def eval_multi(f, point):
    return sum(c*prod(x**e for x, e in zip(point, powers)) for powers, c in f.items())


def valuation_primitive_block():
    a, b = [0, 0, 1, 11, 10, 2], [1, 4, 8, 2]
    q, r = pseudo(a, b)
    assert primitive(a)[0] == primitive(b)[0] == 1
    assert q == [-4, 8, 8] and r == [4, 8]
    assert add(mul(q, b), r) == scale(a, 8)
    return {'u': a, 'v': b, 'q': q, 'r': r,
            'p': 2, 'j': 3, 'k': 1, 'P': 2, 'a1': 4,
            'conclusion': 'Both inputs primitive; p^j=8 does not divide a1=4.'}


def resultant_notes_block():
    rng = random.Random(2026110405)
    zero_constant = 0
    for _ in range(100):
        n = rng.randrange(1, 5)
        m = rng.randrange(n, 7)
        a = [rng.randrange(-3, 4) for _ in range(m)]+[rng.choice([1,2,3])]
        b = [rng.randrange(-3, 4) for _ in range(n)]+[rng.choice([1,2,3])]
        mat = shifted_rows(a, b, n-1, m-1)
        original = [row[:] for row in mat]
        for i in range(n):
            mat[n-1-i] = [sum(b[j]*original[n-1-i-j][k]
                                    -a[j]*original[n+m-1-i-j][k]
                                    for j in range(n-i)) for k in range(m+n)]
        assert all(not any(row[-n:]) for row in mat[:m])
        assert det([row[:m] for row in mat[:m]]) == det(original)
        zero_constant += b[0] == 0
    # Root-product formula has an independent oracle from explicit integer roots.
    for _ in range(60):
        alpha = [rng.randrange(-5,6) for _ in range(rng.randrange(1,6))]
        beta = [rng.randrange(-5,6) for _ in range(rng.randrange(1,5))]
        ca, cb = rng.choice([1,2,3]), rng.choice([1,2,3])
        a, b = [ca], [cb]
        for r in alpha:
            a = mul(a, [-r, 1])
        for r in beta:
            b = mul(b, [-r, 1])
        assert resultant(a,b) == ca**len(beta)*cb**len(alpha)*prod(x-y for x in alpha for y in beta)
    return {'reduced_determinants': 100, 'zero_b0_cases': zero_constant,
            'root_product_cases': 60}


def growth_block():
    a, b = [1,1,1,1], [-1,-1,1]
    q, r = pseudo(a,b)
    assert q == [2,1] and r == [3,4]
    rng = random.Random(2026110406)
    raw_witness = None
    for trial in range(1000):
        a = [rng.choice([-1,0,1]) for _ in range(4)]+[1]
        b = [rng.choice([-1,0,1]) for _ in range(3)]+[1]
        u, g, h, raw = sequence(a,b)
        bound_squared = 5**3*4**4
        assert max(abs(x) for v in u[1:] for x in v)**2 <= bound_squared
        for i, r in enumerate(raw, start=1):
            if r and max(map(abs,r))**2 > bound_squared:
                raw_witness = {'u': a, 'v': b, 'step_i': i, 'raw_remainder': r,
                    'normalized_sequence': u[1:], 'g': g[1:], 'h': h[1:],
                    'bound_squared': bound_squared, 'trial': trial}
                break
        if raw_witness:
            break
    return {'N_cubed_witness': {'u': [1,1,1,1], 'v': [-1,-1,1],
                               'q': [2,1], 'r': [3,4], 'N': 1},
            'raw_remainder_witness': raw_witness}


def coefficient_path(f, leading=False, sparse=False):
    degrees = []
    while len(next(iter(f))):
        groups = {}
        for powers, c in f.items():
            groups.setdefault(powers[0], {})[powers[1:]] = c
        d = max(groups)
        if sparse and len(groups) == 1:
            d = min(d, 1)
        degrees.append(d)
        k = max(groups) if leading else min(groups, key=lambda i: (len(groups[i]), i))
        f = groups[k]
    return degrees


def grid_block():
    rng = random.Random(2026110404)
    counts = Counter()
    for n in range(1, 5):
        for _ in range(60):
            f = {tuple(rng.randrange(4) for _ in range(n)): rng.choice([-2,-1,1,2])
                 for _ in range(rng.randrange(1, 15))}
            zeros = sum(eval_multi(f, p) == 0 for p in product(range(4), repeat=n))
            for d in [list(map(max, zip(*f))), coefficient_path(f),
                      coefficient_path(f, leading=True), coefficient_path(f, sparse=True)]:
                assert zeros <= 4**n-prod(4-dj for dj in d)
            assert sum(coefficient_path(f, leading=True)) <= max(map(sum, f))
            d = coefficient_path(f, sparse=True)
            assert 2**sum(dj > 1 for dj in d) <= len(f)
            counts[n] += 1
    # f=x+y, choose coefficient of x^0, then y: d1+d2=2 > total degree1.
    f = {(1,0): 1, (0,1): 1}
    assert coefficient_path(f) == [1,1]
    # f=x on {0,1}^2: two zero vectors; denominator in the book gives 1.
    zeros = sum(p[0] == 0 for p in product(range(2), repeat=2))
    assert zeros == 2 and F(zeros,2) > F(1,2) and F(zeros,4) == F(1,2)
    return {'polynomials_by_dimension': dict(counts), 'bounds_per_polynomial': 4,
            'C0194': {'zero_vectors': 2, 'sample_space': 4, 'printed_denominator': 2},
            'C0195': {'polynomial': 'x+y', 'selected_coefficient': 'y',
                      'coordinate_degree_path': [1,1], 'total_degree': 1}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--resume', action='store_true')
    args = ap.parse_args()
    data = json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'blocks': {}}
    for name, fn in [('determinants', determinant_block), ('scaling', scaling_block),
                     ('divisibility', divisibility_block), ('grid', grid_block),
                     ('valuation_primitive', valuation_primitive_block),
                     ('resultant_notes', resultant_notes_block), ('growth', growth_block)]:
        if name in data['blocks']:
            print('REUSE', name, flush=True)
            continue
        start = time.perf_counter()
        result = fn()
        result['seconds'] = time.perf_counter()-start
        data['blocks'][name] = result
        OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')
        print('PASS', name, result['seconds'], flush=True)
    data['status'] = 'passed'
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n')


if __name__ == '__main__':
    main()
