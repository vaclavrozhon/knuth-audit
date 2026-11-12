"""Counterexamples to missing hypotheses in TAOCP 3.2.2-26."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent


def cycle(coeff,seed,m):
    state=tuple(seed);seen=set();out=[]
    while state not in seen:
        seen.add(state);out.append(state[0])
        state=state[1:]+(sum(a*x for a,x in zip(coeff,state[::-1]))%m,)
    assert state==tuple(seed)
    return out


def main():
    zero_count_rows=[]
    for alpha in range(1,11):
        m=3**alpha
        word=cycle((0,0,4),(0,0,1),m)
        assert len(word)==m and word.count(0)==2*3**(alpha-1)
        for n,x in enumerate(word):
            expected=0 if n%3!=2 else pow(4,n//3,m)
            assert x==expected
        assert pow(4,3**(alpha-1),m)==1
        if alpha>1:assert pow(4,3**(alpha-2),m)!=1
        row=dict(alpha=alpha,period=len(word),zeros=word.count(0))
        if alpha%2==0:row['N_over_claimed_power']=word.count(0)//3**(alpha//2)
        zero_count_rows.append(row)

    uniform_seed_cases=0
    for e in range(1,8):
        m=2**e
        for seed in product(range(m),repeat=2):
            word=cycle((1,-1),seed,m)
            assert 6%len(word)==0 and word.count(0)<=6
            uniform_seed_cases+=1
    discrepancy_rows=[]
    for e in range(1,21):
        m=2**e;word=cycle((1,-1),(1,1),m)
        assert len(word)==(3 if e==1 else 6)
        if e>=2:
            count=sum(2*x<m and 2*word[(n+1)%len(word)]<m
                      for n,x in enumerate(word))
            discrepancy=abs(Fraction(count,len(word))-Fraction(1,4))
            assert count==3 and discrepancy==Fraction(1,4)
            discrepancy_rows.append(dict(alpha=e,period=len(word),box_count=count,
                                         box_volume='1/4',discrepancy_lower_bound='1/4'))
    result=dict(status='passed',missing_primitivity=zero_count_rows,
                bounded_period_uniform_seed_cases=uniform_seed_cases,
                missing_growth=discrepancy_rows,
                scope='Exact counterexamples; not a disproof of the primitive, growing-period formulation.')
    (ROOT/'results/reiser-hypotheses.json').write_text(json.dumps(result,indent=2)+'\n')
    print('passed;',sum(x['period'] for x in zero_count_rows),'ternary states;',
          uniform_seed_cases,'binary initial pairs;',len(discrepancy_rows),'discrepancy boxes')


if __name__=='__main__':main()
