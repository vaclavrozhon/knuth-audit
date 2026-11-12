#!/usr/bin/env python3
"""Exact short sums; only 80 small binary matrices validate the count identities.

No MMIX/assembler, no old benchmark, no enumeration of the 9x8 input space.
The proof of the formulas is notes/exercises-1.3.2-020-binary-recovery.md.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import time

BASE = Path(__file__).resolve().parent


def expectations(m, n):
    q = F(1, 2**m)
    b = 1-q
    c = 1-F(1, 2**n)
    a = 1-b**n
    success_b = 1-c**m
    geom_c = sum(c**r for r in range(m))
    w0, w1 = F(1, 2)-q, F(1, 2)
    # Row reach is shared by both algorithms.
    reach_b = sum(b**n+c**r-1 for r in range(m))
    reach = a+reach_b
    success = a+success_b
    # I: stores A and strict minimum changes B in every reached full row scan.
    row_a = F(n, 2)+sum(F(1, 2**k) for k in range(1, n+1))
    row_b = F(1, 2)-F(1, 2**n)
    row_a_b = n*w0*b**(n-1)+sum(w1**k*b**(n-k) for k in range(1, n+1))
    row_b_b = w1*b**(n-1)-w1**n
    stores = (m-1)*row_a_b+(geom_c-(m-1))*row_a
    changes = (m-1)*row_b_b+(geom_c-(m-1))*row_b
    zeros_b = m*n*w0*b**(n-1)+(geom_c-m)*F(n, 2)
    prefix = sum(b**j*(1-b**(n-1-j)) for j in range(n))
    columns_a = a+w0*prefix
    columns_b = zeros_b+success_b
    loads_a = m*a+sum(F(f, 2**f) for f in range(2, m+1))*prefix
    loads_b = n*sum(
        F(f, 2**f)*(
            (f-1)*b**(n-1)
            +F(1, 2)*sum(
                b**(n-1)+(1-F(1, 2**(n-1)))*c**(r-f-1)-1
                for r in range(f+1, m+1)
            )
        ) for f in range(1, m+1)
    )+m*success_b
    columns, loads = columns_a+columns_b, loads_a+loads_b
    # II: scan-prefix lengths conditional on all columns being nonzero.
    scan_b = sum(F(1, 2**k)*(b**(n-k)+c**(r-1)-1)
                 for r in range(1, m+1) for k in range(n))
    equals_b = sum(F(1, 2**k)*(b**(n-k)+c**(r-1)-1)
                   for r in range(1, m+1) for k in range(1, n+1))
    scan = n*a+scan_b
    equals = F(n, 2)-n*w0*b**(n-1)+equals_b
    i = dict(R=reach, A=stores, B=changes, C=columns, D=loads, S=success)
    ii = dict(R=reach, K=scan, H=equals, S=success)
    i['mems'] = n*reach+stores+columns+loads
    i['oops'] = (6*n-6)*reach+9*stores-2*changes+2*columns+7*loads+3*success+6
    ii['mems'] = (m+1)*n+scan+equals
    ii['oops'] = 5*m*n+4*n+11+9*scan-2*reach+5*equals+4*success
    return {'I': i, 'II': ii}


def direct_counts(matrix):
    m, n = len(matrix), len(matrix[0])
    # Scan order is explicit: rows top-to-bottom in this representation;
    # row minima right-to-left, candidate columns in ascending order.
    i = dict(R=0, A=0, B=0, C=0, D=0, S=0)
    for row in matrix:
        i['R'] += 1
        current = row[-1]
        i['A'] += 1
        columns = [n-1]
        for j in range(n-2, -1, -1):
            if row[j] < current:
                current = row[j]
                columns = [j]
                i['A'] += 1
                i['B'] += 1
            elif row[j] == current:
                columns.append(j)
                i['A'] += 1
        for j in reversed(columns):
            i['C'] += 1
            for other in matrix:
                i['D'] += 1
                if other[j] > current:
                    break
            else:
                i['S'] = 1
                return_i = True
                break
        else:
            return_i = False
        if return_i:
            break
    maxima = [max(row[j] for row in matrix) for j in range(n)]
    z = min(maxima)
    ii = dict(R=0, K=0, H=0, S=0)
    for row in matrix:
        ii['R'] += 1
        for value in reversed(row):
            ii['K'] += 1
            if value < z:
                break
            if value == z:
                ii['H'] += 1
        else:
            ii['S'] = 1
            break
    return {'I': i, 'II': ii}


def serialized(x):
    if isinstance(x, F):
        return {'numerator': x.numerator, 'denominator': x.denominator, 'decimal': float(x)}
    if isinstance(x, dict):
        return {k: serialized(v) for k, v in x.items()}
    if isinstance(x, list):
        return [serialized(v) for v in x]
    return x


def main():
    started = time.monotonic()
    validations = []
    for m, n in [(2, 2), (2, 3)]:
        totals = {'I': {k: 0 for k in ['R', 'A', 'B', 'C', 'D', 'S']},
                  'II': {k: 0 for k in ['R', 'K', 'H', 'S']}}
        count = 0
        for bits in product([0, 1], repeat=m*n):
            matrix = [bits[r*n:(r+1)*n] for r in range(m)]
            direct = direct_counts(matrix)
            for method in totals:
                for k in totals[method]:
                    totals[method][k] += direct[method][k]
            count += 1
        formula = expectations(m, n)
        for method in totals:
            for k in totals[method]:
                assert F(totals[method][k], count) == formula[method][k], (m, n, method, k)
        validations.append({'rows': m, 'columns': n, 'binary_matrices': count,
                            'all_count_expectations_match': True})
    result = expectations(9, 8)
    difference = {k: result['I'][k]-result['II'][k] for k in ['mems', 'oops']}
    output = {'purpose': 'Exact binary9x8 expectations from finite proven sums; no9x8 enumeration.',
              'small_independent_count_validations': validations,
              'expected_counts': serialized(result),
              'solution_I_minus_II': serialized(difference),
              'elapsed_seconds': time.monotonic()-started}
    (BASE/'results/saddle20-binary-expectations.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({'elapsed_seconds': output['elapsed_seconds'], 'small_matrices': 80,
                      'I': {k: float(result['I'][k]) for k in ['mems', 'oops']},
                      'II': {k: float(result['II'][k]) for k in ['mems', 'oops']}}))


if __name__ == '__main__':
    main()
