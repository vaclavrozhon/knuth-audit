"""Small exact interval certificate for every printed decimal in MPR5.

The infinite tail is bounded analytically; no game simulation or large scores.
"""
from datetime import datetime, timezone
from fractions import Fraction as Q
from pathlib import Path
import json
import os
import time


def decimal(n, places):
    s = str(n).zfill(places+1)
    return s[:-places]+'.'+s[-places:]


def outward(bounds, places=24):
    lo, hi = bounds
    scale = 10**places
    a = lo.numerator*scale // lo.denominator
    b = -((-hi.numerator*scale) // hi.denominator)
    return [decimal(a, places), decimal(b, places)]


def main():
    started = time.perf_counter()
    K = 12
    w = [Q(1, 2**(k*k)) for k in range(K+1)]
    Dlo = sum(w)
    tail = Q(1, 2**((K+1)**2)) / (1-Q(1, 2**(2*K+3)))
    Dhi = Dlo+tail
    even = sum(w[::2])
    intervals = {'D': (Dlo, Dhi), 'E': (even/Dhi, (even+tail)/Dlo)}
    numerators = {'A_gt_B': Q(0), 'A_lt_B': Q(0), 'A_eq_B': Q(0), 'AB_positive': Q(0)}
    for j, a in enumerate(w):
        for k, c in enumerate(w):
            mass = a*c
            # Latent j chooses A=m_j for even j, otherwise0.
            # Latent k chooses B=m_k for odd k, otherwise0.
            if j % 2 == 0 and (k % 2 == 0 or j > k):
                numerators['A_gt_B'] += mass
            elif k % 2 == 1 and (j % 2 == 1 or k > j):
                numerators['A_lt_B'] += mass
            else:
                assert j % 2 == 1 and k % 2 == 0
                numerators['A_eq_B'] += mass
            if j % 2 == 0 and k % 2 == 1:
                numerators['AB_positive'] += mass
    assert sum(numerators[key] for key in ['A_gt_B', 'A_lt_B', 'A_eq_B']) == Dlo**2
    omitted_pair_mass = Dhi**2-Dlo**2
    for key, numerator in numerators.items():
        intervals[key] = (numerator/Dhi**2, (numerator+omitted_pair_mass)/Dlo**2)
    p1000 = Q(99, 100)**1000
    intervals['P1000'] = (p1000, p1000)
    assert p1000 < Q(1, 10000)
    printed = {'D': '1.56447', 'E': '0.67915', 'A_gt_B': '0.47402',
               'A_lt_B': '0.30807', 'A_eq_B': '0.21790',
               'AB_positive': '0.21790', 'P1000': '0.000043'}
    certificates = {}
    for key, value in printed.items():
        center = Q(value)
        half_unit = Q(1, 2*10**len(value.split('.')[1]))
        lo, hi = intervals[key]
        assert center-half_unit <= lo <= hi < center+half_unit
        certificates[key] = {
            'printed': value,
            'outward_decimal_bounds': outward((lo, hi)),
            'rounding_interval': [str(center-half_unit), str(center+half_unit)],
            'exact_rounding_inequalities_pass': True,
        }
        if key != 'P1000':
            certificates[key]['exact_rational_bounds'] = [str(lo), str(hi)]
    result = {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'All MPR5 printed decimals, using13 one-dimensional weights,169 latent pairs and a rigorous infinite-tail bound. No simulation or large-score enumeration.',
        'K': K,
        'D_partial_sum': str(Dlo),
        'unnormalized_tail_upper_bound': str(tail),
        'omitted_pair_mass_upper_bound': str(omitted_pair_mass),
        'certificates': certificates,
        'P1000_below_0_0001_exact': True,
        'elapsed_seconds': time.perf_counter()-started,
        'execution_nice': os.getpriority(os.PRIO_PROCESS, 0),
        'old_tests_repeated': 0,
    }
    root = Path(__file__).resolve().parent
    (root/'results/sequential/mpr-005-probabilities.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({'bounds': {k: v['outward_decimal_bounds'] for k, v in certificates.items()},
                      'elapsed_seconds': result['elapsed_seconds'],
                      'execution_nice': result['execution_nice']}))


if __name__ == '__main__':
    main()
