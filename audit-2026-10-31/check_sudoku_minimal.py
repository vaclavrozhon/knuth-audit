#!/usr/bin/env python3
"""DLX54: complete descending subset census with independently checked witnesses."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import tempfile
import time
from dlx1_audit_tools import ROOT, sha, run, input_text
from check_sudoku_native import instance
from check_sudoku_basics import UNITS

OUT = ROOT/'results/sudoku_minimal'


def build_oracle():
    path = OUT/'oracle-build.json'
    source = ROOT/'sudoku_subset_oracle.cpp'
    if path.exists():
        data = json.loads(path.read_text())
        assert data['source_sha256'] == sha(source) and data['binary_sha256'] == sha(data['binary'])
        return data
    build = Path(tempfile.mkdtemp(prefix='knuth-vol4b-sudoku-subsets-'))
    binary = build/'oracle'
    command = ['c++', '-O3', '-std=c++17', '-Wall', '-Wextra', str(source), '-o', str(binary)]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    (OUT/'oracle-build.log').write_text(result.stdout+result.stderr)
    data = dict(built_at_utc=datetime.now(timezone.utc).isoformat(), command=command,
                source_sha256=sha(source), binary=str(binary), binary_sha256=sha(binary))
    path.write_text(json.dumps(data, indent=2)+'\n')
    return data


class Oracle:
    def __init__(self, initial, reference):
        self.initial, self.reference = initial, reference
        self.positions = [v for v,k in enumerate(initial) if k]
        self.build = build_oracle()
        self.process = subprocess.Popen([self.build['binary']], stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE, text=True, bufsize=1)
        self.process.stdin.write(''.join(map(str,initial))+'\n'+''.join(map(str,reference))+'\n')
        self.process.stdin.flush()
        self.records = {}

    def unique(self, mask):
        if mask in self.records:
            return self.records[mask]['unique']
        self.process.stdin.write(str(mask)+'\n'); self.process.stdin.flush()
        line = self.process.stdout.readline().split()
        assert len(line) == 3 and int(line[0]) == mask, line
        alternative = None if line[2] == '-' else [int(c) for c in line[2]]
        if alternative is not None:
            assert len(alternative) == 81 and alternative != self.reference
            assert all({alternative[v] for v in unit} == set(range(1,10)) for unit in UNITS)
            assert all(not (mask>>i&1) or alternative[v] == self.initial[v] for i,v in enumerate(self.positions))
        self.records[mask] = dict(mask=mask, unique=alternative is None,
                                  coordinate_nodes=int(line[1]), alternative=alternative)
        return alternative is None

    def close(self):
        self.process.stdin.close()
        assert self.process.wait(timeout=5) == 0


def main():
    start = time.monotonic()
    initial = json.loads((ROOT/'results/sudoku_basics/pdf-grids.json').read_text())['sources']['29a']['board']
    reference = json.loads((ROOT/'results/sudoku_basics/basics.json').read_text())['solutions']['a'][0]
    oracle = Oracle(initial, reference)
    assert len(oracle.positions) == 32
    full = (1<<32)-1
    assert oracle.unique(full)
    frontier = {full:0}
    rounds, minimal = [], []
    # W contains known essential clues. Their essentiality persists in every
    # uniquely solvable subset containing them. Merge that knowledge at joins.
    while frontier:
        next_round = {}
        round_size = next(iter(frontier)).bit_count()
        rounds.append(dict(clues=round_size, candidates=len(frontier)))
        for mask, essential in sorted(frontier.items()):
            assert mask.bit_count() == round_size and not essential & ~mask
            children = []
            for i in range(32):
                bit = 1<<i
                if mask & bit and not essential & bit:
                    child = mask ^ bit
                    if oracle.unique(child):
                        children.append(child)
                    else:
                        essential |= bit
            if not children:
                assert essential == mask
                minimal.append(mask)
            else:
                for child in children:
                    assert not essential & ~child
                    next_round[child] = next_round.get(child,0) | essential
        print('round',round_size,'candidates',len(frontier),'queries',len(oracle.records),flush=True)
        frontier = next_round
    oracle.close()
    counts = Counter(m.bit_count() for m in minimal)
    assert counts == {27:8, 26:154, 25:387, 24:206, 23:22}
    assert len(minimal) == 777
    printed_round_counts = [1,22,200,978,2780,4609,4249,1950,373,22]
    # Keep the discrepancy explicit: our frontier merges essential sets for
    # repeated X. The book says candidate PAIRS, so a difference alone is not
    # yet evidence of a typographical error.
    round_differences = [dict(clues=r['clues'], actual=r['candidates'], printed=p)
                         for r,p in zip(rounds,printed_round_counts) if r['candidates'] != p]
    assert sum(not oracle.records[full^(1<<i)]['unique'] for i in range(32)) == 10
    # Save the complete query/certificate set before the independent DLX pass.
    (OUT/'subset-queries.json').write_text(json.dumps(sorted(oracle.records.values(),key=lambda x:x['mask']), separators=(',',':'))+'\n')
    (OUT/'minimal-masks.json').write_text(json.dumps(sorted(minimal))+'\n')
    native = []
    for i, mask in enumerate(sorted(minimal)):
        board = [0]*81
        for j,v in enumerate(oracle.positions):
            if mask>>j&1:
                board[v] = initial[v]
        names, rows, moves, primary = instance(board)
        stats, _ = run(OUT/'minimal-native', f'{mask:08x}', input_text(names,rows,primary))
        assert stats['solutions'] == 1
        native.append(dict(mask=mask, **stats))
        if i%100 == 99:
            print('DLX minimal certificates',i+1,flush=True)
    diagram = json.loads((OUT/'pdf-grids.json').read_text())['sources']['54']['cells']
    board = [int(c) if c != '.' else 0 for c in diagram]
    assert all(not k or k == initial[v] for v,k in enumerate(board))
    mask = sum(1<<i for i,v in enumerate(oracle.positions) if board[v])
    assert mask in minimal and mask.bit_count() == 23
    # Clue subsets are listed in increasing clue order; compare these tuples.
    last = max(tuple(i for i in range(32) if m>>i&1) for m in minimal if m.bit_count() == 23)
    assert tuple(i for i in range(32) if mask>>i&1) == last
    assert next(s for s in native if s['mask']==mask)['nodes'] == 220
    # The last two clues in row-major order are 9 and 5, as in the question.
    assert [initial[v] for v in oracle.positions[-2:]] == [9,5]
    # Their simultaneous deletion is unique; it is among the recorded unique
    # supersets, or can be verified by a direct independent DLX call.
    short = list(initial)
    for v in oracle.positions[-2:]:
        short[v] = 0
    names, rows, _, primary = instance(short)
    short_stats,_ = run(OUT/'minimal-native','omit-final-95',input_text(names,rows,primary))
    assert short_stats['solutions'] == 1
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), oracle_source_sha256=oracle.build['source_sha256'],
                  grids_sha256=sha(OUT/'pdf-grids.json'), queries_sha256=sha(OUT/'subset-queries.json'),
                  minimal_masks_sha256=sha(OUT/'minimal-masks.json'), reference=reference,
                  clue_positions=oracle.positions, rounds=rounds, minimal_counts=dict(sorted(counts.items())),
                  printed_round_counts=printed_round_counts, round_differences=round_differences,
                  queries=len(oracle.records), queries_excluding_full=len(oracle.records)-1,
                  all_negative_answers_have_valid_witnesses=True, native_minimals=native,
                  diagram_mask=mask, final_95_omission=short_stats, seconds=time.monotonic()-start,
                  scope='Complete subset enumeration; all pruned nonunique masks have independently '
                        'validated alternative completions. All777 minimal unique masks separately '
                        'certified by unmodified DLX1. Historical call and mem counts assessed separately.')
    (OUT/'minimal.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Completed:',len(minimal),'minimal masks;',len(oracle.records),'queries;',round(result['seconds'],2),'seconds',flush=True)


if __name__ == '__main__':
    main()
