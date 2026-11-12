"""Reproduce the exploratory exact bounds for TAOCP2 3.3.3-19.

These are finite checks, not a proof of the conjectured general bounds.
The initial two censuses ran inline; their aggregate output is preserved in
results/discrepancy-frontier.json. Use --resume to preserve completed blocks.
"""
import argparse
from fractions import Fraction as Q
import json
from math import gcd
from pathlib import Path

from verify_dedekind import psi, sigma

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/discrepancy-frontier.json'


def quotients(a, m):
    out = []
    while a:
        q, r = divmod(m, a)
        out.append(q)
        m, a = a, r
    return out


def all_rectangles():
    import numpy as np
    count = 0
    bad = []
    top = Q(0)
    witness = None
    for m in range(2, 161):
        for a in range(1, m):
            if gcd(a, m) != 1:
                continue
            qs = quotients(a, m)
            v = np.zeros(m + 1, dtype=np.int64)
            ys = np.arange(m + 1)
            best = 0
            for w in range(1, m):
                x = a * (w - 1) % m
                v[x + 1:] += m
                v -= ys
                best = max(best, int(v.max() - v.min()))
            ratio = Q(4 * best, m * sum(qs))
            if ratio > top:
                top, witness = ratio, dict(m=m, a=a, numerator=best, quotients=qs)
            if ratio > 1:
                bad.append(dict(m=m, a=a, numerator=best, quotients=qs))
            count += 1
    return dict(cases=count, max_modulus=160, exceptions=bad,
                maximum_ratio=str(top), first_maximizer=witness)


def centered_walk(a, m):
    s = lo = hi = 0
    for j in range(m):
        s += 2 * (a * j % m) - (m - 1)
        lo, hi = min(lo, s), max(hi, s)
    return Q(hi - lo, 2 * m)


def centered_walks():
    count = equal = 0
    bad = []
    for m in range(2, 501):
        for a in range(1, m):
            if gcd(a, m) != 1:
                continue
            actual, bound = centered_walk(a, m), Q(sum(quotients(a, m)), 8)
            if actual > bound:
                bad.append(dict(a=a, m=m, actual=str(actual), bound=str(bound)))
            equal += actual == bound
            count += 1
    return dict(cases=count, max_modulus=500, exceptions=bad, equality_cases=equal)


def midpoint_identity():
    cases = rectangles = 0
    for m in range(2, 22):
        for a in range(1, m):
            if gcd(a, m) != 1:
                continue
            ap = pow(a, -1, m)
            tau = []
            for c in range(m):
                direct = 12 * sum(Q(2*j+1-m, 2*m) *
                                  Q(2*((a*j+c) % m)+1-m, 2*m)
                                  for j in range(m))
                formula = (sigma(a, m, c) + 6*psi(Q(ap*c, m))
                           - 6*psi(Q(c, m)) + 3*(c == 0) - Q(3, m))
                assert direct == formula, (a, m, c, direct, formula)
                tau.append(direct)
                cases += 1
            assert max(tau)-min(tau) == 12*centered_walk(ap, m)
            # The exact four-corner formula has no boundary correction.
            for w in range(1, m):
                for bot, top in {(0, 1), (0, m), (1, m), (m//3, 2*m//3+1)}:
                    n = sum(bot <= a*x % m < top for x in range(w))
                    q = (tau[-bot % m] - tau[-top % m]
                         + tau[(a*w-top) % m] - tau[(a*w-bot) % m]) / 12
                    assert q == Q(n)-Q(w*(top-bot), m)
                    rectangles += 1
    return dict(cases=cases, rectangles=rectangles,
                scope='Midpoint sums, sigma identity, centered-walk oscillation, exact four-corner counts.')


def exact_extrema_and_reciprocity():
    import numpy as np
    cases = recurrences = brute_cases = 0
    for m in range(2, 101):
        for a in range(1, m):
            if gcd(a, m) != 1:
                continue
            ap = pow(a, -1, m)
            # tau*m, with an irrelevant additive constant removed.
            tau = [0]
            for c in range(m-1):
                j = -ap*(c+1) % m
                tau.append(tau[-1]-6*(2*j+1-m))
            assert all(tau[c] == tau[(a-1-c) % m] for c in range(m))
            low = min(range(m), key=tau.__getitem__)
            high = max(range(m), key=tau.__getitem__)
            w = ap*(a-1-high-low) % m
            bot, height = -high % m, (high-low) % m
            assert 0 < w < m and 0 < height < m
            number = sum((a*x-bot) % m < height for x in range(w))
            numerator = m*number-w*height
            span = tau[high]-tau[low]
            assert 6*numerator == span
            assert Q(numerator, m) == 2*centered_walk(a, m)
            if m <= 60:
                # Independent exhaustive rectangle optimization, a new
                # comparison against the exact extremum/witness identity.
                values = np.zeros(m+1, dtype=np.int64)
                ys = np.arange(m+1)
                brute = 0
                for width in range(1, m):
                    values[a*(width-1) % m+1:] += m
                    values -= ys
                    brute = max(brute, int(values.max()-values.min()))
                assert numerator == brute
                brute_cases += 1

            # Integer-scaled independent prefix sums for the reciprocity.
            tail = [0]
            for j in range(1, a):
                tail.append(tail[-1]+2*(m*j % a)-a)
            direct = 0
            for n in range(1, m):
                direct += 2*(a*n % m)-m
                b, r = divmod(a*n, m)
                assert a*direct + m*tail[b] == r*(a+r-m)
                recurrences += 1
            cases += 1
    assert centered_walk(3, 10) == Q(3, 4)
    assert Q(3, 4) > Q(3, 8)+centered_walk(1, 3)
    return dict(models=cases, brute_rectangle_models=brute_cases,
                exact_reciprocities=recurrences,
                scope='Proves/checks mD=2R and a maximum rectangle witness; does not prove R<=sum(quotients)/8.',
                rejected_recurrence_example=dict(a=3, m=10, actual='3/4', proposed='17/24'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    result = json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}
    for name, fun in [('all_rectangles', all_rectangles),
                      ('centered_walks', centered_walks),
                      ('midpoint_identity', midpoint_identity),
                      ('exact_extrema_and_reciprocity', exact_extrema_and_reciprocity)]:
        if name in result:
            continue
        result[name] = fun()
        OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
        print(name, result[name], flush=True)
