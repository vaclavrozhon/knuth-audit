"""Checkpointed exact/interval checks for spectral F and exercises25--30."""
import argparse
from collections import Counter,defaultdict
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json
from math import gcd,prod
from pathlib import Path
import time
import mpmath as mp
import sympy as sp

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/spectral-discrepancy.json'
z=sp.Symbol('z');mp.mp.dps=65;mp.iv.dps=65

@lru_cache(None)
def cyclotomic(m):return sp.Poly(sp.cyclotomic_poly(m,z),z)

def root_value(coeff,m):
    p=sp.Poly.from_dict({(k,):v for k,v in coeff.items() if v},z)
    return p.rem(cyclotomic(m)).as_expr()

def squared_sum(exponents,m):
    c=Counter(x%m for x in exponents);out=Counter()
    for i,a in c.items():
        for j,b in c.items():out[(i-j)%m]+=a*b
    return root_value(out,m)

def order(a,m):
    x=a%m;n=1
    while x!=1:x=x*a%m;n+=1;assert n<=m
    return n

def states(a,c,m):
    xs=[];x=0
    while not xs or x!=0:
        xs.append(x);x=(a*x+c)%m
        assert len(xs)<=m
    return xs

def full_period():
    models=gauss=shifts=reductions=0
    for m in range(2,33):
        for a in range(1,m):
            if gcd(a,m)!=1:continue
            for c in sorted({1,m-1}):
                xs=states(a,c,m)
                if len(xs)!=m:continue
                s=order(a,m);b=xs[s%m]
                assert gcd(b,m)==s and b%s==0
                qp=b//s;assert gcd(qp,m)==1
                for k in range(m):
                    exps=[xs[j]+j*k for j in range(m)]
                    expected=m*m//s if (k+qp)%(m//s)==0 else 0
                    assert squared_sum(exps,m)==expected,(m,a,c,k)
                    gauss+=1
                    for ell in [1,m-1]:
                        left=Counter((xs[(j+ell)%m]+j*k)%m for j in range(m))
                        right=Counter((x-ell*k)%m for x in exps)
                        assert left==right;shifts+=1
                for q in range(1,m):
                    d=gcd(q,m);M=m//d;ss=order(a,M)
                    ys=[(q//d*x)%M for x in xs]
                    assert sorted(ys[:M])==list(range(M))
                    assert all(ys[j]==ys[j%M] for j in range(m))
                    assert ss<=s and M*M*s<=m*m*ss
                    reductions+=1
                models+=1
    return dict(models=models,exact_squared_sums=gauss,shift_identities=shifts,
                reduced_moduli=reductions,
                method='Integer cyclotomic remainders of direct squared sums; actual orbits and coefficient-histogram shift identities.')

def endpoints(x):
    def cv(v):
        sign,mantissa,exponent,_=v
        return Q((-1)**sign*mantissa)*Q(2)**exponent
    return tuple(map(cv,x._mpi_))

def interval_json(x):return [str(v) for v in endpoints(x)]

def weights(m):
    return [mp.iv.mpf(1)]+[1/(m*mp.iv.sin(mp.iv.pi*k/m)) for k in range(1,m)]

def csc_sums():
    models=0
    for m in range(2,129):
        r=weights(m)
        for d in sp.divisors(m):
            L=m//d;rr=weights(L);f=sum(rr[1:L//2+1],mp.iv.mpf(0))
            bound=2+2*f/d
            for q in range(d):
                val=sum(r[q::d],mp.iv.mpf(0))
                assert endpoints(val)[1]<endpoints(bound)[0]
                models+=1
    asymptotics=[]
    for m in [10,100,1000,10000]:
        r=weights(m);f=sum(r[1:m//2+1],mp.iv.mpf(0))
        integral=-mp.iv.log(mp.iv.tan(mp.iv.pi/(2*m)))/mp.iv.pi
        gap=f-integral
        residual=gap-mp.iv.euler/mp.iv.pi
        assert endpoints(gap)[0]>Q(18,100)
        lo,hi=endpoints(residual);assert -Q(1,m)<lo<hi<Q(1,m)
        total=sum(r,mp.iv.mpf(0))
        corrected=2/mp.iv.pi*(mp.iv.log(m)+mp.iv.euler+mp.iv.log(2/mp.iv.pi))+1
        printed=2/mp.iv.pi*(mp.iv.log(m)+1+mp.iv.log(2/mp.iv.pi))+1
        asymptotics.append(dict(m=m,f=interval_json(f),integral_gap=interval_json(gap),
                corrected_residual=interval_json(total-corrected),printed_residual=interval_json(total-printed)))
    return dict(residue_class_models=models,asymptotics=asymptotics,
                limiting_integral_gap=interval_json(mp.iv.euler/mp.iv.pi),
                limiting_printed_residual=interval_json(2*(mp.iv.euler-1)/mp.iv.pi),
                scope='65-decimal outward intervals. General asymptotic proof is in the accompanying note, not inferred from four sizes.')

def rho(x,m):return min(x%m,(-x)%m) if x%m else 1
def class_index(x,m):
    if x==0:return 0
    return rho(x,m).bit_length()*(1 if 2*x<=m else -1)
def ell(x):return 2**max(0,abs(x)-1)
def trunc(u,m,mu):
    v=list(u)
    for _ in range(mu):
        for j,x in enumerate(v):
            if rho(x,m)>1:
                v[j]=x//2 if 2*x<=m else m-(m-x)//2
                break
    return tuple(v)

def dyadic():
    models=vectors=classes=0;largest_mu=0
    for t,limit in [(2,64),(3,24),(4,10)]:
        for m in range(2,limit+1):
            for a in range(1,m):
                if gcd(a,m)!=1:continue
                powers=[pow(a,j,m) for j in range(t)]
                bad=[]
                for tail in product(range(m),repeat=t-1):
                    u=tuple([(-sum(x*y for x,y in zip(tail,powers[1:])))%m])+tail
                    if any(u):bad.append(u)
                pm=min(prod(rho(x,m) for x in u) for u in bad)
                mu=pm.bit_length()-1;largest_mu=max(largest_mu,mu)
                groups=defaultdict(list)
                for u in bad:groups[tuple(class_index(x,m) for x in u)].append(u)
                for L,us in groups.items():
                    keys=[trunc(u,m,mu) for u in us]
                    assert len(keys)==len(set(keys))
                    assert len(us)<=max(1,prod(ell(x) for x in L)//2**mu)
                    for u in us:
                        assert all(ell(li)<=rho(x,m)<2*ell(li) for li,x in zip(L,u))
                        k=sum(x!=0 for x in u);assert k>=2
                        length=sum(rho(x,m)**2 for x in u if x)
                        product_squared=prod(rho(x,m)**2 for x in u if x)
                        assert product_squared>=length-k+1
                        assert 4**k*product_squared>=8*length
                vectors+=len(bad);classes+=len(groups);models+=1
    return dict(models=models,bad_vectors=vectors,classes=classes,largest_mu=largest_mu,
                square_typo_example=dict(m=2,a=1,u=[1,1],squared_norm=2,nonzero_components=2),
                scope='Exact congruence enumeration, dyadic fiber injectivity and class counts; norm-product bounds entirely integral.')

def primitive_gauss():
    models=sums=polynomials=0;zero=[]
    for p in [2,3,5,7,11,13]:
        for a in range(1,p):
            if order(a,p)!=p-1:continue
            xs=[pow(a,j,p) for j in range(p-1)]
            M=p*(p-1)
            for k in range(p-1):
                exps=[x*(p-1)+j*k*p for j,x in enumerate(xs)]
                val=squared_sum(exps,M)
                assert val==(1 if k==0 else p)
                sums+=1
            zero.append(dict(p=p,a=a,k=0,squared=1));models+=1
        if p<=11:
            for t in [2,3,4]:
                for u in product(range(p),repeat=t):
                    if not any(u):continue
                    roots=sum(sum(u[j]*pow(a,j,p) for j in range(t))%p==0 for a in range(1,p))
                    assert roots<=t-1
                    polynomials+=1
    return dict(models=models,exact_squared_sums=sums,zero_frequency=zero,
                polynomial_root_bounds=polynomials,
                scope='Direct mixed-root sums reduced modulo the cyclotomic polynomial of order p(p-1). Trivial multiplicative character has magnitude1, not sqrt(p).')

def cf_products():
    models=0;boundary_equal=0
    for m in range(2,161):
        for a in range(1,m):
            if gcd(a,m)!=1:continue
            ds=[];u,v=m,a
            while v:ds.append(u//v);u,v=v,u%v
            qs=[1];ps=[0];pm,pn=1,0;qm,qn=0,1
            for d in ds[:-1]:
                pm,pn=pn,d*pn+pm;qm,qn=qn,d*qn+qm
                ps.append(pn);qs.append(qn)
            via_cf=min(q*abs(a*q-m*p) for q,p in zip(qs,ps))
            direct=min(q*min(a*q%m,(-a*q)%m) for q in range(1,m))
            assert via_cf==direct
            A=max(ds);assert A*direct<=m<(A+2)*direct
            boundary_equal+=int(A*direct==m);models+=1
    return dict(models=models,lower_ratio_equalities=boundary_equal,
                scope='Independent all-denominator product minimum versus convergents; exact A<=m/min_product<A+2.')

def combined():
    m1,m2=2**31-1,2**31-249;m=m1*m2
    a=1431853894371298687;cases=0
    assert a%m1==48271 and a%m2==40692
    for seed in [(1,1),(1,2),(m1-1,m2-1),(17,29)]:
        x,y=seed;w=(x*m2-y*m1)%m
        for n in range(1000):
            u=(Q(x,m1)-Q(y,m2))%1;zz=(x-y)%m1
            assert u==Q(w,m)
            error=Q((m2-m1)*y,m)
            assert (u-Q(zz,m1)-error).denominator==1
            circular=(u-Q(zz,m1))%1
            assert min(circular,1-circular)<=Q((m1-m2)*(m2-1),m)
            x,y,w=48271*x%m1,40692*y%m2,a*w%m;cases+=1
    table=json.loads((ROOT/'results/spectral-table.json').read_text());cf=[]
    for row,A in [('8',3),('13',2)]:
        d=table['rows'][row];u,v=d['m'],d['a'];digits=[]
        while v:digits.append(u//v);u,v=v,u%v
        assert max(digits)==A
        cf.append(dict(row=int(row),digits=digits,max_quotient=A))
    return dict(exact_states=cases,table_quotients=cf,
                coefficient=str(Q(m1-m2,m)),max_circular_error=str(Q((m1-m2)*(m2-1),m)),
                wrap_example=dict(X0=1,Y0=1,Z0=0,U0=str(1-Q(m1-m2,m))),
                scope='Exercise32: exact CRT and circular approximation. Ordinary absolute closeness fails at wraparound, already signaled by modulo1 in the answer; not classified separately as an error.')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    r=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}
    for key,fun in [('full_period',full_period),('csc_sums',csc_sums),('dyadic',dyadic),('primitive_gauss',primitive_gauss),('cf_products',cf_products),('combined',combined)]:
        if key in r:continue
        start=time.monotonic();r[key]=fun();r[key]['seconds']=time.monotonic()-start
        OUT.write_text(json.dumps(r,indent=2)+'\n');print(key,'complete',r[key]['seconds'],flush=True)
