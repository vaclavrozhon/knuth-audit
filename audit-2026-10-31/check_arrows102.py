"""General stable-labeling reduction, finite oracle, and original pi-day input."""
from collections import Counter
from itertools import product
from pathlib import Path
import json
import random
import re
import subprocess
import tempfile
from colored_dlx import ColoredDLX
from check_zebra101 import NoEvents
from puzzle_xcc import ROOT, OUT, COLORS, encode, native, read_models, colors_for, save, sha


def instance(adj, given):
    n=len(adj); delta=max(map(len,adj),default=0)
    pred=[[u for u in range(n) if v in adj[u]] for v in range(n)]
    primary=[name for v in range(n) for name in [f'H{v}',f'I{v}']]
    primary += [f'E{v}d{d}' for v in range(n) for d in range(delta+1)]
    secondary=[f'v{v}' for v in range(n)]
    secondary += [f'{c}{v}d{d}' for v in range(n) for d in range(delta+1) for c in 'hi']
    rows=[]
    for v in range(n):
        for mask in range(1<<(delta+1)):
            d=mask.bit_count()
            if d>len(adj[v]) or (v in given and d!=given[v]):continue
            rows.append([(f'H{v}',0),(f'v{v}',d+1)] +
                        [(f'h{v}d{k}',1+((mask>>k)&1)) for k in range(delta+1)])
        for d in range(len(adj[v])+1):
            if v in given and d!=given[v]:continue
            rows.append([(f'I{v}',0),(f'v{v}',d+1)] +
                        [(f'i{v}d{k}',1+int(k==d)) for k in range(delta+1)] +
                        [(f'h{u}d{d}',2) for u in pred[v]])
        for d in range(delta+1):
            for k,w in enumerate(adj[v]):
                rows.append([(f'E{v}d{d}',0),(f'h{v}d{d}',2),(f'i{w}d{d}',2)] +
                            [(f'i{u}d{d}',1) for u in adj[v][:k]])
            rows.append([(f'E{v}d{d}',0),(f'h{v}d{d}',1)] +
                        [(f'i{w}d{d}',1) for w in adj[v]])
    return encode(primary,secondary,rows)


def oracle(adj,given):
    return {labels for labels in product(*(range(len(a)+1) for a in adj))
            if all(labels[v]==d for v,d in given.items()) and
            all(labels[v]==len({labels[w] for w in a}) for v,a in enumerate(adj))}


def small_checks():
    checked=models=empty=self_loops=sinks=0
    def check(adj,given):
        nonlocal checked,models,empty,self_loops,sinks
        enc=instance(adj,given)
        dlx=ColoredDLX(len(enc['names']),enc['primary'],enc['rows'])
        dlx.events=NoEvents();dlx.solve()
        actual=[]
        for model in dlx.solutions:
            colors=colors_for(enc,model)
            actual.append(tuple(colors[f'v{v}']-1 for v in range(len(adj))))
        expected=oracle(adj,given)
        assert len(actual)==len(set(actual)) and set(actual)==expected,(adj,given,expected,actual)
        for labels in expected:
            assert all(len(a)>1 or labels[v]==len(a) for v,a in enumerate(adj))
            for u in range(len(adj)):
                for v in range(len(adj)):
                    if set(adj[v])<=set(adj[u]):assert labels[u]>=labels[v]
        checked+=1;models+=len(actual);empty+=not actual
        self_loops+=any(v in a for v,a in enumerate(adj));sinks+=any(not a for a in adj)
    for n in range(1,4):
        for mask in range(1<<(n*n)):
            adj=[[w for w in range(n) if mask&(1<<(n*v+w))] for v in range(n)]
            check(adj,{})
            for v in range(n):
                for d in range(n+1):check(adj,{v:d})
    rng=random.Random(102)
    for _ in range(200):
        n=rng.choice([4,5])
        adj=[[w for w in range(n) if rng.randrange(4)==0] for v in range(n)]
        given={v:rng.randrange(n+1) for v in range(n) if rng.randrange(3)==0}
        check(adj,given)
    return dict(instances=checked,models=models,unsatisfiable=empty,
                instances_with_self_loops=self_loops,instances_with_sinks=sinks,
                coverage='Every directed simple graph with loops on1..3 vertices, no fixed label and every one-vertex fixed label in0..n;200 seeded graphs on4/5 vertices.')


def pi_graph():
    source=ROOT/'sources/questionnaires/back-pi-day.w'
    text=re.search(r'char johan\[10\]\[10\]=\{(.*?)\};',source.read_text(),re.S).group(1)
    cells=re.findall(r'([NSEW])\+(\d)',text)
    assert len(cells)==100
    adj=[];given={}
    for v,(direction,digit) in enumerate(cells):
        i,j=divmod(v,10)
        successors={'N':[10*k+j for k in range(i)],'S':[10*k+j for k in range(i+1,10)],
                    'E':[10*i+k for k in range(j+1,10)],'W':[10*i+k for k in range(j)]}[direction]
        adj.append(successors)
        if int(digit):given[v]=int(digit)
        if len(successors)<=1:given[v]=len(successors)
    parallel=sum(cells[u][0]==cells[v][0] and
                 ((u//10==v//10 and cells[u][0] in 'EW') or (u%10==v%10 and cells[u][0] in 'NS'))
                 for u in range(100) for v in range(u+1,100))
    assert parallel==123
    return adj,given,cells


def original_generator():
    source=ROOT/'sources/puzzles101_107/pi-day-dlx.w'
    directory=Path(tempfile.mkdtemp(prefix='knuth-vol4b-piday-',dir='/tmp'))
    commands=[['ctangle',str(source),'-',str(directory/'pi-day-dlx.c')],
              ['gcc','-O2','-std=gnu99','-Wno-implicit-int',str(directory/'pi-day-dlx.c'),'-o',str(directory/'pi-day-dlx')]]
    builds=[]
    for command in commands:
        p=subprocess.run(command,capture_output=True,text=True)
        builds.append(dict(command=command,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr))
        assert p.returncode==0,p.stderr
    generated=subprocess.run([str(directory/'pi-day-dlx')],capture_output=True,text=True,timeout=30)
    assert generated.returncode==0,generated.stderr
    path=OUT/'pi-day-generated.dlx';path.write_text(generated.stdout)
    save(OUT/'pi-day-build.json',dict(source_sha256=sha(source),builds=builds,
         binary_sha256=sha(directory/'pi-day-dlx'),input_sha256=sha(path),
         returncode=generated.returncode,stderr=generated.stderr))
    lines=[line for line in generated.stdout.splitlines() if line.strip() and not line.startswith('|')]
    first=lines[0].split();bar=first.index('|')
    rows=[]
    for line in lines[1:]:
        row=[]
        for token in line.split():
            name,sep,color=token.partition(':')
            row.append((name,COLORS.index(color)+1 if sep else 0))
        rows.append(row)
    return encode(first[:bar],first[bar+1:],rows)


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    small=small_checks();save(OUT/'arrows-small.json',small)
    print('Small graph checks:',small,flush=True)
    enc=original_generator()
    assert (enc['primary'],len(enc['names'])-enc['primary'],len(enc['rows']))==(880,1216,11351)
    result=native('pi-day-author',enc,limit=600)
    assert result['status']=='completed' and result['solutions']==1
    models=read_models('pi-day-author',enc)
    colors=colors_for(enc,next(iter(models)))
    labels=tuple(colors[f'{v:02d}']-1 for v in range(100))
    adj,given,cells=pi_graph()
    assert all(labels[v]==len({labels[w] for w in adj[v]}) for v in range(100))
    assert all(labels[v]==d for v,d in given.items())
    previous=json.loads((ROOT/'results/questionnaires/pi-day-verified.json').read_text())
    assert labels==tuple(previous['solution'][str(v)] for v in range(100))
    # Printed sample options, derived directly from the verified solution.
    sees={labels[w] for w in adj[0]}
    assert labels[0]==3 and sees=={4,7,9}
    assert [u for u in range(100) if 0 in adj[u]]==[1,3,5,70,80]
    assert all(labels[10*j]!=4 for j in range(1,5)) and labels[50]==4
    save(OUT/'arrows-checked.json',dict(script_sha256=sha(__file__),small_graphs=small,
         pi_day=dict(primary=enc['primary'],secondary=len(enc['names'])-enc['primary'],
                     options=len(enc['rows']),solutions=1,labels=labels,parallel_arrow_pairs=123,
                     initial_mems=result['initial_mems'],search_mems=result['net_search_mems'],nodes=result['nodes']),
         original_model_agrees_with_independent_equations_and_earlier_stability_solution=True,
         sample_H00_I00_E004_verified=True))
    print('Pi day original XCC:',result['initial_mems'],result['net_search_mems'],result['nodes'])


if __name__=='__main__':main()
