#!/usr/bin/env python3
"""Exact independent validators for TAOCP2 pp391-394 and exercises9,10,17."""
from pathlib import Path
from math import gcd, isqrt, lcm, prod
from collections import Counter
import argparse
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/primality-basic.json'


def power(a, e, n):
    """Left-to-right binary modular exponentiation, checked against builtin pow."""
    value = 1
    for digit in bin(e)[2:]:
        value = value*value % n
        if digit == '1':
            value = value*a % n
    assert value == pow(a, e, n)
    return value


def certificates():
    data = json.loads((ROOT/'results/primality-certificates.json').read_text())
    proved = set()
    sizes = {}
    powers = 0
    for node in data['nodes']:
        n, fs, a = node['n'], node['factors'], node['witness']
        assert n not in proved and 1 <= a < n
        assert prod(p**e for p, e in fs) == n-1
        assert len({p for p, e in fs}) == len(fs)
        assert all(p in proved and isinstance(e, int) and e > 0 for p, e in fs)
        assert power(a, n-1, n) == 1
        for p, e in fs:
            assert power(a, (n-1)//p, n) != 1
        if not fs:
            assert n == 2
        size = 1+sum(e*sizes[p] for p, e in fs)
        assert 2**(size+1) <= n*n  # Exactly size <= 2 lg n - 1.
        sizes[n] = size
        powers += 1+len(fs)
        proved.add(n)
    assert set(data['targets']) <= proved
    # Printed Pratt tree uses these witnesses, which need not be generator choices.
    tree = {2: (1, []), 3: (2, [2]), 7: (3, [2, 3]), 1009: (11, [2]*4+[7, 3, 3])}
    counts = {}
    for n, (a, children) in tree.items():
        assert 1+prod(children) == n and power(a, n-1, n) == 1
        assert all(power(a, (n-1)//p, n) != 1 for p in children)
        counts[n] = 1+sum(counts[p] for p in children)
    assert counts[1009] == 13
    return dict(nodes=len(proved), modular_power_checks=powers,
                all_targets=data['targets'], printed_pratt_tree_nodes=counts[1009],
                largest_unfolded_tree=max(sizes.items(), key=lambda pair: pair[1]))


def printed_example():
    n0 = 37866809061660057264219253397
    n1 = 13191270754108226049301
    n2 = 143675413657196977
    n3 = 1824032775457
    n4 = 1653701519
    n5 = 2**107+2**54+1
    n6 = 192343993140277293096491917
    numbers = [n0, n1, n2, n3, n4, n5, n6]
    assert (2**107-2**54+1)*n5 == 2**214+1
    assert 2**107-2**54+1 == 5*857*n0
    assert n0-1 == 2**2*19*107*353*n1
    assert n1 == 91813*n2
    assert n2-1 == 2**4*3**2*547*n3
    assert n3 == 1103*n4
    assert n4-1 == 2*7*19*23*137*1973
    assert n5 == 843589*n6
    assert n6 == 8174912477117*23528569104401
    assert 2**214+1 == 5*857*843589*8174912477117*23528569104401*n0
    assert [len(str(n)) for n in [2**214+1,n5,n0,n6,n0*n6]] == [65,33,29,27,55]
    assert all(n0%d for d in range(2, 1000))
    fermat = [power(3, n-1, n) for n in numbers]
    assert [v == 1 for v in fermat] == [True,False,True,False,True,False,False]
    rows = [(2,2,1),(2,7,766408626),(2,19,332952683),
            (2,23,1154237810),(2,137,373782186),(2,1973,490790919),
            (3,2,1),(5,2,1),(7,2,1653701518)]
    for a,p,v in rows:
        assert power(a, (n4-1)//p, n4) == v
        assert power(a, n4-1, n4) == 1
    assert n4 % 5 == 4
    assert power(2, n4-1, n4) == 1
    assert gcd(power(2,(n4-1)//23,n4)-1,n4) == 1
    assert gcd(power(2,(n4-1)//1973,n4)-1,n4) == 1
    assert (23*1973)**2 > n4
    f5 = 2**32+1
    assert power(3, 2**32, f5) == 3029026160
    pseudoprime = (2**28-9)//7
    assert 7*pseudoprime == 2**28-9
    assert pseudoprime == 2341*16381 and power(3,pseudoprime-1,pseudoprime) == 1
    assert 23528569104401-1 == 2**4*5**2*67*107*199*41231
    return dict(fermat_remainders=fermat, n4_table_rows=rows,
                full_factorization=[5,857,843589,8174912477117,23528569104401,n0],
                partial_factor=23*1973, F5_remainder=3029026160,
                base3_pseudoprime=pseudoprime)


def rho_example():
    rows = [[int(x) for x in line.split(',')] for line in
            (ROOT/'results/primality-rho.csv').read_text().splitlines()]
    assert {r[0] for r in rows} == {8174912477117,23528569104401}
    for p,mu,period,m in rows:
        block = 1 << (max(mu+1,period)-1).bit_length()
        assert m == block-1+period
    first = min(row[3] for row in rows)
    assert first == 6432966
    # Independent CRT calculation of the first collision: x_m and x_anchor
    # are reconstructed from both prime orbits, then exactly one big gcd.
    residues = []
    anchor = (1 << (first.bit_length()-1))-1
    for p,mu,period,m in rows:
        indices = [anchor, first]
        reduced = [i if i < mu else mu+(i-mu)%period for i in indices]
        x = 2
        wanted = set(reduced)
        values = {}
        for i in range(max(reduced)+1):
            if i in wanted:
                values[i] = x
            x = (x*x+1)%p
        residues.append((p,values[reduced[0]],values[reduced[1]]))
    p,a,b = residues[0]
    q,c,d = residues[1]
    inv = pow(p,-1,q)
    x_anchor = a+p*((c-a)*inv%q)
    x_first = b+p*((d-b)*inv%q)
    factor = gcd(x_first-x_anchor,p*q)
    assert factor == p and 1 < factor < p*q
    return dict(prime_orbit_rows=rows, first_iteration=first,
                anchor_index=anchor, gcd_factor=factor)


def trial_prime(n):
    return n >= 2 and all(n%d for d in range(2,isqrt(n)+1))


def carmichael_census():
    path = ROOT/'results/carmichael-census.csv'
    rows = [[int(x) for x in line.split(',')] for line in path.read_text().splitlines()]
    prime_set = {p for row in rows for p in row[1:]}
    assert all(trial_prime(p) for p in prime_set)
    records = {}
    for n,*fs in rows:
        assert fs == sorted(set(fs)) and len(fs) >= 3
        assert prod(fs) == n < 10**12 and all((n-1)%(p-1) == 0 for p in fs)
        assert n not in records
        records[n] = fs
    by_length = dict(sorted(Counter(len(fs) for fs in records.values()).items()))
    assert by_length == {3:1000,4:2102,5:3156,6:1714,7:262,8:7}
    assert len(records) == 8241
    # Independent exhaustive integer factorization below one million, as opposed
    # to generation from prime prefixes and arithmetic progressions.
    limit = 1000000
    spf = list(range(limit))
    for p in range(2,isqrt(limit-1)+1):
        if spf[p] == p:
            for k in range(p*p,limit,p):
                if spf[k] == k:
                    spf[k] = p
    direct = []
    for n in range(3,limit,2):
        m=n; fs=[]; squarefree=True
        while m>1:
            p=spf[m];m//=p;fs.append(p)
            if m%p == 0:
                squarefree=False;break
        if squarefree and len(fs)>=3 and all((n-1)%(p-1)==0 for p in fs):
            direct.append(n)
    assert direct == sorted(n for n in records if n<limit)
    assert direct[0] == 561 and len(direct) == 43
    examples=[[3,11,17],[5,13,17],[7,11,13,41],[5,7,17,19,73],[5,7,17,73,89,107]]
    for fs in examples:
        assert records[prod(fs)] == fs
    # Small direct unit test checks the exponent formulation independently.
    unit_cases = 0
    for n in range(3,1000,2):
        if spf[n] == n:
            continue
        universal = all(power(a,n-1,n)==1 for a in range(1,n) if gcd(a,n)==1)
        assert universal == (n in records)
        unit_cases += 1
    assert lcm(2,10,16) == 80
    assert all(power(a,80,561)==power(a,560,561)==1 for a in range(1,561) if gcd(a,561)==1)
    return dict(count=len(records), by_prime_factor_count=by_length,
                distinct_primes_trial_proved=len(prime_set), smallest=min(records),
                largest=max(records), independent_direct_limit=limit,
                direct_count=len(direct), composite_unit_checks=unit_cases,
                examples=[prod(fs) for fs in examples],
                census_sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--resume',action='store_true')
    ap.add_argument('--only',nargs='*')
    args = ap.parse_args()
    data = json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'checks':{}}
    for name,fn in [('certificates',certificates),('printed_example',printed_example),
                    ('rho_example',rho_example),('carmichael_census',carmichael_census)]:
        if args.only and name not in args.only:
            continue
        if name in data['checks']:
            continue
        start=time.monotonic()
        result=fn()
        data['checks'][name]=dict(status='passed',seconds=time.monotonic()-start,result=result)
        OUT.write_text(json.dumps(data,indent=2)+'\n')
        print(name,'PASSED',flush=True)


if __name__ == '__main__':
    main()
