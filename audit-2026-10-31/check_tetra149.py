"""Two bounded, independent complete censuses; exact model-set comparison."""
from datetime import datetime,timezone
from itertools import combinations,permutations
from pathlib import Path
import json,os,re,subprocess,tempfile,time
import tetra149 as h
import puzzle_xcc as xcc


def main():
    out=h.OUT/'bounded';out.mkdir(exist_ok=True)
    assert not (out/'started.json').exists(),'Never silently restart a previous search.'
    assert os.getpriority(os.PRIO_PROCESS,0)>=15
    start=time.monotonic()
    xcc.save(out/'started.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),pid=os.getpid(),nice=os.getpriority(os.PRIO_PROCESS,0),
        checker_sha256=xcc.sha(__file__),geometry_sha256=xcc.sha(h.__file__),cpp_sha256=xcc.sha(h.ROOT/'count_tetra149.cpp'),timeout_seconds_per_method=60))
    assert len(h.EVEN)==12 and len(h.WORDS)==120 and len(h.TYPES)==10
    cells={tuple(sorted((v,w))) for ids in h.CORNERS for v,w in combinations(ids,2)}
    nearest={tuple(sorted((i,j))) for i,v in enumerate(h.VERTICES) for j,w in enumerate(h.VERTICES)
        if i<j and sum(abs(a-b) for a,b in zip(v,w))==2}
    assert cells==nearest and len(cells)==60
    assert sum(len(list(combinations(ids,2))) for ids in h.CORNERS)==60
    assert max(len(set(a)&set(b)) for a,b in combinations(h.CORNERS,2))==1
    case=out/'vertices.case';case.write_text('\n'.join(' '.join(map(str,c)) for c in h.CORNERS)+'\n')
    build=Path(tempfile.mkdtemp(prefix='knuth-vol4b-tetra149-build-'));binary=build/'vertex-colors'
    cmd=['g++','-std=c++17','-O2','-Wall','-Wextra',str(h.ROOT/'count_tetra149.cpp'),'-o',str(binary)]
    compiled=subprocess.run(cmd,capture_output=True,text=True,timeout=60)
    (out/'compile.log').write_text(compiled.stdout+compiled.stderr);assert compiled.returncode==0
    command=['timeout','60',str(binary)];t=time.monotonic()
    with case.open('rb') as fin,(out/'independent.out').open('wb') as fout,(out/'independent.log').open('wb') as ferr:
        proc=subprocess.Popen(command,stdin=fin,stdout=fout,stderr=ferr)
        xcc.save(out/'independent-run.json',dict(status='running',wrapper_pid=os.getpid(),pid=proc.pid,command=command,
            started_at_utc=datetime.now(timezone.utc).isoformat(),timeout_seconds=60,input_sha256=xcc.sha(case),binary_sha256=xcc.sha(binary),source_sha256=xcc.sha(h.ROOT/'count_tetra149.cpp')))
        rc=proc.wait()
    meta=json.loads((out/'independent-run.json').read_text());meta.update(returncode=rc,status='completed' if rc==0 else 'incomplete',
        elapsed_seconds=time.monotonic()-t,finished_at_utc=datetime.now(timezone.utc).isoformat(),stdout_sha256=xcc.sha(out/'independent.out'),stderr_sha256=xcc.sha(out/'independent.log'))
    xcc.save(out/'independent-run.json',meta);assert rc==0,('Incomplete; do not restart',rc)
    count,nodes=map(int,re.fullmatch(r'COMPLETED (\d+) (\d+)\n',(out/'independent.log').read_text()).groups())
    models=(out/'independent.out').read_text().splitlines();assert len(models)==len(set(models))==count
    expanded=set()
    for m in models:
        h.validate(m);assert ''.join(m[i] for i in h.CORNERS[0])=='abcd'
        for p in permutations('abcde'): expanded.add(m.translate(str.maketrans('abcde',''.join(p))))
    assert len(expanded)==120*count
    xcc.OUT=out;enc=h.encoding();assert enc['primary']==20 and len(enc['names'])==40 and len(enc['rows'])==1200
    native=xcc.native('native',enc,limit=60);assert native['status']=='completed','Native limit reached; do not extend or restart.'
    decoded=set()
    for model in xcc.read_models('native',enc):
        assert len(model)==10
        colors=xcc.colors_for(enc,model)
        m=''.join(chr(96+colors['v'+''.join(map(str,v))]) for v in h.VERTICES)
        h.validate(m);assert m not in decoded;decoded.add(m)
    assert decoded==expanded and len(decoded)==native['solutions']==2880 and count==24
    figures=json.loads((h.OUT/'figures-checked.json').read_text());orbit=h.orbit(figures['original']['model'])
    assert decoded==orbit
    (out/'all-models.txt').write_text('\n'.join(sorted(decoded))+'\n')
    xcc.save(out/'checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=xcc.sha(__file__),
        dependencies={str(p.relative_to(h.ROOT)):xcc.sha(p) for p in [Path(h.__file__),h.ROOT/'count_tetra149.cpp',Path(xcc.__file__),h.OUT/'figures-checked.json']},
        vertices=20,edges=60,unit_tetrahedra=10,proper_rotations=12,types=10,options=1200,
        independent_normalized_count=count,independent_nodes=nodes,independent_elapsed_seconds=meta['elapsed_seconds'],
        native_count=native['solutions'],native_elapsed_seconds=native['elapsed_seconds'],native_net_mems=native['net_search_mems'],
        complete_sets_equal=True,all_models_valid=True,all_models_in_one_symmetry_orbit=True,stabilizer=1,
        input_sha256=xcc.sha(case),binary_sha256=xcc.sha(binary),independent_terminal_sha256=xcc.sha(out/'independent-run.json'),
        native_terminal_sha256=xcc.sha(out/'native.json'),models_sha256=xcc.sha(out/'all-models.txt'),
        total_elapsed_seconds=time.monotonic()-start))
    print('PASS149:20vertices/60edges/10cells; two complete equal2880-model sets,24 color classes; one2880-element orbit.')
    print('Seconds:',meta['elapsed_seconds'],native['elapsed_seconds'],'native net mems',native['net_search_mems'])


if __name__=='__main__':main()
