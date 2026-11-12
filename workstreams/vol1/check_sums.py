"""Exact finite checks supplementing the general proofs of TAOCP 1.2.3-1..35."""
from fractions import Fraction as F
from itertools import product, combinations
from math import prod, isqrt
from pathlib import Path
from random import Random
import json

ROOT = Path(__file__).resolve().parent


def oriented(lo, hi, f):
    if lo <= hi:
        return sum(f(j) for j in range(lo, hi+1))
    return -sum(f(j) for j in range(hi+1, lo))


def homogeneous(xs, degree):
    if degree < 0:
        return 0
    c = [1] + [0]*degree
    for x in xs:
        for k in range(1, degree+1):
            c[k] += x*c[k-1]
    return c[degree]


def main():
    counts = {}
    grid = [F(k, 2) for k in range(-8, 9)]
    total = 0
    for n in range(21):
        for x in grid:
            g = sum(x**j for j in range(n+1))
            t = sum(j*x**j for j in range(n+1))
            if x != 1:
                assert g == (1-x**(n+1))/(1-x)
                assert t == (n*x**(n+2)-(n+1)*x**(n+1)+x)/(x-1)**2
            else:
                assert g == n+1 and t == F(n*(n+1), 2)
            u = sum((n-k)*x**k for k in range(n+1))
            assert (x-1)*u+n+1 == g
            total += 1
    counts['geometric_weighted_and_digit_identities'] = total
    total = negative_roots = 0
    for length in range(1, 7):
        n = length-1
        for a in product(range(-2, 3), repeat=length):
            lower = prod(a[i]*a[j] for i in range(length) for j in range(i+1))
            upper = prod(a[i]*a[j] for i in range(length) for j in range(i, length))
            assert lower == upper == prod(a)**(n+2)
            assert lower*upper == prod(a)**(2*n+4)
            if lower < 0:
                assert isqrt(lower*upper) == -lower
                negative_roots += 1
            s1, s2, s3 = (sum(x**r for x in a) for r in (1, 2, 3))
            double = sum(a[i]*a[j] for i in range(length) for j in range(i+1))
            triple = sum(a[i]*a[j]*a[k] for i in range(length)
                         for j in range(i+1) for k in range(j+1))
            assert 2*double == s1*s1+s2
            assert 6*triple == s1**3+3*s1*s2+2*s3
            total += 1
    counts['signed_triangular_products_and_symmetric_sums'] = total
    counts['square_root_step_negative_witnesses'] = negative_roots
    assert prod([-1, 1])**3 == -1
    total = 0
    for length in range(8):
        for a in product([F(0), F(1, 4), F(1, 2), F(1)], repeat=length):
            assert prod(1-x for x in a) >= 1-sum(a)
            total += 1
    counts['product_inequality'] = total
    for n in range(1, 101):
        assert prod(1-F(1, j*j) for j in range(2, n+1)) == F(n+1, 2*n)
    counts['telescoping_product'] = 100
    total = 0
    for n in range(1, 7):
        for xs in combinations(range(-3, 4), n):
            ds = [prod(x-y for y in xs if x != y) for x in xs]
            for r in range(n+4):
                assert sum(F(x**r, d) for x, d in zip(xs, ds)) == homogeneous(xs, r-n+1)
                total += 1
    counts['lagrange_and_sylvester_identities'] = total
    total = 0
    for n in range(1, 9):
        for m in range(1, n+1):
            for x in grid:
                ans = sum(prod((x+k-r for r in range(1, n+1) if r != m), start=F(1)) /
                          prod(k-r for r in range(1, n+1) if r != k)
                          for k in range(1, n+1))
                assert ans == 1
                total += 1
    counts['exercise_34'] = total
    rng = Random(123003)
    for case in range(1000):
        n = case % 11
        a, b, x, y = [[rng.randrange(-5, 6) for _ in range(n)] for _ in range(4)]
        lhs = sum(a[j]*x[j] for j in range(n))*sum(b[j]*y[j] for j in range(n))
        rhs = sum(a[j]*y[j] for j in range(n))*sum(b[j]*x[j] for j in range(n))
        rhs += sum((a[j]*b[k]-a[k]*b[j])*(x[j]*y[k]-x[k]*y[j])
                   for j in range(n) for k in range(j+1, n))
        assert lhs == rhs
        a.sort(); b.sort()
        assert sum(a)*sum(b) <= n*sum(u*v for u, v in zip(a, b))
    counts['binet_and_monotone_inequality'] = 1000
    total = 0
    f = lambda j: j**3-2*j+1
    for p, q, r in product(range(-5, 6), repeat=3):
        assert oriented(p, q, f)+oriented(q+1, r, f) == oriented(p, r, f)
        total += 1
    for m, n in product(range(-5, 6), repeat=2):
        assert oriented(m, n, lambda j: f(j)-f(j-1)) == f(n)-f(m-1)
    counts['oriented_concatenation'] = total
    counts['oriented_telescoping'] = 121
    result = {'arithmetic': 'Exact integers and fractions; general proofs are in notes/sums-and-products.md.',
              'counts': counts,
              'V1-C0003': {'n': 1, 'a': [-1, 1], 'P1': -1, 'P2': -1, 'sqrt_P1P2': 1},
              'V1-C0004': {'a_j': 'j', 'm': 2, 'n': 0, 'oriented_sum': -1,
                            'set_index_sum_and_2007_answer': 0,
                            'status': 'Editorial interpretation remains candidate.'},
              'infinite_interchange': {'row_sum': -1, 'column_sum': 1,
                                      'evidence': 'General sparse-array proof, not a finite truncation limit test.'}}
    (ROOT/'results/sums.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(counts))


if __name__ == '__main__':
    main()
