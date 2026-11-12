"""Build and run the independent upper-triangle enumerator, retaining terminals."""
from datetime import datetime, timezone
from pathlib import Path
import fcntl
import json
import os
import subprocess
import tempfile
import time
from layout_native import ROOT, OUT, save, sha


def main():
    lock = (OUT / 'transpose-cell.lock').open('w')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    directory = Path(tempfile.mkdtemp(prefix='knuth-vol4b-transpose-', dir='/tmp'))
    source = ROOT / 'enumerate_transpose_sudoku.cpp'
    binary = directory / 'transpose-sudoku'
    command = ['g++', '-std=c++17', '-O3', '-Wall', '-Wextra', str(source), '-o', str(binary)]
    proc = subprocess.run(command, capture_output=True, text=True)
    save(OUT / 'transpose-build.json', dict(command=command, returncode=proc.returncode,
        stdout=proc.stdout, stderr=proc.stderr, source_sha256=sha(source)))
    assert proc.returncode == 0, proc.stderr
    for base in [2, 3]:
        label = f'transpose-cell-n{base*base}'
        assert not (OUT / (label + '-run.json')).exists(), 'Inspect previous metadata; never restart blindly.'
        command = ['timeout', '172800', str(binary), str(base)]
        meta = dict(status='running', wrapper_pid=os.getpid(), command=command,
            started_utc=datetime.now(timezone.utc).isoformat(), timeout_seconds=172800,
            source_sha256=sha(source), binary_sha256=sha(binary), script_sha256=sha(__file__))
        start = time.monotonic()
        with (OUT / (label + '.out')).open('w') as fout, (OUT / (label + '.log')).open('w') as ferr:
            child = subprocess.Popen(command, stdout=fout, stderr=ferr)
            meta['pid'] = child.pid
            save(OUT / (label + '-run.json'), meta)
            rc = child.wait()
        meta.update(status='completed' if rc == 0 else 'incomplete', returncode=rc,
            finished_utc=datetime.now(timezone.utc).isoformat(), elapsed_seconds=time.monotonic()-start,
            stdout_sha256=sha(OUT / (label + '.out')), stderr_sha256=sha(OUT / (label + '.log')))
        if rc == 0:
            raw = json.loads((OUT / (label + '.out')).read_text())
            meta.update(raw)
            if base == 2:
                expected = json.loads((OUT / 'sudoku114-n4-improved-checked.json').read_text())['boards']
                assert set(map(tuple, raw['witnesses'])) == set(map(tuple, expected))
                assert raw['solutions'] == 2
            else:
                assert raw['solutions'] == 30258432, raw['solutions']
        save(OUT / (label + '.json'), meta)
        save(OUT / (label + '-run.json'), meta)
        print(label, meta['status'], meta.get('solutions'), flush=True)
        assert rc == 0, meta


if __name__ == '__main__':
    main()
