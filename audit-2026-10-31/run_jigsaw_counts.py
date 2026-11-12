#!/usr/bin/env python3
"""Persisted DLX1 versus independent cell-mask counts, including long n7."""
from datetime import datetime,timezone
import gzip
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
from dlx1_audit_tools import ROOT,sha,validated_binary,statistics

OUT=ROOT/'results/jigsaw/tilings'


def now():return datetime.now(timezone.utc).isoformat()


def main():
    work=Path(tempfile.mkdtemp(prefix='knuth-vol4b-jigsaw-count-'))
    binary=work/'jigsaw-count'
    command=['g++','-O3','-std=c++17',str(ROOT/'jigsaw_count.cc'),'-o',str(binary)]
    subprocess.run(command,check=True)
    native=validated_binary()
    state=dict(status='running',pid=os.getpid(),started_at_utc=now(),cases={},
               source_sha256=sha(__file__),cpp_sha256=sha(ROOT/'jigsaw_count.cc'),
               build_command=command,binary=str(binary),binary_sha256=sha(binary),
               dlx1_binary=native,dlx1_sha256=sha(native),timeout_per_method_seconds=86400)
    path=OUT/'count-wrapper.json'
    def save():path.write_text(json.dumps(state,indent=2)+'\n')
    save()
    for label,n,expected in [('n3',3,0),('n4',4,33),('n5',5,2082),('n6',6,320098),
                             ('rainbow',9,98556),('rainbow-no-sudoku',9,42669),('n7',7,132418528)]:
        rows=json.loads(gzip.decompress((OUT/(label+'.json.gz')).read_bytes()))
        maskpath=OUT/(label+'.masks')
        maskpath.write_text(f'{n} {len(rows)}\n'+'\n'.join(format(sum(1<<v for v in row),'x') for row in rows)+'\n')
        case=dict(expected=expected,methods={});state['cases'][label]=case
        for method,cmd,inp in [('cell-mask',[str(binary),str(maskpath)],None),
                               ('dlx1',[native,'v129'],OUT/(label+'.dlx'))]:
            dest=OUT/f'{label}-{method}'
            meta=dict(status='running',command=cmd,started_at_utc=now(),input_sha256=sha(inp or maskpath))
            case['methods'][method]=meta;state['active_case']=label+'-'+method
            start=time.monotonic()
            with open(str(dest)+'.out','w') as stdout,open(str(dest)+'.log','w') as stderr:
                stream=open(inp) if inp else subprocess.DEVNULL
                child=subprocess.Popen(cmd,stdin=stream,stdout=stdout,stderr=stderr)
                meta['pid']=child.pid;save()
                try: code=child.wait(timeout=86400)
                except subprocess.TimeoutExpired:
                    child.kill();child.wait();meta.update(status='timeout',finished_at_utc=now());save();raise
                finally:
                    if inp:stream.close()
            assert code==0,(label,method,code)
            stats=json.loads(Path(str(dest)+'.out').read_text()) if method=='cell-mask' else statistics(Path(str(dest)+'.log').read_text())
            meta.update(status='finished',finished_at_utc=now(),elapsed_seconds=time.monotonic()-start,
                        output=stats,stdout_sha256=sha(str(dest)+'.out'),stderr_sha256=sha(str(dest)+'.log'))
            save();assert stats['solutions']==expected,(label,method,stats)
            print(label,method,stats['solutions'],round(meta['elapsed_seconds'],3),flush=True)
        case['independent_counts_equal']=True;save()
    state.update(status='verified',finished_at_utc=now(),active_case=None);save()


if __name__=='__main__':main()
