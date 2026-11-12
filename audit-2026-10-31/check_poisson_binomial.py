"""MPR 28-29: exact extremal/convex-order checks and Samuels bounds."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
from random import Random
import json
import sympy as sp


@lru_cache(None)
def distribution(ps):
    out=[F(1)]
    for p in ps:
        nxt=[F(0)]*(len(out)+1)
        for k,x in enumerate(out):
            nxt[k]+=(1-p)*x
            nxt[k+1]+=p*x
        out=nxt
    return tuple(out)


def binomial(n,p):
    return tuple(F(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n+1))


@lru_cache(None)
def extremal_distributions(n,mean):
    out=set()
    for zeros in range(n+1):
        for ones in range(n-zeros+1):
            interior=n-zeros-ones
            if interior:
                a=(mean-ones)/interior
                if not 0<=a<=1:
                    continue
                out.add(distribution((F(0),)*zeros+(F(1),)*ones+(a,)*interior))
            elif mean==ones:
                out.add(tuple(F(k==ones) for k in range(n+1)))
    return tuple(out)


def main():
    rng=Random(20261031)
    vectors=hinges=tail_bounds=extremal_checks=0
    biases=(F(0),F(1,4),F(1,2),F(3,4),F(1))
    for n in range(1,9):
        functions=[tuple(rng.randrange(-3,4) for _ in range(n+1)) for __ in range(5)]
        maxima={}
        for ps in combinations_with_replacement(biases,n):
            actual=distribution(ps)
            mean=sum(ps)
            equal=binomial(n,mean/n)
            for pivot in range(1,n):
                lhs=sum(max(0,k-pivot)*w for k,w in enumerate(actual))
                rhs=sum(max(0,k-pivot)*w for k,w in enumerate(equal))
                assert lhs<=rhs
                hinges+=1
            for m in range(n):
                if mean>=m+1:
                    assert sum(actual[:m+1])<=sum(equal[:m+1])
                    tail_bounds+=1
            for index,g in enumerate(functions):
                key=mean,index
                if key not in maxima:
                    maxima[key]=max(sum(gg*w for gg,w in zip(g,d))
                                    for d in extremal_distributions(n,mean))
                assert sum(gg*w for gg,w in zip(g,actual))<=maxima[key]
                extremal_checks+=1
            vectors+=1
    samuels=0
    for n in range(1,26):
        for m in range(n+1):
            maxp=min(F(1),F(m+1,n))
            for k in range(17):
                p=maxp*k/16
                actual=sum(binomial(n,p)[:m+1])
                rhs=((1-p)*(m+1)/((1-p)*m+1))**(n-m)
                assert actual>=rhs
                samuels+=1
    symbol=sp.symbols('p')
    derivatives=0
    for n in range(3,10):
        for m in range(1,n-1):
            B=sum(sp.binomial(n,k)*symbol**k*(1-symbol)**(n-k) for k in range(m+1))
            R=(((1-symbol)*(m+1))/((1-symbol)*m+1))**(n-m)
            A=sp.Rational((m+1)**(n-m),comb(n,m))
            ff=symbol**m*((1-symbol)*m+1)**(n-m+1)
            claimed=(n-m)*comb(n,m)*(1-symbol)**(n-m-1)*(A-ff)/((1-symbol)*m+1)**(n-m+1)
            assert sp.factor(sp.diff(B-R,symbol)-claimed)==0
            derivatives+=1
    # Exercise 28(b): the negative quantity -min(a,1-b) is the step epsilon,
    # not the induced product increment delta.
    a,b=F(1,4),F(3,4)
    epsilon=-min(a,1-b)
    product_change=(a+epsilon)*(b-epsilon)-a*b
    assert epsilon==F(-1,4) and product_change==F(-3,16)
    assert a*b+epsilon==F(-1,16) # impossible as a new joint-success probability
    report={'exercises':'MPR 28-29','probability_vectors':vectors,
            'scope':'All nondecreasing probability vectors of lengths 1..8 on {0,1/4,1/2,3/4,1}; sums are invariant under permutation.',
            'convex_hinge_checks':hinges,'lower_tail_comparisons':tail_bounds,
            'nonconvex_extremal_comparisons':extremal_checks,
            'samuels_exact_inequalities':samuels,'symbolic_derivative_identities':derivatives,
            'F016_step_symbol':{'page':374,'answer':'MPR 28(b)',
                'printed':'using delta = -min(p_(n-1),1-p_n)',
                'corrected':'using epsilon = -min(p_(n-1),1-p_n)',
                'example':'a=1/4,b=3/4: epsilon=-1/4, actual product increment delta=-3/16. Using printed delta would make A and C equal -1/16.',
                'consequence':'The smoothing argument and theorem are correct after the symbol correction.'},
            'limitations':'Finite checks supplement the smoothing proof and Samuels derivative proof; they are not a search over all real probability vectors.'}
    (Path(__file__).parent/'results/poisson_binomial.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
