"""Independent Boolean/cardinality models for DLX105--107, exhaustively solved.

Run with /tmp/knuth-audit-sat-venv/bin/python. Model blocking projects away
auxiliary cardinality variables and unconstrained letters of unused cells.
"""
from datetime import datetime,timezone
from itertools import combinations
from pathlib import Path
import json,os,time
from pysat.card import CardEnc,EncType
from pysat.formula import CNF,IDPool
from pysat.solvers import Solver
from puzzle_xcc import OUT,save,sha
from word_puzzles import WORDS105,WORDS106,WORDS107,ALPHABET107,placements,orbit


def independent_catalog(words,n):
    """Every ordered pair of endpoints; independently derive straight segments."""
    catalog=[]
    for wi,word in enumerate(words):
        length=len(word)-1
        for first in range(n*n):
            r,c=divmod(first,n)
            for last in range(n*n):
                rr,cc=divmod(last,n);dr,dc=rr-r,cc-c
                if max(abs(dr),abs(dc))!=length or abs(dr) not in (0,length) or abs(dc) not in (0,length):continue
                step=(dr//length)*n+dc//length
                letters=tuple((first+k*step,ch) for k,ch in enumerate(word))
                catalog.append((wi,letters))
    return catalog


def check(label,words,n,copies,sudoku=False):
    places=placements(words,n,False)
    keys=[(p['word'],tuple(p['letters'])) for p in places]
    assert len(keys)==len(set(keys))
    assert set(keys)==set(independent_catalog(words,n))
    pool=IDPool();cnf=CNF()
    pv=[pool.id(('placement',k)) for k in range(len(places))]
    alphabet=ALPHABET107 if sudoku else sorted(set(''.join(words)))
    cell={(c,l):pool.id(('cell',c,l)) for c in range(n*n) for l in alphabet}
    def exact(lits,bound=1):
        cnf.extend(CardEnc.equals(lits=lits,bound=bound,vpool=pool,encoding=EncType.seqcounter).clauses)
    def atmost(lits):
        cnf.extend([-a,-b] for a,b in combinations(lits,2))
    for wi in range(len(words)):exact([pv[k] for k,p in enumerate(places) if p['word']==wi],copies)
    for k,p in enumerate(places):
        for c,l in p['letters']:cnf.append([-pv[k],cell[c,l]])
    for c in range(n*n):
        lits=[cell[c,l] for l in alphabet]
        if sudoku:exact(lits)
        else:atmost(lits)
    if sudoku:
        for l in alphabet:
            for r in range(9):atmost([cell[9*r+c,l] for c in range(9)])
            for c in range(9):atmost([cell[9*r+c,l] for r in range(9)])
            for r in range(3):
                for c in range(3):atmost([cell[9*(3*r+i)+3*c+j,l] for i in range(3) for j in range(3)])
    path=OUT/(label+'-sat.cnf');cnf.to_file(str(path))
    started=time.monotonic()
    meta=dict(status='running',pid=os.getpid(),started_utc=datetime.now(timezone.utc).isoformat(),
              variables=pool.top,clauses=len(cnf.clauses),formula_sha256=sha(path),solver='Glucose4 viaPySAT',
              script_sha256=sha(__file__))
    save(OUT/(label+'-sat-run.json'),meta)
    models=set()
    with Solver(name='g4',bootstrap_with=cnf.clauses) as solver:
        while solver.solve():
            values={v for v in solver.get_model() if v>0}
            chosen=tuple(k for k,v in enumerate(pv) if v in values)
            assert len(chosen)==len(words)*copies
            board=['.']*(n*n)
            for k in chosen:
                for c,l in places[k]['letters']:
                    assert board[c] in ('.',l);board[c]=l
            block=[-pv[k] for k in chosen]
            if sudoku:
                for (c,l),v in cell.items():
                    if v in values:
                        assert board[c] in ('.',l);board[c]=l;block.append(-v)
            model=(chosen,''.join(board))
            assert model not in models;models.add(model)
            solver.add_clause(block)
        stats=solver.accum_stats()
    previous=json.loads((OUT/(label+'-decoded.json')).read_text())
    expected={(tuple(m['chosen']),m['board']) for m in previous['models']}
    assert models==expected,(label,len(models),len(expected),len(models-expected),len(expected-models))
    relevant={m for m in models if m[1].count('.')==1} if label=='words105' else models
    meta.update(status='completed',elapsed_seconds=time.monotonic()-started,stats=stats,
                total_models=len(models),requested_models=len(relevant),
                requested_boards=len({b for c,b in relevant}),
                requested_dihedral_classes=len({min(orbit(b,n)) for c,b in relevant}),
                exact_model_set_equal_to_original_dlx=True,exhausted=True)
    save(OUT/(label+'-sat.json'),meta);save(OUT/(label+'-sat-run.json'),meta)
    print(label,'SAT complete',len(models),'requested',len(relevant),'seconds',meta['elapsed_seconds'],flush=True)


def main():
    jobs=[('words105',WORDS105,6,1,False),('words106',WORDS106,5,2,False),
          ('words107-pair',['COMPUTER','CORPORATE'],9,1,True),
          ('words107-eleven',[w for w in WORDS107 if w!='CORPORATE'],9,1,True)]
    for args in jobs:check(*args)


if __name__=='__main__':main()
