#!/usr/bin/env python3
"""Persist native and independent billion-node checks; never overwrite a run."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import fcntl
import json
import os
from pathlib import Path
import subprocess
import tempfile
import threading
import time
from dlx1_audit_tools import ROOT,sha,validated_binary,statistics,decode_rows
from prepare_pentomino_main import OUT


def now():return datetime.now(timezone.utc).isoformat()


def main():
    lock=open(OUT/'large.lock','w');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    path=OUT/'large-wrapper.json'
    assert not path.exists(),'Review the existing run; do not restart automatically.'
    instances=json.loads((OUT/'instances.json').read_text())
    short=json.loads((OUT/'short-check.json').read_text())
    build=json.loads((ROOT/'results/dancing_links/dlx1-build.json').read_text())
    validated_binary()
    for b in build['binaries'].values():assert sha(b['path'])==b['sha256']
    work=Path(tempfile.mkdtemp(prefix='knuth-vol4b-pentmain-'));binary=work/'mask'
    command=['g++','-O3','-std=c++17',str(ROOT/'pentomino_mask.cc'),'-o',str(binary)]
    subprocess.run(command,check=True)
    state=dict(status='running',pid=os.getpid(),started_at_utc=now(),cases={},
      source_sha256=sha(__file__),cpp_sha256=sha(ROOT/'pentomino_mask.cc'),
      instances_sha256=sha(OUT/'instances.json'),short_sha256=sha(OUT/'short-check.json'),
      build_command=command,binary=str(binary),binary_sha256=sha(binary),
      native_binaries=build['binaries'],timeout_per_case_seconds=86400)
    mutex=threading.Lock()
    def save():
        tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(state,indent=2)+'\n');tmp.replace(path)
    save()
    # Establish the separate mask implementation against every finished short
    # case, including secondary items and fixed first-cell branching.
    state['mask_short_checks']={}
    for label,expected in short['cases'].items():
        p=OUT/(label+'.masks');assert sha(p)==instances['cases'][label]['masks_sha256']
        cmd=[str(binary),str(p)];r=subprocess.run(cmd,text=True,capture_output=True,check=True,timeout=300)
        actual=json.loads(r.stdout)
        assert actual['profile']==expected['native']['profile'] and actual['solutions']==expected['native']['solutions']
        state['mask_short_checks'][label]=actual;save()
    def run_case(label,method):
        c=instances['cases'][label];native=method=='dlx1'
        inp=OUT/(label+('.dlx' if native else '.masks'))
        assert sha(inp)==c['input_sha256' if native else 'masks_sha256']
        exe=build['binaries']['dlx1-nomrv' if c['nomrv'] else 'dlx1']['path'] if native else str(binary)
        cmd=[exe,'v129','m1'] if native else [exe,str(inp)]
        dest=OUT/(label+'-'+method);start=time.monotonic()
        meta=dict(status='running',command=cmd,input_sha256=sha(inp),started_at_utc=now())
        with open(str(dest)+'.out','w') as stdout,open(str(dest)+'.log','w') as stderr:
            stream=open(inp) if native else subprocess.DEVNULL
            child=subprocess.Popen(cmd,stdin=stream,stdout=stdout,stderr=stderr)
            with mutex:
                meta['pid']=child.pid;state['cases'][label+'-'+method]=meta;save()
            try:code=child.wait(timeout=86400)
            except subprocess.TimeoutExpired:
                child.kill();child.wait()
                with mutex:meta.update(status='timeout',finished_at_utc=now());save()
                return
            finally:
                if native:stream.close()
        assert code==0,(label,method,code)
        stats=statistics(Path(str(dest)+'.log').read_text()) if native else json.loads(Path(str(dest)+'.out').read_text())
        if native:
            models=decode_rows(Path(str(dest)+'.out').read_text(),c['names'],c['rows'])
            assert models=={tuple(m) for m in short['cases']['full']['models']}
        assert stats['solutions']==8
        if c['expected_nodes'] is not None:assert stats['nodes']==c['expected_nodes'],(label,stats)
        else:assert 1.45e9<=stats['nodes']<1.55e9
        with mutex:
            meta.update(status='finished',finished_at_utc=now(),elapsed_seconds=time.monotonic()-start,
                output=stats,stdout_sha256=sha(str(dest)+'.out'),stderr_sha256=sha(str(dest)+'.log'));save()
        print(label,method,stats['nodes'],flush=True)
    jobs=[(label,method) for label in ('full-cells-secondary','first-cell-3x20') for method in ('mask','dlx1')]
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures=[pool.submit(run_case,*j) for j in jobs]
        for future in futures:future.result()
    if any(v['status']!='finished' for v in state['cases'].values()):
        state.update(status='incomplete',finished_at_utc=now());save();return
    for label in ('full-cells-secondary','first-cell-3x20'):
        assert state['cases'][label+'-mask']['output']['profile']==state['cases'][label+'-dlx1']['output']['profile']
    state.update(status='verified',finished_at_utc=now());save()


if __name__=='__main__':main()
