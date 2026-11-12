#!/usr/bin/env python3
"""DLX55--56: clue examples, local trades, and complete automorphism check."""
from datetime import datetime, timezone
from itertools import permutations, product
import json
import time
from check_sudoku_basics import UNITS
from check_sudoku_minimal import Oracle
from check_sudoku_native import instance
from dlx1_audit_tools import ROOT, sha, run, input_text, decode_rows

OUT = ROOT/'results/sudoku_variants'
DIGITS = set(range(1,10))


def valid(board):
    return len(board) == 81 and all({board[v] for v in unit} == DIGITS for unit in UNITS)


def native_unique(label,board):
    names,rows,moves,primary = instance(board)
    stats,text = run(OUT/'clues',label,input_text(names,rows,primary),models=True)
    (OUT/'clues'/f'{label}.models').write_text(text)
    selected, = decode_rows(text,names,rows)
    completed = list(board)
    for r in selected:
        v,k = moves[r]; assert not completed[v]; completed[v] = k
    assert valid(completed) and stats['solutions'] == 1
    return completed,stats


def check_clues(label,initial,reference=None):
    completed,stats = native_unique(label,initial)
    if reference is not None:
        assert completed == reference
    oracle = Oracle(initial,completed)
    full = (1<<len(oracle.positions))-1
    assert oracle.unique(full)
    for i in range(len(oracle.positions)):
        assert not oracle.unique(full^(1<<i))
    oracle.close()
    return dict(initial=initial,solution=completed,clues=len(oracle.positions),
                native=stats,coordinate_oracle=oracle.build,
                single_clue_deletions=list(oracle.records.values()))


def bands_ok(order):
    return len(set(order)) == 9 and all(len({order[3*b+k]//3 for k in range(3)}) == 1 for b in range(3))


def band_orders():
    triples = list(permutations(range(3)))
    return [tuple(3*outer[b]+inners[b][k] for b in range(3) for k in range(3))
            for outer in triples for inners in product(triples,repeat=3)]


def automorphisms(board):
    """The first source row and a column permutation force digits and all rows."""
    expected_rows = {tuple(board[9*i:9*i+9]):i for i in range(9)}
    results = []
    for transpose in [False,True]:
        base = [board[9*j+i] for i in range(9) for j in range(9)] if transpose else board
        for columns in band_orders():
            for first_row in range(9):
                renaming = {base[9*first_row+columns[j]]:board[j] for j in range(9)}
                rows = [-1]*9
                for i in range(9):
                    row = tuple(renaming[base[9*i+j]] for j in columns)
                    if row not in expected_rows:
                        break
                    rows[expected_rows[row]] = i
                else:
                    if bands_ok(rows):
                        assert all(renaming[base[9*rows[i]+columns[j]]] == board[9*i+j] for i in range(9) for j in range(9))
                        results.append(dict(transpose=transpose,rows=rows,columns=columns,renaming=renaming))
    return results


def group_trades(board):
    """All12 Latin3 replacements of each of nine disjoint critical groups."""
    trades = []
    partition = set()
    latin = [a+b+c for a,b,c in product(permutations(range(3)),repeat=3)
             if all(len({a[j],b[j],c[j]}) == 3 for j in range(3))]
    assert len(latin) == 12
    for band in range(3):
        for residue in range(1,4):
            values = [residue,residue+3,residue+6]
            positions = [v for v in range(27*band,27*band+27) if board[v] in values]
            assert len(positions) == 9 and not partition.intersection(positions)
            partition.update(positions)
            assert all([v%9 for v in positions[3*r:3*r+3]] == [v%9 for v in positions[:3]] for r in range(3))
            models = []
            for replacement in latin:
                changed = list(board)
                for v,k in zip(positions,replacement):
                    changed[v] = values[k]
                assert valid(changed)
                models.append(changed)
            counts = [sum(s[v] == board[v] for s in models) for v in positions]
            assert counts == [4]*9 and board in models
            trades.append(dict(positions=positions,values=values,replacements=models,
                               completions_fixing_each_single_clue=counts))
    assert partition == set(range(81))
    return trades


def main():
    start = time.monotonic()
    grids = json.loads((OUT/'pdf-grids.json').read_text())['sources']
    bases = json.loads((ROOT/'results/sudoku_basics/pdf-grids.json').read_text())['sources']
    results = {}
    for name in ['55a','55b','56']:
        board = [0 if x == '.' else int(x) for x in grids[name]['cells']]
        results[name] = check_clues(name,board,bases['28'+name[-1]]['board'] if name.startswith('55') else None)
        print(name,results[name]['clues'],'clues: unique and every clue necessary',flush=True)
    results['55_groups'] = {name:group_trades(bases['28'+name]['board']) for name in 'ab'}
    source = ROOT/'sources/sudoku/dobrichev-40puz2.txt'
    collection = source.read_text().splitlines()
    diagram = ''.join(str(k) if k else '.' for k in results['56']['initial'])
    matches = [i+1 for i,line in enumerate(collection) if line.strip().replace('0','.') == diagram]
    assert matches
    results['56']['primary_collection'] = dict(path=str(source.relative_to(ROOT)),sha256=sha(source),matching_lines=matches)
    autos = automorphisms(results['56']['solution'])
    assert len(autos) == 1 and not autos[0]['transpose']
    assert autos[0]['rows'] == list(range(9)) and list(autos[0]['columns']) == list(range(9))
    results['56']['automorphisms'] = autos
    results['56']['automorphism_search_cases'] = 2*1296*9
    results.update(status='verified',source_sha256=sha(__file__),checked_at_utc=datetime.now(timezone.utc).isoformat(),
                   elapsed_seconds=time.monotonic()-start,
                   scope='55a minimum18 proved by disjoint local trades and explicit unique18 clues. '
                         '55b20-clue witness checked; excluding19 still requires a separate certificate. '
                         '56 verifies the40-clue example and trivial automorphism group, not global optimality40.')
    (OUT/'clue-bounds.json').write_text(json.dumps(results,indent=2)+'\n')
    print('automorphisms',len(autos),'seconds',results['elapsed_seconds'])


if __name__ == '__main__':
    main()
