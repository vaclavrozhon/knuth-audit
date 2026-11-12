#!/usr/bin/env python3
"""DLX27: literal secondary-item gadgets against independent crossing graphs."""
from collections import Counter, deque
from datetime import datetime, timezone
from itertools import combinations, product
import hashlib
import json

from check_langford_algorithm import oracle, valid
from dlx1_audit_tools import ROOT, sha, input_text, run, decode_rows

OUT=ROOT/'results/planar_langford'
EXAMPLE=(12,10,8,6,4,11,9,7,5,4,6,8,10,12,5,7,9,11,3,1,2,1,3,2)


def gadget(i,j):
    h=(i+1)//2; k=j+i+1
    cells=[(j,t) for t in range(1,h+1)]+[(x,h) for x in range(j+1,k+1)]
    cells += [(k,t) for t in range(h-1,0,-1)]
    assert len(cells)==len(set(cells))
    return tuple(cells)


def intervals(sequence):
    n=len(sequence)//2
    result=[]
    for i in range(1,n+1):
        pos=[j+1 for j,x in enumerate(sequence) if x==i]
        assert len(pos)==2 and pos[1]-pos[0]==i+1
        result.append(tuple(pos))
    assert len(sequence)==2*n and set(sequence)==set(range(1,n+1))
    return result


def cross(a,b):
    j,k=a; p,q=b
    return j<p<k<q or p<j<q<k


def page_assignments(sequence):
    """All 2-colorings of the interval-crossing graph, fixing label n above."""
    arcs=intervals(sequence); n=len(arcs)
    adjacency=[[] for _ in arcs]
    for i,j in combinations(range(n),2):
        if cross(arcs[i],arcs[j]): adjacency[i].append(j);adjacency[j].append(i)
    colors=[None]*n;components=[]
    for root in range(n):
        if colors[root] is not None: continue
        colors[root]=0;component=[];queue=deque([root])
        while queue:
            u=queue.popleft();component.append(u)
            for v in adjacency[u]:
                if colors[v] is None: colors[v]=1-colors[u];queue.append(v)
                elif colors[v]==colors[u]: return set(),components+[component]
        components.append(component)
    out=set()
    fixed=next(i for i,c in enumerate(components) if n-1 in c)
    for free in product([0,1],repeat=len(components)-1):
        flips=list(free);flips.insert(fixed,colors[n-1])
        result=list(colors)
        for c,flip in zip(components,flips):
            for v in c: result[v]^=flip
        assert result[n-1]==0
        out.add(tuple(result))
    assert len(out)==2**(len(components)-1)
    return out,components


def encoding(n,sequence=None):
    names=[f'L{i}' for i in range(1,n+1)]+[f'S{j}' for j in range(1,2*n+1)]
    primary=len(names)
    names += [f'{side}{j}_{h}' for side in ['u','d']
              for j in range(1,2*n+1) for h in range(1,(n+1)//2+1)]
    index={name:i+1 for i,name in enumerate(names)}
    rows=[];metadata=[]
    prescribed=intervals(sequence) if sequence else None
    for i in range(1,n+1):
        for j in range(1,2*n-i):
            if prescribed and j!=prescribed[i-1][0]:continue
            for side in range(1 if i==n else 2):
                prefix='ud'[side]
                row=[i,n+j,n+j+i+1]+[index[f'{prefix}{x}_{h}'] for x,h in gadget(i,j)]
                assert len(row)==len(set(row))
                rows.append(tuple(row));metadata.append((i,j,side))
    return names,rows,primary,metadata


def decode(models,metadata,n):
    out=set()
    for model in models:
        assert len(model)==n
        sequence=[0]*(2*n);sides=[None]*n
        for r in model:
            i,j,side=metadata[r];k=j+i+1
            assert sides[i-1] is None and sequence[j-1]==sequence[k-1]==0
            sides[i-1]=side;sequence[j-1]=sequence[k-1]=i
        sequence=tuple(sequence);sides=tuple(sides)
        assignments,_=page_assignments(sequence)
        assert sides in assignments
        key=sequence,sides
        assert key not in out;out.add(key)
    return out


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    pair_checks=0;pair_summary=[]
    for n in range(1,17):
        choices=[(i,j,j+i+1,frozenset(gadget(i,j)))
                 for i in range(1,n+1) for j in range(1,2*n-i)]
        count=0
        for a,b in combinations(choices,2):
            if len({a[1],a[2],b[1],b[2]})<4:continue
            assert bool(a[3]&b[3])==cross(a[1:3],b[1:3])
            count+=1
        pair_checks+=count;pair_summary.append(dict(n=n,endpoint_disjoint_pairs=count))
    cases=[]
    for n in range(1,12):
        ordinary=oracle(n)
        expected=set()
        for signed in ordinary:
            assert valid(signed)
            sequence=tuple(map(abs,signed));assignments,_=page_assignments(sequence)
            expected.update((sequence,sides) for sides in assignments)
        names,rows,primary,metadata=encoding(n)
        stats,text=run(OUT,f'n{n}',input_text(names,rows,primary),models=True)
        actual=decode(decode_rows(text,names,rows),metadata,n)
        assert actual==expected and len(actual)==stats['solutions']
        counts=Counter(sequence for sequence,sides in actual)
        cases.append(dict(n=n,ordinary_sequences=len(ordinary),planar_sequences=len(counts),
            page_assignments=len(actual),multiplicity_histogram=dict(Counter(counts.values())),
            full_model_sets_equal=True,**stats,
            models_sha256=hashlib.sha256(json.dumps(sorted(actual)).encode()).hexdigest()))
        print(dict(n=n,ordinary=len(ordinary),planar=len(counts),models=len(actual)),flush=True)
    names,rows,primary,metadata=encoding(12,EXAMPLE)
    stats,text=run(OUT,'n12-printed-example',input_text(names,rows,primary),models=True)
    models=decode(decode_rows(text,names,rows),metadata,12)
    expected,components=page_assignments(EXAMPLE)
    assert models=={(EXAMPLE,sides) for sides in expected} and len(models)>1
    report=dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=sha(__file__),helper_sha256=sha(ROOT/'dlx1_audit_tools.py'),
        ordinary_oracle_sha256=sha(ROOT/'check_langford_algorithm.py'),
        gadget_pair_checks=pair_checks,pair_summary=pair_summary,cases=cases,
        printed_example=dict(sequence=EXAMPLE,components=[[v+1 for v in c] for c in components],
                             page_assignments=sorted(expected),**stats),
        scope='General gadget-intersection and crossing-graph proofs in PLANAR_LANGFORD_PROGRESS_NOTES.md; '
              'all model sets n1..11; prescribed n12 split example. The historical missing8 correction is already applied.')
    (OUT/'verified.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(status='verified',gadget_pair_checks=pair_checks,
                          example_components=report['printed_example']['components'],
                          example_multiplicity=len(models)),indent=2),flush=True)


if __name__=='__main__':main()
