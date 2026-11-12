#!/usr/bin/env python3
"""DLX32: independently enumerate row subsets and verify all five claims."""
from collections import Counter
from datetime import datetime, timezone
from itertools import combinations
import json

from dlx1_audit_tools import ROOT, sha, input_text, run, decode_rows

OUT = ROOT / 'results/dlx_structure'


def subsets(rows, primary):
    solutions = set()
    for bits in range(1 << len(rows)):
        covered = 0
        for i, row in enumerate(rows):
            if bits >> i & 1:
                if row & covered:
                    break
                covered |= row
        else:
            if covered & primary == primary:
                solutions.add(bits)
    return solutions


def all_claims(rows, primary, solutions):
    projections = [row & primary for row in rows]
    assert all(projections)
    uniform = len(set(p.bit_count() for p in projections)) <= 1
    quasi = False
    q = primary
    while q:
        degrees = {(row & q).bit_count() for row in rows}
        if len(degrees) == 1 and 0 not in degrees:
            quasi = True
        q = (q-1) & primary
    distances = Counter()
    for left, right in combinations(solutions, 2):
        only_left = left & ~right
        only_right = right & ~left
        distance = (left ^ right).bit_count()
        assert distance != 1
        if distance == 2:
            assert only_left.bit_count() == only_right.bit_count() == 1
            a = only_left.bit_length()-1
            b = only_right.bit_length()-1
            assert projections[a] == projections[b]
        if distance == 3:
            if only_left.bit_count() == 2:
                only_left, only_right = only_right, only_left
            assert only_left.bit_count() == 1 and only_right.bit_count() == 2
            a = only_left.bit_length()-1
            b, c = [i for i in range(len(rows)) if only_right >> i & 1]
            assert projections[a] == projections[b] | projections[c]
            assert not projections[b] & projections[c]
        if uniform or quasi:
            assert distance % 2 == 0
        distances[distance] += 1
    return distances, uniform, quasi


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    examples = []
    for label, names, rows, nprimary, expected_distance in [
        ('distance2', ['a', 'x', 'y'], [3, 5], 1, 2),
        ('distance3', ['a', 'b'], [3, 1, 2], 2, 3),
        ('f109-total-uniform', ['a', 'b', 'x', 'y'], [3, 5, 10], 2, 3),
    ]:
        primary = (1 << nprimary)-1
        expected = subsets(rows, primary)
        assert len(expected) == 2
        assert len({(a ^ b).bit_count() for a, b in combinations(expected, 2)}) == 1
        assert next((a ^ b).bit_count() for a, b in combinations(expected, 2)) == expected_distance
        option_lists = [tuple(i+1 for i in range(len(names)) if row >> i & 1) for row in rows]
        stats, output = run(OUT, label, input_text(names, option_lists, nprimary), models=True)
        (OUT / f'{label}.models').write_text(output)
        actual = decode_rows(output, names, option_lists)
        assert actual == {tuple(i for i in range(len(rows)) if bits >> i & 1) for bits in expected}
        assert stats['solutions'] == 2
        examples.append(dict(primary=names[:nprimary], secondary=names[nprimary:],
                             options=[[names[i] for i in range(len(names)) if row >> i & 1] for row in rows],
                             solution_vectors=[[(bits >> i) & 1 for i in range(len(rows))] for bits in sorted(expected)],
                             distance=expected_distance, **stats))
    counts = Counter()
    distances = Counter()
    for n in range(1, 5):
        for nprimary in range(1, n+1):
            primary = (1 << nprimary)-1
            universe = [row for row in range(1, 1 << n) if row & primary]
            for size in range(min(5, len(universe))+1):
                for rows in combinations(universe, size):
                    solutions = subsets(rows, primary)
                    found, uniform, quasi = all_claims(rows, primary, solutions)
                    counts['problems'] += 1
                    counts['solutions'] += len(solutions)
                    counts['uniform_primary_problems'] += uniform
                    counts['quasi_uniform_problems'] += quasi
                    distances.update(found)
    # Repeated options are distinct coordinates, as explicitly allowed in DLX30/39.
    for rows in [(1, 1), (3, 3, 1, 2), (3, 5, 10, 3)]:
        primary = 1 if rows == (1, 1) else 3
        all_claims(rows, primary, subsets(rows, primary))
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), examples=examples, exhaustive=dict(counts),
                  solution_pair_distances=dict(sorted(distances.items())),
                  duplicate_option_cases=3,
                  finding='F109: equal total option sizes do not imply even distance; equal PRIMARY sizes do.',
                  scope='All families of up to five distinct options on up to four items, '
                        'every nonempty primary prefix; exact subset enumeration. General proofs in notes.')
    (OUT / 'diversity.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'examples'}, indent=2))


if __name__ == '__main__':
    main()
