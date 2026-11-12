"""Inspect archived spectral certificates; no lattice search or LLL rerun.

Checks transforms, witnesses and stored rounding intervals. The lower-bound
argument remains the reviewed exact sphere enumeration and its archived run.
Also records short modular witnesses for specific claims in the prose.
"""
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import gcd, prod
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def det(matrix):
    a = [list(map(Q, row)) for row in matrix]
    result = Q(1)
    for j in range(len(a)):
        k = next((i for i in range(j, len(a)) if a[i][j]), None)
        if k is None:
            return Q(0)
        if k != j:
            a[k], a[j] = a[j], a[k]
            result = -result
        pivot = a[j][j]
        result *= pivot
        for i in range(j+1, len(a)):
            q = a[i][j]/pivot
            a[i] = [x-q*y for x, y in zip(a[i], a[j])]
    return result


def rounding_interval(value):
    mantissa, exponent = value.lower().split('e') if 'e' in value.lower() else (value, '0')
    places = len(mantissa.split('.')[1]) if '.' in mantissa else 0
    half = Q(10)**(int(exponent)-places)/2
    return Q(value)-half, Q(value)+half


def main():
    started = time.monotonic()
    names = ['spectral-table.json', 'spectral-details.json', 'spectral-extensions.json']
    data = {n: json.loads((ROOT/'results'/n).read_text()) for n in names}
    table = data[names[0]]
    assert table['complete'] and len(table['rows']) == 29
    models = witnesses = 0
    mismatch = []
    for line, row in table['rows'].items():
        assert row['complete'] and len(row['dimensions']) == 5
        a, m = row['a'], row['m']
        for dimension, entry in row['dimensions'].items():
            t = int(dimension)
            if a is None:
                p = 2**31-1
                coeff = [[1, 0], [0, 1]]
                while len(coeff) < t:
                    coeff.append([(271828183*coeff[-1][j]-314159269*coeff[-2][j]) % p
                                  for j in range(2)])
                original = [[p, 0]+[0]*(t-2), [0, p]+[0]*(t-2)]
                original += [[-coeff[j][0], -coeff[j][1]]+
                             [int(k == j) for k in range(2, t)] for j in range(2, t)]
                assert m == p*p
            else:
                original = [[m]+[0]*(t-1)] + [
                    [-pow(a, j, m)]+[int(k == j) for k in range(1, t)] for j in range(1, t)]
            cert = entry['independent']
            transform, basis = cert['transform'], cert['basis']
            assert abs(det(transform)) == 1
            assert [[sum(transform[i][k]*original[k][j] for k in range(t))
                     for j in range(t)] for i in range(t)] == basis
            assert abs(det(basis)) == m
            star, norms = [], []
            for vector in basis:
                orthogonal = list(map(Q, vector))
                for prev, norm in zip(star, norms):
                    projection = dot(vector, prev)/norm
                    orthogonal = [x-projection*y for x, y in zip(orthogonal, prev)]
                norm = dot(orthogonal, orthogonal)
                assert norm > 0 and all(dot(orthogonal, prev) == 0 for prev in star)
                star.append(orthogonal)
                norms.append(norm)
            assert norms == list(map(Q, cert['gram_schmidt_squared']))
            assert prod(norms) == m*m
            assert cert['squared'] == entry['squared']
            vectors = cert['vectors']
            assert vectors and len(vectors) == len({tuple(v) for v in vectors})
            for vector in vectors:
                assert any(vector) and dot(vector, vector) == entry['squared']
                if a is None:
                    assert all(sum(vector[j]*coeff[j][k] for j in range(t)) % p == 0
                               for k in range(2))
                else:
                    assert sum(vector[j]*pow(a, j, m) for j in range(t)) % m == 0
                witnesses += 1
            if not entry['squared_matches']:
                mismatch.append([int(line), t, entry['printed_squared']])
            models += 1
    assert models == 145 and mismatch == [[29, 5, '2e165']]

    details = data[names[1]]
    intervals = []
    for record in details['table_intervals']['table']:
        intervals.extend([record['lg'], record['merit']])
    intervals.extend(details['table_intervals']['upper_bounds'])
    intervals.extend(details['examples']['worked_example_decimals'])
    intervals.append(details['examples']['mu9'])
    intervals.extend(details['errata_and_periods']['killingbeck']['merits'])
    for record in intervals:
        low, high = map(Q, record['enclosure'])
        lower_round, upper_round = rounding_interval(record['printed'])
        assert lower_round < low <= high < upper_round

    randu = data[names[2]]['shorter_periods']['randu_unchanged']
    for r in randu:
        assert dot(r['witness'], r['witness']) == r['squared']
        assert sum(v*pow(65539, j, 2**30) for j, v in enumerate(r['witness'])) % 2**30 == 0

    # Newly checked prose claims for rows17–19; primality of p and its factor
    # list already have a reviewed exact certificate in spectral-details.
    p = 2**31-1
    factors = [2, 3, 7, 11, 31, 151, 331]
    primitive = {}
    for a in [314159269, 62089911, 16807]:
        values = {q: pow(a, (p-1)//q, p) for q in factors}
        assert pow(a, p-1, p) == 1 and all(x != 1 for x in values.values())
        primitive[a] = values
    p2 = 2**31-249
    separating_power = pow(48271, p2-1, p)
    assert separating_power != 1 and p2 < p
    joint_period = (p-1)*(p2-1)//gcd(p-1, p2-1)
    assert joint_period == details['errata_and_periods']['combined']['period']
    result = {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Stored transforms, basis determinants, orthogonal norms, witnesses and rounding-interval inclusion; no new LLL or lattice enumeration.',
        'minimum_lower_bound_scope': 'Accepted from reviewed original rational sphere-enumeration program and archived successful run; witness validation alone is not a minimum proof.',
        'table_certificates': models, 'minimum_witnesses': witnesses,
        'stored_intervals_checked': len(intervals),
        'approximation_candidate': mismatch,
        'randu_stronger_congruence_witnesses': len(randu),
        'new_primitive_root_witnesses': primitive,
        'combined_output_period': {'value': joint_period, 'p1': p, 'p2': p2,
                                   'a1_power_p2_minus_1_mod_p1': separating_power,
                                   'proof': 'For nonzero seeds, output period T implies (a1^T-1)X_n = Y_(n+T)-Y_n mod p1. Comparing n and n+p2-1 forces a1^T=1. Then Y_(n+T)=Y_n as both are between1 and p2-1<p1, forcing a2^T=1.'},
        'inputs': [{'path': 'workstreams/vol2/results/'+n,
                    'sha256': sha256((ROOT/'results'/n).read_bytes()).hexdigest()} for n in names],
        'seconds': time.monotonic()-started,
    }
    output = ROOT/'results/sequential-spectral-certificates.json'
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['table_certificates', 'minimum_witnesses',
                     'stored_intervals_checked', 'randu_stronger_congruence_witnesses', 'seconds']}))


if __name__ == '__main__':
    main()
