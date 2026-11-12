"""New small oracle checks and four bounded counts; no cover optimization."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import random
import subprocess
import tempfile
import time
from puzzle_xcc import save, sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/usa239_246'


def components(mask, adjacency):
    result=[]
    while mask:
        component=frontier=mask&-mask
        while frontier:
            b=frontier&-frontier;frontier^=b
            new=adjacency[b.bit_length()-1]&mask&~component
            component|=new;frontier|=new
        mask^=component;result.append(component)
    return result


def encode(weights, adjacency, low, high):
    return f'{len(weights)} {low} {high}\n'+''.join(f'{w} {a}\n' for w,a in zip(weights,adjacency))


def main():
    assert os.nice(0)>=15
    assert not (OUT/'population-runs.json').exists()
    temp=Path(tempfile.mkdtemp(prefix='knuth-vol4b-usa-pop-'))
    binary=temp/'count';source=ROOT/'usa_population_options.cpp'
    command=['g++','-O3','-std=c++17',str(source),'-o',str(binary)]
    subprocess.run(command,check=True)
    randomizer=random.Random(239246);small=[]
    # Full subset oracle is independent of the frontier generation order.
    for case in range(30):
        n=3+case%8;weights=[randomizer.randrange(1,9) for _ in range(n)]
        adj=[0]*n
        for i in range(n):
            for j in range(i):
                if randomizer.randrange(3)==0:adj[i]|=1<<j;adj[j]|=1<<i
        low=randomizer.randrange(1,sum(weights)+1);high=low+randomizer.randrange(1,12)
        def pop(mask):return sum(weights[i] for i in range(n) if mask>>i&1)
        wanted=[];count=0
        for mask in range(1,1<<n):
            if low<=pop(mask)<high and len(components(mask,adj))==1:
                count+=1
                valid=True
                for c in components(((1<<n)-1)^mask,adj):
                    d=pop(c)
                    # Explicit number-of-parts feasibility, not the source formula.
                    valid &= any(k*low<=d<=k*(high-1) for k in range(1,d//low+1))
                if valid:wanted.append(mask)
        run=subprocess.run([str(binary)],input=encode(weights,adj,low,high),text=True,capture_output=True,check=True,timeout=5)
        actual=list(map(int,run.stdout.split()));terminal=json.loads(run.stderr)
        assert sorted(actual)==wanted
        assert terminal['interval_count']==count and terminal['reduced_count']==len(wanted)
        small.append(dict(n=n,weights=weights,adjacency=adj,low=low,high=high,oracle_interval=count,oracle_reduced=len(wanted),terminal=terminal))
    figures=json.loads((OUT/'figures.json').read_text());data=figures['data'];cases=[]
    report=dict(at_utc=datetime.now(timezone.utc).isoformat(),nice=os.nice(0),runner_sha256=sha(__file__),source_sha256=sha(source),
                binary_sha256=sha(binary),temp=str(temp),compile_command=command,figures_sha256=sha(OUT/'figures.json'),small_cases=small,cases=cases,status='running')
    save(OUT/'population-runs.json',report)
    for name,dc,low,high in [('pop38',False,37000000,39000000),('pop-broad8',False,34009354,43726312),
                             ('pop51',False,50500000,51500000),('pop44-dc',True,43000000,45000001)]:
        names=sorted(s for s in data['population'] if dc or s!='DC');index={s:i for i,s in enumerate(names)}
        weights=[data['population'][s] for s in names];adj=[0]*len(names)
        for a,b in data['edges']:
            if a in index and b in index:adj[index[a]]|=1<<index[b];adj[index[b]]|=1<<index[a]
        inp=OUT/(name+'.input');inp.write_text(encode(weights,adj,low,high))
        dest=OUT/(name+'.out');log=OUT/(name+'.log');t=time.monotonic()
        case=dict(name=name,states=names,low=low,high_exclusive=high,limit_seconds=20,nice=os.nice(0),input_sha256=sha(inp))
        with inp.open() as i,dest.open('w') as o,log.open('w') as e:
            child=subprocess.Popen([str(binary)],stdin=i,stdout=o,stderr=e)
            case['pid']=child.pid
            try:child.wait(timeout=20);case['returncode']=child.returncode
            except subprocess.TimeoutExpired:
                child.terminate();child.wait();case['status']='timeout_incomplete_not_unsat'
        case['wall_seconds']=time.monotonic()-t;case['output_sha256']=sha(dest);case['log_sha256']=sha(log)
        if case.get('returncode')==0:
            terminal=json.loads(log.read_text());assert terminal['complete']
            masks=list(map(int,dest.read_text().split()))
            assert len(masks)==len(set(masks))==terminal['reduced_count']
            # Validate a reproducible sample plus every printed option in this range.
            samples=randomizer.sample(masks,min(250,len(masks)))
            for mask in samples:
                total=sum(weights[i] for i in range(len(names)) if mask>>i&1)
                assert low<=total<high and len(components(mask,adj))==1
                for c in components(((1<<len(names))-1)^mask,adj):
                    d=sum(weights[i] for i in range(len(names)) if c>>i&1)
                    assert any(k*low<=d<=k*(high-1) for k in range(1,d//low+1))
            case.update(status='complete',terminal=terminal,independent_sample_masks=samples,all_output_masks_unique=True)
        else:assert case['status']=='timeout_incomplete_not_unsat'
        cases.append(case);save(OUT/'population-runs.json',report)
        print(name,case['status'],case['wall_seconds'],case.get('terminal'),flush=True)
        # A timeout is recorded, not retried; stop adding further enumeration work.
        if case['status']!='complete':break
    report['status']='finished';save(OUT/'population-runs.json',report)


if __name__=='__main__':main()
