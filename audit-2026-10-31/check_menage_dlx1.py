#!/usr/bin/env python3
"""Reproduce the approximate DLX14 mems with explicit item ordering.

Small cases compare full model sets against a permutation oracle. The large
n10 cases compare counts with the earlier independent seating DP. MRV uses
unmodified archived author DLX1; first-item selection is our documented
change file. Output formatting and initialization are excluded from search
mems, as in the author's accounting.
"""
from datetime import datetime,timezone
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import hashlib
import json
import re
import subprocess
import time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/menage'


def input_text(n,order):
    seats=[f'S{j}' for j in range(n)];men=[f'M{k}' for k in range(n)]
    names=seats+men if order=='seats-first' else [v for pair in zip(seats,men) for v in pair]
    rows=[f'S{j} M{k}' for j in range(n) for k in range(n) if j not in (k,(k+1)%n)]
    return '\n'.join([' '.join(names)]+rows)+'\n'


def decode(text,n):
    models=set();current=None;rows=0
    def finish():
        if current is not None:
            assert rows==n and sorted(current)==list(range(n))
            assert all(seat not in (k,(k+1)%n) for k,seat in enumerate(current))
            model=tuple(current);assert model not in models;models.add(model)
    for line in text.splitlines():
        if re.fullmatch(r'\d+:',line):
            finish();current=[None]*n;rows=0
            assert int(line[:-1])==len(models)+1
        elif line.strip():
            assert current is not None
            seats=re.findall(r'\bS(\d+)\b',line);men=re.findall(r'\bM(\d+)\b',line)
            assert len(seats)==len(men)==1
            husband=int(men[0]);seat=int(seats[0]);assert current[husband] is None
            current[husband]=seat;rows+=1
    finish()
    return models


def main():
    build=json.loads((ROOT/'results/dancing_links/dlx1-build.json').read_text())
    for item in build['sources'].values():
        assert hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest()==item['sha256']
    for item in build['binaries'].values():
        assert hashlib.sha256(Path(item['path']).read_bytes()).hexdigest()==item['sha256']
    previous=json.loads((OUT/'finite-identity.json').read_text())
    cases=[]
    def run(n,order,variant,models):
        label=f'n{n}-{order}-{variant}'
        data=input_text(n,order);input_path=OUT/(label+'.dlx');input_path.write_text(data)
        command=[build['binaries'][variant]['path'],'v129']+(['m1'] if models else [])
        start=time.monotonic()
        result=subprocess.run(command,input=data,text=True,capture_output=True,check=True,timeout=120)
        elapsed=time.monotonic()-start
        (OUT/(label+'.log')).write_text(result.stderr)
        match=re.search(r'Altogether (\d+) solutions?, (\d+)\+(\d+) mems, (\d+) updates, (\d+) bytes, (\d+) nodes',result.stderr)
        assert match,result.stderr
        count,initial,mems,updates,bytes_used,nodes=map(int,match.groups())
        assert count==previous['subset_dp'][str(n)]
        case=dict(label=label,n=n,order=order,variant=variant,command=command,
            input_sha256=hashlib.sha256(data.encode()).hexdigest(),elapsed_seconds=elapsed,
            solutions=count,initialization_mems=initial,search_mems=mems,
            mems_per_solution=str(Fraction(mems,count)) if count else None,
            updates=updates,bytes=bytes_used,nodes=nodes)
        if models:
            expected={order for order in permutations(range(n))
                if all(seat not in (k,(k+1)%n) for k,seat in enumerate(order))}
            observed=decode(result.stdout,n)
            assert observed==expected and len(observed)==count
            canonical=json.dumps(sorted(observed),separators=(',',':')).encode()
            case.update(full_model_sets_equal=True,model_set_sha256=hashlib.sha256(canonical).hexdigest())
        else:assert not result.stdout
        cases.append(case)
    for n in range(2,9):
        for variant in ['dlx1','dlx1-nomrv']:run(n,'alternating',variant,True)
    for order in ['seats-first','alternating']:
        for variant in ['dlx1','dlx1-nomrv']:run(10,order,variant,False)
    comparison=[]
    for variant,printed in [('dlx1',180),('dlx1-nomrv',275)]:
        case=next(c for c in cases if c['n']==10 and c['order']=='alternating' and c['variant']==variant)
        value=Fraction(case['search_mems'],case['solutions'])
        assert abs(value-printed)<Fraction(5,2)
        comparison.append(dict(variant=variant,printed_approximation=printed,
            observed=float(value),absolute_difference=float(abs(value-printed)),
            interpretation='Within2.5 mems per solution; nearest multiple of5 agrees. The book says about.'))
    report=dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        build_metadata='../dancing_links/dlx1-build.json',cases=cases,comparison=comparison,
        scope='14 complete small model sets; four n10 counts and explicit mem accounting. This supports the approximate published costs for alternating item order, not a claim to have recovered an unpublished original first-item program.')
    (OUT/'dlx1-verified.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(status=report['status'],complete_small_model_sets=14,comparison=comparison),indent=2))


if __name__=='__main__':main()
