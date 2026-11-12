#!/usr/bin/env python3
"""Literal small queens searches independently check analytical access counts."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/queen_backtrack_mems'


def stamp():
    return datetime.now(timezone.utc).isoformat()


def save(path,data):
    temporary=path.with_suffix(path.suffix+'.partial')
    temporary.write_text(json.dumps(data,indent=2)+'\n')
    temporary.replace(path)


def naive(n,reverse=False):
    rows=[];profile=[0]*(n+1);mems=0
    def visit():
        nonlocal mems
        r=len(rows);profile[r]+=1
        if r==n:return
        for t in range(n):
            legal=True
            for j in (range(r-1,-1,-1) if reverse else range(r)):
                mems+=1
                if rows[j]==t or abs(rows[j]-t)==r-j:
                    legal=False;break
            if legal:
                mems+=1;rows.append(t);visit();rows.pop();mems+=1
    visit();return profile,mems


def arrays(n):
    a=[False]*n;b=[False]*(2*n-1);c=[False]*(2*n-1)
    profile=[0]*(n+1);mems=5*n-2
    def visit(r):
        nonlocal mems
        profile[r]+=1
        if r==n:return
        for t in range(n):
            mems+=1
            if a[t]:continue
            mems+=1
            if b[t+r]:continue
            mems+=1
            if c[t-r+n-1]:continue
            a[t]=b[t+r]=c[t-r+n-1]=True
            mems+=4 # Three flags and x[r].
            visit(r+1)
            mems+=4 # Restore t=x[r], then clear the three flags.
            a[t]=b[t+r]=c[t-r+n-1]=False
    visit(0);return profile,mems


def walker(n):
    mask=(1<<n)-1;profile=[0]*(n+1);mems=0;found=0
    stack=[];r=0;a=b=c=0;s=mask
    profile[0]=1
    while True:
        if r==n:
            found+=1
        elif s:
            t=s&-s;s-=t
            stack.append((a,b,c,s));mems+=4
            a=a|t;b=(b|t)>>1;c=((c|t)<<1)&mask
            r+=1;s=mask&~(a|b|c);profile[r]+=1
            continue
        if not r:break
        r-=1;a,b,c,s=stack.pop();mems+=4
    assert found==profile[-1]
    return profile,mems


def main():
    OUT.mkdir(exist_ok=True)
    temporary=Path(tempfile.mkdtemp(prefix='knuth-vol4b-queenmem-'))
    source=ROOT/'queen_backtrack_mems.cpp';binary=temporary/'queen-mems'
    command=['g++','-O3','-march=native','-std=c++17','-Wall','-Wextra','-Werror',str(source),'-o',str(binary)]
    meta=dict(pid=os.getpid(),status='running',started_at_utc=stamp(),
              command=[sys.executable]+sys.argv,compile_command=command,
              source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
              timeout_seconds=3600,small_checks=[])
    destination=OUT/'run.json';save(destination,meta)
    try:
        subprocess.run(command,check=True)
        meta['binary_sha256']=hashlib.sha256(binary.read_bytes()).hexdigest()
        for n in range(1,11):
            result=json.loads(subprocess.check_output([str(binary),str(n)]))
            for label,oracle in [('naive_forward_total_mems',naive(n)),
                                  ('naive_reverse_total_mems',naive(n,True)),
                                  ('array_total_mems',arrays(n)),
                                  ('walker_total_mems',walker(n))]:
                profile,mems=oracle
                assert profile==result['profile'],(n,label,'profile')
                assert mems==result[label],(n,label,mems,result[label])
            meta['small_checks'].append(result)
        save(destination,meta)
        print('40 literal small-case access/profile comparisons passed.',flush=True)
        large_command=[str(binary),'16'];meta['large_command']=large_command
        with (OUT/'n16.json').open('w') as out,(OUT/'n16.log').open('w') as log:
            process=subprocess.Popen(large_command,stdout=out,stderr=log)
            meta['large_pid']=process.pid;meta['large_started_at_utc']=stamp();save(destination,meta)
            start=time.monotonic()
            try:meta['returncode']=process.wait(timeout=3600)
            except subprocess.TimeoutExpired:
                process.terminate()
                try:process.wait(timeout=10)
                except subprocess.TimeoutExpired:process.kill();process.wait()
                meta['returncode']=124
            meta['elapsed_seconds']=time.monotonic()-start
        assert meta['returncode']==0,meta
        result=json.loads((OUT/'n16.json').read_text())
        assert result['solutions']==14772512 and result['nodes']==1141190303
        assert result['profile']==[1,16,210,2236,19688,141812,838816,3998456,
            15324708,46358876,108478966,193892860,260303408,253897632,
            171158018,72002088,14772512]
        meta.update(status='verified',finished_at_utc=stamp())
        save(destination,meta)
        print(json.dumps(result,indent=2),flush=True)
    except Exception as error:
        meta.update(status='incomplete',error=repr(error),finished_at_utc=stamp())
        save(destination,meta)
        raise


if __name__=='__main__':main()
