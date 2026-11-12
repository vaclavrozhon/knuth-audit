"""Independent finite checks for TAOCP 1.2.10, with rational certificates.

Enumerate inputs through the actual maximum algorithm, then compare to
PGFs, Stirling-number formulas, and fixed-multiplicity formulas.
No previous checker is executed on import.
"""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import permutations, product, combinations_with_replacement
from math import comb, factorial
from pathlib import Path
import json

from check_gamma_constants import (
    outward, constant, sqrt_interval, div, scalar, serialize,
    bernoulli_numbers,
)

ROOT = Path(__file__).resolve().parent
COUNTS = Counter()


def check(test, category, detail=None):
    assert test, (category, detail)
    COUNTS[category] += 1


def convolution(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def algorithm_m(a):
    n = len(a)
    j, k, m = n-1, n-2, a[-1]
    steps = [1, 0, 0, 0, 0]
    while True:
        steps[1] += 1
        if k < 0:
            return j, steps
        steps[2] += 1
        if not a[k] <= m:
            j, m = k, a[k]
            steps[3] += 1
        k -= 1
        steps[4] += 1


def pgf_records(n):
    a = [Q(1)]
    for j in range(2, n+1):
        a = convolution(a, [Q(j-1,j), Q(1,j)])
    return a


def cumulants(probabilities, order=8):
    # Compute coefficients of log(M(t)) by M'=K'M.
    a = [sum(p*Q(i**r, factorial(r)) for i,p in enumerate(probabilities))
         for r in range(order+1)]
    assert a[0] == 1
    k = [Q(0)]*(order+1)
    for r in range(1, order+1):
        k[r] = a[r] - sum((j*k[j]*a[r-j] for j in range(1,r)), Q(0))/r
    return [factorial(r)*k[r] for r in range(order+1)]


def rounded(interval, digits):
    lo, hi = interval
    a = (lo*10**digits+Q(1,2)).numerator // (lo*10**digits+Q(1,2)).denominator
    b = (hi*10**digits+Q(1,2)).numerator // (hi*10**digits+Q(1,2)).denominator
    assert a == b, interval
    s = str(a).rjust(digits+1, '0')
    return s[:-digits]+'.'+s[-digits:]


def main():
    s1 = [[1]]
    s2 = [[1]]
    for n in range(1, 17):
        c, s = [0]*(n+1), [0]*(n+1)
        for k in range(1,n+1):
            c[k] = s1[-1][k-1]+((n-1)*s1[-1][k] if k<n else 0)
            s[k] = s2[-1][k-1]+(k*s2[-1][k] if k<n else 0)
        s1.append(c);s2.append(s)

    for n in range(1,9):
        hist = Counter()
        for a in permutations(range(n)):
            j, steps = algorithm_m(a)
            check(j == a.index(n-1), 'permutation_maximum')
            updates = steps[3]
            check(steps == [1,n,n-1,updates,n-1], 'step_counts')
            hist[updates] += 1
            if n<=7:
                inv = [a.index(v) for v in range(n)]
                for k,l in enumerate(a):
                    check(all(v<l for v in a[:k]) == all(v>k for v in inv[l+1:]),
                          'inverse_records')
        coeff = pgf_records(n)
        for k in range(n):
            check(Q(hist[k],factorial(n)) == coeff[k] == Q(s1[n][k+1],factorial(n)),
                  'permutation_distribution', (n,k))

    bern = bernoulli_numbers(16)
    bern[1] = Q(1,2)  # Current convention in TAOCP.
    for n in range(1,8):
        for m in range(1,5):
            hist = Counter()
            distinct = Counter()
            joint = defaultdict(Counter)
            multiplicity = defaultdict(Counter)
            for a in product(range(m), repeat=n):
                j, steps = algorithm_m(a)
                check(j == max(i for i,v in enumerate(a) if v==max(a)), 'ties_rightmost')
                updates = steps[3]
                hist[updates] += 1
                d = len(set(a));distinct[d] += 1;joint[d][updates] += 1
                multiplicity[tuple(a.count(v) for v in range(m))][updates] += 1
            for d in range(1,min(m,n)+1):
                expected = factorial(m)//factorial(m-d)*s2[n][d]
                check(distinct[d] == expected, 'occupancy_distribution')
                for k in range(n):
                    check(Q(joint[d][k],distinct[d]) == (Q(s1[d][k+1],factorial(d)) if k<d else 0),
                          'conditional_distinct_distribution')
            for k in range(n):
                expected = sum(comb(m,d)*s2[n][d]*s1[d][k+1]
                               for d in range(k+1,min(m,n)+1))
                check(hist[k] == expected, 'mixture_record_distribution')
            empirical = 1+sum(Q(k*v,m**n) for k,v in hist.items())
            geometric = sum((1-(1-Q(j,m))**n)/j for j in range(1,m+1))
            bernoulli = sum(Q(1,j) for j in range(1,n+1)) + sum(
                Q(comb(n,k)-1,k)*bern[k]/m**k for k in range(1,n+1))-Q(n-1,m)
            check(empirical == geometric == bernoulli, 'expected_records_bernoulli')
            for ks, hh in multiplicity.items():
                p, tail = [Q(1)], 0
                for kr in reversed(ks):
                    if tail+kr:
                        p = convolution(p,[Q(tail,tail+kr),Q(kr,tail+kr)])
                    tail += kr
                assert p[0] == 0
                p = p[1:]
                total = sum(hh.values())
                for k in range(max(len(p),n)):
                    check(Q(hh[k],total) == (p[k] if k<len(p) else 0),
                          'fixed_multiplicity_pgf', (ks,k))

    for n in range(1,6):
        for a in product((-1,0,2), repeat=n):
            left = [i for i in range(n) if all(a[j]<a[i] for j in range(i))]
            right = [i for i in range(n) if all(a[j]>a[i] for j in range(i+1,n))]
            for b in combinations_with_replacement((-2,0,1),n):
                reduced = max(max(a[i]-b[i] for i in left),max(b[i]-a[i] for i in right))
                check(reduced == max(abs(x-y) for x,y in zip(a,b)), 'subtraction_records')

    cumulant_samples = []
    for n in range(1,17):
        pp = pgf_records(n)
        h = [sum(Q(1,j**r) for j in range(1,n+1)) for r in (1,2,3)]
        kap = cumulants(pp,3)
        check(kap[1:] == [h[0]-1,h[0]-h[1],h[0]-3*h[1]+2*h[2]], 'record_cumulants')
        uniform = [Q(0)]+[Q(1,n)]*n
        ku = cumulants(uniform)
        check(ku[1] == Q(n+1,2), 'uniform_mean')
        for r in range(2,9):
            check(ku[r] == Q(n**r-1,r)*bern[r], 'uniform_cumulants')
        for p in [Q(0),Q(1,5),Q(1,2),Q(3,5),Q(1)]:
            binom = [comb(n,k)*p**k*(1-p)**(n-k) for k in range(n+1)]
            kb = cumulants(binom,3)
            check(kb[1:] == [n*p,n*p*(1-p),n*p*(1-p)*(1-2*p)], 'binomial_cumulants')
        if n==12:
            cumulant_samples.append({'n':n,'pgf':[str(x) for x in pp],
                                     'mean':str(kap[1]),'variance':str(kap[2])})
            check(kap[1] == Q(58301,27720), 'figure10_mean')
            check(rounded(outward(kap[2]),2)=='1.54', 'figure10_variance')

    h1000 = sum(Q(1,j) for j in range(1,1001))
    v1000 = h1000-sum(Q(1,j*j) for j in range(1,1001))
    mu, sd = outward(h1000-1), sqrt_interval(outward(v1000))
    check(rounded(mu,2)=='6.49' and rounded(sd,2)=='2.42', 'exercise3_rounding')
    check(rounded(sqrt_interval(outward(Q(72,25))),3)=='1.697', 'figure11_deviation')

    percentages = []
    for r, target in [(1,'68.268949213709'),(2,'95.449973610364'),(3,'99.730020393674')]:
        total = sum(Q((-1)**k*r**(2*k+1),2**k*factorial(k)*(2*k+1)) for k in range(81))
        remainder = Q(r**163,2**81*factorial(81)*163)
        # Taylor's integral remainder for exp(-u), u>=0: next sign negative.
        integ = outward(total-remainder,total)
        percent = scalar(div(integ,sqrt_interval(scalar(constant('pi'),2))),200)
        check(rounded(percent,12)==target, 'gaussian_percentages')
        percentages.append({'r':r,'percent':serialize(percent),'rounded_12':target})

    # Exact counterexamples to the two tail claims.
    p2 = pgf_records(2)
    check(p2 == [Q(1,2),Q(1,2)], 'C0013_distribution')
    k2 = cumulants(p2,2)
    check(all((Q(i)-k2[1])**2 == k2[2] for i in range(2)), 'C0013_standardization')
    tail = sum(Q(comb(8,k)*3**(8-k),4**8) for k in range(6,9))
    check(tail == Q(277,65536) > Q(1,256), 'C0015_binomial_counterexample')
    check(Q(1,6)<Q(1,4), 'C0015_missing_n')

    result = {'counts':dict(COUNTS),'total_checks':sum(COUNTS.values()),
              'record_samples':cumulant_samples,'n1000':{'mean':serialize(mu),'deviation':serialize(sd)},
              'gaussian_percentages':percentages,
              'C0015':{'actual_tail':str(tail),'claimed_bound_after_inserting_n':'1/256'}}
    (ROOT/'results/analysis-records.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'total_checks':sum(COUNTS.values()),'counts':dict(COUNTS)}))


if __name__ == '__main__':
    main()
