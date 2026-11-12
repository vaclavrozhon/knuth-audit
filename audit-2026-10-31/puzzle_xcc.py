"""Named XCC inputs and original-DLX2 evidence for exercises 101--107.

Explicit colors are positive integers; zero denotes an uncolored occurrence.
This module has no import-time searches. Completed native runs are immutable.
"""
from datetime import datetime, timezone
from pathlib import Path
import gzip
import hashlib
import json
import os
import re
import subprocess
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/puzzles101_107'
NATIVE = Path('/tmp/knuth-vol4b-colored-4ulh1ceo/dlx2-original')
COLORS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    temp.replace(path)


def encode(primary, secondary, options):
    names = list(primary) + list(secondary)
    assert len(names) == len(set(names))
    assert all(0 < len(x) <= 8 and ':' not in x and not any(c.isspace() for c in x) for x in names)
    ids = {x: i + 1 for i, x in enumerate(names)}
    rows = [tuple((ids[x], c) for x, c in option) for option in options]
    for row in rows:
        assert len(row) == len(set(i for i, c in row))
        assert any(i <= len(primary) for i, c in row)
        assert all(0 <= c <= len(COLORS) and (i > len(primary) or c == 0) for i, c in row)
    return dict(names=names, primary=len(primary), rows=rows)


def native_text(enc):
    n = enc['primary']
    def token(i, c):
        return enc['names'][i - 1] + (':' + COLORS[c - 1] if c else '')
    header = ' '.join(enc['names'][:n]) + ' | ' + ' '.join(enc['names'][n:])
    return header + '\n' + '\n'.join(' '.join(token(i, c) for i, c in row) for row in enc['rows']) + '\n'


def native(label, enc, *, models=True, limit=600, extra=()):
    OUT.mkdir(parents=True, exist_ok=True)
    terminal = OUT / (label + '.json')
    inp = OUT / (label + '.dlx')
    text = native_text(enc)
    if terminal.exists():
        meta = json.loads(terminal.read_text())
        assert meta['status'] == 'completed', (label, meta['status'])
        assert inp.read_text() == text and meta['input_sha256'] == sha(inp)
        assert meta['stderr_sha256'] == sha(OUT / (label + '.log'))
        assert meta['stdout_sha256'] == sha(OUT / (label + '.out.gz'))
        return meta
    inp.write_text(text)
    command = ['timeout', str(limit), str(NATIVE), 'v129', 'm1' if models else 'm0', *extra]
    start = time.monotonic()
    meta = dict(status='running', wrapper_pid=os.getpid(), command=command,
                started_utc=datetime.now(timezone.utc).isoformat(), timeout_seconds=limit,
                input_sha256=sha(inp), binary_sha256=sha(NATIVE),
                source_sha256=sha(ROOT / 'sources/knuth-programs/dlx2.w'),
                runner_sha256=sha(__file__), primary=enc['primary'],
                items=len(enc['names']), options=len(enc['rows']))
    with inp.open('rb') as fin, (OUT / (label + '.log')).open('wb') as err:
        proc = subprocess.Popen(command, stdin=fin, stdout=subprocess.PIPE, stderr=err)
        meta['pid'] = proc.pid
        save(OUT / (label + '-run.json'), meta)
        with gzip.open(OUT / (label + '.out.gz'), 'wb') as fout:
            for block in iter(lambda: proc.stdout.read(65536), b''):
                fout.write(block)
        rc = proc.wait()
    log = (OUT / (label + '.log')).read_text()
    match = re.search(r'Altogether (\d+) solutions?, (\d+)\+(\d+)-(\d+) mems, .*?, (\d+) nodes', log)
    meta.update(status='completed' if rc == 0 and match else 'incomplete', returncode=rc,
                finished_utc=datetime.now(timezone.utc).isoformat(), elapsed_seconds=time.monotonic() - start,
                stderr_sha256=sha(OUT / (label + '.log')), stdout_sha256=sha(OUT / (label + '.out.gz')))
    if match:
        count, init, mem, unmem, nodes = map(int, match.groups())
        meta.update(solutions=count, initial_mems=init, search_mems=mem, unmems=unmem,
                    net_search_mems=mem - unmem, nodes=nodes)
    save(terminal, meta)
    save(OUT / (label + '-run.json'), meta)
    return meta


def read_models(label, enc):
    lines = native_text(enc).splitlines()[1:]
    lookup = {tuple(sorted(line.split())): i for i, line in enumerate(lines)}
    assert len(lookup) == len(lines), 'Duplicate input rows require a different decoder'
    models, model = [], None
    with gzip.open(OUT / (label + '.out.gz'), 'rt') as stream:
        for line in stream:
            if re.fullmatch(r'\d+:\s*', line):
                if model is not None:
                    models.append(tuple(sorted(model)))
                model = []
            elif line.strip():
                assert model is not None, line
                tokens = re.sub(r'\s*\(\d+ of \d+\)\s*$', '', line).split()
                model.append(lookup[tuple(sorted(tokens))])
    if model is not None:
        models.append(tuple(sorted(model)))
    assert len(models) == len(set(models))
    return set(models)


def colors_for(enc, model):
    colors = {}
    for ri in model:
        for i, c in enc['rows'][ri]:
            if c:
                name = enc['names'][i - 1]
                assert name not in colors or colors[name] == c
                colors[name] = c
    return colors
