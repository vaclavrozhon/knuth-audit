#!/usr/bin/env python3
"""DLX41: frontier counting versus independent row search and original DLX1."""
from datetime import datetime, timezone
import json
import time

from check_frontier_cover import count_frontier, OUT
from dlx1_audit_tools import ROOT, input_text, run, sha


def instance(n, bees=False):
    names = ([f'r{i}' for i in range(1, n+1)]
             + [f'c{j}' for j in range(1, n+1)]
             + ([] if bees else [f'a{k}' for k in range(2, 2*n+1)])
             + [f'b{k}' for k in range(1-n, n)])
    ids = {name: j+1 for j, name in enumerate(names)}
    rows = [tuple(ids[name] for name in
                  [f'r{i}', f'c{j}']
                  + ([] if bees else [f'a{i+j}']) + [f'b{i-j}'])
            for i in range(1, n+1) for j in range(1, n+1)]
    masks = [sum(1 << (item-1) for item in row) for row in rows]
    return names, rows, masks, (1 << (2*n))-1


def row_search(n, bees=False):
    """Separate coordinate search: one square per row, no exact-cover database."""
    mask = (1 << n)-1
    def rec(cols, up, down):
        if cols == mask:
            return 1
        choices = mask & ~(cols | down | (0 if bees else up))
        total = 0
        while choices:
            bit = choices & -choices
            choices -= bit
            total += rec(cols | bit, (up | bit) >> 1, (down | bit) << 1)
        return total
    return rec(0, 0, 0)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    cases = []
    for bees in (False, True):
        for n in range(1, 12):
            names, rows, masks, primary = instance(n, bees)
            label = ('bees' if bees else 'queens')+f'-n{n}'
            started = time.monotonic()
            result = count_frontier(masks, primary, verify=False, trace=True)
            result.update(n=n, bees=bees, matrix_columns=len(names), label=label,
                          elapsed_frontier=time.monotonic()-started)
            expected = row_search(n, bees)
            assert result['solutions'] == expected
            result['independent_row_count'] = expected
            assert result['frontier_max'] <= 3*n
            if n == 11:
                original, _ = run(OUT, label+'-dlx1', input_text(names, rows, 2*n))
                assert original['solutions'] == expected
                result['original_dlx1'] = original
            (OUT/(label+'.json')).write_text(json.dumps(result, indent=2)+'\n')
            cases.append({k: v for k, v in result.items() if k != 'trace'})
            print(label, expected, result['peak'], result['peak_after_compression'],
                  result['frontier_max'], flush=True)
    output = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__),
                  frontier_source_sha256=sha(ROOT/'check_frontier_cover.py'), cases=cases,
                  scope='Counts checked independently by row-coordinate search through n=11; '
                        'original unmodified DLX1 checked at n=11. Dictionary operations '
                        'do not reproduce the original randomized binary-tree mem accounting.')
    (OUT/'queens.json').write_text(json.dumps(output, indent=2)+'\n')


if __name__ == '__main__':
    main()
