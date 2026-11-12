"""Exact exercise 7.2.2--61: differences, coin partitions, and lower bound."""
from pathlib import Path
from math import comb,factorial
from itertools import product
import json,time,sys
import mpmath as mp


def coefficients(maxn):
    # P_1(m)=1. The Newton coefficients of Q_n are the differences of
    # P_n(1),...,P_n(n). To evaluate Q_n at 2m, use additions only.
    values=[1];all_coeff=[];pn=[]
    for n in range(1,maxn+1):
        t=values.copy()
        for k in range(1,n):
            for j in range(n-1,k-1,-1):t[j]-=t[j-1]
        all_coeff.append(t);pn.append(values[0])
        state=[0]+t
        q=[]
        for k in range(2*(n+1)):
            for j in range(n):state[j]+=state[j+1]
            if k%2==1:q.append(state[0])
        values=q
    return pn,all_coeff


def coin_coeff(n,mmax):
    top=(1<<n)*mmax
    dp=[0]*top;dp[0]=1
    for k in range(n):
        coin=1<<k
        for j in range(coin,top):dp[j]+=dp[j-coin]
    return [dp[(1<<n)*m-1] for m in range(1,mmax+1)]


def main():
    # P_200 has more than 4300 decimal digits; all integers are computed here.
    sys.set_int_max_str_digits(0)
    started=time.monotonic();pn,coef=coefficients(200)
    assert pn[:6]==[1,2,6,26,166,1626]
    assert coef[1]==[2,2] and coef[2]==[6,14,8]
    checked=0
    for n in range(1,9):
        for m,count in enumerate(coin_coeff(n,20),1):
            q=sum(a*comb(m,k) for k,a in enumerate(coef[n-1],1))
            previous=sum(a*comb(m-1,k) for k,a in enumerate(coef[n-1],1))
            assert q-previous==count
            assert count*factorial(n-1)>=2**comb(n,2)*m**(n-1)
            checked+=1
    # Independent b(j)=b(j-1)+[j even]b(j/2), no polynomial machinery.
    b=[1]*(1<<20)
    for j in range(1,len(b)):b[j]=b[j-1]+(b[j//2] if j%2==0 else 0)
    assert [b[(1<<n)-1] for n in range(1,21)]==pn[:20]
    # Explicit bijection for every sequence through length 6.
    counts=[]
    def sequences(n,prefix=(1,)):
        if len(prefix)==n:yield prefix;return
        for x in range(1,2*prefix[-1]+1):yield from sequences(n,prefix+(x,))
    for n in range(1,7):
        images=set()
        for seq in sequences(n):
            a=tuple(2*seq[i]-seq[i+1] for i in range(n-1))+(2*seq[-1]-1,)
            assert all(x>=0 for x in a) and sum(x*2**(n-1-i) for i,x in enumerate(a))==2**n-1
            images.add(a)
        assert len(images)==pn[n-1];counts.append(len(images))
    mp.mp.dps=60
    asym=[]
    for n in [10,20,40,80,100,150,200]:
        t=mp.log(n,2)
        main=mp.mpf(comb(n,2))-mp.log(mp.factorial(n-1),2)+t*(t-1)/2
        asym.append({'n':n,'residual':str(mp.log(pn[n-1],2)-main)})
    out={'status':'pass','P_n_first20':pn[:20],'coefficients_first8':coef[:8],
         'general_m_coin_checks':checked,'all_sequences_bijection_counts':counts,
         'P_200':str(pn[-1]),'asymptotic_residuals':asym,
         'elapsed_seconds':time.monotonic()-started,'asymptotic_proof_status':'Mahler 1940, pp.121-123, plus the explicit substitution in ESTIMATION_NOTES.md; the finite residuals are supplementary only'}
    R=Path(__file__).resolve().parent/'results/estimation';(R/'cayley-verified.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='P_200'},indent=2))

if __name__=='__main__':main()
