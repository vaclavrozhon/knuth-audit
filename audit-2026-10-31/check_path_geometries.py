"""Exhaust the 625 maximum-horizontal geometries, up to their D2 symmetries."""
from collections import Counter,defaultdict
from itertools import product
from pathlib import Path
import gzip,hashlib,json,subprocess,threading,time
from pysat.solvers import Solver
from check_path_dominoes import catalog,encode,options_for,verify,save_cnf
ROOT=Path(__file__).parent;OUT=ROOT/'results/path_dominoes/geometries'


def orbit(cols):
    return {tuple(cols),tuple(reversed(cols)),tuple(8-c for c in cols),tuple(8-c for c in reversed(cols))}


def geometry(cols):
    places=set();taken=set()
    for j,c in enumerate(cols):
        cells=((2*j,c),(2*j+1,c));places.add(cells);taken.update(cells)
    for r in range(8):
        for c in range(9):
            if (r,c) in taken:continue
            cells=((r,c),(r,c+1));assert c+1<9 and (r,c+1) not in taken
            places.add(cells);taken.update(cells)
    assert len(places)==36 and len(taken)==72
    return places


def solve(cols,models,inventory,limit=120):
    label='-'.join(map(str,cols));base=OUT/label
    existing=base.with_suffix('.json')
    if existing.exists():
        old=json.loads(existing.read_text())
        if old.get('proof_verified'):return old
    top,clauses,options=encode(8,9,inventory,geometry=geometry(cols))
    lookup={(o['cells'],o['mask']):i for i,o in enumerate(options,1)}
    for model in models:
        verify(model,8,9,inventory,32)
        clauses.append([-lookup[o['cells'],o['mask']] for o in model])
    start=time.monotonic()
    with Solver(name='g4',bootstrap_with=clauses,with_proof=True) as solver:
        timer=threading.Timer(limit,solver.interrupt);timer.start()
        try:answer=solver.solve_limited(expect_interrupt=True)
        finally:timer.cancel()
        out=dict(columns=cols,orbit_size=len(orbit(cols)),known_models=len(models),variables=top,
                 clauses=len(clauses),seconds=time.monotonic()-start,
                 status='EXHAUSTED' if answer is False else 'TIMEOUT' if answer is None else 'NEW_MODEL')
        if answer is True:
            selected=[options[v-1] for v in solver.get_model() if 1<=v<=len(options)]
            verify(selected,8,9,inventory,32);out['new_model']=selected
        elif answer is False:
            cnf=base.with_suffix('.cnf');proof=base.with_suffix('.drat')
            save_cnf(cnf,top,clauses);proof.write_text('\n'.join(solver.get_proof())+'\n')
            p=subprocess.run(['/tmp/knuth-drat-trim/drat-trim',str(cnf),str(proof),'-t','120'],text=True,capture_output=True,timeout=130)
            base.with_suffix('.verification.txt').write_text(p.stdout+p.stderr)
            out['proof_verified']=p.returncode==0 and 's VERIFIED' in p.stdout
            assert out['proof_verified'],p.stdout+p.stderr
            for path in [cnf,proof]:
                data=path.read_bytes();out[path.suffix[1:]+'_sha256']=hashlib.sha256(data).hexdigest()
                path.with_suffix(path.suffix+'.gz').write_bytes(gzip.compress(data,mtime=0));path.unlink()
        existing.write_text(json.dumps(out,indent=2)+'\n');return out


def main():
    OUT.mkdir(exist_ok=True);all_patterns,_,_=catalog()
    inventory=Counter(v for p,v in all_patterns.items() if len(p) in (1,2))
    global_options=options_for(8,9,inventory);by_geo=defaultdict(list);seen=set()
    for line in (ROOT/'results/path_dominoes/max36.models.jsonl').read_text().splitlines():
        ids=tuple(sorted(json.loads(line)));assert ids not in seen;seen.add(ids)
        selected=[global_options[v-1] for v in ids];verify(selected,8,9,inventory,32)
        vertical=sorted(o['cells'][0] for o in selected if o['orientation']=='V')
        assert [r for r,c in vertical]==[0,2,4,6] and all(c%2==0 for r,c in vertical)
        cols=tuple(c for r,c in vertical);by_geo[cols].append(selected)
    assert len(seen)==6420
    representatives=sorted({min(orbit(cols)) for cols in product(range(0,9,2),repeat=4)})
    assert len(representatives)==169
    results=[]
    for cols in representatives:
        assert all(len(by_geo[member])==len(by_geo[cols]) for member in orbit(cols))
        result=solve(cols,by_geo[cols],inventory);results.append(result)
        print(json.dumps({k:v for k,v in result.items() if k not in ('new_model','cnf_sha256','drat_sha256')}),flush=True)
        summary=dict(geometries=625,orbits=169,verified_models=len(seen),completed=len(results),
                     exhausted=sum(x['status']=='EXHAUSTED' for x in results),
                     weighted_models=sum(x['orbit_size']*x['known_models'] for x in results),results=results)
        (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    if all(x['status']=='EXHAUSTED' for x in results):
        assert sum(x['orbit_size']*x['known_models'] for x in results)==6420
        print('ALL 625 GEOMETRIES EXHAUSTED WITH VERIFIED PROOFS',flush=True)

if __name__=='__main__':main()
