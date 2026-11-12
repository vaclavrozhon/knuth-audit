#!/usr/bin/env python3
"""Investigate historical DLX36/41 costs using specified item-order variants."""
from datetime import datetime, timezone
import json
import subprocess
import time

from check_dlx_lexicographic_native import BOOK32, decode, queens_input
from check_frontier_queens import instance
from dlx1_audit_tools import ROOT, input_text, run, sha, statistics


def organ_pipe(n):
    return [((n-1-j if j & 1 else n+j) >> 1)+1 for j in range(n)]


def main():
    output = ROOT/'results/frontier_cover'
    cases = []
    for bees in (False, True):
        names, rows, _, _ = instance(11, bees)
        row_names = [[names[i-1] for i in row] for row in rows]
        for trim in (False, True):
            secondary = names[22:]
            if trim:
                secondary = [name for name in secondary
                             if sum(name in row for row in row_names) > 1]
            order = [name for i in organ_pipe(11) for name in (f'r{i}', f'c{i}')]+secondary
            ids = {name: i+1 for i, name in enumerate(order)}
            reordered = [tuple(ids[name] for name in row if name in ids) for row in row_names]
            label = ('bees' if bees else 'queens')+'-n11-organpipe'+('-trim' if trim else '')
            stats, _ = run(output, label, input_text(order, reordered, 22))
            assert stats['solutions'] == (596483 if bees else 2680)
            stats.update(bees=bees, trim_singleton_diagonals=trim)
            cases.append(stats)
    (output/'organ-pipe-costs.json').write_text(json.dumps(dict(
        status='verified', source_sha256=sha(__file__),
        checked_at_utc=datetime.now(timezone.utc).isoformat(), cases=cases), indent=2)+'\n')
    print('n11', [{k: x[k] for k in ('label', 'solutions', 'search_mems', 'nodes')}
                  for x in cases], flush=True)

    output = ROOT/'results/lexicographic'
    build = json.loads((output/'native-build.json').read_text())
    binary = build['binaries']['lex']['path']
    assert sha(binary) == build['binaries']['lex']['sha256']
    data = queens_input(32).splitlines()
    header = data[0].split()
    assert header[64] == '|'
    data[0] = ' '.join(header[:32]+[f'c{i}' for i in organ_pipe(32)]+header[64:])
    data = '\n'.join(data)+'\n'
    label = 'n32-lex-organpipe-columns'
    path = output/(label+'.dlx')
    path.write_text(data)
    command = [binary, 'v129', 'm1', 't1']
    start = time.monotonic()
    result = subprocess.run(command, input=data, text=True, capture_output=True,
                            timeout=900, check=True)
    (output/(label+'.log')).write_text(result.stderr)
    (output/(label+'.models')).write_text(result.stdout)
    assert decode(result.stdout, 32) == [BOOK32]
    stats = statistics(result.stderr)
    stats.update(command=command, input_sha256=sha(path), binary_sha256=sha(binary),
                 source_sha256=sha(__file__), elapsed_seconds=time.monotonic()-start,
                 checked_at_utc=datetime.now(timezone.utc).isoformat(),
                 scope='Same validated LL adaptation; only the trailing column-item priority changes.')
    (output/(label+'.json')).write_text(json.dumps(stats, indent=2)+'\n')
    print('n32', stats, flush=True)


if __name__ == '__main__':
    main()
