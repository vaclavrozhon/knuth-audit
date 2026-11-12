"""Validate a constructive proof for every2099200 admissible border words."""
from datetime import datetime,timezone
from pathlib import Path
import json,os,subprocess,tempfile
import borders127_128 as b
from border_orbits127 import boundary
from macmahon126 import save,sha,text,edge_name


def main():
    out=b.OUT;end=out/'border-witness127-run.json'
    stdout=out/'border-witness127.models.txt';stderr=out/'border-witness127.stderr'
    reps=out/'geometric_D6-representatives.txt';enc=b.problem127('000000000000')
    enc['header'].remove('*');enc['rows'].pop()
    inp=out/'border-witness127.xcc';border=out/'border-witness127.edges'
    if end.exists():
        meta=json.loads(end.read_text());assert meta['status']=='completed'
        assert meta['model_sha256']==sha(b.__file__) and meta['source_sha256']==sha(b.ROOT/'border_witness127.cpp')
        for f,h in meta['files'].items():assert sha(out/f)==h
    else:
        inp.write_text(text(enc));border.write_text(' '.join(map(edge_name,boundary()))+'\n')
        tmp=Path(tempfile.mkdtemp(prefix='knuth-vol4b-border127-'));binary=tmp/'witness'
        compile_cmd=['c++','-O3','-std=c++17',str(b.ROOT/'border_witness127.cpp'),'-o',str(binary)]
        subprocess.run(compile_cmd,check=True)
        cmd=['timeout','3600',str(binary),str(reps),str(border)]
        meta=dict(status='running',wrapper_pid=os.getpid(),command=cmd,compile_command=compile_cmd,
                  started_at_utc=datetime.now(timezone.utc).isoformat(),timeout_seconds=3600,
                  binary_sha256=sha(binary),source_sha256=sha(b.ROOT/'border_witness127.cpp'),model_sha256=sha(b.__file__))
        with inp.open('rb') as fin,stdout.open('wb') as fout,stderr.open('wb') as ferr:
            proc=subprocess.Popen(cmd,stdin=fin,stdout=fout,stderr=ferr);meta['pid']=proc.pid;save(end,meta);rc=proc.wait()
        meta.update(status='completed' if rc==0 else 'incomplete',returncode=rc,
                    finished_at_utc=datetime.now(timezone.utc).isoformat(),files={p.name:sha(p) for p in [inp,border,reps,stdout,stderr]})
        save(end,meta);assert rc==0
    checked=[]
    for line in stdout.read_text().splitlines():
        w,cs,n=line.split();b.validate127(cs,b.problem127(w));checked.append((w,int(n)))
    assert [w for w,n in checked]==reps.read_text().splitlines() and len(checked)==7889
    census=json.loads((out/'orbits127-checked.json').read_text())
    assert census['groups']['geometric_D6']['representatives_sha256']==sha(reps)
    save(out/'border-witness127-checked.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
         validator_sha256=sha(__file__),model_sha256=sha(b.__file__),run_sha256=sha(end),census_sha256=sha(out/'orbits127-checked.json'),
         geometrically_validated_witnesses=len(checked),group_size=288,covered_labeled_even_borders=2099200,
         total_nodes=sum(n for w,n in checked),max_nodes=max(n for w,n in checked),
         proof='Every actual D6 x S4 boundary orbit has an explicit valid completion. Isometries and global color permutations preserve the full tile set and matching, so all2099200 admissible labeled boundaries are completable. Parity excludes all others.'))
    print('PASS127:7889 valid witnesses cover all2099200 even boundaries by genuine geometric symmetries.')


if __name__=='__main__':main()
