"""One bounded SAT attempt on the corrected reduced Y-tiling problem; no benchmark."""
from collections import Counter,defaultdict
from datetime import datetime,timezone
from itertools import combinations
from pathlib import Path
from threading import Timer
import json,os,time
from pysat.solvers import Solver
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/exchanges208_214/y-bounded.json'
S=[['01','11','21','31','10'],['00','01','02','03','11'],
   ['00','10','20','30','21'],['10','11','12','13','02'],
   ['01','11','21','31','20'],['00','01','02','03','12'],
   ['00','10','20','30','11'],['10','11','12','13','01']]


def normalized(cells):
    r=min(x for x,y in cells);c=min(y for x,y in cells)
    return tuple(sorted((x-r,y-c) for x,y in cells))


def y_orientations():
    # Independent geometric construction: a four-cell bar and an off-center arm.
    out=set();base=[(0,0),(1,0),(2,0),(3,0),(1,1)]
    for reflect in [False,True]:
        cells=[(x,-y if reflect else y) for x,y in base]
        for _ in range(4):out.add(normalized(cells));cells=[(y,-x) for x,y in cells]
    return out


def validate(selected):
    counts=Counter(p for q in selected for p in q['cells'])
    assert set(counts)=={(r,c) for r in range(15) for c in range(15)}
    assert set(counts.values())=={1} and len(selected)==45
    assert all(normalized(q['cells']) in y_orientations() for q in selected)
    assert sum((7,7) in q['cells'] for q in selected)==1
    assert all(q['orientation']==0 for q in selected if (7,7) in q['cells'])
    sec=Counter(q['secondary'] for q in selected if q['secondary'] is not None)
    assert all(n==1 for n in sec.values())


def main():
    assert not OUT.exists();assert os.nice(0)>=15
    started=time.monotonic();shapes=[[(int(t[0]),int(t[1])) for t in ss] for ss in S]
    assert {normalized(s) for s in shapes}==y_orientations()
    options=[];cellvars=defaultdict(list);secvars=defaultdict(list)
    for k,shape in enumerate(shapes):
        for i in range(15):
            for j in range(15):
                cells=[(i+a,j+b) for a,b in shape]
                if any(a>=15 or b>=15 for a,b in cells):continue
                if (7,7) in cells and k!=0:continue
                secondary={4:('V',i,j),5:('H',i+1,j),6:('V',i,j+1),7:('H',i,j)}.get(k)
                options.append(dict(orientation=k,anchor=[i,j],cells=cells,secondary=secondary));var=len(options)
                for p in cells:cellvars[p].append(var)
                if secondary is not None:secvars[secondary].append(var)
    clauses=[]
    for vs in cellvars.values():clauses.append(vs);clauses += [[-a,-b] for a,b in combinations(vs,2)]
    for vs in secvars.values():clauses += [[-a,-b] for a,b in combinations(vs,2)]
    report=dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
        dependency_sha256={'puzzle_xcc.py':sha(ROOT/'puzzle_xcc.py')},pid=os.getpid(),nice=os.nice(0),
        method='Glucose4, exact-cover cell clauses plus corrected secondary conflicts; selected tilings independently validated geometrically.',
        solver_time_limit_seconds=20,variables=len(options),clauses=len(clauses),
        expected_count_from_book=16,status='running',completed=False,solutions=[],
        limitation='A timeout is incomplete, not UNSAT. No historical mem count or runtime comparison is reproduced.')
    save(OUT,report)
    with Solver(name='g4',bootstrap_with=clauses) as solver:
        timer=Timer(20,solver.interrupt);timer.daemon=True;timer.start()
        try:
            while True:
                ok=solver.solve_limited(expect_interrupt=True)
                if ok is None:report['status']='time_limit';break
                if not ok:report['status']='complete';report['completed']=True;break
                selected_vars=[v for v in solver.get_model() if 1<=v<=len(options)]
                selected=[options[v-1] for v in selected_vars];validate(selected)
                report['solutions'].append(selected);save(OUT,report)
                solver.add_clause([-v for v in selected_vars])
            report['solver_statistics']=solver.accum_stats()
        finally:timer.cancel()
    report['solution_count']=len(report['solutions']);report['wall_seconds']=time.monotonic()-started
    report['completed_at_utc']=datetime.now(timezone.utc).isoformat();save(OUT,report)
    print(json.dumps({k:v for k,v in report.items() if k not in ['solutions','dependency_sha256']},ensure_ascii=False))


if __name__=='__main__':main()
