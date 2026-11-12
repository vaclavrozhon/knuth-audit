"""Exact coefficient/transcription checks for TAOCP 1.2.11.3.

General error estimates and identities are proved in notes/asymptotic-*.md.
The Ramanujan inequality has its separate complete certificate.
"""
from collections import Counter
from datetime import datetime, timezone
from math import comb, factorial
from pathlib import Path
import json
import sympy as s

ROOT=Path(__file__).resolve().parent
COUNTS=Counter()


def check(condition, category):
    assert condition, category
    COUNTS[category]+=1


def exponential_coefficients(exponent, last):
    out=[s.Integer(1)]
    for j in range(1,last+1):
        out.append(s.expand(sum(k*exponent.get(k,0)*out[j-k] for k in range(1,j+1))/j))
    return out


def gaussian_integral(poly, t):
    return s.simplify(sum(c*2**s.Rational(j[0]-1,2)*s.gamma(s.Rational(j[0]+1,2))
                          for j,c in s.Poly(poly,t).terms()))


def main():
    u,w,e,t,a,y=s.symbols('u w e t a y')
    base=sum(2*s.Rational((-1)**j,j+2)*u**j for j in range(7))
    c=[s.Integer(0)]+[s.series(base**(-s.Rational(k,2)),u,0,k).removeO().coeff(u,k-1)/k for k in range(1,7)]
    wanted=[0,1,s.Rational(1,3),s.Rational(1,36),-s.Rational(1,270),s.Rational(1,4320),s.Rational(1,17010)]
    for k in range(1,7): check(c[k]==wanted[k],'inverse_coefficients')
    inverse=sum(c[k]*w**k for k in range(1,7))
    composed=s.series(2*(inverse-s.log(1+inverse))-w*w,w,0,8).removeO()
    check(s.expand(composed)==0,'inverse_composition')
    forward=s.series(u*s.sqrt(base),u,0,6).removeO()
    check(s.expand(forward-(u-u*u/3+7*u**3/36-73*u**4/540+1331*u**5/12960))==0,'forward_coefficients')

    root=s.sqrt(s.pi/2)
    q=s.expand(-1+sum(k*c[k]*s.gamma(s.Rational(k,2))*2**(s.Rational(k,2)-1)*e**(k-2) for k in range(1,6)))
    q_print=root/e-s.Rational(1,3)+root*e/12-s.Rational(4,135)*e**2+root*e**3/288
    check(s.simplify(q-q_print)==0,'Q_from_Watson')
    r=s.expand(2*root/e*(1+e**2/12+e**4/288)-q)
    r_print=root/e+s.Rational(1,3)+root*e/12+s.Rational(4,135)*e**2+root*e**3/288
    check(s.simplify(r-r_print)==0,'R_from_exact_identity')
    I2=y-y**3*e**2/6+(y**4/12+y**5/40)*e**4
    norm=e/s.sqrt(2*s.pi)*(1-e**2/12+e**4/288)
    A=s.series(1+norm*(I2-(q+1)),e,0,5).removeO().expand()
    A_print=s.Rational(1,2)+(y-s.Rational(2,3))*e/s.sqrt(2*s.pi)+(s.Rational(23,270)-y/12-y**3/6)*e**3/s.sqrt(2*s.pi)
    check(s.simplify(A-A_print)==0,'Theorem_A_and_integer_power_cancellation')

    # Discrete saddle expansion: integrate polynomial coefficients, then
    # independently add the Euler endpoint/derivative corrections.
    terms=exponential_coefficients({j:-a*t**j/j-t**(j+2)/(j+2) for j in range(1,5)},4)
    integrals=[gaussian_integral(p,t) for p in terms]
    half=sum(integrals[j]*e**(j-1) for j in range(5))+s.Rational(1,2)
    for j,p in enumerate(terms):
        for k in [1,2]:
            if j+2*k-1<=3:
                coef=s.expand(p*(1-t*t/2+t**4/8)).coeff(t,2*k-1)
                half-=s.bernoulli(2*k)*coef*e**(j+2*k-1)/(2*k)
    half=s.expand(half)
    first=root/e-s.Rational(1,6)-a+(s.Rational(1,12)+a/2+a*a/2)*root*e
    for j in [-1,0,1]: check(s.simplify((half-first).coeff(e,j))==0,'exercise_14e_coefficients')
    full=sum(2*integrals[j]*e**(j-1) for j in [0,2,4])
    inv_stirling=1-e**2/12+e**4/288
    def factorial_weight(series):
        return s.series(inv_stirling*(series.subs(a,s.Rational(1,2))+
                    e**2/12*series.subs(a,-s.Rational(1,2))+
                    e**4/288*series.subs(a,-s.Rational(3,2))),e,0,4).removeO().expand()
    p=factorial_weight(half)
    total=factorial_weight(full)
    p_print=root/e-s.Rational(2,3)+s.Rational(11,24)*root*e+s.Rational(4,135)*e**2-s.Rational(71,1152)*root*e**3
    check(s.simplify(p-p_print)==0,'P_from_discrete_saddle')
    ss=s.series((total-p).subs(e,e/s.sqrt(1-e**2)),e,0,4).removeO()
    s_print=root/e+s.Rational(2,3)-root*e/24-s.Rational(4,135)*e**2+s.Rational(49,1152)*root*e**3
    check(s.simplify(ss-s_print)==0,'S_from_full_saddle_and_shift')

    z,v=s.symbols('z v')
    exponents={3*j-4:s.Rational((-1)**(j+1),j)*v**j for j in range(2,5)}
    ex7=exponential_coefficients(exponents,8)
    J=s.expand(sum(s.integrate(p,(v,0,y))*z**(j-1) for j,p in enumerate(ex7)))
    J_print=y/z-y**3*z/6+y**5*z**3/40+y**4*z**4/12-y**7*z**5/336-y**6*z**6/36+(y**9/3456-y**5/20)*z**7
    check(s.expand(J-J_print)==0,'moving_endpoint_exercise_7')

    x=s.symbols('x')
    coeff=1/(1-x)
    row=[1]
    qr=[]
    for m in range(1,6):
        coeff=s.cancel(-x*s.diff(coeff,x)/(1-x))
        if m==1: row=[1]
        else:
            row=[(j+1)*(row[j] if j<len(row) else 0)+(2*m-j-1)*(row[j-1] if j>0 else 0) for j in range(m)]
        rm=sum(b*x**(j+1) for j,b in enumerate(row))
        qm=sum(b*x**(2*m-1-j) for j,b in enumerate(row))
        check(s.cancel(coeff-(-1)**m*rm/(1-x)**(2*m+1))==0,'R_ODE_vs_Eulerian_recurrence')
        check(s.expand(qm-x**(2*m)*rm.subs(x,1/x))==0,'Q_R_reciprocal_polynomials')
        qr.append({'m':m,'r':str(rm),'q':str(qm),'Eulerian_row':row})

    def Q(n):
        return sum(s.Rational(factorial(n),factorial(n-j)*n**j) for j in range(1,n+1))
    for n in range(1,17):
        lhs=sum((-1)**k*comb(n,k)*k**(n-1)*Q(k) for k in range(1,n+1))
        check(lhs==(-1)**n*factorial(n-1),'finite_difference_identity_16')
    b=s.symbols('b')
    for n in range(8):
        direct=sum(comb(n,k)*(x+k)**k*(b+n-k)**(n-k) for k in range(n+1))
        closed=sum(comb(n,k)*factorial(k)*(x+b+n)**(n-k) for k in range(n+1))
        check(s.expand(direct-closed)==0,'Cauchy_Abel_polynomial_identity_18')

    result={'status':'passed','utc':datetime.now(timezone.utc).isoformat(),'counts':dict(COUNTS),
            'arithmetic':'exact rational/symbolic algebra; no numerical asymptotic fitting',
            'inverse_c1_to_c6':list(map(str,c[1:])),
            'general_saddle_expansion':str(half),'P':str(p),'Q':str(q),'R':str(r),'S':str(s.expand(ss)),
            'parameter_polynomials':qr,
            'limits':'Coefficient and finite transcription checks supplement general proofs and analytic remainder bounds in notes/asymptotic-*.md.'}
    (ROOT/'results/asymptotic-calculations.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':sum(COUNTS.values()),'counts':dict(COUNTS)}))


if __name__=='__main__':
    main()
