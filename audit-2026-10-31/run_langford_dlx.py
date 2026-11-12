#!/usr/bin/env python3
"""Durable n16 DLX15 memory comparison; no retries of incomplete cases."""
from datetime import datetime, timezone
from pathlib import Path
import fcntl
import json
import os
import subprocess
import sys
import time

from check_langford_dlx import encoding, OUT
from dlx1_audit_tools import ROOT, sha, input_text, validated_binary, statistics

LIMIT = 172800


def now():
    return datetime.now(timezone.utc).isoformat()


def save(path, data):
    temp = path.with_suffix(path.suffix+'.partial')
    temp.write_text(json.dumps(data, indent=2)+'\n')
    temp.replace(path)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT/'large.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        validation_path = OUT/'validation.json'
        validation = json.loads(validation_path.read_text())
        assert validation['status'] == 'verified'
        assert validation['source_sha256'] == sha(ROOT/'check_langford_dlx.py')
        assert validation['helper_sha256'] == sha(ROOT/'dlx1_audit_tools.py')
        binary = validated_binary()
        binary_hash = sha(binary)
        metadata = dict(status='running', pid=os.getpid(), started_at_utc=now(),
            command=[sys.executable]+sys.argv, binary=binary, binary_sha256=binary_hash,
            validation_sha256=sha(validation_path), source_sha256=sha(__file__),
            time_limit_seconds_per_case=LIMIT, cases=[])
        destination = OUT/'large-wrapper.json'
        save(destination, metadata)
        for cut in ('special', 'one'):
            label = f'n16-{cut}'
            run_path = OUT/(label+'-run.json')
            names, rows = encoding(16, cut)
            data = input_text(names, rows)
            input_path, log_path = OUT/(label+'.dlx'), OUT/(label+'.log')
            if run_path.exists():
                case = json.loads(run_path.read_text())
                if (case.get('status') == 'finished' and case['binary_sha256'] == binary_hash
                    and case['input_sha256'] == sha(input_path)
                    and case['log_sha256'] == sha(log_path)
                    and input_path.read_text() == data):
                    metadata['cases'].append(case)
                    save(destination, metadata)
                    continue
                metadata.update(status='incomplete', error='Existing case needs review: '+label)
                save(destination, metadata)
                raise RuntimeError(metadata['error'])
            input_path.write_text(data)
            command = [binary, 'v129', 'd10000000000']
            case = dict(label=label, n=16, cut=cut, status='running', command=command,
                binary_sha256=binary_hash, input_sha256=sha(input_path),
                started_at_utc=now(), timeout_seconds=LIMIT)
            metadata['cases'].append(case)
            metadata['active_case'] = label
            start = time.monotonic()
            with input_path.open() as inp, log_path.open('w') as log:
                process = subprocess.Popen(command, stdin=inp, stdout=subprocess.DEVNULL, stderr=log)
                case['pid'] = process.pid
                save(run_path, case)
                save(destination, metadata)
                try:
                    rc = process.wait(timeout=LIMIT)
                except subprocess.TimeoutExpired:
                    process.terminate()
                    try:
                        process.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait()
                    rc = 124
            case.update(returncode=rc, elapsed_seconds=time.monotonic()-start, finished_at_utc=now())
            try:
                assert rc == 0
                text = log_path.read_text()
                assert 'TIMEOUT' not in text
                value = statistics(text)
                assert value['solutions'] == 326721800 and len(value['profile']) == 17
                case.update(status='finished', result=value, log_sha256=sha(log_path))
            except Exception as error:
                case.update(status='incomplete', error=repr(error))
            save(run_path, case)
            save(destination, metadata)
            print(label, case['status'], case.get('result'), flush=True)
        metadata.update(status='finished' if all(c['status'] == 'finished' for c in metadata['cases'])
                        else 'incomplete', finished_at_utc=now())
        metadata.pop('active_case', None)
        if metadata['status'] == 'finished':
            special, one = [case['result']['search_mems'] for case in metadata['cases']]
            metadata['comparison'] = dict(special_mems=special, one_mems=one,
                special_saving_fraction=1-special/one, special_mems_per_solution=special/326721800)
        save(destination, metadata)


if __name__ == '__main__':
    main()
