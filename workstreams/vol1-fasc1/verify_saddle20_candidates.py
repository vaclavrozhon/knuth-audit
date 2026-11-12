#!/usr/bin/env python3
"""Only the new candidate variant and new exact distinct comparison bounds.

No old verifier is executed. Binary reference expectations are read from the
saved certificate; no9x8 matrix space, MMIX or assembler is run.
"""
from fractions import Fraction as F
from math import comb
from itertools import product
from pathlib import Path
import json
import time

BASE = Path(__file__).resolve().parent


def integral(m, k, n):
    return m*sum(F((-1)**(a+b)*comb(k, a)*comb(n-1, b), m*(b+1)+a)
                 for a in range(k+1) for b in range(n))


def distinct(m, n):
    p = F(m+n, comb(m+n, m))
    skipped = F(m-1, 2)*p
    rows = m-skipped
    harmonic = sum(F(1, k) for k in range(1, n+1))
    candidate_scan = F(0)
    all_scan = F(0)
    equals = F(0)
    for j in range(n):
        first = (n-j)*integral(m, j, n-j)
        second = j*integral(m, j-1, n-j+1) if j else 0
        candidate_scan += first+second
        all_scan += m*first+second
        equals += integral(m, j, n-j)
    dc = F((m+1)*n, n-1)-F(m+n, n-1)*p
    star_i_mems = m*n+m*harmonic+m+dc
    star_i_oops = 6*m*n+7*m*harmonic-2*m+7*dc+6
    i = {'mems_lower': star_i_mems-(2*n+m+1)*skipped,
         'mems_upper': star_i_mems-(n+3)*skipped,
         'oops_lower': star_i_oops-(13*n+7*m-2)*skipped+3*p,
         'oops_upper': star_i_oops-(6*n+12)*skipped+3*p}
    ii_star_mems = (m+1)*n+all_scan+equals
    ii_star_oops = 5*m*n+4*n+11+9*all_scan-2*rows+5*equals+4*p
    ii = {'mems_lower': ii_star_mems-n*skipped,
          'mems_upper': ii_star_mems-skipped,
          'oops_lower': ii_star_oops-9*n*skipped,
          'oops_upper': ii_star_oops-9*skipped}
    iii = {'R': rows, 'C': F(1), 'K': candidate_scan, 'S': p,
           'mems': m*n+rows+candidate_scan,
           'oops': 5*m*n+4*n+10+6*rows+8*candidate_scan+3*p}
    assert iii['mems'] < ii['mems_lower'] < ii['mems_upper'] < i['mems_lower']
    assert iii['oops'] < ii['oops_lower'] < ii['oops_upper'] < i['oops_lower']
    return {'I_bounds': i, 'II_bounds': ii, 'III_exact': iii,
            'all_row_K_II': all_scan, 'all_row_H_II': equals,
            'expected_rows_skipped_after_saddle': skipped}


def binary_counts(m, n):
    b = 1-F(1, 2**m)
    c = 1-F(1, 2**n)
    a = 1-b**n
    def q(r, k):
        return F(1, 2**k)*(b**(n-k)+c**(r-1)-1)
    rows = a+sum(q(r, 0) for r in range(1, m+1))
    candidates = a+sum(q(r, 1) for r in range(1, m+1))
    scan = n*a+sum(q(r, 1)+sum(q(r, k) for k in range(1, n))
                   for r in range(1, m+1))
    success = a+1-c**m
    return dict(R=rows, C=candidates, K=scan, S=success)


def direct_new_counts(matrix):
    m, n = len(matrix), len(matrix[0])
    maxima = [max(row[j] for row in matrix) for j in range(n)]
    z = min(maxima)
    best = max(j for j in range(n) if maxima[j] == z)
    out = dict(R=0, C=0, K=0, S=0)
    for row in matrix:
        out['R'] += 1
        if row[best] != z:
            continue
        out['C'] += 1
        for value in reversed(row):
            out['K'] += 1
            if value < z:
                break
        else:
            out['S'] = 1
            break
    return out


def serial(x):
    if isinstance(x, F):
        return dict(numerator=x.numerator, denominator=x.denominator, decimal=float(x))
    if isinstance(x, dict):return {k: serial(v) for k, v in x.items()}
    if isinstance(x, list):return [serial(v) for v in x]
    return x


def main():
    start = time.monotonic()
    checks = []
    # Only the new method; the two earlier program verifiers are not rerun.
    for m, n in [(2, 2), (3, 2)]:
        totals = dict(R=0, C=0, K=0, S=0)
        count = 0
        for bits in product([0, 1], repeat=m*n):
            values = direct_new_counts([bits[r*n:(r+1)*n] for r in range(m)])
            for k, v in values.items():totals[k] += v
            count += 1
        expected = binary_counts(m, n)
        assert all(F(v, count) == expected[k] for k, v in totals.items())
        checks.append(dict(rows=m, columns=n, matrices=count, new_method_counts_match=True))
    m, n = 9, 8
    binary = binary_counts(m, n)
    binary['mems'] = m*n+binary['R']+binary['K']
    binary['oops'] = 5*m*n+4*n+11+6*binary['R']-binary['C']+8*binary['K']+3*binary['S']
    saved = json.loads((BASE/'results/saddle20-binary-expectations.json').read_text())
    for cost in ['mems', 'oops']:
        ref = saved['expected_counts']['II'][cost]
        assert binary[cost] < F(ref['numerator'], ref['denominator'])
    distinct_result = distinct(m, n)
    result = {'purpose': 'Concrete general third MMIX method; exact new counts and fixed9x8 comparisons.',
              'binary_new_method_checks': checks, 'binary_9x8': serial(binary),
              'distinct_9x8': serial(distinct_result),
              'elapsed_seconds': time.monotonic()-start}
    (BASE/'results/saddle20-candidates-expectations.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'elapsed_seconds': result['elapsed_seconds'], 'new_small_cases': 80,
                      'binary_III': {k: float(binary[k]) for k in ['mems', 'oops']},
                      'distinct_III': {k: float(distinct_result['III_exact'][k]) for k in ['mems', 'oops']}}))


if __name__ == '__main__':main()
