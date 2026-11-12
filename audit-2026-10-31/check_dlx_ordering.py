#!/usr/bin/env python3
"""DLX20--21: bit constructions, exact models, and author-program mems."""
from datetime import datetime, timezone
from itertools import product
from math import comb
import hashlib
import json
import re

from dlx1_audit_tools import ROOT, input_text, run, decode_rows, sha
from spacer_algorithm_x import SpacerX

OUT = ROOT/'results/dlx_ordering'


def pair_lists(m, j):
    a, b = [], []
    t = j
    while t > 0:
        a.append(t)
        t &= t-1
    t = -1-j
    while t > -m:
        b.append(-t)
        t &= t-1
    return a, b


def encoding(m, k):
    names = [f'a{i}' for i in range(1, k+1)]
    names += [f'y{i}_{r}' for i in range(1, k) for r in range(1, m)]
    index = {name: i+1 for i, name in enumerate(names)}
    rows = []
    for i in range(1, k+1):
        for j in range(m):
            a, b = pair_lists(m, j)
            row = [f'a{i}']
            if i > 1:
                row += [f'y{i-1}_{r}' for r in b]
            if i < k:
                row += [f'y{i}_{r}' for r in a]
            rows.append(tuple(index[name] for name in row))
    return names, rows


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    pairs, membership_checks, failures = 0, 0, 0
    for m in range(1, 129):
        sets = [(set(a), set(b)) for a, b in (pair_lists(m, j) for j in range(m))]
        width = (m-1).bit_length()
        for j, (a, b) in enumerate(sets):
            direct_a = {r for r in range(1, m) if r <= j < min(m, r+(r & -r))}
            direct_b = {r for r in range(1, m) if r-(r & -r) <= j < r}
            assert a == direct_a and b == direct_b
            assert len(a) <= width and len(b) <= width and len(a)+len(b) <= width
            if m & (m-1) == 0:
                assert len(a)+len(b) == width
            membership_checks += 1
        for r in range(1, m):
            for side in (0, 1):
                assert sum(r in pair[side] for pair in sets) <= r & -r
        for j in range(m):
            for k in range(m):
                common = sets[j][0] & sets[k][1]
                assert bool(common) == (j > k)
                if j > k:
                    corrected = j & -(1 << ((j & ~k).bit_length()-1))
                    printed = j & -(1 << ((j-k).bit_length()-1))
                    assert corrected in common
                    failures += printed not in common
                pairs += 1
    a6, _ = pair_lists(7, 6)
    _, b3 = pair_lists(7, 3)
    assert set(a6) & set(b3) == {4}
    assert (6 & -(1 << ((6-3).bit_length()-1))) == 6
    example_names, example_rows = encoding(4, 3)
    example = [[example_names[i-1] for i in row] for row in example_rows[4:8]]
    assert example == [['a2', 'y1_1', 'y1_2'], ['a2', 'y1_2', 'y2_1'],
                       ['a2', 'y1_3', 'y2_2'], ['a2', 'y2_3', 'y2_2']]
    cases = []
    for m in range(1, 9):
        for k in range(1, 7):
            names, rows = encoding(m, k)
            expected = {tuple(i*m+j for i, j in enumerate(values))
                        for values in product(range(m), repeat=k)
                        if all(a <= b for a, b in zip(values, values[1:]))}
            assert len(expected) == comb(m+k-1, k)
            audit = SpacerX(names, rows, k).solve()
            assert audit.solutions == expected
            stats, text = run(OUT, f'm{m}-k{k}', input_text(names, rows, k), models=True)
            if k == 1:
                # With one layer all m options are the same singleton {a1}.
                # Their positions distinguish the indexed options.
                printed = re.findall(r'^\s*a1 \((\d+) of (\d+)\)$', text, re.M)
                assert printed == [(str(j+1), str(m)) for j in range(m)]
                assert re.findall(r'^(\d+):$', text, re.M) == [str(j+1) for j in range(m)]
            else:
                assert decode_rows(text, names, rows) == expected
            assert stats['solutions'] == len(expected)
            assert stats['profile'] == [audit.profile[i] for i in range(k+1)]
            cases.append(dict(m=m, k=k, **stats,
                full_model_sets_equal=True,
                model_set_sha256=hashlib.sha256(json.dumps(sorted(expected)).encode()).hexdigest()))
    names, rows = encoding(20, 8)
    large, _ = run(OUT, 'm20-k8', input_text(names, rows, 8))
    assert large['solutions'] == comb(27, 8) == 2220075
    large['mems_per_solution'] = large['search_mems']/large['solutions']
    report = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=sha(__file__), helpers_sha256=sha(ROOT/'dlx1_audit_tools.py'),
        pair_checks=pairs, membership_checks=membership_checks,
        printed_witness_failures=failures,
        known_erratum=dict(date='2026-01-05', page=419, exercise=20,
            counterexample=dict(m=7, j=6, k=3, printed=6, corrected=4, shared=[4])),
        example_m4_internal=example, small_cases=cases, large_case=large,
        scope='General proof in DLX_ENCODINGS_NOTES.md; all pairs for m1..128; '
              '48 complete small model sets against Cartesian products; m20k8 full count and mems. '
              'The larger model set is certified by the encoding bijection and complete enumeration count, '
              'not by storing all 2220075 printed models.')
    (OUT/'verified.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(status=report['status'], pair_checks=pairs,
        small_model_sets=len(cases), large=large), indent=2), flush=True)


if __name__ == '__main__':
    main()
