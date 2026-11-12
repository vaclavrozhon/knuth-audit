#!/usr/bin/env python3
"""DLX72: exact counting identities and reproducible, independently solved samples."""
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from fractions import Fraction
import gzip
import json
import math
import platform
import random
import subprocess
import time
from dlx1_audit_tools import ROOT, sha, validated_binary, statistics, input_text
from check_dominosa_records import OUT, EDGES, PAIRS, build, tilings, instance

TRIALS = 10000
SEED = 202611020072


def zipped_json(path, records):
    with gzip.GzipFile(path,'wb',mtime=0) as f:
        for record in records:
            f.write((json.dumps(record,separators=(',',':'))+'\n').encode())


def summary(counts):
    n=len(counts);s=sum(counts);ss=sum(x*x for x in counts)
    return dict(trials=n,solvable=sum(x>0 for x in counts),unique=counts.count(1),
      maximum=max(counts),sum=s,sum_squares=ss,mean=s/n,
      population_sd=math.sqrt(ss/n-(s/n)**2),sample_sd=math.sqrt((ss-s*s/n)/(n-1)),
      histogram=dict(sorted(Counter(counts).items())))


def main():
    started=time.monotonic();OUT.mkdir(parents=True,exist_ok=True)
    build_info=build();native_binary=validated_binary();tiles=tilings(build_info)
    rng=random.Random(SEED);samples=[]
    for mode in ['i','ii']:
        for trial in range(TRIALS):
            if mode=='i':
                board=[x for x in range(7) for _ in range(8)]
                rng.shuffle(board);packing=None
            else:
                packing=rng.randrange(len(tiles));pieces=list(PAIRS);rng.shuffle(pieces)
                board=[None]*56
                for e,(x,y) in zip(tiles[packing],pieces):
                    if x!=y and rng.randrange(2):x,y=y,x
                    u,v=EDGES[e];board[u]=x;board[v]=y
                assert Counter(board)=={x:8 for x in range(7)}
            samples.append(dict(mode=mode,trial=trial,board=''.join(map(str,board)),packing=packing))
    zipped_json(OUT/'random-inputs.jsonl.gz',samples)
    print('Saved 20000 independently generated inputs; starting cell-first solver.',flush=True)
    p=subprocess.run([build_info['binary']],input='\n'.join(x['board'] for x in samples)+'\n',
                     text=True,capture_output=True,check=True,timeout=1800)
    cell=[json.loads(s) for s in p.stdout.splitlines()]
    assert len(cell)==len(samples)
    for s,c in zip(samples,cell):s['cell_search']=c
    zipped_json(OUT/'random-cell.jsonl.gz',samples)
    print('Cell-first solver finished; comparing every count with original DLX1.',flush=True)
    def native(sample):
        names,rows=instance(list(map(int,sample['board'])))
        p=subprocess.run([native_binary,'v129'],input=input_text(names,rows),text=True,
                         capture_output=True,check=True,timeout=120)
        assert not p.stdout
        stat=statistics(p.stderr)
        assert stat['solutions']==sample['cell_search']['count'],sample
        return stat
    with ThreadPoolExecutor(max_workers=2) as pool:
        for i,(sample,stat) in enumerate(zip(samples,pool.map(native,samples)),1):
            sample['native']=stat
            if i%2000==0:print('Independent complete counts agree:',i,flush=True)
    zipped_json(OUT/'random-checked.jsonl.gz',samples)
    M=math.factorial(56)//math.factorial(8)**7
    N=len(tiles)*math.factorial(28)*2**21
    ratio=Fraction(N,M)
    original={}
    for mode,s,ss in [('i',2256,95918),('ii',508506,144119964)]:
        original[mode]=dict(trials=10000,sum=s,sum_squares=ss,mean=s/10000,
          population_sd=math.sqrt(ss/10000-(s/10000)**2),
          sample_sd=math.sqrt((ss-s*s/10000)/9999),scope='Arithmetic only; original samples/seeds unavailable.')
    result=dict(status='verified',source_sha256=sha(__file__),build=build_info,
      native_binary=native_binary,native_binary_sha256=sha(native_binary),
      seed=SEED,python_version=platform.python_version(),trials_per_model=TRIALS,
      exact=dict(M=M,N=N,expected_model_i=str(ratio),expected_model_i_decimal=float(ratio)),
      original_moments=original,experiments={},
      inputs_sha256=sha(OUT/'random-inputs.jsonl.gz'),
      checked_samples_sha256=sha(OUT/'random-checked.jsonl.gz'),
      all_counts_independently_equal=True,
      scope='Fresh seeded samples for answer72 operational models. These do not reproduce historical samples or historical mem totals.')
    for mode in ['i','ii']:
        subset=[s for s in samples if s['mode']==mode]
        stats=summary([s['cell_search']['count'] for s in subset])
        stats['native_initialization_mems']=sum(s['native']['initialization_mems'] for s in subset)
        stats['native_search_mems']=sum(s['native']['search_mems'] for s in subset)
        # Wilson interval for the estimated uniqueness probability (95%).
        n=TRIALS;p=stats['unique']/n;z=1.959963984540054
        center=(p+z*z/(2*n))/(1+z*z/n)
        half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/(1+z*z/n)
        stats['unique_probability']=p;stats['unique_wilson95']=[center-half,center+half]
        result['experiments'][mode]=stats
        print(mode,{k:v for k,v in stats.items() if k!='histogram'},flush=True)
    result.update(checked_at_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-started)
    (OUT/'random-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: 20000 complete counts agree; exact identities and historical moment arithmetic checked.')


if __name__=='__main__':main()
