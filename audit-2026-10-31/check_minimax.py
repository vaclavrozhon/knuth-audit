#!/usr/bin/env python3
"""Check DLX84--85 against every row subset, not another search variant."""
from datetime import datetime, timezone
from itertools import combinations, product
from pathlib import Path
import hashlib, json, random
from colored_dlx import brute
from minimax_dlx import MinimaxDLX

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/minimax_mc'


def main():
    rng = random.Random(840085)
    universe = [tuple([(i,0) for i in (1,2) if mask>>(i-1)&1]+
                      ([] if c is None else [(3,c)]))
                for mask,c in product(range(1,4),(None,0,1,2))]
    cases = [(3,2,rows) for k in range(6) for rows in combinations(universe,k)]
    for _ in range(4000):
        primary = rng.randrange(1,5)
        n = primary+rng.randrange(4)
        rows = []
        for __ in range(rng.randrange(12)):
            items = rng.sample(range(1,n+1),rng.randrange(1,n+1))
            if not any(i<=primary for i in items):
                items.append(rng.randrange(1,primary+1))
            rows.append(tuple((i,0 if i<=primary else rng.randrange(3)) for i in items))
        cases.append((n,primary,rows))
    cases.append((0,0,[]))
    digest = hashlib.sha256()
    repaired = cuts = multi = unsat = jumps = 0
    witnesses = {}
    for number,(n,primary,rows) in enumerate(cases):
        all_models = brute(primary,rows)
        optimum = min((max(m,default=-1) for m in all_models),default=None)
        expected = {m for m in all_models if max(m,default=-1)==optimum}
        unsat += not bool(expected)
        multi += len(expected)>1
        for mrv,one in product((False,True),repeat=2):
            got = MinimaxDLX(n,primary,rows).solve_minimax(mrv=mrv,one=one)
            assert (got.solutions<=expected and len(got.solutions)==min(1,len(expected))) if one else got.solutions==expected, (number,n,primary,rows,mrv,one,got.solutions,expected)
            ranks = [max(m,default=-1) for m in got.incumbents]
            assert all(a>b if one else a>=b for a,b in zip(ranks,ranks[1:]))
            repaired += got.repaired_successors
            cuts += len(got.cut_events)
            jumps += sum(e['k']+1<e['depth'] for e in got.cut_events) if one else 0
            digest.update(json.dumps([number,mrv,one,sorted(got.solutions),got.cut_events]).encode())
            if len(got.cut_events)>1 and 'multiple_improvements' not in witnesses:
                witnesses['multiple_improvements'] = dict(n=n,primary=primary,rows=rows,mrv=mrv,one=one,
                    events=got.cut_events,incumbents=got.incumbents,solutions=sorted(got.solutions))
            if got.repaired_successors and 'successor_repair' not in witnesses:
                witnesses['successor_repair'] = dict(n=n,primary=primary,rows=rows,mrv=mrv,one=one,
                    events=got.cut_events,repairs=got.repaired_successors,solutions=sorted(got.solutions))
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),matrices=len(cases),
        policies=4,runs=4*len(cases),unsatisfiable=unsat,multiple_optima=multi,cutoff_changes=cuts,
        successor_repairs=repaired,nonlocal_backjumps=jumps,complete_model_digest=digest.hexdigest(),
        witnesses=witnesses,source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
          for p in ('check_minimax.py','minimax_dlx.py','colored_dlx.py')})
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'minimax.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('witnesses','source_sha256')}))


if __name__=='__main__': main()
