"""Independent checks for TAOCP 3.4.1 D/E and exercise 16.

General distribution proofs are in notes/distributions-other.md.
This checks exact derivative/Jacobian identities and certifies the two
printed rejection-cost bounds. Completed blocks are checkpointed.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
import sys
import mpmath as mp
import sympy as s

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/distributions-other.json'
I = mp.iv
I.dps = 70
mp.mp.dps = 80


def as_q(t):
    sign, mantissa, exponent, _ = t
    return (-1 if sign else 1)*Q(mantissa)*Q(2)**exponent


def bounds(v):
    return tuple(as_q(t) for t in v._mpi_)


def serial(v):
    lo, hi = bounds(v)
    return dict(enclosure=[str(lo), str(hi)],
                decimal=mp.nstr((mp.mpf(lo.numerator)/lo.denominator+mp.mpf(hi.numerator)/hi.denominator)/2, 35))


def iq(v):
    v = Q(v)
    return I.mpf(v.numerator)/v.denominator


def interval(lo, hi):
    return I.mpf([iq(lo).a, iq(hi).b])


def exponential():
    # Mixture weights are L^k/k!, with L=ln 2; k=1 uses the old U.
    L, z = s.symbols('L z', positive=True)
    terms = []
    for k in range(1, 17):
        # Compare differentiated minimum CDF with the shifted-exp series.
        density = L**k/s.factorial(k)*k/L*(1-z/L)**(k-1)
        assert s.simplify(density-(L-z)**(k-1)/s.factorial(k-1)) == 0
        terms.append(k)
    # Table length sufficient for representative binary precisions.
    rows = []
    log2 = I.log(2)
    for t in [8, 16, 24, 32, 53, 64, 128]:
        threshold = Q(1)-Q(1, 2**t)
        total = I.mpf(0)
        term = I.mpf(1)
        k = 0
        while bounds(total)[0] <= threshold:
            previous = total
            k += 1
            term *= log2/k
            total += term
        assert bounds(previous)[1] < threshold
        rows.append(dict(bits_after_shift=t, last_k=k, Qk=serial(total)))
    return dict(series_coefficients=len(terms), table_lengths=rows,
                expected_new_uniforms=serial(1+log2),
                proof='Sum of minimum densities is exp(L-z)=2 exp(-z); independent geometric block mass is 2^(-j-1). Finite words require a trailing-zero convention in S1.')


def gamma_bounds():
    k, y, b = s.symbols('k y b', positive=True)
    derivative = 2*y/(1+y*y)+b*k/(k+b*y)-b
    target = -y*(b*y-1)**2/((1+y*y)*(k+b*y))
    numerator = s.together(derivative-target).as_numer_denom()[0]
    assert s.rem(s.Poly(numerator,b),s.Poly(b*b-2*k-1,b)) == 0
    # The sign proof applies also to negative y when k+b*y>0.
    cost_at_three = 2*I.pi*I.sqrt(5)/I.e**2
    assert bounds(cost_at_three)[1] < Q('1.902')
    # Mean cost decreases for k>=2 by the analytic psi bound in the notes.
    psi_margin = 1/(2*k)-1/(12*k*k)-1/(2*k+1)
    assert s.factor(psi_margin) == (4*k-1)/(12*k*k*(2*k+1))
    # Cover all 0<=a<=1, including interval gamma's minimum.
    grid = []
    for j in range(200):
        a = interval(Q(j,200),Q(j+1,200))
        cost = (a+I.e)/(I.e*I.gamma(a+1))
        assert bounds(cost)[1] < Q('1.4'), (j,serial(cost))
        grid.append(dict(a=[str(Q(j,200)),str(Q(j+1,200))],cost=serial(cost)))
    root = mp.findroot(lambda a:1/(a+mp.e)-mp.digamma(a+1),(.7,.9))
    return dict(large_shape_cost_at_a3=serial(cost_at_three),
                small_shape_cover=grid,
                maximum_numerical_locator=dict(a=mp.nstr(root,35),cost=mp.nstr((root+mp.e)/(mp.e*mp.gamma(root+1)),35)),
                proof='A proposal log ratio has derivative -y*(b*y-1)^2/((1+y^2)*(k+b*y)); b^2=2k+1. Strict cost monotonicity for k>=2 is analytic. Small-shape bound certified on 200 covering intervals; numerical root is only explanatory.')


def transformations():
    # Gamma sum/ratio Jacobian and the Jöhnk construction share x=r*t,y=r*(1-t).
    r,t=s.symbols('r t',positive=True)
    J=s.Matrix([[s.diff(r*t,r),s.diff(r*t,t)],
                [s.diff(r*(1-t),r),s.diff(r*(1-t),t)]]).det()
    assert J == -r
    # Student alternative after the 1999 repair, k=nu-2.
    nu,x=s.symbols('nu x',positive=True)
    k=s.symbols('k',positive=True)
    inverse=s.sqrt(k)*x/s.sqrt(nu+x*x)
    derivative=s.sqrt(k)*nu/(nu+x*x)**s.Rational(3,2)
    assert s.simplify(s.diff(inverse,x)-derivative)==0
    assert s.simplify(1-inverse**2/k-nu/(nu+x*x))==0
    # F distribution from beta, parameters A=nu1/2, B=nu2/2.
    n1,n2=s.symbols('n1 n2',positive=True)
    beta_inverse=n1*x/(n2+n1*x)
    assert s.simplify(s.diff(beta_inverse,x)-n1*n2/(n2+n1*x)**2)==0
    # The three-dimensional disk-to-sphere map has z=2S-1 and radius²=4S(1-S).
    S=s.symbols('S',real=True)
    assert s.expand(4*S*(1-S)+(2*S-1)**2)==1
    # Check moments of the beta law and order statistic by independent
    # exact polynomial integration for all integer shapes 1..12.
    z=s.symbols('z')
    cases=0
    for a in range(1,13):
        for b in range(1,13):
            n=a+b-1
            density=s.Poly(factorial(n)//(factorial(a-1)*factorial(b-1))*z**(a-1)*(1-z)**(b-1),z)
            coeff={power[0]:Q(int(coef)) for power,coef in density.terms()}
            for moment in range(4):
                value=sum(c/Q(power+moment+1) for power,c in coeff.items())
                expected=Q(1)
                for j in range(moment):expected*=Q(a+j,a+b+j)
                assert value==expected
                cases+=1
    return dict(symbolic_jacobians=4,beta_order_statistic_moments=cases,
                scope='Exact identities supplement the general density proofs, including the repaired Student denominator 1-2/nu.')


def main():
    out=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('exponential',exponential),('gamma_bounds',gamma_bounds),('transformations',transformations)]:
        if name in out:continue
        print('START',name,flush=True)
        out[name]=fn()
        OUT.write_text(json.dumps(out,indent=2)+'\n')
        print('PASS',name,flush=True)


if __name__=='__main__':main()
