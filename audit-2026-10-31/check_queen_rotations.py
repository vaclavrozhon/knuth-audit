#!/usr/bin/env python3
"""DLX24: rotational orbit encoding and the printed symmetry filters."""
from collections import Counter
from datetime import datetime, timezone
from itertools import permutations
import hashlib
import json

from dlx1_audit_tools import ROOT, sha, input_text, run, decode_rows
from spacer_algorithm_x import SpacerX

OUT = ROOT/'results/queen_rotations'
QS = [0, 0, 1, 2, 1, 4, 3, 12, 18, 32, 105, 310, 734, 2006]
QD = [1, 1, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 32, 64]


def valid(points, n):
    return (len(points) == n and len({r for r, c in points}) == n
            and len({c for r, c in points}) == n
            and len({r+c for r, c in points}) == n
            and len({r-c for r, c in points}) == n)


def rotate(points, n, steps=1):
    points = frozenset(points)
    for _ in range(steps):
        points = frozenset((c, n+1-r) for r, c in points)
    return points


def problem(n, turn, rule='none'):
    names = [f'r{i}' for i in range(1, n+1)]+[f'c{j}' for j in range(1, n+1)]
    names += [f'a{s}' for s in range(2, 2*n+1)]+[f'b{d}' for d in range(1-n, n)]
    index = {name: i+1 for i, name in enumerate(names)}
    orbits = set()
    for r in range(1, n+1):
        for c in range(1, n+1):
            orbit = {(r, c)}
            current = frozenset(orbit)
            for _ in range(4//turn-1):
                current = rotate(current, n, turn)
                orbit.update(current)
            # A single orbit may already contain mutually attacking queens.
            if any(len({f(r, c) for r, c in orbit}) != len(orbit)
                   for f in [lambda r,c:r, lambda r,c:c, lambda r,c:r+c, lambda r,c:r-c]):
                continue
            orbits.add(tuple(sorted(orbit)))
    rows, groups, seen = [], [], set()
    for orbit in sorted(orbits):
        row = tuple(index[name] for r, c in orbit
                    for name in [f'r{r}', f'c{c}', f'a{r+c}', f'b{r-c}'])
        assert len(row) == len(set(row))
        rs, cs = {r for r, c in orbit}, {c for r, c in orbit}
        boundary = (n+1)//2
        if rule == 'half-corrected' and any(r == 1 and 2*c > n for r, c in orbit):
            continue
        if rule == 'half-printed-geometric' and any(r == 1 and c >= boundary for r, c in orbit):
            continue
        if rule == 'half-printed-literal' and 1 in rs and any(c >= boundary for c in cs):
            continue
        if rule == 'quarter-printed-geometric' and any(r < boundary and c >= boundary for r, c in orbit):
            continue
        if rule == 'quarter-printed-literal' and any(r < boundary for r in rs) and any(c >= boundary for c in cs):
            continue
        if rule == 'deduplicate':
            key = frozenset(row)
            if key in seen:
                continue
            seen.add(key)
        rows.append(row)
        groups.append(orbit)
    return names, rows, groups


def geometric_models(solutions, groups, n, turn):
    out = set()
    for model in solutions:
        points = [point for r in model for point in groups[r]]
        assert valid(points, n)
        points = frozenset(points)
        assert rotate(points, n, turn) == points
        model = tuple(c for r, c in sorted(points))
        assert model not in out
        out.add(model)
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    small = []
    for n in range(4, 10):
        queens = {p for p in permutations(range(1, n+1))
                  if valid(list(enumerate(p, 1)), n)}
        for turn in [2, 1]:
            expected = {p for p in queens if rotate(enumerate(p, 1), n, turn)
                        == frozenset(enumerate(p, 1))}
            names, rows, groups = problem(n, turn)
            audit = SpacerX(names, rows, 2*n).solve()
            actual = geometric_models(audit.solutions, groups, n, turn)
            assert actual == expected
            small.append(dict(n=n, turn_degrees=90*turn, full_models_equal=True,
                              solutions=len(actual), options=len(rows)))
    # The n4/n5 option counts agree with every orbit in the printed examples.
    assert [len(problem(n, turn)[1]) for n in [4, 5] for turn in [2, 1]] == [4, 2, 5, 3]
    cases = []
    for n in range(4, 18):
        for turn, rule in [(2, 'none'), (2, 'half-corrected'), (1, 'none'), (1, 'deduplicate')]:
            names, rows, groups = problem(n, turn, rule)
            models = turn == 2 or rule == 'deduplicate'
            stats, text = run(OUT, f'n{n}-r{turn*90}-{rule}', input_text(names, rows, 2*n), models=models)
            expected = 4*QS[n-4]+2*QD[n-4] if turn == 2 else 2*QD[n-4]
            divisor = 2 if rule == 'half-corrected' else 2**(n//4) if rule == 'deduplicate' else 1
            assert stats['solutions']*divisor == expected
            item = dict(n=n, turn_degrees=90*turn, rule=rule, divisor=divisor, **stats)
            if models:
                actual = geometric_models(decode_rows(text, names, rows), groups, n, turn)
                assert len(actual) == stats['solutions']
                item.update(every_model_validated=True,
                    model_set_sha256=hashlib.sha256(json.dumps(sorted(actual)).encode()).hexdigest())
            cases.append(item)
    failures = []
    for n in [4, 5, 6, 7, 8]:
        for turn, rules in [(2, ['half-printed-geometric', 'half-printed-literal']),
                            (1, ['quarter-printed-geometric', 'quarter-printed-literal'])]:
            for rule in rules:
                names, rows, groups = problem(n, turn, rule)
                audit = SpacerX(names, rows, 2*n).solve()
                failures.append(dict(n=n, turn_degrees=90*turn, rule=rule,
                    solutions=len(audit.solutions), options=len(rows)))
    assert all(x['solutions'] == 0 for x in failures if x['n'] == 4)
    names, rows, groups = problem(32, 1, 'deduplicate')
    large, text = run(OUT, 'n32-r90-deduplicate', input_text(names, rows, 64), models=True)
    actual = geometric_models(decode_rows(text, names, rows), groups, 32, 1)
    assert len(actual) == large['solutions'] == 1589
    large.update(every_model_validated=True, doubled_symmetric_classes=large['solutions']*2**7,
                 model_set_sha256=hashlib.sha256(json.dumps(sorted(actual)).encode()).hexdigest())
    report = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=sha(__file__), helper_sha256=sha(ROOT/'dlx1_audit_tools.py'),
        small_cases=small, table_cases=cases, printed_filter_cases=failures,
        large_n32=large,
        scope='General orbit and duplicate-row proofs in QUEEN_SYMMETRY_NOTES.md. '
              '12 complete permutation model sets; all half-turn and deduplicated quarter-turn '
              'models for n4..17 individually checked; n32 all1589 reduced models checked. '
              'The Qa row of the printed table needs total queen counts separately. '
              'Printed filters fail on n4 under both literal item-membership and geometric readings.')
    (OUT/'verified.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(status=report['status'], small_cases=len(small), table_cases=len(cases),
                          n4_filter_failures=[x for x in failures if x['n']==4], n32=large), indent=2), flush=True)


if __name__ == '__main__':
    main()
