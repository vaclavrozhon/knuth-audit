#!/usr/bin/env python3
"""Replay a uniform induction for Harris's connected-region construction."""
from datetime import datetime,timezone
import json
from dlx1_audit_tools import ROOT,sha
from check_jigsaw_small import units,violations
from check_jigsaw_symmetry import maps,moved
from check_sudoku_extensions import native

OUT=ROOT/'results/sudoku_extensions'


def regions(n):
    result=[{c for c in range(n-2)}|{n,2*n},
            {n-2,n-1}|{n+c for c in range(1,n-1)},
            {n*r+n-1 for r in range(1,n)}|{n*(n-1)+n-2}]
    for R in range(4,n+1):
        result.append({(R-2)*n+c for c in range(R-3,n-1)}|{(R-1)*n+c for c in range(R-2)})
    return [sorted(s)for s in result]


def proof(n):
    reg=regions(n);assert len(reg)==n and all(len(s)==n for s in reg)
    assert sorted(v for s in reg for v in s)==list(range(n*n))
    for s in reg:
        reached={s[0]}
        while True:
            nxt=reached|{v for v in s if any(abs(v//n-w//n)+abs(v%n-w%n)==1 for w in reached)}
            if nxt==reached:break
            reached=nxt
        assert reached==set(s)
        if n>=4:assert len({v//n for v in s})>1 and len({v%n for v in s})>1
    board=[0]*(n*n)
    for r in range(n):board[r*n]=r+1
    d=dict(nrows=n,ncols=n,regions=reg,omitted=[]);us=units(d)
    peers=[set()for _ in board]
    for u in us:
        for v in u:peers[v].update(u)
    # Row0 versus regionA: its final two symbols are {2,3}.
    # Row1 versus regionB then gives rightmost=3, so row0 rightmost=2.
    # RegionC versus the final column gives bottom penultimate=2.
    seed=[(0,n-2,3),(0,n-1,2),(1,n-1,3),(n-1,n-2,2)]
    for r,c,k in seed:
        v=r*n+c;assert board[v]in (0,k);board[v]=k
    steps=[]
    def force(r,c,k,unit):
        v=r*n+c
        if board[v]:assert board[v]==k;return
        available=[w for w in unit if board[w]==0 and all(board[t]!=k for t in peers[w])]
        assert available==[v],(n,r,c,k,available)
        board[v]=k;steps.append(dict(row=r,column=c,value=k,unit=unit))
    for r in range(n-2,0,-1):force(r,r-1,2,reg[r+1])
    for k in range(2,n):
        for r in range(k+1,n):force(r,r-k,k+1,reg[r])
        for r in range(k):force(r,n-k+r,k+1,us[r])
    for r in range(1,n):force(r,r,1,us[r])
    expected=[1+(r-c)%n for r in range(n)for c in range(n)]
    assert board==expected and not violations(d,board)
    return dict(n=n,seed=seed,forced_steps=steps,solution=board,regions=reg)


def main():
    cases=[proof(n)for n in range(3,33)]
    native_cases={}
    for n in range(3,10):
        p=cases[n-3];alphabet='123456789'[:n];board=['.']*(n*n)
        for r in range(n):board[r*n]=alphabet[r]
        d=dict(nrows=n,ncols=n,regions=p['regions'],omitted=[],cells=board)
        solution=''.join(alphabet[k-1]for k in p['solution'])
        native_cases[str(n)]=native('64-proof-n'+str(n),d,alphabet,[solution])
    diagrams=json.loads((OUT/'pdf-diagrams.json').read_text())['sources']
    p=cases[4];printed=diagrams['64-proof']
    assert moved(tuple(map(tuple,p['regions'])),maps(7)[6])==tuple(sorted(map(tuple,printed['regions'])))
    solution=[1+(c-r)%7 for r in range(7)for c in range(7)]
    for v,ch in enumerate(printed['cells']):
        if ch in '1234567':assert solution[v]==int(ch)
        elif ch in 'abcdef':assert solution[v]==3
        elif ch in 'ghijkl':assert solution[v]==4
    result=dict(status='verified',source_sha256=sha(__file__),checked_at_utc=datetime.now(timezone.utc).isoformat(),
                proof_scope='General induction is written in SUDOKU_EXTENSIONS_NOTES.md; finite certificate replays n3--32 supplement, not replace, that proof.',
                construction_cases=cases,native_cases=native_cases,book_diagram_transpose=True,
                original_source_sha256=sha(ROOT/'sources/sudoku_extensions/harris-proof.html'))
    (OUT/'clueless-proof.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS uniform induction replay n3--32; originalDLX1 n3--9; entire printed diagram')


if __name__=='__main__':main()
