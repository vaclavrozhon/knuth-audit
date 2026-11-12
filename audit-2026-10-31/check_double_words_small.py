#!/usr/bin/env python3
"""Geometry, both orbit actions, book witnesses and small complete XCC models."""
from collections import Counter
from datetime import datetime,timezone
from itertools import product
import hashlib,json,random
from colored_dlx import ColoredDLX
from double_word_tools import ROOT,OUT,dictionary,down_words,orbit,validate,encoding,model_rows,geometric_models,SQUARES,LEFT,RIGHT


def main():
    words=dictionary(5);rank={w:i+1 for i,w in enumerate(words)}
    squares={}
    for n,s in SQUARES.items():
        rows=s.split();w=dictionary(n,True);r={word:i+1 for i,word in enumerate(w)}
        squares[str(n)]=dict(rows=rows,columns=down_words(rows,'square'),maximum_rank=validate(rows,w,'square'),ranks={word:r[word] for word in rows+down_words(rows,'square')})
    best88='BLAST EARTH ANGER SCOPE TENSE'.split()
    assert validate(best88,words,'square')==1720 and rank['ARGON']==1720 and rank['PEERS']==1800
    stairs=[]
    for kind,examples,start in [('left',LEFT,2),('right',RIGHT,1)]:
        for p,s in enumerate(examples,start):
            rows=s.split();assert len(rows)==p
            maximum=validate(rows,words,kind);down=down_words(rows,kind)
            variants=orbit(rows,kind);assert len(variants)==2*p
            for other in variants:
                assert validate(list(other),words,kind)==maximum
                assert orbit(other,kind)==variants
            minima=[v for v in variants if rank[v[0]]==min(rank[x] for x in list(v)+down_words(v,kind))]
            assert len(minima)==1
            if kind=='left':assert maximum<=500 if p!=8 else maximum==504
            else:assert maximum<=1300 if p not in (2,3) else maximum>1300
            stairs.append(dict(kind=kind,period=p,rows=rows,down=down,maximum_rank=maximum,
                               ranks={w:rank[w] for w in rows+down},canonical=list(minima[0])))
    assert rank['NOTED']==504
    diagrams=[]
    for kind,s in [('left','STAIR SHARP STEMS SCRAP'),('right','STAIR SLOOP STOOD STEER')]:
        rows=s.split();diagrams.append(dict(kind=kind,rows=rows,down=down_words(rows,kind),maximum_rank=validate(rows,words,kind)))
    rng=random.Random(870090);cases=[];digest=hashlib.sha256();nonempty=0
    for kind,n,p in [('square',2,2),('square',3,3),('left',2,1),('left',2,2),('left',3,2),('left',3,3),('right',2,1),('right',2,2),('right',3,2),('right',3,3)]:
        universe=[''.join(x) for x in product('ABC' if n==2 else 'AB',repeat=n)]
        # Include complete dictionaries and random ordered subsets; rank order matters.
        dicts=[universe]+[rng.sample(universe,rng.randrange(1,len(universe)+1)) for _ in range(25)]
        for w in dicts:
            expected=set(geometric_models(w,kind,p));rank0={word:i for i,word in enumerate(w)}
            nonempty+=bool(expected)
            reduced={rows for rows in expected if (rank0[rows[0]]<rank0[down_words(rows,kind)[0]] if kind=='square'
                 else rank0[rows[0]]==min(rank0[x] for x in list(rows)+down_words(rows,kind)))}
            assert len(expected)==len(reduced)*(2 if kind=='square' else 2*p)
            for symmetry in (False,True):
                enc=encoding(w,kind,p,symmetry)
                run=ColoredDLX(len(enc['names']),enc['primary'],enc['rows']).solve(root=1,prefix83=symmetry)
                got={tuple(model_rows(m,enc)) for m in run.solutions}
                assert len(got)==len(run.solutions)
                assert got==(reduced if symmetry else expected),(kind,w,p,symmetry,got,expected)
                digest.update(json.dumps([kind,p,w,symmetry,sorted(got)]).encode())
            cases.append(dict(kind=kind,n=n,p=p,words=len(w),all_models=len(expected),orbits=len(reduced)))
    old=ROOT/'results/word_rectangles/cell-5x5.json';oldmeta=ROOT/'results/word_rectangles/cell-5x5-run.json'
    olddata=json.loads(old.read_text());oldrun=json.loads(oldmeta.read_text())
    assert olddata['verified'] and oldrun['returncode']==0
    assert olddata['count']==1787056 and olddata['repeated_words']==1140528
    assert (olddata['count']-olddata['repeated_words'])//2==323264
    assert 45.5e9<=olddata['mems']<46.5e9
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),book_squares=squares,
        book88=dict(rows=best88,columns=down_words(best88,'square'),maximum_rank=1720),
        book_stairs=stairs,question_diagrams=diagrams,cases=cases,small_matrices=len(cases),
        small_runs=2*len(cases),nonempty=nonempty,complete_model_digest=digest.hexdigest(),
        prior_5x5=dict(count=olddata['count'],repeated=olddata['repeated_words'],double_oriented=646528,double_orbits=323264,mems=olddata['mems'],
            evidence={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (old,oldmeta)}),
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['double_word_tools.py','check_double_words_small.py','colored_dlx.py']})
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'small-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:',len(cases),'geometric/XCC cases;',len(stairs),'printed stairs; six squares and both diagrams')
    print('Stair maxima:',[(x['kind'],x['period'],x['maximum_rank']) for x in stairs])


if __name__=='__main__':main()
