"""Recorded original native solvers for the independent DLX108--114 inputs."""
from datetime import datetime, timezone
from pathlib import Path
import fcntl
import gzip
import json
import os
import re
import subprocess
import time
from puzzle_xcc import encode, native_text, save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/layouts108_114'
NATIVE = Path('/tmp/knuth-vol4b-colored-4ulh1ceo/dlx2-original')


def run(label, enc, *, binary=NATIVE, every=1, limit=172800, source=None):
    OUT.mkdir(exist_ok=True)
    lock = (OUT / (label + '.lock')).open('w')
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    text = native_text(enc) if isinstance(enc, dict) else enc
    inp = OUT / (label + '.dlx')
    terminal = OUT / (label + '.json')
    if terminal.exists():
        meta = json.loads(terminal.read_text())
        assert meta['status'] == 'completed', meta
        assert inp.read_text() == text and meta['input_sha256'] == sha(inp)
        assert meta['stdout_sha256'] == sha(OUT / (label + '.out.gz'))
        assert meta['stderr_sha256'] == sha(OUT / (label + '.log'))
        return meta
    assert not (OUT / (label + '-run.json')).exists(), 'Inspect the earlier run before resuming.'
    inp.write_text(text)
    source = source or ROOT / 'sources/knuth-programs/dlx2.w'
    command = ['timeout', str(limit), str(binary), 'v129', 'm' + str(every)]
    meta = dict(status='running', wrapper_pid=os.getpid(), command=command,
                started_utc=datetime.now(timezone.utc).isoformat(), timeout_seconds=limit,
                input_sha256=sha(inp), binary_sha256=sha(binary), source_sha256=sha(source),
                source=str(source), runner_sha256=sha(__file__), model_output_period=every)
    if isinstance(enc, dict):
        meta.update(primary=enc['primary'], items=len(enc['names']), options=len(enc['rows']),
                    total_option_length=sum(map(len, enc['rows'])))
    start = time.monotonic()
    with inp.open('rb') as fin, (OUT / (label + '.log')).open('wb') as err:
        proc = subprocess.Popen(command, stdin=fin, stdout=subprocess.PIPE, stderr=err)
        meta['pid'] = proc.pid
        save(OUT / (label + '-run.json'), meta)
        with gzip.open(OUT / (label + '.out.gz'), 'wb') as fout:
            for block in iter(lambda: proc.stdout.read(65536), b''):
                fout.write(block)
        rc = proc.wait()
    log = (OUT / (label + '.log')).read_text()
    match = re.search(r'Altogether (\d+) solutions?, (\d+)\+(\d+)(?:-(\d+))? mems, .*?, (\d+) nodes', log)
    meta.update(status='completed' if rc == 0 and match else 'incomplete', returncode=rc,
                finished_utc=datetime.now(timezone.utc).isoformat(), elapsed_seconds=time.monotonic() - start,
                stdout_sha256=sha(OUT / (label + '.out.gz')), stderr_sha256=sha(OUT / (label + '.log')))
    if match:
        count, init, mem, unmem, nodes = (int(x or 0) for x in match.groups())
        meta.update(solutions=count, initial_mems=init, search_mems=mem, unmems=unmem,
                    net_search_mems=mem-unmem, nodes=nodes)
    save(terminal, meta)
    save(OUT / (label + '-run.json'), meta)
    return meta


def read_models(label, enc):
    lookup = {tuple(sorted(line.split())): i for i, line in enumerate(native_text(enc).splitlines()[1:])}
    assert len(lookup) == len(enc['rows'])
    model = None
    with gzip.open(OUT / (label + '.out.gz'), 'rt') as stream:
        for line in stream:
            if re.fullmatch(r'\d+:\s*', line):
                if model is not None:
                    yield tuple(sorted(model))
                model = []
            elif line.strip():
                assert model is not None, line
                tokens = re.sub(r'\s*\(\d+ of \d+\)\s*$', '', line).split()
                model.append(lookup[tuple(sorted(tokens))])
    if model is not None:
        yield tuple(sorted(model))
