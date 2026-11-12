"""Exact identities and queue histories for TAOCP 1, §2.2.1-12,14.

Decimal ratios are illustrations only; the asymptotic proof is in the notes.
"""
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import json


def falling(x, n):
    result = Fraction(1)
    for j in range(n):
        result *= x-j
    return result


def coefficient_checks():
    cases = 0
    for n in range(1, 65):
        for k in range(n):
            direct = (-1)**n*falling(Fraction(2*k+1, 2), n)/factorial(n)
            m = n-k-1
            gamma_ratio = Fraction(factorial(2*m), 4**m*factorial(m)*factorial(n))
            corrected = falling(Fraction(-1, 2), k+1)*gamma_ratio
            assert direct == corrected
            cases += 1
    # The first-printing factor has the wrong sign already at k=1,n=2.
    direct = falling(Fraction(3, 2), 2)/2
    old = -falling(Fraction(3, 2), 2)*Fraction(1, 2)
    assert direct == Fraction(3, 8) and old == Fraction(-3, 8)
    return dict(exact_cases=cases, first_printing_counterexample=dict(
        k=1, n=2, actual=str(direct), old_expression=str(old)))


def queue_checks(max_insertions, direct_if_empty):
    visited = 0
    complete = Counter()

    def visit(r, s, reference, inserted, removed, operations, costs):
        nonlocal visited
        visited += 1
        assert tuple(reversed(r))+s == reference
        assert all(pushes <= 2 and pops <= 2 for pushes, pops in costs.values())
        assert sum(a+b for a, b in costs.values()) <= 4*inserted
        if not reference:
            complete[inserted] += 1
        if inserted < max_insertions:
            token = inserted+1
            counts = dict(costs, **{})
            counts[token] = (1, 0)
            if direct_if_empty and not r and not s:
                visit((token,), (), reference+(token,), token, removed, operations+'I', counts)
            else:
                visit(r, s+(token,), reference+(token,), token, removed, operations+'I', counts)
        if reference:
            counts = dict(costs)
            if not r:
                r, s = tuple(reversed(s)), ()
                for token in r:
                    a, b = counts[token]
                    counts[token] = a+1, b+1
            token = r[-1]
            assert token == reference[0]
            a, b = counts[token]
            counts[token] = a, b+1
            visit(r[:-1], s, reference[1:], inserted, removed+1, operations+'O', counts)

    visit((), (), (), 0, 0, '', {})
    assert [complete[n] for n in range(max_insertions+1)] == [
        comb(2*n, n)//(n+1) for n in range(max_insertions+1)]
    return dict(max_insertions=max_insertions, prefixes_checked=visited,
                completed_histories_by_size=dict(complete),
                direct_insertion_when_both_empty=direct_if_empty)


def asymptotic_ratios():
    b = [1, 1]
    for n in range(2, 1001):
        numerator = 3*(2*n-3)*b[-1]-(n-3)*b[-2]
        assert numerator % n == 0
        b.append(numerator//n)
    rows = []
    with localcontext() as ctx:
        ctx.prec = 60
        pi = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164')
        sqrt2 = Decimal(2).sqrt()
        for n in (20, 100, 500, 1000):
            common = pi.sqrt()*Decimal(n)*Decimal(n).sqrt()
            a_leading = Decimal(4)**n/common
            b_leading = (sqrt2-1)*(3+2*sqrt2)**n/(Decimal(8).sqrt().sqrt()*common)
            rows.append(dict(n=n,
                catalan_ratio=str(Decimal(comb(2*n, n)//(n+1))/a_leading),
                restricted_deque_ratio=str(Decimal(b[n])/b_leading)))
    return rows


def main():
    result = dict(status='passed', coefficient_identity=coefficient_checks(),
                  queues=[queue_checks(9, option) for option in (False, True)],
                  illustrative_asymptotic_ratios=asymptotic_ratios(),
                  scope='Finite exact checks; asymptotic ratios are not proofs of a limit or an error bound.')
    dest = Path(__file__).resolve().parent/'results/queue-asymptotics.json'
    dest.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
