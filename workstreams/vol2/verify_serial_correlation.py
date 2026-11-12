"""TAOCP 3.3.2 K and exercises17--20: exact algebra and counterexamples."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial, prod
from pathlib import Path
import json
import sys
import sympy as s
import mpmath as mp

ROOT = Path(__file__).resolve().parent
DEST = ROOT/'results/serial-correlation.json'


def algebra():
    cases = 0
    for n in range(2,7):
        u = s.symbols('u:'+str(n))
        v = s.symbols('v:'+str(n))
        uu,vv = sum(x*x for x in u),sum(x*x for x in v)
        uv = sum(x*y for x,y in zip(u,v))
        assert s.expand(uu*vv-uv*uv-sum((u[i]*v[j]-u[j]*v[i])**2
                                      for i in range(n) for j in range(i+1,n)))==0
        den = n*uu-sum(u)**2
        assert s.expand(den-sum((u[i]-u[j])**2 for i in range(n) for j in range(i+1,n)))==0
        cases += 2
    rows = []
    for n in range(3,9):
        u = s.symbols('u:'+str(n));s1=sum(u);s2=sum(x*x for x in u)
        x = sum(u[i]*u[(i+1)%n] for i in range(n))
        def types(poly):
            out = Counter()
            for exponents,coefficient in s.Poly(s.expand(poly),*u).terms():
                out[tuple(sorted((i for i in exponents if i),reverse=True))] += coefficient
            return {key:val for key,val in out.items() if val}
        def expected(e4=0,e31=0,e22=0,e211=0,e1111=0):
            return {a:b for a,b in [((4,),e4),((3,1),e31),((2,2),e22),
                                    ((2,1,1),e211),((1,1,1,1),e1111)] if b}
        assert types(s2*s2)==expected(e4=n,e22=n*(n-1))
        assert types(s2*s1*s1)==expected(e4=n,e31=2*n*(n-1),e22=n*(n-1),e211=n*(n-1)*(n-2))
        assert types(s1**4)==expected(e4=n,e31=4*n*(n-1),e22=3*n*(n-1),e211=6*n*(n-1)*(n-2),e1111=n*(n-1)*(n-2)*(n-3))
        assert types(x*x)==expected(e22=n,e211=2*n,e1111=n*(n-3))
        assert types(x*s1*s1)==expected(e31=2*n,e22=2*n,e211=5*n*(n-2),e1111=n*(n-2)*(n-3))
        assert types((u[0]-u[1])**4)==expected(e4=2,e31=-8,e22=6)
        rows.append(n)
    return dict(binet_and_denominator_identities=cases,all_six_fourth_degree_expansions_n=rows)


def exchangeability():
    cases = models = 0
    rows = []
    for n in range(2,11):
        grouped = defaultdict(lambda:[0,Q(0),Q(0),Q(0)])
        for u in product([0,1,3],repeat=n):
            s1=sum(u);s2=sum(x*x for x in u);den=n*s2-s1*s1
            if not den:
                continue
            num=n*sum(u[i]*u[(i+1)%n] for i in range(n))-s1*s1
            rho=Q(num,den)
            key=tuple(sorted(u))
            g=grouped[key];g[0]+=1;g[1]+=rho;g[2]+=rho*rho;g[3]+=Q((u[0]-u[1])**4,den*den)
            cases += 1
        for u,(count,first,second,fourth) in grouped.items():
            mean=first/count;variance=second/count-mean*mean
            assert mean==Q(-1,n-1)
            if n>2:
                assert variance==Q(n*n,(n-1)**2*(n-2))-Q(n**3,2*(n-2))*fourth/count
                centered=[n*x-sum(u) for x in u]
                kurtosis=Q(sum(x**4 for x in centered),sum(x*x for x in centered)**2)
                assert variance==Q(n*n-3*n+3,(n-1)**2*(n-2))-Q(n,(n-1)*(n-2))*kurtosis
            else:
                assert variance==0
            models += 1
        rows.append(dict(n=n,multisets=len(grouped)))
    return dict(sequences=cases,multiset_models=models,by_length=rows)


def gaussian():
    determinants=[];moments=[]
    w,z=s.Rational(1,20),s.Rational(1,30)
    for n in range(3,21):
        shift=s.zeros(n)
        for i in range(n):shift[i,(i+1)%n]=1
        projection=s.eye(n)-s.ones(n)/n
        b=(shift+shift.T)/2-s.ones(n)/n
        den=(s.eye(n)-2*w*b-2*z*projection).det(method='domain-ge')
        a=1-2*z
        independent=2*w**n*(s.chebyshevt(n,a/(2*w))-1)/(a-2*w)
        assert den==independent
        determinants.append(dict(n=n,determinant=str(den)))
        coefs=[s.S.One]
        logs=[]
        power=s.eye(n)
        row=[]
        for r in range(1,min(8,n-1)+1):
            power=power*b
            trace=s.trace(power)
            walk=s.Rational(n,2**r)*sum(comb(r,j) for j in range(r+1) if (r-2*j)%n==0)-1
            assert trace==walk
            logs.append(s.Rational(2**(r-1),r)*trace)
            coefs.append(s.expand(sum(k*logs[k-1]*coefs[r-k] for k in range(1,r+1))/r))
            moment=s.factor(factorial(r)*coefs[r]/(2**r*s.rf(s.Rational(n-1,2),r)))
            k=(r+1)//2
            even=s.rf(s.Rational(1,2),k)/s.rf(s.Rational(n+1,2),k)
            want=even if r%2==0 else -s.Rational(n+1,n-1)*even
            assert moment==want
            if n==3:assert moment==s.Rational(-1,2)**r
            if n==4:assert moment==s.Rational((-1)**r,2*r+1)
            row.append(str(moment))
        moments.append(dict(n=n,powers_starting_at1=row))
    return dict(exact_determinants=determinants,exact_spherical_moments=moments,
                printed_origin_value_n4='1/4, must be 1',
                printed_moments_n3=['-1/5','1/7'],correct_moments_n3=['-1/2','1/4'])


def log_interval(n,terms=110):
    """Rational log enclosure from 2*atanh((y-1)/(y+1))."""
    def atanh(u):
        total=2*sum(u**(2*j+1)/Q(2*j+1) for j in range(terms))
        remainder=2*u**(2*terms+1)/((2*terms+1)*(1-u*u))
        return total,total+remainder
    k=n.bit_length()-1
    lo2,hi2=atanh(Q(1,3))
    y=Q(n,2**k)
    lo,hi=atanh((y-1)/(y+1))
    return k*lo2+lo,k*hi2+hi


def concentration():
    mp.mp.dps=80
    rows=[]
    scale=10**50
    for k in [10,100,1000]:
        root=mp.findroot(lambda x:x/mp.log(x)-k**3,(k**3*mp.log(k),10*k**3*mp.log(k)))
        n=int(mp.ceil(root))
        lo,hi=log_interval(n);prevlo,prevhi=log_interval(n-1)
        assert Q(n,1)/hi>k**3 and Q(n-1,1)/prevlo<k**3
        lowcube,highcube=lo/n,hi/n
        assert Q(1,(k+1)**3)<lowcube<highcube<Q(1,k**3)
        flo=int(s.integer_nthroot(lowcube.numerator*scale**3//lowcube.denominator,3)[0])
        fhi=int(s.integer_nthroot(highcube.numerator*scale**3//highcube.denominator,3)[0])+1
        dl,dh=Q(flo,scale),Q(fhi,scale)
        assert dl**3<=lowcube and dh**3>=highcube
        lowerlo,lowerhi=dl*(1-dl),dh*(1-dh)
        p=Q(1,k+1)
        delta=(mp.log(n)/n)**(mp.mpf(1)/3)
        normalized=(mp.mpf(n)*p.numerator/p.denominator-n*delta*(1-delta))/mp.sqrt(n*mp.mpf(p.numerator)/p.denominator*(1-mp.mpf(p.numerator)/p.denominator))
        rows.append(dict(k=k,n=n,m=k+1,delta_lower=str(dl),delta_upper=str(dh),
                         lower_probability_bound=[str(lowerlo),str(lowerhi)],
                         mean_minus_lower_in_standard_deviations=str(normalized)))
    return dict(alpha=1,M='5/6',certified_ceiling=True,examples=rows,
                proof='Along these ceilings the standardized lower threshold tends to0; binomial CLT makes one-cell failure tend to1/2.')


def fft_check():
    import numpy as np
    rows=[]
    for n in [2,4,8,16,32,64,128,256]:
        u=np.array([(j*j+3*j+7)%23 for j in range(n)],dtype=float)
        transformed=np.fft.ifft(np.abs(np.fft.fft(u))**2).real
        direct=np.array([sum(u[j]*u[(j+q)%n] for j in range(n)) for q in range(n)])
        assert np.max(np.abs(transformed-direct))<1e-8
        rows.append(dict(n=n,maximum_error=float(np.max(np.abs(transformed-direct)))))
    return rows


def main():
    out=json.loads(DEST.read_text()) if '--resume' in sys.argv and DEST.exists() else {}
    for name,fn in [('algebra',algebra),('exchangeability',exchangeability),
                    ('gaussian',gaussian),('concentration',concentration),('fft',fft_check)]:
        if name in out:continue
        print('START',name,flush=True);out[name]=fn()
        DEST.write_text(json.dumps(out,indent=2)+'\n');print('PASS',name,flush=True)
    print('ALL BLOCKS COMPLETE',flush=True)


if __name__=='__main__':main()
