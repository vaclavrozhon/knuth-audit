"""Exact checks for the variable-model four-cycle, SAT exercise 322."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json


def constraints(v):
    a,b,ap,bp,c,d,cp,dp,mu,nu=v
    means=(mu*a+(1-mu)*ap,mu*b+(1-mu)*bp,nu*c+(1-nu)*cp,nu*d+(1-nu)*dp)
    covered=all(ai+dj>=1 or bi+cj>=1 for ai,bi in [(a,b),(ap,bp)] for cj,dj in [(c,d),(cp,dp)])
    return means,covered


def orbit(v,N):
    out={v};queue=[v]
    for v in queue:
        a,b,ap,bp,c,d,cp,dp,mu,nu=v
        images=[(b,a,bp,ap,d,c,dp,cp,mu,nu),
                (ap,bp,a,b,c,d,cp,dp,N-mu,nu),
                (a,b,ap,bp,cp,dp,c,d,mu,N-nu),
                (d,c,dp,cp,b,a,bp,ap,nu,mu)]
        for w in images:
            if w not in out:out.add(w);queue.append(w)
    return out


def main():
    N=6;states={}
    for r in range(1,N):
        pairs=[(a,ap) for a in range(N+1) for ap in range(N+1) if 3*(r*a+(N-r)*ap)<=N*N]
        states[r]=[(a,b,ap,bp) for a,ap in pairs for b,bp in pairs]
    expected=set()
    for r in range(1,N):expected|=orbit((4,0,0,4,2,2,2,2,3,r),N)
    expected|=orbit((6,0,0,3,0,6,3,0,2,2),N)
    solutions=set();candidates=0
    for mu,nu in product(range(1,N),repeat=2):
        for a,b,ap,bp in states[mu]:
            for c,d,cp,dp in states[nu]:
                candidates+=1
                if not (a+d>=N or b+c>=N):continue
                if not (a+dp>=N or b+cp>=N):continue
                if not (ap+d>=N or bp+c>=N):continue
                if not (ap+dp>=N or bp+cp>=N):continue
                solutions.add((a,b,ap,bp,c,d,cp,dp,mu,nu))
    assert solutions==expected
    printed=tuple(map(Q,[1,0,0,Q(1,2),0,1,Q(1,2),0,Q(1,3),Q(2,3)]))
    corrected=printed[:-1]+(Q(1,3),)
    means,covered=constraints(printed);goodmeans,goodcovered=constraints(corrected)
    assert means==(Q(1,3),Q(1,3),Q(1,6),Q(2,3)) and covered
    assert goodmeans==(Q(1,3),)*4 and goodcovered
    assignments=list(product(range(3),range(2),range(3),[0]))
    physical=[0]*16
    for w,x,y,z in assignments:
        events=((w,x) in [(1,0),(2,0)],(x,y) in [(1,1),(1,2)],(y,z)==(0,0),(z,w)==(0,0))
        physical[sum(int(v)<<i for i,v in enumerate(events))]+=1
    assert physical[0]==0
    for i in range(4):assert sum(count for s,count in enumerate(physical) if s>>i&1)==6
    # Every event set on a pair of fair bits, all 16^4 systems. Compare the
    # actual avoidance probability with the conditional Frechet lower bound.
    projections=[]
    for w,x,y,z in product(range(2),repeat=4):
        projections.append((2*w+x,2*x+y,2*y+z,2*z+w))
    systems=0;strict=0;small=0
    conditional_counts={}
    for A,B,C,D in product(range(16),repeat=4):
        good=sum(not any(mask>>j&1 for mask,j in zip((A,B,C,D),idx)) for idx in projections)
        lower=0
        for x,z in product(range(2),repeat=2):
            a=sum(A>>(2*w+x)&1 for w in range(2));b=sum(B>>(2*x+y)&1 for y in range(2))
            c=sum(C>>(2*y+z)&1 for y in range(2));d=sum(D>>(2*z+w)&1 for w in range(2))
            lower+=max(0,2-a-d)*max(0,2-b-c)
        assert good>=lower
        systems+=1;strict+=good>lower
        if max(A.bit_count(),B.bit_count(),C.bit_count(),D.bit_count())<=1:
            assert good>0;small+=1
    report={'coordinate_and_weight_grid_denominator':N,'constraint_systems_considered':candidates,
            'solutions':len(solutions),'solutions_all_match_two_corrected_symmetry_families':True,
            'F031_printed_means':list(map(str,means)),
            'F031_corrected_means':list(map(str,goodmeans)),
            'F031_correction':'nu=1/3, not 2/3, with all other displayed values unchanged.',
            'F032_diagram':'The right diagram has C varying along W and D along Y, contrary to C(Y,Z), D(Z,W). Swap W and Y on that diagram.',
            'physical_first_solution_assignments':len(assignments),
            'physical_first_solution_marginals':['1/3']*4,
            'physical_first_solution_avoidance_probability':0,
            'fair_bit_event_systems':systems,'strict_Frechet_bounds':strict,
            'systems_with_all_p_at_most_one_third':small,
            'scope':'Finite exact checks; full classification by the 16 coverage patterns is proved in VARIABLE_CYCLE_NOTES.md. The equality in answer (a) is read after extremal rearrangement, not as an identity for an arbitrary fixed event system.'}
    (Path(__file__).parent/'results/variable_cycle.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
