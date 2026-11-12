#!/usr/bin/env python3
"""DLX57: all box patterns, complete covers, and explicit geometry witnesses."""
from collections import Counter
from datetime import datetime, timezone
from itertools import permutations, product
import json
import time
from check_sudoku_basics import UNITS
from check_sudoku_clue_bounds import bands_ok, band_orders
from dlx1_audit_tools import ROOT, sha, run, input_text, decode_rows

OUT = ROOT/'results/sudoku_variants/trios57'
T = {tuple(p) for p in product(range(1,4),range(4,7),range(7,10))}


def trios(board):
    h = [tuple(sorted(board[9*i+3*b:9*i+3*b+3])) for i in range(9) for b in range(3)]
    v = [tuple(sorted(board[9*(3*b+r)+j] for r in range(3))) for j in range(9) for b in range(3)]
    return h,v


def patterns():
    # Independent brute-force digit placement and structured Latin3 generation.
    brute = {p for p in permutations(range(1,10))
             if all(len({(p[3*i+j]-1)//3 for j in range(3)}) == 3
                    and len({(p[3*j+i]-1)//3 for j in range(3)}) == 3 for i in range(3))}
    latin = [a+b+c for a,b,c in product(permutations(range(3)),repeat=3)
             if all(len({a[j],b[j],c[j]}) == 3 for j in range(3))]
    structured = set()
    for layout in latin:
        for digits in product(permutations(range(1,4)),permutations(range(4,7)),permutations(range(7,10))):
            counters = [0,0,0]; p = []
            for group in layout:
                p.append(digits[group][counters[group]]); counters[group] += 1
            structured.add(tuple(p))
    assert brute == structured and len(brute) == 2592
    return sorted(brute)


def instance(group_order_only=False):
    ps = patterns()
    names = [f'b{b}' for b in range(9)]
    names += [f'{t}{i}{k}' for t in 'rc' for i in range(9) for k in range(1,10)]
    names += [t+''.join(map(str,s)) for t in 'hv' for s in sorted(T)]
    index = {s:i+1 for i,s in enumerate(names)}
    rows,moves,counts = [],[],Counter()
    for box in range(9):
        for p in ps:
            if box == 0 and p != (1,4,7,8,2,5,6,9,3):
                continue
            if box in (1,2):
                allowed = (p[0] in (1,2,3) and p[1] in (4,5,6) and p[2] in (7,8,9)) if group_order_only else (p[0] == box+1 and p[1] in (5,6) and p[2] in (8,9))
                if not allowed:
                    continue
            option = [f'b{box}']
            for r in range(3):
                for c in range(3):
                    i,j = 3*(box//3)+r,3*(box%3)+c
                    k = p[3*r+c]
                    option += [f'r{i}{k}',f'c{j}{k}']
            option += ['h'+''.join(map(str,sorted(p[3*r:3*r+3]))) for r in range(3)]
            option += ['v'+''.join(map(str,sorted(p[3*r+c] for r in range(3)))) for c in range(3)]
            assert len(option) == len(set(option)) == 25
            rows.append([index[s] for s in option]); moves.append((box,p)); counts[box] += 1
    assert len(rows) == (16417 if group_order_only else 15681)
    return names,rows,moves,dict(counts)


def bitset_covers(rows,nitems):
    item_rows = [0]*nitems
    row_items = []
    for i,row in enumerate(rows):
        row_items.append(sum(1<<(j-1) for j in row))
        for j in row:
            item_rows[j-1] |= 1<<i
    conflicts = []
    for row in rows:
        mask = 0
        for j in row:
            mask |= item_rows[j-1]
        conflicts.append(mask)
    profile = Counter(); solutions = set()
    def visit(items,active,chosen):
        profile[len(chosen)] += 1
        if not items:
            solutions.add(tuple(sorted(chosen))); return
        candidates,best = None,len(rows)+1
        remaining = items
        while remaining:
            bit = remaining&-remaining; remaining ^= bit
            available = item_rows[bit.bit_length()-1]&active
            size = available.bit_count()
            if size < best:
                candidates,best = available,size
                if not best:
                    return
        while candidates:
            bit = candidates&-candidates; candidates ^= bit
            r = bit.bit_length()-1
            visit(items&~row_items[r],active&~conflicts[r],chosen+[r])
    visit((1<<nitems)-1,(1<<len(rows))-1,[])
    return solutions,dict(profile)


def geometry(source,target,require_boxes=True):
    # With no symbol relabeling, a first source row forces all columns and rows.
    for first in range(9):
        lookup = {source[9*first+j]:j for j in range(9)}
        columns = [lookup[k] for k in target[:9]]
        if require_boxes and not bands_ok(columns):
            continue
        moved = {tuple(source[9*i+j] for j in columns):i for i in range(9)}
        if not all(tuple(target[9*i:9*i+9]) in moved for i in range(9)):
            continue
        rows = [moved[tuple(target[9*i:9*i+9])] for i in range(9)]
        if not require_boxes or bands_ok(rows):
            assert all(source[9*rows[i]+columns[j]] == target[9*i+j] for i in range(9) for j in range(9))
            return dict(rows=rows,columns=columns,box_preserving=bands_ok(rows) and bands_ok(columns))
    return None


def isotopy(source,target):
    expected_rows = {tuple(target[9*i:9*i+9]):i for i in range(9)}
    for columns in band_orders():
        for first in range(9):
            renaming = {source[9*first+columns[j]]:target[j] for j in range(9)}
            rows = [-1]*9
            for i in range(9):
                row = tuple(renaming[source[9*i+j]] for j in columns)
                if row not in expected_rows:
                    break
                rows[expected_rows[row]] = i
            else:
                if bands_ok(rows):
                    assert all(renaming[source[9*rows[i]+columns[j]]] == target[9*i+j] for i in range(9) for j in range(9))
                    return dict(rows=rows,columns=columns,renaming=renaming)
    raise AssertionError('No symbol/row/column isotopy')


def exclusion_certificate(source,target):
    trials = []
    for transpose in [False,True]:
        base = [source[9*j+i] for i in range(9) for j in range(9)] if transpose else source
        for first in range(9):
            lookup = {base[9*first+j]:j for j in range(9)}
            columns = [lookup[k] for k in target[:9]]
            possible_rows = [tuple(base[9*i+j] for j in columns) for i in range(9)]
            missing = next(i for i in range(9) if tuple(target[9*i:9*i+9]) not in possible_rows)
            trials.append(dict(transpose=transpose,first_source_row=first,forced_columns=columns,
                               impossible_target_row=missing,possible_source_rows=possible_rows))
    return dict(source=source,target=target,trials=trials,
                argument='The source row sent to target row0 forces every column because symbols are distinct. '
                         'Each of9 choices (also after transposition) then lacks a required target row. '
                         'This excludes arbitrary row/column permutations, even without box restrictions.')


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    start = time.monotonic()
    names,rows,moves,counts = instance()
    stats,text = run(OUT,'57',input_text(names,rows),models=True,timeout=600)
    (OUT/'57.models').write_text(text)
    native = decode_rows(text,names,rows)
    print('native',len(native),'solutions,',stats['nodes'],'nodes',flush=True)
    independent,profile = bitset_covers(rows,len(names))
    assert independent == native and len(native) == 432
    n2,r2,m2,c2 = instance(group_order_only=True)
    stats2,text2 = run(OUT,'57-group-order',input_text(n2,r2),models=True,timeout=600)
    (OUT/'57-group-order.models').write_text(text2)
    native2 = decode_rows(text2,n2,r2)
    independent2,profile2 = bitset_covers(r2,len(n2))
    assert native2 == independent2 and len(native2) == 864
    print('group-order',len(native2),'solutions,',stats2,flush=True)
    diagrams = json.loads((ROOT/'results/sudoku_variants/pdf-grids.json').read_text())['sources']
    shown = [int(k) for k in diagrams['57']['cells']]
    models,geometries = [],[]
    classes = []
    for selected in sorted(native2):
        assert len(selected) == 9
        board = [0]*81
        for r in selected:
            b,p = m2[r]
            for i in range(3):
                for j in range(3):
                    board[9*(3*(b//3)+i)+3*(b%3)+j] = p[3*i+j]
        assert all({board[v] for v in unit} == set(range(1,10)) for unit in UNITS)
        assert all(set(ts) == T and len(ts) == len(set(ts)) == 27 for ts in trios(board))
        for cl in classes:
            g = geometry(cl['representative'],board,False)
            if g is not None:
                strict = geometry(cl['representative'],board)
                assert strict is not None
                cl['members'].append(len(models))
                geometries.append(dict(class_index=classes.index(cl),**strict))
                break
        else:
            classes.append(dict(representative=board,members=[len(models)],
                                isotopy_from_shown=isotopy(shown,board)))
            geometries.append(dict(class_index=len(classes)-1,rows=list(range(9)),columns=list(range(9)),box_preserving=True))
        models.append(board)
    assert shown in models
    assert len(classes) == 6 and all(len(c['members']) == 144 for c in classes)
    counterexample = next(b for b in models if geometry(shown,b,False) is None)
    exclusion = exclusion_certificate(shown,counterexample)
    print('six row/column classes:',[len(c['members']) for c in classes],flush=True)
    literal_models = [b for b in models if b[3] == 2]
    assert len(literal_models) == 432
    assert {b[3] for b in models} == {2,3}
    for b in models:
        swapped = [b[9*i+j] for i in range(9) for j in [0,1,2,6,7,8,3,4,5]]
        assert swapped in models and (b[3] == 2) != (swapped[3] == 2)
    basic = json.loads((ROOT/'results/sudoku_basics/pdf-grids.json').read_text())['sources']
    pi = json.loads((ROOT/'results/sudoku_basics/basics.json').read_text())['solutions']['a'][0]
    examples = {}
    for name,board in [('28a',basic['28a']['board']),('28b',basic['28b']['board']),('29a',pi)]:
        h,v = trios(board)
        examples[name] = dict(horizontal=len(set(h)),vertical=len(set(v)),
                              h368=h.count((3,6,8)),v368=v.count((3,6,8)),
                              horizontal_sets=sorted(set(h)),vertical_sets=sorted(set(v)))
    assert [(x['horizontal'],x['vertical']) for x in examples.values()] == [(9,3),(3,3),(26,23)]
    assert examples['29a']['h368'] == 1 and examples['29a']['v368'] == 2
    mapping = [8,1,3,7,0,5,6,2,4]
    diagonal = []
    for band in range(2):
        for stack in range(2):
            a = [shown[9*(3*band+i)+3*stack+j] for i in range(3) for j in range(3)]
            b = [shown[9*(3*(band+1)+i)+3*(stack+1)+j] for i in range(3) for j in range(3)]
            assert b == [a[k] for k in mapping]
            diagonal.append(dict(source_box=3*band+stack,target_box=3*(band+1)+stack+1,source=a,target=b))
    result = dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
                  book_box_pattern_count=2592,box_pattern_methods='All9! digit permutations versus12 Latin3 group layouts times6^3 digit orders',
                  normalized_options=len(rows),options_per_box=counts,book_reported_options=16417,
                  native=stats,independent_bitset_profile=profile,models=models,geometry_witnesses=geometries,
                  group_order_only=dict(options=len(r2),options_per_box=c2,native=stats2,independent_profile=profile2),
                  literal_models=literal_models,row_column_classes=classes,nonisomorphism_certificate=exclusion,
                  examples=examples,diagonal_box_permutation=mapping,diagonal_checks=diagonal,
                  elapsed_seconds=time.monotonic()-start,
                  scope='The literal1472AB3CD restriction gives432 solutions and15681 options. '
                        'Allowing the first-row2 and3 to exchange stacks gives864 solutions and16417 options, '
                        'with explicit stack-swap pairing. There are six row/column classes, all equivalent '
                        'after additionally permitting symbol renaming. All models and stated trio examples validated.')
    (OUT/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(options=len(rows),native=stats,independent_profile=profile,seconds=result['elapsed_seconds']),indent=2))


if __name__ == '__main__':
    main()
