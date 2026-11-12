#!/usr/bin/env python3
"""Small solver-free certificate for the row/column isomorphism claim in DLX57."""
from collections import Counter
from datetime import datetime, timezone
import json
from dlx1_audit_tools import ROOT, sha

OUT = ROOT/'results/sudoku_variants/trios57'


def verify_grid(board):
    target = set(range(1,10))
    for i in range(9):
        assert set(board[9*i:9*i+9]) == target
        assert {board[9*j+i] for j in range(9)} == target
    for br in range(3):
        for bc in range(3):
            assert {board[9*(3*br+i)+3*bc+j] for i in range(3) for j in range(3)} == target
    expected = {(a,b,c) for a in (1,2,3) for b in (4,5,6) for c in (7,8,9)}
    h = [tuple(sorted(board[9*i+3*b:9*i+3*b+3])) for i in range(9) for b in range(3)]
    v = [tuple(sorted(board[9*(3*b+i)+j] for i in range(3))) for j in range(9) for b in range(3)]
    assert set(h) == set(v) == expected and len(h) == len(v) == 27
    assert [board[9*i+j] for i in range(3) for j in range(3)] == [1,4,7,8,2,5,6,9,3]
    assert board[0:3] == [1,4,7] and board[3] == 2 and board[6] == 3
    assert {board[4],board[7]} == {5,6} and {board[5],board[8]} == {8,9}


def transitions(board):
    result = {}
    for i in range(9):
        for j in range(9):
            if i == j:
                continue
            mapping = dict(zip(board[9*i:9*i+9],board[9*j:9*j+9]))
            p = tuple(mapping[k] for k in range(1,10))
            result.setdefault(p,[]).append([i,j])
    assert sum(map(len,result.values())) == 72
    return result


def main():
    source = OUT/'validation.json'
    data = json.loads(source.read_text())
    c = data['nonisomorphism_certificate']
    a,b = c['source'],c['target']
    verify_grid(a); verify_grid(b)
    mb = transitions(b)
    certificates = []
    for transpose in [False,True]:
        base = [a[9*j+i] for i in range(9) for j in range(9)] if transpose else a
        ma = transitions(base)
        permutation = next(p for p in mb if p not in ma)
        certificates.append(dict(transposed_source=transpose,permutation=list(permutation),
                                 witness_target_rows=mb[permutation][0],
                                 source_occurrences=0,target_occurrences=len(mb[permutation]),
                                 all_source_permutations=[list(p) for p in sorted(ma)]))
    classes = data['row_column_classes']
    # Check every positive symbol/row/column transformation directly.
    for cl in classes:
        g = cl['isotopy_from_shown']; d = {int(k):v for k,v in g['renaming'].items()}
        rep = cl['representative']
        assert [d[a[9*g['rows'][i]+g['columns'][j]]] for i in range(9) for j in range(9)] == rep
        for model_index in cl['members']:
            g = data['geometry_witnesses'][model_index]
            assert [rep[9*g['rows'][i]+g['columns'][j]] for i in range(9) for j in range(9)] == data['models'][model_index]
    result = dict(status='verified',source_sha256=sha(__file__),input_sha256=sha(source),
                  checked_at_utc=datetime.now(timezone.utc).isoformat(),source=a,counterexample=b,
                  transition_certificates=certificates,
                  argument='Permuting columns leaves the value-to-value permutation between each ordered pair of rows unchanged. '
                           'Permuting rows only reorders the72 pairs. A transition present in the counterexample is absent '
                           'from the printed grid (and another excludes its transpose). Hence symbol renaming is essential.',
                  positive_transformations_checked=len(data['models']),
                  literal_class_sizes=[sum(data['models'][i][3] == 2 for i in c['members']) for c in classes])
    assert result['literal_class_sizes'] == [72]*6
    (OUT/'small-certificates.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Verified two valid normalized grids, absent row-transition permutations, and864 positive symbol/row/column maps.')


if __name__ == '__main__':
    main()
