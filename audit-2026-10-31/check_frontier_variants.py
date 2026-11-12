#!/usr/bin/env python3
"""Independent immutable-map DP; explicitly retain only future-relevant bits."""
from collections import defaultdict
from datetime import datetime, timezone
import json

from check_frontier_cover import count_frontier, OUT
from check_frontier_queens import instance
from dlx1_audit_tools import ROOT, input_text, run, sha


def active_map(rows, primary):
    future = [0]*(len(rows)+1)
    for k in range(len(rows)-1, -1, -1):
        future[k] = future[k+1] | rows[k]
    db = {0: 1}
    trace = []
    for k, row in enumerate(rows):
        before = len(db)
        added = defaultdict(int, db)
        for key, count in db.items():
            if not key & row:
                added[key | row] += count
        must = primary & row & ~future[k+1]
        compressed = defaultdict(int)
        for key, count in added.items():
            if key & must == must:
                compressed[key & future[k+1]] += count
        db = compressed
        trace.append(dict(before=before, after_N3=len(added), after_N4=len(db)))
    assert set(db) <= {0}
    answer = db.get(0, 0) if primary & future[0] == primary else 0
    return answer, trace


def main():
    # A different diagonal direction is a different input order after reflection.
    n = 11
    names = ([f'r{i}' for i in range(1, n+1)] + [f'c{j}' for j in range(1, n+1)]
             + [f'a{k}' for k in range(2, 2*n+1)])
    ids = {name: j+1 for j, name in enumerate(names)}
    rows = [tuple(ids[name] for name in (f'r{i}', f'c{j}', f'a{i+j}'))
            for i in range(1, n+1) for j in range(1, n+1)]
    masks = [sum(1 << (i-1) for i in row) for row in rows]
    primary = (1 << (2*n))-1
    result = count_frontier(masks, primary, verify=False, trace=True)
    result['original_dlx1'], _ = run(OUT, 'bees-sum-n11-dlx1', input_text(names, rows, 2*n))
    assert result['solutions'] == result['original_dlx1']['solutions'] == 596483
    result.update(source_sha256=sha(__file__),
                  description='Only a_(i+j) secondary diagonals, row-major order. '
                              'Reflection of the b_(i-j) model changes the option order.')
    (OUT/'bees-sum-n11.json').write_text(json.dumps(result, indent=2)+'\n')

    comparisons = []
    for label, tested_rows, prim, expected in [
            ('queens-n11', instance(11, False)[2], primary, 2680),
            ('bees-n11', instance(11, True)[2], primary, 596483),
            ('bees-sum-n11', masks, primary, 596483)]:
        literal = json.loads((OUT/(label+'.json')).read_text())
        answer, trace = active_map(tested_rows, prim)
        assert answer == literal['solutions'] == expected
        for actual, reference in zip(trace, literal['trace']):
            assert all(actual[key] == reference[key] for key in actual)
        assert len(trace) == len(literal['trace'])
        comparisons.append(dict(label=label, solutions=answer, prefix_checks=len(trace),
                                peak=max(x['after_N3'] for x in trace),
                                reference_sha256=sha(OUT/(label+'.json'))))

    # Check the explicit general frontier formulas separately from solution counting.
    frontier_cases = []
    for n in range(1, 61):
        names, _, rows, _ = instance(n, False)
        past = 0
        suffix = [0]*(len(rows)+1)
        for k in range(len(rows)-1, -1, -1):
            suffix[k] = suffix[k+1] | rows[k]
        maximum = 0
        for k, row in enumerate(rows):
            f = suffix[k+1]
            nu = ((past & row) | (past & f) | (row & f)).bit_count()
            i, j = k//n+1, k%n+1
            if n >= 2 and i == 1:
                assert nu == 3*j-(j == n)
            if n >= 3 and 2 <= i <= n-1:
                assert nu == 3*n-1+(j in (1, n))
            assert nu <= 3*n
            maximum = max(maximum, nu)
            past |= row
        frontier_cases.append(dict(n=n, max_frontier=maximum, cells=n*n))
    output = dict(status='verified', source_sha256=sha(__file__),
                  checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  immutable_map_comparisons=comparisons, frontier_formulas=frontier_cases,
                  scope='Three complete n11 counts and all 363 database lengths independently checked; '
                        'frontier formulas checked for every square through n=60.')
    (OUT/'independent.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: v for k, v in output.items() if k != 'frontier_formulas'}, indent=2))


if __name__ == '__main__':
    main()
