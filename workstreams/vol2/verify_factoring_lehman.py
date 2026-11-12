#!/usr/bin/env python3
"""Exact verification of a rounded Lehman search and its Dirichlet witnesses.

The proof is in notes/factoring-context.md.  This implementation deliberately
uses slightly enlarged integer intervals, not the original optimized program.
An independent Eratosthenes table supplies the primality/factor oracle.
"""
from pathlib import Path
from math import isqrt, gcd
import argparse
import json
import os
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/factoring-lehman.json'


def icbrt(n):
    lo, hi = 0, 1 << ((n.bit_length() + 2) // 3)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid
    return lo


def ceil_cbrt(n):
    r = icbrt(n)
    return r + (r**3 < n)


def interval(n, k, length):
    base = 4*k*n
    start = isqrt(base)
    start += start*start < base
    width = isqrt(length // (16*k))
    width += 16*k*width*width < length
    assert 16*k*(width-1)**2 < length <= 16*k*width*width
    return start, start + width


def search(n):
    if n % 2 == 0:
        return 2, 0, 'even'
    length = ceil_cbrt(n)
    bound = isqrt(n) if n < 64 else length
    for d in range(3, bound+1, 2):
        if n % d == 0:
            return d, 0, 'trial'
    if n < 64:
        return n, 0, 'prime_small'
    root = isqrt(n)
    if root*root == n:
        return root, 0, 'square'
    tests = 0
    for k in range(1, length+1):
        start, end = interval(n, k, length)
        for x in range(start, end+1):
            tests += 1
            assert x < n
            y = isqrt(x*x-4*k*n)
            if y*y == x*x-4*k*n:
                assert (x+y) % 2 == 0
                d = gcd((x+y)//2, n)
                assert 1 < d < n and n % d == 0
                return d, tests, 'lehman'
    return n, tests, 'prime'


def sieve(limit):
    smallest = list(range(limit+1))
    for p in range(2, isqrt(limit)+1):
        if smallest[p] == p:
            for n in range(p*p, limit+1, p):
                if smallest[n] == n:
                    smallest[n] = p
    return smallest


def all_inputs():
    limit = 100000
    oracle = sieve(limit)
    kinds = {}
    max_tests = (0, 0)
    for n in range(2, limit+1):
        d, tests, kind = search(n)
        assert n % d == 0 and d > 1
        assert (d == n) == (oracle[n] == n), (n, d, oracle[n])
        length = ceil_cbrt(n)
        assert 2*tests <= 5*length
        kinds[kind] = kinds.get(kind, 0) + 1
        max_tests = max(max_tests, (tests, n))
    return dict(inputs=limit-1, limit=limit, cases=kinds,
                maximum_candidate_tests=max_tests)


def dirichlet_witnesses():
    oracle = sieve(2000)
    primes = [p for p in range(3, 2001) if oracle[p] == p]
    count = 0
    max_denominator = 0
    for j, p in enumerate(primes):
        for q in primes[j+1:]:
            n = p*q
            if p**3 <= n:
                continue
            length = ceil_cbrt(n)
            Q = icbrt(p**3 // n)
            assert Q >= 1 and Q**3*n <= p**3 < (Q+1)**3*n
            candidates = []
            for b in range(1, Q+1):
                floor_a = b*q // p
                for a in (floor_a, floor_a+1):
                    if abs(a*p-b*q)*(Q+1) <= p:
                        candidates.append((a, b))
            assert candidates, (p, q, Q)
            a, b = candidates[0]
            k, x, y = a*b, a*p+b*q, abs(a*p-b*q)
            assert 1 <= a < q and 1 <= b < p
            assert 1 <= k <= length and y**3 < n
            assert x*x-y*y == 4*k*n
            start, end = interval(n, k, length)
            assert start <= x <= end
            assert gcd(a*p, n) == p and gcd(b*q, n) == q
            count += 1
            max_denominator = max(max_denominator, Q)
    return dict(semiprimes=count, prime_limit=2000,
                maximum_Dirichlet_denominator=max_denominator,
                all_witnesses_in_search_interval=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    result = json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'checkpoints': {}}
    result['pid'] = os.getpid()
    start = time.monotonic()
    for name, fn in [('all_inputs', all_inputs), ('dirichlet_witnesses', dirichlet_witnesses)]:
        if name in result['checkpoints']:
            print('reuse', name, flush=True)
            continue
        tick = time.monotonic()
        result['checkpoints'][name] = {'result': fn(), 'seconds': time.monotonic()-tick}
        OUT.write_text(json.dumps(result, indent=2)+'\n')
        print('passed', name, flush=True)
    result['status'] = 'passed'
    result['elapsed_this_run'] = time.monotonic()-start
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print('ALL PASSED', result['pid'], result['elapsed_this_run'], flush=True)
