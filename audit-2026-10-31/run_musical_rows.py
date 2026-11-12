"""Durable independent musical-row count queue. Freeze while running."""
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import subprocess
import tempfile
import time
from puzzle_xcc import ROOT, OUT, save, sha


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    directory=Path(tempfile.mkdtemp(prefix='knuth-vol4b-music-',dir='/tmp'))
    binary=directory/'enumerate-musical-rows'
    source=ROOT/'enumerate_musical_rows.cpp'
    command=['g++','-O3','-std=c++17','-Wall','-Wextra',str(source),'-o',str(binary)]
    build=subprocess.run(command,capture_output=True,text=True)
    save(OUT/'music-build.json',dict(command=command,returncode=build.returncode,
         stdout=build.stdout,stderr=build.stderr,source_sha256=sha(source),
         binary_sha256=sha(binary) if binary.exists() else None))
    assert build.returncode==0,build.stderr
    state=dict(status='running',wrapper_pid=os.getpid(),started_utc=now(),done=[],
               script_sha256=sha(__file__),source_sha256=sha(source))
    for n in range(2,19):
        label=f'music-{n}'
        terminal=OUT/(label+'.json')
        if terminal.exists():
            previous=json.loads(terminal.read_text());assert previous['status']=='completed'
            state['done'].append(n);continue
        rowfile=OUT/(label+'.rows.bin')
        args=[str(binary),str(n)]+([str(rowfile)] if n<=14 else [])
        command=['timeout','172800',*args]
        start=time.monotonic()
        with (OUT/(label+'.out')).open('wb') as output,(OUT/(label+'.log')).open('wb') as err:
            proc=subprocess.Popen(command,stdout=output,stderr=err)
            meta=dict(status='running',n=n,command=command,pid=proc.pid,wrapper_pid=os.getpid(),
                      started_utc=now(),timeout_seconds=172800,binary_sha256=sha(binary),
                      source_sha256=sha(source),script_sha256=sha(__file__))
            save(OUT/(label+'-run.json'),meta)
            state['current']=n;state['pid']=proc.pid;save(OUT/'music-queue.json',state)
            rc=proc.wait()
        meta.update(returncode=rc,finished_utc=now(),elapsed_seconds=time.monotonic()-start,
                    status='completed' if rc==0 else 'incomplete',stdout_sha256=sha(OUT/(label+'.out')),
                    stderr_sha256=sha(OUT/(label+'.log')))
        if rc==0:
            meta.update(json.loads((OUT/(label+'.out')).read_text()))
            if n<=14:
                assert rowfile.stat().st_size==n*meta['solutions']
                meta['rows_sha256']=sha(rowfile)
        save(terminal,meta);save(OUT/(label+'-run.json'),meta)
        print(label,meta['status'],meta.get('solutions'),flush=True)
        if rc:break
        state['done'].append(n)
    state.update(status='completed' if len(state['done'])==17 else 'incomplete',finished_utc=now())
    save(OUT/'music-queue.json',state)


if __name__=='__main__':main()
