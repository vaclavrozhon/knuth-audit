"""Independent exact checks of TAOCP 3.3.2 G, exercises 11--14 and 25.

Comparison-pattern probabilities use a rank recurrence, not the printed
moment formulas. Completed blocks are checkpointed for --resume.
"""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations
from math import factorial as fac, comb
from pathlib import Path
import json
import sys
import sympy as s

ROOT = Path(__file__).resolve().parent
DEST = ROOT/'results/run-tests.json'


@lru_cache(None)
def pattern_probability(pattern):
    """Probability of specified consecutive comparisons in iid continuous data."""
    dp = [1]
    for up in pattern:
        k = len(dp)
        prefix = [0]
        for x in dp:
            prefix.append(prefix[-1]+x)
        dp = [prefix[r] if up else prefix[k]-prefix[r]
              for r in range(k+1)]
    return Q(sum(dp), fac(len(pattern)+1))


def indicator_probability(n, *events):
    edges = {}
    for p,i in events:
        if i < 1 or i+p-1 > n:
            return Q(0)
        requested = ([(i-1,False)] if i > 1 else [])
        requested += [(j,True) for j in range(i,i+p-1)]
        for j,up in requested:
            if j in edges and edges[j] != up:
                return Q(0)
            edges[j] = up
    result = Q(1)
    block = []
    previous = -2
    for j,up in sorted(edges.items()):
        if j != previous+1 and block:
            result *= pattern_probability(tuple(block))
            block = []
        block.append(up)
        previous = j
    return result*pattern_probability(tuple(block))


def book_indicator(n,p,i):
    return Q(p+(i==1),fac(p+1)) if i <= n-p+1 else Q(0)


def book_joint(n,p,i,q,j):
    assert i < j
    if i+p < j <= n-q+1:
        return Q((p+(i==1))*q,fac(p+1)*fac(q+1))
    if i+p == j <= n-q+1:
        return Q(p+(i==1),fac(p+1)*fac(q))-Q(p+q+(i==1),fac(p+q+1))
    return Q(0)


def mean(n,p):
    if p > n:
        return Q(0)
    return Q((n+1)*p,fac(p+1))-Q(p-1,fac(p))


def covariance(n,p,q):
    if max(p,q) > n:
        return Q(0)
    if p+q > n:
        return mean(n,max(p,q))-mean(n,p)*mean(n,q)
    z = p+q
    f = (n+1)*(Q(z*(1-p*q)+p*q,fac(p+1)*fac(q+1))-Q(2*z,fac(z+1)))
    f += Q(2*(z-1),fac(z))
    f += Q((z*z-z-2)*p*q-z*z-p*p*q*q+1,fac(p+1)*fac(q+1))
    return mean(n,max(p,q))+f


def coefficients(t):
    """Grouped counts (R_1,...,R_(t-1),R'_t) = D (R'_1,...,R'_t)."""
    d = s.eye(t)
    for j in range(t-1):
        d[j,j+1] = -1
    n = 2*t
    c = s.Matrix(t,t,lambda i,j: covariance(n,i+1,j+1))
    cnext = s.Matrix(t,t,lambda i,j: covariance(n+1,i+1,j+1))
    c1 = d*(cnext-c)*d.T
    c2 = d*c*d.T-n*c1
    mu = d*s.Matrix([mean(n,p) for p in range(1,t+1)])
    b = d*s.Matrix([Q(p,fac(p+1)) for p in range(1,t+1)])
    return c1,c2,b,mu-n*b


def indicator_checks():
    first = pairs = moments = arrangements = 0
    for n in range(1,17):
        for p in range(1,min(n,6)+1):
            for i in range(1,n+1):
                assert book_indicator(n,p,i) == indicator_probability(n,(p,i))
                first += 1
                for q in range(1,min(n,6)+1):
                    for j in range(i+1,n+1):
                        assert book_joint(n,p,i,q,j) == indicator_probability(n,(p,i),(q,j)), (n,p,i,q,j)
                        pairs += 1
    for n in range(1,11):
        for p in range(1,n+1):
            m = sum(indicator_probability(n,(p,i)) for i in range(1,n+1))
            assert m == mean(n,p)
            for q in range(1,n+1):
                e = sum(indicator_probability(n,(p,i),(q,j))
                        for i in range(1,n+1) for j in range(1,n+1))
                assert e-m*mean(n,q) == covariance(n,p,q), (n,p,q)
                moments += 1
    for p in range(1,16):
        for q in range(1,16):
            count = (p+q+1)*comb(p+q,p)-comb(p+q+1,p+1)-(p+q+1)+1
            pattern = (False,)+(True,)*(p-1)+(False,)+(True,)*(q-1)
            assert pattern_probability(pattern)*fac(p+q+1) == count
            arrangements += 1
    return dict(single_indicators=first,indicator_pairs=pairs,
                moment_pairs=moments,exercise13_arrangements=arrangements,
                independent_model='rank DP for prescribed rises and falls')


def algorithm_r(values):
    n = len(values)
    u = list(values)+[values[-1]]
    j = -1
    counts = [0]*6
    while True:
        r = 0
        while True:
            r += 1
            j += 1
            if not u[j] < u[j+1]:
                break
        counts[min(r,6)-1] += 1
        if j == n-1:
            return counts


def enumeration():
    cases = 0
    moment_pairs = 0
    for n in range(1,9):
        total = [0]*n
        second = [[0]*n for _ in range(n)]
        for u in permutations(range(n)):
            starts = [0]+[i+1 for i in range(n-1) if u[i]>u[i+1]]+[n]
            lengths = [b-a for a,b in zip(starts,starts[1:])]
            rprime = [sum(r >= p for r in lengths) for p in range(1,n+1)]
            assert algorithm_r(u) == [sum(min(r,6)==p for r in lengths) for p in range(1,7)]
            cases += 1
            for i,x in enumerate(rprime):
                total[i] += x
                for j,y in enumerate(rprime):
                    second[i][j] += x*y
        for i in range(n):
            assert Q(total[i],fac(n)) == mean(n,i+1)
            for j in range(n):
                cov = Q(second[i][j],fac(n))-Q(total[i]*total[j],fac(n)**2)
                assert cov == covariance(n,i+1,j+1)
                moment_pairs += 1
    u = [1,2,9,8,5,3,6,7,0,4]
    starts = [0]+[i+1 for i in range(9) if u[i]<u[i+1]]+[10]
    down = [u[a:b] for a,b in zip(starts,starts[1:])]
    assert down == [[1],[2],[9,8,5,3],[6],[7,0],[4]]
    # Exercise 14: one run includes its stopping comparison, discards that
    # comparison's final value; successive blocks thus have disjoint inputs.
    for r in range(1,21):
        assert pattern_probability((True,)*(r-1)+(False,)) == Q(1,fac(r))-Q(1,fac(r+1))
    return dict(permutations=cases,exhaustive_covariances=moment_pairs,
                descending_example=down,exercise14_probabilities=20)


def matrix_checks():
    c1,c2,b,bias = coefficients(6)
    printed1 = s.Matrix([
        ['23/180','-7/360','-5/336','-433/60480','-13/5670','-121/181440'],
        ['-7/360','2843/20160','-989/20160','-7159/362880','-10019/1814400','-1303/907200'],
        ['-5/336','-989/20160','54563/907200','-21311/1814400','-62369/19958400','-7783/9979200'],
        ['-433/60480','-7159/362880','-21311/1814400','886657/39916800','-257699/239500800','-62611/239500800'],
        ['-13/5670','-10019/1814400','-62369/19958400','-257699/239500800','29874811/5448643200','-1407179/21794572800'],
        ['-121/181440','-1303/907200','-7783/9979200','-62611/239500800','-1407179/21794572800','2134697/1816214400']])
    printed2 = s.Matrix([
        ['83/180','-29/180','-11/210','-41/12096','91/25920','41/18144'],
        ['-29/180','-305/4032','319/20160','2557/72576','10177/604800','413/64800'],
        ['-11/210','319/20160','-58747/907200','19703/604800','239471/19958400','39517/9979200'],
        ['-41/12096','2557/72576','19703/604800','-220837/4435200','1196401/239500800','360989/239500800'],
        ['91/25920','10177/604800','239471/19958400','1196401/239500800','-139126639/7264857600','4577641/10897286400'],
        ['41/18144','413/64800','39517/9979200','360989/239500800','4577641/10897286400','-122953057/21794572800']])
    assert c1 == printed1 and c2 == printed2
    assert b == s.Matrix(['1/6','5/24','11/120','19/720','29/5040','1/840'])
    a = c1.inv()
    assert c1*a == s.eye(6)
    printed_a = s.Matrix([
        ['4529.4','9044.9',13568,18091,22615,27892],
        ['9044.9',18097,27139,36187,45234,55789],
        [13568,27139,40721,54281,67852,83685],
        [18091,36187,54281,72414,90470,111580],
        [22615,45234,67852,90470,113262,139476],
        [27892,55789,83685,111580,139476,172860]]).applyfunc(lambda x:s.Rational(str(x)))
    deviations = []
    for i in range(6):
        for j in range(6):
            diff = abs(a[i,j]-printed_a[i,j])
            # First two printed entries have one decimal, all others integers.
            unit = Q(1,10) if (i,j) in [(0,0),(0,1),(1,0)] else 1
            assert diff <= unit/2
            deviations.append(dict(i=i+1,j=j+1,exact=str(a[i,j]),
                                   decimal=str(a[i,j].evalf(18)),
                                   printed=str(printed_a[i,j]),
                                   error_last_units=float(diff/unit)))
    _,dd = c1.LDLdecomposition(hermitian=False)
    _,dp = printed_a.LDLdecomposition(hermitian=False)
    assert all(dd[i,i] > 0 and dp[i,i] > 0 for i in range(6))
    expectations = []
    for n in [4000,10000,1000000]:
        ev = (s.trace(printed_a*(n*c1+c2))+(bias.T*printed_a*bias)[0])/(n-6)
        expectations.append(dict(n=n,exact=str(ev),decimal=float(ev)))
    return dict(rational_entries_checked=72,means=list(map(str,b)),
                mean_boundary_bias=list(map(str,bias)),inverse_entries=deviations,
                exact_ldl_positive_pivots=[str(dd[i,i]) for i in range(6)],
                rounded_A_positive_pivots=[str(dp[i,i]) for i in range(6)],
                expected_printed_statistic=expectations,
                limiting_expected_printed_statistic=str(s.trace(printed_a*c1)))


def research25():
    rows = []
    for t in [5,6,7,8,10,12,16,20]:
        c1,c2,b,bias = coefficients(t)
        a = c1.inv()
        k = a*c2*a
        assert c1*a == s.eye(t)
        ratios = [k[i,j]/a[i,j] for i in range(t) for j in range(t)]
        v = s.Matrix(range(1,t+1))
        rare_slope = (v.T*c1*v)[0]
        rare_intercept = (v.T*c2*v)[0]
        rows.append(dict(t=t,minimum=str(min(ratios).evalf(20)),
                         maximum=str(max(ratios).evalf(20)),
                         aggregate_ratio=str((rare_intercept/rare_slope).evalf(20)),
                         aggregate_slope=str(rare_slope),
                         aggregate_intercept=str(rare_intercept)))
    return dict(exact_rational_matrix_products=True,ratios=rows,
                limitation='Numerical investigation, not a general asymptotic proof.')


def main():
    out = json.loads(DEST.read_text()) if '--resume' in sys.argv and DEST.exists() else {}
    for name,fn in [('indicators',indicator_checks),('enumeration',enumeration),
                    ('matrices',matrix_checks),('research25',research25)]:
        if name in out:
            continue
        print('START',name,flush=True)
        out[name] = fn()
        DEST.write_text(json.dumps(out,indent=2)+'\n')
        print('PASS',name,flush=True)
    print('ALL BLOCKS COMPLETE',flush=True)


if __name__ == '__main__':
    main()
