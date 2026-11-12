"""Exact multivariate checks for TAOCP 1.2.9-23.

Direct index sums are compared with subset polynomials and independent
generating functions. The binomial matrix uses SymPy's characteristic
polynomial, separately from Fibonacci product coefficients.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, prod
from pathlib import Path
from sympy import Matrix
import hashlib
import json

ROOT = Path(__file__).resolve().parent
COUNTS = {}


def check(name, value):
    assert value, name
    COUNTS[name] = COUNTS.get(name, 0)+1


def bc(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def add(a, b, scale=1):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, 0)+scale*v
        if not c[k]:
            del c[k]
    return c


def mul(a, b, degree=None):
    c = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            k = tuple(x+y for x, y in zip(ka, kb))
            if degree is None or sum(k) <= degree:
                c[k] = c.get(k, 0)+va*vb
    return {k: v for k, v in c.items() if v}


def power(a, n, m, degree=None):
    out = {(0,)*m: 1}
    for _ in range(n):
        out = mul(out, a, degree)
    return out


def subset_polynomials(m):
    f, g, h, d = {}, {}, {}, {}
    for bits in product((0, 1), repeat=m):
        if any(bits[i] and bits[i+1] for i in range(m-1)):
            continue
        kept = tuple(1-b for b in bits)
        g[kept] = 1
        if not bits[0]:
            f[kept] = 1
        if not (bits[0] and bits[-1]):
            h[kept] = 1
            d[bits] = (-1)**sum(bits)
    return f, g, h, d


def all_exponents(m, degree):
    if m == 0:
        yield ()
    else:
        for k in range(degree+1):
            for tail in all_exponents(m-1, degree-k):
                yield (k,)+tail


def main():
    for m in range(1, 6):
        f, g, h, _ = subset_polynomials(m)
        zero, z = {(0,)*m: 1}, {(1,)*m: 1}
        s_previous, s_current = {}, zero
        for n in range(5):
            direct_s = {}
            direct_t = [{} for _ in range(n+1)]
            for ks in product(range(n+1), repeat=m):
                coefficient_s = prod(bc(ks[i], n-ks[(i+1) % m]) for i in range(m))
                if coefficient_s:
                    direct_s[ks] = coefficient_s
                chain = prod(bc(ks[i], n-ks[i+1]) for i in range(m-1))
                if chain:
                    for r in range(n+1):
                        coefficient_t = bc(r, n-ks[0])*chain
                        if coefficient_t:
                            direct_t[r][ks] = coefficient_t
            check('cyclic_direct_polynomial_and_recurrence', direct_s == s_current)
            COUNTS['cyclic_coefficients_compared'] = COUNTS.get('cyclic_coefficients_compared', 0)+len(direct_s)
            for r in range(n+1):
                expected = mul(power(f, n-r, m), power(g, r, m))
                check('open_chain_direct_polynomial_and_factorization', direct_t[r] == expected)
                COUNTS['open_chain_coefficients_compared'] = COUNTS.get('open_chain_coefficients_compared', 0)+len(expected)
            s_previous, s_current = s_current, add(mul(h, s_current), mul(z, s_previous), (-1)**(m+1))

    for m in range(1, 8):
        _, _, _, d = subset_polynomials(m)
        degree = 6
        one, z = {(0,)*m: Q(1)}, {(1,)*m: Q(1)}
        w = add(add(one, mul(d, d), -1), z, 4)
        series, w_power = dict(one), dict(one)
        for j in range(1, degree+1):
            w_power = mul(w_power, w, degree)
            series = add(series, w_power, Q(comb(2*j, j), 4**j))
        for ks in all_exponents(m, degree):
            direct = prod(comb(ks[i]+ks[(i+1) % m], ks[i]) for i in range(m))
            check('infinite_cyclic_coefficients_and_square_root', series.get(ks, 0) == direct)

    # One-dimensional specialization of the finite sums, independent matrix power.
    for m in range(1, 9):
        for value in (-4, -1, 0, 1, 2, Q(1, 3)):
            mat = Matrix([[value, 1], [value, 0]])**m
            trace, determinant = mat.trace(), mat.det()
            f, g, h, _ = subset_polynomials(m)
            value_h = sum(coefficient*value**sum(ks) for ks, coefficient in h.items())
            check('equal_variables_matrix_trace', value_h == trace)
            check('equal_variables_matrix_determinant', determinant == (-1)**m*value**m)

    fibs = [0, 1]
    for _ in range(20):
        fibs.append(fibs[-1]+fibs[-2])
    for n in range(1, 17):
        matrix = Matrix(n, n, lambda i, j: bc(i, n-1-j))
        actual = list(reversed(matrix.charpoly().all_coeffs()))
        for k in range(n+1):
            fibonomial = prod((Q(fibs[n-k+j], fibs[j]) for j in range(1, k+1)), start=Q(1))
            target = (-1)**((n-k+1)//2)*fibonomial
            check('right_justified_pascal_characteristic_coefficients', actual[k] == target)

    result = {'status': 'passed', 'counts': COUNTS, 'total_checks_and_compared_coefficients': sum(COUNTS.values()),
              'limits': {'finite_sums': 'All coefficients for 1<=m<=5, 0<=n<=4, 0<=r<=n.',
                         'infinite_series': 'All monomials of total degree <=6, 1<=m<=7.',
                         'equal_variables': '1<=m<=8 and six exact specializations.',
                         'characteristic_polynomial': 'Matrices of size 1 through 16.'},
              'method': 'Exact multivariate coefficient dictionaries, direct index enumeration, subset enumeration, and independent matrix arithmetic.',
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'results/carlitz.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
