"""Independent SAT prefix certificates for the two n=16 lexical extrema."""
from pathlib import Path
from itertools import combinations
import json,time
from pysat.solvers import Solver
ROOT=Path(__file__).parent;OUT=ROOT/'results/langford_costs'
n=16;rows=[(i,j,j+i+1) for i in range(1,n+1) for j in range(2*n-i-1)]
groups=[[v for v,(i,j,k) in enumerate(rows,1) if i==a] for a in range(1,n+1)]
groups += [[v for v,(i,j,k) in enumerate(rows,1) if p in (j,k)] for p in range(2*n)]
clauses=[]
for group in groups:
    clauses.append(group)
    clauses.extend([-a,-b] for a,b in combinations(group,2))
reports=[]
for descending in [False,True]:
    start=time.monotonic();seq=[0]*(2*n);fixed=[];trace=[]
    with Solver(name='g4',bootstrap_with=clauses) as sat:
        while 0 in seq:
            pos=seq.index(0)
            candidates=sorted([(i,v,k) for v,(i,j,k) in enumerate(rows,1) if j==pos],reverse=descending)
            for i,v,k in candidates:
                ok=sat.solve(assumptions=fixed+[v]);trace.append(dict(slot=pos+1,value=i,satisfiable=ok))
                if ok:
                    assert not seq[k]
                    fixed.append(v);seq[pos]=seq[k]=i;break
            else:raise AssertionError('No completion')
    for i in range(1,n+1):
        p=[j for j,x in enumerate(seq) if x==i];assert len(p)==2 and p[1]-p[0]==i+1
    reports.append(dict(kind='max' if descending else 'min',sequence=seq,trace=trace,seconds=time.monotonic()-start))
basics=json.loads((OUT/'basics.json').read_text())
assert reports[0]['sequence']==basics['lexmin'] and reports[1]['sequence']==basics['lexmax']
assert reports[1]['sequence']>basics['printed_lexmax']
(OUT/'sat-lex.json').write_text(json.dumps(dict(variables=len(rows),clauses=len(clauses),extrema=reports),indent=2)+'\n')
print('SAT extrema agree with independent direct DFS:',[r['sequence'] for r in reports])
