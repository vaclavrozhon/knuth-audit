#!/usr/bin/env python3
"""DLX55b: enumerate minimal small trades and certify the19-clue obstruction.

Run with the existing PySAT venv under an external3600s timeout. Checkpoints
contain complete independently validated trade witnesses and are resumable.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import gzip
import json
import os
import subprocess
import sys
import time
from pysat.card import CardEnc, EncType
from pysat.formula import CNF
from pysat.solvers import Solver
from check_sudoku_basics import UNITS
from dlx1_audit_tools import ROOT, sha

OUT = ROOT/'results/sudoku_variants/unavoidable55'


def encode_sudoku():
    groups = [[9*v+k for k in range(1,10)] for v in range(81)]
    groups += [[9*v+k for v in unit] for unit in UNITS for k in range(1,10)]
    clauses = []
    for group in groups:
        clauses.append(group)
        clauses.extend([-a,-b] for i,a in enumerate(group) for b in group[i+1:])
    return clauses


def decode(model):
    positives = set(x for x in model if 0<x<=729)
    board = [next(k for k in range(1,10) if 9*v+k in positives) for v in range(81)]
    assert len(positives) == 81
    assert all({board[v] for v in unit} == set(range(1,10)) for unit in UNITS)
    return board


def proof(label,clauses):
    cnf = CNF(from_clauses=clauses)
    cnf.to_file(str(OUT/(label+'.cnf')))
    start = time.monotonic()
    with Solver(name='g4',bootstrap_with=clauses,with_proof=True) as solver:
        assert not solver.solve(),label
        lines = solver.get_proof()
        stats = solver.accum_stats()
    path = OUT/(label+'.drat')
    path.write_text('\n'.join(lines)+'\n')
    command = ['/tmp/knuth-drat-trim/drat-trim',str(OUT/(label+'.cnf')),str(path)]
    result = subprocess.run(command,text=True,capture_output=True,timeout=600)
    (OUT/(label+'-verify.log')).write_text(result.stdout+result.stderr)
    assert result.returncode == 0 and 'VERIFIED' in result.stdout,(label,result.stdout[-1000:])
    digest = sha(path)
    with gzip.open(str(path)+'.gz','wb') as output:
        output.write(path.read_bytes())
    size = path.stat().st_size
    path.unlink()
    return dict(status='UNSAT with independently checked DRAT',cnf_sha256=sha(OUT/(label+'.cnf')),
                proof_sha256=digest,proof_bytes=size,compressed_proof_sha256=sha(str(path)+'.gz'),
                verifier_command=command,verifier_sha256=sha(command[0]),solver_statistics=stats,
                elapsed_seconds=time.monotonic()-start)


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    start = time.monotonic()
    source = ROOT/'results/sudoku_basics/pdf-grids.json'
    reference = json.loads(source.read_text())['sources']['28b']['board']
    known = [9*v+k for v,k in enumerate(reference)]
    clauses = encode_sudoku()+[[-x for x in known]]
    clauses += CardEnc.atmost(lits=[-x for x in known],bound=18,top_id=729,encoding=EncType.totalizer).clauses
    checkpoint = OUT/'trades.json'
    records = json.loads(checkpoint.read_text()) if checkpoint.exists() else []
    for r in records:
        assert [v for v in range(81) if r['alternative'][v] != reference[v]] == r['positions']
        assert all({r['alternative'][v] for v in unit} == set(range(1,10)) for unit in UNITS)
        clauses.append([known[v] for v in r['positions']])
    state = dict(status='running',pid=os.getpid(),command=[sys.executable,str(Path(__file__).resolve())],
                 external_timeout_seconds=3600,started_at_utc=datetime.now(timezone.utc).isoformat(),
                 source_sha256=sha(__file__),reference_sha256=sha(source),resumed_trades=len(records))
    (OUT/'run.json').write_text(json.dumps(state,indent=2)+'\n')
    with Solver(name='cadical195',bootstrap_with=clauses) as solver:
        while solver.solve():
            board = decode(solver.get_model())
            difference = {v for v in range(81) if board[v] != reference[v]}
            assert 0<len(difference)<=18
            for v in sorted(difference):
                if v not in difference:
                    continue
                assumptions = [known[u] for u in range(81) if u not in difference or u == v]
                if solver.solve(assumptions=assumptions):
                    board = decode(solver.get_model())
                    new = {u for u in range(81) if board[u] != reference[u]}
                    assert new < difference and v not in new
                    difference = new
            positions = sorted(difference)
            assert all(not set(r['positions']).issubset(difference) for r in records)
            records.append(dict(positions=positions,alternative=board))
            clause = [known[v] for v in positions]
            clauses.append(clause); solver.add_clause(clause)
            if len(records)%50 == 0:
                checkpoint.write_text(json.dumps(records,indent=2)+'\n')
                state.update(trades=len(records),elapsed_seconds=time.monotonic()-start)
                (OUT/'run.json').write_text(json.dumps(state,indent=2)+'\n')
                print('trades',len(records),'seconds',round(time.monotonic()-start,2),flush=True)
    checkpoint.write_text(json.dumps(records,indent=2)+'\n')
    state.update(phase='proofs',trades=len(records),size_distribution=dict(Counter(len(r['positions']) for r in records)))
    (OUT/'run.json').write_text(json.dumps(state,indent=2)+'\n')
    print('enumeration complete',len(records),state['size_distribution'],flush=True)
    exhaustive = proof('enumeration-exhaustive',clauses)
    hit = [[v+1 for v in r['positions']] for r in records]
    hit += CardEnc.atmost(lits=list(range(1,82)),bound=19,top_id=81,encoding=EncType.seqcounter).clauses
    # The nine disjoint-group constraints are independently established in
    # clue-bounds.json. They are redundant for a unique Sudoku but aid search.
    bounds = json.loads((ROOT/'results/sudoku_variants/clue-bounds.json').read_text())
    top = max(abs(x) for c in hit for x in c)
    for group in bounds['55_groups']['b']:
        encoded = CardEnc.atleast(lits=[v+1 for v in group['positions']],bound=2,top_id=top,encoding=EncType.seqcounter)
        hit += encoded.clauses; top = encoded.nv
    obstruction = proof('no19clues',hit)
    state.update(status='verified',finished_at_utc=datetime.now(timezone.utc).isoformat(),
                 elapsed_seconds=time.monotonic()-start,enumeration_certificate=exhaustive,
                 no19_certificate=obstruction,trades_sha256=sha(checkpoint),
                 book_claimed_trades=2043,book_count_matches=len(records)==2043)
    (OUT/'run.json').write_text(json.dumps(state,indent=2)+'\n')
    print(json.dumps({k:state[k] for k in ['status','trades','size_distribution','book_count_matches','elapsed_seconds']},indent=2))


if __name__ == '__main__':
    main()
