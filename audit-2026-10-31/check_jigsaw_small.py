#!/usr/bin/env python3
"""Complete model comparisons for jigsaw puzzles59--61 and main figures34--35."""
from collections import Counter
from datetime import datetime,timezone
from itertools import combinations
import json
from dlx1_audit_tools import ROOT,sha,run,input_text,decode_rows

OUT=ROOT/'results/jigsaw'


def units(diagram):
    nr,nc=diagram['nrows'],diagram['ncols']
    allowed=set(range(nr*nc))-set(diagram['omitted'])
    return [[r*nc+c for c in range(nc) if r*nc+c in allowed] for r in range(nr)]+[
        [r*nc+c for r in range(nr) if r*nc+c in allowed] for c in range(nc)]+diagram['regions']


def violations(diagram,board):
    return [dict(unit=i,cells=u,values=''.join(board[v] for v in u))
            for i,u in enumerate(units(diagram)) if len({board[v] for v in u})<len(u)]


def coordinate_solutions(diagram,alphabet,board=None,limit=None):
    """Cell-first DFS with hidden singles; no exact-cover matrix or links."""
    if board is None:board=list(diagram['cells'])
    else:board=list(board)
    us=units(diagram)
    allowed=sorted(set(range(len(board)))-set(diagram['omitted']))
    peers=[set() for _ in board]
    for u in us:
        for v in u:peers[v].update(u)
    for v in allowed:peers[v].discard(v)
    for u in us:
        vals=[board[v] for v in u if board[v]!='.']
        assert len(vals)==len(set(vals))
    bits={ch:1<<i for i,ch in enumerate(alphabet)}
    full=(1<<len(alphabet))-1
    solutions=[];nodes=0
    def visit():
        nonlocal nodes
        nodes+=1
        best=None;domains={}
        for v in allowed:
            if board[v]!='.':continue
            used=0
            for w in peers[v]:used|=bits.get(board[w],0)
            avail=full&~used
            if not avail:return
            domains[v]=avail
            if best is None or avail.bit_count()<best[0]:best=(avail.bit_count(),v,avail)
        if best is None:
            assert not violations(diagram,board)
            solutions.append(''.join(board));return
        # A full-size unit must still contain each missing symbol. A symbol
        # with zero possible cells is a contradiction; one forces a move.
        if best[0]>1:
            for u in us:
                if len(u)!=len(alphabet):continue
                used=0
                for v in u:used|=bits.get(board[v],0)
                missing=full&~used
                while missing:
                    b=missing&-missing;missing^=b
                    places=[v for v in u if domains.get(v,0)&b]
                    if not places:return
                    if len(places)==1:best=(1,places[0],b);break
                if best[0]==1:break
        _,v,avail=best
        while avail:
            b=avail&-avail;avail^=b;board[v]=alphabet[b.bit_length()-1]
            visit()
            if limit and len(solutions)>=limit:break
        board[v]='.'
    visit()
    return sorted(solutions),nodes


def instance(diagram,alphabet,board=None):
    nr,nc=diagram['nrows'],diagram['ncols']
    if board is None:board=diagram['cells']
    allowed=sorted(set(range(nr*nc))-set(diagram['omitted']))
    boxes={v:b for b,us in enumerate(diagram['regions']) for v in us}
    primary=[f'p{v//nc}{v%nc}' for v in allowed];secondary=[]
    for kind in 'rcb':
        count=nr if kind=='r' else nc if kind=='c' else len(diagram['regions'])
        for i in range(count):
            size=sum(v//nc==i for v in allowed) if kind=='r' else sum(v%nc==i for v in allowed) if kind=='c' else len(diagram['regions'][i])
            (primary if size==len(alphabet) else secondary).extend(f'{kind}{i}{k}' for k in alphabet)
    def option(v,k):return [f'p{v//nc}{v%nc}',f'r{v//nc}{k}',f'c{v%nc}{k}',f'b{boxes[v]}{k}']
    used={s for v in allowed if board[v]!='.' for s in option(v,board[v])}
    primary=[s for s in primary if s not in used]
    names=primary+[s for s in secondary if s not in used]
    index={s:i+1 for i,s in enumerate(names)}
    rows,moves=[],[]
    for v in allowed:
        for k in alphabet:
            o=option(v,k)
            if not used.intersection(o):
                rows.append([index[s] for s in o]);moves.append((v,k))
    return names,rows,moves,len(primary)


def native_case(label,diagram,alphabet,expected,board=None):
    if board is None:board=diagram['cells']
    names,rows,moves,primary=instance(diagram,alphabet,board)
    stats,txt=run(OUT/'native',label,input_text(names,rows,primary),models=True)
    model_path=OUT/'native'/(label+'.models');model_path.write_text(txt)
    actual=set()
    for selected in decode_rows(txt,names,rows):
        b=list(board)
        for row in selected:
            v,k=moves[row];assert b[v]=='.';b[v]=k
        assert not violations(diagram,b)
        actual.add(''.join(b))
    assert actual==set(expected),(label,len(actual),len(expected))
    stats.update(items=len(names),primary_items=primary,options=len(rows),
                 model_sha256=sha(model_path),independent_complete_sets_equal=True)
    return stats


def main():
    diagrams=json.loads((OUT/'pdf-diagrams.json').read_text())['sources']
    result=dict(status='running',source_sha256=sha(__file__),
                extract_sha256=sha(OUT/'pdf-diagrams.json'),puzzles={})
    for letter,alphabet,expected_nodes in [('a','123456789',1105),('b','ADEGIMNRT',910),('c','AFKLNTVWY',122)]:
        d=diagrams['34'+letter]
        models,nodes=coordinate_solutions(d,alphabet)
        assert models==[''.join(diagrams['59'+letter]['cells'])]
        native=native_case('59'+letter,d,alphabet,models)
        result['puzzles']['59'+letter]=dict(coordinate_nodes=nodes,solutions=models,native=native,
                                           book_nodes=expected_nodes,node_match=native['nodes']==expected_nodes)
        print('59'+letter,'nodes',native['nodes'],'book',expected_nodes,flush=True)
    for letter,expected_nodes in zip('abc',[23,26,16]):
        d=diagrams['60q'+letter]
        models,nodes=coordinate_solutions(d,'123456')
        assert models==[''.join(diagrams['60a'+letter]['cells'])]
        native=native_case('60'+letter,d,'123456',models)
        result['puzzles']['60'+letter]=dict(coordinate_nodes=nodes,solutions=models,native=native,
                                           book_nodes=expected_nodes,node_match=native['nodes']==expected_nodes)
        print('60'+letter,'nodes',native['nodes'],'book',expected_nodes,flush=True)
    # The two elementary deductions in the main text, using the original clues.
    candidates={}
    for label,value,positions in [('34a','4',range(9)),('34b','A',range(2,81,9))]:
        d=diagrams[label];us=units(d)
        candidates[label]=[v for v in positions if d['cells'][v]=='.' and
                           all(value not in [d['cells'][w] for w in u] for u in us if v in u)]
    assert candidates=={'34a':[7,8],'34b':[2]},candidates
    result['main_text_deductions']=candidates
    assert not violations(diagrams['35a'],diagrams['35a']['cells'])
    assert not violations(diagrams['35c'],diagrams['35c']['cells'])
    standard=[[9*(3*a+r)+3*b+c for r in range(3) for c in range(3)] for a in range(3) for b in range(3)]
    assert all(len({diagrams['35c']['cells'][v] for v in u})==9 for u in standard)
    d=diagrams['35b'];bad=violations(d,d['cells']);assert len(bad)==3
    repairs=[]
    for v in range(63):
        for k in '123456789':
            if k==d['cells'][v]:continue
            b=list(d['cells']);b[v]=k
            if not violations(d,b):repairs.append(dict(cell=v,row=v//7+1,column=v%7+1,value=k,rows=[''.join(b[r*7:r*7+7]) for r in range(9)]))
    assert len(repairs)==1 and repairs[0]['cell']==41 and repairs[0]['value']=='5'
    result['F116']=dict(violations=bad,all_single_cell_repairs=repairs,scope='row6,column7; 1-based')
    # For61 first enumerate every complete grid with two independent solvers.
    d=diagrams['35a'];empty=['.']*25
    models,nodes=coordinate_solutions(d,'12345',empty)
    native=native_case('61-empty',d,'12345',models,empty)
    reference=''.join(d['cells']);refid=models.index(reference)
    agreeing=[0]*25
    for i,model in enumerate(models):
        for v in range(25):
            if model[v]==reference[v]:agreeing[v]|=1<<i
    unique=[];ambiguous=[];use_all=[]
    for subset in combinations(range(25),5):
        candidates=(1<<len(models))-1
        for v in subset:candidates&=agreeing[v]
        assert candidates>>refid&1
        if candidates.bit_count()==1:
            unique.append(list(subset))
            if len({reference[v] for v in subset})==5:use_all.append(list(subset))
            b=['.']*25
            for v in subset:b[v]=reference[v]
            # A separate coordinate solve for each positive uniqueness claim.
            actual,_=coordinate_solutions(d,'12345',b,limit=2)
            assert actual==[reference]
        else:
            other=candidates&~(1<<refid)
            witness=(other&-other).bit_length()-1
            assert all(models[witness][v]==reference[v] for v in subset)
            ambiguous.append([list(subset),witness])
    assert len(unique)==1315 and len(use_all)==175
    printed=[v for v,k in enumerate(diagrams['61']['cells']) if k!='.']
    assert printed==use_all[0]
    assert all(diagrams['61']['cells'][v]==reference[v] for v in printed)
    (OUT/'61-models.json').write_text(json.dumps(models)+'\n')
    (OUT/'61-subsets.json').write_text(json.dumps(dict(unique=unique,all_five_digits=use_all,
            ambiguous_with_alternative_model_index=ambiguous))+'\n')
    result['61']=dict(complete_grids=len(models),coordinate_nodes=nodes,native=native,
                      subsets=53130,unique=len(unique),all_five_digits=len(use_all),
                      lexicographic_first_all=unique[0],lexicographic_first_five_digits=use_all[0],
                      printed_clue_positions=printed,models_sha256=sha(OUT/'61-models.json'),
                      subset_certificate_sha256=sha(OUT/'61-subsets.json'))
    result.update(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat())
    (OUT/'small.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS61',len(models),len(unique),len(use_all),unique[0],use_all[0],flush=True)


if __name__=='__main__':main()
