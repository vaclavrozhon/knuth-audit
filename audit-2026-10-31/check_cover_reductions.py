#!/usr/bin/env python3
"""DLX33-35: exact solution bijections and the complete dimension bound."""
from collections import Counter
from datetime import datetime, timezone
from itertools import combinations
import json
import random

from check_cover_diversity import subsets
from dlx1_audit_tools import ROOT, sha, input_text, run, decode_rows

OUT = ROOT / 'results/dlx_structure'


def immutable(n, rows):
    """MRV recursion without links; output row-coordinate bitsets, duplicates retained."""
    answers = set()

    def visit(uncovered, active, chosen):
        if not uncovered:
            assert chosen not in answers
            answers.add(chosen)
            return
        choices = [[i for i in active if rows[i] >> j & 1]
                   for j in range(n) if uncovered >> j & 1]
        branch = min(choices, key=len)
        for i in branch:
            visit(uncovered & ~rows[i], [k for k in active if not rows[i] & rows[k]],
                  chosen | 1 << i)

    visit((1 << n)-1, list(range(len(rows))), 0)
    return answers


def matsui(n, rows):
    return n+1, [row << 1 for row in rows] + [1, (1 << (n+1))-1]


def split_once(n, rows, j, broken=False):
    order = [j] + [k for k in range(n) if k != j]
    permuted = [sum(((row >> k) & 1) << i for i, k in enumerate(order)) for row in rows]
    t = sum(row & 1 for row in permuted)
    assert t > 3
    out = []
    position = 0
    for row in permuted:
        if row & 1:
            position += 1
            # The first old column becomes position 2 after two columns are prepended.
            newbits = 2 if position <= t//2 else (6 if broken else 4)
            out.append(((row & ~1) << 2) | newbits)
        else:
            out.append(row << 2)
    out += [3, 5]  # printed 110...0 and 101...0, in low-bit-first convention
    return n+2, out


def sums(n, rows):
    return [sum((row >> j) & 1 for row in rows) for j in range(n)]


def potential(n, rows):
    return sum(max(c-3, 0) for c in sums(n, rows))


def at_most_three(n, rows):
    start = potential(n, rows)
    steps = 0
    while True:
        counts = sums(n, rows)
        j = next((j for j, c in enumerate(counts) if c > 3), None)
        if j is None:
            break
        old = potential(n, rows)
        degrees = [row.bit_count() for row in rows]
        n, rows = split_once(n, rows, j)
        assert [row.bit_count() for row in rows] == degrees + [2, 2]
        assert potential(n, rows) == old-1
        steps += 1
    assert steps == start
    return n, rows, steps


def exactly_three(n, rows):
    counts = sums(n, rows)
    assert all(c <= 3 for c in counts)
    x = sum((c < 3) << j for j, c in enumerate(counts))
    y = sum((c < 2) << j for j, c in enumerate(counts))
    z = sum((c < 1) << j for j, c in enumerate(counts))
    result = list(rows) + [x | (6 << n), y | (5 << n), z | (3 << n), 7 << n]
    assert sums(n+3, result) == [3] * (n+3)
    return n+3, result


def check_case(n, rows):
    m = len(rows)
    assert all(0 < row < 1 << n for row in rows)
    expected = subsets(rows, (1 << n)-1)
    assert immutable(n, rows) == expected
    nn, converted = matsui(n, rows)
    added = immutable(nn, converted)
    assert added == {solution | 1 << m for solution in expected} | {1 << (m+1)}
    if n:
        posting = immutable(n, list(rows) + [(1 << n)-1])
        assert posting == expected | {1 << m}
    nn, converted, steps = at_most_three(n, list(rows))
    assert nn == n+2*steps and len(converted) == m+2*steps
    changed = immutable(nn, converted)
    projected = [solution & ((1 << m)-1) for solution in changed]
    assert set(projected) == expected and len(projected) == len(expected)
    final_n, final_rows = exactly_three(nn, converted)
    forced = immutable(final_n, final_rows)
    assert forced == {solution | 1 << (len(final_rows)-1) for solution in changed}
    return len(expected), steps, len(converted), nn


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    counts = Counter()
    # Includes 0x0; nonempty zero-width rows are excluded by the question.
    cases = [(0, ())]
    for n in range(1, 5):
        for m in range(6):
            cases.extend((n, rows) for rows in combinations(range(1, 1 << n), m))
    cases += [(1, (1,) * t) for t in range(1, 21)]
    cases += [(4, tuple(range(1, 16))), (5, (1, 2, 4, 8, 16, 3, 12, 31))]
    rng = random.Random(20261101)
    cases += [(rng.randrange(1, 7), ()) for _ in range(20)]
    for _ in range(100):
        n = rng.randrange(1, 7)
        cases.append((n, tuple(rng.randrange(1, 1 << n) for _ in range(rng.randrange(1, 13)))))
    for n, rows in cases:
        solutions, steps, out_m, out_n = check_case(n, rows)
        counts['cases'] += 1
        counts['original_solutions'] += solutions
        counts['total_splits'] += steps
        counts['max_output_rows'] = max(counts['max_output_rows'], out_m)
        counts['max_output_columns'] = max(counts['max_output_columns'], out_n)
    # Minimal-degree demonstration of the already published 011 -> 001 correction.
    # Four duplicate one-item options are valid distinct row coordinates.
    known = []
    for broken in [True, False]:
        n, rows = split_once(1, [1]*4, 0, broken)
        actual = immutable(n, rows)
        assert len(actual) == (2 if broken else 4)
        known.append(dict(broken=broken, solutions=len(actual)))
    # A distinct-row example is checked additionally by the author's actual DLX1.
    original = (3, [1, 3, 5, 7, 2, 4])
    examples = []
    for label, n, rows in [('reduction-original', *original),
                            ('reduction-broken', *split_once(*original, 0, True)),
                            ('reduction-corrected', *split_once(*original, 0, False))]:
        names = [f'c{j}' for j in range(n)]
        options = [tuple(j+1 for j in range(n) if row >> j & 1) for row in rows]
        stats, output = run(OUT, label, input_text(names, options), models=True)
        (OUT / f'{label}.models').write_text(output)
        actual = decode_rows(output, names, options)
        expected = {tuple(j for j in range(len(rows)) if solution >> j & 1)
                    for solution in immutable(n, rows)}
        assert actual == expected
        examples.append(dict(n=n, row_masks=rows, **stats))
    assert examples[0]['solutions'] == examples[2]['solutions'] == 4
    assert examples[1]['solutions'] == 2
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), independent_subset_sha256=sha(ROOT / 'check_cover_diversity.py'),
                  counts=dict(counts), known_2025_01_02_erratum=known, author_dlx_examples=examples,
                  zero_dimension=dict(matsui_valid=True, posting_empty_row_violates_input_definition=True,
                                      resolution='Use the original construction for 0x0; current replacement needs n>0.'),
                  scope='Every transformed solution projects uniquely to an original solution; '
                        'all generated solutions compared, including duplicates, empty columns and 0x0. '
                        'General bijections and exact truncated-subtraction size bound are proved in notes.')
    (OUT / 'reductions.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'author_dlx_examples'}, indent=2))


if __name__ == '__main__':
    main()
