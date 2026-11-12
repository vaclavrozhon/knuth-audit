"""TAOCP 3.3.2-28/29: exact word counts and independent partition series."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import factorial, comb
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parent
DEST=ROOT/'results/birthday-spacings.json'


def stirling(n,k):
    a=[1]+[0]*k
    for i in range(n):a=[0]+[a[j-1]+j*a[j] for j in range(1,k+1)]
    return a[k]


def partition_counts(n,cap):
    a=[1]+[0]*cap
    for k in range(1,n+1):
        for m in range(k,cap+1):a[m]+=a[m-k]
    return a


def numerator(n,r):
    """Printed b_nr(z)/(n!(n-1)!) = numerator(z)/prod(1-z^j)."""
    a=Counter()
    if r==0:a[n*(n+1)//2]=Q(1)
    elif r==1:
        base=n*(n-1)//2
        for k in range(1,n):a[base+k]+=Q(1,2);a[base+n]-=Q(1,2)
    elif r==2:
        base=(n-1)*(n-2)//2
        for k in range(1,n):
            for j in range(1,k):
                for e,c in ((j+k,1),(j+n-1,-1),(n+k,-1),(2*n-1,1)):
                    a[base+e]+=Q(c,4)
            for e,c in ((2*k,1),(k+n-1,-1),(n+k,-1),(2*n-1,1)):
                a[base+e]+=Q(c,6)
    else:raise ValueError(r)
    return {k:v for k,v in a.items() if v}


def generic_numerators(n):
    answer=[Counter() for _ in range(n)]
    for bits in product((0,1),repeat=n-1):
        base=n*(n+1)//2-sum((n-k)*b for k,b in enumerate(bits,1))
        a={base:Q(1)};c=1;den=1
        for k,b in enumerate(bits,1):
            c=1+b*c;den*=c
            if b:
                updated=Counter(a)
                for e,v in a.items():updated[e+n-k]-=v
                a={e:v for e,v in updated.items() if v}
        for e,v in a.items():answer[sum(bits)][e]+=v/den
    return [{e:v for e,v in a.items() if v} for a in answer]


def word_enumeration():
    models={};total=0
    for n in range(1,7):
        for m in range(1,8):
            hist=Counter()
            for word in product(range(m),repeat=n):
                y=sorted(word);gaps=[y[j+1]-y[j] for j in range(n-1)]+[y[0]+m-y[-1]]
                hist[n-len(set(gaps)),gaps.count(0)]+=1
            total+=m**n
            models[n,m]=hist
            p=partition_counts(n,m)
            N=n*(n+1)//2
            q=p[m-N] if m>=N else 0
            assert hist[0,0]==m*factorial(n)*factorial(n-1)*q
            for (r,s),v in hist.items():
                if s:
                    assert v==stirling(n,n-s)*models[n-s,m][r+1-s,0]
            if n>=2:
                p1=partition_counts(n-1,m);N1=n*(n-1)//2
                q1=p1[m-N1] if m>=N1 else 0
                expected=m*factorial(n)*factorial(n-1)*(Q(q)+Q(q1,2))
                assert hist[0,0]+hist[0,1]==expected
    assert sum(v for (r,s),v in models[2,3].items() if r==0)==9
    # Printed minus gives 3/9 instead of the actual 9/9.
    return dict(models=len(models),words=total,
                counterexample=dict(n=2,m=3,no_equal_spacings=9,all_words=9,
                                    printed_probability='1/3',correct_probability='1'),
                positive_counts={f'{n},{m},{r}':v for (n,m),h in models.items()
                                 for (r,s),v in h.items() if s==0})


def sorted_partitions(total,n,minimum=1):
    if n==0:
        if total==0:yield ()
        return
    for first in range(minimum,total//n+1):
        for rest in sorted_partitions(total-first,n-1,first):yield (first,)+rest


def generating_functions(words):
    cap=48;checks=0;partitions=0;generic_cases=0
    for n in range(1,10):
        dp=partition_counts(n,cap)
        generic=generic_numerators(n)
        for r in range(min(3,n)):
            assert generic[r]==numerator(n,r);generic_cases+=1
        # Direct sorted partitions, each weighted by n!/product multiplicity!.
        for m in range(1,cap+1):
            counts=Counter()
            for parts in sorted_partitions(m,n):
                multiplicities=Counter(parts);weight=factorial(n)
                for v in multiplicities.values():weight//=factorial(v)
                counts[n-len(multiplicities)]+=weight;partitions+=1
            for r in range(n):
                value=sum(c*dp[m-e] for e,c in generic[r].items() if e<=m)
                assert factorial(n)*value==counts[r]
                key=f'{n},{m},{r}'
                if n<=6 and m<=7:
                    assert m*factorial(n-1)*counts[r]==words['positive_counts'].get(key,0)
                checks+=1
            assert sum(counts.values())==(comb(m-1,n-1) if m>=n else 0)
    return dict(coefficient_checks=checks,sorted_partitions=partitions,
                simplified_numerators=generic_cases,maximum_n=9,maximum_m=cap)


def main():
    out=json.loads(DEST.read_text()) if '--resume' in sys.argv and DEST.exists() else {}
    for name,fn in [('words',word_enumeration),('generating_functions',lambda:generating_functions(out['words']))]:
        if name in out:continue
        print('START',name,flush=True);out[name]=fn()
        DEST.write_text(json.dumps(out,indent=2)+'\n');print('PASS',name,flush=True)
    print('ALL BLOCKS COMPLETE',flush=True)


if __name__=='__main__':main()
