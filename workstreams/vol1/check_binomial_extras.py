"""Exact supplementary checks for TAOCP 1.2.6-51,53,56,59,63,68.

Proofs are recorded separately. Tests stress signs, negative indices,
fractional upper indices, and the finite boundary cases.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from functools import cache
from itertools import combinations, product
from math import ceil, comb, prod
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent
counts = Counter()


def check(label, left, right):
    assert left == right, (label, left, right)
    counts[label] += 1


@cache
def choose(r, k):
    if k < 0:
        return Q(0)
    return prod((Q(r-j, j+1) for j in range(k)), start=Q(1))


def sign(k):
    return 1 if k % 2 == 0 else -1


def oriented_sum(f, m):
    return sum((f(k) for k in range(m+1)), Q(0)) if m >= -1 else -sum((f(k) for k in range(m+1, 0)), Q(0))


params = [Q(-3), Q(-1, 2), Q(0), Q(1, 2), Q(2)]
for r, s, n, m in product(params, params, range(-3, 10), range(-3, 12)):
    check('exercise53a', oriented_sum(lambda k: choose(r, k)*choose(s, n-k)*(n*r-(r+s)*k), m),
          (m+1)*(n-m)*choose(r, m+1)*choose(s, n-m))
for n, m in product(range(1, 15), range(20)):
    check('exercise53b_n_positive_m_nonnegative',
          sum((-choose(2*k-1, k)*choose(2*n-2*k, n-k)/Q(2*k-1) for k in range(m+1)), Q(0)),
          Q(n-m, 2*n)*choose(2*m, m)*choose(2*n-2*m, n-m)+choose(2*n, n)/2)

for l, m, n, r, s in product(range(-4, 5), range(-2, 7), range(6), params, params):
    check('exercise63_double_sum',
          sum((sign(j+k)*choose(j+k, k+l)*choose(r, j)*choose(n, k)
               *choose(s+n-j-k, m-j) for j in range(m+1) for k in range(n+1)), Q(0)),
          sign(l)*choose(n+r, n+l)*choose(s-r, m-n-l))

# Enumerate tuples directly, independently of the greedy proof.
for d in range(1, 6):
    values = sorted(sum(comb(a, j) for j, a in enumerate(t, 1))
                    for t in combinations(range(11), d))
    check('combinadic_consecutive_unique', values, list(range(comb(11, d))))
triples = sorted((sum(comb(a, j) for j, a in enumerate(t, 1)), ''.join(map(str, t[::-1])))
                 for t in combinations(range(7), 3))
check('combinadic_printed_first_21', [t for n, t in triples[:21]],
      ['210','310','320','321','410','420','421','430','431','432','510',
       '520','521','530','531','532','540','541','542','543','610'])
quadruples = sorted((sum(comb(a, j) for j, a in enumerate(t, 1)), ''.join(map(str, t[::-1])))
                    for t in combinations(range(6), 4))
check('combinadic_printed_first_8_four_places', [t for n, t in quadruples[:8]],
      ['3210','4210','4310','4320','4321','5210','5310','5320'])

tab = [[Q(0)]*25 for _ in range(25)]
tab[0][0] = 1
for n in range(25):
    tab[n][0] = 1
    for k in range(1, 25):
        if n:
            tab[n][k] = tab[n-1][k]+tab[n-1][k-1]+choose(n, k)
    for k in range(25):
        check('exercise59_recurrence', tab[n][k], (n+1)*choose(n, k)-choose(n, k+1))

x, y = sp.symbols('x y')
zs = sp.symbols('z1:5')
for n in range(5):
    polynomial = y**n
    for k in range(1, n+1):
        for indices in combinations(range(n), k):
            w = sum(zs[i] for i in indices)
            polynomial += x*(x+w)**(k-1)*(y-w)**(n-k)
    check('hurwitz_distinct_weights_polynomial', sp.expand(polynomial-(x+y)**n), 0)

for n, p in product(range(21), [Q(-1), Q(-1, 3), Q(0), Q(1, 7), Q(1, 2), Q(4, 5), Q(1), Q(5, 4)]):
    lhs = sum((abs(k-n*p)*choose(n, k)*p**k*(1-p)**(n-k) for k in range(n+1)), Q(0))
    a = ceil(n*p)
    rhs = 2*a*choose(n, a)*p**a*(1-p)**(n+1-a) if 1 <= a <= n and p not in (0, 1) else Q(0)
    check('exercise68_mean_absolute_deviation', lhs, rhs)

result = {'status': 'passed', 'utc': datetime.now(timezone.utc).isoformat(),
          'arithmetic': 'integers, Fraction, SymPy exact polynomials',
          'sympy_version': sp.__version__, 'counts': dict(counts),
          'limits': 'Finite checks supplement the proofs; no claim of universal validity from sampling.'}
(ROOT/'results/binomial-extras.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
