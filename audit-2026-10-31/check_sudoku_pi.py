#!/usr/bin/env python3
"""DLX44: certified digits of pi, and the published22-clue diagonal Sudoku."""
from datetime import datetime, timezone
from fractions import Fraction as F
import json
from check_sudoku_basics import OUT, UNITS, DIGITS
from dlx1_audit_tools import ROOT, sha, run, input_text, decode_rows


def atan_interval(q, terms):
    partial = sum((F((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(terms)), F(0))
    following = partial + F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(partial, following), max(partial, following)


def main():
    a, b = atan_interval(5, 70); c, d = atan_interval(239, 20)
    low, high = 16*a-4*d, 16*b-4*c
    def floor(x): return x.numerator//x.denominator
    assert floor(low*10**32) == floor(high*10**32)
    digits = str(floor(low*10**32))
    assert len(digits) == 33 and digits[-1] == '0' and '0' not in digits[:-1]
    # tan(4 arctan(1/5) - arctan(1/239)) = 1, and the angle lies in(0,pi/2).
    t = F(1,5)
    t = 2*t/(1-t*t); t = 2*t/(1-t*t)
    assert (t-F(1,239))/(1+t*F(1,239)) == 1
    sources = json.loads((OUT/'pdf-grids.json').read_text())['sources']
    actual = ''.join(str(k) for k in sources['29a']['board'] if k)
    assert actual == digits[:32]

    # Visual transcription of the Pythagoras magazine reproduction, clockwise from3.
    positions = [(0,2),(0,4),(0,5),(1,6),(1,7),(2,8),(3,8),(4,8),(5,8),
                 (6,7),(7,6),(7,5),(7,4),(8,3),(8,2),(7,1),(6,0),(5,0),
                 (4,0),(3,0),(2,1),(1,2)]
    observed = '3141592653589793238462'
    assert observed == digits[:22]
    board = [0]*81
    for (i,j), k in zip(positions,map(int,observed)): board[9*i+j] = k
    units = UNITS+[[9*i+i for i in range(9)],[9*i+8-i for i in range(9)]]
    peers = [set().union(*(set(u) for u in units if v in u))-{v} for v in range(81)]
    independent = []
    def visit():
        choices = [(DIGITS-{board[w] for w in peers[v]}, v) for v in range(81) if not board[v]]
        if not choices:
            assert all({board[v] for v in unit} == DIGITS for unit in units)
            independent.append(tuple(board)); return
        values, v = min(choices,key=lambda t:(len(t[0]),t[1]))
        for k in sorted(values):
            board[v] = k; visit(); board[v] = 0
    visit()
    assert len(independent) == 1
    def option(v,k):
        return [f'p{v//9}{v%9}']+[f'u{i}-{k}' for i,u in enumerate(units) if v in u]
    all_names = [f'p{i}{j}' for i in range(9) for j in range(9)]+[f'u{i}-{k}' for i in range(29) for k in range(1,10)]
    used = {name for v,k in enumerate(board) if k for name in option(v,k)}
    names = [s for s in all_names if s not in used]; idx = {s:i+1 for i,s in enumerate(names)}
    rows, moves = [], []
    for v in range(81):
        for k in range(1,10):
            o = option(v,k)
            if not used.intersection(o):
                rows.append([idx[s] for s in o]); moves.append((v,k))
    stats, text = run(OUT/'pi','circle22',input_text(names,rows),models=True)
    (OUT/'pi/circle22.models').write_text(text)
    native = []
    for selected in decode_rows(text,names,rows):
        model = list(board)
        for r in selected:
            v,k = moves[r]; assert not model[v]; model[v] = k
        native.append(tuple(model))
    assert native == independent
    result = dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), image_sha256=sha(ROOT/'sources/sudoku/pyth-pi-circle.png'),
                  pi_interval=[str(low),str(high)],first_33_digits=digits,clues29a=actual,
                  circle_positions=positions,circle_board=board,circle_solution=independent[0],
                  native=stats,scope='Exact rational certification, all32 row-major clues of29a; '
                  'all22 visually transcribed circle clues, complete independent diagonal-Sudoku solutions, '
                  'and original DLX1. The original book page144 was not obtained; the Pythagoras magazine reproduction is the source.')
    (OUT/'pi.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(first_33_digits=digits, circle_solutions=len(native),native=stats),indent=2))


if __name__ == '__main__':
    main()
