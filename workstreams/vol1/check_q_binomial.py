"""Exact finite checks supplementing the proofs in notes/q-binomial.md.

The coefficient product is evaluated directly with rational arithmetic;
independent polynomial multiplication checks the finite q-binomial theorem.
No finite experiment is used as a proof of analytic convergence.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from functools import cache
from itertools import product
from math import comb, factorial, prod
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
counts = Counter()


def check(label, left, right):
    assert left == right, (label, left, right)
    counts[label] += 1


@cache
def g(q, r, k):
    if k < 0:
        return Q(0)
    return prod(((1-q**(r-i))/(1-q**(i+1)) for i in range(k)), start=Q(1))


@cache
def qfactorial(q, n):
    assert n >= 0
    return prod((sum((q**i for i in range(j)), Q(0)) for j in range(1, n+1)), start=Q(1))


def parity(k):
    return 1 if k % 2 == 0 else -1


def choose(n, k):
    if k < 0 or n < k:
        return 0
    return comb(n, k)


qs = [Q(1, 2), Q(2), Q(-1, 2)]
for q in qs:
    for r, k in product(range(-4, 9), range(-2, 12)):
        check('recurrence_first', g(q, r, k), g(q, r-1, k)+q**(r-k)*g(q, r-1, k-1))
        check('recurrence_second', g(q, r, k), q**k*g(q, r-1, k)+g(q, r-1, k-1))
        check('upper_negation', g(q, r, k), parity(k)*q**(k*r-k*(k-1)//2)*g(q, k-r-1, k))
    for n in range(15):
        coefficients = [Q(1)]
        for j in range(n):
            coefficients = [coefficients[k] if k < len(coefficients) else Q(0)
                            for k in range(len(coefficients)+1)]
            for k in range(len(coefficients)-1, 0, -1):
                coefficients[k] += q**j * coefficients[k-1]
        check('finite_product_coefficients', coefficients,
              [g(q, n, k)*q**(k*(k-1)//2) for k in range(n+1)])
        for k in range(n+1):
            check('lower_reflection', g(q, n, k), g(q, n, n-k))
            check('reciprocal_q', g(q, n, k), q**(k*(n-k))*g(1/q, n, k))
    for r, s, n in product(range(-3, 7), range(-3, 7), range(-2, 10)):
        check('vandermonde_first',
              sum((g(q, r, k)*g(q, s, n-k)*q**((r-k)*(n-k)) for k in range(n+1)), Q(0)),
              g(q, r+s, n))
        check('vandermonde_second',
              sum((g(q, r, k)*g(q, s, n-k)*q**((s-n+k)*k) for k in range(n+1)), Q(0)),
              g(q, r+s, n))
    for m, n, r, s in product(range(-2, 6), range(-2, 6), range(-2, 6), range(-2, 6)):
        check('pfaff_including_negative_indices',
              sum((g(q, m-r+s, k)*g(q, n+r-s, n-k)*g(q, r+k, m+n)
                   *q**((m-r+s-k)*(n-k)) for k in range(n+1)), Q(0)),
              g(q, r, m)*g(q, s, n))
    for l, m, n in product(range(6), repeat=3):
        check('q_dixon',
              sum((parity(k)*g(q, l+m, l+k)*g(q, m+n, m+k)*g(q, n+l, n+k)
                   *q**((3*k*k-k)//2) for k in range(-min(l, m, n), min(l, m, n)+1)), Q(0)),
              qfactorial(q, l+m+n)/(qfactorial(q, l)*qfactorial(q, m)*qfactorial(q, n)))
        check('ordinary_dixon',
              sum(parity(k)*choose(l+m, l+k)*choose(m+n, m+k)*choose(n+l, n+k)
                  for k in range(-min(l, m, n), min(l, m, n)+1)),
              factorial(l+m+n)//(factorial(l)*factorial(m)*factorial(n)))

# Polynomial coefficients from the recurrence: check positivity, degree,
# and palindromy without evaluating q at numerical points.
triangle = [[(1,)]]
for n in range(1, 17):
    row = []
    for k in range(n+1):
        first = triangle[-1][k] if k < n else ()
        second = triangle[-1][k-1] if k else ()
        coefficients = [0]*(k*(n-k)+1)
        for j, a in enumerate(first):
            coefficients[j] += a
        for j, a in enumerate(second):
            coefficients[j+n-k] += a
        row.append(tuple(coefficients))
        check('polynomial_nonnegative', all(a >= 0 for a in coefficients), True)
        check('polynomial_degree', len(coefficients)-1, k*(n-k))
        check('polynomial_monic', coefficients[-1], 1)
        check('polynomial_palindromic', coefficients, coefficients[::-1])
    triangle.append(row)

# C0006: compare the original product definition with the exact divergent
# summands, and independently multiply the finite product on the right.
q, x = Q(1, 2), Q(3, 4)
for k in range(26):
    check('C0006_exact_terms', g(q, -1, k)*q**(k*(k-1)//2)*x**k, Q(-3, 2)**k)
    finite_product = prod(((1+q**j*x)/(1+q**(j-1)*x) for j in range(k+1)), start=Q(1))
    check('C0006_telescoping_product', finite_product, (1+q**k*x)/(1+x/q))
check('C0006_product_limit', 1/(1+x/q), Q(2, 5))

result = {'status': 'passed', 'utc': datetime.now(timezone.utc).isoformat(),
          'arithmetic': 'integers and Fraction only', 'counts': dict(counts),
          'limits': 'Finite checks supplement universal proofs; C0006 divergence follows from its exact term formula.'}
(ROOT/'results/q-binomial.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
