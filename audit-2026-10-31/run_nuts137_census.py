"""Validate S6 maps independently, then run the full exact histogram job."""
from datetime import datetime, timezone
from itertools import permutations
from pathlib import Path
import gzip
import json
import os
import random
import subprocess
import tempfile
import nuts137 as n


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    out=n.OUT/'census';out.mkdir(exist_ok=True)
    assert not (out/'run.json').exists(), 'Do not restart or overwrite an existing census.'
    build=Path(tempfile.mkdtemp(prefix='knuth-vol4b-nuts137-census-'))
    binary=build/'census-nuts137'
    source=n.ROOT/'census_nuts137.cpp'
    command=['g++','-std=c++17','-O3','-Wall','-Wextra',str(source),'-o',str(binary)]
    result=subprocess.run(command,capture_output=True,text=True)
    (out/'build.log').write_text(result.stdout+result.stderr)
    assert result.returncode==0
    n.save(out/'build.json',dict(command=command,source_sha256=n.sha(source),binary=str(binary),
                              binary_sha256=n.sha(binary),compiler=subprocess.check_output(['g++','--version'],text=True)))
    tables=[]
    for p in permutations('123456'):
        rename=dict(zip('123456',p))
        tables.append([n.TYPES.index(n.canonical(''.join(rename[c] for c in t))) for t in n.TYPES])
    cpp=subprocess.check_output([str(binary),'--maps'],text=True)
    assert [list(map(int,row.split())) for row in cpp.splitlines()]==tables
    rng=random.Random(1372026)
    cases=[sorted(rng.sample(range(120),7)) for _ in range(32)]
    cases.extend([[n.TYPES.index(x) for x in c['nuts']]
                  for c in json.loads((n.OUT/'book-cases-checked.json').read_text())['cases'][::2]])
    expected=[]
    for ids in cases:
        orbit=[tuple(sorted(t[i] for i in ids)) for t in tables]
        representative=min(orbit)
        assert representative[0]==0
        key=0
        for i in representative[1:]: key=(key<<7)|i
        h=orbit.count(representative)
        assert len(set(orbit))*h==720
        expected.append([key,h])
    rows='\n'.join(' '.join(map(str,ids)) for ids in cases)+'\n'
    actual=subprocess.check_output([str(binary),'--canonical'],input=rows,text=True)
    assert [list(map(int,row.split())) for row in actual.splitlines()]==expected
    n.save(out/'preflight-checked.json',dict(at_utc=now(),source_sha256=n.sha(__file__),
        cpp_sha256=n.sha(source),all_86400_rename_entries_equal=True,
        canonical_cases=[dict(types=ids,key=ex[0],stabilizer=ex[1]) for ids,ex in zip(cases,expected)],
        direct_all720_permutations_agree=True))
    output=out/'census.tsv'
    command=['timeout','172800',str(binary),str(output)]
    meta=dict(status='running',started_at_utc=now(),wrapper_pid=os.getpid(),command=command,
              timeout_seconds=172800,source_sha256=n.sha(source),runner_sha256=n.sha(__file__),
              binary_sha256=n.sha(binary),total_sets=59487568920,
              acceptance='Require terminal zero exit, full histogram, independent orbit-weight checks and solution-count calibration. No partial count accepted.')
    n.save(out/'run.json',meta)
    with (out/'stdout.json').open('w') as stdout,(out/'progress.log').open('w') as stderr:
        child=subprocess.Popen(command,stdout=stdout,stderr=stderr)
        meta['pid']=child.pid;n.save(out/'run.json',meta)
        rc=child.wait()
    meta.update(returncode=rc,finished_at_utc=now(),status='completed' if rc==0 else 'incomplete')
    if rc==0:
        meta['census_sha256']=n.sha(output)
        with output.open('rb') as src,gzip.open(out/'census.tsv.gz','wb') as dst:
            while chunk:=src.read(1024*1024): dst.write(chunk)
        meta['census_gzip_sha256']=n.sha(out/'census.tsv.gz')
        meta['stdout_sha256']=n.sha(out/'stdout.json')
    n.save(out/'run.json',meta)
    print(json.dumps(meta,indent=2),flush=True)


if __name__=='__main__':
    main()
