#!/usr/bin/env python3
"""Audit the two complete printed memory tables and literal Algorithm X."""
from collections import Counter
from datetime import datetime,timezone
from itertools import combinations
from pathlib import Path
import hashlib
import json
import random
from spacer_algorithm_x import SpacerX

ROOT=Path(__file__).resolve().parent
ROWS=[(3,5),(1,4,7),(2,3,6),(1,4,6),(2,7),(4,5,7)]
# Transcribed from visually checked PDF pp68/417. None means a printed dash.
TABLE1=dict(
    L=[7,0,1,2,3,4,5,6],R=[1,2,3,4,5,6,7,0],
    T=[None,2,2,2,3,2,2,3,0,3,5,-1,1,4,7,-2,2,3,6,-3,1,4,6,-4,2,7,-5,4,5,7,-6],
    U=[None,20,24,17,27,28,22,29,None,3,5,9,1,4,7,12,2,9,6,16,12,13,18,20,16,14,24,21,10,25,27],
    D=[None,12,16,9,13,10,18,14,10,17,28,14,20,21,25,18,24,3,22,22,1,27,6,25,2,29,29,4,5,7,None])
TABLE11=dict(
    L=[0,0,0,0,3,0,5,6],R=[0,2,3,5,5,0,0,0],
    T=[None,2,1,1,1,0,0,1,0,3,5,-1,1,4,7,-2,2,3,6,-3,1,4,6,-4,2,7,-5,4,5,7,-6],
    U=[None,20,16,9,27,5,6,25,None,3,5,9,1,4,7,12,2,9,6,16,12,4,18,20,16,7,24,4,10,25,27],
    D=[None,12,16,9,27,5,6,25,10,3,5,14,20,21,25,18,2,3,6,22,1,27,6,25,2,7,29,4,5,7,None])


def compare_table(run,table):
    cells=0
    for name,values in table.items():
        for index,expected in enumerate(values):
            if expected is not None:
                assert getattr(run,name)[index]==expected,(name,index,expected,getattr(run,name)[index])
                cells+=1
    assert run.names[1:]==list('abcdefg')
    return cells+7


def subset_oracle(n,primary,rows):
    result=set()
    for bits in range(1<<len(rows)):
        picked=tuple(j for j in range(len(rows)) if bits>>j&1)
        counts=Counter(i for j in picked for i in rows[j])
        if all(counts[i]==1 for i in range(1,primary+1)) and all(counts[i]<=1 for i in range(primary+1,n+1)):
            result.add(picked)
    return result


def main():
    example=SpacerX(list('abcdefg'),ROWS)
    cells=compare_table(example,TABLE1)
    assert example.describe(21)==(['d','f','a'],(2,3))
    assert example.describe(0) is None and example.describe(example.Z+1) is None
    assert example.T[23]==-4 and example.D[23]==25
    first=[]
    def observe(run,level,item,chosen):
        if not first:
            assert (level,item,chosen)==(2,5,[12,16])
            first.append(dict(level=level,item=item,chosen=chosen,
                              table_cells=compare_table(run,TABLE11)))
    example.solve(observer=observe)
    assert example.solutions=={(0,3,4)} and len(first)==1
    # The answer12 color-printing convention, including a purified negative
    # node whose original color is saved at the item header (pp89–90).
    colors=[0]*(example.Z+1);colors[21]=-1;colors[4]=17;colors[22]=23
    assert example.describe(21,colors)==(['d:17','f:23','a'],(2,3))
    counts=Counter();by_n=Counter();rng=random.Random(6132026);case_keys=set()
    def audit(n,primary,rows):
        case_keys.add((n,primary,tuple(rows)))
        expected=subset_oracle(n,primary,rows)
        names=[('#' if i%2 else '')+str(i) for i in range(1,n+1)]
        for policy in ('first','mrv','sharp'):
            run=SpacerX(names,rows,primary).solve(policy)
            assert run.solutions==expected,(n,primary,rows,policy)
            counts.update(run.checks);counts['complete_runs']+=1
        by_n[n]+=1;counts['input_cases']+=1
    for n in range(5):
        for primary in range(n+1):
            all_rows=[tuple(i+1 for i in range(n) if bits>>i&1)
                      for bits in range(1,1<<n) if bits & ((1<<primary)-1)]
            for size in range(min(3,len(all_rows))+1):
                for rows in combinations(all_rows,size):audit(n,primary,rows)
    for _ in range(300):
        n=rng.randint(1,7);primary=rng.randint(1,n);rows=[]
        for _ in range(rng.randrange(10)):
            row={rng.randint(1,primary)}
            row.update(i for i in range(1,n+1) if rng.randrange(3)==0)
            row=list(row);rng.shuffle(row);rows.append(tuple(row))
        audit(n,primary,rows)
    counts['unique_input_layouts']=len(case_keys)
    result=dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                    for p in ['spacer_algorithm_x.py','check_spacer_algorithm_x.py']},
                table1_cells=cells,first_X7=first[0],table1=TABLE1,answer11=TABLE11,
                example_solution_options=[1,4,5],counts=dict(counts),inputs_by_n=dict(by_n),
                independent_oracle='All subsets of options; full solution sets, including duplicate option identities.',
                scope='Literal I1–I5 and X1–X8, both complete tables, all cover/uncover restorations, MRV/sharp priorities, residual columns, and cyclic row descriptions.')
    out=ROOT/'results/dancing_links';out.mkdir(exist_ok=True)
    (out/'spacer-verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','table1_cells','first_X7','counts','inputs_by_n']},indent=2))


if __name__=='__main__':main()
