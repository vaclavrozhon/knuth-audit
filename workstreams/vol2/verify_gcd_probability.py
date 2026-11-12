#!/usr/bin/env python3
"""Finite independent checks for the density arguments in TAOCP 4.5.2-10--14."""
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json, sys, time
import mpmath as mp
from sympy.ntheory.modular import crt
from sympy import primerange
from sources.slash_arithmetic import mobius_sieve

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/gcd-probability.json'


def finite():
    limit=512;mu=mobius_sieve(limit);q=[0]*(limit+1)
    tau=[0]*(limit+1);phi=[0]*(limit+1)
    for d in range(1,limit+1):
        for k in range(d,limit+1,d):
            tau[k]+=1;phi[k]+=mu[d]*(k//d)
    hist=Counter();records=[];hist_entries=0
    for n in range(1,limit+1):
        for v in range(1,n):hist[gcd(n,v)]+=2
        hist[n]+=1
        q[n]=sum(mu[d]*(n//d)**2 for d in range(1,n+1))
        assert q[n]==hist[1] and sum(hist.values())==n*n
        for d in range(1,n+1):
            assert hist[d]==q[n//d];hist_entries+=1
        common=sum(tau[d]*hist[d] for d in range(1,n+1))
        assert common==sum((n//d)**2 for d in range(1,n+1))
        gsum=sum(d*hist[d] for d in range(1,n+1))
        assert gsum==sum(phi[d]*(n//d)**2 for d in range(1,n+1))
        assert sum(hist[d] for d in [1,2,3])==sum(q[n//d] for d in [1,2,3])
        if n in [1,2,3,4,8,16,32,64,128,256,512]:
            records.append(dict(n=n,coprime_count=q[n],prob_gcd_le_3=str(F(sum(hist[d] for d in [1,2,3]),n*n)),
                                mean_gcd=str(F(gsum,n*n)),mean_common_divisors=str(F(common,n*n))))
    return dict(square_side=limit,direct_pairs=limit*limit,exact_histogram_entries=hist_entries,records=records)


def odd():
    limit=256;mu=mobius_sieve(2*limit);hist=Counter();records=[]
    for n in range(1,limit+1):
        last=2*n-1
        for v in range(1,last,2):hist[gcd(last,v)]+=2
        hist[last]+=1
        exact=sum(mu[d]*((last//d+1)//2)**2 for d in range(1,last+1,2))
        assert hist[1]==exact
        if n in [1,2,4,8,16,32,64,128,256]:
            records.append(dict(n=n,coprime_count=exact,total=n*n))
    return dict(direct_odd_pairs=limit*limit,records=records)


def constants():
    mp.mp.dps=80
    z2=mp.zeta(2);L=-mp.diff(mp.zeta,2)/z2
    vals={'coprime':1/z2,'gcd_le_3':mp.mpf(49)/(6*mp.pi**2),
          'common_divisor_mean':z2,'odd_coprime':8/mp.pi**2,
          'log_gcd_mean':L,'odd_log_gcd_mean':L-mp.log(2)/3}
    assert mp.nint(vals['coprime']*10**5)==60793
    assert mp.nint(vals['gcd_le_3']*10**5)==82746
    assert mp.nint(vals['log_gcd_mean']*10**5)==56996
    assert mp.nint(vals['odd_log_gcd_mean']*10**5)==33891
    # Independent positive-term truncation: prime powers with weight log(p).
    cutoff=10000;partial=mp.fsum(mp.log(p)/(p*p-1) for p in primerange(2,cutoff+1))
    # Remaining primes are a subset of all integers greater than cutoff;
    # 1/(p^2-1) <= 1/((1-cutoff^-2)*p^2), followed by an integral bound.
    bound=(mp.log(cutoff)+1)/cutoff/(1-mp.mpf(1)/cutoff**2)
    assert partial<L<partial+bound
    return dict(values={k:mp.nstr(v,65) for k,v in vals.items()},prime_cutoff=cutoff,
                independent_prime_sum=mp.nstr(partial,65),tail_upper_bound=mp.nstr(bound,30),
                precision_note='80 decimal digit numerical evaluation; the analytic identities are proved separately.')


def shifted_counterexample():
    # Distinct primes for every grid position; CRT chooses both offsets.
    primes=list(primerange(2,500));records=[]
    for n in range(2,8):
        ps=primes[:n*n]
        f=int(crt(ps,[-i for i in range(n) for j in range(n)])[0])
        g=int(crt(ps,[-j for i in range(n) for j in range(n)])[0])
        for i in range(n):
            for j in range(n):
                assert (f+i)%ps[i*n+j]==(g+j)%ps[i*n+j]==0
                assert gcd(f+i,g+j)>1
        records.append(dict(n=n,f=f,g=g,coprime_count=0,prime_matrix=[ps[i*n:(i+1)*n] for i in range(n)]))
    return dict(known_2004_erratum_witnesses=records)


if __name__=='__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('finite',finite),('odd',odd),('constants',constants),('shifted_counterexample',shifted_counterexample)]:
        if name in data:continue
        start=time.monotonic();value=fn()
        data[name]=dict(status='passed',seconds=time.monotonic()-start,result=value)
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,'passed',round(data[name]['seconds'],3),flush=True)
