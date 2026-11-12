#!/usr/bin/env python3
"""DLX43–50: positional PDF grids, independent Sudoku logic, and full solutions."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from itertools import combinations
import json
from pathlib import Path
import re
import subprocess
import xml.etree.ElementTree as ET

from dlx1_audit_tools import ROOT, sha, run, input_text, decode_rows

OUT = ROOT/'results/sudoku_basics'
BOOK = ROOT.parent/'books/taocp-vol4b-ed1-print2-2022.pdf'
DIGITS = set(range(1, 10))
UNITS = ([[9*r+c for c in range(9)] for r in range(9)]
         + [[9*r+c for r in range(9)] for c in range(9)]
         + [[9*r+c for r in range(3*(b//3), 3*(b//3)+3)
             for c in range(3*(b % 3), 3*(b % 3)+3)] for b in range(9)])
PEERS = [set().union(*(set(u) for u in UNITS if v in u))-{v} for v in range(81)]


def words(page):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT/f'page{page}-bbox.html'
    if not path.exists():
        subprocess.run(['pdftotext', '-f', str(page+20), '-l', str(page+20),
                        '-bbox', str(BOOK), str(path)], check=True)
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', ' ', path.read_text())
    result = []
    for w in ET.fromstring(text).iter():
        if w.tag.endswith('word') and (w.text or '').isdigit():
            box = [float(w.get(k)) for k in ('xMin', 'yMin', 'xMax', 'yMax')]
            result.append(dict(text=w.text, bbox=box,
                               x=(box[0]+box[2])/2, y=(box[1]+box[3])/2))
    return result


def grid(page, x0, y0, step, ymin=False):
    """Map every numeric word in the specified 9x9 rectangle to its cell."""
    cells = [set() for _ in range(81)]
    glyphs = []
    for w in words(page):
        y = w['bbox'][1] if ymin else w['y']
        r, c = round((y-y0)/step), round((w['x']-x0)/step)
        if not (0 <= r < 9 and 0 <= c < 9):
            continue
        if ymin and abs(y-y0-r*step) > .03:
            continue
        values = [int(d) for d in w['text']]
        assert len(set(values)) == len(values) and not cells[9*r+c].intersection(values), (page, r, c, w)
        cells[9*r+c].update(values)
        glyphs.append(dict(row=r, column=c, **w))
    return cells, glyphs


def clues(cells):
    assert all(len(cell) <= 1 for cell in cells)
    return [next(iter(cell)) if cell else 0 for cell in cells]


def candidates(board):
    for unit in UNITS:
        values = [board[v] for v in unit if board[v]]
        assert len(values) == len(set(values))
    return [{value} if value else DIGITS-{board[w] for w in PEERS[v]}
            for v, value in enumerate(board)]


def all_solutions(board):
    """Independent cell-MRV recursion, with row/column/box masks only."""
    board = list(board)
    rows, cols, boxes = [0]*9, [0]*9, [0]*9
    for v, value in enumerate(board):
        if value:
            r, c = divmod(v, 9); b = 3*(r//3)+c//3; bit = 1 << value
            assert not (rows[r] | cols[c] | boxes[b]) & bit
            rows[r] |= bit; cols[c] |= bit; boxes[b] |= bit
    out = []
    def visit():
        best, bits, size = None, 0, 10
        for v, value in enumerate(board):
            if not value:
                r, c = divmod(v, 9); b = 3*(r//3)+c//3
                choices = 1022 & ~(rows[r] | cols[c] | boxes[b])
                if choices.bit_count() < size:
                    best, bits, size = v, choices, choices.bit_count()
        if best is None:
            for unit in UNITS:
                assert {board[v] for v in unit} == DIGITS
            out.append(tuple(board))
            return
        r, c = divmod(best, 9); b = 3*(r//3)+c//3
        while bits:
            bit = bits & -bits; bits -= bit
            board[best] = bit.bit_length()-1
            rows[r] |= bit; cols[c] |= bit; boxes[b] |= bit
            visit()
            rows[r] ^= bit; cols[c] ^= bit; boxes[b] ^= bit
            board[best] = 0
    visit()
    return out


def single_items(board):
    cand = candidates(board)
    out = {}
    for v, values in enumerate(cand):
        if not board[v] and len(values) == 1:
            out[f'p{v//9}{v % 9}'] = (v, next(iter(values)))
    for kind, units in zip('rcb', (UNITS[:9], UNITS[9:18], UNITS[18:])):
        for i, unit in enumerate(units):
            present = {board[v] for v in unit}
            for value in sorted(DIGITS-present):
                slots = [v for v in unit if value in cand[v]]
                if len(slots) == 1:
                    out[f'{kind}{i}{value}'] = (slots[0], value)
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    sources = {}
    for z, x in enumerate((159.984, 269.124, 377.124)):
        for figure, y in ((28, 223.112), (29, 440.672)):
            cells, glyphs = grid(74, x, y, 8.9533, ymin=True)
            sources[f'{figure}{"abc"[z]}'] = dict(board=clues(cells), glyphs=glyphs)
    for key, page, x, y, step in [('31', 75, 236.355, 272.065, 15.936),
                                  ('32', 76, 248.775, 242.605, 15.936),
                                  ('33', 76, 248.775, 520.945, 15.936),
                                  ('48a', 425, 163.195, 307.471, 14.346),
                                  ('48b', 425, 336.142, 307.481, 14.338)]:
        cells, glyphs = grid(page, x, y, step)
        sources[key] = dict(cells=[sorted(s) for s in cells], glyphs=glyphs)
        assert all(cells), (key, [v for v, s in enumerate(cells) if not s])
    assert [sum(bool(v) for v in sources['29'+s]['board']) for s in 'abc'] == [32, 17, 16]
    (OUT/'pdf-grids.json').write_text(json.dumps(dict(book_sha256=sha(BOOK), sources=sources), indent=2)+'\n')

    # Exercise43: all 243 printed entries, and all three types of units.
    for z, label in enumerate('abc'):
        board = sources['28'+label]['board']
        assert all(board)
        for unit in UNITS:
            assert {board[v] for v in unit} == DIGITS
        for i in range(9):
            i1, i0 = divmod(i, 3)
            for j in range(9):
                j1, j0 = divmod(j, 3)
                formulas = [((3*i0+i1)+j) % 9,
                            3*((i0+j1) % 3)+(i1+j0) % 3,
                            3*((i0+i1+j1) % 3)+(i0-i1+j0) % 3]
                assert board[9*i+j]-1 == formulas[z]
    def perm(i):
        a, b = divmod(i, 3)
        return 3*a+(a+b) % 3
    inverse = {perm(i): i for i in range(9)}
    for i in range(9):
        for j in range(9):
            b = sources['28b']['board'][9*perm(i)+inverse[j]]-1
            assert perm(b) == sources['28c']['board'][9*i+j]-1

    # Initial charts, independent completions, exact-cover singleton lists.
    solutions = {}
    for label in 'abc':
        board = sources['29'+label]['board']
        if label in 'ab':
            chart = sources['31' if label == 'a' else '32']['cells']
            assert [sorted(s) for s in candidates(board)] == chart, label
        solutions[label] = all_solutions(board)
        assert len(solutions[label]) == (2 if label == 'c' else 1)
    assert [sum(len(s) for v, s in enumerate(candidates(sources['29'+x]['board']))
                if not sources['29'+x]['board'][v]) for x in 'ab'] == [146, 307]

    a = list(sources['29a']['board'])
    singles46 = list(single_items(a))
    expected46 = 'p44 p84 r33 r44 r48 r52 r59 r86 r88 c22 c43 b07 b32 b39 b43 b54 b58'.split()
    assert singles46 == expected46, (singles46, expected46)
    sequence45 = []
    while not all(a):
        naked = [(v, next(iter(s))) for v, s in enumerate(candidates(a)) if not a[v] and len(s) == 1]
        assert naked
        v, value = min(naked); a[v] = value; sequence45.append(f'p{v//9}{v % 9}')
    expected45 = ('p44 p84 p74 p24 p54 p14 p82 p42 p31 p32 p40 p45 p46 p50 '
                  'p72 p60 p00 p62 p61 p65 p35 p67 p70 p71 p75 p83 p13 p03 p18 '
                  'p16 p07 p01 p05 p15 p21 p25 p76 p36 p33 p37 p27 p28 p53 p56 '
                  'p06 p08 p58 p77 p88').split()
    assert sequence45 == expected45 and tuple(a) == solutions['a'][0]
    b = list(sources['29b']['board']); initial47 = single_items(b)
    b[2*9+3] = 3; singles47 = single_items(b)
    assert list(singles47) == 'r13 c03 b03 b24 b49 b69'.split(), singles47
    assert {'b24', 'b49', 'b69'} <= initial47.keys()
    forced = [('c33', 2*9+3, 3)]
    while single_items(b):
        choices = single_items(b)
        key = min(choices, key=lambda s: ('prcb'.index(s[0]), s[1:]))
        v, value = choices[key]; b[v] = value; forced.append((key, v, value))
    assert len(forced) == 16
    chart33 = candidates(b)
    assert [sorted(s) for s in chart33] == sources['33']['cells']
    row_value = [{j for j in range(9) if k in chart33[9*i+j]} for i in range(9) for k in range(1, 10)]
    value_col = [{i for i in range(9) if k in chart33[9*i+j]} for k in range(1, 10) for j in range(9)]
    chart_mismatches = [dict(row=v//9, value=v%9+1,
                             expected_columns=sorted(expected), printed_columns=printed)
                        for v, (expected, printed) in enumerate(zip(row_value, sources['48a']['cells']))
                        if sorted(expected) != printed]
    assert chart_mismatches == [dict(row=5, value=5, expected_columns=[4], printed_columns=[6])]
    # The original clue itself proves this discrepancy, before any solving.
    assert sources['29b']['board'][9*5+4] == 5
    assert sources['29b']['board'][9*5+5] == 3
    assert 5 not in chart33[9*5+6]
    assert [sorted(s) for s in value_col] == sources['48b']['cells']

    c0, c1 = solutions['c']
    swapped = tuple(15-v if v in (7, 8) else v for v in c0)
    assert c1 == swapped
    distinguishing = [(v, value) for v in range(81) if c0[v] != c1[v] for value in (c0[v], c1[v])]
    assert len(distinguishing) == 36
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), pdf_grids_sha256=sha(OUT/'pdf-grids.json'),
                  formula_entries_checked=243, isotopy_pairs_checked=81,
                  chart_cells_checked=405, naked_sequence45=sequence45, singleton_items46=singles46,
                  chart_mismatches=chart_mismatches, chart_cells_matching=404,
                  initial_hidden47=initial47, after_first_hidden47=singles47,
                  forced_to_chart33=forced, solutions=solutions,
                  exercise50=dict(complete_solutions=2, distinguishing_clues=distinguishing),
                  scope='Positional extraction and every value/candidate in28–29,31–33,48a–b; '
                        'all solutions by independent coordinate search. Historical claims and '
                        'the actual DLX profiles are separate follow-up checks.')
    (OUT/'basics.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('solutions', 'exercise50')}, indent=2))


if __name__ == '__main__':
    main()
