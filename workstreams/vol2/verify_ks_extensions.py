"""Remaining KS quantiles and exercises 19,21,22: independent finite models."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb,factorial
from pathlib import Path
import json,random,sys
import mpmath as mp
import sympy as sp
ROOT=Path(__file__).resolve().parent
mp.mp.dps=90

def save(o):
    (ROOT/'results/ks-extensions.json').write_text(json.dumps(o,indent=2)+'\n')

def fmt(x):return mp.nstr(x,35)

def simplex(bounds):
    # Ordered-uniform integral: independent of the nonnegative binomial DP.
    poly=[mp.mpf(1)]
    for b in bounds:
        a=[mp.mpf(0)]+[c/(i+1) for i,c in enumerate(poly)]
        a[0]=-sum(c*b**i for i,c in enumerate(a));poly=a
    return sum(poly)*factorial(len(bounds))

def barrier_dp(bounds):
    # At boundary b_j, at most j-1 observations may have fallen below it.
    n=len(bounds);prev=mp.mpf(0);dp={0:mp.mpf(1)}
    for j,b in enumerate(bounds,1):
        q=(b-prev)/(1-prev);new={}
        for old,w in dp.items():
            for extra in range(j-old):
                total=old+extra
                term=w*comb(n-old,extra)*q**extra*(1-q)**(n-old-extra)
                new[total]=new.get(total,mp.mpf(0))+term
        dp=new;prev=b
    return sum(dp.values())

def weighted_bounds(n,s):
    lam=s/mp.sqrt(n);ans=[]
    for j in range(1,n+1):
        a=mp.mpf(j)/n
        ans.append((2*a+lam**2-lam*mp.sqrt(lam**2+4*a*(1-a)))/(2*(1+lam**2)))
    return ans

def weighted_cdf(n,s):return barrier_dp(weighted_bounds(n,s))

def stat_keys(counts):
    n=sum(counts);k=len(counts);cum=0;d=0
    for j,c in enumerate(counts,1):
        cum+=c;d=max(d,abs(k*cum-n*j))
    return d,sum((k*c-n)**2 for c in counts)

def compositions(n,k):
    if k==1:yield(n,);return
    for a in range(n+1):
        for rest in compositions(n-a,k-1):yield(a,)+rest

def multinomial_weight(counts):
    rem=sum(counts);w=1
    for a in counts:
        w*=comb(rem,a);rem-=a
    return w

def critical(hist,denom,alpha=F(1,20)):
    above=0
    for key,mass in sorted(hist.items(),reverse=True):
        if F(above+mass,denom)>=alpha:
            return key,(alpha*denom-above)/mass
        above+=mass
    raise AssertionError('no critical atom')

def rejection(hist,denom,c,gamma):
    return (sum(m for k,m in hist.items() if k>c)+gamma*hist.get(c,0))/denom

def main():
    out=json.loads((ROOT/'results/ks-extensions.json').read_text()) if '--resume' in sys.argv else {'status':'partial'}
    if 'limit_quantiles' not in out:
        entries=[]
        for p,s in zip(['.01','.05','.25','.5','.75','.95','.99'],['.07089','.1601','.3793','.5887','.8326','1.2239','1.5174']):
            q=mp.sqrt(-mp.log(1-mp.mpf(p))/2);half=mp.mpf(5)*10**(-len(s.split('.')[1])-1)
            assert abs(q-mp.mpf(s))<half
            entries.append(dict(p=p,printed=s,exact_numeric=fmt(q)))
        out['limit_quantiles']=entries;save(out);print('LIMIT',len(entries),flush=True)
    if 'multivariate19' not in out:
        u,v,theta=sp.symbols('u v theta',real=True)
        c=u*v*(1+theta*(1-u)*(1-v));density=sp.diff(c,u,v)
        assert sp.expand(density-(1+theta*(1-2*u)*(1-2*v)))==0
        mass=sp.integrate(density,(u,0,1),(v,0,1))
        expected=sp.expand(sp.integrate((1-c)*density,(u,0,1),(v,0,1)))
        assert mass==1 and expected==sp.Rational(3,4)-theta/18
        out['multivariate19']=dict(cdf=str(c),density=str(density),mean_positive_statistic_n1=str(expected),valid_density_range='-1<=theta<=1; strictly positive for |theta|<1');save(out);print('MULTIVARIATE',flush=True)
    if 'weighted22' not in out:
        cases=[]
        for n in [1,2,3,5,10,20]:
            for s in [mp.mpf('.25'),mp.mpf(1),mp.mpf(2),mp.mpf(5)]:
                bounds=weighted_bounds(n,s)
                assert all(0<b<=mp.mpf(j)/n for j,b in enumerate(bounds,1))
                a=simplex(bounds);b=barrier_dp(bounds)
                assert abs(a-b)<mp.mpf('1e-65'),(n,s,a,b)
                if n==1:assert abs(a-s*s/(1+s*s))<mp.mpf('1e-70')
                cases.append(dict(n=n,s=fmt(s),cdf=fmt(a)))
        quantiles=[]
        for n in [1,5,20]:
            lo=mp.mpf(0);hi=mp.mpf(8)
            assert weighted_cdf(n,hi)>mp.mpf('.95')
            for _ in range(95):
                mid=(lo+hi)/2
                if weighted_cdf(n,mid)<mp.mpf('.95'):lo=mid
                else:hi=mid
            q=(lo+hi)/2
            assert abs(simplex(weighted_bounds(n,q))-mp.mpf('.95'))<mp.mpf('1e-27')
            quantiles.append(dict(n=n,p='.95',quantile=fmt(q)))
            print('WEIGHTED QUANTILE',n,fmt(q),flush=True)
        base=json.loads((ROOT/'results/ks.json').read_text())
        q=mp.mpf(next(z['calculated'] for z in base['table2'] if z['n']==20 and z['p']=='.95'))
        qweighted=mp.mpf(quantiles[-1]['quantile'])
        ordinary=[max(mp.mpf(0),mp.mpf(j)/20-q/mp.sqrt(20)) for j in range(1,21)]
        weighted=weighted_bounds(20,qweighted)
        powers=[]
        for name,G in [('null',lambda u:u),('diffuse_u^0.8',lambda u:u**mp.mpf('.8')),('tail_5pct_uniform_0_.001',lambda u:mp.mpf('.95')*u+mp.mpf('.05')*min(1000*u,1))]:
            vals=[]
            for bounds in [ordinary,weighted]:
                b=[G(u) for u in bounds];v=barrier_dp(b);w=simplex(b)
                assert abs(v-w)<mp.mpf('1e-60')
                vals.append(1-v)
            powers.append(dict(alternative=name,ordinary_power=fmt(vals[0]),weighted_power=fmt(vals[1])))
        out['weighted22']=dict(cdf_two_models=cases,quantiles=quantiles,power_n20=powers,ordinary95_threshold=fmt(q));save(out);print('WEIGHTED ALL',flush=True)
    if 'discrete21' not in out:
        # Independent ordered-word model for three ordered atoms.
        orderedcases=0
        for n in range(1,6):
            for probs in [(1,1,1),(1,2,3)]:
                a=[Counter(),Counter()];b=[Counter(),Counter()]
                for counts in compositions(n,3):
                    w=multinomial_weight(counts)
                    for p,c in zip(probs,counts):w*=p**c
                    for k,key in enumerate(stat_keys(counts)):a[k][key]+=w
                for word in product(range(3),repeat=n):
                    counts=[word.count(i) for i in range(3)];w=1
                    for i in word:w*=probs[i]
                    for k,key in enumerate(stat_keys(counts)):b[k][key]+=w
                    orderedcases+=1
                assert a==b and sum(a[0].values())==sum(probs)**n
        rows=[];rng=random.Random(20261101)
        for n in [20,60]:
            configs=list(compositions(n,4)); models=[]
            for name,probs in [('null',(1,1,1,1)),('shift',(7,7,3,3)),('alternating',(7,3,7,3))]:
                hist=[Counter(),Counter()];denom=sum(probs)**n
                for counts in configs:
                    w=multinomial_weight(counts)
                    for p,c in zip(probs,counts):w*=p**c
                    for k,key in enumerate(stat_keys(counts)):hist[k][key]+=w
                assert all(sum(h.values())==denom for h in hist)
                models.append((name,probs,hist,denom))
            null=models[0];critical_values=[critical(h,null[3]) for h in null[2]]
            assert all(rejection(h,null[3],c,g)==F(1,20) for h,(c,g) in zip(null[2],critical_values))
            assert F(sum(key*mass for key,mass in null[2][1].items()),null[3]*4*n)==3
            for name,probs,hist,denom in models:
                powers=[rejection(h,denom,c,g) for h,(c,g) in zip(hist,critical_values)]
                samples=[]
                for _ in range(3):
                    counts=[0]*4
                    for _ in range(n):
                        u=rng.randrange(sum(probs));c=0
                        while u>=probs[c]:u-=probs[c];c+=1
                        counts[c]+=1
                    keys=stat_keys(counts)
                    tails=[F(sum(mass for x,mass in h.items() if x>=key),null[3]) for key,h in zip(keys,null[2])]
                    samples.append(dict(counts=counts,KS_unscaled=str(F(keys[0],4*n)),Pearson=str(F(keys[1],4*n)),null_upper_tail=[str(x) for x in tails]))
                rows.append(dict(n=n,alternative=name,probability_numerators=list(probs),configurations=len(configs),randomized_power_exact=[str(x) for x in powers],power=[float(x) for x in powers],critical=[dict(key=c,boundary_rejection=str(g)) for c,g in critical_values],samples=samples))
            out['discrete21_partial']=rows;save(out);print('DISCRETE',n,len(configs),flush=True)
        out['discrete21']=dict(independent_ordered_words=orderedcases,rows=rows);out.pop('discrete21_partial',None);save(out)
    out['status']='all_checks_passed';save(out);print('ALL',flush=True)

if __name__=='__main__':main()
