#!/usr/bin/env python3
"""DLX69: all original districts and complete capacity-constrained covers."""
from collections import Counter
from datetime import datetime,timezone
import gzip
import json
import re
import subprocess
import time
import extract_jigsaw as geometry
from dlx1_audit_tools import ROOT,sha,decode_rows,statistics
from prepare_convex68 import convex,bounded
from check_sudoku_multiplicity import build

OUT=ROOT/'results/convex68'


def capacity_covers(tiles,kinds,target):
    masks=[sum(1<<v for v in tile) for tile in tiles]
    incidence=[[i for i,t in enumerate(tiles) if v in t] for v in range(81)]
    remaining=dict(target);models=set();nodes=0
    def visit(uncovered,chosen):
        nonlocal nodes
        nodes+=1
        if not uncovered:
            assert not any(remaining.values())
            models.add(tuple(sorted(chosen)));return
        best=None
        scan=uncovered
        while scan:
            bit=scan&-scan;scan-=bit;v=bit.bit_length()-1
            choices=[i for i in incidence[v] if remaining.get(kinds[i],0)
                     and masks[i]&uncovered==masks[i]]
            if best is None or len(choices)<len(best):best=choices
            if not choices:return
        for i in best:
            remaining[kinds[i]]-=1
            visit(uncovered^masks[i],chosen+[i])
            remaining[kinds[i]]+=1
    visit((1<<81)-1,[])
    return models,nodes


def main():
    start=time.monotonic();geometry.OUT=OUT
    diagrams={}
    for label,page,x,y,step in [('69i',131,121.92,174.42,76.2/9),
                              ('69ii',131,263.28,174.42,76.2/9),
                              ('69a',431,348.69,71.689,57.101/9)]:
        d=geometry.extract(page,9,9,x,y,step,'BL');diagrams[label]=d
        assert len(d['regions'])==9 and all(len(t)==9 for t in d['regions'])
    board=diagrams['69i']['cells']
    assert all(d['cells']==board for d in diagrams.values()) and Counter(board)=={'B':36,'L':45}
    district_counts={label:sorted(sum(board[v]=='B' for v in t) for t in d['regions'])
                     for label,d in diagrams.items()}
    assert district_counts['69i']==[4]*9
    assert all(sum(k>=5 for k in district_counts[label])==7 for label in ['69ii','69a'])
    options=json.loads((OUT/'options.json').read_text())
    assert sha(OUT/'n9.json.gz')==options['cases']['n9']['json_sha256']
    tiles=sorted(map(tuple,json.loads(gzip.decompress((OUT/'n9.json.gz').read_bytes()))))
    kinds=[sum(board[v]=='B' for v in t) for t in tiles]
    counts=Counter(kinds)
    assert [counts[k] for k in (6,5,1,0)]==[1647,2362,163,2]
    printed=tuple(sorted(tiles.index(tuple(t)) for t in diagrams['69a']['regions']))
    assert all(convex([(v%9,v//9) for v in t]) and bounded([(v%9,v//9) for v in t],4)
               for t in diagrams['69a']['regions'])
    nativebuild=build();result=dict(status='running',source_sha256=sha(__file__),
      geometry_helper_sha256=sha(ROOT/'extract_jigsaw.py'),
      source_pdf_sha256=sha(geometry.BOOK),placement_sha256=sha(OUT/'n9.json.gz'),
      diagrams=diagrams,district_B_counts=district_counts,placement_B_counts=dict(counts),
      printed_relevant_counts=[1467,2362,163,2],actual_relevant_counts=[1647,2362,163,2],cases={})
    for label,target,expected in [('case1',{6:1,5:6,0:2},0),('case2',{5:7,1:1,0:1},60)]:
        selected=[i for i,k in enumerate(kinds) if k in target]
        local_tiles=[tiles[i] for i in selected];local_kinds=[kinds[i] for i in selected]
        independent,nodes=capacity_covers(local_tiles,local_kinds,target)
        names=[f'p{r}{c}' for r in range(9) for c in range(9)]+[f'N{k}' for k in target]
        index={name:i+1 for i,name in enumerate(names)}
        rows=[[v+1 for v in t]+[index[f'N{k}']] for t,k in zip(local_tiles,local_kinds)]
        header=names[:81]+[f'{target[k]}|N{k}' for k in target]
        data='\n'.join([' '.join(header)]+[' '.join(names[v-1] for v in row) for row in rows])+'\n'
        (OUT/(label+'.mcc')).write_text(data)
        command=[nativebuild['binary'],'v129','m1']
        run=subprocess.run(command,input=data,text=True,capture_output=True,check=True,timeout=600)
        (OUT/(label+'.log')).write_text(run.stderr);(OUT/(label+'.models')).write_text(run.stdout)
        native=decode_rows(run.stdout,names,rows)
        stats=statistics(re.sub(r', \d+ cleansings','',run.stderr))
        assert native==independent and len(native)==expected==stats['solutions']
        expanded=set()
        for model in native:
            cells=[v for i in model for v in local_tiles[i]]
            assert len(cells)==81 and set(cells)==set(range(81))
            assert Counter(local_kinds[i] for i in model)==target
            expanded.add(tuple(sorted(selected[i] for i in model)))
        if label=='case2':assert printed in expanded
        result['cases'][label]=dict(target=target,solutions=len(native),independent_nodes=nodes,
           full_sets_equal=True,native=stats,command=command,binary_sha256=nativebuild['binary_sha256'],
           input_sha256=sha(OUT/(label+'.mcc')),models_sha256=sha(OUT/(label+'.models')),
           complete_models=sorted(expanded))
        print(label,len(native),'full model sets agree',flush=True)
    result.update(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-start)
    (OUT/'bitland69.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: all three diagrams, all counts, all60 solutions',flush=True)


if __name__=='__main__':main()
