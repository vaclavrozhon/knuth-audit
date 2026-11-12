"""Exact certificates for TAOCP 1.2.11.3-13.

The contour argument is in notes/ramanujan-bound.md. This checks its
constants, polynomial signs for every n>=128, and all 127 smaller cases.
No floating-point evaluation of Q, R, exp, or gamma is used.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json
import sympy as s

from check_gamma_constants import (
    constant, outward, add, neg, mul, div, scalar, sqrt_interval,
    log_interval, exp_interval, serialize,
)

ROOT = Path(__file__).resolve().parent
COUNTS = Counter()


def check(condition, category):
    assert condition, category
    COUNTS[category] += 1


def power(a, n):
    result = outward(1)
    for _ in range(n):
        result = mul(result, a)
    return result


def main():
    pi = constant('pi')
    ep = power(exp_interval(scalar(pi, F(1, 4))), 4)
    pi2 = mul(pi, pi)
    lower = div(pi2, scalar(add(outward(1), mul(add(scalar(pi, 2), outward(1)), ep)), 2))
    upper = div(pi2, add(outward(1), neg(div(add(pi, outward(1)), ep))))
    logs = [log_interval(lower), log_interval(upper)]
    log_bound = max(abs(v) for interval in logs for v in interval)
    modulus = sqrt_interval(add(outward(log_bound**2), scalar(pi2, 4)))
    cauchy = div(scalar(modulus, 4), pi)
    check(cauchy[1] < 11, 'Cauchy_coefficient_constant')
    check(exp_interval(outward(F(1,12)))[1] < F(11,10), 'Stirling_factor')

    root2 = sqrt_interval(outward(2))
    rho = div(add(outward(1), root2), pi)
    tail = div(scalar(power(rho, 11), 11), add(outward(1), neg(rho)))
    H = scalar(mul(mul(sqrt_interval(scalar(pi, 2)), add(outward(1), root2)), tail), F(33,40))
    check(H[1] < 14, 'arc_constant_H10')
    mu = div(outward(11), mul(power(pi, 10), add(pi, outward(-1))))
    G = div(scalar(mu, F(11*128*10395,10)), root2)
    check(G[1] < 57, 'vertical_constant_G10')
    check(14**2 * 128**9 * 10**14 < 2**128, 'arc_at_128')
    check(F(129,128)**9 < 2, 'arc_decreases_for_all_larger_integers')

    z, v, t = s.symbols('z v t')
    # h=2(1-(1+z)exp(-z))/z^2, Phi=-log h.
    h = sum(2*s.Rational((-1)**j, factorial(j)*(j+2))*z**j for j in range(11))
    phi = s.series(-s.log(h), z, 0, 11).removeO().expand()
    B = {}
    for k in range(1,11):
        B[k] = s.expand(sum((-1)**(k-j)*comb(k,j)*j*
                           s.prod(1-r*v for r in range(1,j)) for j in range(1,k+1)))
    D = s.expand(sum(phi.coeff(z,k)*B[k] for k in range(1,11)))
    # The paper prints +1794 on p.109 and -17984 on p.113.
    # Exact expansion gives +17984; retain that correction explicitly.
    printed = [F(2,3),F(8,135),F(-16,2835),F(-32,8505),
               F(17984,12629925),F(13159709,9699782400),
               F(-977069,1039262400),F(-36669961,28291032000),
               F(117191,56582064),F(-479,561330)]
    for j, value in enumerate(printed):
        check(D.coeff(v,j)==value, 'D10_independent_coefficients')

    n = s.symbols('n')
    Dn = D.subs(v,1/n)
    delta = s.Rational(1,10**7)/n**3 + 57/n**5
    low = s.Rational(2,3)+8/(135*(n+s.Rational(8,45)))
    high = s.Rational(2,3)+8/(135*(n+s.Rational(2,21)))
    signs = {}
    for label, difference in [('lower',Dn-delta-low), ('upper',high-Dn-delta)]:
        num, den = s.fraction(s.cancel(difference))
        # Positive coefficients after n=t+128 certify every real n>=128.
        shifted = s.Poly(s.expand(num.subs(n,t+128)),t)
        check(all(c>0 for c in shifted.all_coeffs()), 'polynomial_positive_'+label)
        check(all(c>=0 for c in s.Poly(den,n).all_coeffs()), 'denominator_positive_'+label)
        signs[label] = {'numerator':str(num), 'denominator':str(den),
                        'shift':128, 'shifted_coefficients_descending':list(map(str,shifted.all_coeffs()))}

    finite = []
    en = outward(1)
    e = constant('e')
    for k in range(1,128):
        en = mul(en,e)
        term = q = F(1)
        for j in range(1,k):
            term *= F(k-j,k)
            q += term
        dn = add(scalar(en,F(factorial(k),k**k)),outward(-2*q))
        lower_bound = F(2,3)+F(8,135)/(k+F(8,45))
        upper_bound = F(2,3)+F(8,135)/(k+F(2,21))
        check(lower_bound<dn[0] and dn[1]<upper_bound, 'finite_Ramanujan_interval')
        finite.append({'n':k,'D_interval':serialize(dn),
                       'lower_margin':serialize(outward(dn[0]-lower_bound)),
                       'upper_margin':serialize(outward(upper_bound-dn[1]))})

    result = {'status':'passed','utc':datetime.now(timezone.utc).isoformat(),
              'arithmetic':'exact rational and outward rational interval arithmetic; exact symbolic polynomials',
              'counts':dict(COUNTS),'constants':{'cauchy_M':serialize(cauchy),'H10':serialize(H),'G10':serialize(G)},
              'phi_coefficients_1_to_10':[str(phi.coeff(z,k)) for k in range(1,11)],
              'D10_coefficients':list(map(str,printed)),
              'source_corrections':['The n^-4 coefficient is +17984/12629925; p.109 omits digit 8 and p.113 has a minus sign.'],
              'tail_certificate':signs,
              'finite_cases':finite,
              'limits':'Uses the analytic contour argument recorded in notes/ramanujan-bound.md; samples alone are not a proof for all n.'}
    (ROOT/'results/ramanujan-bound.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':sum(COUNTS.values()),'counts':dict(COUNTS),'constants':result['constants']}))


if __name__=='__main__':
    main()
