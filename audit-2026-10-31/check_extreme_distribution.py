"""Exact atomic laws, lopsided comparisons, and inflation for SAT 344-345."""
from itertools import product,combinations
from pathlib import Path
import json
from check_cographs import scaled_mobius


def graphs(n):
    edges=list(combinations(range(n),2))
    for mask in range(1<<len(edges)):
        adj=[0]*n
        for k,(i,j) in enumerate(edges):
            if mask>>k&1:adj[i]|=1<<j;adj[j]|=1<<i
        yield adj


def submasks(mask):
    s=mask
    while True:
        yield s
        if not s:break
        s=(s-1)&mask


def atomic_law(adj,pnums):
    n=len(adj);D=4**n;pi=[]
    for mask in range(1<<n):
        if any(mask>>i&1 and mask&adj[i] for i in range(n)):pi.append(0);continue
        v=4**(n-mask.bit_count())
        for i in range(n):
            if mask>>i&1:v*=pnums[i]
        pi.append(v)
    atoms=pi.copy()
    for i in range(n):
        for mask in range(1<<n):
            if not mask>>i&1:atoms[mask]-=atoms[mask|1<<i]
    return pi,atoms,D


def dependency_checks(adj,atoms,D,pnums,pden):
    full=(1<<len(adj))-1;checks=0
    for i in range(len(adj)):
        remote=full^(adj[i]|1<<i)
        for J in submasks(remote):
            denominator=sum(v for S,v in enumerate(atoms) if not S&J)
            numerator=sum(v for S,v in enumerate(atoms) if not S&J and S>>i&1)
            assert pden*numerator==pnums[i]*denominator
            checks+=1
    return checks


def main():
    laws=legal=interior=boundaries=atom_formula_checks=dep_checks=inflations=0
    for n in range(1,5):
        full=(1<<n)-1
        for adj in graphs(n):
            for nums in product(range(5),repeat=n):
                pi,q,D=atomic_law(adj,nums);values=scaled_mobius(adj,nums)
                assert sum(q)==D
                legal_here=all(v>=0 for v in q)
                assert legal_here==all(v>=0 for v in values)
                assert (legal_here and q[0]>0)==all(v>0 for v in values)
                laws+=1
                for S in range(1<<n):
                    neighbors=S
                    for i in range(n):
                        if S>>i&1:neighbors|=adj[i]
                    rest=full^neighbors
                    if pi[S]==0:expected=0
                    else:
                        numerator=pi[S]*values[rest]
                        assert numerator%4**rest.bit_count()==0
                        expected=numerator//4**rest.bit_count()
                    assert q[S]==expected;atom_formula_checks+=1
                if legal_here:
                    legal+=1;interior+=q[0]>0
                    dep_checks+=dependency_checks(adj,q,D,nums,4)
                    if not q[0]:
                        boundaries+=1
                        # Independent fair OR flips on every currently false event.
                        new=[v*2**S.bit_count() for S,v in enumerate(q)]
                        for i in range(n):
                            for S in range(1<<n):
                                if S>>i&1:new[S]+=new[S^(1<<i)]
                        assert sum(new)==D*2**n and new[0]==0
                        dep_checks+=dependency_checks(adj,new,D*2**n,[v+4 for v in nums],8)
                        inflations+=1
    # All event systems on a four-point uniform space, through three events.
    event_systems=lopsidependent_systems=comparison_vectors=ratio_checks=0
    for n in range(1,4):
        for events in product(range(16),repeat=n):
            avoid=[15]*(1<<n)
            for S in range(1,1<<n):
                bit=S&-S;i=bit.bit_length()-1
                avoid[S]=avoid[S^bit]&(~events[i]&15)
            nums=[v.bit_count() for v in events]
            for adj in graphs(n):
                event_systems+=1;valid=True
                for i in range(n):
                    remote=((1<<n)-1)^(adj[i]|1<<i)
                    if any(4*(events[i]&avoid[J]).bit_count()>nums[i]*avoid[J].bit_count() for J in submasks(remote)):
                        valid=False;break
                if not valid:continue
                lopsidependent_systems+=1;vals=scaled_mobius(adj,nums)
                if not all(v>0 for v in vals):continue
                comparison_vectors+=1
                beta=[v*4**(n-S.bit_count()) for S,v in enumerate(vals)]
                alpha=[v.bit_count() for v in avoid]
                for J in range(1<<n):
                    assert alpha[J]*4**(n-1)>=beta[J]
                    for i in range(n):
                        if not J>>i&1:
                            K=J|1<<i
                            assert alpha[K]*beta[J]>=alpha[J]*beta[K]
                            ratio_checks+=1
    # Lovasz parameterization, with an exact common probability denominator.
    theta_vectors=theta_ratios=0
    for n in range(1,5):
        den=4**n
        for adj in graphs(n):
            for theta in product(range(4),repeat=n):
                nums=[]
                for i in range(n):
                    v=theta[i]*4**(n-1-adj[i].bit_count())
                    for j in range(n):
                        if adj[i]>>j&1:v*=4-theta[j]
                    nums.append(v)
                vals=scaled_mobius(adj,nums,den)
                assert all(v>0 for v in vals)
                for J in range(1<<n):
                    lower=(den//4)**J.bit_count()
                    for j in range(n):
                        if J>>j&1:lower*=4-theta[j]
                    assert vals[J]>=lower
                    for i in range(n):
                        if not J>>i&1:
                            assert vals[J|1<<i]>=(den//4)*(4-theta[i])*vals[J]
                            theta_ratios+=1
                theta_vectors+=1
    report={'atomic_laws':laws,'closed_neighborhood_atom_formula_checks':atom_formula_checks,
            'legal_laws':legal,'strictly_interior_laws':interior,'boundary_laws':boundaries,
            'exact_dependency_equalities':dep_checks,'independent_OR_inflations':inflations,
            'event_system_graph_pairs':event_systems,'lopsidependent_pairs':lopsidependent_systems,
            'lopsided_comparison_vectors_inside_R':comparison_vectors,'strong_ratio_comparisons':ratio_checks,
            'Lovasz_theta_vectors':theta_vectors,'Lovasz_local_ratio_checks':theta_ratios,
            'scope':'All graphs on <=4 vertices with probabilities in {0,1/4,1/2,3/4,1}; all event systems on a four-point uniform space through three events; all theta vectors in {0,1/4,1/2,3/4} through four vertices. General proofs in EXTREME_DISTRIBUTION_NOTES.md. No additional new finding; F035 is applied.'}
    (Path(__file__).parent/'results/extreme_distribution.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()
