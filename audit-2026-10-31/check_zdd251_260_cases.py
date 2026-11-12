"""New bounded ZDD cases only; never repeat the accepted 48/300 old cases."""
from pathlib import Path
from datetime import datetime, timezone
from functools import lru_cache
from itertools import combinations
from math import factorial, comb
import json
import os
import re
import subprocess
import time
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/zdd251_260'
BIN = Path(os.environ.get('KNUTH_ZDD_NEW_BIN', '/tmp/knuth-vol4b-zdd/dlx6'))


def model(names, rows, heuristic='mrv'):
    """Declarative remaining-row recursion; no links or native solver code."""
    masks = [sum(1 << i for i in row) for row in rows]
    cache = {0: (1, 1)}
    instructions, states = {}, {}
    count_global = 0

    def visit(s):
        nonlocal count_global
        if s in cache:
            count_global += cache[s][0]
            return cache[s]
        old_count = count_global
        active = [k for k, m in enumerate(masks) if m & s == m]
        columns = {i: [k for k in active if masks[k] >> i & 1]
                   for i in range(len(names)) if s >> i & 1}
        i = min(columns, key=lambda i: (len(columns[i]), i)) if heuristic == 'mrv' else min(columns)
        choices = columns[i]
        # Header removal plus one removal for every other item of each row.
        updates = 1 + sum(len(rows[k]) - 1 for k in choices)
        z = count = 0
        branches = []
        for k in choices:
            current = [t for t in active if t not in choices]
            pivot_pos = rows[k].index(i)
            order = rows[k][pivot_pos + 1:] + rows[k][:pivot_pos]
            for j in order:
                removed = [t for t in current if j in rows[t]]
                updates += 1 + sum(len(rows[t]) - 1 for t in removed)
                current = [t for t in current if j not in rows[t]]
            child_s = s ^ masks[k]
            child_count, child_z = visit(child_s)
            count += child_count
            branches.append(dict(option=k + 1, child=child_s, count=child_count))
            if child_count:
                node = len(instructions) + 2
                instructions[node] = (k + 1, z, child_z)
                z = node
        # This is precisely the global COUNT delta in answer 253.
        assert count_global - old_count == count
        cache[s] = (count, z)
        states[s] = dict(pivot=i, updates=updates, branches=branches, count=count)
        return cache[s]

    count, root = visit((1 << len(names)) - 1)
    assert count_global == count
    stats = dict(count=count, updates=sum(v['updates'] for v in states.values()),
                 nodes=len(instructions) + 2 if count else 1, signatures=len(cache))
    return dict(stats=stats, root=root, instructions=instructions, states=states)


def native(names, rows, name):
    source = ' '.join(names) + '\n' + '\n'.join(' '.join(names[i] for i in row) for row in rows) + '\n'
    path = OUT / (name + '.xcc')
    cmd = [str(BIN), 'v1', 'm1', 'd0', 'T100000000']
    reused, elapsed = path.exists(), None
    if reused:
        assert path.read_text() == source
        stderr = (OUT / (name + '.log')).read_text()
        stdout = (OUT / (name + '.zdd')).read_text()
    else:
        path.write_text(source)
        started = time.monotonic()
        p = subprocess.run(cmd, input=source, text=True, capture_output=True, timeout=8, check=True)
        elapsed = time.monotonic() - started
        stderr, stdout = p.stderr, p.stdout
        (OUT / (name + '.log')).write_text(stderr)
        (OUT / (name + '.zdd')).write_text(stdout)
    assert 'Altogether ' in stderr and 'TIMEOUT' not in stderr and 'overflow' not in stderr.lower()
    stats = dict(count=int(re.search(r'Altogether (\d+) solution', stderr)[1]),
                 updates=int(re.search(r'(\d+) updates', stderr)[1]),
                 nodes=int(re.search(r'(\d+) ZDD node', stderr)[1]),
                 signatures=sum(map(int, re.search(r'(\d+)\+(\d+) signatures', stderr).groups())))
    # DLX6 prints node addresses in hex, but option numbers in decimal.
    nodes = {int(a, 16): (int(b), int(c, 16), int(d, 16))
             for a, b, c, d in re.findall(r'([0-9a-f]+): \(~(\d+)\?([0-9a-f]+):([0-9a-f]+)\)', stdout)}
    return dict(stats=stats, instructions=nodes, root=max(nodes), command=cmd,
                elapsed_seconds=elapsed, reused_saved_terminal=reused)


def family(nodes, root):
    @lru_cache(None)
    def walk(i):
        if i == 0:
            return frozenset()
        if i == 1:
            return frozenset([()])
        var, lo, hi = nodes[i]
        if var == 0:
            return walk(hi)
        assert all(var not in a for a in walk(hi))
        return walk(lo) | frozenset(tuple(sorted(a + (var,))) for a in walk(hi))
    return walk(root)


def main():
    assert not (OUT / 'cases-checked.json').exists()
    started = time.monotonic()
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    # The existing binary's original build inputs must still match the archive.
    build = BIN.parent
    for p in ['dlx6.w', 'dlx6-small.ch', 'gb_flip.w', 'gb_flip.ch', 'boilerplate.w']:
        assert sha(build / p) == sha(ROOT / 'sources/knuth-programs' / p), p
    names = ['00', '01', '10', '02', '11', '20', '12', '21']
    pairs = ['00 01', '00 10', '01 02', '01 11', '02 12', '10 11', '10 20', '11 12', '11 21', '20 21']
    rows = [tuple(names.index(s) for s in p.split()) for p in pairs]
    printed122 = {12: (2, 8, 11), 11: (4, 10, 3), 10: (3, 0, 9), 9: (8, 0, 2),
                  8: (1, 0, 7), 7: (7, 4, 6), 6: (5, 0, 5), 5: (9, 0, 1),
                  4: (6, 0, 3), 3: (5, 0, 2), 2: (10, 0, 1)}
    printed252 = {13: (2, 7, 12), 12: (10, 0, 11), 11: (4, 10, 8), 10: (3, 0, 9),
                  9: (8, 0, 1), 8: (5, 0, 1), 7: (1, 0, 6), 6: (5, 0, 5),
                  5: (7, 3, 4), 4: (9, 0, 1), 3: (6, 0, 2), 2: (10, 0, 1)}
    expected = {(1, 5, 6, 10), (1, 5, 7, 9), (2, 3, 8, 10), (2, 4, 5, 10)}
    first = model(names, rows, 'first')
    mrv = model(names, rows)
    original = native(names, rows, 'domino252')
    assert first['instructions'] == printed122
    assert mrv['stats'] == original['stats']
    for nodes, root in [(printed122, 12), (printed252, 13), (mrv['instructions'], mrv['root']),
                        (original['instructions'], original['root'])]:
        assert set(family(nodes, root)) == expected
    # Both diagrams are the precise output up to names of node IDs.
    def canonical(nodes, i):
        if i < 2:
            return i
        v, lo, hi = nodes[i]
        return (v, canonical(nodes, lo), canonical(nodes, hi))
    assert canonical(mrv['instructions'], mrv['root']) == canonical(printed252, 13)
    save(OUT / 'domino252.json', dict(leftmost=first, mrv=mrv, native=original,
         printed122=printed122, printed252=printed252, solutions=sorted(expected)))
    report = []
    for q, r in [(2, 2), (2, 3), (3, 2), (3, 3), (4, 3)]:
        left = list(range(1, 2*q + 2))
        right = list(range(2*q + 2, 2*q + 2*r + 2))
        names = ['m'] + [f'L{i}' for i in range(2*q + 1)] + [f'R{i}' for i in range(2*r)]
        rows = [(0, left[0]), (0, right[0])] + list(combinations(left, 2)) + list(combinations(right, 2))
        name = f'bizarre256-{q}-{r}'
        direct, original = model(names, rows), native(names, rows, name)
        assert direct['stats'] == original['stats'], (name, direct['stats'], original['stats'])
        assert direct['stats']['count'] == factorial(2*q)*factorial(2*r)//(2**(q+r)*factorial(q)*factorial(r))
        save(OUT / (name + '.json'), dict(model=direct, native=original))
        report.append(dict(case=name, q=q, r=r, stats=direct['stats']))
    for n in range(3, 25):
        names = [f'{c}{i}' for i in range(n) for c in 'XY']
        rows = [(2*i, 2*j + 1) for i in range(n) for j in range(n) if (j-i) % n in [0, 1, n-1]]
        name = f'circular260-{n}'
        direct, original = model(names, rows), native(names, rows, name)
        assert direct['stats'] == original['stats'], (name, direct['stats'], original['stats'])
        a, b = 2, 1
        for _ in range(n):
            a, b = b, a+b
        assert direct['stats']['count'] == a + 2
        save(OUT / (name + '.json'), dict(model=direct, native=original))
        report.append(dict(case=name, n=n, stats=direct['stats'],
                           printed=dict(signatures=6*n+9, nodes=8*n-9, updates=34*n-58)))
    # Small empirical exercise 14 family only. No exponential large-n queue.
    for n in range(3, 10):
        names = [f'{c}{i}' for i in range(n) for c in 'XY']
        rows = [(2*i, 2*j + 1) for i in range(n) for j in range(n) if (j-i) % n not in [0, 1]]
        name = f'menage260-{n}'
        direct, original = model(names, rows), native(names, rows, name)
        first = model(names, rows, 'first')
        assert direct['stats'] == original['stats'], (name, direct['stats'], original['stats'])
        # Inclusion-exclusion on the forbidden 2n-cycle's k-matchings.
        count = sum((-1)**k * (2*n*comb(2*n-k, k)//(2*n-k)) * factorial(n-k) for k in range(n+1))
        assert first['stats']['count'] == direct['stats']['count'] == count
        save(OUT / (name + '.json'), dict(model=direct, native=original, leftmost=first))
        report.append(dict(case=name, n=n, stats=direct['stats'], leftmost=first['stats']))
    save(OUT / 'cases-checked.json', dict(at_utc=datetime.now(timezone.utc).isoformat(),
         checker_sha256=sha(__file__), binary=str(BIN), binary_sha256=sha(BIN), nice=os.getpriority(os.PRIO_PROCESS, 0),
         elapsed_seconds=time.monotonic()-started, new_native_cases=35, cases=report,
         old_successful_cases_repeated=0, new_long_jobs=0,
         artifact_hashes={str(p.relative_to(ROOT)):sha(p) for p in OUT.iterdir() if p.suffix in ['.xcc','.zdd','.log'] or p.stem.startswith(('domino','bizarre','circular','menage'))}))
    print('PASS: new domino, five bizarre graphs, 22 circular and seven small menage cases.', flush=True)
    for q in report:
        if q['case'].startswith('bizarre') or q['case'] in ['circular260-3','circular260-4','circular260-5','circular260-6','circular260-24']:
            print(q)


if __name__ == '__main__':
    main()
