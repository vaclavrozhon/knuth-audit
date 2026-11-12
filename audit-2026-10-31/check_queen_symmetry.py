#!/usr/bin/env python3
"""Build/validate independent queen counts, or resume completed large cases."""
from datetime import datetime, timezone
from itertools import permutations
from pathlib import Path
import argparse
import fcntl
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import time

from dlx1_audit_tools import ROOT, sha
from check_queen_rotations import valid, rotate, QS, QD

OUT=ROOT/'results/queen_symmetry'
QA=[0,1,0,4,11,42,89,329,1765,9197,45647,284743,1846189,11975869]
LIMIT=172800


def now():return datetime.now(timezone.utc).isoformat()


def save(path,value):
    temp=path.with_suffix(path.suffix+'.partial')
    temp.write_text(json.dumps(value,indent=2)+'\n');temp.replace(path)


def python_counts(models,n):
    labels=['22a','22b','22c','23a','23b']
    answer={label:dict(total=0,half=0,quarter=0,weak=0,stronger=0,oriented=0) for label in labels}
    for p in models:
        points=set(enumerate(p,1));main=[r for r,c in points if r==c]
        anti=[r for r,c in points if r+c==n+1];mid=n//2+1
        center=n%2 and (mid,mid) in points
        if not main and not anti:label='22a' if n%2 else '23a'
        elif bool(main)!=bool(anti):label='22b'
        else:label='23b' if center else '22c'
        s=answer[label];s['total']+=1;s['half']+=rotate(points,n,2)==points;s['quarter']+=rotate(points,n)==points
        if label=='22a':s['oriented']+=p.index(mid)+1<p[mid-1]<mid
        if label=='22b':s['oriented']+=bool(main) and main[0]<mid and p[-1]>p.index(n)+1
        if label=='22c':s['oriented']+=main[0]<anti[0]<mid
        if label in ('23a','23b'):
            a=p[0];b=p.index(n)+1;c=n+1-p[-1];d=n-p.index(1)
            weak=all(a<=x<n+1-a for x in (b,c,d))
            strong=(a<b and a<c and a<d) or (a==b and a<c and a<d) or (a==b==c and a<d) or (a==b==c==d) or (a==c and a<b and a<d)
            s['weak']+=weak;s['stronger']+=weak and strong
    return answer


def validate():
    OUT.mkdir(parents=True,exist_ok=True)
    build=Path(tempfile.mkdtemp(prefix='knuth-vol4b-queen-symmetry-'));binary=build/'queen-symmetry'
    command=['g++','-O3','-std=c++17',str(ROOT/'queen_symmetry.cpp'),'-o',str(binary)]
    subprocess.run(command,check=True)
    cases=[]
    for n in range(4,11):
        result=json.loads(subprocess.check_output([str(binary),str(n),'--models'],text=True,timeout=120))
        expected={p for p in permutations(range(1,n+1)) if valid(list(enumerate(p,1)),n)}
        observed={tuple(p) for p in result.pop('models')}
        assert observed==expected and len(observed)==result['total']
        assert result['cases']==python_counts(expected,n)
        assert (result['Qa'],result['Qs'],result['Qd'])==(QA[n-4],QS[n-4],QD[n-4])
        cases.append(dict(**result,full_model_set_sha256=hashlib.sha256(json.dumps(sorted(observed)).encode()).hexdigest()))
    report=dict(status='verified',checked_at_utc=now(),source_sha256=sha(ROOT/'queen_symmetry.cpp'),
        checker_sha256=sha(__file__),binary=str(binary),binary_sha256=sha(binary),build_command=command,cases=cases)
    save(OUT/'validation.json',report);print('verified7 complete model sets',flush=True)


def large():
    with (OUT/'large.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        validation=json.loads((OUT/'validation.json').read_text());binary=Path(validation['binary'])
        assert validation['status']=='verified' and validation['binary_sha256']==sha(binary)
        assert validation['source_sha256']==sha(ROOT/'queen_symmetry.cpp')
        assert validation['checker_sha256']==sha(__file__)
        dest=OUT/'large-wrapper.json'
        meta=dict(status='running',pid=os.getpid(),started_at_utc=now(),command=[sys.executable]+sys.argv,
                  validation_sha256=sha(OUT/'validation.json'),binary=str(binary),binary_sha256=sha(binary),
                  source_sha256=validation['source_sha256'],timeout_seconds_per_case=LIMIT,cases=[])
        save(dest,meta)
        for n in range(11,18):
            label=f'n{n}';run_path=OUT/(label+'-run.json');data_path=OUT/(label+'.json')
            if run_path.exists():
                case=json.loads(run_path.read_text())
                if (case['status']=='finished' and case['binary_sha256']==sha(binary)
                    and case['result_sha256']==sha(data_path)):
                    meta['cases'].append(case);save(dest,meta);continue
                meta.update(status='incomplete',error='Existing incomplete case needs review: '+label)
                save(dest,meta);raise RuntimeError(meta['error'])
            command=[str(binary),str(n)]
            case=dict(label=label,n=n,status='running',started_at_utc=now(),command=command,
                      binary_sha256=sha(binary),timeout_seconds=LIMIT)
            meta['cases'].append(case);meta['active_case']=label
            with data_path.open('w') as out,(OUT/(label+'.log')).open('w') as log:
                process=subprocess.Popen(command,stdout=out,stderr=log);case['pid']=process.pid
                save(run_path,case);save(dest,meta);start=time.monotonic()
                try:rc=process.wait(timeout=LIMIT)
                except subprocess.TimeoutExpired:
                    process.terminate()
                    try:process.wait(timeout=10)
                    except subprocess.TimeoutExpired:process.kill();process.wait()
                    rc=124
            case.update(returncode=rc,elapsed_seconds=time.monotonic()-start,finished_at_utc=now())
            try:
                assert rc==0
                value=json.loads(data_path.read_text())
                assert (value['Qa'],value['Qs'],value['Qd'])==(QA[n-4],QS[n-4],QD[n-4])
                assert value['total']==8*value['Qa']+4*value['Qs']+2*value['Qd']
                assert all(value['cases'][label]['total']==8*value['cases'][label]['oriented'] for label in ['22a','22b','22c'])
                case.update(status='finished',result_sha256=sha(data_path),total=value['total'])
            except Exception as error:case.update(status='incomplete',error=repr(error))
            save(run_path,case);save(dest,meta);print(n,case['status'],case.get('total'),flush=True)
        meta.update(status='finished' if all(c['status']=='finished' for c in meta['cases']) else 'incomplete',finished_at_utc=now())
        meta.pop('active_case',None);save(dest,meta)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['validate','large']);args=parser.parse_args()
    validate() if args.command=='validate' else large()
