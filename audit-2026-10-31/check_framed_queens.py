"""Validate both enumerators, partitioning, and the C4 orbit weight formula."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import subprocess
import time

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT/'framed_queens.cpp'
OUT = ROOT/'results/framed_queens'
MASK = (1 << 64)-1
FIELDS = ['count', 'hash_sum_mod_2_64', 'hash_xor']


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pins(n):
    return [(0, 1), (1, n-1), (n-2, 0), (n-1, n-2)]


def valid_pairs(cells):
    return all(r != s and c != d and abs(r-s) != abs(c-d)
               for i, (r, c) in enumerate(cells) for s, d in cells[i+1:])


def prefixes(n):
    return [(c, d) for c in range(n) for d in range(n)
            if valid_pairs(pins(n)+[(2, c), (3, d)])]


def add(total, result):
    for key in ['count', 'full_count_numerator']:
        total[key] = total.get(key, 0)+result[key]
    total['hash_sum_mod_2_64'] = (total.get('hash_sum_mod_2_64', 0)+result['hash_sum_mod_2_64']) & MASK
    total['hash_xor'] = total.get('hash_xor', 0) ^ result['hash_xor']


def run(binary, n, method, prefix=(), filtered=False):
    command = [str(binary), str(n), method]+[str(c) for c in prefix]
    if filtered:
        command.append('--orbit-filter')
    result = json.loads(subprocess.check_output(command, text=True, timeout=180))
    assert result['method'] == method and result['n'] == n
    assert result['orbit_filter'] == filtered
    return result


def boards(n):
    """Independent Python set-based search, used only for n=17 and n=18."""
    board = dict(pins(n))
    columns = {c for _, c in board.items()}
    sums = {r+c for r, c in board.items()}
    diffs = {r-c for r, c in board.items()}

    def search():
        if len(board) == n:
            yield tuple(board[r] for r in range(n))
            return
        choices = [(r, [c for c in range(n) if c not in columns
                        and r+c not in sums and r-c not in diffs])
                   for r in range(n) if r not in board]
        r, options = min(choices, key=lambda pair: len(pair[1]))
        for c in options:
            board[r] = c; columns.add(c); sums.add(r+c); diffs.add(r-c)
            yield from search()
            del board[r]; columns.remove(c); sums.remove(r+c); diffs.remove(r-c)
    return list(search())


def rotate(board):
    result = [None]*len(board)
    for r, c in enumerate(board):
        result[c] = len(board)-1-r
    return tuple(result)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    sha = digest(SOURCE)
    binary = Path('/tmp')/('knuth-vol4b-framed-'+sha[:16])
    command = ['g++', '-O3', '-std=c++17', '-Wall', '-Wextra', str(SOURCE), '-o', str(binary)]
    subprocess.run(command, check=True)
    result = dict(status='running', started_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha, binary=str(binary), binary_sha256=digest(binary),
                  compile_command=command,
                  compiler=subprocess.check_output(['g++', '--version'], text=True).splitlines()[0],
                  baseline='small-comparison.json', baseline_sha256=digest(OUT/'small-comparison.json'),
                  raw=[], orbit_filtered=[], partitioned=[], explicit_orbits=[])
    baseline = {(r['n'], r['method']): r for r in json.loads((OUT/'small-comparison.json').read_text())['results']}
    start = time.monotonic()
    for n in range(4, 23):
        for method in ['rows', 'mrv']:
            got = run(binary, n, method)
            assert all(got[k] == baseline[n, method][k] for k in FIELDS), (n, method)
            assert got['all_models_pairwise_validated']
            result['raw'].append(got)
        print('raw', n, got['count'], flush=True)
    for n in range(8, 23):
        totals = {}
        for method in ['rows', 'mrv']:
            total = {}
            for c in range(n):
                add(total, run(binary, n, method, [c], True))
            assert total['full_count_numerator'] == 3*baseline[n, method]['count']
            totals[method] = total
        assert totals['rows'] == totals['mrv']
        result['orbit_filtered'].append(dict(n=n, **totals['rows']))
        print('orbit-filter', n, totals['rows'], flush=True)
    for n in [17, 18, 19]:
        parts = []
        total = {}
        for prefix in prefixes(n):
            a = run(binary, n, 'rows', prefix)
            b = run(binary, n, 'mrv', prefix)
            assert all(a[k] == b[k] for k in FIELDS)
            add(total, a)
            parts.append(dict(prefix=prefix, **{k:a[k] for k in FIELDS}))
        assert all(total[k] == baseline[n, 'rows'][k] for k in FIELDS)
        result['partitioned'].append(dict(n=n, prefix_count=len(parts), totals=total, parts=parts))
        print('two-row partition', n, len(parts), flush=True)
    for n in [17, 18]:
        models = set(boards(n))
        assert len(models) == baseline[n, 'rows']['count']
        weighted = Fraction(0)
        kept = 0
        for board in models:
            rotations = [board]
            for _ in range(3):
                rotations.append(rotate(rotations[-1]))
            assert all(q in models for q in rotations)
            values = [q[2] for q in rotations]
            inverse = tuple(board.index(c) for c in range(n))
            assert values == [board[2], n-1-inverse[2], n-1-board[n-3], inverse[n-3]]
            if values[0] == min(values):
                kept += 1
                weighted += Fraction(4, values.count(values[0]))
        assert weighted == len(models)
        filtered = next(x for x in result['orbit_filtered'] if x['n'] == n)
        assert filtered['count'] == kept
        result['explicit_orbits'].append(dict(n=n, models=len(models), kept=kept,
                                              weighted_total=int(weighted)))
    result.update(status='pass', finished_at_utc=datetime.now(timezone.utc).isoformat(),
                  elapsed_seconds=time.monotonic()-start)
    (OUT/'validation.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS', result['elapsed_seconds'], flush=True)


if __name__ == '__main__':
    main()
