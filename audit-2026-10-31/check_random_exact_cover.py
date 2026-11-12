#!/usr/bin/env python3
"""DLX39: exact expectations with repeated options and independent enumeration."""
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import cache
from itertools import product
from math import comb, factorial, prod
import json
import random

from dlx1_audit_tools import ROOT, sha, input_text, run
from spacer_algorithm_x import SpacerX

OUT = ROOT / 'results/random_exact_cover'


@cache
def stirling(n, k):
    if n == k == 0:
        return 1
    if n <= 0 or k <= 0 or k > n:
        return 0
    return k * stirling(n-1, k) + stirling(n-1, k-1)


def covers(rows, n):
    """Enumerate coordinates, keeping equal rows as different coordinates."""
    result = []
    for mask in range(1 << len(rows)):
        used = 0
        for j, row in enumerate(rows):
            if mask >> j & 1:
                if row & used:
                    break
                used |= row
        else:
            if used == (1 << n)-1:
                result.append(mask)
    return result


def dynamic_count(rows, n):
    """Independent subset-sum DP on item masks; no dancing links."""
    counts = {0: 1}
    for row in rows:
        for used, count in list(counts.items()):
            if not used & row:
                counts[used | row] = counts.get(used | row, 0) + count
    return counts.get((1 << n)-1, 0)


def bernoulli_expectation(n, m, p):
    normalizer = 1-(1-p)**n
    return sum(comb(m, k)*factorial(k)*stirling(n, k)
               * (p*(1-p)**(k-1))**n / normalizer**k
               for k in range(1, min(n, m)+1))


def occupancy(N, m, k):
    return Fraction(sum((-1)**j*comb(k, j)*(N-j)**m
                        for j in range(k+1)), N**m)


def uniform_expectations(n, r, m):
    if n % r:
        return Fraction(0), Fraction(0)
    k = n // r
    N = comb(n, r)
    P = factorial(n) // (factorial(k)*factorial(r)**k)
    indexed = Fraction(P*prod(range(m-k+1, m+1)), N**k) if m >= k else Fraction(0)
    geometric = P*occupancy(N, m, k)
    return indexed, geometric


def options(rows, n):
    return [tuple(i+1 for i in range(n) if row >> i & 1) for row in rows]


def decimal_string(q):
    with localcontext() as ctx:
        ctx.prec = 45
        return str(Decimal(q.numerator)/Decimal(q.denominator))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    totals = Counter()
    a_results = []
    for n in range(1, 4):
        for m in range(5):
            sums = [Fraction(0), Fraction(0)]
            masses = [Fraction(0), Fraction(0)]
            ps = [Fraction(1, 3), Fraction(2, 5)]
            probabilities = [{row: p**row.bit_count()*(1-p)**(n-row.bit_count())
                              / (1-(1-p)**n) for row in range(1, 1 << n)} for p in ps]
            for rows in product(range(1, 1 << n), repeat=m):
                count = len(covers(rows, n))
                assert dynamic_count(rows, n) == count
                for j, weights in enumerate(probabilities):
                    probability = prod(weights[row] for row in rows)
                    masses[j] += probability
                    sums[j] += probability*count
                totals['bernoulli_input_matrices'] += 1
            for j, p in enumerate(ps):
                assert masses[j] == 1
                assert sums[j] == bernoulli_expectation(n, m, p)
                a_results.append(dict(n=n, m=m, p=str(p), expectation=str(sums[j])))

    b_results = []
    cases = [(n, r, m) for n in range(1, 5) for r in range(1, n+1) for m in range(5)]
    cases += [(6, 2, 3), (6, 3, 3)]
    for n, r, m in cases:
        universe = [row for row in range(1 << n) if row.bit_count() == r]
        indexed_sum = geometric_sum = 0
        for rows in product(universe, repeat=m):
            solutions = covers(rows, n)
            indexed_sum += len(solutions)
            geometric_sum += len({tuple(sorted(rows[j] for j in range(m) if mask >> j & 1))
                                  for mask in solutions})
            totals['uniform_input_matrices'] += 1
        indexed, geometric = uniform_expectations(n, r, m)
        assert indexed == Fraction(indexed_sum, len(universe)**m)
        assert geometric == Fraction(geometric_sum, len(universe)**m)
        k = n // r
        if n % r == 0:
            # Independent positive Stirling-number expression printed for g.
            N = len(universe)
            positive = Fraction(sum(stirling(m, t)*factorial(t)*comb(N-k, t-k)
                                    for t in range(k, min(m, N)+1)), N**m)
            assert positive == occupancy(N, m, k)
        b_results.append(dict(n=n, r=r, m=m, indexed=str(indexed), geometric=str(geometric)))

    examples = []
    for label, n, rows in [
        ('f110-two-items', 2, [1, 1, 2]),
        ('f110-book-parameters', 100,
         [(1 << 5)-1]*481 + [((1 << 5)-1) << (5*j) for j in range(1, 20)]),
    ]:
        expected = 2 if n == 2 else 481
        names = [f'x{i}' for i in range(1, n+1)]
        opts = options(rows, n)
        stats, _ = run(OUT, label, input_text(names, opts))
        assert stats['solutions'] == expected
        if n == 2:
            literal = SpacerX(names, opts).solve()
            assert literal.solutions == {(0, 2), (1, 2)}
            assert covers(rows, n) == [5, 6]
        # In the large witness the twenty disjoint block types force one choice
        # of every type. Only the first block has multiplicity greater than one.
        assert len(set(rows)) == (2 if n == 2 else 20)
        examples.append(dict(n=n, m=len(rows), indexed_solutions=expected,
                             geometric_solutions=1, **stats))

    # Reproducible experiments with both generators, independently counted by DP.
    experiments = []
    for seed in range(202611010, 202611020):
        rng = random.Random(seed)
        n, m = 12, 36
        for mode in ('bernoulli', 'uniform'):
            rows = []
            rejected = 0
            while len(rows) < m:
                if mode == 'bernoulli':
                    row = sum(1 << j for j in range(n) if rng.randrange(5) == 0)
                else:
                    row = sum(1 << j for j in rng.sample(range(n), 3))
                if row:
                    rows.append(row)
                else:
                    rejected += 1
            expected = dynamic_count(rows, n)
            label = f'{mode}-{seed}'
            stats, _ = run(OUT, label, input_text([f'x{i}' for i in range(n)], options(rows, n)))
            assert stats['solutions'] == expected
            experiments.append(dict(seed=seed, mode=mode, n=n, m=m,
                                    p='1/5' if mode == 'bernoulli' else None,
                                    r=3 if mode == 'uniform' else None,
                                    rejected_empty_rows=rejected,
                                    duplicate_rows=m-len(set(rows)), **stats))

    # Exact large-parameter expectations; Decimal is only used for presentation.
    a_correct = bernoulli_expectation(100, 500, Fraction(1, 20))
    p = Fraction(1, 20)
    a_unconditioned = sum(comb(500, k)*(k*p*(1-p)**(k-1))**100 for k in range(1, 501))
    large = []
    for m in (500, 1000, 1500):
        indexed, geometric = uniform_expectations(100, 5, m)
        assert indexed > geometric
        large.append(dict(n=100, r=5, m=m, indexed=decimal_string(indexed),
                          geometric=decimal_string(geometric),
                          relative_underestimate=decimal_string(1-geometric/indexed)))
    a_decimal = decimal_string(a_correct)
    a_wrong_decimal = decimal_string(a_unconditioned)
    assert round(Decimal(a_decimal), 3) == Decimal('297.041')
    assert round(Decimal(a_wrong_decimal), 2) == Decimal('3736.96')
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__),
                  independent_literal_sha256=sha(ROOT/'spacer_algorithm_x.py'),
                  totals=dict(totals), bernoulli=a_results, uniform=b_results,
                  examples=examples, experiments=experiments,
                  book_bernoulli={'conditioned': a_decimal, 'unconditioned': a_wrong_decimal},
                  book_uniform=large,
                  smallest_expectations={'n': 1, 'r': 1, 'm': 2,
                                         'indexed': '2', 'geometric': '1'},
                  finding='F110: P*g counts distinct geometric partitions, '
                          'not subsets of indexed options when repetitions are allowed.',
                  limits='No reproduction of the book historical random samples or their mem counts; '
                         'seeds and source implementation were not specified.')
    (OUT/'expectations.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('bernoulli', 'uniform', 'experiments', 'examples')}, indent=2))


if __name__ == '__main__':
    main()
