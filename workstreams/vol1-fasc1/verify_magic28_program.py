#!/usr/bin/env python3
"""One new19x19 MMIX execution, checked against the closed coordinate formula.

This does not repeat the accepted MIX or mathematical magic-square tests.
The complete native output and nominal instruction profile are checked.
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
SOURCES=BASE/'sources'
RESULTS=BASE/'results'


def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=15, 'Use nice -n15.'
    logs=[]
    started=time.monotonic()
    archive=SOURCES/'mmix-20250620.tar.gz'
    source=SOURCES/'magic28.mms'
    result={
        'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope':'One new complete MMIX19x19 generator and formatter; no old MIX or numerical verifier rerun.',
        'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    }
    def checkpoint():
        (RESULTS/'magic28-build-and-run.json').write_text(json.dumps(logs,indent=2)+'\n')
        (RESULTS/'magic28-program.json').write_text(json.dumps(result,indent=2)+'\n')
    def run(command,cwd,timeout=30):
        begin=time.monotonic()
        p=subprocess.run(command,cwd=cwd,text=True,capture_output=True,timeout=timeout)
        logs.append({'command':command,'returncode':p.returncode,
                     'stdout':p.stdout,'stderr':p.stderr,
                     'elapsed_seconds':time.monotonic()-begin})
        checkpoint()
        p.check_returncode()
        return p

    with tempfile.TemporaryDirectory(prefix='magic28-new-build-',dir=RESULTS) as temp:
        build=Path(temp)
        wanted=['Makefile','mmixal.w','mmix-arith.w','mmix-io.w',
                'mmix-sim.w','abstime.w','boilerplate.w']
        with tarfile.open(archive) as tar:
            for name in wanted:
                content=tar.extractfile(name).read()
                (build/name).write_bytes(content)
        run(['make','basic','CFLAGS=-O0'],build)
        shutil.copyfile(source,build/'magic28.mms')
        run([str(build/'mmixal'),'-o','magic28.mmo','-l','magic28.lst','magic28.mms'],build)
        (RESULTS/'magic28-listing.txt').write_text((build/'magic28.lst').read_text())
        result['object_sha256']=hashlib.sha256((build/'magic28.mmo').read_bytes()).hexdigest()
        p=run([str(build/'mmix'),'-q','-P','magic28.mmo'],build,timeout=10)
        (RESULTS/'magic28-simulator-profile.txt').write_text(p.stdout)
    n=19;h=n//2
    expected=[[None]*n for _ in range(n)]
    for q in range(n):
        for s in range(n):
            r=(h+1+q+s)%n;c=(h-q+s)%n
            assert expected[r][c] is None
            expected[r][c]=n*q+s+1
    formatted=''.join(' '.join(f'{v:03d}' for v in row)+'\n' for row in expected)
    assert len(formatted)==4*n*n
    assert p.stdout.startswith(formatted), 'Output differs from independent closed formula.'
    (RESULTS/'magic28-output.txt').write_text(formatted)
    target=n*(n*n+1)//2
    assert all(sum(row)==target for row in expected)
    assert all(sum(expected[r][c] for r in range(n))==target for c in range(n))
    assert sum(expected[r][r] for r in range(n))==target
    assert sum(expected[r][n-1-r] for r in range(n))==target
    assert sorted(v for row in expected for v in row)==list(range(1,n*n+1))
    stats=re.findall(r'(\d+) instructions?, (\d+) mems?, (\d+) oops?;',p.stdout)
    assert len(stats)==1,stats
    instructions,mems,oops=map(int,stats[0])
    result.update(n=n,output_bytes=len(formatted),rows=n,columns=n,magic_sum=target,
                  output_sha256=hashlib.sha256(formatted.encode()).hexdigest(),
                  output_matches_every_byte=True,instructions=instructions,
                  mems=mems,oops=oops,expected_mems=2888,expected_oops=65815,
                  elapsed_seconds=time.monotonic()-started)
    checkpoint()
    assert (mems,oops)==(2888,65815),(mems,oops)
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
