#!/usr/bin/env python3
"""DLX22: literal pairwise encodings versus independent complete queen counts."""
from datetime import datetime, timezone
import hashlib
import json
import subprocess

from check_dlx_ordering import pair_lists
from check_queen_rotations import valid
from dlx1_audit_tools import ROOT, sha, input_text, run, decode_rows

OUT=ROOT/'results/queen_symmetry'
PRINTED_A=[0,0,1,8,260,9709,371590]
PRINTED_B=[0,0,1,4,14,21,109,500,2453,14498,89639,568849]
PRINTED_C=[1,0,3,6,24,68,191,1180,5944,29761,171778,1220908]


def oriented(p, case):
    n=len(p);h=n//2+1
    main=[i for i,c in enumerate(p,1) if i==c]
    anti=[i for i,c in enumerate(p,1) if i+c==n+1]
    if case=='a':return n%2 and not main and not anti and p.index(h)+1<p[h-1]<h
    if case=='b':return bool(main) and not anti and main[0]<h and p[-1]>p.index(n)+1
    return bool(main) and bool(anti) and main[0]<anti[0]<h


def problem(n,case):
    h=n//2+1
    assert case!='a' or n%2
    m=h-2 if case in ('a','c') else n-3
    numbers=sorted(range(1,n+1),key=lambda i:(abs(2*i-n-1),-i))
    prim=[v for i in numbers for v in [f'r{i}',f'c{i}']]
    if case in ('b','c'):prim+=['b0']
    if case=='c':prim+=[f'a{n+1}']
    secondary=[f'a{s}' for s in range(2,2*n+1)]+[f'b{d}' for d in range(1-n,n)]
    names=prim+[name for name in secondary if name not in prim]+[f'y{r}' for r in range(1,m)]
    index={name:i+1 for i,name in enumerate(names)}
    alpha={};beta={}
    for k in range(m):
        if case=='a':a,b=(k+1,h),(h,k+2)
        elif case=='b':a,b=(n,n-k-1),(n-k-2,n)
        else:a,b=(k+1,k+1),(k+2,n-k-1)
        alpha[a]=k;beta[b]=k
    rows=[];points=[]
    for c in range(1,n+1):
        for r in range(1,n+1):
            if case=='a':
                if r==c or r+c==n+1 or (c==h and r>c) or (r==h and c>r) or (r,c) in [(h-1,h),(h,1)]:continue
            elif case=='b':
                if r+c==n+1 or (r==c and r>=h) or (r,c) in [(n,2),(n-1,n)]:continue
            else:
                if (r==c and r>=h-1) or (r+c==n+1 and r>=h) or (r,c)==(1,n):continue
            row=[f'r{r}',f'c{c}',f'a{r+c}',f'b{r-c}']
            if (r,c) in alpha:row += [f'y{t}' for t in pair_lists(m,alpha[r,c])[0]]
            if (r,c) in beta:row += [f'y{t}' for t in pair_lists(m,beta[r,c])[1]]
            rows.append(tuple(index[name] for name in row));points.append((r,c))
    return names,rows,points,len(prim)


def main():
    validation=json.loads((OUT/'validation.json').read_text());binary=validation['binary']
    assert sha(binary)==validation['binary_sha256']
    large=json.loads((OUT/'large-wrapper.json').read_text());assert large['status']=='finished'
    for case in large['cases']:
        assert sha(OUT/(case['label']+'.json'))==case['result_sha256']
    oracle_counts={c['n']:c for c in validation['cases']}
    oracle_counts.update({n:json.loads((OUT/f'n{n}.json').read_text()) for n in range(11,18)})
    small_models={n:{tuple(p) for p in json.loads(subprocess.check_output([binary,str(n),'--models'],text=True))['models']}
                  for n in range(5,11)}
    cases=[]
    for case in ['a','b','c']:
        ns=range(5,18,2) if case=='a' else range(5,17)
        printed=PRINTED_A if case=='a' else PRINTED_B if case=='b' else PRINTED_C
        for n,book_count in zip(ns,printed):
            names,rows,points,primary=problem(n,case)
            stats,text=run(OUT,f'answer22{case}-n{n}',input_text(names,rows,primary),models=n<=10)
            assert stats['solutions']==oracle_counts[n]['cases']['22'+case]['oriented']
            result=dict(n=n,case=case,printed_count=book_count,**stats)
            if n<=10:
                expected={p for p in small_models[n] if oriented(p,case)}
                actual=set()
                for solution in decode_rows(text,names,rows):
                    board=sorted(points[r] for r in solution);assert valid(board,n)
                    p=tuple(c for r,c in board);assert p not in actual;actual.add(p)
                assert actual==expected
                result.update(full_model_sets_equal=True,model_set_sha256=hashlib.sha256(json.dumps(sorted(actual)).encode()).hexdigest())
            cases.append(result)
    discrepancies=[dict(n=c['n'],case=c['case'],printed=c['printed_count'],actual=c['solutions'])
                   for c in cases if c['solutions']!=c['printed_count']]
    assert discrepancies==[dict(n=16,case='c',printed=1220908,actual=1220918)]
    report=dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=sha(__file__),pair_helper_sha256=sha(ROOT/'check_dlx_ordering.py'),
        cases=cases,discrepancies=discrepancies,
        scope='31 full exact-cover counts agree with independent row-bit enumeration;15 small full model sets. '
              'General orbit proof in QUEEN_SYMMETRY_NOTES.md. Counts alone are not the general proof.')
    (OUT/'pair-verified.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(status=report['status'],cases=len(cases),discrepancies=discrepancies,
        largest=[dict(case=c['case'],n=c['n'],solutions=c['solutions'],mems=c['search_mems'])
                 for c in cases if c['n']==(17 if c['case']=='a' else 16)]),indent=2),flush=True)


if __name__=='__main__':main()
