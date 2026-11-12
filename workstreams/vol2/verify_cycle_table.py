"""Compare SSY's mutable table to the closed table invariant; test boundaries.

Nontermination is proved in the accompanying note, not inferred from a timeout.
"""
from pathlib import Path
from fractions import Fraction
import json

ROOT = Path(__file__).resolve().parent


def value(i, mu, period):
    return i if i < mu else mu + (i - mu) % period


def figure4(mu, period, memory, gap, limit):
    table = []
    b = 1
    searches = []
    for i in range(limit):
        if i % b == 0 and len(table) == memory:
            table = [(j, x) for j, x in table if j % (2 * b) == 0]
            b *= 2
        if i % b == 0:
            table.append((i, value(i, mu, period)))
        n = i + 1
        expected_b = 1 << ((n - 1) // memory).bit_length()
        assert b == expected_b
        # Reconstruct the book's table directly, without using update history.
        expected = [(j, value(j, mu, period)) for j in range(0, n, expected_b)]
        assert table == expected and len(table) <= memory
        if n % (gap * b) < b:
            searches.append(n)
            matches = [j for j, x in table if x == value(n, mu, period)]
            if matches:
                return n, min(matches), searches
    return None, None, searches


def main():
    valid_cases = 0
    for memory in range(2, 13):
        for gap in range(1, memory):
            for mu in range(32):
                for period in range(1, 33):
                    total = mu + period
                    bn = 1 << ((total - 1) // memory).bit_length()
                    bound = total + (2 * gap + 1) * bn
                    n, j, _ = figure4(mu, period, memory, gap, bound)
                    assert n is not None and total <= n < bound
                    assert j >= mu and (n - j) % period == 0
                    if 2 * total >= memory:
                        assert memory * n < (memory + 4 * gap + 2) * total
                    valid_cases += 1
    n, j, searches = figure4(0, 3, 2, 2, 10000)
    assert n is None and searches == [2 ** k for k in range(1, 14)]
    n, j, searches = figure4(0, 1, 2, 3, 10000)
    assert n is None and searches == []
    n, j, searches = figure4(0, 1, 8, 3, 30)
    assert n == 3 and Fraction(8 * n, 8 + 4 * 3 + 2) > 1
    result = dict(
        status='all assertions passed',
        valid_parameter_cases=valid_cases,
        valid_scope='2<=memory<=12, 1<=gap<memory, 0<=mu<=31, 1<=period<=32',
        no_search_example=dict(memory=2, gap=3, mu=0, period=1,
                               finite_trace_steps=10000, searches=0,
                               nontermination_proof='notes/C0002-cycle-table-boundaries.md'),
        endpoint_example=dict(memory=2, gap=2, mu=0, period=3,
                              finite_trace_steps=10000,
                              search_indices=[2 ** k for k in range(1, 14)]),
        early_bound_example=dict(memory=8, gap=3, mu=0, period=1,
                                 stopping_index=3, claimed_lower_bound='12/11'),
    )
    (ROOT / 'results/cycle-table.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
