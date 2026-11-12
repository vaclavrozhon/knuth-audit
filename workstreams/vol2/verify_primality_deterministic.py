#!/usr/bin/env python3
"""Exact checks of TAOCP2 exercises4.5.4-24,26,27; checkpointed by block."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
from math import gcd, isqrt
import argparse
import json
import time

from verify_primality_probabilistic import factor, odd_part, algorithm_p

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/primality-deterministic.json'


def prime_trial(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


@lru_cache(None)
def accepted(n):
    k, q = odd_part(n-1)
    return tuple(x == 0 or algorithm_p(n, x, k, q) for x in range(n))


def nonuniform():
    rows = comparisons = 0
    failures = []
    for n in range(9, 1024, 2):
        if prime_trial(n):
            continue
        row = accepted(n)
        b = sum(row)-1
        prefix = 0
        for r in range(n):
            if r:
                prefix += row[r]
            assert prefix <= min(b, r)
            for q in range(1, 5):
                bound = q*n+r
                zeros = q*(b+1)+prefix-1
                repaired = q*Fraction(n, 3)+min(Fraction(n, 4), r)-1
                assert zeros <= repaired <= Fraction(bound, 2)-1
                assert 2*zeros <= bound-1
                printed_left = q*(Fraction(n-1, 4)+1)+min(b+1, r)
                printed_right = q*Fraction(n, 3)+min(Fraction(n, 4), r)
                if printed_left > printed_right:
                    failures.append([n, bound, str(printed_left), str(printed_right)])
                comparisons += 1
        rows += 1
    covers = []
    for bound in [9, 12, 64, 256, 1024, 4096, 10000]:
        initial = [n for n in range(9, bound+1, 2) if not prime_trial(n)]
        remaining = initial[:]
        bases = []
        while remaining:
            for a in range(2, bound+1):
                rejected = [n for n in remaining if not accepted(n)[a % n]]
                if 2*len(rejected) >= len(remaining):
                    bases.append(a)
                    remaining = [n for n in remaining if accepted(n)[a % n]]
                    break
            else:
                raise AssertionError('No halving column')
        assert len(bases) <= bound.bit_length()-1
        assert len(set(bases)) == len(bases)
        # Independent repeated exponentiation directly from the odd part,
        # without the cached row or algorithm_p's early exits.
        for n in range(3, bound+1, 2):
            k, q = odd_part(n-1)
            tests = []
            for a in bases:
                z = a % n
                tests.append(z == 0 or pow(z, q, n) == 1 or
                             any(pow(z, (1 << j)*q, n) == n-1 for j in range(k)))
            assert all(tests) == prime_trial(n)
        covers.append(dict(N=bound, bases=bases, composite_rows=len(initial)))
    n, bound = 9, 12
    exact_passes = [x for x in range(2, bound+1) if accepted(n)[x % n]]
    assert exact_passes == [8, 9, 10]
    return dict(composite_rows=rows, row_endpoint_checks=comparisons,
                false_printed_inequalities=len(failures), first_failure=failures[0],
                example=dict(n=n, N=bound, accepted_columns=exact_passes,
                             printed_chain=['5','6','21/4','21/4','11/2','6']),
                finite_covers=covers)


def pocklington():
    cases = primes = witnesses = 0
    boundary = []
    for f in range(1, 49):
        ps = [p for p, e in factor(f)]
        for r in range(1, f+2):
            n = f*r+1
            certificate = []
            for p in ps:
                x = next((x for x in range(1, n)
                          if pow(x, n-1, n) == 1 and
                          gcd(pow(x, (n-1)//p, n)-1, n) == 1), None)
                if x is None:
                    break
                certificate.append([p, x])
            success = len(certificate) == len(ps)
            assert success == prime_trial(n)
            if success:
                primes += 1
                witnesses += len(certificate)
            if r == f+1 and success:
                boundary.append([f, r, n])
            cases += 1
    return dict(parameter_pairs=cases, prime_pairs=primes,
                verified_witnesses=witnesses,
                printed_boundary='r=f+1 is included in the printed exercise and general proof',
                boundary_prime_pairs=boundary)


def proth():
    limit=(1 << 12)*((1 << 12)+1)+1
    prime = bytearray(b'\x01')*(limit+1)
    prime[0:2] = b'\x00\x00'
    for p in range(2, isqrt(limit)+1):
        if prime[p]:
            start = p*p
            prime[start::p] = b'\x00'*((limit-start)//p+1)
    cases = reductions = 0
    mismatches = []
    for e in range(1, 13):
        power = 1 << e
        for k in range(1, power+2):
            if k % 3 == 0:
                continue
            n=k*power+1
            residue=pow(3, k*(power//2), n)
            test=residue==n-1
            if test != bool(prime[n]):
                mismatches.append(dict(k=k, exponent=e, n=n, residue=residue,
                                       prime=bool(prime[n])))
            assert (test or n==3) == bool(prime[n])
            for x in sorted({0, 1, 2, n//2, n-2, n-1}):
                a,b=divmod(x*x,power)
                reduced=b-a//k+power*(a % k)
                assert 1-n <= reduced <= n-2
                result=reduced+n if reduced<0 else reduced
                assert result==x*x % n
                reductions += 1
            cases += 1
    assert mismatches==[dict(k=1, exponent=1, n=3, residue=0, prime=True)]
    return dict(parameter_pairs=cases, sieve_limit=limit, modular_reductions=reductions,
                sole_mismatch=mismatches[0])


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--block',choices=['nonuniform','pocklington','proth','all'],default='all');args=parser.parse_args()
    state=json.loads(OUT.read_text()) if OUT.exists() else dict(checkpoints={})
    for name, fn in [('nonuniform',nonuniform),('pocklington',pocklington),('proth',proth)]:
        if args.block not in (name,'all') or name in state['checkpoints']:
            continue
        start=time.monotonic();result=fn()
        state['checkpoints'][name]=dict(status='passed',seconds=time.monotonic()-start,result=result)
        OUT.write_text(json.dumps(state,indent=2)+'\n')
        print(json.dumps({name:state['checkpoints'][name]}),flush=True)


if __name__=='__main__':main()
