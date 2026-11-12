#!/usr/bin/env python3
"""Exact audit of TAOCP 4.5.4-42; independent divisor enumeration."""
from pathlib import Path
from math import gcd, isqrt
from random import Random
import hashlib
import json
import os
import time

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / 'results/lenstra-residues.json'


def parameters(n, r, s, rounded_up):
    assert 0 < r < s < n and gcd(r, s) == gcd(n, s) == 1
    inverse = pow(r, -1, s)
    rp = n * inverse % s
    u = rp * inverse % s
    w = ((n - r * rp) // s * inverse) % s
    theta = isqrt(n // s)
    if rounded_up and theta * theta * s < n:
        theta += 1
    return rp, u, w, theta


def solve(n, r, s, *, printed_denominator=False, rounded_up=True, trace=False):
    rp, u, w, theta = parameters(n, r, s, rounded_up)
    u1, u3, v1, v3 = 1, u, 0, s
    outputs, rows = set(), []
    attempts = states = 0
    while True:
        assert (v3 - u * v1) % s == 0
        assert abs(u1 * v3 - v1 * u3) == s
        assert 0 <= v3 <= s and abs(v1) <= s
        states += 1
        row = {'v1': v1, 'v3': v3, 'candidates': []}
        if v1 == 0:
            for a in range(theta // s + 1):
                d = a * s + r
                attempts += 1
                if n % d == 0:
                    outputs.add(d)
        elif v3 == 0:
            assert v1 == -s  # gcd(u,s)=1 and the parity correction in L4.
            for b in range(theta // s + 1):
                d = b * s + rp
                attempts += 1
                if n % d == 0:
                    outputs.add(n // d)
        else:
            lo, hi = (-theta, theta) if v1 < 0 else (1, 2 * theta)
            first = (lo - w * v1 + s - 1) // s
            last = (hi - w * v1) // s
            for k in range(first, last + 1):
                z = w * v1 + k * s
                discriminant = (z * s + v3 * r + v1 * rp)**2 - 4 * v1 * v3 * n
                attempts += 1
                if discriminant < 0:
                    continue
                square_root = isqrt(discriminant)
                if square_root**2 != discriminant:
                    continue
                for sign in (-1, 1):
                    an = z * s - v3 * r + v1 * rp + sign * square_root
                    bn = z * s + v3 * r - v1 * rp - sign * square_root
                    ad = 2 * v3 * s
                    bd = 2 * (v3 if printed_denominator else v1) * s
                    if an % ad or bn % bd:
                        continue
                    a, b = an // ad, bn // bd
                    if a <= 0 or b <= 0:
                        continue
                    if not printed_denominator:
                        assert a * v3 + b * v1 == z
                        assert (a * s + r) * (b * s + rp) == n
                    outputs.add(a * s + r)
                    if trace:
                        row['candidates'].append({'k': k, 'z': z, 'D': discriminant,
                                                  'sign': sign, 'lambda': a, 'mu': b,
                                                  'output': a * s + r})
        if trace:
            rows.append(row)
        if v3 == 0:
            break
        q = u3 // v3
        if u3 == q * v3 and v1 < 0:
            q -= 1
        u1, u3, v1, v3 = v1, v3, u1 - q * v1, u3 - q * v3
    return outputs, {'states': states, 'attempts': attempts,
                     'theta': theta, 'r_prime': rp, 'u': u, 'w': w,
                     **({'trace': rows} if trace else {})}


def divisors_trial(n):
    out = set()
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.update((d, n // d))
    return out


def counterexamples():
    original, detail = solve(14, 1, 3, printed_denominator=True, rounded_up=False, trace=True)
    fixed, _ = solve(14, 1, 3)
    assert original == {1, 4, 7} and fixed == {1, 7}
    assert divisors_trial(14) & {1, 4, 7} == {1, 7}
    rp, u, w, theta = parameters(36, 1, 5, False)
    assert (rp, u, w, theta) == (1, 1, 2, 2)
    assert (1 * 5 + 1)**2 == 36 and 1 * 1 * 5 > theta**2
    # Exact roots of the two-equation system, independently via substitution:
    # 14,1,3 at (v1,v3)=(2,1), z=2 -> lambda+2mu=2.
    # lambda=1 forces mu=1/2, whereas the printed formula gives mu=1.
    assert (3 * 1 + 1) * (3 + 4) == 2 * 14
    return {'status': 'passed', 'formula_case': {'N': 14, 'r': 1, 's': 3,
            'printed': sorted(original), 'corrected': sorted(fixed), **detail},
            'floor_case': {'N': 36, 'r': 1, 's': 5, 'lambda': 1, 'mu': 1,
                           'lambda_mu_s': 5, 'theta_squared': 4}}


def exhaustive_small():
    digest = hashlib.sha256()
    counts = {'instances': 0, 'empty_classes': 0, 'outputs': 0,
              'states': 0, 'quadratic_or_endpoint_attempts': 0,
              'floor_variant_mismatches': 0}
    for n in range(3, 161):
        divisors = divisors_trial(n)
        for s in range(2, n):
            if gcd(n, s) != 1:
                continue
            by_residue = {}
            for d in divisors:
                by_residue.setdefault(d % s, set()).add(d)
            for r in range(1, s):
                if gcd(r, s) != 1:
                    continue
                expected = by_residue.get(r, set())
                actual, stat = solve(n, r, s)
                assert actual == expected, (n, r, s, actual, expected)
                # This finite comparison does not prove the floor variant generally.
                floored, _ = solve(n, r, s, rounded_up=False)
                counts['floor_variant_mismatches'] += floored != expected
                counts['instances'] += 1
                counts['empty_classes'] += not expected
                counts['outputs'] += len(actual)
                counts['states'] += stat['states']
                counts['quadratic_or_endpoint_attempts'] += stat['attempts']
                digest.update(f'{n},{r},{s}:{sorted(actual)}\n'.encode())
    return {'status': 'passed', 'N_inclusive': [3, 160], **counts, 'sha256': digest.hexdigest()}


def factorized_divisors(exponents):
    primes = (2, 3, 5, 7)
    ds = [1]
    n = 1
    for p, e in zip(primes, exponents):
        ds = [d * p**j for d in ds for j in range(e + 1)]
        n *= p**e
    assert len(ds) == len(set(ds))
    return n, set(ds)


def large_exact():
    rng = Random(198442)
    cases = []
    digest = hashlib.sha256()
    for i in range(12):
        exponents = (30 + i, 18 + i % 5, 7 + i % 3, 3 + i % 4)
        n, divisors = factorized_divisors(exponents)
        # Exact cube-root bracket; a different oracle from the Euclidean/quadratic algorithm.
        lo, hi = 0, 1 << ((n.bit_length() + 2) // 3)
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if mid**3 <= n:
                lo = mid
            else:
                hi = mid
        s = lo + rng.randrange(1, 500)
        while gcd(n, s) != 1:
            s += 1
        assert s**3 > n
        ds = sorted(divisors)
        residues = {1, s - 1}
        residues.update(rng.choice(ds) % s for _ in range(25))
        residues.update(rng.randrange(1, s) for _ in range(25))
        instances = attempts = outputs = max_states = 0
        grouped = {}
        for d in divisors:
            grouped.setdefault(d % s, set()).add(d)
        for r in sorted(residues):
            if gcd(r, s) != 1:
                continue
            want = grouped.get(r, set())
            got, stat = solve(n, r, s)
            assert got == want, (n, r, s, got, want)
            instances += 1
            outputs += len(got)
            attempts += stat['attempts']
            max_states = max(max_states, stat['states'])
            digest.update(f'{n},{r},{s}:{sorted(got)}\n'.encode())
        cases.append({'N': str(n), 's': str(s), 'N_bits': n.bit_length(),
                      'exponents_2_3_5_7': exponents, 'all_divisors': len(divisors),
                      'instances': instances, 'outputs': outputs,
                      'attempts': attempts, 'max_states': max_states})
    return {'status': 'passed', 'cases': cases,
            'instances': sum(c['instances'] for c in cases), 'sha256': digest.hexdigest()}


def main():
    out = {'pid': os.getpid(), 'status': 'running', 'blocks': []}
    begin = time.monotonic()
    print('pid', os.getpid(), flush=True)
    for fn in [counterexamples, exhaustive_small, large_exact]:
        start = time.monotonic()
        result = fn()
        result['name'] = fn.__name__
        result['seconds'] = time.monotonic() - start
        out['blocks'].append(result)
        RESULT.write_text(json.dumps(out, indent=2) + '\n')
        print(fn.__name__, result['status'], result['seconds'], flush=True)
    out['status'] = 'passed'
    out['seconds'] = time.monotonic() - begin
    RESULT.write_text(json.dumps(out, indent=2) + '\n')


if __name__ == '__main__':
    main()
