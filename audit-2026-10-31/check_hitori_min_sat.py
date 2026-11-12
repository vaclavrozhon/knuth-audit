"""SAT search for <=11-black hitori covers on 7x7.

For each white vertex u without a black neighbor, auxiliary labels on W-u
certify that two neighbors of u lie in different connected components.
This is a necessary articulation condition even without global white
connectedness. The connected encoding found a valid 11-black witness;
it does NOT prove an impossibility. The mod-5 construction is audited
separately in check_hitori_sparse.py.
"""
from pathlib import Path
import argparse,gzip,hashlib,json,threading,time,subprocess
from pysat.card import CardEnc,EncType
from pysat.solvers import Solver
from check_hitori import Board
ROOT=Path(__file__).parent;OUT=ROOT/'results/hitori_min_sat'


def encode(m,n,k,connected=False):
    N=m*n;neigh={v:[w for w in range(N) if abs(w//n-v//n)+abs(w%n-v%n)==1] for v in range(N)}
    edges=[(v,w) for v in range(N) for w in neigh[v] if v<w]
    clauses=[[-v-1,-w-1] for v,w in edges]
    card=CardEnc.atmost(list(range(1,N+1)),bound=k,top_id=N,encoding=EncType.seqcounter)
    clauses+=card.clauses;top=max(N,card.nv)
    for u in range(N):
        label={}
        for v in range(N):
            if v!=u:top+=1;label[v]=top
        for v,w in edges:
            if u in (v,w):continue
            clauses += [[v+1,w+1,-label[v],label[w]],[v+1,w+1,label[v],-label[w]]]
        trigger=[u+1]+[v+1 for v in neigh[u]]
        clauses += [trigger+[label[v] for v in neigh[u]],trigger+[-label[v] for v in neigh[u]]]
    if connected:
        reach=[]
        for t in range(N):
            layer=[]
            for v in range(N):top+=1;layer.append(top)
            reach.append(layer)
        clauses += [[1,reach[0][0]],[-1,-reach[0][0]],[-1,reach[0][1]],[1,-reach[0][1]]]
        clauses += [[-reach[0][v]] for v in range(2,N)]
        for t in range(N):
            for v in range(N):
                clauses.append([-reach[t][v],-v-1])
                if t:clauses.append([-reach[t][v]]+[reach[t-1][w] for w in [v]+neigh[v]])
        clauses += [[v+1,reach[-1][v]] for v in range(N)]
    return top,clauses


def validate():
    checks=0
    for m,n in [(1,2),(1,3),(2,2),(2,3),(3,3)]:
        N=m*n;board=Board(m,n)
        for connected in (False,True):
            top,clauses=encode(m,n,N,connected)
            with Solver(name='g4',bootstrap_with=clauses) as solver:
                for black in range(1<<N):
                    white=board.full^black
                    independent=not black&board.neighbors(black)
                    if connected:expected=board.cover(black)
                    else:
                        # Direct component count before and after deleting each
                        # undominated white vertex, independent of SAT labels.
                        def comps(mask):
                            ans=0
                            while mask:
                                seen=mask&-mask
                                while True:
                                    nxt=seen|(board.neighbors(seen)&mask)
                                    if nxt==seen:break
                                    seen=nxt
                                mask^=seen;ans+=1
                            return ans
                        count=comps(white);undom=white&~board.neighbors(black)
                        expected=independent and all(comps(white^(1<<v))>count for v in range(N) if undom>>v&1)
                    observed=solver.solve(assumptions=[v+1 if black>>v&1 else -v-1 for v in range(N)])
                    assert observed==expected,(m,n,black,connected,observed,expected)
                    checks+=1
    return checks


def main():
    p=argparse.ArgumentParser();p.add_argument('--solver',default='g4');p.add_argument('--limit',type=int,default=900);p.add_argument('--connected',action='store_true');args=p.parse_args()
    OUT.mkdir(exist_ok=True);checks=validate();top,clauses=encode(7,7,11,args.connected)
    name='7x7-atmost11'+('-connected' if args.connected else '-relaxed')+'-'+args.solver
    base=OUT/name;cnf=f'p cnf {top} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses)
    base.with_suffix('.cnf').write_text(cnf)
    print(json.dumps(dict(name=name,validation_checks=checks,variables=top,clauses=len(clauses))),flush=True)
    start=time.monotonic()
    with Solver(name=args.solver,bootstrap_with=clauses,with_proof=True) as s:
        timer=threading.Timer(args.limit,s.interrupt);timer.start()
        try:answer=s.solve_limited(expect_interrupt=True)
        finally:timer.cancel()
        out=dict(name=name,validation_checks=checks,variables=top,clauses=len(clauses),answer=answer,seconds=time.monotonic()-start,stats=s.accum_stats())
        if answer:
            black=sum(1<<(v-1) for v in s.get_model() if 0<v<=49)
            out['black']=[divmod(v,7) for v in range(49) if black>>v&1];out['is_hitori_cover']=Board(7,7).cover(black)
        elif answer is False:
            proof='\n'.join(s.get_proof())+'\n';base.with_suffix('.drat').write_text(proof)
            result=subprocess.run(['/tmp/knuth-drat-trim/drat-trim',str(base.with_suffix('.cnf')),str(base.with_suffix('.drat'))],capture_output=True,text=True,timeout=600)
            base.with_suffix('.verify.txt').write_text(result.stdout+result.stderr)
            out['proof_verified']='s VERIFIED' in result.stdout;assert out['proof_verified']
            for suffix in ('.cnf','.drat'):
                path=base.with_suffix(suffix);data=path.read_bytes();out[suffix[1:]+'_sha256']=hashlib.sha256(data).hexdigest()
                with gzip.open(str(path)+'.gz','wb') as f:f.write(data)
                path.unlink()
        base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)

if __name__=='__main__':main()
