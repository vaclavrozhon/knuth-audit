#!/usr/bin/env python3
"""Exact algebra and separate numerical checks for TAOCP4.5.2-23--29.

Uses saved fixed-point results; never repeats that computation. Floating
checks are diagnostics, not interval certificates. General proofs are in
notes/gcd-model.md.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial
import json, sys, time
import sympy as s
from sympy.functions.combinatorial.numbers import stirling
import mpmath as mp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/gcd-model.json'


def algebra():
    x, t = s.symbols('x t', positive=True)
    S = s.Function('S')
    G = lambda z: S(1/z)-S(z)
    lhs = 2*G(x)-5*G(2*x)+2*G(4*x)
    # G(1+2t)=S(2t)-2S(t), obtained by splitting the defining sum.
    translated = lambda z: S(2*z)-2*S(z)
    rhs = translated(x)-2*translated(2*x)+2*translated(1/(2*x))-translated(1/(4*x))
    assert s.expand(lhs-rhs) == 0
    phi = (1+s.sqrt(5))/2
    assert s.simplify(1+2*phi-phi**3) == 0
    assert s.simplify(1+1/phi-phi) == 0
    assert s.simplify(1+1/(2*phi)-phi**2/2) == 0
    assert s.simplify(1+4*phi-2*phi**2) != 0
    # The involution in exercise25 must hold for any odd analytic series.
    N = 16
    lam = [F(0)] + [F((-1)**((j-1)//2), j*j+1) if j%2 else F(0) for j in range(1,N+1)]
    rho = [F(0)] + [(-1)**n*sum(F(int(stirling(n,k,kind=1))*factorial(k),factorial(n))*lam[k] for k in range(1,n+1)) for n in range(1,N+1)]
    for n in range(1,N+1):
        back = -sum(F(int(stirling(n,k,kind=2))*factorial(k),factorial(n))*rho[k] for k in range(1,n+1))
        assert back == lam[n]
    assert rho[2] == lam[1]/2
    assert -rho[3] == lam[1]/3+lam[3]
    assert rho[4] == lam[1]/4+F(3,2)*lam[3]
    assert -rho[5] == lam[1]/5+F(7,4)*lam[3]+lam[5]
    # Exact preimages of X'=min(2^k X/(1-X),(1-X)/(2^k X)).
    cases = 0
    for k in range(1,9):
        for den in range(2,19):
            for num in range(1,den):
                X=F(num,den);Y=min(2**k*X/(1-X),(1-X)/(2**k*X))
                for threshold in [F(1,17),F(1,3),F(2,3),F(1)]:
                    a=threshold/(2**k+threshold);b=1/(1+2**k*threshold)
                    assert (Y>=threshold) == (a<=X<=b)
                    cases+=1
    return dict(stirling_orders=N,exact_preimage_cases=cases,
                functional_identity=True,golden_ratio_correct_rhs='-2*G(1+4*phi)',
                golden_ratio_printed_rhs='2*G(2*phi**2)')


def psi_coefficients():
    # This triangular recurrence follows directly from equation55.
    p=[F(0),F(1)]
    assert s.bernoulli(1)==s.Rational(1,2)
    for n in range(2,65):
        p.append(sum(comb(n-1,j-1)*p[j] for j in range(1,n))/(2*(2**n-1)))
    for n in range(1,65):
        bern=sum((-1)**k*F(s.bernoulli(k))*comb(n,k)/F(2**(k+1)-1) for k in range(n))/(2*n)+(F(1,2) if n==1 else 0)
        assert bern==p[n],(n,bern,p[n])
        assert p[n]>0
    assert p[2]==F(1,6) and p[3]==F(2,21)
    # A finite literal sum, with a rigorous remaining geometric bound.
    mp.mp.dps=60
    checks=[]
    for n in [1,2,3,7,16]:
        partial=sum(F(sum(a**(n-1) for a in range(2**j)),2**(j*(n+1)+1)) for j in range(13))
        assert 0<=p[n]-partial<=F(1,2**13)
        checks.append(dict(n=n,coefficient=str(p[n]),tail=str(p[n]-partial)))
    return dict(exact_coefficients=64,literal_sum_checks=checks,
                convention='Bernoulli B1=+1/2; corrected formula includes(-1)^k')


def saved_distribution():
    mp.mp.dps=60
    d=json.loads((ROOT/'results/gcd-distribution.json').read_text())
    expected={'1':'.3979226812','3':'-.0210096400','5':'.0013749841','7':'-.0000960351'}
    for row in d.values():
        assert row['diagnostics'][-1]['iteration']==45
        assert mp.mpf(row['diagnostics'][-1]['max_change'])<mp.mpf('1e-17')
        assert abs(mp.mpf(row['S1'])-mp.mpf('.5432582959'))<mp.mpf('5e-11')
        for k,w in expected.items():
            assert abs(mp.mpf(row['odd_coefficients'][k])-mp.mpf(w))<mp.mpf('5e-11')
    diff={k:mp.nstr(abs(mp.mpf(d['2048']['odd_coefficients'][k])-mp.mpf(d['4096']['odd_coefficients'][k])),8) for k in expected}
    for v in diff.values():assert mp.mpf(v)<mp.mpf('2e-14')
    # Brent1999 p12 values visually transcribed, not claimed independently
    # certified to40 digits by our lower precision calculation.
    K=mp.mpf('.7059712461019163915293141358528817666677')
    lam=mp.mpf('.3979226811883166440767071611426549823098')
    assert abs(mp.mpf(d['4096']['two_over_b'])-K)<mp.mpf('2e-18')
    assert abs(mp.mpf(d['4096']['odd_coefficients']['1'])-lam)<mp.mpf('2e-18')
    return dict(reused='gcd-distribution.json',two_grid_coefficient_differences=diff,
                S1=d['4096']['S1'],scope='Floating diagnostics; not a rigorous interval certificate.')


def mellin():
    mp.mp.dps=80
    ln2=mp.log(2);c=2*mp.pi**2/ln2
    f=lambda x:sum(mp.power(2,-k)/(1+mp.power(2,k)*x) for k in range(1,301))
    phi=lambda x:sum(1/(mp.power(2,k)+x) for k in range(1,301))
    P=lambda t:(2*mp.pi/ln2)*sum(mp.sin(2*mp.pi*m*t)/mp.sinh(m*c) for m in range(1,9))
    bound=(4*mp.pi/ln2)*mp.exp(-c)/((1-mp.exp(-c))*(1-mp.exp(-2*c)))
    assert bound<mp.mpf('8e-12')
    cases=[]
    for x in [mp.mpf(1)/7,mp.mpf(1)/3,mp.sqrt(2)/4,mp.power(2,-20),mp.mpf(1),mp.sqrt(2),mp.mpf(3),mp.mpf(100)]:
        direct=f(x)-f(1/x)
        closed=x*mp.log(x,2)+x/2+x*P(mp.log(x,2))-x*x/(1+x)+(1-x*x)*phi(x)
        error=abs(direct-closed)
        assert error<mp.mpf('1e-72'),(x,error)
        assert abs(f(1/x)-(1-phi(x)))<mp.mpf('1e-76')
        cases.append(dict(x=mp.nstr(x,20),error=mp.nstr(error,8)))
    return dict(cases=cases,periodic_absolute_bound=mp.nstr(bound,30),
                scope='80-digit floating evaluation; omitted series tails below1e-86 for these inputs.')


def asymptotic():
    mp.mp.dps=70;ln2=mp.log(2)
    tau=lambda x:sum(mp.power(4,-j)/mp.expm1(x/mp.power(2,j)) for j in range(1,251))
    rem=lambda x:sum(mp.power(4,r)/mp.expm1(mp.power(2,r)*x) for r in range(12))
    def Q(x):
        return (mp.zeta(2)+2*sum(mp.re(mp.zeta(2+2j*mp.pi*k/ln2)*mp.gamma(2+2j*mp.pi*k/ln2)*mp.exp(-2j*mp.pi*k*mp.log(x,2))) for k in range(1,11)))/ln2
    rows=[]
    for n in [1,2,3,8,32,100]:
        t=tau(mp.mpf(n));r=rem(mp.mpf(n));q=Q(mp.mpf(n))/n**2
        assert abs(4*tau(2*mp.mpf(n))-t-1/mp.expm1(n))<mp.mpf('1e-65')
        assert abs(q-t-r)<mp.mpf('1e-60'),(n,q-t-r)
        rows.append(dict(n=n,tau=mp.nstr(t,30),omitted_remainder=mp.nstr(r,30),error=mp.nstr(q-t-r,8)))
    # The printed S estimate is not uniform in m. A general bound includes
    # q(1+q)/(1-q)^3; both sides are evaluated with high precision here.
    inequalities=0;nonuniform=[]
    for n in [1,2,3,8,32,100]:
        for m in [2,4,16,256,1024]:
            S=sum((1-mp.mpf(k)/m)**n for k in range(1,m))
            q=mp.exp(-mp.mpf(n)/m);T=q/(1-q)
            upper=2*mp.mpf(n)/m**2*q*(1+q)/(1-q)**3
            assert 0<=T-S<=upper;inequalities+=1
            if m==1024:nonuniform.append(dict(n=n,ratio_to_printed_error=mp.nstr((T-S)/(q*n/m**2),15)))
    return dict(mellin_rows=rows,uniform_bound_cases=inequalities,
                nonuniform_diagnostics=nonuniform,
                exact_correction='tau(x)=x^-2 Q(log2 x)-sum_{r>=0}4^r/(exp(2^r*x)-1)',
                scope='General proof and bounds in notes/gcd-model.md; numerical checks are diagnostics.')


if __name__=='__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('algebra',algebra),('psi_coefficients',psi_coefficients),('saved_distribution',saved_distribution),('mellin',mellin),('asymptotic',asymptotic)]:
        if name in data:continue
        start=time.monotonic();value=fn()
        data[name]=dict(status='passed',seconds=time.monotonic()-start,result=value)
        OUT.write_text(json.dumps(data,indent=2)+'\n')
        print(name,'passed',round(data[name]['seconds'],3),flush=True)
