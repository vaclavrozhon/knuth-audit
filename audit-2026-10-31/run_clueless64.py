#!/usr/bin/env python3
"""Persist full DLX64 class census, validating every model and rare class."""
from datetime import datetime,timezone
import gzip
import json
import os
from pathlib import Path
import subprocess
import time
from dlx1_audit_tools import ROOT,sha,validated_binary,input_text,statistics,decode_rows,run
from check_jigsaw_small import instance,violations
from check_jigsaw_symmetry import maps

OUT=ROOT/'results/sudoku_extensions/clueless64'


def main():
    build=json.loads((OUT/'build.json').read_text())
    assert build['source_sha256']==sha(ROOT/'clueless_census.cc')
    assert build['binary_sha256']==sha(build['binary'])
    native=validated_binary()
    state=dict(status='running',pid=os.getpid(),source_sha256=sha(__file__),build=build,
               native=native,native_sha256=sha(native),started_at_utc=datetime.now(timezone.utc).isoformat(),cases={})
    def save(): (OUT/'run.json').write_text(json.dumps(state,indent=2)+'\n')
    save()
    for n in range(1,7):
        case=dict(status='running',input_sha256=sha(OUT/f'n{n}.masks'))
        state['cases'][str(n)]=case;state['active_case']=n
        command=[build['binary'],str(OUT/f'n{n}.masks')];case['command']=command
        start=time.monotonic()
        with (OUT/f'n{n}.jsonl').open('w')as out,(OUT/f'n{n}.log').open('w')as log:
            p=subprocess.Popen(command,stdout=out,stderr=log);case['pid']=p.pid;save()
            p.wait(timeout=3600);assert p.returncode==0
        case['summary']=json.loads((OUT/f'n{n}.log').read_text());save()
        rows=[json.loads(s)for s in (OUT/f'n{n}.jsonl').read_text().splitlines()]
        assert len(rows)==len({x['regions']for x in rows})==case['summary']['classes']
        weight=0;witnesses=0;rare=[]
        with gzip.open(OUT/f'n{n}-native-rare.log.gz','wt')as log:
            for x in rows:
                key=x['regions'];regions=[[i for i,c in enumerate(key)if c==str(j)]for j in range(n)]
                assert len(key)==n*n and all(len(r)==n for r in regions)
                # Independent coordinate checks: connected cells and D4 orbit.
                for r in regions:
                    seen={r[0]}
                    while True:
                        more=seen|{v for v in r if any(abs(v//n-w//n)+abs(v%n-w%n)==1 for w in seen)}
                        if more==seen:break
                        seen=more
                    assert seen==set(r)
                transforms=[]
                for m in maps(n):
                    changed=['']*(n*n)
                    for v,c in enumerate(key):changed[m[v]]=c
                    labels={};encoded=''
                    for c in changed:
                        if c not in labels:labels[c]=str(len(labels))
                        encoded+=labels[c]
                    transforms.append(encoded)
                assert key==min(transforms)and transforms.count(key)==x['stabilizer']
                weight+=8//x['stabilizer']
                d=dict(nrows=n,ncols=n,cells=list('123456'[:n]+'.'*(n*n-n)),omitted=[],regions=regions)
                for sol in x['solutions']:
                    assert sol[:n]=='123456'[:n]and not violations(d,sol)
                    assert all(set(sol[v]for v in u)==set('123456'[:n])for u in regions)
                    witnesses+=1
                assert len(set(x['solutions']))==len(x['solutions'])
                if len(x['solutions'])<2 and n>1:
                    names,opts,moves,primary=instance(d,'123456'[:n])
                    data=input_text(names,opts,primary)
                    p=subprocess.run([native,'v129','m1','t2'],input=data,text=True,capture_output=True,check=True,timeout=60)
                    stats=statistics(p.stderr)
                    assert stats['solutions']==len(x['solutions']),(n,key,stats)
                    actual=[]
                    for selected in decode_rows(p.stdout,names,opts):
                        board=list(d['cells'])
                        for r in selected:v,k=moves[r];board[v]=k
                        actual.append(''.join(board))
                    assert sorted(actual)==x['solutions']
                    rare.append(dict(regions=key,solutions=stats['solutions'],nodes=stats['nodes'],input_sha256=sha_bytes(data)))
                    log.write(key+'\n'+p.stderr+p.stdout)
        assert weight==case['summary']['packings']
        # A complete unmodified-DLX1 tiling count, independent of our census.
        tokens=(OUT/f'n{n}.masks').read_text().split();masks=[int(t,16)for t in tokens[2:]]
        matrix=[[v+1 for v in range(n*n)if mask>>v&1]for mask in masks]
        native_count,_=run(OUT/'packings',f'n{n}',input_text([f'p{r}{c}'for r in range(n)for c in range(n)],matrix),timeout=600)
        assert native_count['solutions']==weight
        (OUT/f'n{n}-rare-checks.json').write_text(json.dumps(rare,indent=2)+'\n')
        case.update(status='verified',elapsed_seconds=time.monotonic()-start,models_sha256=sha(OUT/f'n{n}.jsonl'),
                    coordinate_witnesses_validated=witnesses,rare_native_checks=len(rare),
                    rare_checks_sha256=sha(OUT/f'n{n}-rare-checks.json'),native_tiling_count=native_count,
                    rare_log_sha256=sha(OUT/f'n{n}-native-rare.log.gz'))
        save();print('PASS n',n,case['summary'],'rare native',len(rare),flush=True)
    state.update(status='verified',active_case=None,finished_at_utc=datetime.now(timezone.utc).isoformat());save()


def sha_bytes(s):
    import hashlib
    return hashlib.sha256(s.encode()).hexdigest()


if __name__=='__main__':main()
