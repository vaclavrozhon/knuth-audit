"""Exact finite-distribution and sequence checks for SAT 306-308."""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict
from pathlib import Path
import json
import random


def stats(p,n):
    q=sum(p[:n],Q(0))
    e=sum((i+1)*v for i,v in enumerate(p[:n]))
    cost=e+n*(1-q)
    return q,e,cost


def periodic_mean(p,cutoffs):
    survival=Q(1);cost=Q(0)
    for n in cutoffs:
        q,e,c=stats(p,n)
        cost+=survival*c
        survival*=1-q
    return cost/(1-survival) if survival<1 else None


def markov_mean(p,cutoffs):
    """Independent one-step hazard chain, solved by rational elimination."""
    initial=(0,0);states=[initial];edges={};index={initial:0}
    for trial,elapsed in states:
        oldq=stats(p,elapsed)[0]
        newq=stats(p,elapsed+1)[0]
        assert oldq<1
        failure=(1-newq)/(1-oldq)
        nxt=(trial,elapsed+1) if elapsed+1<cutoffs[trial] else ((trial+1)%len(cutoffs),0)
        edges[trial,elapsed]=(nxt,failure)
        if failure and nxt not in index:
            index[nxt]=len(states);states.append(nxt)
    matrix=[]
    for j,state in enumerate(states):
        row=[Q(0)]*(len(states)+1);row[j]=Q(1);row[-1]=Q(1)
        nxt,prob=edges[state]
        if prob:row[index[nxt]]-=prob
        matrix.append(row)
    for j in range(len(states)):
        pivot=next(i for i in range(j,len(states)) if matrix[i][j])
        matrix[j],matrix[pivot]=matrix[pivot],matrix[j]
        scale=matrix[j][j];matrix[j]=[v/scale for v in matrix[j]]
        for i in range(len(states)):
            if i==j or not matrix[i][j]:continue
            scale=matrix[i][j]
            matrix[i]=[a-scale*b for a,b in zip(matrix[i],matrix[j])]
    return matrix[0][-1],len(states)


def main():
    distribution_count=0;constant_cutoffs=0
    distributions=[]
    for weights in product(range(4),repeat=5):
        if not sum(weights[:4]):continue
        total=sum(weights);p=tuple(Q(w,total) for w in weights[:4])
        distributions.append(p)
        candidates=[(stats(p,n)[2]/stats(p,n)[0],Q(n)/stats(p,n)[0])
                    for n in range(1,5) if stats(p,n)[0]]
        ell=min(x for x,_ in candidates);L=min(x for _,x in candidates)
        assert ell<=L<=2*ell-1
        for n in range(1,7):
            q,e,c=stats(p,n)
            assert c==n-sum(stats(p,j)[0] for j in range(1,n))
            if q:constant_cutoffs+=1
        distribution_count+=1
    rng=random.Random(306307);periodic_cases=0;markov_states=0
    while periodic_cases<120:
        p=rng.choice(distributions);cutoffs=tuple(rng.randrange(1,7) for _ in range(rng.randrange(1,5)))
        formula=periodic_mean(p,cutoffs)
        if formula is None:continue
        direct,size=markov_mean(p,cutoffs)
        assert formula==direct
        ell=min(stats(p,n)[2]/stats(p,n)[0] for n in range(1,5) if stats(p,n)[0])
        assert direct>=ell
        periodic_cases+=1;markov_states+=size
    region_cases=0
    for w in product(range(11),repeat=3):
        if not sum(w) or not w[0]:continue
        p=tuple(Q(x,sum(w)) for x in w)
        costs=[stats(p,n)[2]/stats(p,n)[0] for n in (1,2,3)]
        x,y,z=p
        region=Q(1,2)<x<1 and 0<=y<(2*x-1)*(1-x)/x
        assert (costs[0]<costs[2]<costs[1])==region
        region_cases+=1
    harmonic=[Q(0)]
    for k in range(1,140):harmonic.append(harmonic[-1]+Q(1,k))
    heavy_tail=[]
    for n in range(101):
        values=[Q(k+1,k)*(n+harmonic[k]) for k in range(1,n+30)]
        k=1+min(range(len(values)),key=values.__getitem__)
        assert n<=k+1-harmonic[k+1]
        if k>1:assert n>k-harmonic[k]
        heavy_tail.append((n,n+k,str(values[k-1])))
    assert heavy_tail[10][1]==23
    # F027: wrong algorithm, exact finite counterexample, p1=p_infinity=1/2.
    alpha=Q(1);wrong=Q(0);correct=Q(0);iterations=[]
    for j in range(1,5):
        oldalpha=alpha;alpha/=2
        wrong+=Q(1,2)+alpha
        correct+=oldalpha*Q(1,2)+alpha
        iterations.append({'j':j,'survival':str(alpha),'printed_sum':str(wrong),'correct_truncated_sum':str(correct)})
    assert wrong==Q(47,16)>2 and correct==Q(15,8)<2
    # F029: shifted geometric distribution from 306(j), with mean 3.
    shifted=[]
    for N in range(2,30):
        q=1-Q(1,2**(N-1));truncated=3-Q(1,2**(N-2));ell=truncated/q
        assert ell>3 and truncated<3<4
        shifted.append((N,str(ell),str(truncated)))
    assert shifted[0][1]=='4'
    # Independent iterative generator (131) and position/sum identities.
    u=v=1;prefix=[0];positions=defaultdict(list)
    for n in range(1,300001):
        exponent=v.bit_length()-1;k=len(positions[exponent])
        assert n==2**(exponent+1)*(k+1)-1-k.bit_count()
        positions[exponent].append(n);prefix.append(prefix[-1]+v)
        u,v=(u+1,1) if u&-u==v else (u,2*v)
    sigma_cases=0;gap_cases=0
    for a in range(7):
        for b in range(7):
            s=a+b
            def sigma(k):return prefix[positions[a][2**b*k-1]]
            assert sigma(1)==(s-1)*2**s+2**(a+1)
            for k in range(1,33):
                U=2**s*k
                direct=sum(2**c*((U-1)//2**c) for c in range(U.bit_length()))+2**(a+1)-1
                assert sigma(k)==direct
                sigma_cases+=1
                if k<32:
                    gap=sigma(k+1)-sigma(k)
                    rho=(k&-k).bit_length()-1
                    assert gap==2**s*(s-1+2**(rho+1))
                    assert gap<=(s+2*k-1)*2**s
                    gap_cases+=1
    report={'finite_distributions':distribution_count,'constant_cutoff_checks':constant_cutoffs,
            'L_bound_checks':distribution_count,'periodic_strategies':periodic_cases,
            'independent_hazard_chain_states':markov_states,'three_point_region_checks':region_cases,
            'heavy_tail_optima_checked':101,'heavy_tail_n10':heavy_tail[10],
            'Luby_terms_and_position_checks':300000,'Sigma_checks':sigma_cases,'gap_checks':gap_cases,
            'F027_iterations':iterations,'F027_true_mean':2,
            'F028':'P_j=product_(i<j)(1-q_Ni) is Pr(X>T_(j-1)), not Pr(X>T_j). At j=1 in the F027 example: 1 versus 1/2.',
            'F029':'Answer 306(h) starts with N*=infinity but then asserts a truncated mean exceeds l(n). In the 306(j) distribution, N*=infinity and l(2)=4, whereas every truncated mean is <3. The proof should instead begin with E_infinity=infinity.',
            'F029_shifted_geometric_first_five':shifted[:5],
            'scope':'Exact rational distributions and finite sequence identities. General proofs, infinite tails, and universal constants are in RESTART_NOTES.md.'}
    (Path(__file__).parent/'results/restarts.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
