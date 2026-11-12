#!/usr/bin/env python3
"""Exact checks for Harris and TAOCP 4.5.2-35/36; proofs are in gcd-extremal.md."""
from collections import Counter
from math import gcd
from pathlib import Path
import json, sys, time
from verify_gcd_basic import binary, euclid
from verify_gcd_bins import table

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/gcd-extremal.json'


def harris(u, v):
    assert u >= v > 0 and u % 2 and v % 2
    origin = u, v
    rows = []
    while True:
        q, r = divmod(u, v)
        if r % 2:
            q += 1
            r -= v
        assert q % 2 and abs(r) < v and r % 2 == 0
        assert u == q*v+r
        if rows: assert q >= 3
        if not r:
            rows.append((u, v, q, r, 0))
            assert v == gcd(*origin)
            return v, rows
        e = (abs(r) & -abs(r)).bit_length()-1
        w = abs(r) >> e
        assert e >= 1 and 2*w < v and w % 2
        rows.append((u, v, q, r, e))
        u, v = v, w


def nearest(u, v):
    count = 0
    while v:
        q = (2*u+v)//(2*v)
        u, v = v, abs(u-q*v)
        count += 1
    return count


def harris_checks():
    pairs = 0
    minima = {}
    for u in range(1, 1024, 2):
        for v in range(1, u+1, 2):
            d, rows = harris(u, v)
            k = len(rows)
            assert v >= (2**k-1)*d
            assert u >= (2**(k+1)-3)*d
            old = minima.get(k)
            if old is None or u+v < sum(old): minima[k] = (u, v)
            pairs += 1
    for k, pair in minima.items():
        assert pair == (2**(k+1)-3, 2**k-1)
    long = 0
    for k in range(1, 201):
        pair = 2**(k+1)-3, 2**k-1
        assert len(harris(*pair)[1]) == k
        a, b = 6*2**k-5, 6*2**(k-1)-5
        assert len(harris(a,b)[1]) == k
        assert len(euclid(a,b)[1]) <= 5
        long += 2
    pell = [0, 1]
    for _ in range(101): pell.append(2*pell[-1]+pell[-2])
    rieger = []
    for k in range(2, 101, 2):
        K = 4*k+3
        p, q = pell[k], pell[k+1]
        tail = (2**K*pow(p,-1,q)) % q
        if tail % 2 == 0: tail += q
        assert 0 < tail < 2*q and tail % 2
        r = {k+1:tail, k:(2**K-p*tail)//q}
        assert r[k] > 2*r[k+1]
        for j in range(k-1,0,-1): r[j] = 2*r[j+1]+r[j+2]
        for j in range(1,k+1):
            assert r[j] > 2*r[j+1]
            assert r[j] % 2 == j % 2
            assert pell[j+1]*r[j]+pell[j]*r[j+1] == 2**K
        y = 2*2**K+r[1]
        x = 3*y+2**K
        H = len(harris(x,y)[1]); E = len(euclid(x,y)[1]); N = nearest(x,y)
        assert H == 2 and E >= N > k
        rieger.append(dict(k=k,input_bits=x.bit_length(),H=H,E=E,N=N))
    example = 28567, 3829
    d, rows = harris(*example)
    assert d == 7 and len(rows) == 4
    assert len(euclid(*example)[1]) == 6 and nearest(*example) == 5
    return dict(exhaustive_odd_pairs=pairs,limit=1023,minimal_pairs=minima,
                large_extremal_pairs=long,rieger_short_harris=rieger,
                harris_original_example=rows)


def support(m,n):
    assert m >= n >= 0
    if m == n:
        return {'stop'} | {(r,n) for r in range(n-1)} | {(n,r) for r in range(n-1)}
    if n == 0: return {(r,0) for r in range(m)}
    if m == 2 and n == 1: return {(0,1)}
    return {(r,n) for r in range(m)}


def graph_checks():
    L = {}; supports = 0
    for m in range(97):
        for n in range(m+1):
            edges = support(m,n)
            if m <= 32:
                assert edges == set(table(m,n)),(m,n,edges,set(table(m,n)))
                supports += 1
            distance = 1+max(0 if x=='stop' else L[tuple(sorted(x,reverse=True))] for x in edges)
            assert distance == m+n//2+1-int(m==n==1),(m,n,distance)
            L[m,n] = distance
    path = [(2,2),(2,0),(1,0),(0,0),'stop']
    for a,b in zip(path,path[1:]): assert b in support(*a)
    assert L[2,2] == 4
    actual = max(binary(u,v)[1]['C'] for u in [5,7] for v in [5,7])
    assert actual == 3
    return dict(dynamic_program_vertices=len(L),largest_index=96,
                supports_compared_to_validated_table=supports,
                unattainable_path=path,actual_max_at_2_2=actual)


def jacobsthal(k): return (2**k-(-1)**k)//3


def constructions():
    counts = Counter()
    for m in range(1,129):
        for n in range(1,m+1):
            a = jacobsthal(n+2)
            u,v = (2**(m+1)-a,a) if m>n else (a,a+(-1)**n)
            assert u.bit_length()-1 == m and v.bit_length()-1 == n
            d,s,rows = binary(u,v)
            assert d == 1 and s['C'] == m+1,(m,n,u,v,s)
            counts['constructed_pairs'] += 1
            if m == n:
                original = max(a,2*jacobsthal(n+1))
                assert sorted([original,jacobsthal(n+3)-original]) == sorted([u,v])
                counts['known_2005_equivalences'] += 1
        u,v = 2**(m+1)-2,2**(m+1)-1
        d,s,_ = binary(u,v)
        assert d == 1 and (s['B'],s['C'],s['D'],s['E']) == (1,m+1,2*m,m)
        counts['worst_program_examples'] += 1
    for m in [256,512,1024,2048]:
        for n in [1,2,3,m//2,m-1,m]:
            a = jacobsthal(n+2)
            u,v = (2**(m+1)-a,a) if m>n else (a,a+(-1)**n)
            assert u.bit_length()-1 == m and v.bit_length()-1 == n
            assert binary(u,v)[1]['C'] == m+1
            counts['large_pairs'] += 1
    return dict(counts)


if __name__ == '__main__':
    data = json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('harris',harris_checks),('graph',graph_checks),('constructions',constructions)]:
        if name in data: continue
        start = time.monotonic(); value = fn()
        data[name] = dict(status='passed',seconds=time.monotonic()-start,result=value)
        OUT.write_text(json.dumps(data,indent=2)+'\n')
        print(name,'passed',round(data[name]['seconds'],3),flush=True)
