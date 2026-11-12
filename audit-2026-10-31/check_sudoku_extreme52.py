#!/usr/bin/env python3
"""Identify the cited puzzle, validate uniqueness, and measure explicit random seeds."""
from datetime import datetime, timezone
from itertools import permutations, product
from statistics import mean, stdev
import json
import subprocess
import time
from dlx1_audit_tools import ROOT, sha, run, input_text, decode_rows, validated_binary, statistics
from check_sudoku_native import instance
from check_sudoku_basics import UNITS
from check_sudoku_minimal import Oracle

OUT = ROOT/'results/sudoku_minimal'


def identify(target):
    path = ROOT/'sources/sudoku/eleven-26370.txt'
    puzzles = path.read_text().splitlines()
    assert len(puzzles) == 26370
    source = puzzles[6538][:81]
    assert len(source) == 81 and set(source) <= set('.123456789')
    p3 = list(permutations(range(3)))
    perms = [tuple(3*bands[i]+inside[i][j] for i in range(3) for j in range(3))
             for bands in p3 for inside in product(p3, repeat=3)]
    tr = [sum(x != '.' for x in target[9*r:9*r+9]) for r in range(9)]
    tc = [sum(target[9*r+c] != '.' for r in range(9)) for c in range(9)]
    found = []
    for transpose in (False, True):
        s = ''.join(source[9*c+r] if transpose else source[9*r+c] for r in range(9) for c in range(9))
        sr = [sum(x != '.' for x in s[9*r:9*r+9]) for r in range(9)]
        sc = [sum(s[9*r+c] != '.' for r in range(9)) for c in range(9)]
        rs = [p for p in perms if [sr[r] for r in p] == tr]
        cs = [p for p in perms if [sc[c] for c in p] == tc]
        for rp, cp in product(rs, cs):
            transformed = ''.join(s[9*r+c] for r in rp for c in cp)
            if [v != '.' for v in transformed] != [v != '.' for v in target]:
                continue
            mapping, valid = {'.':'.'}, True
            for x, y in zip(transformed,target):
                if x in mapping and mapping[x] != y:
                    valid = False
                    break
                mapping[x] = y
            if valid and len(set(mapping.values())) == len(mapping):
                found.append(dict(transpose=transpose, rows=rp, columns=cp, digit_map=mapping))
    assert len(found) == 1
    record = dict(source_path=str(path.relative_to(ROOT)), source_sha256=sha(path),
                  ordinal=6539, source_grid=source, book_grid=target, transformations=found)
    (OUT/'52-isomorphism.json').write_text(json.dumps(record,indent=2)+'\n')
    return record


def main():
    start = time.monotonic()
    source = json.loads((OUT/'pdf-grids.json').read_text())['sources']['52']['cells']
    target = ''.join(source)
    mapping = identify(target)
    board = [int(c) if c != '.' else 0 for c in source]
    names, rows, moves, primary = instance(board)
    data = input_text(names,rows,primary)
    out = OUT/'extreme52'
    stats, text = run(out,'printed',data,models=True)
    assert stats['solutions'] == 1
    (out/'printed.models').write_text(text)
    selections = decode_rows(text,names,rows)
    assert len(selections) == 1
    complete = list(board)
    for row in next(iter(selections)):
        v,k = moves[row]
        assert not complete[v]
        complete[v] = k
    assert all({complete[v] for v in unit} == set(range(1,10)) for unit in UNITS)
    oracle = Oracle(board,complete)
    mask = (1<<sum(bool(k) for k in board))-1
    assert oracle.unique(mask)
    oracle.close()
    binary = validated_binary()
    samples = []
    with (out/'randomized-logs.jsonl').open('w') as log:
        for seed in range(1000):
            command = [binary,'v129',f's{seed}']
            result = subprocess.run(command,input=data,text=True,capture_output=True,check=True,timeout=60)
            assert not result.stdout
            sample = statistics(result.stderr)
            assert sample['solutions'] == 1
            sample['seed'] = seed
            samples.append(sample)
            log.write(json.dumps(dict(command=command,log=result.stderr))+'\n')
            if seed%100 == 99:
                print('Randomized seeds',seed+1,flush=True)
    summary = {key:dict(mean=mean(s[key] for s in samples),stdev=stdev(s[key] for s in samples),
                       minimum=min(s[key] for s in samples),maximum=max(s[key] for s in samples))
               for key in ('nodes','search_mems','initialization_mems')}
    record = dict(status='verified for stated scope',checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__),grids_sha256=sha(OUT/'pdf-grids.json'),
                  mapping=mapping,deterministic=stats,solution=complete,
                  models_sha256=sha(out/'printed.models'),coordinate_uniqueness=oracle.records[mask],
                  random_seeds=[0,999],samples=samples,summary=summary,
                  randomized_logs_sha256=sha(out/'randomized-logs.jsonl'),seconds=time.monotonic()-start,
                  limits='Current archived DLX1 and explicitly specified seeds; no claim to reproduce '
                         'Stappers historical seed set or to prove this is hardest in the entire collection '
                         'or among all Sudoku puzzles. Canonical equivalence established, but global '
                         'lexicographic minimality of the printed form is not asserted.')
    (OUT/'extreme52.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__ == '__main__':
    main()
