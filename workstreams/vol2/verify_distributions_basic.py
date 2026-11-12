"""Exact checks for TAOCP 2, section 3.4.1 A/B and exercises 1--9, 13--15.

General arguments are in notes/distributions-basic.md; these finite tests
independently count outputs and check the resulting probability/covariance laws.
Use --resume to retain completed blocks.
"""
from collections import Counter
from fractions import Fraction as Q
import json
from pathlib import Path
from random import Random
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/distributions-basic.json'


def integer_choices():
    cases = comparisons = 0
    for m in range(1, 129):
        for k in range(1, 161):
            high = Counter(k*u//m for u in range(m))
            low = Counter(u % k for u in range(m))
            quotient, residue = divmod(m, k)
            accepted = Counter(u % k for u in range(k*quotient))
            for r in range(k):
                want = ((m*(r+1)+k-1)//k - (m*r+k-1)//k)
                assert high[r] == want
                assert abs(Q(want, m)-Q(1, k)) < Q(1, m)
                assert low[r] == quotient + (r < residue)
                assert accepted[r] == quotient
                comparisons += 1
            h = (k+1)//2
            assert sum(v for r, v in low.items() if 2*r < k) == quotient*h+min(residue, h)
            cases += 1
    examples = []
    for m, k in [(12, 4), (256, 86), (12, 8), (256, 170), (256, 171)]:
        p = Q(sum(2*(u % k) < k for u in range(m)), m)
        examples.append(dict(m=m, k=k, lower_half_probability=str(p)))
    assert examples[0]['lower_half_probability'] == '1/2'
    assert examples[2]['lower_half_probability'] == '2/3'
    return dict(models=cases, individual_counts=comparisons, examples=examples,
                formula='m=q*k+s; Pr(U mod k < k/2)=(q*ceil(k/2)+min(s,ceil(k/2)))/m')


def compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total+1):
        for tail in compositions(total-first, length-1):
            yield (first,)+tail


def alias_table(weights):
    k = len(weights)
    remaining = sorted((Q(w, sum(weights)), i) for i, w in enumerate(weights))
    p, y = [None]*k, [None]*k
    while len(remaining) > 1:
        q1, i = remaining.pop(0)
        qn, j = remaining.pop()
        assert q1 <= Q(1, k) <= qn
        p[i], y[i] = k*q1, j
        remaining.append((qn-(Q(1, k)-q1), j))
        remaining.sort()
    last, i = remaining[0]
    assert last == Q(1, k)
    p[i], y[i] = Q(1), i
    return p, y


def alias_choices():
    cases = probes = 0
    for k in range(1, 8):
        for total in range(1, 11):
            for weights in compositions(total, k):
                p, y = alias_table(weights)
                mass = [Q(0) for _ in weights]
                for i in range(k):
                    assert 0 <= p[i] <= 1
                    mass[i] += p[i]/k
                    mass[y[i]] += (1-p[i])/k
                    assert Q(weights[y[i]], total) >= Q(1, k)
                    threshold = (i+p[i])/k
                    for v in {Q(0), p[i]/2, p[i], (1+p[i])/2}:
                        if v == 1:
                            continue
                        u = (i+v)/k
                        assert int(k*u) == i
                        assert (v < p[i]) == (u < threshold)
                        probes += 1
                assert mass == [Q(w, total) for w in weights]
                cases += 1
    p = [Q(x, 9) for x in [0, 0, 4, 8, 9, 7, 9, 9, 9, 7, 7, 8, 4, 0, 0, 0]]
    y = [5, 9, 7, 4, 4, 6, 6, 7, 8, 8, 4, 7, 10, 6, 7, 8]
    mass = [Q(0) for _ in p]
    for i in range(16):
        mass[i] += p[i]/16
        mass[y[i]] += (1-p[i])/16
    dice = Counter(a+b for a in range(1, 7) for b in range(1, 7))
    assert mass == [Q(dice[i], 36) for i in range(16)]
    return dict(exhaustive_distributions=cases, threshold_probes=probes,
                dice_probability_vector=[str(x) for x in mass],
                last_entry_convention='P=1, unused Y=self; stop before redundant deletion/reinsertion')


def continuous_identities():
    import sympy as s
    x = s.symbols('x', positive=True)
    f = s.sqrt(2/s.pi)*s.exp(-x*x/2)
    assert s.simplify(s.diff(f, x, 2)-(x*x-1)*f) == 0
    disk = 2/s.pi*(s.asin(x)+x*s.sqrt(1-x*x))
    assert s.simplify(s.diff(disk, x)-4/s.pi*s.sqrt(1-x*x)) == 0
    assert disk.subs(x, 0) == 0 and disk.subs(x, 1) == 1
    logistic = 2/s.pi*s.asin(s.sqrt(x))
    assert s.simplify(s.diff(logistic, x)-1/(s.pi*s.sqrt(x*(1-x)))) == 0
    assert logistic.subs(x, 0) == 0 and logistic.subs(x, 1) == 1
    bad_mass = s.sqrt(s.pi/2)
    import mpmath as mp
    mp.mp.dps = 60
    return dict(disk_cdf=str(disk), normal_second_derivative=str(s.diff(f, x, 2)),
                polar_mean=str(4/mp.pi), polar_standard_deviation=str(4/mp.pi*mp.sqrt(1-mp.pi/4)),
                logistic_cdf=str(logistic), printed_logistic_total_mass=str(bad_mass),
                printed_logistic_total_mass_decimal=str(mp.sqrt(mp.pi/2)),
                scope='Symbolic local identities supplement the elementary distribution proofs; no simulation as proof.')


def covariance():
    rng = Random(34113)
    cases = singular = 0
    for n in range(1, 8):
        for rank_cap in range(n+1):
            for _ in range(8):
                b = [[rng.randrange(-3, 4) for _ in range(rank_cap)] for _ in range(n)]
                c = [[sum(b[i][h]*b[j][h] for h in range(rank_cap)) for j in range(n)] for i in range(n)]
                l = [[Q(i == j) for j in range(n)] for i in range(n)]
                d = []
                for j in range(n):
                    pivot = Q(c[j][j])-sum(l[j][h]**2*d[h] for h in range(j))
                    assert pivot >= 0
                    d.append(pivot)
                    for i in range(j+1, n):
                        residual = Q(c[i][j])-sum(l[i][h]*l[j][h]*d[h] for h in range(j))
                        if pivot == 0:
                            assert residual == 0
                            l[i][j] = Q(0)
                        else:
                            l[i][j] = residual/pivot
                for i in range(n):
                    for j in range(n):
                        assert sum(l[i][h]*d[h]*l[j][h] for h in range(n)) == c[i][j]
                cases += 1
                singular += any(x == 0 for x in d)
    return dict(exact_gram_models=cases, singular_models=singular, dimensions='1..7',
                factorization='C=L*diag(d)*L^T, so A=L*diag(sqrt(d)) gives A*A^T=C, including zero pivots.')


def main():
    out = json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name, fn in [('integer_choices', integer_choices), ('alias_choices', alias_choices),
                     ('continuous_identities', continuous_identities), ('covariance', covariance)]:
        if name in out:
            continue
        print('START', name, flush=True)
        out[name] = fn()
        OUT.write_text(json.dumps(out, indent=2)+'\n')
        print('PASS', name, flush=True)
    print('ALL BLOCKS COMPLETE', flush=True)


if __name__ == '__main__':
    main()
