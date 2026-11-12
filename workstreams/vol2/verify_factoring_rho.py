#!/usr/bin/env python3
"""Exact finite rho checks, bounds for exercise4, and rigorous model constants."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd, isqrt, prod
import csv
import json
import os
import time
import argparse

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/factoring-rho.json'
LIMIT=50000
spf=list(range(LIMIT+1))
for p in range(2,isqrt(LIMIT)+1):
    if spf[p]==p:
        for n in range(p*p,LIMIT+1,p):
            if spf[n]==n:spf[n]=p


def algorithm_b(N):
    n,x,anchor,ell,k,m=N,5,2,1,1,1
    trace=[];history=[2%N,5%N];calls=0
    while True:
        if spf[n]==n:
            trace.append(dict(value=n,m=m,call=calls,kind='prime'))
            return trace,'done'
        while True:
            assert x%n==history[m]%n and anchor%n==history[ell-1]%n
            assert ell==1<<(m.bit_length()-1) and k==2*ell-m
            assert n*prod(t['value'] for t in trace)==N
            calls+=1
            g=gcd(anchor-x,n)
            if g>1:
                trace.append(dict(value=g,m=m,call=calls,kind='gcd'))
                if g==n:return trace,'failed'
                n//=g;x%=n;anchor%=n
                break
            k-=1
            if k==0:anchor=x;ell*=2;k=ell
            x=(x*x+1)%n;m+=1
            history.append((history[-1]*history[-1]+1)%N)


def b_checks():
    failures=0;composite=set();examples={}
    for n in range(2,LIMIT+1):
        trace,status=algorithm_b(n)
        assert prod(t['value'] for t in trace)==n
        failures+=status=='failed'
        for t in trace:
            g=t['value']
            if spf[g]!=g:composite.add(g)
        if n in (4,6,25,25852):examples[str(n)]=dict(trace=trace,status=status)
    for g in composite:
        ts,status=algorithm_b(g)
        assert status=='failed' and len(ts)==1 and ts[0]['value']==g
    ex=examples['25852']['trace']
    assert [t['value'] for t in ex]==[4,23,281]
    assert ex[0]['call']==3 and ex[1]['call']==10
    assert ex[1]['m']-ex[0]['m']==6  # six advances, plus repeated B3 after division
    return dict(inputs=LIMIT-1,terminal_failures=failures,composite_outputs_checked=len(composite),examples=examples)


def next_power(n):
    return 1<<(n-1).bit_length()


def finite_bounds():
    for l in range(1,513):
        direct=sum(next_power(max(l+1-lam,lam)) for lam in range(1,l+1))
        q=1<<(l.bit_length()-1)
        formula=q*(3*l-2*q)
        assert direct==formula and 8*l*l<=8*formula<=9*l*l
    summaries={}
    for m in range(1,97):
        p=F(1);Q=F(0);E=F(0)
        for l in range(1,m+1):
            Q+=p
            q=1<<(l.bit_length()-1)
            f=q*(3*l-2*q)
            E+=(F(f)+F(l*(l+1),2)-l)*p/m
            p*=F(m-l,m)
        assert F(3,2)*Q-F(1,2)<=E<=F(13,8)*Q-F(1,2)
        if m in (1,2,4,16,64,96):
            summaries[str(m)]={'Q':str(Q),'mean':str(E)}
    return dict(exact_f_values=512,finite_mapping_sizes=96,examples=summaries)


def abstract_detection(mu,lam,skip):
    # Independent sequence labels for a tail followed by a cycle.
    def state(n):
        return n if n<mu else mu+(n-mu)%lam
    m,ell,k=1,1,1
    checks=0
    while True:
        if not skip or m==1 or 2*k<=ell:
            checks+=1
            if state(m)==state(ell-1):return m,checks
        k-=1
        if not k:ell*=2;k=ell
        m+=1


def skipping():
    checks=0
    for mu in range(128):
        for lam in range(1,129):
            ell=next_power(max(mu+1,lam))
            ordinary=ell-1+lam
            got,c=abstract_detection(mu,lam,True)
            if (mu,lam)==(0,1):
                assert (got,c)==(1,1)
            else:
                ell=max(2,ell)
                h=ell//2
                delta=lam*((h+lam)//lam)
                assert (got,c)==(ell-1+delta,delta)
                e_mu=0 if mu==0 else 1<<(mu.bit_length()-1)
                assert got-ordinary==e_mu-e_mu%lam
            checks+=1
    return dict(tail_cycle_pairs=checks,initial_fixed_point_explicit=True)


def census_check():
    with (ROOT/'results/factoring-rho-census.csv').open() as f:
        rows=[{k:int(v) for k,v in r.items()} for r in csv.DictReader(f)]
    sieve=bytearray(b'\1')*1000000
    sieve[:2]=b'\0\0'
    for p in range(2,1000):
        if sieve[p]:
            sieve[p*p:1000000:p]=b'\0'*(((999999-p*p)//p)+1)
    assert [r['p'] for r in rows]==[p for p in range(1000000) if sieve[p]]
    expected=[(999863,276),(999883,409),(999907,2106),(999917,1561),(999931,1593),
              (999953,1091),(999959,474),(999961,1819),(999979,395),(999983,814)]
    assert [(r['p'],r['m']) for r in rows[-10:]]==expected
    assert all(r['m']==next_power(max(r['mu']+1,r['lambda']))-1+r['lambda'] for r in rows)
    assert all(r['m']**2<144*r['p'] for r in rows)
    maxrow=max(rows,key=lambda r:r['m'])
    ratrow=max(rows,key=lambda r:F(r['m']**2,r['p']))
    assert (maxrow['p'],maxrow['m'])==(874771,7685)
    assert (ratrow['p'],ratrow['m'])==(290047,6251)
    return dict(primes=len(rows),printed_ten=expected,maximum=maxrow,ratio_maximum=ratrow,
                sum_iterations=sum(r['m'] for r in rows))


def trial_prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))


def f8_certificate():
    certificates=[]
    factorizations={3853149761:{2:6,5:1,719:1,16747:1},
                    1238926361552897:{2:11,157:1,3853149761:1}}
    proved={2,5,157,719,16747}
    assert all(trial_prime(q) for q in proved)
    for n,fs in factorizations.items():
        assert prod(q**e for q,e in fs.items())==n-1 and all(q in proved for q in fs)
        for a in range(2,10000):
            if pow(a,n-1,n)==1 and all(gcd(pow(a,(n-1)//q,n)-1,n)==1 for q in fs):
                break
        else:raise AssertionError(n)
        certificates.append(dict(n=n,factors=fs,witness=a))
        proved.add(n)
    p=1238926361552897
    assert ((1<<256)+1)%p==0
    assert trial_prime(850112303) and trial_prime(695361131)
    return dict(certificates=certificates,prime=p,fermat_quotient=((1<<256)+1)//p,
                large_record_primality_verified=True)


def constants():
    from flint import arb,ctx
    ctx.dps=90
    pi=arb.pi();ln2=arb(2).log();gamma=arb.const_euler();Q=(pi/2).sqrt()
    B=(3/(4*ln2)+arb(1)/2)*Q
    floyd=pi*pi/12*Q
    skips=3/(4*ln2)*Q
    gcds=((pi.log()-gamma)/(4*ln2)+arb(1)/2)*Q
    crossover=(3*floyd-B)/(B-floyd)
    rounded=[(B,'1.98277'),(floyd,'1.03081'),(3*floyd,'3.09243'),
             (skips,'1.35611'),(gcds,'.88319'),(crossover,'1.17')]
    for v,t in rounded:
        scale=10**len(t.split('.')[1]);mid=arb(t)
        assert v>mid-arb(1)/(2*scale) and v<mid+arb(1)/(2*scale)
    # Subsequence constants for fixed powers-of-two phase.
    # q(3x-2q) integrated exactly for q<=x<=2q.
    phases={}
    for phase in (arb(0),arb(1)/2):
        val=arb(0)
        for j in range(-50,6):
            q=arb(2)**(arb(j)-phase)
            integral=Q*((2*q/arb(2).sqrt()).erf()-(q/arb(2).sqrt()).erf())
            val+=3*q*((-q*q/2).exp()-(-2*q*q).exp())-2*q*q*integral
        lower_x=arb(2)**(-50-phase);upper_x=arb(2)**(6-phase)
        tail=arb(3)/8*lower_x**3+arb(9)/8*(upper_x+1/upper_x)*(-upper_x*upper_x/2).exp()
        full=val+Q/2
        phases['0' if phase==0 else '1/2']=dict(value=full.str(70),absolute_tail=tail.str(25),
                lower=(full-tail).str(70),upper=(full+tail).str(70))
    return dict(brent_phase_average=B.str(60),floyd=floyd.str(60),skipped=skips.str(60),
                gcds=gcds.str(60),gcd_cost_crossover=crossover.str(60),
                fixed_phase_subsequence_limits=phases,
                scope='Phase-average constants are approximations for a fixed dyadic schedule, as stated in the book; rigorous finite bounds do not assume a uniform phase.')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--resume',action='store_true')
    args=parser.parse_args();result=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'checkpoints':{}}
    result['pid']=os.getpid();start=time.monotonic()
    for name,fn in [('algorithmB',b_checks),('finite_bounds',finite_bounds),('skip_checks',skipping),
                    ('small_census',census_check),('F8',f8_certificate),('constants',constants)]:
        if name in result['checkpoints']:
            print('reuse',name,flush=True);continue
        t=time.monotonic();result['checkpoints'][name]={'result':fn(),'seconds':time.monotonic()-t}
        OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print('passed',name,flush=True)
    result['status']='passed';result['elapsed_this_run']=time.monotonic()-start
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print('ALL PASSED',result['pid'],result['elapsed_this_run'],flush=True)
