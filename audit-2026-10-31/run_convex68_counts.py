#!/usr/bin/env python3
"""Persisted independent cell-mask and unmodified DLX1 full convex counts."""
from datetime import datetime,timezone
import gzip
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
from dlx1_audit_tools import ROOT,sha,validated_binary,statistics

OUT=ROOT/'results/convex68'
EXPECTED={'n2':2,'n3':10,'n4':117,'n5':2908,'n6':162616,
          'n7':18187302,'n9':8113709,'n9-no-square':5406376}


def now():return datetime.now(timezone.utc).isoformat()


def main():
    work=Path(tempfile.mkdtemp(prefix='knuth-vol4b-convex68-'))
    binary=work/'cell-mask'
    build=['g++','-O3','-std=c++17',str(ROOT/'jigsaw_count.cc'),'-o',str(binary)]
    subprocess.run(build,check=True)
    native=validated_binary()
    state=dict(status='running',pid=os.getpid(),started_at_utc=now(),cases={},
       source_sha256=sha(__file__),cpp_sha256=sha(ROOT/'jigsaw_count.cc'),
       build_command=build,binary=str(binary),binary_sha256=sha(binary),
       dlx1_binary=native,dlx1_sha256=sha(native),timeout_per_method_seconds=86400)
    path=OUT/'counts.json'
    def save():path.write_text(json.dumps(state,indent=2)+'\n')
    save()
    options=json.loads((OUT/'options.json').read_text())
    # Finish all independent counts before starting the expensive DLX1 cases.
    for method in ('cell-mask','dlx1'):
        for label,expected in EXPECTED.items():
            n=options['cases'][label]['n']
            rowsfile=OUT/(label+'.json.gz')
            assert sha(rowsfile)==options['cases'][label]['json_sha256']
            rows=json.loads(gzip.decompress(rowsfile.read_bytes()))
            maskpath=OUT/(label+'.masks')
            maskpath.write_text(f'{n} {len(rows)}\n'+'\n'.join(format(sum(1<<v for v in t),'x') for t in rows)+'\n')
            inp=OUT/(label+'.dlx') if method=='dlx1' else None
            if inp:assert sha(inp)==options['cases'][label]['dlx_sha256']
            cmd=[native,'v129'] if inp else [str(binary),str(maskpath)]
            case=state['cases'].setdefault(label,dict(expected=expected,methods={}))
            meta=dict(status='running',command=cmd,started_at_utc=now(),input_sha256=sha(inp or maskpath))
            case['methods'][method]=meta;state['active_case']=label+'-'+method
            dest=OUT/f'{label}-{method}'
            start=time.monotonic()
            with open(str(dest)+'.out','w') as stdout,open(str(dest)+'.log','w') as stderr:
                stream=open(inp) if inp else subprocess.DEVNULL
                child=subprocess.Popen(cmd,stdin=stream,stdout=stdout,stderr=stderr)
                meta['pid']=child.pid;save()
                try:code=child.wait(timeout=86400)
                except subprocess.TimeoutExpired:
                    child.kill();child.wait();meta.update(status='timeout',finished_at_utc=now())
                    state['status']='timeout';save();raise
                finally:
                    if inp:stream.close()
            assert code==0,(label,method,code)
            stats=statistics(Path(str(dest)+'.log').read_text()) if inp else json.loads(Path(str(dest)+'.out').read_text())
            meta.update(status='finished',finished_at_utc=now(),elapsed_seconds=time.monotonic()-start,
                output=stats,stdout_sha256=sha(str(dest)+'.out'),stderr_sha256=sha(str(dest)+'.log'))
            save();assert stats['solutions']==expected,(label,method,stats)
            case['independent_counts_equal']=len(case['methods'])==2;save()
            print(label,method,stats['solutions'],round(meta['elapsed_seconds'],3),flush=True)
    state.update(status='verified',finished_at_utc=now(),active_case=None);save()


if __name__=='__main__':main()
