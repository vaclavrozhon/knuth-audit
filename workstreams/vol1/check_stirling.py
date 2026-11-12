"""Exact independent arithmetic checks for the Stirling audit.

Proofs and analytic convergence arguments are in notes/stirling-*.md.
This script checks table transcription, all finite identity families, and
the first six coefficient polynomials used in the analytic proof.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
counts = Counter()


def check(label, left, right):
    assert left == right, (label, left, right)
    counts[label] += 1


def choose(r, k):
    if k < 0:
        return 0
    a = Q(1)
    for j in range(k):
        a *= Q(r - j, j + 1)
    assert a.denominator == 1
    return a.numerator


def make_table(kind, size):
    tab = [[0] * (size + 1) for _ in range(size + 1)]
    tab[0][0] = 1
    for n in range(1, size + 1):
        for k in range(1, n + 1):
            multiplier = n - 1 if kind == 'c' else k
            tab[n][k] = multiplier * tab[n - 1][k] + tab[n - 1][k - 1]
    return tab


C = make_table('c', 30)
S = make_table('S', 30)


def entry(tab, n, k):
    return tab[n][k] if 0 <= k <= n else 0


literal_c = [
    [1], [0, 1], [0, 1, 1], [0, 2, 3, 1], [0, 6, 11, 6, 1],
    [0, 24, 50, 35, 10, 1], [0, 120, 274, 225, 85, 15, 1],
    [0, 720, 1764, 1624, 735, 175, 21, 1],
    [0, 5040, 13068, 13132, 6769, 1960, 322, 28, 1],
]
literal_s = [
    [1], [0, 1], [0, 1, 1], [0, 1, 3, 1], [0, 1, 7, 6, 1],
    [0, 1, 15, 25, 10, 1], [0, 1, 31, 90, 65, 15, 1],
    [0, 1, 63, 301, 350, 140, 21, 1],
    [0, 1, 127, 966, 1701, 1050, 266, 28, 1],
]
for tab, literal in [(C, literal_c), (S, literal_s)]:
    for n, row in enumerate(literal):
        check('table_2_rows', tab[n][:n + 1], row)

for n in range(25):
    check('row_sums', sum(C[n]), factorial(n))
    check('alternating_row_sums', sum((-1)**k * C[n][k] for k in range(n + 1)),
          int(n == 0) - int(n == 1))
    for m in range(n + 3):
        for a, b in [(C, S), (S, C)]:
            value = sum(entry(a, n, k) * entry(b, k, m) * (-1)**(n - k)
                        for k in range(n + 1))
            check('eq47_both_inverses', value, int(n == m))
        check('eq51_forward', sum(entry(C, n, k) * choose(k, m) for k in range(n + 1)),
              entry(C, n + 1, m + 1))
        check('eq51_inverse', sum(entry(C, n + 1, k + 1) * choose(k, m) * (-1)**(k + m)
                                  for k in range(n + 1)), entry(C, n, m))
        check('eq52_forward', sum(choose(n, k) * entry(S, k, m) for k in range(n + 1)),
              entry(S, n + 1, m + 1))
        check('eq52_inverse', sum(choose(n, k) * entry(S, k + 1, m + 1) * (-1)**(n - k)
                                  for k in range(n + 1)), entry(S, n, m))
        check('eq53_surjections', sum(choose(m, k) * (-1)**(m - k) * k**n
                                      for k in range(m + 1)), factorial(m) * entry(S, n, m))
        check('eq55', sum(entry(S, n + 1, k + 1) * entry(C, k, m) * (-1)**(k + m)
                           for k in range(n + 1)), choose(n, m))
        check('eq56_first', sum(entry(C, k, m) * (factorial(n) // factorial(k))
                                for k in range(n + 1)), entry(C, n + 1, m + 1))
        check('eq56_second', sum(entry(S, k, m) * (m + 1)**(n - k)
                                 for k in range(n + 1)), entry(S, n + 1, m + 1))
        check('exercise61', sum(entry(C, n + 1, k + 1) * entry(S, k, m) * (-1)**(k + m)
                                for k in range(n + 1)),
              factorial(n) // factorial(m) if n >= m else 0)
    for d in range(9):
        for a, b in [(C, S), (S, C)]:
            value = sum(choose(d - n, d + k) * choose(d + n, n + k) * entry(a, d + k, k)
                        for k in range(d + 1))
            check('eq54_both', value, entry(b, n, n - d))

x, p = sp.symbols('x p')
P, R = [], []
for d in range(7):
    pc = sp.interpolate([(n, entry(C, n, n - d)) for n in range(2*d + 1)], x)
    ps = sp.interpolate([(n, entry(S, n, n - d)) for n in range(2*d + 1)], x)
    P.append(sp.expand(pc))
    R.append(sp.expand(ps))
    check('polynomial_degrees', sp.degree(pc, x), 2*d)
    check('polynomial_degrees', sp.degree(ps, x), 2*d)
    check('polynomial_duality', sp.expand(ps - pc.subs(x, d - x)), 0)
    check('polynomial_leading_coefficients', sp.Poly(pc, x).LC(), sp.Rational(1, 2**d*factorial(d)))
    check('polynomial_leading_coefficients', sp.Poly(ps, x).LC(), sp.Rational(1, 2**d*factorial(d)))
    if d:
        check('polynomial_difference_c', sp.expand(pc.subs(x, x+1) - pc - x*P[d-1]), 0)
        check('polynomial_difference_s', sp.expand(ps.subs(x, x+1) - ps - (x+1-d)*R[d-1]), 0)


def symbolic_choose(z, k):
    return sp.Rational(1, factorial(k)) * sp.prod(z-j for j in range(k))


for d, coeff in [(2, [1, 2]), (3, [1, 8, 6])]:
    check('eq57_first', sp.expand(P[d] - sum(a*symbolic_choose(x+j, 2*d)
                                            for j, a in enumerate(coeff))), 0)
    check('eq57_second', sp.expand(R[d] - sum(a*symbolic_choose(x+len(coeff)-1-j, 2*d)
                                             for j, a in enumerate(coeff))), 0)


def multiply(a, b, degree=6):
    return [sp.expand(sum(a[j]*b[k-j] for j in range(k+1))) for k in range(degree+1)]


def power_unit(a, exponent):
    """Coefficient expansion via finite generalized binomial theorem."""
    a = list(a)
    check('unit_series_constant', a[0], 1)
    a[0] = 0
    apow = [sp.Integer(1)] + [sp.Integer(0)]*6
    result = [sp.Integer(0)]*7
    for j in range(7):
        factor = symbolic_choose(exponent, j)
        result = [sp.expand(v + factor*w) for v, w in zip(result, apow)]
        apow = multiply(apow, a)
    return result


log_series = [sp.Rational(1, j+1) for j in range(7)]
a = multiply(power_unit(log_series, p-1), [sp.Integer(1)]*7)
exp_unit = [sp.Rational((-1)**j, factorial(j+1)) for j in range(7)]
h = multiply(power_unit(exp_unit, p-1), [sp.Rational((-1)**j, factorial(j)) for j in range(7)])
for k in range(7):
    rising = sp.prod(p+j for j in range(k))
    check('analytic_coefficient_A4', sp.expand(rising*a[k] - R[k].subs(x, -p)), 0)
    check('analytic_coefficient_A8', sp.expand(rising*h[k] - (-1)**k*P[k].subs(x, -p)), 0)

result = {'status': 'passed', 'utc': datetime.now(timezone.utc).isoformat(),
          'arithmetic': 'integers, Fraction, SymPy exact polynomials',
          'sympy_version': sp.__version__, 'counts': dict(counts),
          'limits': 'Finite checks supplement proofs; do not certify analytic convergence or historical claims.'}
(ROOT/'results/stirling.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
