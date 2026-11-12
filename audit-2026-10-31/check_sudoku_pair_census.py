#!/usr/bin/env python3
"""Replay literal (W,X) pairs using fully validated archived certificates."""
from datetime import datetime, timezone
import gzip
import json
from dlx1_audit_tools import ROOT, sha
from check_sudoku_basics import UNITS

OUT = ROOT/'results/sudoku_minimal'


def main():
    source = json.loads((ROOT/'results/sudoku_basics/pdf-grids.json').read_text())['sources']['29a']['board']
    base = json.loads((OUT/'minimal.json').read_text())
    positions = base['clue_positions']
    q = {r['mask']:r['unique'] for r in json.loads((OUT/'subset-queries.json').read_text())}
    extra = json.loads(gzip.decompress((OUT/'pair-extra-queries.json.gz').read_bytes()))
    for record in extra:
        mask = record['mask']
        assert mask not in q
        board = list(map(int,record['alternative']))
        assert len(board) == 81 and board != base['reference']
        assert all({board[v] for v in u} == set(range(1,10)) for u in UNITS)
        assert all(not (mask>>i&1) or board[v] == source[v] for i,v in enumerate(positions))
        q[mask] = False
    frontier, rounds = {(0,(1<<32)-1)}, []
    while frontier:
        next_round = set()
        size = next(iter(frontier))[1].bit_count()
        rounds.append(dict(clues=size,pairs=len(frontier),distinct_subsets=len({x for w,x in frontier})))
        for w,x in frontier:
            good, bad = [], 0
            for i in range(32):
                bit = 1<<i
                if x & bit and not w & bit:
                    if q[x^bit]:
                        good.append(x^bit)
                    else:
                        bad |= bit
            for child in good:
                next_round.add((w|bad,child))
        frontier = next_round
    previous = json.loads((OUT/'pair-census.json').read_text())
    assert rounds == previous['rounds']
    previous.update(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                    source_sha256=sha(__file__), subset_queries_sha256=sha(OUT/'subset-queries.json'),
                    extra_queries_sha256=sha(OUT/'pair-extra-queries.json.gz'),
                    note='All47293 extra queries are nonunique, with independently validated full alternatives. '
                         'Literal pair deduplication and subset deduplication are different policies. Neither '
                         'reproduces4249 at size26, but unspecified historical caching prevents a definitive correction.')
    (OUT/'pair-census.json').write_text(json.dumps(previous,indent=2)+'\n')
    print(json.dumps(rounds))


if __name__ == '__main__':
    main()
