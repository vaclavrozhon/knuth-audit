"""Exact audit of 3.2.1.3, including the amended million-triple example."""
from math import comb,gcd
from pathlib import Path
from fractions import Fraction
import json
import random
from verify_multiplier_periods import factors,full_criterion

ROOT=Path(__file__).resolve().parent


def potency(b,m):
    value=b%m;s=1
    while value:
        value=value*b%m;s+=1
        assert s<=m
    return s


def main():
    counts=dict(mix_transitions=0,potencies=0,binomial_values=0,planes=0,inverses=0)
    rng=random.Random(20261101)
    for B in list(range(2,9))+[10,16,64,100,256]:
        m=B**5
        xs=range(m) if B<=10 else [0,1,m-1,m//2]+[rng.randrange(m) for _ in range(1000)]
        assert full_criterion(m,B*B+1,1)
        assert potency(B*B,m)==3
        for x in xs:
            digits=[];t=x
            for _ in range(5):t,r=divmod(t,B);digits.append(r)
            digits=list(reversed(digits))[2:]+[0,0]
            shifted=0
            for d in digits:shifted=shifted*B+d
            A=(shifted+x)%m;A=(A+1)%m
            assert A==((B*B+1)*x+1)%m
            counts['mix_transitions']+=1
    for m in range(2,129):
        for a in range(m):
            if not full_criterion(m,a,1):continue
            b=a-1;s=potency(b,m)
            if b:
                fs=dict(factors(b))
                expected=max((e+fs[p]-1)//fs[p] for p,e in factors(m))
                assert s==expected
            else:assert s==1
            counts['potencies']+=1
            inverse=sum((-b)**j for j in range(s))%m
            assert a*inverse%m==1;counts['inverses']+=1
            cs=[c for c in range(1,m) if gcd(c,m)==1] if m<=40 else [1,m-1]
            for c in cs:
                x=0;xs=[]
                for n in range(2*m+1):
                    direct=c*sum(comb(n,j+1)*b**j for j in range(min(n,s)))%m
                    assert direct==x;counts['binomial_values']+=1
                    xs.append(x);x=(a*x+c)%m
                if s==2:
                    d=c*b%m
                    for x,y,z in zip(xs,xs[1:],xs[2:]):
                        assert x-2*y+z in (d+m,d-m,d,d-2*m)
                        counts['planes']+=1
    assert potency(3141592620,2**35)==18
    assert potency(2**23+2**13+2**2,2**35)==18
    table=json.loads((ROOT/'results/modulus-table.json').read_text())['table_rows']
    possible=[(r['base'],r['exponent'],r['sign']) for r in table
              if max(e for p,e in r['factors'])>=4]
    assert possible==[(2,27,1),(10,9,-1)]

    m=2**35;a=2**17+3;x=1
    hist20=[0]*8000;hist10=[0]*1000;counterexample=None
    all_offsets=set();missing_floor_count=0
    for n in range(1_000_000):
        xs=[x]
        for _ in range(2):xs.append(a*xs[-1]%m)
        x=a*xs[-1]%m
        assert xs[2]==(m//2+6*xs[1]-9*xs[0])%m
        ys=[20*z//m for z in xs]
        # Exact rational formula with floor, evaluated without floating point.
        numerator=10*m+120*xs[1]-180*xs[0]
        assert (numerator//m)%20==ys[2]
        offset=(ys[2]-10-6*ys[1]+9*ys[0])%20
        assert offset not in range(6,11)
        all_offsets.add(offset)
        if offset==11:
            missing_floor_count+=1
            if counterexample is None:
                counterexample=dict(triple_index=n,state_index=3*n,states=xs,bins=ys,offset=offset)
        hist20[(ys[0]*20+ys[1])*20+ys[2]]+=1
        if n<30000:
            ds=[10*z//m for z in xs]
            hist10[(ds[0]*10+ds[1])*10+ds[2]]+=1
    assert counterexample==dict(triple_index=25,state_index=75,
                               states=[12020024059,27570145521,5701049043],bins=[6,16,3],offset=11)
    # Independent recovery of each counterexample state by modular exponentiation.
    assert [pow(a,j,m) for j in (75,76,77)]==counterexample['states']
    eps=[Fraction(20*z,m)-y for z,y in zip(counterexample['states'],counterexample['bins'])]
    value=(10+6*(16+eps[1])-9*(6+eps[0]))%20
    assert value==Fraction(20*5701049043,m) and 3<value<4
    counterexample['right_hand_side_with_actual_fractions']=[value.numerator,value.denominator]
    # Existential obstruction: 6e1-9e2 is strictly between -9 and 6,
    # but equality for (6,16,3) would require it to be 11 modulo 20.
    assert not any(-9<11+20*k<6 for k in range(-10,11))
    assert sum(hist20)==1_000_000 and sum(hist10)==30000
    assert sum(v==0 for v in hist20)>=2000
    result=dict(status='passed',counts=counts,table_moduli_with_potency_at_least_4=possible,
                amended_exercise=dict(triples=1_000_000,bins=20,zero_cells=hist20.count(0),
                                      min_count=min(hist20),max_count=max(hist20),
                                      all_offsets=sorted(all_offsets),missing_floor_cases=missing_floor_count,
                                      histogram=hist20),
                original_exercise=dict(triples=30000,bins=10,zero_cells=hist10.count(0),
                                       min_count=min(hist10),max_count=max(hist10),histogram=hist10),
                counterexample_2016_erratum=counterexample)
    (ROOT/'results/potency.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:({s:t for s,t in v.items() if s!='histogram'} if isinstance(v,dict) else v)
                      for k,v in result.items()},indent=2))


if __name__=='__main__':main()
