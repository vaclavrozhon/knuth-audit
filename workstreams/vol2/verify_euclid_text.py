#!/usr/bin/env python3
"""Exact checks for the previously uncovered text of TAOCP 4.5.3, pp358--361.

The CF cylinders and all three new constant enclosures use rational arithmetic.
Previously certified gamma data are read, not recomputed.  python-flint is used
only for the elementary logarithmic constants in the last checkpoint.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json
import os
import time

ROOT = Path(__file__).resolve().parent


def floor_root(n, k):
    lo, hi = 0, 1 << ((n.bit_length() + k - 1) // k)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**k <= n:
            lo = mid
        else:
            hi = mid
    assert lo**k <= n < (lo + 1)**k
    return lo


def atan_interval(q, terms):
    # Alternating Taylor series, including the first omitted term as an endpoint.
    s = sum((F((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(terms)), F(0))
    t = s + F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(s, t), max(s, t)


def check_cylinders(prefix, lo, hi):
    p0, p1, q0, q1 = 0, 1, 1, 0
    cylinders = []
    for i, a in enumerate(prefix):
        p0, p1, q0, q1 = p1, a*p1+p0, q1, a*q1+q0
        assert abs(p0*q1-p1*q0) == 1
        ends = sorted([F(p1, q1), F(p1+p0, q1+q0)])
        assert ends[0] < lo <= hi < ends[1], (i, a, ends, lo, hi)
        cylinders.append([str(x) for x in ends])
    return cylinders


def constants():
    scale = 10**100
    s = isqrt(8*scale*scale//29)
    sqrt_interval = F(s, scale), F(s+1, scale)
    assert 29*s*s < 8*scale*scale < 29*(s+1)**2
    c = floor_root(2*scale**3, 3)
    cube_interval = F(c, scale), F(c+1, scale)
    a, b = atan_interval(5, 80), atan_interval(239, 25)
    pi_interval = 16*a[0]-4*b[1], 16*a[1]-4*b[0]
    table = {
        'sqrt_8_over_29': ([0, 1, 1, 9, 2, 2, 3, 2, 2, 9, 1, 2, 1, 9, 2, 2,
                           3, 2, 2, 9, 1, 2, 1, 9, 2, 2, 3, 2, 2, 9, 1], sqrt_interval),
        'cube_root_2': ([1, 3, 1, 5, 1, 1, 4, 1, 1, 8, 1, 14, 1, 10, 2, 1,
                        4, 12, 2, 3, 2, 1, 3, 4, 1, 1, 2, 14, 3], cube_interval),
        'pi': ([3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2,
                2, 2, 1, 84, 2, 1, 1, 15, 3, 13], pi_interval),
    }
    result = {}
    for name, (prefix, interval) in table.items():
        cylinders = check_cylinders(prefix, *interval)
        result[name] = {'printed_prefix_including_integer_part': prefix,
                        'rational_enclosure': list(map(str, interval)),
                        'all_prefix_cylinders': cylinders}
    # Prove the full quadratic period by equality of exact algebraic states.
    from verify_euclid_quadratic import Q
    x = Q(0, F(1, 29), 232)
    quotients, seen = [], {}
    while x not in seen:
        seen[x] = len(quotients)
        a0 = x.floor()
        quotients.append(a0)
        x = (x-a0).inv()
    start = seen[x]
    assert quotients[:start] == [0, 1]
    assert quotients[start:] == [1, 9, 2, 2, 3, 2, 2, 9, 1, 2]
    result['sqrt_period'] = {'prefix': quotients[:start], 'period': quotients[start:]}
    # The rational entry is checked by backward evaluation.
    x = F(0)
    for a0 in reversed([3, 1, 1, 1, 2]):
        x = 1/(a0+x)
    assert x == F(8, 29)
    gamma = json.loads((ROOT/'results/euclid-gamma.json').read_text())
    printed_gamma = [0, 1, 1, 2, 1, 2, 1, 4, 3, 13, 5, 1, 1, 8, 1, 2, 4,
                     1, 1, 40, 1, 11, 3, 7, 1, 7, 1, 1, 5, 1, 49]
    assert gamma['checkpoints']['prefix']['result']['full_cf_prefix'][:31] == printed_gamma
    result['gamma_reused_prefix'] = printed_gamma
    result['e_and_phi'] = 'General formulas already proved in euclid-analytic.md and euclid-quadratic.md; printed patterns agree.'
    return result


def finite_identities():
    h, s = F(0), [F(0)]
    for n in range(1, 257):
        s.append(1+sum(s)/n)
        h += F(1, n)
        assert s[n] == h
        lhs = sum(n % k for k in range(1, n+1))
        rhs = n*n-sum((n//q)*(n//q+1)//2 for q in range(1, n+1))
        assert lhs == rhs
    def steps(u, v):
        n = 0
        while v:
            u, v = v, u % v
            n += 1
        return n
    assert [steps(k, 5) for k in range(5)] == [1, 2, 3, 4, 3]
    return {'harmonic_recurrences': 256, 'remainder_sum_identities': 256,
            'T5': '13/5'}


def logarithmic_constants():
    from flint import arb, ctx
    ctx.dps = 90
    phi = (1+arb(5).sqrt())/2
    slope_e = 1/phi.log()
    slope_10 = arb(10).log()/phi.log()
    intercept = (3-phi).log()/phi.log()
    assert arb('4.7849') < slope_10 < arb('4.7850')
    assert arb('.6722') < intercept < arb('.6723')
    # Strict inequalities justify the decimal relaxation on p373 for N>=1.
    assert slope_10 < arb('4.8') and intercept-1 < arb('-.32')
    vals = {'natural_log_slope': slope_e, 'decimal_log_slope': slope_10,
            'intercept': intercept, 'remainder_constant': 1-arb.pi()**2/12}
    return {name: str(v) for name, v in vals.items()}


if __name__ == '__main__':
    started = time.monotonic()
    result = {'pid': os.getpid(), 'scope': 'TAOCP2 pp358--361, rounded bound p373',
              'checkpoints': {}}
    out = ROOT/'results/euclid-text.json'
    for name, fn in [('constants', constants), ('finite', finite_identities),
                     ('logarithms', logarithmic_constants)]:
        t = time.monotonic()
        result['checkpoints'][name] = {'result': fn(), 'seconds': time.monotonic()-t}
        out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
        print('passed', name, flush=True)
    result['seconds'] = time.monotonic()-started
    result['status'] = 'passed'
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print('all passed', result['pid'], result['seconds'], flush=True)
