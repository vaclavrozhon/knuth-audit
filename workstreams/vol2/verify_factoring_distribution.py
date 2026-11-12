#!/usr/bin/env python3
"""Rigorous fixed-point Dickman enclosures and exact finite factor identities.

All numerical enclosure endpoints are integers scaled by SCALE.  No binary
floating-point result participates in a certificate.  For rho on each unit
interval: |rho''|<=1 and |(rho(u-1)/u)''|<=2.  A midpoint rule with linear
interpolation therefore has explicit local error; see the accompanying note.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, isqrt, comb
import argparse
import json
import os
import pickle
import time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/factoring-distribution.json'
CACHE=ROOT/'results/factoring-dickman-grid.pickle'
M=16384
STOP=16
SCALE=1<<90


def ceildiv(a,b):
    return -((-a)//b)


def show(interval):
    lo,hi=interval
    return dict(lower=str(Q(lo,SCALE)),upper=str(Q(hi,SCALE)),
                decimal_display=[lo/SCALE,hi/SCALE])


def build_grid():
    lower=[SCALE]*(M+1)
    upper=lower.copy()
    interp=ceildiv(SCALE,4*M*M)
    error=ceildiv(SCALE,12*M**3)
    for i in range(M,STOP*M):
        j=i-M
        low_integral=(lower[j]+lower[j+1]-(interp if j>=M else 0))//(2*i+1)-error
        high_integral=ceildiv(upper[j]+upper[j+1],2*i+1)+error
        lower.append(max(0,lower[-1]-high_integral))
        upper.append(min(upper[-1],upper[-1]-low_integral,
                         ceildiv(SCALE,factorial((i+1)//M))))
        assert lower[-1]<=upper[-1]
    with CACHE.open('wb') as f:pickle.dump((M,STOP,SCALE,lower,upper),f,protocol=5)
    return lower,upper


def read_grid():
    if CACHE.exists():
        with CACHE.open('rb') as f:m,stop,scale,lower,upper=pickle.load(f)
        assert (m,stop,scale)==(M,STOP,SCALE)
        return lower,upper
    return build_grid()


def at(u,lower,upper):
    u=Q(u)
    if u<=1:return SCALE,SCALE
    if u>=STOP:return 0,ceildiv(SCALE,factorial(u.numerator//u.denominator))
    z=u*M;i=z.numerator//z.denominator;f=z-i
    if not f:return lower[i],upper[i]
    l=Q(lower[i])*(1-f)+lower[i+1]*f-Q(SCALE,8*M*M)
    h=Q(upper[i])*(1-f)+upper[i+1]*f
    return max(0,l.numerator//l.denominator),ceildiv(h.numerator,h.denominator)


TAIL=ceildiv(17*SCALE,16*factorial(16))


def second(beta,lower,upper):
    beta=Q(beta)
    if beta>=Q(1,2):return SCALE,SCALE
    b,d=beta.numerator,beta.denominator
    z=1/beta
    end=min(Q(STOP),z-1)
    full=int(end*M)
    low=high=0
    for i in range(full+1):
        weight=1 if i in (0,full) else 2
        den=2*(d*M-b*i)
        low+=weight*b*lower[i]//den
        high+=ceildiv(weight*b*upper[i],den)
    fraction=end-Q(full,M)
    if fraction:
        left=(Q(lower[full]*b*M,d*M-b*full),Q(upper[full]*b*M,d*M-b*full))
        l,h=at(end,lower,upper)
        right=(Q(l)/(z-end),Q(h)/(z-end))
        a=(left[0]+right[0])*fraction/2
        c=(left[1]+right[1])*fraction/2
        low+=a.numerator//a.denominator
        high+=ceildiv(c.numerator,c.denominator)
    err=ceildiv(5*end.numerator*SCALE,12*end.denominator*M*M)
    l,h=at(z,lower,upper)
    return max(0,low-err+l),high+err+h+(TAIL if z-1>STOP else 0)


def weighted_integral(lower,upper,start,power,shift,curvature):
    low=high=0
    for i in range(start*M,STOP*M+1):
        w=1 if i in (start*M,STOP*M) else 2
        if power:
            num=w*M**(power-1);den=2*(i+shift*M)**power
        else:num=w;den=2*M
        low+=num*lower[i]//den
        high+=ceildiv(num*upper[i],den)
    err=ceildiv(curvature*(STOP-start)*SCALE,12*M*M)
    return low-err,high+err+TAIL


def grid_checks():
    from flint import arb,ctx
    ctx.dps=90
    lower,upper=read_grid()
    # Independent closed form on [1,2] at 33 rational points.
    for k in range(33):
        u=Q(32+k,32);l,h=at(u,lower,upper)
        v=1-(arb(u.numerator)/u.denominator).log()
        assert v>arb(l)/SCALE and v<arb(h)/SCALE if k else v==1
    targets=['.01','.05','.10','.20','.35','.50','.65','.80','.90','.95','.99']
    alphas=['.2697','.3348','.3785','.4430','.5220','.6065','.7047','.8187','.9048','.9512','.9900']
    betas=['.0056','.0273','.0531','.1003','.1611','.2117','.2582','.3104','.3590','.3967','.4517']
    rows=[]
    for prob,a,b in zip(targets,alphas,betas):
        target=Q(prob);result={'probability':prob}
        for label,value in [('alpha',a),('beta',b)]:
            left=Q(value)-Q(1,20000);right=Q(value)+Q(1,20000)
            if label=='alpha':
                lval=at(1/left,lower,upper);rval=at(1/right,lower,upper)
            else:lval=second(left,lower,upper);rval=second(right,lower,upper)
            assert Q(lval[1],SCALE)<target<Q(rval[0],SCALE),(label,prob,value,show(lval),show(rval))
            result[label]={'printed':value,'cdf_at_lower_rounding_edge':show(lval),
                           'cdf_at_upper_rounding_edge':show(rval)}
        rows.append(result)
    return dict(mesh=M,scale_bits=90,stop=STOP,closed_form_checks=33,quantiles=rows,
                integer_values={str(k):show((lower[k*M],upper[k*M])) for k in range(1,STOP+1)})


def integral_checks():
    from flint import arb,ctx
    ctx.dps=90
    lower,upper=read_grid()
    delta=weighted_integral(lower,upper,0,2,1,11)
    probability=weighted_integral(lower,upper,0,1,2,2)
    norm=weighted_integral(lower,upper,0,0,0,1)
    meanpart=weighted_integral(lower,upper,1,2,0,11)
    mean=(SCALE-meanpart[1],SCALE-meanpart[0])
    assert Q(624325,1000000)<Q(delta[0],SCALE)<=Q(delta[1],SCALE)<Q(624335,1000000)
    assert max(delta[0],probability[0],mean[0])<=min(delta[1],probability[1],mean[1])
    e=arb.const_euler().exp()
    assert arb(norm[0])/SCALE<e<arb(norm[1])/SCALE
    # Integral on [n-1,n] = n*rho(n), with a factorial bound on the rest.
    discrete=(sum(n*lower[n*M] for n in range(1,STOP+1)),
              sum(n*upper[n*M] for n in range(1,STOP+1))+ceildiv(17*SCALE,16*factorial(16)))
    assert max(discrete[0],norm[0])<=min(discrete[1],norm[1])
    return {name:show(v) for name,v in [('Golomb_Dickman',delta),('second_below_sqrt_largest',probability),
                                      ('mean_largest_log',mean),('rho_integral',norm),('sum_n_rho_n',discrete)]}


def additive_constant():
    from flint import arb,ctx
    ctx.dps=110
    K=256;phi=list(range(K+1))
    for p in range(2,K+1):
        if phi[p]==p:
            for n in range(p,K+1,p):phi[n]-=phi[n]//p
    for n in range(1,K+1):assert sum(phi[d] for d in range(1,n+1) if n%d==0)==n
    val=arb.const_euler()+sum((arb(phi[n])/n)*arb(n).zeta().log() for n in range(2,K+1))
    tail=arb(3)/(arb(2)**K)
    printed='1.0346538818974379116197942984646382546703'
    low=arb(printed);high=low+arb(1)/(arb(10)**40)
    assert low<val and val+tail<high
    gaussian=(arb(3)/arb(2).sqrt()).erf()
    assert arb('.99725')<gaussian<arb('.99735')
    return dict(partial=val.str(80),tail_bound=tail.str(30),printed40_truncation=printed,
                divisors_identity_count=K,gaussian_three_sigma=gaussian.str(60))


def finite_counts():
    limit=2048
    spf=list(range(limit+1));spf[1]=1
    for p in range(2,isqrt(limit)+1):
        if spf[p]==p:
            for n in range(p*p,limit+1,p):
                if spf[n]==n:spf[n]=p
    primes=[p for p in range(2,limit+1) if spf[p]==p]
    factors=[[] for _ in range(limit+1)]
    for n in range(2,limit+1):factors[n]=sorted(factors[n//spf[n]]+[spf[n]],reverse=True)
    lengths=[len(f) for f in factors]
    total=0
    for N in range(1,limit+1):
        total+=lengths[N];independent=0
        for p in primes:
            if p>N:break
            q=p
            while q<=N:independent+=N//q;q*=p
        assert total==independent
    checks=0
    sizes=list(range(1,129))+list(range(256,limit+1,128))
    for y in range(1,33):
        psi=[0]*(limit+1);second_count=psi.copy();third_count=psi.copy()
        for n in range(1,limit+1):
            f=factors[n]+[1,1,1]
            psi[n]=psi[n-1]+(f[0]<=y)
            second_count[n]=second_count[n-1]+(f[1]<=y)
            third_count[n]=third_count[n-1]+(f[2]<=y)
        for N in sizes:
            big=[p for p in primes if y<p<=N]
            one=psi[N]+sum(psi[N//p] for p in big)
            two=one+sum(psi[N//(p*q)] for j,q in enumerate(big) for p in big[j:] if p*q<=N)
            assert one==second_count[N] and two==third_count[N]
            checks+=1
    return dict(mean_factor_count_identities=limit,two_and_three_factor_counts=checks,
                convention='Prime factors counted with multiplicity; absent factors set to1.')


def figure_and_permutations():
    lower,upper=read_grid()
    figure=[]
    for k in range(1,10):
        a=Q(k,10)
        figure.append(dict(alpha=str(a),F=show(at(1/a,lower,upper)),
                           G=show(second(a,lower,upper))))
    N=20;checks=0
    for r in range(1,N+1):
        # Direct counts by the cycle containing the least element.
        count=[[0]*(N+1) for _ in range(4)]
        for k in range(1,4):
            count[k][0]=1
            for n in range(1,N+1):
                count[k][n]=sum(factorial(n-1)//factorial(n-l)*count[k-(l>r)][n-l]
                                for l in range(1,n+1))
        # Independent marked-cycle generating polynomial.
        powers=[[Q(1)]+[Q(0)]*N]
        for j in range(1,N//(r+1)+1):
            old=powers[-1]
            powers.append([sum((old[n-l]/l for l in range(r+1,n+1)),Q(0))
                           for n in range(N+1)])
        for n in range(1,N+1):
            moments=[sum(v[:n+1])/factorial(j) for j,v in enumerate(powers)]
            for k in range(1,4):
                value=1-sum(((-1)**(j-k)*comb(j-1,k-1)*moments[j]
                             for j in range(k,len(moments))),Q(0))
                assert value==Q(count[k][n],factorial(n))
                checks+=1
    return dict(figure12_grid=figure,permutation_cdf_identities=checks,
                independent_models='Cycle containing least element vs marked-cycle polynomial and binomial inversion.')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--resume',action='store_true')
    args=parser.parse_args();result=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'checkpoints':{}}
    result['pid']=os.getpid();start=time.monotonic()
    for name,fn in [('grid_quantiles',grid_checks),('integrals',integral_checks),
                    ('additive_constant',additive_constant),('finite_counts',finite_counts),
                    ('figure_permutations',figure_and_permutations)]:
        if name in result['checkpoints']:
            print('reuse',name,flush=True);continue
        t=time.monotonic();result['checkpoints'][name]={'result':fn(),'seconds':time.monotonic()-t}
        OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print('passed',name,flush=True)
    result['status']='passed';result['elapsed_this_run']=time.monotonic()-start
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print('ALL PASSED',result['pid'],result['elapsed_this_run'],flush=True)
