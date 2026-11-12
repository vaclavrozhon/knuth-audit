#!/usr/bin/env python3
"""Exact finite audits of TAOCP4.6.3-30/31/32; general proofs are separate."""
import argparse
from datetime import datetime,timezone
from fractions import Fraction
import json
from pathlib import Path
import time

BASE=Path(__file__).resolve().parent
RESULT=BASE/'results/powers-cost.json'


def naf(n):
    digits=[]
    while n:
        digit=(2-n%4) if n&1 else 0
        digits.append(digit)
        n=(n-digit)//2
    return digits


def signed_block():
    # Every signed chain can be replaced by absolute values, with operations
    # a+b and |a-b|, deleting zero and duplicates. No increasing-order pruning.
    states={frozenset({1}):(1,)}
    minimum={1:0};witness={1:[1]};sizes=[1]
    for depth in range(1,7):
        next_states={}
        for state,path in states.items():
            values=sorted(state)
            new_values=set()
            for i,a in enumerate(values):
                for b in values[:i+1]:
                    new_values.add(a+b);new_values.add(abs(a-b))
            for value in new_values-state-{0}:
                target=state|{value}
                if target not in next_states:next_states[target]=path+(value,)
                if value not in minimum:
                    minimum[value]=depth;witness[value]=list(path+(value,))
        states=next_states;sizes.append(len(states))
    old={r['n']:r['length'] for r in map(json.loads,(BASE/'results/powers-optimal.jsonl').read_text().splitlines())}
    for n in range(1,31):assert minimum.get(n,7)==old[n],(n,minimum.get(n),old[n])
    assert old[31]==7 and minimum[31]==6
    # Stronger input for the multiplication-only claim: ±1 and zero are free.
    # Enumerate integer exponent sets; a product creates the sum of two inputs.
    free=frozenset({-1,0,1}); mul_states={free}; mul_sizes=[1]
    reachable=set(free)
    for _ in range(3):
        new=set()
        for state in mul_states:
            for a in state:
                for b in state:
                    if a+b not in state:new.add(state|{a+b})
        mul_states=new;mul_sizes.append(len(new))
        for state in new:reachable.update(state)
    assert 7 not in reachable
    assert sum(d*(1<<i) for i,d in enumerate(naf(7)))==7
    assert len([d for d in naf(7) if d])==2
    assert (7).bit_length()-1+2-1==3
    count=0;extra_top=0
    for n in range(1,65536):
        digits=naf(n);weight=sum(d!=0 for d in digits);top=len(digits)-1
        assert sum(d*(1<<i) for i,d in enumerate(digits))==n
        assert digits[-1]==1 and all(not (a and b) for a,b in zip(digits,digits[1:]))
        assert top in [n.bit_length()-1,n.bit_length()]
        exponent=1;operations=0
        for digit in reversed(digits[:-1]):
            exponent*=2;operations+=1
            if digit:exponent+=digit;operations+=1
        assert exponent==n and operations==top+weight-1
        assert operations<=n.bit_length()-1+weight
        extra_top+=top==n.bit_length()
        count+=1
    return dict(signed_state_counts_by_depth=sizes,first_improvement=31,
                addition_length_31=7,addition_subtraction_length_31=6,
                witness_31=witness[31],positive_targets_below_31_checked=30,
                multiplication_states_with_free_signed_inputs=mul_sizes,
                seven_unreachable_in_three_multiplications=True,
                naf_cases=count,naf_cases_with_extra_leading_bit=extra_top,
                false_printed_count_for_seven=3,correct_count_for_seven=4)


def binary_cost(n):
    if n<=1:return 0
    m=n//2
    return binary_cost(m)+m*m+(2*m if n&1 else 0)


def cost_models_block():
    limit=24
    best_product=[None]*(limit+1);best_sum=[None]*(limit+1)
    features=[{} for _ in range(limit+1)]
    nodes=0
    mask_limit=(1<<(limit+1))-1
    def walk(chain,mask,sums,product_cost,sum_cost,q,f):
        nonlocal nodes
        nodes+=1;n=chain[-1]
        if best_product[n] is None or product_cost<best_product[n]:best_product[n]=product_cost
        if best_sum[n] is None or sum_cost<best_sum[n]:best_sum[n]=sum_cost
        features[n].setdefault((q,f),chain)
        candidates=sums&mask_limit&~((1<<(n+1))-1)
        while candidates:
            bit=candidates&-candidates;candidates-=bit;value=bit.bit_length()-1
            for a in chain:
                if a>value//2:raise AssertionError('missing summand')
                if mask&(1<<(value-a)):
                    cheapest=a*(value-a);break
            simple=value==n+1
            walk(chain+[value],mask|bit,sums|(mask<<value)|(1<<(2*value)),
                 product_cost+cheapest,sum_cost+value,q+simple,f+(not simple))
    walk([1],2,4,0,0,0,0)
    expected=[binary_cost(n) for n in range(1,limit+1)]
    assert best_product[1:]==expected
    frontiers={}
    for n in range(1,limit+1):
        keys=list(features[n])
        pareto=[p for p in keys if not any(t!=p and t[0]<=p[0] and t[1]<=p[1] for t in keys)]
        frontiers[str(n)]=[dict(simple=q,other=f,chain=features[n][q,f]) for q,f in sorted(pareto)]
        assert best_sum[n]>=2*(n-1)
        if n&(n-1)==0:assert best_sum[n]==2*(n-1)
        if n&1:assert 2*best_sum[n]>=5*(n-1)
    fifteen={(r['simple'],r['other']) for r in frontiers['15']}
    assert fifteen=={(14,0),(7,1),(4,2),(2,3)},fifteen
    tests=[(Fraction(1,10),(14,0)),(Fraction(1,5),(7,1)),
           (Fraction(2,5),(4,2)),(Fraction(3,4),(2,3))]
    for epsilon,desired in tests:
        values={p:epsilon*p[0]+p[1] for p in fifteen}
        assert values[desired]==min(values.values())
    return dict(all_ascending_chain_states=nodes,maximum_target=limit,
                minimum_multiplicative_cost=best_product[1:],
                minimum_additive_cost=best_sum[1:],weighted_pareto_frontiers=frontiers,
                n15_breakpoints=['1/7','1/3','1/2'],
                scope='all increasing chains with values<=24, every length; cheapest valid pair for product cost')


def inequalities_block():
    g=[binary_cost(n) for n in range(2049)]
    differences=0
    for n in range(2,len(g)):
        odd=n;v=0
        while odd%2==0:odd//=2;v+=1
        assert g[n]-g[n-1]==v+odd-1
        differences+=1
    lemma=0
    for x in range(1,1024):
        for n in range(x+2,2*x+2):
            assert g[n]-g[x]>=(n-x)**2+2*x-n
            lemma+=1
    # Exact polynomial residuals in the four parity cases of the general lemma.
    parity=0
    for X in range(1,65):
        for D in range(2,X+2):
            N=X+D
            for e in [0,1]:
                for h in [0,1]:
                    x=2*X+e;n=2*N+h
                    if not x+2<=n<=2*x+1:continue
                    lower=D*D+2*X-N+N*N-X*X+2*h*N-2*e*X
                    residual=lower-((n-x)**2+2*x-n)
                    factors={(0,0):(2*D-1)*(X-D),
                             (0,1):(2*D+1)*(X-D),
                             (1,0):(2*D-3)*(X-D+1),
                             (1,1):(2*D-1)*(X-D+1)}
                    assert residual==factors[e,h]>=0
                    parity+=1
    return dict(binary_cost_difference_checks=differences,interval_inequalities=lemma,
                parity_residual_checks=parity,scope='finite verification of the separately proved general induction')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('block',choices=['signed','cost_models','inequalities']);args=parser.parse_args()
    data=json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert args.block not in data['blocks'],'Do not repeat passed blocks'
    start=time.perf_counter();result=globals()[args.block+'_block']()
    data['blocks'][args.block]=dict(status='passed',seconds=time.perf_counter()-start,result=result)
    data['updated_at_utc']=datetime.now(timezone.utc).isoformat();RESULT.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'block':args.block,**data['blocks'][args.block]}),flush=True)
