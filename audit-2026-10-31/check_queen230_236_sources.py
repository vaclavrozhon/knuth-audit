"""Finish source arithmetic, retaining all previously accepted queen censuses."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
from itertools import combinations
import json,time,os,re
from puzzle_xcc import save,sha
import verify_f075_f076,verify_f147
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/queen230_236'
def read(p):return json.loads((ROOT/p).read_text())
def norms(q):
    n=len(q);return [(2*r-n-1)**2+(2*c-n-1)**2 for r,c in enumerate(q,1)]
def rotations(q):
    n=len(q);p={(r,c-1) for r,c in enumerate(q)};a=set(p);kept=[]
    for degree in [90,180,270]:
        a={(c,n-1-r) for r,c in a}
        if a==p:kept.append(degree)
    return kept


def main():
    start=time.monotonic();assert not (OUT/'source-checked.json').exists()
    f=read('results/queen230_236/figures-checked.json');assert sha(ROOT/'extract_queen230_236.py')==f['checker_sha256']
    for p,h in f['dependencies'].items():assert sha(ROOT/p)==h
    for p,h in f['trace_hashes'].items():assert sha(OUT/p)==h
    for p,h in f['accepted_source_hashes'].items():assert sha(ROOT/p)==h
    a=verify_f075_f076.verify();b=verify_f147.verify();assert b['repaired']==f['repaired128']
    save(OUT/'f075-f076-witness.json',a);save(OUT/'f147-witness.json',b)
    text=(ROOT/'sources/queen230_236/original-498.txt').read_text();draft=(ROOT/'sources/queen230_236/draft-188.txt').read_text()
    for t in [text,draft]:assert re.search(r'\b'+r'\s+'.join(map(str,verify_f075_f076.N20))+r'\b',t)
    old=read('results/queen_costs/verified-summary.json');dlx=read('results/queen_costs/dlx5-verified.json')
    assert old['N2_constant']==680
    for k,n in [('distance_min',8),('distance_max',8),('floor_min',96),('norm_squared_min',16),('norm_squared_max',8),('ultimate',16)]:assert old[k]['count']==n
    assert dlx['distance_min']['gap']==17905986 and dlx['distance_max']['gap']==85831444
    assert all(dlx[k]['gap']>16 for k in ['distance_min','distance_max','product_min','product_max'])
    figs=read('results/queen_costs/figures-verified.json');p,q=figs['112'][1:]
    assert p[:4]==q[:4] and p[-4:]==q[-4:] and [17-c for c in p[4:12]]==q[4:12]
    assert sum(int((w/4)**.5) for w in norms(figs['112'][0]))==86
    assert sum(Fraction(w*w,4) for w in norms(figs['477'][0]))==127760
    assert sum(Fraction(w*w,4) for w in norms(figs['477'][1]))==127760
    assert sum(Fraction(w*w,4) for w in norms(figs['477'][2]))==187760
    assert sorted(norms(figs['477'][0]))!=sorted(norms(figs['477'][1]))
    # Literal four-option counterexample from236; complete16 subsets only.
    rows=[({1},1),({2},2),({1,3},3),({2,3},3)];solutions=[]
    for mask in range(16):
        chosen=[i for i in range(4) if mask>>i&1];flat=[v for i in chosen for v in rows[i][0]]
        if sorted(flat)==[1,2,3]:solutions.append(chosen)
    assert solutions==[[1,2],[0,3]]
    assert min(solutions,key=max)==[1,2]
    assert sorted((rows[i][1] for i in [0,3]),reverse=True)<sorted((rows[i][1] for i in [1,2]),reverse=True)
    # N2 formula for every permutation follows because the column summands are permuted.
    assert 2*sum(Fraction(2*k-17,2)**2 for k in range(1,17))==680
    spectra={str(n):rotations(q) for n,q in [(16,figs['152'][0])]+[(int(k),v) for k,v in f['large_permutations'].items() if k!='128']+[(128,f['repaired128'])]}
    assert spectra['16']==spectra['32']==[90,180,270]
    assert all(spectra[str(n)]==[] for n in [17,18,19,64,128])
    # Known threshold certificate is reused, with its explicit all-large-N inequality.
    threshold=read('results/queen_costs/power-threshold.json');ends=read('results/queen_costs/power-threshold-endpoints.json')
    assert threshold['classes']==1846955 and threshold['ultimate_classes']==8
    assert ends['large_bound']['exact_inequality'] and 16*113**80<117**80
    accepted=[str(p.relative_to(ROOT)) for p in sorted((ROOT/'results/queen_costs').glob('*.json'))]
    dependencies=['verify_f075_f076.py','verify_f147.py','extract_queen230_236.py']
    save(OUT/'source-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),nice=os.nice(0),wall_seconds=time.monotonic()-start,
        dependencies={p:sha(ROOT/p) for p in dependencies},accepted_data_hashes={p:sha(ROOT/p) for p in accepted},
        current_evidence_sha256={p:sha(ROOT/p) for p in ['results/queen230_236/figures-checked.json','sources/queen230_236/original-498.txt','sources/queen230_236/draft-188.txt']},
        old_optimal_sets_accepted=True,old_threshold_certificate_accepted=True,new_enumerated_subsets=16,example236_solutions=solutions,
        middle_eight_rows_reflect=True,quarterturn_invariance=spectra,old_censuses_repeated=0,new_optimization_searches=0,
        higher_n_global_optimality_independently_reproved=False,rotation_conjecture_proved_for_all_n=False))
    print('PASS:short witnesses F075/F076/F147,16subsets,source costs/reflection; old optimal sets and threshold reused, no optimization.')


if __name__=='__main__':main()
