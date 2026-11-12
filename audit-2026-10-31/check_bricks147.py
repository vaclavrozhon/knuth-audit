"""Short brick censuses; stop the larger catalogue at the first time limit."""
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
import json,shutil,subprocess,tempfile,time
import bricks147 as h


def classification(dims,models):
    remaining=set(models);orbits=[]
    while remaining:
        row=min(remaining);acted=h.orbit(dims,row);orbit=set(acted)
        assert orbit<=remaining and orbit<=models
        stabilizer=acted.count(row);assert len(orbit)*stabilizer==len(acted)
        _,bounds=h.validate(dims,row)
        repeat=tuple(bounds[2*i]==bounds[2*i+1] for i in range(3))
        # Only equal-length axes may be exchanged.
        repeat=max(tuple(repeat[p[i]] for i in range(3)) for p,sgn,perm in h.group(dims))
        orbits.append(dict(model=row,size=len(orbit),automorphisms=stabilizer,repeat_axes=repeat,boundary=bounds))
        remaining-=orbit
    hist={}
    for r in orbits:
        key=''.join('1' if b else '0' for b in r['repeat_axes']);hist.setdefault(key,Counter())[r['automorphisms']]+=1
    return dict(orbits=orbits,histogram={k:dict(v) for k,v in hist.items()},spatial_group_size=len(h.group(dims)))


def main():
    out=h.OUT/'bounded';out.mkdir(exist_ok=True)
    assert not (out/'started.json').exists(),'No automatic rerun.'
    h.save(out/'started.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=h.sha(__file__),nice=15,per_case_limit_seconds=60))
    temp=Path(tempfile.mkdtemp(prefix='knuth-vol4b-bricks147-cpp-'));source=h.ROOT/'count_bricks147.cpp';copy=temp/source.name;shutil.copy2(source,copy);binary=temp/'count'
    command=['g++','-O3','-std=c++17',str(copy),'-o',str(binary)]
    with (out/'build.log').open('w') as s:r=subprocess.run(command,stdout=s,stderr=s)
    assert r.returncode==0
    h.save(out/'build.json',dict(command=command,source_sha256=h.sha(source),binary=str(binary),binary_sha256=h.sha(binary)))
    cases=[(1,1,1),(1,1,2),(1,1,3),(1,2,2),(1,2,3),(2,2,2),(2,2,3),(2,2,4),(2,2,5),(2,3,3),(2,3,4),(2,3,5),(3,3,3)]
    accepted=[];interrupted=None
    for dims in cases:
        label='x'.join(map(str,dims));inp=out/(label+'.case');inp.write_text(h.direct_case(dims))
        command=['timeout','60',str(binary)];start=time.monotonic()
        with inp.open('rb') as i,(out/(label+'.out')).open('wb') as o,(out/(label+'.log')).open('wb') as e:
            r=subprocess.run(command,stdin=i,stdout=o,stderr=e)
        meta=dict(dims=dims,status='completed' if r.returncode==0 else 'incomplete',returncode=r.returncode,command=command,
            elapsed_seconds=time.monotonic()-start,source_sha256=h.sha(source),binary_sha256=h.sha(binary),
            input_sha256=h.sha(inp),stdout_sha256=h.sha(out/(label+'.out')),stderr_sha256=h.sha(out/(label+'.log')))
        h.save(out/(label+'-run.json'),meta)
        if r.returncode:
            interrupted=label;print('INCOMPLETE',label,'rc',r.returncode,'larger cases not started.',flush=True);break
        lines=(out/(label+'.out')).read_text().splitlines();models=set()
        for line in lines[:-1]:
            t=line.split();assert t[0]=='M';row=tuple(h.cubes.WORDS[int(i)] for i in t[1:]);h.validate(dims,row)
            assert row[0]=='abcdef' and row not in models;models.add(row)
        terminal=lines[-1].split();assert terminal[0]=='C' and len(models)==int(terminal[1]);nodes=int(terminal[2])
        classified=classification(dims,models)
        result=dict(dims=dims,models=len(models),nodes=nodes,all_models_directly_valid=True,
            terminal_sha256=h.sha(out/(label+'-run.json')),geometry_sha256=h.sha(h.__file__),checker_sha256=h.sha(__file__),**classified)
        h.save(out/(label+'-checked.json'),result);accepted.append(label)
        print('COMPLETE',label,'models',len(models),'orbits',len(classified['orbits']),'nodes',nodes,'seconds',meta['elapsed_seconds'],'hist',classified['histogram'],flush=True)
    h.save(out/'batch-status.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),completed=accepted,interrupted=interrupted,
        deliberately_not_started=['x'.join(map(str,d)) for d in cases[len(accepted)+(1 if interrupted else 0):]],
        no_timeout_inferred_as_unsatisfiable=True,no_restarts=True))


if __name__=='__main__':main()
