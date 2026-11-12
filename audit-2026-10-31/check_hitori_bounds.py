"""Exact witnesses and boundary estimate for TAOCP 4B X443."""
from itertools import product
from pathlib import Path
import json
from check_hitori import Board
ROOT=Path(__file__).parent


def puzzle_solutions(puzzle):
    m=len(puzzle);n=len(puzzle[0]);board=Board(m,n);solutions=[]
    for black in range(board.full+1):
        if not board.cover(black,False):continue
        for line in ([r*n+c for c in range(n)] for r in range(m)):
            vals=[puzzle[v//n][v%n] for v in line if not black>>v&1]
            if len(vals)!=len(set(vals)):break
        else:
            for line in ([r*n+c for r in range(m)] for c in range(n)):
                vals=[puzzle[v//n][v%n] for v in line if not black>>v&1]
                if len(vals)!=len(set(vals)):break
            else:solutions.append(black)
    return solutions


def boundary_max(m,n):
    perimeter=([(0,c) for c in range(n)]+[(r,n-1) for r in range(1,m)]+
               [(m-1,c) for c in range(n-2,-1,-1)]+[(r,0) for r in range(m-2,0,-1)])
    weights=[2 if r in (0,m-1) and c in (0,n-1) else 1 for r,c in perimeter]
    best=0
    for first in (0,1):
        states={first:first*weights[0]}
        for weight in weights[1:]:
            nxt={}
            for previous,value in states.items():
                for bit in (0,1):
                    if previous and bit:continue
                    nxt[bit]=max(nxt.get(bit,-1),value+bit*weight)
            states=nxt
        best=max(best,max(value for last,value in states.items() if not(first and last)))
    return best


def main():
    family=[]
    for n in range(1,102,2):
        board=Board(3,n);black=sum(1<<(r*n+c) for r in (0,2) for c in range(0,n,2))
        assert board.cover(black)
        s=black.bit_count();assert s==n+1 and 3*s>3*n+2
        family.append(dict(rows=3,columns=n,black=s,printed_bound_numerator=3*n+2))
    puzzles=[]
    for puzzle in [('AAA',),('AAA','BCD','EEE')]:
        sols=puzzle_solutions(puzzle);assert len(sols)==1
        black=sols[0];s=black.bit_count();m=len(puzzle);n=len(puzzle[0])
        assert 3*s>m*n+2
        puzzles.append(dict(puzzle=puzzle,unique_black_mask=black,black_cells=s,
                            black_positions=[(r,c) for r in range(m) for c in range(n) if black>>(r*n+c)&1]))
    perimeter_checks=0
    for m in range(2,101):
        for n in range(m,101):
            corrected=m+n+2-(m%2==0)-(n%2==0)
            assert boundary_max(m,n)<=corrected
            perimeter_checks+=1
    counts=json.loads((ROOT/'results/hitori_counts.json').read_text())['cases']
    violations=[]
    for case in counts:
        m=case['rows'];n=case['columns'];s=case['max_black']
        assert 3*s<=m*n+3-(m%2==0)-(n%2==0)
        if 3*s>m*n+2:violations.append(dict(rows=m,columns=n,black=s))
    out=dict(family=family,puzzles=puzzles,perimeter_checks=perimeter_checks,
             table_violations=violations,
             corrected_boundary='b+2c <= m+n+2-[m even]-[n even]',
             corrected_universal_bound='3s <= mn+3-[m even]-[n even]',
             proof='Sum the four side bounds ceil(length/2). Each corner is counted twice. For m,n>1, compare white edge count with white vertex count minus one. Handle one-dimensional paths separately: maximum black count is 0,1,2 for lengths1,2,>=3.')
    (ROOT/'results/hitori_bounds.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='family'}))

if __name__=='__main__':main()
