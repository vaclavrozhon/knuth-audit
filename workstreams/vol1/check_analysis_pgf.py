"""Symbolic and rational cross-checks for TAOCP 1.2.10.

The probability inequalities themselves are proved in analysis-tails.md;
these checks cover the algebra, moment identities, and numerical cutoffs.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial
from pathlib import Path
from collections import Counter
import json
import sympy as s

from check_analysis_records import convolution, cumulants, pgf_records
from check_gamma_constants import (
    outward, log_point, add, exp_point, scalar, serialize,
)

ROOT = Path(__file__).resolve().parent
COUNTS = Counter()


def check(value, category):
    assert value, category
    COUNTS[category] += 1


def weighted_partitions(total, largest):
    if largest == 0:
        if total == 0:
            yield []
        return
    for k in range(total//largest+1):
        for rest in weighted_partitions(total-k*largest, largest-1):
            yield rest+[k]


def main():
    z, p, e = s.symbols('z p epsilon', positive=True)
    n = s.symbols('n', positive=True)
    g = (z**(n+1)-z)/(n*(z-1))
    d1 = (n*z**(n+1)-(n+1)*z**n+1)/(n*(z-1)**2)
    d2 = (n*(n-1)*z**(n+1)-2*(n+1)*(n-1)*z**n+n*(n+1)*z**(n-1)-2)/(n*(z-1)**3)
    for order, target in [(1,d1),(2,d2)]:
        check(s.simplify(s.diff(g,z,order)-target)==0, 'uniform_derivatives')

    q = 1-p
    dp = (p+e)*s.log((p+e)/p)+(q-e)*s.log((q-e)/q)
    check(s.simplify(s.diff(dp,e,2)-1/((p+e)*(q-e)))==0, 'binomial_rate_derivative')
    symmetric = (s.Rational(1,2)+e)*s.log(1+2*e)+(s.Rational(1,2)-e)*s.log(1-2*e)
    check(s.simplify(s.diff(symmetric,e,2)-1/(s.Rational(1,4)-e**2))==0,
          'symmetric_rate_derivative')
    expansion = s.series(symmetric,e,0,18).removeO().expand()
    for k in range(1,9):
        check(expansion.coeff(e,2*k)==s.Rational(2**(2*k-1),2*k*k-k), 'C0015_series_coefficients')

    q = p+1
    fminus = (p-e)*s.log(p/(p-e))+(q-e)*s.log((q-e)/q)
    fplus = (q+e)*s.log(1+e/q)-(p+e)*s.log(1+e/p)
    check(s.simplify(s.diff(fminus,e,2)+1/((p-e)*(q-e)))==0, 'negative_binomial_lower_derivative')
    check(s.simplify(s.diff(fplus,e)-s.log(1+e/q)+s.log(1+e/p))==0,
          'negative_binomial_upper_derivative')
    gn = (q-p*z)**(-n)
    mean = s.diff(gn,z).subs(z,1)
    variance = s.diff(gn,z,2).subs(z,1)+mean-mean**2
    check(s.simplify(mean-n*p)==0 and s.simplify(variance-n*p*q)==0,
          'negative_binomial_moments')

    # Compare the partition formula with coefficients computed from M'=K'M.
    distributions = [[Q(1,2),Q(1,2)], [Q(1,3),Q(0),Q(2,3)],
                     [Q(1,2),Q(1,3),Q(0),Q(1,6)], pgf_records(7)]
    for probs in distributions:
        mom = [sum(prob*i**r for i,prob in enumerate(probs)) for r in range(9)]
        ks = cumulants(probs,8)
        central = [sum(prob*(i-mom[1])**r for i,prob in enumerate(probs)) for r in range(9)]
        for r in range(1,9):
            def formula(ms):
                total = Q(0)
                for kk in weighted_partitions(r,r):
                    count = sum(kk)
                    term = Q((-1)**(count-1)*factorial(r)*factorial(count-1))
                    for j,k in enumerate(kk,1):
                        term *= Q(ms[j]**k, factorial(k)*factorial(j)**k)
                    total += term
                return total
            check(formula(mom)==ks[r], 'moment_cumulant_partition_formula')
            if r>=2:
                check(formula(central)==ks[r], 'central_moment_cumulants')

    # EGF in n for r-th moments of A+1, independently extracted by polynomial products.
    degree = 10
    logseries = [Q(0)]+[Q(1,k) for k in range(1,degree+1)]
    powers = [[Q(1)]+[Q(0)]*degree]
    for k in range(1,7):
        powers.append(convolution(powers[-1],logseries)[:degree+1])
    stir = [[1]]
    for r in range(1,7):
        prev = stir[-1]
        stir.append([0]+[prev[k-1]+(k*prev[k] if k<r else 0) for k in range(1,r+1)])
    for r in range(7):
        coefficients = [sum(stir[r][k]*sum(powers[k][:j+1]) for k in range(r+1))
                        for j in range(degree+1)]
        for j in range(1,degree+1):
            direct = sum(prob*(k+1)**r for k,prob in enumerate(pgf_records(j)))
            check(coefficients[j]==direct, 'record_moment_generating_identity')

    f = (1+z)/2
    g = 1/(2-z)
    h = g.subs(z,f)
    check(s.simplify(h-2/(3-z))==0 and h.subs(z,0)==s.Rational(2,3), 'C0014_infinite_composition')
    def mv(fun):
        m = s.diff(fun,z).subs(z,1)
        return m, s.diff(fun,z,2).subs(z,1)+m-m*m
    mf,vf = mv(f);mg,vg = mv(g);mh,vh = mv(h)
    check(mh==mf*mg and vh==vg*mf**2+mg*vf, 'compound_moments')
    mixture = f/3+2*g/3
    mm,vm = mv(mixture)
    check(mm==mf/3+2*mg/3 and vm==vf/3+2*vg/3+s.Rational(2,9)*(mf-mg)**2,
          'mixture_moments')

    cutoff_log = add(log_point(Q(25,108)*2),outward(1-Q(25,108)))
    check(cutoff_log[1]<0, 'chernoff_cutoff_4_32')
    c2 = scalar(exp_point(Q(1,2)),Q(1,2))
    check(c2[1]<Q(825,1000), 'chernoff_cutoff_2')
    result = {'counts':dict(COUNTS),'total_checks':sum(COUNTS.values()),
              'log_2c_4_32':serialize(cutoff_log),'c_2':serialize(c2),
              'sympy_version':s.__version__}
    (ROOT/'results/analysis-pgf.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':
    main()
