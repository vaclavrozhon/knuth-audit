"""TAOCP 3.3.1 KS formulas, finite distributions and linear-time algorithm."""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import comb,factorial,floor
from pathlib import Path
import json
import sys
import mpmath as mp
import sympy as sp
ROOT=Path(__file__).resolve().parent
mp.mp.dps=70
TABLE='''1 .01000 .05000 .2500 .5000 .7500 .9500 .9900
2 .01400 .06749 .2929 .5176 .7071 1.0980 1.2728
3 .01699 .07919 .3112 .5147 .7539 1.1017 1.3589
4 .01943 .08789 .3202 .5110 .7642 1.1304 1.3777
5 .02152 .09471 .3249 .5245 .7674 1.1392 1.4024
6 .02336 .1002 .3272 .5319 .7703 1.1463 1.4144
7 .02501 .1048 .3280 .5364 .7755 1.1537 1.4246
8 .02650 .1086 .3280 .5392 .7797 1.1586 1.4327
9 .02786 .1119 .3274 .5411 .7825 1.1624 1.4388
10 .02912 .1147 .3297 .5426 .7845 1.1658 1.4440
11 .03028 .1172 .3330 .5439 .7863 1.1688 1.4484
12 .03137 .1193 .3357 .5453 .7880 1.1714 1.4521
15 .03424 .1244 .3412 .5500 .7926 1.1773 1.4606
20 .03807 .1298 .3461 .5547 .7975 1.1839 1.4698
30 .04354 .1351 .3509 .5605 .8036 1.1916 1.4801'''


def mm(x):return mp.mpf(x.numerator)/x.denominator if isinstance(x,F) else mp.mpf(x)


def save(out):
    (ROOT/'results/ks.json').write_text(json.dumps(out,indent=2)+'\n')


def probability(n,t,positive=True):
    if t<=0:return t*0
    if t>=n:return t*0+1
    start=floor(t)
    if positive:
        return 1-t*sum(comb(n,k)*(k-t)**k*(t+n-k)**(n-k-1) for k in range(start+1,n+1))/n**n
    return t*sum(comb(n,k)*(k-t)**k*(t+n-k)**(n-k-1) for k in range(start+1))/n**n


def cdf(n,s):return probability(n,mm(s)*mp.sqrt(n))


def volume(n,t):
    # Nested integration of the order-statistic simplex, polynomial coefficients.
    poly=[F(1)]
    for j in range(1,n+1):
        a=max(F(0),j-t)
        new=[F(0)]+[c/F(i+1) for i,c in enumerate(poly)]
        new[0]=-sum(c*a**i for i,c in enumerate(new))
        poly=new
    return sum(c*n**i for i,c in enumerate(poly))*F(factorial(n),n**n)


def statistics(data):
    u=sorted(data);n=len(u)
    return max(F(j+1,n)-x for j,x in enumerate(u)),max(x-F(j,n) for j,x in enumerate(u))


def sup_at_knots(data):
    n=len(data);knots=set(data)
    return (max(F(sum(y<=x for y in data),n)-x for x in knots),
            max(x-F(sum(y<x for y in data),n) for x in knots))


def buckets(data,m,approximate=False):
    n=len(data);a=[F(1)]*m;b=[F(0)]*m;c=[0]*m
    for y in data:
        assert 0<=y<1
        k=int(m*y);a[k]=min(a[k],y);b[k]=max(b[k],y);c[k]+=1
    j=0;rp=rm=F(0)
    for k in range(m):
        if c[k]:
            if approximate:a[k]=b[k]=F(2*k+1,2*m)
            rm=max(rm,a[k]-F(j,n));j+=c[k];rp=max(rp,F(j,n)-b[k])
    return rp,rm


def main():
    if '--resume' in sys.argv:
        out=json.loads((ROOT/'results/ks.json').read_text())
    else:
        out={'status':'partial'}
        tests=0
        for n in range(1,11):
            for j in range(1,5*n):
                t=F(j,5);v=volume(n,t)
                assert v==probability(n,t)==probability(n,t,False),(n,t,v)
                tests+=1
        out['exact_cdf_three_models']=tests;save(out);print('CDF',tests,flush=True)
        x,t=sp.symbols('x t');polys={};symbolic=0
        for n in range(8):
            for k in range(n+1):
                if n==k:actual=x**n/sp.factorial(n)
                else:
                    anti=sp.integrate(polys[n-1,k],x)
                    actual=sp.expand(anti-anti.subs(x,n-t))
                polys[n,k]=actual
                total=0
                for r in range(k+1):
                    if r==n:term=(r-t)**r/sp.factorial(r)
                    else:term=(x+t-n)*(r-t)**r*(x+t-r)**(n-r-1)/(sp.factorial(r)*sp.factorial(n-r))
                    total+=term
                assert sp.expand(actual-total)==0,(n,k)
                symbolic+=1
        out['exercise17_symbolic_polynomials']=symbolic;save(out);print('POLYNOMIALS',symbolic,flush=True)
    entries=[]
    for row in TABLE.splitlines():
        fields=row.split();n=int(fields[0])
        for p,s in zip(['.01','.05','.25','.50','.75','.95','.99'],fields[1:]):
            target=mp.mpf(p);lo=mp.mpf(0);hi=mp.sqrt(n)
            for _ in range(135):
                mid=(lo+hi)/2
                if cdf(n,mid)<target:lo=mid
                else:hi=mid
            q=(lo+hi)/2;half=mp.mpf(5)*mp.mpf(10)**(-len(s.split('.')[1])-1)
            assert abs(q-mp.mpf(s))<=half,(n,p,s,mp.nstr(q,35))
            assert abs(probability(n,q*mp.sqrt(n),False)-target)<mp.mpf('1e-37')
            entries.append(dict(n=n,p=p,printed=s,calculated=mp.nstr(q,40)))
        out['table2']=entries;save(out)
    print('TABLE2',len(entries),flush=True)
    gridcases=0;bucketcases=0
    for den in [4,7]:
        values=[F(j,den) for j in range(den)]
        for n in range(1,8):
            for data in combinations_with_replacement(values,n):
                expected=statistics(data);assert expected==sup_at_knots(data)
                assert statistics([1-x for x in data])==expected[::-1]
                assert all(0<=x<=1 for x in expected)
                for m in [n,n+1,2*n]:
                    assert buckets(data,m)==expected,(data,m)
                    bucketcases+=1
                for m in {1,2,max(1,n//2),n}:
                    approx=buckets(data,m,True)
                    assert all(abs(a-b)<=F(1,2*m) for a,b in zip(approx,expected))
                    bucketcases+=1
                gridcases+=1
    out['algorithm23']=dict(grid_samples=gridcases,bucket_comparisons=bucketcases);save(out);print('BUCKETS',gridcases,bucketcases,flush=True)
    data=[F(s) for s in '.414 .732 .236 .162 .259 .442 .189 .693 .098 .302 .442 .434 .141 .017 .318 .869 .772 .678 .354 .718'.split()]
    plus,minus=statistics(data);assert plus==F(129,500) and minus==F(6,125)
    out['exercise5']=dict(unscaled=[str(plus),str(minus)],statistics=[mp.nstr(mm(d)*mp.sqrt(20),35) for d in [plus,minus]],cdf=[str(probability(20,d*20)) for d in [plus,minus]],cdf_decimal=[mp.nstr(mm(probability(20,d*20)),35) for d in [plus,minus]])
    validation=[]
    for d in [plus,minus]:
        integrated=volume(20,20*d)
        assert integrated==probability(20,20*d)==probability(20,20*d,False)
        validation.append(dict(d=str(d),cdf=str(integrated),independent_nested_integration_equal=True))
    assert probability(20,20*minus)==minus*(1+minus)**19
    out['exercise5']['independent_validation']=validation
    save(out);print('EX5',out['exercise5']['cdf_decimal'],flush=True)
    asym=[]
    for n in [100,400,1600]:
        for s in [mp.mpf('.25'),mp.mpf('.5'),mp.mpf(1),mp.mpf('1.5'),mp.mpf(2)]:
            exact=cdf(n,s)
            approx=1-mp.exp(-2*s*s)*(1-2*s/(3*mp.sqrt(n))+(2*s*s/3-4*s**4/9)/n)
            asym.append(dict(n=n,s=str(s),cdf=mp.nstr(exact,35),scaled_remainder=mp.nstr((exact-approx)*n**mp.mpf('1.5'),25)))
        out['asymptotic20_numeric']=asym;save(out)
    out['status']='all_checks_passed';save(out);print('ALL',flush=True)


if __name__=='__main__':main()
