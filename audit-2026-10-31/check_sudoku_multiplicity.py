#!/usr/bin/env python3
"""DLX51: independent capacity search and an archived unmodified DLX3 build."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import json
import re
import shutil
import subprocess
import tempfile
import time
from dlx1_audit_tools import ROOT, sha, decode_rows
from check_sudoku_basics import UNITS

OUT = ROOT/'results/sudoku_minimal'
TARGET = Counter([1, 2, 3, 4, 5, 6, 7, 7, 9])


def coordinate_solutions(initial):
    board = list(initial)
    need = [[0]+[TARGET[k] for k in range(1, 10)] for _ in range(27)]
    groups = [(v//9, 9+v%9, 18+3*(v//27)+(v%9)//3) for v in range(81)]
    for v, k in enumerate(board):
        if k:
            for group in groups[v]:
                need[group][k] -= 1
                assert need[group][k] >= 0
    solutions, nodes = set(), 0
    def visit():
        nonlocal nodes
        nodes += 1
        best, allowed = None, list(range(10))
        for v, k in enumerate(board):
            if not k:
                choices = [k for k in TARGET if all(need[g][k] for g in groups[v])]
                if len(choices) < len(allowed):
                    best, allowed = v, choices
                if not choices:
                    return
        if best is None:
            assert all(not any(n) for n in need)
            solutions.add(tuple(board))
            return
        for k in allowed:
            board[best] = k
            for g in groups[best]:
                need[g][k] -= 1
            visit()
            for g in groups[best]:
                need[g][k] += 1
        board[best] = 0
    visit()
    return solutions, nodes


def build():
    out = OUT/'multiplicity'
    out.mkdir(exist_ok=True)
    manifest = out/'build.json'
    if manifest.exists():
        data = json.loads(manifest.read_text())
        assert sha(data['binary']) == data['binary_sha256']
        assert all(sha(ROOT/v['path']) == v['sha256'] for v in data['sources'].values())
        return data
    source = ROOT/'sources/knuth-programs'
    directory = Path(tempfile.mkdtemp(prefix='knuth-vol4b-sudoku-multiplicity-'))
    names = ['dlx3.w', 'gb_flip.w', 'gb_flip.ch', 'boilerplate.w']
    for name in names:
        shutil.copy2(source/name, directory/name)
    commands = [['ctangle', 'gb_flip.w', 'gb_flip.ch'], ['ctangle', 'dlx3.w'],
                ['cc', '-O2', '-Wno-implicit-int', '-Wno-implicit-function-declaration',
                 'dlx3.c', 'gb_flip.c', '-o', 'dlx3']]
    with (out/'build.log').open('w') as log:
        for command in commands:
            subprocess.run(command, cwd=directory, stdout=log, stderr=subprocess.STDOUT, check=True)
    data = dict(built_at_utc=datetime.now(timezone.utc).isoformat(), commands=commands,
                binary=str(directory/'dlx3'), binary_sha256=sha(directory/'dlx3'),
                sources={name:dict(path=str((source/name).relative_to(ROOT)), sha256=sha(source/name)) for name in names},
                scope='Unmodified archived author DLX3, built in an isolated temporary directory.')
    manifest.write_text(json.dumps(data, indent=2)+'\n')
    return data


def main():
    start = time.monotonic()
    source = json.loads((ROOT/'results/sudoku_basics/pdf-grids.json').read_text())['sources']['29c']['board']
    diagrams = json.loads((OUT/'pdf-grids.json').read_text())['sources']
    expected, nodes = coordinate_solutions(source)
    assert len(expected) == 6
    names = [f'p{i}{j}' for i in range(9) for j in range(9)]
    names += [f'{t}{i}{k}' for t in 'rcb' for i in range(9) for k in TARGET]
    indices = {name:i+1 for i,name in enumerate(names)}
    rows, moves = [], []
    for v in range(81):
        i, j = divmod(v, 9)
        for k in TARGET:
            if source[v] and source[v] != k:
                continue
            rows.append([indices[s] for s in (f'p{i}{j}', f'r{i}{k}', f'c{j}{k}', f'b{3*(i//3)+j//3}{k}')])
            moves.append((v, k))
    header = [('2|' if name[0] != 'p' and name[-1] == '7' else '')+name for name in names]
    data = '\n'.join([' '.join(header)]+[' '.join(names[i-1] for i in row) for row in rows])+'\n'
    build_info = build()
    out = OUT/'multiplicity'
    (out/'51.mcc').write_text(data)
    command = [build_info['binary'], 'v129', 'm1']
    result = subprocess.run(command, input=data, text=True, capture_output=True, check=True, timeout=300)
    (out/'51.models').write_text(result.stdout)
    (out/'51.log').write_text(result.stderr)
    count = int(re.search(r'Altogether (\d+) solution', result.stderr)[1])
    native = set()
    for selection in decode_rows(result.stdout, names, rows):
        board = [0]*81
        for row in selection:
            v, k = moves[row]
            assert not board[v]
            board[v] = k
        assert all(Counter(board[v] for v in u) == TARGET for u in UNITS)
        assert all(not k or k == board[v] for v,k in enumerate(source))
        native.add(tuple(board))
    assert count == len(native) == 6 and native == expected
    partial = [int(c) if c != '.' else 0 for c in diagrams['51']['cells']]
    intersection = [next(iter(values)) if len(values) == 1 else 0
                    for v in range(81) for values in [{board[v] for board in expected}]]
    assert partial == intersection
    ordinary = json.loads((ROOT/'results/sudoku_basics/basics.json').read_text())['solutions']['c']
    collapsed = [tuple(7 if k == 8 else k for k in board) for board in ordinary]
    assert len(set(collapsed)) == 1 and collapsed[0] in expected
    # Conversely every successful 7-to-8 split would be one of these two
    # independently exhaustively enumerated ordinary completions of (29c).
    record = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), grids_sha256=sha(OUT/'pdf-grids.json'),
                  initial_sha256=sha(ROOT/'results/sudoku_basics/pdf-grids.json'),
                  ordinary_solutions_sha256=sha(ROOT/'results/sudoku_basics/basics.json'),
                  coordinate_nodes=nodes, solutions=sorted(expected),
                  native_command=command, binary_sha256=build_info['binary_sha256'],
                  input_sha256=sha(out/'51.mcc'), models_sha256=sha(out/'51.models'),
                  items=len(names), options=len(rows), partial_cells=sum(bool(k) for k in partial),
                  partial_equals_full_intersection=True, ordinary_collapsed_solution=collapsed[0],
                  splittable_multiset_solutions=1, ordinary_splits=2, seconds=time.monotonic()-start)
    (OUT/'multiplicity.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('coordinate_nodes','items','options','partial_cells','splittable_multiset_solutions','ordinary_splits','seconds')}, indent=2))


if __name__ == '__main__':
    main()
