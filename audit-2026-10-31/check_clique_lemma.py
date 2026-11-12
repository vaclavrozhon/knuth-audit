"""Exact checks of the clique Local Lemma, including overlapping covers."""
from fractions import Fraction as Q
from itertools import combinations,product
from math import prod
from pathlib import Path
import random,json
from check_extreme_distribution import graphs,submasks


def mobius(adj,p):
    values=[Q(1)]*(1<<len(adj))
    for mask in range(1,len(values)):
        bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit
        values[mask]=values[rest]-p[i]*values[rest&~adj[i]]
    return values


def graph_from_cover(n,cover):
    adj=[0]*n
    for U in cover:
        for i in range(n):
            if U>>i&1:adj[i]|=U^(1<<i)
    return adj


def check_parameters(n,cover,theta):
    full=(1<<n)-1;adj=graph_from_cover(n,cover)
    sigma=[sum(t.values()) for t in theta]
    assert all(v<1 for v in sigma)
    p=[min(theta[j][i]*prod(1+theta[k][i]-sigma[k] for k in range(len(cover)) if k!=j and cover[k]>>i&1)
           for j in range(len(cover)) if cover[j]>>i&1) for i in range(n)]
    values=mobius(adj,p)
    assert all(x>0 for x in values)
    assert values[full]>=prod(1-v for v in sigma)
    hints=bounds=partitions=0
    for i in range(n):
        E=p[i]*values[full&~(adj[i]|1<<i)]/values[full]
        for j,U in enumerate(cover):
            if not U>>i&1:continue
            assert E<=theta[j][i]/(1-sigma[j]);bounds+=1
            for S in submasks(full^U):
                assert p[i]*values[S&~adj[i]]<=theta[j][i]*values[S];hints+=1
                # Correct inductive partition: assign a vertex to the LAST
                # clique containing it, in the chosen order.
                other=[V for k,V in enumerate(cover) if k!=j and V>>i&1]
                union=0
                for V in other:union|=V
                X=S&union;Y=S^X;parts=[];later=0
                for V in reversed(other):
                    parts.append(S&V&~later);later|=V
                parts.reverse();seen=Y
                for V,part in zip(other,parts):
                    assert not seen&V and not seen&part
                    if part:assert seen.bit_count()<S.bit_count()
                    seen|=part;partitions+=1
                assert seen==S
    # Last-occurrence blocks also justify the final avoidance product.
    later=0;parts=[]
    for U in reversed(cover):parts.append(U&~later);later|=U
    seen=0
    for U,part in zip(cover,reversed(parts)):
        assert not seen&U and not seen&part
        seen|=part;partitions+=1
    assert seen==full
    return hints,bounds,partitions


def main():
    families=vectors=hints=bounds=partitions=0
    rng=random.Random(356)
    for n in range(1,5):
        full=(1<<n)-1
        for t in range(1,4 if n<=3 else 5):
            for cover in combinations(range(1,1<<n),t):
                covered=0
                for U in cover:covered|=U
                if covered!=full:continue
                families+=1
                incidences=[(j,i) for j,U in enumerate(cover) for i in range(n) if U>>i&1]
                if n<=3:
                    assignments=product([Q(0),Q(1,4)],repeat=len(incidences))
                else:
                    assignments=[]
                    # Each clique sum is <=3/4, including zero coordinates.
                    for _ in range(8):
                        assignments.append([Q(rng.randrange(4),4*cover[j].bit_count()) for j,i in incidences])
                for ts in assignments:
                    theta=[{} for U in cover]
                    for (j,i),v in zip(incidences,ts):theta[j][i]=v
                    h,b,z=check_parameters(n,cover,theta)
                    vectors+=1;hints+=h;bounds+=b;partitions+=z
    # Specialization 356(c), independently using all induced polynomials.
    specialized=0
    for n in range(1,6):
        for adj in graphs(n):
            if n<=4:theta_grid=product([Q(0),Q(1,8),Q(3,8)],repeat=n)
            else:theta_grid=([Q(rng.choice([0,1,3]),8) for _ in range(n)] for _ in range(16))
            for ts in theta_grid:
                p=[]
                for i in range(n):
                    factors=[1-ts[j] for j in range(n) if adj[i]>>j&1]
                    p.append(ts[i]*prod(factors)/max(factors,default=Q(1)))
                assert all(v>0 for v in mobius(adj,p));specialized+=1
    # Concrete failure of the printed conditioning step in 356(a).
    # G=K3, A0 empty, A1 and A2 disjoint with probability 2/5 each.
    cover=[1,3,7];theta=[{0:Q(0)},{0:Q(0),1:Q(2,3)},{0:Q(0),1:Q(2,5),2:Q(2,5)}]
    check_parameters(3,cover,theta)
    p=[Q(0),Q(2,5),Q(2,5)]
    assert p[2]/(1-p[1])==Q(2,3)>theta[2][2]
    # A cover can cover all edges and still omit an isolated vertex.
    adj=graph_from_cover(2,[1]);assert adj==[0,0]
    assert mobius(adj,[Q(0),Q(1)])[-1]==0
    # F039: the final '>' in 355 is reversed; strictness also needs care.
    assert Q(1,4)/(1-Q(1,4)-Q(1,4))==Q(1,2)<1
    assert 1-Q(1,2)*(1+1)-0==0  # Nonisolated vertex, zero-weight neighbor.
    result=dict(clique_cover_families=families,parameter_vectors=vectors,
                conditional_hint_checks=hints,resampling_bounds=bounds,
                partition_checks=partitions,specialized_theta_vectors=specialized,
                overlap_counterexample={'cover':cover,'p':['0','2/5','2/5'],
                   'printed_conditional':'2/3','claimed_upper_bound':'2/5'},
                uncovered_isolate={'cover':[1],'p':['0','1'],'M':'0'},
                slack_counterexample={'p':['1/4','1/4'],'delta':'1','E':'1/2'})
    Path('results/clique_lemma.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
