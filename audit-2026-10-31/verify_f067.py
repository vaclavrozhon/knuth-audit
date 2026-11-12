"""Certify the saved 20-position component without a full-board census."""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parent
BOARD = frozenset((r, c) for r in range(8) for c in range(8))


def dominates(queens):
    return all(any(r == s or c == t or abs(r-s) == abs(c-t) for s, t in queens) for r, c in BOARD)


def main():
    start = time.monotonic()
    path = ROOT / 'results/queen_domination/components-direct.json'
    data = json.loads(path.read_text())['last_printed_diagram']
    members = {frozenset(map(tuple, f)) for f in data['members']}
    seed = frozenset([(0, 2), (2, 7), (3, 3), (5, 0), (7, 5)])
    assert len(members) == len(data['members']) == 20
    assert seed == frozenset(map(tuple, data['seed'])) and seed in members
    for f in members:
        assert len(f) == 5 and f <= BOARD and dominates(f)
    adj = {f: set() for f in members}
    for a, b in combinations(members, 2):
        if len(a ^ b) == 2:
            adj[a].add(b)
            adj[b].add(a)
    reached, todo = {seed}, [seed]
    while todo:
        for f in adj[todo.pop()]-reached:
            reached.add(f)
            todo.append(f)
    assert reached == members
    # Exhaust all single relocations from these 20 positions, not all 64-choose-5 sets.
    checked = 0
    for f in members:
        for old in f:
            kept = f-{old}
            for new in BOARD-f:
                moved = kept | {new}
                checked += 1
                if dominates(moved):
                    assert moved in members, 'A relocation escapes the saved component'
    edges = sum(map(len, adj.values()))//2
    assert edges == 26 and checked == 20*5*59
    print(json.dumps(dict(valid=True, connected=True, closed=True, component_size=20, edges=edges,
        compared_with_printed_sizes=[8, 12], checked_single_relocations=checked,
        full_census=False, seconds=time.monotonic()-start,
        witness_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()), indent=2))


if __name__ == '__main__':
    main()
