#!/usr/bin/env python3
"""All 10080 normalized card placements, compared with original colored DLX2."""
from collections import Counter
from datetime import datetime,timezone
from itertools import permutations
import json
import re
import subprocess
import time
from dlx1_audit_tools import ROOT,sha
from check_jigsaw_small import coordinate_solutions,violations,units
from check_sudoku_queens58 import build
from check_sudoku_clue_bounds import automorphisms

OUT=ROOT/'results/sudoku_extensions/cards66'


def diagram(cards,order):
    board=['.']*81
    for slot,k in enumerate(order):
        r,c=divmod(slot,3)
        for v,value in cards[k].items():board[(3*r+v//3)*9+3*c+v%3]=value
    return dict(nrows=9,ncols=9,cells=board,omitted=[],regions=[
        [9*(3*r+i)+3*c+j for i in range(3)for j in range(3)]for r in range(3)for c in range(3)])


def independent(cards):
    result=[];models=set();histogram=Counter();consistent=0
    for rest in permutations(range(2,10)):
        order=(1,)+rest
        if order[4]!=min(order[i]for i in [4,5,7,8]):continue
        d=diagram(cards,order);valid=True
        for unit in units(d):
            clues=[d['cells'][v]for v in unit if d['cells'][v]!='.']
            if len(clues)!=len(set(clues)):valid=False;break
        if valid:
            consistent+=1
            solutions,nodes=coordinate_solutions(d,'123456789')
            for s in solutions:models.add((''.join(map(str,order)),s))
        else:solutions=[];nodes=0
        histogram[len(solutions)]+=1
        result.append(dict(order=''.join(map(str,order)),locally_consistent=valid,coordinate_nodes=nodes,solutions=solutions))
    assert len(result)==10080
    return models,dict(placements=result,histogram=dict(histogram),locally_consistent=consistent)


def native(cards,label):
    names=[f'p{r}{c}'for r in range(9)for c in range(9)]
    names += [f'{t}{i}{k}'for t in 'rcb'for i in range(9)for k in range(1,10)]
    names += [str(k)for k in range(1,10)]+[f's{i}'for i in range(9)]
    second=[f'v{r}{c}'for r in range(9)for c in range(9)]
    options=[];moves=[]
    for r in range(9):
        for c in range(9):
            for k in range(1,10):
                options.append([f'p{r}{c}',f'r{r}{k}',f'c{c}{k}',f'b{3*(r//3)+c//3}{k}',f'v{r}{c}:{k}'])
                moves.append(('cell',9*r+c,str(k)))
    for k in range(1,10):
        for slot in ([0]if k==1 else range(1,9)):
            r,c=divmod(slot,3)
            options.append([str(k),f's{slot}']+[f'v{3*r+v//3}{3*c+v%3}:{value}'for v,value in cards[k].items()])
            moves.append(('card',slot,k))
    data='\n'.join([' '.join(names+['|']+second)]+[' '.join(o)for o in options])+'\n'
    path=OUT/(label+'.xcc');path.write_text(data)
    info=build();command=[info['binary'],'v129','m1'];start=time.monotonic()
    with (OUT/(label+'.models')).open('w')as output,(OUT/(label+'.log')).open('w')as log:
        p=subprocess.run(command,input=data,text=True,stdout=output,stderr=log,check=True,timeout=600)
    log=(OUT/(label+'.log')).read_text()
    match=re.search(r'Altogether (\d+) solutions?, (\d+)\+(\d+)-(\d+) mems, (\d+) updates, (\d+) cleansings, (\d+) bytes, (\d+) nodes',log)
    assert match,log[-1000:]
    stats=dict(zip(['solutions','initialization_mems','search_mems','removed_mems','updates','cleansings','bytes','nodes'],map(int,match.groups())))
    lookup={frozenset(o):m for o,m in zip(options,moves)}
    actual=set();selected=[];active=False
    def finish():
        if not active:return
        assert len(selected)==90
        board=['.']*81;order=[0]*9
        for kind,v,k in selected:
            if kind=='cell':assert board[v]=='.';board[v]=k
            else:assert not order[v];order[v]=k
        assert sorted(order)==list(range(1,10))and order[0]==1
        d=diagram(cards,order)
        assert not violations(d,board)and all(v=='.'or v==board[i]for i,v in enumerate(d['cells']))
        model=(''.join(map(str,order)),''.join(board));assert model not in actual;actual.add(model)
    for line in (OUT/(label+'.models')).read_text().splitlines():
        if re.fullmatch(r'\d+:',line):finish();selected=[];active=True
        elif line.strip():
            m=re.fullmatch(r'\s*(.*?) \(\d+ of \d+\)',line);assert m,line
            selected.append(lookup[frozenset(m[1].split())])
    finish();assert len(actual)==stats['solutions']
    normalized={m for m in actual if m[0][4]==min(m[0][i]for i in [4,5,7,8])}
    assert len(actual)==4*len(normalized)
    return normalized,dict(command=command,input_sha256=sha(path),build=info,statistics=stats,
                           elapsed_seconds=time.monotonic()-start,models_sha256=sha(OUT/(label+'.models')),
                           normalization='Card1 fixed in slot0; remaining row/column swaps give four copies. Keep c4=min(c4,c5,c7,c8).')


def main():
    OUT.mkdir(exist_ok=True)
    ds=json.loads((OUT.parent/'pdf-diagrams.json').read_text())['sources']
    result=dict(status='running',source_sha256=sha(__file__),cases={})
    for label in ['i','ii']:
        cards={k:{v:c for v,c in enumerate(ds[f'66-{label}-{k}']['cells'])if c!='.'}for k in range(1,10)}
        expected,ind=independent(cards)
        (OUT/(label+'-independent.json')).write_text(json.dumps(ind,indent=2)+'\n')
        print(label,'independent',ind['histogram'],flush=True)
        actual,meta=native(cards,label)
        assert actual==expected
        byorder=Counter(order for order,board in actual)
        if label=='i':
            assert byorder=={'192435768':1}
            board=next(iter(actual))[1]
            autos=automorphisms(tuple(map(int,board)));assert len(autos)==6
        else:
            assert byorder['149523786']==1 and byorder['149325687']==10
            autos=[]
        result['cases'][label]=dict(cards=cards,native=meta,independent_sha256=sha(OUT/(label+'-independent.json')),
                                   histogram=ind['histogram'],solutions_by_order=dict(byorder),models=sorted(actual),
                                   automorphisms=autos,automorphism_helper_sha256=sha(ROOT/'check_sudoku_clue_bounds.py'))
        (OUT/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
        print(label,'native',meta['statistics']['solutions'],'normalized',dict(byorder),flush=True)
    result.update(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat())
    (OUT/'validation.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
