#!/usr/bin/env python3
"""Apply answer36 to original DLX1; compare all small solutions and first n32."""
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import time

from dlx1_audit_tools import ROOT, sha, input_text, statistics

OUT = ROOT/'results/lexicographic'
BOOK32 = (1, 3, 5, 2, 4, 9, 11, 13, 15, 6, 18, 24, 26, 30, 25, 31,
          28, 32, 27, 29, 16, 19, 10, 8, 17, 12, 21, 7, 14, 23, 20, 22)


def queens_input(n):
    names = ([f'r{i}' for i in range(1, n+1)] + [f'c{i}' for i in range(1, n+1)]
             + [f'a{i}' for i in range(2, 2*n+1)] + [f'b{i}' for i in range(1-n, n)])
    lookup = {name: i+1 for i, name in enumerate(names)}
    rows = [tuple(lookup[name] for name in (f'r{i}', f'c{j}', f'a{i+j}', f'b{i-j}'))
            for i in range(1, n+1) for j in range(1, n+1)]
    return input_text(names, rows, 2*n)


def queen_oracle(n):
    solutions = []
    def walk(prefix, columns, plus, minus):
        row = len(prefix)+1
        if row > n:
            solutions.append(tuple(prefix))
            return
        for column in range(1, n+1):
            if column not in columns and row+column not in plus and row-column not in minus:
                walk(prefix+[column], columns | {column}, plus | {row+column}, minus | {row-column})
    walk([], set(), set(), set())
    return solutions


def decode(text, n):
    result = []
    q = None
    for line in text.splitlines():
        if re.fullmatch(r'\d+:', line):
            if q is not None:
                assert all(q)
                result.append(tuple(q))
            assert int(line[:-1]) == len(result)+1
            q = [None]*n
        elif line.strip():
            match = re.fullmatch(r'\s*(.*?) \(\d+ of \d+\)', line)
            assert match, line
            words = match[1].split()
            row = next(int(x[1:]) for x in words if x.startswith('r'))
            column = next(int(x[1:]) for x in words if x.startswith('c'))
            assert q[row-1] is None
            q[row-1] = column
            assert set(words) == {f'r{row}', f'c{column}', f'a{row+column}', f'b{row-column}'}
    if q is not None:
        assert all(q)
        result.append(tuple(q))
    assert len(set(result)) == len(result)
    for q in result:
        assert set(q) == set(range(1, n+1))
        assert len({r+c for r, c in enumerate(q, 1)}) == n
        assert len({r-c for r, c in enumerate(q, 1)}) == n
    return result


def execute(binary, n, mode, first=False):
    label = f'n{n}-{mode}'
    data = queens_input(n)
    (OUT/f'{label}.dlx').write_text(data)
    command = [str(binary), 'v129', 'm1'] + (['t1'] if first else [])
    record = dict(status='running', command=command, runner_sha256=sha(__file__),
                  binary_sha256=sha(binary), input_sha256=sha(OUT/f'{label}.dlx'),
                  started_at_utc=datetime.now(timezone.utc).isoformat(), timeout_seconds=900)
    path = OUT/f'{label}-run.json'
    start = time.monotonic()
    with (OUT/f'{label}.dlx').open() as stdin, (OUT/f'{label}.models').open('w') as stdout, (OUT/f'{label}.log').open('w') as stderr:
        proc = subprocess.Popen(command, stdin=stdin, stdout=stdout, stderr=stderr)
        record['pid'] = proc.pid
        path.write_text(json.dumps(record, indent=2)+'\n')
        try:
            ret = proc.wait(timeout=900)
        except subprocess.TimeoutExpired:
            proc.kill(); proc.wait()
            record.update(status='timeout', finished_at_utc=datetime.now(timezone.utc).isoformat())
            path.write_text(json.dumps(record, indent=2)+'\n')
            raise
    record.update(status='finished' if ret == 0 else 'failed', returncode=ret,
                  finished_at_utc=datetime.now(timezone.utc).isoformat(), elapsed_seconds=time.monotonic()-start)
    path.write_text(json.dumps(record, indent=2)+'\n')
    assert ret == 0
    actual = decode((OUT/f'{label}.models').read_text(), n)
    stats = statistics((OUT/f'{label}.log').read_text())
    assert len(actual) == stats['solutions']
    record.update(stats, models_sha256=sha(OUT/f'{label}.models'), log_sha256=sha(OUT/f'{label}.log'))
    path.write_text(json.dumps(record, indent=2)+'\n')
    return record, actual


def main():
    OUT.mkdir(exist_ok=True, parents=True)
    prior = json.loads((ROOT/'results/dancing_links/dlx1-build.json').read_text())
    build = Path(tempfile.mkdtemp(prefix='knuth-vol4b-lex-'))
    sources = {}
    for name in ['dlx1.w', 'gb_flip.w', 'gb_flip.ch', 'boilerplate.w']:
        src = ROOT/prior['sources'][name]['path']
        assert sha(src) == prior['sources'][name]['sha256']
        shutil.copyfile(src, build/name)
        sources[name] = dict(path=str(src.relative_to(ROOT)), sha256=sha(src))
    for name in ['dlx1-lexicographic.ch', 'dlx1-nomrv.ch']:
        shutil.copyfile(ROOT/name, build/name)
        sources[name] = dict(path=name, sha256=sha(ROOT/name))
    commands = [['ctangle', 'gb_flip.w', 'gb_flip.ch']]
    binaries = {}
    for mode, change in [('lex', 'dlx1-lexicographic.ch'), ('first', 'dlx1-nomrv.ch')]:
        commands += [['ctangle', 'dlx1.w', change, f'{mode}.c'],
                     ['cc', '-O2', '-Wno-implicit-int', '-Wno-implicit-function-declaration',
                      f'{mode}.c', 'gb_flip.c', '-o', mode]]
        binaries[mode] = build/mode
    for command in commands:
        result = subprocess.run(command, cwd=build, text=True, capture_output=True)
        assert result.returncode == 0, (command, result.stdout, result.stderr)
    manifest = dict(build_directory=str(build), commands=commands, sources=sources,
                    binaries={k: dict(path=str(p), sha256=sha(p)) for k, p in binaries.items()},
                    scope='Both are audit adaptations of the original DLX1: first changes only '
                          'branch selection; lex adds the answer36 LL mechanism.')
    (OUT/'native-build.json').write_text(json.dumps(manifest, indent=2)+'\n')
    small = []
    for n in range(1, 10):
        expected = queen_oracle(n)
        for mode in binaries:
            stats, actual = execute(binaries[mode], n, mode)
            assert actual == expected, (n, mode)
            small.append(dict(n=n, mode=mode, solutions=len(actual), nodes=stats['nodes']))
    (OUT/'native-small.json').write_text(json.dumps(dict(status='verified', cases=small), indent=2)+'\n')
    large = []
    for mode in binaries:
        stats, actual = execute(binaries[mode], 32, mode, first=True)
        assert actual == [BOOK32]
        large.append(dict(mode=mode, **stats))
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  runner_sha256=sha(__file__), small_complete_sets=small,
                  book32=BOOK32, large=large,
                  scope='Full lexicographic model sequences for n1–9, then first n32 '
                        'with both LL+MRV and first-item-only; every reported placement validated.')
    (OUT/'native.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'small_cases': len(small),
                      'large': [{k: x[k] for k in ('mode', 'solutions', 'search_mems', 'nodes', 'elapsed_seconds')}
                                for x in large]}, indent=2))


if __name__ == '__main__':
    main()
