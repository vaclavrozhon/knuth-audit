"""Exact cross-checks of printed formulas in TAOCP 1.2.11.2.

General proofs and all error bounds are in notes/euler-*.md.
This script checks transcription, both endpoint conventions, independent
coefficient constructions, and the printed Kinkelin-Glaisher constant.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json
import sympy as s

from check_gamma_constants import (
    bernoulli_numbers, outward, add, neg, scalar, log_point,
    exp_interval, serialize, prefix,
)

ROOT = Path(__file__).resolve().parent
COUNTS = Counter()


def check(condition, category):
    assert condition, category
    COUNTS[category] += 1


def deriv_monomial(degree, order, x):
    if order > degree:
        return Q(0)
    return Q(factorial(degree), factorial(degree-order))*x**(degree-order)


def bernoulli_polynomial(m, b):
    return [Q(comb(m, j))*b[m-j] for j in range(m+1)]


def value(poly, x):
    return sum((a*x**j for j, a in enumerate(poly)), Q(0))


def main():
    b = bernoulli_numbers(16)
    B = [(-1)**j*x for j, x in enumerate(b)]
    for n in range(16):
        check(sum(comb(n,k)*(-1)**(n-k)*B[k] for k in range(n+1))
              == B[n]-(n==1), 'current_recurrence')
        for x in [Q(-3), Q(0), Q(1,2), Q(1), Q(5,3)]:
            old = value(bernoulli_polynomial(n,b),x)
            new = sum((comb(n,k)*B[k]*(x-1)**(n-k) for k in range(n+1)),Q(0))
            check(old == new, 'polynomial_conventions')

    # Integrate the actual periodic remainder cell by cell, independently
    # of the boundary corrections, for a basis of polynomial functions.
    for degree in range(13):
        for lower, upper in [(0,0),(0,1),(0,3),(1,1),(1,2),(1,5),(-2,3)]:
            direct = sum((Q(k)**degree for k in range(lower,upper+1)),Q(0))
            for m in range(1,9):
                integral = Q(upper**(degree+1)-lower**(degree+1),degree+1)
                approximation = integral+Q(lower)**degree
                for j in range(1,m+1):
                    delta = deriv_monomial(degree,j-1,Q(upper))-deriv_monomial(degree,j-1,Q(lower))
                    approximation += B[j]*delta/factorial(j)
                remainder = Q(0)
                if degree>=m:
                    p = bernoulli_polynomial(m,b)
                    for cell in range(lower,upper):
                        for i, coefficient in enumerate(p):
                            for j in range(degree-m+1):
                                remainder += coefficient*comb(degree-m,j)*Q(cell)**(degree-m-j)/Q(i+j+1)
                    remainder *= Q((-1)**(m+1)*factorial(degree),factorial(m)*factorial(degree-m))
                check(approximation+remainder==direct,'current_euler_exact_remainder')
                old_approx = approximation-Q(upper)**degree
                check(old_approx+remainder==direct-Q(upper)**degree,'original_euler_endpoints')

    for m in range(13):
        poly=bernoulli_polynomial(m+1,b)
        for n in range(13):
            current=(value(poly,Q(n+1))-B[m+1])/Q(m+1)+Q(0)**m
            original=(value(poly,Q(n))-b[m+1])/Q(m+1)
            check(current==sum(k**m for k in range(n+1)), 'corrected_power_sums')
            check(original==sum(k**m for k in range(n)), 'original_power_sums')

    z,r=s.symbols('z r')
    stirling_log=sum(s.Rational(b[2*j].numerator,b[2*j].denominator)*z**(2*j-1)/(2*j*(2*j-1)) for j in range(1,5))
    factorial_series=s.series(s.exp(stirling_log),z,0,5).removeO().expand()
    factorial_print=[Q(1),Q(1,12),Q(1,288),Q(-139,51840),Q(-571,2488320)]
    for k,wanted in enumerate(factorial_print):
        check(factorial_series.coeff(z,k)==wanted,'printed_factorial_coefficients')

    central_log=s.expand(stirling_log.subs(z,z/2)-2*stirling_log)
    central=s.series(s.exp(central_log),z,0,7).removeO().expand()
    central_print=[Q(1),Q(-1,8),Q(1,128),Q(5,1024),Q(-21,32768),Q(-399,262144),Q(869,4194304)]
    cycle=[[1]]
    for n in range(1,13):
        prev=cycle[-1]
        cycle.append([0]+[(prev[k-1] if k-1<len(prev) else 0)+(n-1)*(prev[k] if k<len(prev) else 0) for k in range(1,n+1)])
    for k,wanted in enumerate(central_print):
        poly=s.interpolate([(n,cycle[n][n-k] if n>=k else 0) for n in range(2*k+1)],r)
        check(poly.subs(r,s.Rational(1,2))==wanted,'central_coefficients_from_cycle_counts')
        check(central.coeff(z,k)==wanted,'central_coefficients_from_log_factorials')

    a=s.symbols('a',positive=True)
    bb, ln_n, sigma=s.symbols('b ln_n sigma',real=True)
    logx=2*ln_n+s.log(a)+sum((-1)**(j+1)*(bb*z/a)**j/s.Integer(j) for j in range(1,4))
    x=a/z**2+bb/z
    actual=s.expand((x+s.Rational(1,2))*logx-x+sigma)
    target=2*a*ln_n/z**2+a*(s.log(a)-1)/z**2+2*bb*ln_n/z+bb*s.log(a)/z+ln_n+bb**2/(2*a)+s.log(a)/2+sigma+(3*a-bb**2)*bb*z/(6*a**2)
    for k in [-2,-1,0,1]:
        check(s.simplify(s.expand(actual-target).coeff(z,k))==0,'quadratic_factorial_expansion')
    c=s.symbols('c',positive=True)
    ratio=target.subs({a:c,bb:0})-target.subs({a:c,bb:-1})-s.log(c)/z-target.subs({a:1,bb:0})+target.subs({a:1,bb:-1})
    ratio_target=(c-1)/(2*c)-(c-1)*(2*c-1)*z/(6*c**2)
    check(s.simplify(ratio-ratio_target)==0,'binomial_ratio_cancellation')

    # A is bounded by a finite sum of certified logarithms and the analytic
    # first-omitted-term bound P2. No special-function evaluation is used.
    n,t=16,4
    log_product=outward(0)
    for k in range(1,n+1):
        log_product=add(log_product,scalar(log_point(k),k))
    main_part=add(scalar(log_point(n),Q(n*n+n,2)+Q(1,12)),outward(-Q(n*n,4)))
    corrections=sum((-b[2*j]/Q((2*j-2)*(2*j-1)*(2*j)*n**(2*j-2)) for j in range(2,t+1)),Q(0))
    center=add(add(log_product,neg(main_part)),outward(-corrections))
    error=abs(b[2*t+2])/Q((2*t)*(2*t+1)*(2*t+2)*n**(2*t))
    log_A=add(center,(-error,error))
    A=exp_interval(log_A)
    check(prefix(A,7)=='1.2824271','printed_Kinkelin_Glaisher_digits')
    result={'status':'passed','utc':datetime.now(timezone.utc).isoformat(),
            'arithmetic':'exact rationals, symbolic algebra, outward rational intervals',
            'counts':dict(COUNTS),'A_interval':serialize(A),'log_A_interval':serialize(log_A),
            'A_parameters':{'n':n,'t':t,'log_error_bound':str(error)},
            'limits':'Finite checks supplement the general proofs. No bibliographic or historical conclusion follows from these calculations.'}
    (ROOT/'results/euler-summation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':sum(COUNTS.values()),'counts':dict(COUNTS),'A_interval':serialize(A)}))


if __name__=='__main__':
    main()
