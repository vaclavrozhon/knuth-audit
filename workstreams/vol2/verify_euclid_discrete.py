#!/usr/bin/env python3
"""Exact finite checks for TAOCP 4.5.3, pages 368--373 and exercises26--29."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import gcd
from collections import Counter
import json,os,sys,time
from flint import arb,arb_series,ctx

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/euclid-discrete.json'

def steps(u,v):
    n=0
    while v:
        u,v=v,u%v;n+=1
    return n

def cf(p,q):
    a=[]
    while p:
        k,r=divmod(q,p);a.append(k);q,p=p,r
    return a

def value(a):
    x=F(0)
    for k in reversed(a):x=1/(k+x)
    return x

@lru_cache(None)
def factors(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=1
    return out

def divisors(n):
    ds=[1]
    for p,e in factors(n).items():ds=[d*p**k for d in ds for k in range(e+1)]
    return ds

def phi(n):
    for p in factors(n):n=n//p*(p-1)
    return n

def mu(n):
    fs=factors(n)
    return 0 if any(e>1 for e in fs.values()) else (-1)**len(fs)

def rounded(q,digits):
    k=(2*q.numerator*10**digits+q.denominator)//(2*q.denominator)
    return f'{k//10**digits}.{k%10**digits:0{digits}d}'

def finite_tables():
    nlist=list(range(95,106))+list(range(996,1002))+[9999,10000,10001,49998,49999,50000,50001,99999,100000,100001]
    expected_T='5.0 4.4 5.3 4.8 4.7 4.6 5.3 4.6 5.3 4.7 4.6 6.5 7.3 7.0 6.8 6.4 6.7 8.6 8.3 9.1 9.8 10.6 9.7 10.0 10.7 10.3 11.0'.split()
    expected_tau='5.4 5.3 5.3 5.6 5.2 5.2 5.4 5.3 5.4 5.3 5.6 7.2 7.3 7.3 7.3 7.3 7.4 9.21 9.21 9.22 10.59 10.58 10.57 10.59 11.170 11.172 11.172'.split()
    rows=[]
    for n,t,ta in zip(nlist,expected_T,expected_tau,strict=True):
        total=0;coprime=0;count=0
        for m in range(n):
            s=steps(m,n);total+=s
            if gcd(m,n)==1:coprime+=s;count+=1
        assert count==phi(n)
        a,b=F(total,n),F(coprime,count)
        assert rounded(a,1)==t,(n,a,t)
        assert rounded(b,len(ta.split('.')[1]))==ta,(n,b,ta)
        rows.append({'n':n,'sum_steps':total,'phi':count,'sum_coprime_steps':coprime,'T':str(a),'tau':str(b),'printed_T':t,'corrected_printed_tau':ta})
    equalities=[]
    for n in [50,60]:
        vals=[F(sum(steps(m,k) for m in range(k) if gcd(m,k)==1),phi(k)) for k in [n,2*n]]
        assert vals[0]==vals[1]
        equalities.append({'n':n,'tau_n_equals_tau_2n':str(vals[0])})
    return {'rows':rows,'tau_equalities':equalities}

def fraction_table():
    table29=[[29],[14,2],[9,1,2],[7,4],[5,1,4],[4,1,5],[4,7],
             [3,1,1,1,2],[3,4,2],[2,1,9],[2,1,1,1,3],[2,2,2,2],[2,4,3],[2,14],
             [1,1,14],[1,1,4,3],[1,1,2,2,2],[1,1,1,1,1,3],[1,1,1,9],[1,2,4,2],[1,2,1,1,1,2],
             [1,3,7],[1,3,1,5],[1,4,1,4],[1,6,4],[1,8,1,2],[1,13,2],[1,28]]
    assert all(cf(m,29)==table29[m-1] and value(table29[m-1])==F(m,29) for m in range(1,29))
    counts=Counter(a for row in table29 for a in row)
    assert sum(counts.values())==96 and [counts[k] for k in [1,2,3]]==[39,21,8]
    assert sum(steps(m,100) for m in range(100))==456
    return {'table29':table29,'table29_counts':dict(sorted(counts.items())),'T100':'114/25'}

def exact_identities():
    reversals=0;convolutions=0;square_pairs=0
    totals={};coprime={}
    for n in range(1,513):
        totals[n]=sum(steps(m,n) for m in range(n))
        coprime[n]=sum(steps(m,n) for m in range(n) if gcd(m,n)==1)
        assert totals[n]==sum(coprime[d] for d in divisors(n));convolutions+=1
        for m in range(1,n//2+1):
            a=cf(m,n);b=a[::-1];x=value(b)
            assert a[0]>=2 and a[-1]>=2
            assert (x*n).denominator==1 and 0<x<=F(1,2)
            assert cf((x*n).numerator,n)==b
            if gcd(m,n)==1:assert (m*(x*n).numerator-(-1)**(len(a)-1))%n==0
            reversals+=1
    for N in [1,2,3,4,7,10,17,29,50,100,128]:
        direct=sum(steps(m,n) for m in range(1,N+1) for n in range(1,N+1))
        assert direct==2*sum(totals[n] for n in range(1,N+1))-N*(N+1)//2
        square_pairs+=N*N
    arithmetic=0
    for n in range(1,1025):
        ds=divisors(n)
        assert sum(mu(d) for d in ds)==int(n==1)
        assert sum(phi(d) for d in ds)==n
        assert sum(mu(n//d)*d for d in ds)==phi(n)
        fs=factors(n)
        for p,e in fs.items():
            assert sum(int(len(factors(d))==1 and p in factors(d)) for d in ds)==e
            assert sum(mu(n//d)*factors(d).get(p,0) for d in ds)==int(len(fs)==1)
            lhs=F(sum(phi(d)*factors(d).get(p,0) for d in ds),n)
            rhs=F(e)-sum(F(1,p**k) for k in range(1,e+1))
            assert lhs==rhs
        arithmetic+=1
    return {'reverse_fractions':reversals,'gcd_convolutions':convolutions,'square_pair_checks':square_pairs,'number_theory_inputs':arithmetic,'maximum_n_reversal':512}

def constants():
    ctx.dps=100
    a=12*arb(2).log()/arb.pi()**2
    zp=arb_series([2,1],prec=2).zeta()[1]
    gamma=arb.const_euler()
    C=a/2*(3*arb(2).log()+4*gamma-24/arb.pi()**2*zp-2)-arb(1)/2
    D=C-a/2+a*zp/arb(2).zeta()-arb(1)/2
    direct=a/2*(3*arb(2).log()+4*gamma-12/arb.pi()**2*zp-3)-1
    assert (D-direct).contains(0)
    def round_arb(x,d):return str((x*10**d+arb(1)/2).floor().unique_fmpz())
    assert round_arb(C,10)=='14670780794'
    assert round_arb(D,10)=='653514259'
    assert round_arb(a,9)=='842765913'
    assert round_arb(a*arb(10).log(),4)=='19405'
    probs=[(arb((k+1)**2)/((k+1)**2-1)).log()/arb(2).log()*100 for k in range(1,5)]
    assert [round_arb(q,3) for q in probs]==['41504','16993','9311','5889']
    return {'leading_coefficient':a.str(60),'base10_coefficient':(a*arb(10).log()).str(60),'zeta_prime_2':zp.str(60),'Porter_C':C.str(60),'square_constant':D.str(60),'quotient_percentages':[p.str(40) for p in probs],'working_decimal_precision':ctx.dps}

def main():
    print('PID',os.getpid(),flush=True)
    out=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {'scope':'4.5.3 discrete tables and arithmetic identities; asymptotic proofs in notes/euclid-discrete.md','checkpoints':{}}
    for name,fn in [('tables',finite_tables),('fraction_table',fraction_table),('identities',exact_identities),('constants',constants)]:
        if name in out['checkpoints']:print('SKIP',name,flush=True);continue
        start=time.monotonic();out['checkpoints'][name]=fn()
        OUT.write_text(json.dumps(out,indent=2)+'\n')
        print('PASS',name,round(time.monotonic()-start,3),flush=True)
    print('ALL DISCRETE CHECKPOINTS PASSED',flush=True)

if __name__=='__main__':main()
