"""Keep the complete verification job separate from the frozen census generator."""
from datetime import datetime,timezone
from pathlib import Path
import json
import os
import subprocess
import tempfile
import nuts137 as n


def now(): return datetime.now(timezone.utc).isoformat()


def main():
    out=n.OUT/'census'
    original=json.loads((out/'run.json').read_text())
    assert original['status']=='completed' and original['returncode']==0
    assert n.sha(out/'census.tsv')==original['census_sha256']
    assert not (out/'verifier-run.json').exists()
    build=Path(tempfile.mkdtemp(prefix='knuth-vol4b-nuts137-verify-'))
    binary=build/'verify-census'
    source=n.ROOT/'verify_nuts137_census.cpp'
    command=['g++','-std=c++17','-O3','-Wall','-Wextra',str(source),'-o',str(binary)]
    compiled=subprocess.run(command,capture_output=True,text=True)
    (out/'verifier-build.log').write_text(compiled.stdout+compiled.stderr)
    assert compiled.returncode==0
    n.save(out/'verifier-build.json',dict(command=command,source_sha256=n.sha(source),
        binary=str(binary),binary_sha256=n.sha(binary),compiler=subprocess.check_output(['g++','--version'],text=True)))
    command=['timeout','172800',str(binary),str(out/'census.tsv')]
    meta=dict(status='running',started_at_utc=now(),wrapper_pid=os.getpid(),command=command,
        timeout_seconds=172800,source_sha256=n.sha(source),runner_sha256=n.sha(__file__),
        binary_sha256=n.sha(binary),census_metadata_sha256=n.sha(out/'run.json'),
        census_sha256=original['census_sha256'])
    n.save(out/'verifier-run.json',meta)
    with (out/'verifier-stdout.json').open('w') as stdout,(out/'verifier-progress.log').open('w') as stderr:
        child=subprocess.Popen(command,stdout=stdout,stderr=stderr)
        meta['pid']=child.pid;n.save(out/'verifier-run.json',meta)
        rc=child.wait()
    meta.update(returncode=rc,finished_at_utc=now(),status='completed' if rc==0 else 'incomplete',
                stdout_sha256=n.sha(out/'verifier-stdout.json'),stderr_sha256=n.sha(out/'verifier-progress.log'))
    n.save(out/'verifier-run.json',meta)
    print(json.dumps(meta,indent=2),flush=True)


if __name__=='__main__': main()
