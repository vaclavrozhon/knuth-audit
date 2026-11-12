"""Independently check the discrepant2x2x4 table, omitted sizes, and two hole witnesses."""
from datetime import datetime,timezone
from pathlib import Path
import gzip,json,re,subprocess,time
import bricks147 as h
import graph_native as native
from check_bricks147 import classification


def direct_models(path,dims):
    result=set();lines=path.read_text().splitlines()
    for line in lines[:-1]:
        fields=line.split();assert fields[0]=='M'
        row=tuple(h.cubes.WORDS[int(i)] for i in fields[1:]);h.validate(dims,row)
        assert row not in result;result.add(row)
    assert lines[-1].split()[0]=='C' and int(lines[-1].split()[1])==len(result)
    return result,int(lines[-1].split()[2])


def native_models(path,enc):
    lookup={tuple(sorted(r)):p for r,p in zip(enc['rows'],enc['placements'])};selected=None;result=[]
    def finish():result.append(tuple(selected[i] for i in range(len(selected))))
    for line in gzip.open(path,'rt'):
        if re.fullmatch(r'\d+:\s*',line):
            if selected is not None:finish()
            selected={}
        elif line.strip():
            fields=re.sub(r'\s*\(\d+ of \d+\)\s*$','',line).split();p=lookup[tuple(sorted(fields))]
            if 'position' in p:
                assert p['position'] not in selected;selected[p['position']]=p['word']
    if selected is not None:finish()
    assert len(set(result))==len(result)
    return set(result)


def irregular(holes):
    dims=(3,3,3);cells=[p for p in h.positions(dims) if p not in holes]
    facets=sorted({f for p in cells for f in h.faces(p)});label=lambda f:''.join(map(str,f))
    primary=[f'p{i}' for i in range(len(cells))]+[f'b{i}' for i in range(6)]
    secondary=h.cubes.TYPES+[label(f) for f in facets];rows=[];placements=[]
    for i,p in enumerate(cells):
        for w in h.cubes.WORDS:
            if i==0 and w!='abcdef':continue
            rows.append([f'p{i}',h.cubes.NAME[w]]+[label(f)+':'+c for f,c in zip(h.faces(p),w)])
            placements.append(dict(position=i,word=w))
    for b in range(6):
        for c in h.cubes.COLORS:
            rows.append([f'b{b}']+[label(f)+':'+c for f in facets if h.boundary(f,dims)==b]);placements.append(dict(boundary=b,color=c))
    return dict(header=primary+['|']+secondary,rows=rows,placements=placements),cells


def check_irregular(cells,row):
    assert len(row)==len(cells) and len({h.cubes.NAME[w] for w in row})==len(row)
    facets={};bounds={}
    for pos,w in zip(cells,row):
        assert sorted(w)==list(h.cubes.COLORS)
        for f,c in zip(h.faces(pos),w):
            if f in facets:assert facets[f]==c
            facets[f]=c;b=h.boundary(f,(3,3,3))
            if b is not None:
                if b in bounds:assert bounds[b]==c
                bounds[b]=c
    assert len(bounds)==6
    return [bounds[b] for b in range(6)]


def main():
    out=h.OUT/'followup';out.mkdir(exist_ok=True)
    assert not (out/'started.json').exists(),'No automatic rerun.'
    h.save(out/'started.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),script_sha256=h.sha(__file__),nice=15,limit_each_seconds=60))
    native.OUT=out
    build=json.loads((h.ROOT/'results/symmetry121_123/native/build.json').read_text())['binaries']['original']
    assert h.sha(build['binary'])==build['sha256']
    for dims in [(2,2,4),(3,3,3)]:
        label='native-'+'x'.join(map(str,dims));enc=h.native_problem(dims)
        h.save(out/(label+'-encoding.json'),enc)
        r=native.run(label,h.cubes.native_text(enc),binary=build['binary'],limit=60,every=1)
        if r['status']!='completed':print('INCOMPLETE',label,flush=True);continue
        models=native_models(out/(label+'.out.gz'),enc)
        for row in models:h.validate(dims,row)
        direct,nodes=direct_models(h.OUT/'bounded'/('x'.join(map(str,dims))+'.out'),dims)
        assert len(models)==r['solutions'] and models==direct
        h.save(out/(label+'-accepted.json'),dict(at_utc=datetime.now(timezone.utc).isoformat(),
            full_sets_equal=True,all_models_directly_valid=True,models=len(models),
            native_terminal_sha256=h.sha(out/(label+'.json')),checker_sha256=h.sha(__file__)))
        print('PASS independent literal book model',label,len(models),'whole sets equal',flush=True)
    direct_build=json.loads((h.OUT/'bounded/build.json').read_text());assert h.sha(direct_build['binary'])==direct_build['binary_sha256']
    for dims in [(2,2,6),(2,2,7)]:
        label='x'.join(map(str,dims));inp=out/(label+'.case');inp.write_text(h.direct_case(dims));start=time.monotonic()
        command=['timeout','60',direct_build['binary']]
        with inp.open('rb') as i,(out/(label+'.out')).open('wb') as o,(out/(label+'.log')).open('wb') as e:r=subprocess.run(command,stdin=i,stdout=o,stderr=e)
        meta=dict(dims=dims,returncode=r.returncode,command=command,status='completed' if r.returncode==0 else 'incomplete',
            elapsed_seconds=time.monotonic()-start,binary_sha256=direct_build['binary_sha256'],input_sha256=h.sha(inp),
            stdout_sha256=h.sha(out/(label+'.out')),stderr_sha256=h.sha(out/(label+'.log')))
        h.save(out/(label+'-run.json'),meta)
        if r.returncode:print('INCOMPLETE',label,flush=True);continue
        models,nodes=direct_models(out/(label+'.out'),dims)
        h.save(out/(label+'-checked.json'),dict(models=len(models),nodes=nodes,all_models_directly_valid=True,**classification(dims,models)))
        print('Additional size',label,'complete',len(models),'nodes',nodes,flush=True)
    for label,holes in [('without-corner',[(0,0,0)]),('without-middle-and-above',[(1,1,1),(1,0,1)])]:
        enc,cells=irregular(holes);h.save(out/(label+'-encoding.json'),enc)
        r=native.run(label,h.cubes.native_text(enc),binary=build['binary'],limit=60,every=1,extra=['t1'])
        if r['status']!='completed' or r.get('solutions')!=1:print('NO WITNESS WITHIN LIMIT',label,flush=True);continue
        models=native_models(out/(label+'.out.gz'),enc);assert len(models)==1;row=next(iter(models))
        bounds=check_irregular(cells,row)
        h.save(out/(label+'-witness.json'),dict(at_utc=datetime.now(timezone.utc).isoformat(),cells=cells,holes=holes,
            model=row,names=[h.cubes.NAME[w] for w in row],boundary=bounds,all_contacts_and_boundaries_valid=True,
            first_solution_only=True,complete_census=False,native_terminal_sha256=h.sha(out/(label+'.json')),checker_sha256=h.sha(__file__)))
        print('PASS first witness',label,len(row),'distinct cubes; no full census',flush=True)


if __name__=='__main__':main()
