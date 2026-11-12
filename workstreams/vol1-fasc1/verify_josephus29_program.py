#!/usr/bin/env python3
"""One new Fenwick MMIX program run against the accepted old rank vector.

No repeated MIX, Josephus census, permutation test or reference enumeration.
The small static tree-shape sum concerns only the new program's cost.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import tarfile
import tempfile
import time

BASE=Path(__file__).resolve().parent
SOURCES=BASE/'sources';RESULTS=BASE/'results'


def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=15,'Use nice -n15.'
    started=time.monotonic();logs=[]
    source=SOURCES/'josephus29-fenwick.mms'
    reference=BASE.parent/'vol1/results/josephus.json'
    ranks=json.loads(reference.read_text())['requested_ranks']
    result={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'scope':'One new Fenwick MMIX24,11 run; the accepted original rank vector is read, not recalculated.',
            'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'reference':'workstreams/vol1/results/josephus.json',
            'reference_sha256':hashlib.sha256(reference.read_bytes()).hexdigest()}
    def checkpoint():
        (RESULTS/'josephus29-build-and-run.json').write_text(json.dumps(logs,indent=2)+'\n')
        (RESULTS/'josephus29-program.json').write_text(json.dumps(result,indent=2)+'\n')
    def run(command,cwd,timeout=30):
        begin=time.monotonic()
        p=subprocess.run(command,cwd=cwd,text=True,capture_output=True,timeout=timeout)
        logs.append({'command':command,'returncode':p.returncode,'stdout':p.stdout,
                     'stderr':p.stderr,'elapsed_seconds':time.monotonic()-begin})
        checkpoint();p.check_returncode();return p
    with tempfile.TemporaryDirectory(prefix='josephus29-new-build-',dir=RESULTS) as tmp:
        build=Path(tmp)
        with tarfile.open(SOURCES/'mmix-20250620.tar.gz') as archive:
            for name in ['Makefile','mmixal.w','mmix-arith.w','mmix-io.w',
                         'mmix-sim.w','abstime.w','boilerplate.w']:
                (build/name).write_bytes(archive.extractfile(name).read())
        run(['make','basic','CFLAGS=-O0'],build)
        shutil.copyfile(source,build/'josephus29.mms')
        run([str(build/'mmixal'),'-o','josephus29.mmo','-l','josephus29.lst','josephus29.mms'],build)
        (RESULTS/'josephus29-listing.txt').write_text((build/'josephus29.lst').read_text())
        result['object_sha256']=hashlib.sha256((build/'josephus29.mmo').read_bytes()).hexdigest()
        p=run([str(build/'mmix'),'-q','-P','josephus29.mmo'],build,timeout=10)
        (RESULTS/'josephus29-simulator-profile.txt').write_text(p.stdout)
    n=24;K=n.bit_length()-1;d=len(str(n))
    expected=' '.join(f'{rank:0{d}d}' for rank in ranks)+'\n'
    assert p.stdout.startswith(expected)
    assert len(expected)==n*(d+1)
    (RESULTS/'josephus29-output.txt').write_text(expected)
    # Each original position is selected exactly once, independent of order.
    outside=feasible=advances=0
    for position in range(1,n+1):
        index=0;bit=1<<K
        while bit:
            candidate=index+bit
            if candidate>n:outside+=1
            else:
                feasible+=1
                if candidate<position:index=candidate;advances+=1
            bit>>=1
        assert index+1==position
    updates=sum(i&-i for i in range(1,n+1))
    assert (outside,feasible,advances,updates)==(0,120,52,68)
    core_mems=n*(K+3)-outside+2*updates
    core_oops=(11*K+100)*n+9*updates-4*outside+5*K+13
    format_mems=n*(d+2)+1
    format_oops=(66*d+16)*n+62*d+22
    stats=re.findall(r'(\d+) instructions?, (\d+) mems?, (\d+) oops?;',p.stdout)
    assert len(stats)==1
    instructions,mems,oops=map(int,stats[0])
    result.update(n=n,m=11,width=d,output_bytes=len(expected),output_ranks=ranks,
                  every_output_byte_agrees=True,last_position=ranks.index(n)+1,
                  static_tree_shape={'outside':outside,'feasible':feasible,
                                     'advances':advances,'update_nodes':updates},
                  core_mems=core_mems,core_oops=core_oops,
                  format_mems=format_mems,format_oops=format_oops,
                  instructions=instructions,mems=mems,oops=oops,
                  expected_mems=core_mems+format_mems,
                  expected_oops=core_oops+format_oops,
                  elapsed_seconds=time.monotonic()-started)
    checkpoint()
    assert (mems,oops)==(core_mems+format_mems,core_oops+format_oops)==(401,7799)
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
