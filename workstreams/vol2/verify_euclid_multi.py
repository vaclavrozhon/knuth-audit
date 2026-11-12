#!/usr/bin/env python3
"""Counterexamples and corrected sharp bounds for TAOCP4.5.3-36."""
from pathlib import Path
from math import gcd,comb
import json,os,sys,time
from verify_euclid_discrete import steps

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/euclid-multi.json'
FIB=[0,1]
while len(FIB)<205:FIB.append(sum(FIB[-2:]))

def run(values,trace=False):
    d=values[-1];count=0;calls=[]
    for k in range(len(values)-2,-1,-1):
        if d==1:break
        u=values[k];v=d;divisions=[]
        while v:
            q,r=divmod(u,v)
            if trace:divisions.append([u,v,q,r])
            u,v=v,r;count+=1
        calls.append({'index_zero_based':k,'input':[values[k],d],'gcd':u,'divisions':divisions})
        d=u
    return count,d,calls

def explicit_and_families():
    rows=[]
    for values,expected in [([5,3,3],4),([3,2,2],3)]:
        count,d,calls=run(values,True);assert count==expected and d==1
        rows.append({'values':values,'N':count,'calls':calls,
                     'printed_min_last':2*FIB[count-len(values)+2],
                     'printed_min_first':2*FIB[count-len(values)+3]+1})
    cases=0
    for n in range(3,17):
        for N in range(n,n+61):
            k=N-n+2
            values=[FIB[k+2]]+[FIB[k+1]]*(n-1)
            count,d,calls=run(values)
            assert count==N and d==1 and len(calls)==n-1
            assert values[-1]==FIB[N-n+3] and values[0]==FIB[N-n+4]
            cases+=1
    return {'counterexamples':rows,'attainment_families':cases,'n_range':'3..16','N_range':'n..n+60'}

def all_residue_transitions():
    # For an arbitrary positive input u, one call depends only on u mod d.
    limit=144;transitions={}
    for d in range(2,limit+1):
        transitions[d]={(gcd(d,r),1+steps(d,r)) for r in range(d)}
    possible={d:{0} for d in range(1,limit+1)}
    rows=[];checked=0
    for s in range(1,9):
        next_possible={1:{0}}
        for d in range(2,limit+1):
            costs={j+c for g,j in transitions[d] for c in possible[g]}
            next_possible[d]=costs
            for N in costs:
                if N>=s+1:assert d>=FIB[N-s+2];checked+=1
        possible=next_possible
        n=s+1
        if n>=3:
            minima={}
            for d,costs in possible.items():
                for N in costs:
                    if N>=n:minima[N]=min(minima.get(N,limit+1),d)
            for N,d in minima.items():assert d==FIB[N-n+3]
            rows.append({'n':n,'minimum_last_by_N':dict(sorted(minima.items()))})
    return {'max_last_input':limit,'max_call_slots':8,'unbounded_other_inputs':'all possible residues are represented',
            'total_distinct_transitions':sum(map(len,transitions.values())),
            'reachable_cost_bound_checks':checked,'minima':rows}

def ordered_lower_lemmas():
    first=second=0
    for u in range(1,801):
        for v in range(1,u+1):
            j=steps(u,v);d=gcd(u,v)
            assert v>=FIB[j+1]*d;second+=1
            if j>=2:assert u>=FIB[j+2]*d;first+=1
    products=0
    for a in range(2,82):
        for b in range(2,82):
            assert FIB[a]*FIB[b]>=FIB[a+b-2];products+=1
    for a in range(81):
        for b in range(81):
            assert FIB[a+3]*FIB[b+2]>=FIB[a+b+3];products+=1
    # Preserve the earlier independent enumeration; do not rerun it.
    pilots=[]
    for n,M,maxN in [(3,90,10),(4,35,9),(5,21,9)]:
        pilots.append({'n':n,'max_input':M,'ordered_tuples':comb(M+n-1,n),
                       'observed_minimum_first_by_N':{N:FIB[N-n+4] for N in range(n,maxN+1)},
                       'provenance':'Successful earlier exhaustive combinations_with_replacement pilot, session66705; results printed before this runner.'})
    return {'second_operand_bounds':second,'first_operand_bounds_j_ge_2':first,
            'fibonacci_product_checks':products,'preserved_ordered_pilots':pilots}

def main():
    print('PID',os.getpid(),flush=True)
    out=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {'scope':'4.5.3-36, C0135, general proof in notes','checkpoints':{}}
    for key,fn in [('explicit_and_families',explicit_and_families),('all_residue_transitions',all_residue_transitions),('ordered_lower_lemmas',ordered_lower_lemmas)]:
        if key in out['checkpoints']:print('SKIP',key,flush=True);continue
        start=time.monotonic();out['checkpoints'][key]=fn();OUT.write_text(json.dumps(out,indent=2)+'\n')
        print('PASS',key,round(time.monotonic()-start,3),flush=True)
    print('ALL MULTI-GCD CHECKPOINTS PASSED',flush=True)

if __name__=='__main__':main()
