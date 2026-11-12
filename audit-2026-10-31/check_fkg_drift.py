"""Exact finite checks for MPR 59, 61, 98-99; general proofs in notes."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from random import Random
import json
from check_ternary_coupling import solve


def four_functions_base():
    cases=0
    for a0,a1,b0,b1,c0,c1,d0,d1 in product(range(4),repeat=8):
        if not (a0*b0<=c0*d0 and a0*b1<=c1*d0 and a1*b0<=c1*d0 and a1*b1<=c1*d1):
            continue
        assert (a0+a1)*(b0+b1)<=(c0+c1)*(d0+d1)
        cases+=1
    return cases


def supported_chains(support,n):
    for s in support:
        for t in support:
            if s&t!=s:
                continue
            reachable={s}
            for k in range(n):
                reachable |= {v|(1<<bit) for v in list(reachable) for bit in range(n)
                               if not v&(1<<bit) and t&(1<<bit) and (v|(1<<bit)) in support}
            if t not in reachable:
                return False
    return True


def fkg(n):
    size=1<<n
    upsets=[]
    for mask in range(1<<size):
        if all(not (mask>>s)&1 or (mask>>(s|(1<<bit)))&1
               for s in range(size) for bit in range(n)):
            upsets.append(mask)
    admissible=0;covariances=0;local_cases=0
    for weights in product(range(3),repeat=size):
        total=sum(weights)
        if not total:
            continue
        global_ok=all(weights[s]*weights[t]<=weights[s|t]*weights[s&t]
                      for s in range(size) for t in range(size))
        support={s for s,w in enumerate(weights) if w}
        closed=all(s|t in support and s&t in support for s in support for t in support)
        if closed and supported_chains(support,n):
            local_ok=all(weights[r|(1<<a)]*weights[r|(1<<b)]<=weights[r]*weights[r|(1<<a)|(1<<b)]
                         for r in range(size) for a in range(n) for b in range(a+1,n)
                         if not r&(1<<a) and not r&(1<<b))
            if local_ok:
                assert global_ok
                local_cases+=1
        if not global_ok:
            continue
        admissible+=1
        masses={mask:sum(w for s,w in enumerate(weights) if (mask>>s)&1)
                for mask in upsets}
        for aa in upsets:
            for bb in upsets:
                # Multiply covariance by the positive normalization total^2.
                assert total*masses[aa&bb]-masses[aa]*masses[bb]>=0
                covariances+=1
    return {'dimension':n,'monotone_boolean_functions':len(upsets),
            'log_supermodular_weight_vectors':admissible,
            'covariances_checked':covariances,
            'local_to_global_cases_checked':local_cases}


def drift():
    rng=Random(20261031)
    cases=0;state_checks=0;strictly_upward_transitions=0
    for N in range(2,15):
        for trial in range(12):
            transition=[[F(0)]*(N+1) for _ in range(N+1)]
            transition[0][0]=F(1)
            means=[F(0)]
            for j in range(1,N+1):
                down=rng.randrange(1,min(j,3)+1)
                upward=rng.randrange(1,4)
                prob=F(rng.randrange(4,9),10)
                # Choose a probability that guarantees positive mean decrease.
                while prob*down-(1-prob)*upward<=0:
                    prob=(1+prob)/2
                transition[j][j-down]+=prob
                upper=min(N,j+upward)
                transition[j][upper]+=1-prob
                strictly_upward_transitions+=upper>j
                means.append(sum((j-k)*weight for k,weight in enumerate(transition[j])))
            g=[F(0)]+[min(means[j:]) for j in range(1,N+1)]
            assert all(0<g[j]<=means[j] for j in range(1,N+1))
            assert all(g[j]<=g[j+1] for j in range(1,N))
            potential=[F(0)]
            for j in range(1,N+1):
                potential.append(potential[-1]+1/g[j])
            matrix=[[F(i==j)-transition[i+1][j+1] for j in range(N)] for i in range(N)]
            expected=solve(matrix,[F(1)]*N)
            for j in range(1,N+1):
                assert expected[j-1]<=potential[j]
                next_potential=sum(w*potential[k] for k,w in enumerate(transition[j]))
                assert next_potential<=potential[j]-1
                state_checks+=1
            cases+=1
    return {'finite_markov_chains':cases,'state_bounds_checked':state_checks,
            'strictly_upward_transitions':strictly_upward_transitions,
            'arithmetic':'Exact rational linear systems.',
            'limitation':'Finite chains corroborate the potential inequality; the infinite-state theorem is proved separately using truncated stopping times.'}


def main():
    report={'four_functions_base_cases':four_functions_base(),
            'fkg':[fkg(n) for n in (1,2,3)],
            'drift':drift(),
            'findings':'No discrepancy in the stated scope.',
            'limitations':'The stronger graded four-functions result mentioned in the bibliographic note is not audited. FKG numerical checks use Boolean increasing functions; the written proof covers arbitrary finite real increasing functions.'}
    (Path(__file__).parent/'results/fkg_drift.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
