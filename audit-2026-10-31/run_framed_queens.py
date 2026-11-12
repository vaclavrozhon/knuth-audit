"""Durable, resumable two-method enumeration of framed 27-queen placements.

Only complete matching parts are reused. A timeout never means zero solutions.
The rotation filter is weighted exactly; see FRAMED_QUEENS_NOTES.md.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import fcntl
import json
import os
import subprocess
import sys
import time
from check_framed_queens import ROOT, SOURCE, OUT, FIELDS, digest, prefixes, add


def now():
    return datetime.now(timezone.utc).isoformat()


def save(path, data):
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(data, indent=2)+'\n')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=27)
    parser.add_argument('--limit', type=int, default=28800)
    args = parser.parse_args()
    assert 8 <= args.n <= 31 and args.limit > 0
    lock = open(Path('/tmp')/f'knuth-vol4b-framed-n{args.n}.lock', 'w')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    validation = json.loads((OUT/'validation.json').read_text())
    assert validation['status'] == 'pass'
    assert validation['source_sha256'] == digest(SOURCE)
    binary = Path(validation['binary'])
    assert digest(binary) == validation['binary_sha256']
    source_sha = validation['source_sha256']
    all_prefixes = prefixes(args.n)
    dest = OUT/f'large-n{args.n}-wrapper.json'
    if dest.exists():
        previous = json.loads(dest.read_text())
        active = previous.get('active_part', {})
        child = active.get('pid')
        if child and Path(f'/proc/{child}/cmdline').exists():
            command = Path(f'/proc/{child}/cmdline').read_bytes().split(b'\0')
            if str(binary).encode() in command:
                raise RuntimeError(f'Previous child {child} is still alive; do not restart its work')
    meta = dict(pid=os.getpid(), status='running', n=args.n,
                started_at_utc=now(), command=[sys.executable]+sys.argv,
                time_limit_seconds_per_method=args.limit, source_sha256=source_sha,
                binary=str(binary), binary_sha256=digest(binary),
                validation='validation.json', validation_sha256=digest(OUT/'validation.json'),
                prefix_rows_zero_based=[2, 3], prefixes=all_prefixes,
                total_prefixes=len(all_prefixes), completed_prefixes=0,
                log=f'results/framed_queens/large-n{args.n}-wrapper.log',
                partial_totals={}, incomplete=[])
    save(dest, meta)
    for index, prefix in enumerate(all_prefixes):
        label = f'n{args.n}-r2-{prefix[0]:02}-r3-{prefix[1]:02}'
        result_path = OUT/(label+'.json')
        result = json.loads(result_path.read_text()) if result_path.exists() else {}
        same_version = (result.get('source_sha256') == source_sha
                        and result.get('binary_sha256') == meta['binary_sha256'])
        reusable = result.get('status') == 'pass' and same_version
        if not reusable:
            if not same_version:
                result = dict(n=args.n, prefix=prefix, status='running', source_sha256=source_sha,
                              binary_sha256=meta['binary_sha256'], started_at_utc=now(), methods={})
            else:
                result['status'] = 'running'
                result.setdefault('resumed_at_utc', []).append(now())
            for method in ['rows', 'mrv']:
                command = [str(binary), str(args.n), method]+[str(c) for c in prefix]+['--orbit-filter']
                previous_run = result['methods'].get(method, {})
                if (previous_run.get('returncode') == 0 and 'result' in previous_run
                        and previous_run.get('command') == command):
                    continue
                output = OUT/(label+'-'+method+'.out')
                run = dict(command=command, time_limit_seconds=args.limit,
                           started_at_utc=now(), output=output.name)
                result['methods'][method] = run
                start = time.monotonic()
                with output.open('w') as log:
                    process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)
                    run['pid'] = process.pid
                    meta['active_part'] = dict(index=index, label=label, method=method,
                                               pid=process.pid, command=command)
                    save(result_path, result); save(dest, meta)
                    try:
                        rc = process.wait(timeout=args.limit)
                    except subprocess.TimeoutExpired:
                        process.terminate()
                        try:
                            process.wait(timeout=10)
                        except subprocess.TimeoutExpired:
                            process.kill(); process.wait()
                        rc = 124
                run.update(returncode=rc, elapsed_seconds=time.monotonic()-start, finished_at_utc=now())
                if rc:
                    result['status'] = 'incomplete'
                    break
                try:
                    run['result'] = json.loads(output.read_text())
                except ValueError:
                    result['status'] = 'invalid_output'
                    break
                got = run['result']
                assert got['n'] == args.n and got['method'] == method and got['orbit_filter']
                save(result_path, result)
            if result['status'] == 'running':
                a, b = (result['methods'][m]['result'] for m in ['rows', 'mrv'])
                compared = FIELDS+['minimum_multiplicities_1_to_4', 'full_count_numerator', 'full_count_denominator']
                result['status'] = 'pass' if all(a[k] == b[k] for k in compared) else 'mismatch'
            result['finished_at_utc'] = now()
            save(result_path, result)
        meta.pop('active_part', None)
        if result['status'] == 'pass':
            add(meta['partial_totals'], result['methods']['rows']['result'])
            meta['completed_prefixes'] += 1
        else:
            meta['incomplete'].append(dict(label=label, status=result['status']))
        save(dest, meta)
        print(label, result['status'], meta['completed_prefixes'], '/', len(all_prefixes),
              'partial weighted numerator / 3:', meta['partial_totals'].get('full_count_numerator', 0), flush=True)
        if result['status'] == 'mismatch':
            raise RuntimeError('The independent enumerators disagree; investigate before continuing')
    if not meta['incomplete']:
        numerator = meta['partial_totals']['full_count_numerator']
        assert numerator % 3 == 0
        meta['full_count'] = numerator//3
        if args.n == 27:
            meta['book_count'] = 34651355392
            meta['matches_book'] = meta['full_count'] == meta['book_count']
        meta['status'] = 'pass' if meta.get('matches_book', True) else 'book_mismatch'
    else:
        meta['status'] = 'incomplete'
    meta['finished_at_utc'] = now()
    save(dest, meta)
    print('FINISHED', meta['status'], meta.get('full_count'), flush=True)


if __name__ == '__main__':
    main()
