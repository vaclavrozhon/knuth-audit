#!/usr/bin/env python3
"""Aggregate the completed rho census; independently compare prime counts.

No Pollard iterates are recomputed. Integer comparisons establish the extrema;
only the descriptive average uses floating-point square roots.
"""
from pathlib import Path
from decimal import Decimal, localcontext
from fractions import Fraction
from math import fsum, sqrt
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parent

def main():
    rows = list(csv.reader((ROOT/'results/factoring-rho-extended.csv').open()))
    counts = list(csv.reader((ROOT/'results/rho-prime-counts.csv').open()))
    assert len(rows) == len(counts) == 999
    assert (ROOT/'results/factoring-rho-extended.log').read_text().rstrip().endswith('ALL SEGMENTS COMPLETE')
    prior = json.loads((ROOT/'results/factoring-rho.json').read_text())
    assert prior['status'] == 'passed'
    small = prior['checkpoints']['small_census']['result']
    total, total_m = small['primes'], small['sum_iterations']
    maximum = dict(small['maximum'])
    ratio = dict(small['ratio_maximum'])
    roots = []
    root_discrepancies = []
    seconds = []
    for i,(r,c) in enumerate(zip(rows,counts),1):
        assert len(r) == 11 and len(c) == 4
        lo,hi,count,sum_m,mp,mm,rp,rm = map(int,r[:8])
        assert lo == i*1000000 and hi == (i+1)*1000000
        assert list(map(int,c[:3])) == [lo,hi,count]
        assert lo <= mp < hi and lo <= rp < hi and count > 0
        assert 0 < mm < 3*hi and 0 < rm <= mm
        assert count <= sum_m <= count*mm
        assert Fraction(rm*rm,rp) >= Fraction(mm*mm,mp)
        # Each segment stored its exact maximum of m(p)^2/p.
        assert rm*rm < 256*rp
        if mm > maximum['m']:
            maximum = dict(p=mp,m=mm)
        if Fraction(rm*rm,rp) > Fraction(ratio['m']**2,ratio['p']):
            ratio = dict(p=rp,m=rm)
        total += count
        total_m += sum_m
        roots.append(float(c[3]))
        root_discrepancies.append(abs(Decimal(r[8])-Decimal(c[3])))
        assert root_discrepancies[-1] <= Decimal('0.0001')
        seconds.append(float(r[10]))
    assert total == 50847534 and total_m == 2086324158209
    assert maximum == dict(p=850112303,m=416784)
    assert ratio == dict(p=695361131,m=406244)
    assert ratio['m']**2 < 256*ratio['p']
    # The prior small census is already validated; read its prime arguments
    # solely to add the previously unneeded sum of square roots.
    small_rows = csv.DictReader((ROOT/'results/factoring-rho-census.csv').open())
    roots.append(fsum(sqrt(int(r['p'])) for r in small_rows))
    sum_roots = fsum(roots)
    with localcontext() as ctx:
        ctx.prec = 40
        ratio_decimal = Decimal(ratio['m'])/Decimal(ratio['p']).sqrt()
    files=['results/factoring-rho-extended.csv','results/rho-prime-counts.csv',
           'results/factoring-rho-census.csv','results/factoring-rho.json']
    result=dict(status='passed',primes=total,segments_new=999,
                sum_iterations=total_m,maximum=maximum,ratio_maximum=ratio,
                ratio_squared_exact=str(Fraction(ratio['m']**2,ratio['p'])),
                ratio_decimal_descriptive=str(ratio_decimal),
                strict_bound='m(p)^2 < 256p for every prime p<10^9',
                sum_square_roots_descriptive=sum_roots,
                sum_m_div_sum_square_roots_descriptive=total_m/sum_roots,
                mean_iterations_descriptive=total_m/total,
                max_segment_root_sum_discrepancy=str(max(root_discrepancies)),
                iteration_seconds_new=fsum(seconds),
                independent_prime_count_method='Unsegmented odd-only Eratosthenes; exact per-segment counts match segmented census.',
                independent_iteration_scope='Two methods for all p<10^6; new p>=10^6 use reviewed dyadic detector once. Published external records also agree.',
                source_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files})
    (ROOT/'results/rho-aggregate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
