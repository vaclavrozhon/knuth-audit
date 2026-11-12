#!/usr/bin/env python3
"""Durable, resumable large Langford checks; never silently retry a timeout."""
from datetime import datetime, timezone
from pathlib import Path
import fcntl
import hashlib
import json
import os
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/langford_mems'
LIMIT=172800


def now():return datetime.now(timezone.utc).isoformat()


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path,data):
    temporary=path.with_suffix(path.suffix+'.partial')
    temporary.write_text(json.dumps(data,indent=2)+'\n')
    temporary.replace(path)


def main():
    OUT.mkdir(exist_ok=True)
    with (OUT/'large.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        validation=json.loads((OUT/'validation.json').read_text())
        assert validation['status']=='verified'
        source_hash=sha(ROOT/'langford_mems.cpp')
        assert source_hash==validation['source_sha256']
        binary=Path(validation['binary']);assert sha(binary)==validation['binary_sha256']
        metadata=dict(status='running',pid=os.getpid(),started_at_utc=now(),
            command=[sys.executable]+sys.argv,source_sha256=source_hash,
            binary=str(binary),binary_sha256=sha(binary),validation_sha256=sha(OUT/'validation.json'),
            time_limit_seconds_per_case=LIMIT,cases=[])
        destination=OUT/'large-wrapper.json'
        save(destination,metadata)
        # Finish the smaller tree first. All three n17 runs really enumerate;
        # a mathematical parity shortcut would not check the printed profiles.
        for mode in ['L21','L20','L']:
            label='n17-'+mode
            run_path=OUT/(label+'-run.json');data_path=OUT/(label+'.json')
            if run_path.exists():
                case=json.loads(run_path.read_text())
                if case['source_sha256']!=source_hash:
                    metadata.update(status='incomplete',error='Existing case has a different source: '+label)
                    save(destination,metadata)
                    raise RuntimeError(metadata['error'])
                if case['status']=='finished':
                    assert case['result_sha256']==sha(data_path)
                    metadata['cases'].append(case);save(destination,metadata)
                    continue
                metadata.update(status='incomplete',error='Existing incomplete case needs review before retry: '+label)
                save(destination,metadata)
                raise RuntimeError(metadata['error'])
            command=[str(binary),'17',mode]
            case=dict(label=label,status='running',command=command,source_sha256=source_hash,
                      started_at_utc=now(),timeout_seconds=LIMIT)
            metadata['cases'].append(case);metadata['active_case']=label
            with data_path.open('w') as output,(OUT/(label+'.log')).open('w') as log:
                process=subprocess.Popen(command,stdout=output,stderr=log)
                case['pid']=process.pid;save(run_path,case);save(destination,metadata)
                start=time.monotonic()
                try:rc=process.wait(timeout=LIMIT)
                except subprocess.TimeoutExpired:
                    process.terminate()
                    try:process.wait(timeout=10)
                    except subprocess.TimeoutExpired:process.kill();process.wait()
                    rc=124
            case.update(returncode=rc,elapsed_seconds=time.monotonic()-start,finished_at_utc=now())
            if rc:
                case['status']='incomplete'
            else:
                try:
                    value=json.loads(data_path.read_text())
                    assert value['n']==17 and value['representatives']==0
                    assert value['nodes']==sum(value['profile']) and len(value['profile'])==18
                    case.update(status='finished',result_sha256=sha(data_path),nodes=value['nodes'],
                        mems=value['mems'],mems_without_cached_L5_read=value['mems_without_cached_L5_read'])
                except Exception as error:
                    case.update(status='incomplete',error=repr(error))
            save(run_path,case);save(destination,metadata)
            print(label,case['status'],case.get('nodes'),case.get('mems'),flush=True)
        metadata.update(status='finished' if all(c['status']=='finished' for c in metadata['cases'])
                        else 'incomplete',finished_at_utc=now())
        metadata.pop('active_case',None)
        save(destination,metadata)


if __name__=='__main__':main()
