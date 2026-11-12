"""Exact audit of TAOCP 4.6.2: B/N, finite fields, and counting formulas.

Coefficient vectors are ascending, with () for zero. Generic ring arithmetic
is reused from the already checked half-gcd block, without rerunning that block.
Independent oracles: exhaustive trial division, exhaustive vector enumeration,
row elimination, and SymPy factorization. No timings claim asymptotic speed.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
import argparse
import datetime
import json
import os
import random
import time
import warnings

import sympy as sp
from verify_fast_sturm import Ring

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / 'results/berlekamp.json'
DATA = json.loads((ROOT / 'sources/berlekamp-printed-data.json').read_text())
X = sp.Symbol('x')
STATS = Counter()


class Field(Ring):
    def rem(self, a, u):
        return self.div(a, u)[1]

    def power(self, a, k, u):
        b = self.one
        while k:
            if k & 1:
                b = self.rem(self.mul(b, a), u)
            a = self.rem(self.mul(a, a), u)
            k //= 2
        return b

    def gcd(self, a, b):
        while b:
            a, b = b, self.rem(a, b)
        return self.poly([self.ratio(c, a[-1]) for c in a]) if a else ()

    def derivative(self, u):
        return self.poly([k*u[k] for k in range(1, len(u))])

    def frobenius(self, u):
        n = len(u)-1
        rows = []
        for k in range(n):
            a = self.power((0, 1), self.p*k, u)
            rows.append([((a[j] if j < len(a) else 0)-(j == k)) % self.p
                         for j in range(n)])
        return rows


def algorithm_n(a, p, pivot_choices=None):
    """Literal column elimination, including rectangular exercise 14."""
    a = [list(row) for row in a]
    m, n = len(a), len(a[0])
    c = [-1]*n
    basis, snapshots = [], []
    for k in range(m):
        available = [j for j in range(n) if a[k][j] and c[j] < 0]
        if available:
            j = pivot_choices.get(str(k), available[0]) if pivot_choices else available[0]
            assert j in available
            z = -pow(a[k][j], -1, p)
            col = [a[s][j]*z % p for s in range(m)]
            assert all(col[s] == 0 for s in range(k))
            for i in range(n):
                t = a[k][i]
                if i != j:
                    for s in range(m):
                        a[s][i] = (a[s][i] + t*col[s]) % p
            for s in range(m):
                a[s][j] = col[s]
            c[j] = k
            snapshots.append([row[:] for row in a])
        else:
            v = [0]*m
            for j in range(n):
                if c[j] >= 0:
                    v[c[j]] = a[k][j]
            v[k] = 1
            basis.append(v)
        for j in range(n):
            if c[j] >= 0:
                assert all(a[c[j]][i] == (-int(i == j)) % p for i in range(n))
    return basis, snapshots


def rank_rows(a, p):
    """Separate conventional row reduction; does not use Algorithm N."""
    a = [list(row) for row in a]
    if not a:
        return 0
    rank = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[pivot], a[rank] = a[rank], a[pivot]
        inv = pow(a[rank][j], -1, p)
        a[rank] = [v*inv % p for v in a[rank]]
        for i in range(rank+1, len(a)):
            t = a[i][j]
            a[i] = [(v-t*w) % p for v, w in zip(a[i], a[rank])]
        rank += 1
    return rank


def vector_times(v, a, p):
    return tuple(sum(v[i]*a[i][j] for i in range(len(a))) % p
                 for j in range(len(a[0])))


def squarefree_berlekamp(u, f):
    if len(u) <= 2:
        return [u] if len(u) == 2 else []
    basis, _ = algorithm_n(f.frobenius(u), f.p)
    factors = [u]
    for v in basis[1:]:
        out = []
        for w in factors:
            for s in range(f.p):
                g = f.gcd(w, f.sub(tuple(v), (s,)))
                if len(g) > 1:
                    out.append(g)
        factors = out
        if len(factors) == len(basis):
            break
    assert len(factors) == len(basis)
    return factors


def berlekamp(u, f):
    if len(u) <= 1:
        return []
    du = f.derivative(u)
    if not du:
        root = tuple(u[::f.p])
        return berlekamp(root, f)*f.p
    d = f.gcd(u, du)
    if d != (1,):
        q, r = f.div(u, d)
        assert not r
        return berlekamp(d, f) + berlekamp(q, f)
    return squarefree_berlekamp(u, f)


def irreducibles(f, max_degree):
    ans = []
    for n in range(1, max_degree+1):
        for coeffs in product(range(f.p), repeat=n):
            u = coeffs+(1,)
            if all(f.rem(u, v) for v in ans if 2*(len(v)-1) <= n):
                ans.append(u)
    return ans


def trial_factor(u, f, primes):
    ans = []
    for v in primes:
        while len(u) >= len(v):
            q, r = f.div(u, v)
            if r:
                break
            ans.append(v)
            u = q
        if u == (1,):
            break
    if u != (1,):
        ans.append(u)
    return sorted(ans)


def sympy_factor(u, p):
    poly = sp.Poly.from_list(list(reversed(u)), X, modulus=p)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        _, factors = sp.factor_list(poly)
    return sorted(tuple(int(c) % p for c in reversed(v.all_coeffs()))
                  for v, multiplicity in factors for _ in range(multiplicity))


def printed():
    f = Field(13)
    u = f.poly(DATA['u'])
    n = len(u)-1
    a = [1]+[0]*(n-1)
    for k, printed_row in enumerate(DATA['shift_rows_descending']):
        assert list(reversed(a)) == printed_row, k
        assert f.poly(a) == f.power((0, 1), k, u)
        a = [(a[j-1] if j else 0)-a[-1]*u[j] for j in range(n)]
        a = [z % 13 for z in a]
        STATS['shift_rows'] += 1
    qi = f.frobenius(u)
    assert qi == [[(z-(i == j)) % 13 for j, z in enumerate(row)]
                  for i, row in enumerate(DATA['Q'])]
    basis, matrices = algorithm_n(qi, 13, DATA['pivots'])
    assert basis == DATA['basis']
    for k, (actual, expected) in enumerate(zip(matrices, DATA['after_pivots'])):
        assert actual == expected, ('printed matrix', k+1, actual, expected)
    assert len(matrices) == 5
    STATS['printed_matrix_entries'] += 64*7
    for s in range(13):
        assert f.gcd(u, f.sub(tuple(basis[1]), (s,))) == tuple(DATA['first_gcds'].get(str(s), [1]))
        w = tuple(DATA['first_gcds']['0'])
        assert f.gcd(w, f.sub(tuple(basis[2]), (s,))) == tuple(DATA['second_gcds'].get(str(s), [1]))
        STATS['printed_gcds'] += 2
    assert sorted(berlekamp(u, f)) == sorted(map(tuple, DATA['factors'])) == sympy_factor(u, 13)
    for p in [2, 5]:
        f = Field(p)
        u = f.poly(DATA['integer_u'])
        record = DATA[f'p{p}']
        w = u if p == 2 else u[1:]
        key = 'Q_minus_I' if p == 2 else 'Q_minus_I_after_removing_x'
        assert f.frobenius(w) == record[key]
        basis, _ = algorithm_n(record[key], p)
        assert len(basis) == 2
        for v in record['basis']:
            assert not any(vector_times(v, record[key], p))
        assert sorted(berlekamp(u, f)) == sorted(map(tuple, record['factors'])) == sympy_factor(u, p)
        STATS['printed_matrix_entries'] += len(w[:-1])**2
        STATS['complete_printed_factorizations'] += 1
    # Exercise 9: coverage of all nonzero residues and actual inverses.
    x = y = 1
    reciprocals = {}
    for _ in range(100):
        assert x not in reciprocals and x*y % 101 == 1
        reciprocals[x] = y
        x, y = 2*x % 101, 51*y % 101
    assert x == y == 1 and set(reciprocals) == set(range(1, 101))
    STATS['reciprocals'] = 100
    # Exercise 14, constant v: first dependence has k=1, not k>=2.
    basis, _ = algorithm_n([[1, 0], [1, 0], [1, 0]], 2)
    assert basis[0] == [1, 1, 0]
    STATS['constant_minimal_polynomial_witnesses'] = 1


def matrices():
    rng = random.Random(46208)
    cases = []
    for p, n in [(2, 3), (3, 2)]:
        for entries in product(range(p), repeat=n*n):
            cases.append((p, [list(entries[i*n:(i+1)*n]) for i in range(n)]))
    for p in [2, 3, 5, 13, 101]:
        for m, n in [(1, 4), (4, 1), (3, 5), (5, 3), (6, 6), (8, 8)]:
            for _ in range(8):
                cases.append((p, [[rng.randrange(p) for _ in range(n)] for _ in range(m)]))
    for p, a in cases:
        basis, _ = algorithm_n(a, p)
        assert len(basis) == len(a)-rank_rows(a, p)
        assert rank_rows(basis, p) == len(basis)
        assert all(not any(vector_times(v, a, p)) for v in basis)
        if p**len(a) <= 243:
            direct = {v for v in product(range(p), repeat=len(a)) if not any(vector_times(v, a, p))}
            span = {tuple(sum(c*b[j] for c, b in zip(cs, basis)) % p for j in range(len(a)))
                    for cs in product(range(p), repeat=len(basis))}
            assert direct == span
            STATS['exhaustive_kernel_comparisons'] += 1
        STATS['matrices'] += 1


def finite():
    for p, max_degree in [(2, 8), (3, 5), (5, 4), (7, 3)]:
        f = Field(p)
        primes = irreducibles(f, max_degree//2)
        for n in range(1, max_degree+1):
            for i, coeffs in enumerate(product(range(p), repeat=n)):
                u = coeffs+(1,)
                actual = sorted(berlekamp(u, f))
                expected = trial_factor(u, f, primes)
                assert actual == expected, (p, u, actual, expected)
                if i < 5 or i % 61 == 0:
                    assert actual == sympy_factor(u, p)
                    STATS['sympy_factorizations'] += 1
                STATS['monic_polynomials_factored'] += 1


def a_np(n, p):
    return sum(int(sp.mobius(n//d))*p**d for d in sp.divisors(n))//n


def counting():
    histograms = []
    for p, max_degree in [(2, 10), (3, 6), (5, 4), (7, 3)]:
        f = Field(p)
        primes = irreducibles(f, max_degree//2)
        for n in range(max_degree+1):
            hist = Counter()
            has_linear = has_quad = count_linear = count_quad = squarefree = irred = 0
            for coeffs in product(range(p), repeat=n):
                fac = trial_factor(coeffs+(1,), f, primes)
                degrees = [len(v)-1 for v in fac]
                l, q = degrees.count(1), degrees.count(2)
                has_linear += bool(l)
                has_quad += bool(q)
                count_linear += l
                count_quad += q
                squarefree += len(set(fac)) == len(fac)
                irred += len(fac) == 1
                hist[len(fac)] += 1
            total = p**n
            linear_complement = sum(F((-1)**k*comb(p, k), p**k) for k in range(min(p, n)+1))
            aq = p*(p-1)//2
            quadratic_complement = sum(F((-1)**k*comb(aq, k), p**(2*k)) for k in range(min(aq, n//2)+1))
            assert F(has_linear, total) == 1-linear_complement
            assert F(has_quad, total) == 1-quadratic_complement
            assert F(count_linear, total) == F(p, p-1)*(1-F(1, p**n))
            assert F(count_quad, total) == F(p, 2*(p+1))*(1-F(1, p**(2*(n//2))))
            assert squarefree == (p**n-p**(n-1) if n >= 2 else p**n)
            if n:
                assert irred == a_np(n, p)
            # Euler product for the full factor-count distribution, using counts
            # from Möbius inversion, independent of enumeration/trial division.
            coeff = {(0, 0): 1}
            for d in range(1, n+1):
                ad = a_np(d, p)
                out = Counter()
                for (degree, factors), val in coeff.items():
                    for k in range((n-degree)//d+1):
                        out[degree+k*d, factors+k] += val*comb(ad+k-1, k)
                coeff = out
            assert hist == {r: c for (d, r), c in coeff.items() if d == n}
            for w in [1, 2, 4]:
                # Logarithmic derivative recurrence in z for G_p(z,w).
                b = [1]
                for k in range(1, n+1):
                    h = sum(b[k-j]*sum(d*a_np(d, p)*w**(j//d) for d in sp.divisors(j)) for j in range(1, k+1))
                    assert h % k == 0
                    b.append(h//k)
                assert b[n] == sum(c*w**r for r, c in hist.items())
                # Witt symmetry: interchange p and w, but keep z^m positive.
                b2 = [1]
                for k in range(1, n+1):
                    h = sum(b2[k-j]*sum(d*a_np(d, w)*p**(j//d) for d in sp.divisors(j)) for j in range(1, k+1))
                    assert h % k == 0
                    b2.append(h//k)
                assert b2[n] == b[n]
            # Printed exact generating function for the mean.
            mean = sum(F(int(sp.totient(d)), d*k)*F(p**k, p**(d*k))
                       for d in range(1, n+1) for k in range(1, n//d+1))
            assert mean == F(sum(r*c for r, c in hist.items()), total)
            histograms.append({'p':p, 'n':n, 'factor_count_histogram':dict(hist),
                               'has_linear':has_linear, 'has_quadratic':has_quad,
                               'quadratic_factor_count':count_quad, 'total':total})
            STATS['distributions'] += 1
            STATS['enumerated_polynomials'] += total
    # The four monic quadratics over F2 give both short counterexamples.
    assert F(1, 4) != F(3, 4)
    assert F(1, 4) != F(1, 2)*(1-F(1, 4))
    return {'histograms':histograms}


def fields():
    for p in list(sp.primerange(3, 200)):
        p = int(p)
        f = Field(p)
        u = (1, 0, 0, 0, 1)
        a = DATA['quartic_Q_minus_I_by_p_mod_8'][str(p % 8)]
        assert f.frobenius(u) == [[v % p for v in row] for row in a]
        roots = {k:next((s for s in range(p) if s*s % p == k % p), None) for k in [-2, -1, 2]}
        if p % 8 == 1:
            i, s = roots[-1], roots[2]
            t = pow(s, -1, p)
            fac = [f.poly([eps*(1+sgn*i)*t, 1]) for eps in [-1, 1] for sgn in [-1, 1]]
        elif p % 8 == 3:
            fac = [f.poly([-1, roots[-2], 1]), f.poly([-1, -roots[-2], 1])]
        elif p % 8 == 5:
            fac = [f.poly([roots[-1], 0, 1]), f.poly([-roots[-1], 0, 1])]
        else:
            fac = [f.poly([1, roots[2], 1]), f.poly([1, -roots[2], 1])]
        v = (1,)
        for g in fac:
            v = f.mul(v, g)
        assert v == u and sorted(fac) == sympy_factor(u, p)
        STATS['quartic_primes'] += 1
    f = Field(13)
    modulus = (2, 0, 1)  # -2=11 is not a square modulo 13.
    assert all((x*x+2) % 13 for x in range(13))
    orders = Counter()
    for a in product(range(13), repeat=2):
        if not any(a):
            continue
        v = (1,)
        for k in range(1, 169):
            v = f.rem(f.mul(v, f.poly(a)), modulus)
            if v == (1,):
                orders[k] += 1
                break
        else:
            raise AssertionError(a)
    assert orders == {int(k):v for k, v in DATA['orders_F169'].items()}
    STATS['F169_nonzero_elements'] = 168
    # Frobenius divisibility iff degree divides exponent, including f=x.
    for p, max_degree in [(2, 6), (3, 4), (5, 3)]:
        f = Field(p)
        for g in irreducibles(f, max_degree):
            d = len(g)-1
            xp = f.rem((0, 1), g)
            xbar = xp
            for m in range(1, 2*max_degree+1):
                xp = f.power(xp, p, g)
                assert (xp == xbar) == (m % d == 0)
                STATS['frobenius_divisibilities'] += 1


def minimal():
    for p, max_degree in [(2, 5), (3, 3), (5, 2)]:
        f = Field(p)
        for n in range(1, max_degree+1):
            for coeffs in product(range(p), repeat=n):
                u = coeffs+(1,)
                if f.gcd(u, f.derivative(u)) != (1,):
                    continue
                kernel, _ = algorithm_n(f.frobenius(u), p)
                r = len(kernel)
                for choices in product(range(p), repeat=r):
                    v = f.poly([sum(c*b[j] for c, b in zip(choices, kernel))
                                for j in range(n)])
                    powers, a = [], (1,)
                    for k in range(r+1):
                        powers.append(list(a)+[0]*(n-len(a)))
                        dependences, _ = algorithm_n(powers, p)
                        if dependences:
                            w = f.poly(dependences[0])
                            assert len(w)-1 == k
                            break
                        a = f.rem(f.mul(a, v), u)
                    else:
                        raise AssertionError((p, u, v))
                    expected = (1,)
                    for s in range(p):
                        if f.gcd(u, f.sub(v, (s,))) != (1,):
                            expected = f.mul(expected, f.poly([-s, 1]))
                    assert w == expected
                    assert 1 <= k <= min(p, r)
                    assert (k == 1) == (len(v) <= 1)
                    STATS['minimal_polynomials'] += 1
    # Independent symbolic expansion of the printed Swinnerton-Dyer example.
    a, b, c = sp.symbols('a b c')
    expr = sp.prod(X-e1*a-e2*b-e3*c for e1 in [-1, 1]
                   for e2 in [-1, 1] for e3 in [-1, 1]).expand()
    poly = sp.Poly(expr, a, b, c)
    result = 0
    for (i, j, k), coefficient in poly.terms():
        assert i % 2 == j % 2 == k % 2 == 0
        result += coefficient*2**(i//2)*3**(j//2)*(-1)**(k//2)
    assert sp.expand(result) == X**8-16*X**6+88*X**4+192*X**2+144
    STATS['swinnerton_dyer_expansions'] = 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('block', choices=['printed', 'matrices', 'finite', 'counting', 'fields', 'minimal'])
    args = parser.parse_args()
    old = json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert args.block not in old['blocks'], 'Successful block already stored; do not rerun.'
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    begin = time.monotonic()
    extra = globals()[args.block]() or {}
    result = {'status':'passed', 'started_at_utc':started, 'pid':os.getpid(),
              'elapsed_seconds':time.monotonic()-begin, 'stats':dict(STATS), **extra}
    old['blocks'][args.block] = result
    RESULT.write_text(json.dumps(old, indent=2)+'\n')
    print(json.dumps({k:v for k, v in result.items() if k != 'histograms'}), flush=True)


if __name__ == '__main__':
    main()
