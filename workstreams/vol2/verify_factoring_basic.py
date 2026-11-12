#!/usr/bin/env python3
"""Exact checks for TAOCP2 4.5.4A and exercises1--3,6,8,29."""
from pathlib import Path
from math import gcd, prod, factorial
from collections import Counter
import argparse
import json
import os
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/factoring-basic.json'
LIMIT = 1_000_000
SPF = list(range(LIMIT+1))
for d in range(2, 1001):
    if SPF[d] == d:
        for v in range(d*d, LIMIT+1, d):
            if SPF[v] == v:
                SPF[v] = d
PRIMES = [n for n in range(2, 1001) if SPF[n] == n]


def oracle_factors(n):
    result = []
    while n > 1:
        p = SPF[n]
        result.append(p)
        n //= p
    return result


def algorithm_a(N, ds, omit_a2=False):
    n, k, divisions = N, 0, 0
    output = []
    while True:
        if n == 1 and not omit_a2:
            return output, divisions, k
        d = ds[k]
        if n > 1:
            assert SPF[n] >= d
        q, r = divmod(n, d)
        divisions += 1
        if r == 0:
            assert SPF[d] == d, (N, d)
            output.append(d)
            n = q
        elif q > d:
            k += 1
        else:
            output.append(n)
            return output, divisions, k


def division():
    seqs = {
        'all': list(range(2, 1002)),
        'primes': PRIMES+[1000],
        'wheel6': [2, 3]+[n for n in range(5, 1002) if gcd(n, 6) == 1],
        'wheel30': [2, 3, 5]+[n for n in range(7, 1002) if gcd(n, 30) == 1],
    }
    counts = {}
    for name, ds in seqs.items():
        for n in range(1, 50001):
            fs, steps, k = algorithm_a(n, ds)
            assert fs == oracle_factors(n), (name, n)
            assert steps == len(fs)+k
        counts[name] = 50000
    for n in range(3, 50001):
        fs = oracle_factors(n)
        out, _, _ = algorithm_a(n, seqs['primes'], omit_a2=True)
        failure = len(fs) >= 2 and fs[-1] == fs[-2]
        assert out == fs+([1] if failure else []), n
    examples = {}
    for n in (25852, 25849):
        fs, steps, k = algorithm_a(n, seqs['primes'])
        examples[str(n)] = dict(factors=fs, divisions=steps, last_index=k)
    assert examples['25852']['divisions'] == 12
    assert examples['25849']['divisions'] == 38
    assert examples['25852']['factors'] == [2, 2, 23, 281]
    assert examples['25849']['factors'] == [25849]
    return dict(input_counts=counts, omitted_A2_cases=49998, examples=examples)


def primorial():
    P = prod(PRIMES)
    s = str(P)
    assert len(PRIMES) == 168 and PRIMES[-1] == 997
    assert len(s) == 416 and s.startswith('19590') and s.endswith('5910')
    for n in range(1000, LIMIT+1):
        assert (gcd(n, P) == 1) == (SPF[n] == n), n
    # Table sentinel suffices for every input below one million, by the proof;
    # here verify the boundary neighborhood, not a duplicate full division census.
    for n in range(997**2, LIMIT+1):
        fs, _, _ = algorithm_a(n, PRIMES+[1000])
        assert fs == oracle_factors(n)
    return dict(primes=PRIMES, primorial=s, digits=len(s), gcd_checks=999001,
                sentinel_checks=LIMIT-997**2+1)


def sieve(N, mode='repaired', fast=False):
    M = N//2
    upper = M if mode == 'original' else M-1
    X = {k: 1 for k in range(1, upper+1)}
    if mode == 'repaired' and M < 2:
        return []
    j, k, p, q = 1, 1, 3, 4
    out = []
    while True:
        assert p == 2*j+1 and q == 2*j+2*j*j
        if fast and q >= M:
            out.extend(2*i+1 for i in range(j, M) if X[i])
            return out
        if X[j]:
            out.append(p)
            k = q
            while k <= upper:
                assert k in X
                X[k] = 0
                k += p
        j += 1
        p += 2
        q += p+p-2
        if j > upper:
            return out


def sieves():
    assert sieve(2, 'original') == [3]
    try:
        sieve(2, 'errata')
    except KeyError as e:
        assert e.args == (1,)
    else:
        raise AssertionError('Expected missing X[1] at N=2')
    for n in range(2, 4097):
        want = [p for p in range(3, n, 2) if SPF[p] == p]
        assert sieve(n) == want
        assert sieve(n, fast=True) == want
        if n >= 4:
            assert sieve(n, 'errata') == want
    return dict(repaired_bounds_checked=4095, fast_bounds_checked=4095,
                errata_bounds_checked=4093, boundary={'N': 2, 'original': [3],
                'errata': 'X[1] outside empty table', 'repaired': []})


def residues():
    checks = 0
    for p in PRIMES:
        if p == 2 or p > 101:
            continue
        roots = Counter((y*y) % p for y in range(p))
        for n in range(1, p):
            multiplicities = [roots.get((x*x-n) % p, 0) for x in range(p)]
            assert sum(multiplicities) == p-1
            assert sum(v > 0 for v in multiplicities) == (p+(1 if n in roots else -1))//2
            checks += 1
    return dict(nonzero_residue_classes=checks, maximum_prime=101)


def smooth():
    checks = 0
    for m in range(1, 7):
        pm = PRIMES[m-1]
        count, r, power = 0, 0, 1
        for n in range(1, 4097):
            if all(p <= pm for p in oracle_factors(n)):
                count += 1
            while power*pm <= n:
                power *= pm
                r += 1
            assert count*factorial(r) >= m**r, (m, n, count, r)
            checks += 1
    return dict(bounds=checks, maximum_m=6, maximum_n=4096)


def mertens():
    from flint import arb, ctx
    ctx.dps = 90
    K = 220
    mu = [0, 1]+[0]*(K-1)
    for n in range(2, K+1):
        p = SPF[n]
        mu[n] = 0 if (n//p) % p == 0 else -mu[n//p]
    value = arb.const_euler()+sum((mu[k]*arb(k).zeta().log()/k for k in range(2, K+1)), arb(0))
    tail = (1+arb(2)/K)*arb(2)**(-K)/(K+1)
    lo, hi = value-tail, value+tail
    printed = '2614972128476427837554268386086958590516'
    # The source rounds the final digit; an initial prefix-only check was too strict.
    scale = 10**len(printed)
    assert lo > (arb(int(printed))-arb(1)/2)/scale
    assert hi < (arb(int(printed))+arb(1)/2)/scale
    return dict(partial_sum=value.str(80), absolute_tail=tail.str(30),
                lower=lo.str(75), upper=hi.str(75), terms=K, precision=ctx.dps,
                printed_digits=printed, convention='rounded at 40 decimal places')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    result = json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'checkpoints': {}}
    result['pid'] = os.getpid()
    started = time.monotonic()
    for name, fn in [('division', division), ('primorial', primorial), ('sieves', sieves),
                     ('residues', residues), ('smooth', smooth), ('mertens', mertens)]:
        if name in result['checkpoints']:
            print('reuse', name, flush=True)
            continue
        t = time.monotonic()
        result['checkpoints'][name] = {'result': fn(), 'seconds': time.monotonic()-t}
        OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
        print('passed', name, flush=True)
    result['status'] = 'passed'
    result['elapsed_this_run'] = time.monotonic()-started
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print('ALL PASSED', result['pid'], result['elapsed_this_run'], flush=True)
