"""Small audit helpers for the archived, unmodified author DLX1 binary."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import time

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validated_binary():
    build = json.loads((ROOT/'results/dancing_links/dlx1-build.json').read_text())
    for source in build['sources'].values():
        assert sha(ROOT/source['path']) == source['sha256']
    binary = build['binaries']['dlx1']
    assert sha(binary['path']) == binary['sha256']
    return binary['path']


def input_text(names, rows, primary=None):
    if primary is None:
        primary = len(names)
    header = list(names[:primary])
    if primary < len(names):
        header += ['|']+list(names[primary:])
    return '\n'.join([' '.join(header)]+[' '.join(names[i-1] for i in row)
                                         for row in rows])+'\n'


def statistics(log):
    match = re.search(r'Altogether (\d+) solutions?, (\d+)\+(\d+) mems, '
                      r'(\d+) updates, (\d+) bytes, (\d+) nodes', log)
    assert match, log[-2000:]
    result = dict(zip(['solutions', 'initialization_mems', 'search_mems',
                       'updates', 'bytes', 'nodes'], map(int, match.groups())))
    result['profile'] = [int(count) for _, count in
                         re.findall(r'^\s+(\d+):\s+(\d+)\s*$', log, re.M)]
    assert sum(result['profile']) == result['nodes']
    return result


def run(output_dir, label, data, models=False, timeout=300):
    binary = validated_binary()
    output_dir.mkdir(parents=True, exist_ok=True)
    input_path = output_dir/(label+'.dlx')
    input_path.write_text(data)
    command = [binary, 'v129']+(['m1'] if models else [])
    start = time.monotonic()
    result = subprocess.run(command, input=data, text=True, capture_output=True,
                            check=True, timeout=timeout)
    (output_dir/(label+'.log')).write_text(result.stderr)
    stats = statistics(result.stderr)
    stats.update(label=label, command=command, input_sha256=sha(input_path),
                 binary_sha256=sha(binary), elapsed_seconds=time.monotonic()-start)
    if not models:
        assert not result.stdout
    return stats, result.stdout


def decode_rows(text, names, rows):
    """Decode cyclically printed rows; callers use distinct option sets."""
    lookup = {frozenset(names[i-1] for i in row): r for r, row in enumerate(rows)}
    assert len(lookup) == len(rows)
    solutions = set()
    current = None
    def finish():
        if current is not None:
            solution = tuple(sorted(current))
            assert solution not in solutions and len(solution) == len(set(solution))
            solutions.add(solution)
    for line in text.splitlines():
        if re.fullmatch(r'\d+:', line):
            finish()
            assert int(line[:-1]) == len(solutions)+1
            current = []
        elif line.strip():
            assert current is not None
            match = re.fullmatch(r'\s*(.*?) \(\d+ of \d+\)', line)
            assert match, line
            current.append(lookup[frozenset(match[1].split())])
    finish()
    return solutions
