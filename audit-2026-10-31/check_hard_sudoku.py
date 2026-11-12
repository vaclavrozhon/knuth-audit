#!/usr/bin/env python3
"""Direct grid and exact-cover checks of 4B exercise 7.2.2.2–515."""
import itertools as it
import json
import re
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/hard_sudoku'
PUZZLES={
 'a':['1....6.8.','5.87214.6','.6.38.2.1','84...3..5','..5.6.8..','6..8...42','3.6.48.2.','4.76321.8','.8.5....4'],
 'b':['1.3.56.89','59738.61.','68.1.93.5','956.318.7','.315.896.','2.896.153','8.96.5.31','.65.13298','31.89.5.6'],
 'c':['1.3.5.7..','.5.79...1','7....125.','..1..5.76','..5.7.1..','47.1..5..','.185....7','5...87.1.','..7.1.8.5'],
 'd':['1.3.56.89','68.3.91.5','.9518.63.','3.896..51','.195.836.','56..319.8','.56.9381.','8.16.5.93','93.81.5.6'],
}
UNITS=[[(i,j) for j in range(9)] for i in range(9)]
UNITS += [[(i,j) for i in range(9)] for j in range(9)]
UNITS += [[(3*a+i,3*b+j) for i in range(3) for j in range(3)] for a in range(3) for b in range(3)]
NEIGHBORS={p:set().union(*(set(u) for u in UNITS if p in u))-{p} for p in it.product(range(9),repeat=2)}

def S(i,j,k):return 1+81*i+9*j+k
def Z(i,j):return 730+min(9*i+j,80-9*i-j)
def V(i,j,k):return 771+81*i+9*j+k
def R(i,k):return 1500+9*i+k
def C(j,k):return 1581+9*j+k
def B(b,k):return 1662+9*b+k
def P(i,j,k):return 1743+81*i+9*j+k

def encode(trades_only=True):
    blocks={}
    q=[]
    groups=[[S(i,j,k) for k in range(9)] for i,j in it.product(range(9),repeat=2)]
    groups += [[S(i,j,k) for i,j in unit] for unit in UNITS for k in range(9)]
    for vs in groups:q.append(vs);q.extend([-a,-b] for a,b in it.combinations(vs,2))
    blocks['sudoku']=q
    blocks['ii']=[list(c) for c in sorted({tuple(sorted({Z(i,j) for i,j in u})) for u in UNITS})]
    strips=[]
    for a,b,q in it.product(range(3),repeat=3):
        strips.append([(3*a+q,3*b+t) for t in range(3)])
        strips.append([(3*a+t,3*b+q) for t in range(3)])
    blocks['iii']=[list(c) for c in sorted({tuple(sorted({-Z(i,j) for i,j in u})) for u in strips})]
    q=[]
    for i,j,k in it.product(range(9),repeat=3):
        v,s,z=V(i,j,k),S(i,j,k),Z(i,j)
        q += [[-v,s],[-v,-z],[v,-s,z]]
    for typ,unit in enumerate(UNITS):
        for k in range(9):
            v=R(typ,k) if typ<9 else C(typ-9,k) if typ<18 else B(typ-18,k)
            vs=[V(i,j,k) for i,j in unit]
            q.append([-v]+vs);q.extend([v,-x] for x in vs)
    for i,j,k in it.product(range(9),repeat=3):
        v=P(i,j,k);vs=[Z(i,j),-R(i,k),-C(j,k),-B(3*(i//3)+j//3,k)]
        q.extend([-v,x] for x in vs);q.append([v]+[-x for x in vs])
    blocks['auxiliary']=q
    q=[]
    pgroups=[[P(i,j,k) for k in range(9)] for i,j in it.product(range(9),repeat=2)]
    pgroups += [[P(i,j,k) for i,j in unit] for unit in UNITS for k in range(9)]
    for vs in pgroups:
        for a in vs:q.append([-a]+[b for b in vs if b!=a])
    blocks['iv_v']=q
    q=[]
    for i,r in it.combinations(range(9),2):
        for j,c in it.combinations(range(9),2):
            sameband=i//3==r//3;samestack=j//3==c//3
            if sameband and samestack:continue # Impossible solution pattern.
            if trades_only and not(sameband or samestack):continue
            for k,l in it.permutations(range(9),2):
                q.append(list(dict.fromkeys([-S(i,j,k),-Z(i,j),-S(i,c,l),-Z(i,c),-S(r,j,l),-Z(r,j),-S(r,c,k),-Z(r,c)])))
    blocks['vi']=q
    blocks['symmetry']=[[S(0,k,k)] for k in range(9)]+[[-Z(0,0)],[Z(0,1)]]
    return blocks

def model_counterexample():
    from pysat.solvers import Solver
    blocks=encode()
    summary={k:dict(clauses=len(v),cells=sum(map(len,v))) for k,v in blocks.items()}
    clauses=[c for v in blocks.values() for c in v]
    summary['total']=dict(variables=2471,clauses=len(clauses),cells=sum(map(len,clauses)))
    (OUT/'encoding-counts.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(summary,flush=True)
    # Four boxes, so the swap is not a valid sudoku trade. Force the literal
    # condition (vi) to fail at rows 2,5 and columns 2,5.
    fixed=[S(1,1,3),S(1,4,6),S(4,1,6),S(4,4,3),Z(1,1),Z(1,4),Z(4,1),Z(4,4)]
    with Solver(name='g4',bootstrap_with=clauses) as solver:
        sat=solver.solve(assumptions=fixed);print('Counterexample SAT:',sat,flush=True)
        if not sat:return
        model=set(solver.get_model())
    assert all(any(x in model for x in c) for c in clauses)
    solution=[''.join(str(next(k+1 for k in range(9) if S(i,j,k) in model)) for j in range(9)) for i in range(9)]
    puzzle=[''.join('.' if Z(i,j) in model else solution[i][j] for j in range(9)) for i in range(9)]
    check=check_conditions(puzzle,solution)
    assert check['i'] and check['ii'] and check['iii'] and check['iv_min']>=2 and check['v_min']>=2
    assert check['vi_violations'] and not any(d['box_preserving'] for d in check['vi_violations'])
    d=dict(puzzle=puzzle,solution=solution,checks=check,fixed=fixed,positive_model=sorted(v for v in model if v>0))
    (OUT/'literal-vi-counterexample.json').write_text(json.dumps(d,indent=2)+'\n')
    print(d,flush=True)

def solve(puzzle):
    grid=[[int(c) if c!='.' else 0 for c in row] for row in puzzle]
    solutions=[]
    def visit():
        best=None;opts=None
        for i,j in it.product(range(9),repeat=2):
            if grid[i][j]:continue
            available=set(range(1,10))-{grid[a][b] for a,b in NEIGHBORS[i,j]}
            if not available:return
            if opts is None or len(available)<len(opts):
                best=(i,j);opts=available
                if len(opts)==1:break
        if best is None:
            assert all({grid[i][j] for i,j in u}==set(range(1,10)) for u in UNITS)
            solutions.append([''.join(map(str,row)) for row in grid]);return
        i,j=best
        for k in sorted(opts):grid[i][j]=k;visit()
        grid[i][j]=0
    visit();return solutions

def check_conditions(puzzle,solution):
    blank={(i,j) for i,j in it.product(range(9),repeat=2) if puzzle[i][j]=='.'}
    candidates={p:set('123456789')-{puzzle[i][j] for i,j in NEIGHBORS[p]} for p in blank}
    iv=min(map(len,candidates.values()))
    choices=[sum((i,j) in blank and k in candidates[i,j] for i,j in unit)
             for unit in UNITS for k in '123456789' if k not in {puzzle[i][j] for i,j in unit}]
    strips=[]
    for a,b in it.product(range(3),repeat=2):
        for q in range(3):
            strips.append(sum((3*a+q,3*b+t) in blank for t in range(3)))
            strips.append(sum((3*a+t,3*b+q) in blank for t in range(3)))
    bad=[]
    for r,s in it.combinations(range(9),2):
        for c,d in it.combinations(range(9),2):
            cells={(r,c),(r,d),(s,c),(s,d)}
            if not cells<=blank:continue
            if solution[r][c]==solution[s][d] and solution[r][d]==solution[s][c]:
                bad.append(dict(rows=[r+1,s+1],columns=[c+1,d+1],digits=[solution[r][c],solution[r][d]],
                                box_preserving=(r//3==s//3 or c//3==d//3)))
    return dict(i=all((8-i,8-j) in blank for i,j in blank),ii=all(set(u)&blank for u in UNITS),
                iii=max(strips)<3,max_blanks_in_box_strip=max(strips),iv_min=iv,v_min=min(choices),
                vi_violations=bad,visible=81-len(blank))

def dlx_count(label,puzzle):
    h=[f'{kind}{a}{b}' for kind in 'PRCB' for a,b in it.product(range(9),repeat=2)]
    rs=[]
    for i,j,k in it.product(range(9),repeat=3):
        if puzzle[i][j]!='.' and int(puzzle[i][j])!=k+1:continue
        rs.append([f'P{i}{j}',f'R{i}{k}',f'C{j}{k}',f'B{3*(i//3)+j//3}{k}'])
    data=' '.join(h)+'\n'+'\n'.join(' '.join(r) for r in rs)+'\n'
    (OUT/f'{label}.xcc').write_text(data)
    r=subprocess.run(['/tmp/knuth-dlx2','v1','d0'],input=data,text=True,capture_output=True)
    (OUT/f'{label}.dlx2.txt').write_text(r.stderr)
    m=re.search(r'Altogether (\d+) solutions?',r.stderr);assert m,r.stderr
    return int(m[1])

def main():
    OUT.mkdir(exist_ok=True,parents=True);result={}
    for label,puzzle in PUZZLES.items():
        sols=solve(puzzle);independent=dlx_count(label,puzzle);assert len(sols)==independent
        checks=[check_conditions(puzzle,s) for s in sols]
        assert all(d['i'] and d['ii'] and d['iii'] for d in checks)
        assert all(d['iv_min']>=(3 if label in 'cd' else 2) and d['v_min']>=(3 if label in 'cd' else 2) for d in checks)
        assert all(not any(v['box_preserving'] for v in d['vi_violations']) for d in checks) if label in 'ab' else True
        result[label]=dict(puzzle=puzzle,solutions=sols,count=len(sols),first_check=checks[0],
                           solutions_violating_literal_vi=sum(bool(d['vi_violations']) for d in checks))
        print(label,len(sols),checks[0],flush=True)
        (OUT/'puzzles.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':main()
