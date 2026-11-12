#!/usr/bin/env python3
"""DLX29's complete printed matrix and exact distributions for DLX31."""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import product
import json
import math

from check_search_trees import construct, immutable_search
from dlx1_audit_tools import ROOT, sha, input_text, run

OUT = ROOT / 'results/dlx_structure'
PRINTED = '''011111000000000
101111000000000
110111000000000
111100000000000
111010000000000
000000011111000
000000101111000
000000110111000
000000111100000
000000111010000
000000111111111
111111000000111
111111111111100
111111111111010'''.splitlines()


def reservoir(lengths):
    distribution = {}
    theta = math.inf
    r = 0
    for i, length in enumerate(lengths):
        if length < theta:
            theta = length
            r = 1
            distribution = {i: F(1)}
        elif length == theta:
            r += 1
            distribution = {j: p * F(r-1, r) for j, p in distribution.items()}
            distribution[i] = F(1, r)
    return distribution


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    leaf = (False, ())
    child = (False, (leaf, leaf, leaf))
    tree = (False, (child, child))
    items, named_rows = construct(tree)
    order = [(a, b, 'leaf') for a in [0, 1] for b in range(3)]
    # Printed order is each child block in full, then the root's three columns.
    order = [c for a in [0, 1] for c in
             ([(a, b, 'leaf') for b in range(3)] +
              [(a, tag) for tag in ['zero', 'one', 'two']])]
    order += [(tag,) for tag in ['zero', 'one', 'two']]
    assert set(order) == set(items) and len(order) == 15
    actual = [''.join(str(int(c in row)) for c in order) for row in named_rows]
    assert actual == PRINTED
    assert immutable_search(order, named_rows) == tree
    rows = [tuple(i+1 for i, bit in enumerate(line) if bit == '1') for line in PRINTED]
    stats, _ = run(OUT, 'answer29-printed', input_text([f'c{i}' for i in range(15)], rows))
    assert stats['solutions'] == 0 and stats['profile'] == [1, 2, 6]

    insertion = []
    distribution = {(): F(1)}
    for n in range(1, 8):
        updated = defaultdict(F)
        for old, p in distribution.items():
            for position in range(n):
                updated[old[:position] + (n,) + old[position:]] += p / n
        distribution = dict(updated)
        assert len(distribution) == math.factorial(n)
        assert set(distribution.values()) == {F(1, math.factorial(n))}
        insertion.append(dict(n=n, permutations=len(distribution), equal_probabilities=True))
    reservoir_cases = 0
    for n in range(1, 8):
        for lengths in product(range(4), repeat=n):
            best = min(lengths)
            indices = [i for i, value in enumerate(lengths) if value == best]
            expected = {i: F(1, len(indices)) for i in indices}
            assert reservoir(lengths) == expected
            reservoir_cases += 1
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), printed_matrix=PRINTED,
                  printed_matrix_statistics=stats, insertion_distributions=insertion,
                  reservoir_cases=reservoir_cases,
                  scope='All 210 printed matrix entries; complete ordered 9-node tree; '
                        'exact, not sampled, probability distributions. General proofs in notes.')
    (OUT / 'randomization.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
