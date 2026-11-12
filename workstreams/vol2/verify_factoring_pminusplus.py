#!/usr/bin/env python3
"""Exact checks for TAOCP 4.5.4-19/20; general proofs are in the notes.

Models: successive powers versus an independent right-to-left power;
Lucas doubling versus companion matrices and quadratic-algebra arithmetic;
exhaustive finite uniform samples for the proper-factor probability bounds.
"""
from collections import Counter
from fractions import Fraction
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import json
import os
import time

BASE = Path(__file__).resolve().parent
OUT = BASE / 'results/factoring-pminusplus.json'


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def power(a, e, n):
    result = 1
    while e:
        if e & 1:
            result = result * a % n
        a = a * a % n
        e >>= 1
    return result


def mm(A, B, n):
    a, b, c, d = A
    e, f, g, h = B
    return ((a*e+b*g) % n, (a*f+b*h) % n,
            (c*e+d*g) % n, (c*f+d*h) % n)


def v_matrix(P, e, n):
    A, R = (P % n, -1 % n, 1, 0), (1, 0, 0, 1)
    while e:
        if e & 1:
            R = mm(R, A, n)
        A = mm(A, A, n)
        e >>= 1
    return (R[0] + R[3]) % n


def v_binary(P, e, n):
    # Invariant: x=V_k(P), y=V_(k+1)(P) for the processed prefix k.
    x, y = 2 % n, P % n
    for bit in bin(e)[2:]:
        middle = (x*y-P) % n
        if bit == '0':
            x, y = (x*x-2) % n, middle
        else:
            x, y = middle, (y*y-2) % n
    return x


def qm(z, w, delta, n):
    x, y = z
    u, v = w
    return ((x*u+delta*y*v) % n, (x*v+y*u) % n)


def qp(z, e, delta, n):
    result = (1, 0)
    while e:
        if e & 1:
            result = qm(result, z, delta, n)
        z = qm(z, z, delta, n)
        e >>= 1
    return result


def odd_part(n):
    s = 0
    while n % 2 == 0:
        n //= 2
        s += 1
    return n, s


def book_example():
    small = [p for p in range(2, 1001) if prime(p)]
    powers = []
    for p in small:
        q = p
        while q*p <= 1000:
            q *= p
        powers.append(q)
    E = prod(powers)
    assert len(small) == 168 and small[-1] == 997
    assert E == lcm(*range(1, 1001)) and E % 428 == 0
    N, p, r, q = 2**214+1, 23528569104401, 8174912477117, 41231
    n6 = p*r
    assert p-1 == 2**4*5**2*67*107*199*q and N % n6 == 0
    assert all(prime(t) for t in [5, 67, 107, 199, q])
    rows = []
    state_checks = 0
    for n in [N, n6]:
        assert pow(2, 214, n) == n-1
        for a in [2, 3]:
            A, exponent = a, 1
            for t in powers:
                A = pow(A, t, n)
                exponent *= t
                assert A == power(a, exponent, n)
                state_checks += 1
            assert A == pow(a, E, n)
            g1, g2 = gcd(A-1, n), gcd(pow(A, q, n)-1, n)
            assert g2 == gcd(power(a, E*q, n)-1, n)
            if a == 2:
                assert A == 1 and g1 == n and g2 == n
            elif n == n6:
                assert g1 == 1 and g2 == p
            rows.append(dict(N=n, base=a, stage1_residue=A,
                             stage1_gcd=g1, stage2_q=q, stage2_gcd=g2))
    # Every exponent, not just the published stage bounds, fails for n6.
    for t in [p, r]:
        assert power(2, 428, t) == 1
        assert power(2, 214, t) != 1 and power(2, 4, t) != 1
    gcd_period = Counter(gcd(power(2, d, n6)-1, n6) for d in range(1, 429))
    assert gcd_period == {1: 427, n6: 1}
    targets = [q for q in range(1001, 100000) if prime(q)]
    wheel = {30*r-k for r in range(33, 3335)
             for k in [1, 7, 11, 13, 17, 19, 23, 29]}
    assert len(targets) == 9424 and set(targets) <= wheel
    assert targets[-1] == 99991 and 99991 == 30*3334-29
    # The six-wheel recurrence alternates +4,+2 from 1009.
    q, step, six = 1009, 4, set()
    while q < 100000:
        six.add(q)
        q, step = q+step, 6-step
    assert set(targets) <= six
    batch_checks = 0
    for n in range(3, 100, 2):
        for A in range(1, n):
            if gcd(A, n) != 1:
                continue
            for r0 in [1, 33, 1375, 3334]:
                for k in [1, 7, 11, 13, 17, 19, 23, 29]:
                    assert gcd(pow(A, 30*r0-k, n)-1, n) == gcd(
                        pow(A, 30*r0, n)-pow(A, k, n), n)
                    batch_checks += 1
    return dict(E=E, E_bits=E.bit_length(), stage1_primes=len(small),
                independent_state_checks=state_checks, examples=rows,
                base2_n6_gcd_period=dict(gcd_period),
                stage2_target_primes=len(targets), wheel_size=len(wheel),
                six_wheel_size=len(six), batch_identity_checks=batch_checks,
                prime_certificates_reused='results/primality-certificates.json')


def lucas_identities():
    sequence_checks = composition_checks = character_checks = product_checks = 0
    for n in range(3, 48, 2):
        for P in range(n):
            v = [2 % n, P]
            for j in range(2, 65):
                v.append((P*v[-1]-v[-2]) % n)
            for e, expected in enumerate(v):
                assert v_binary(P, e, n) == v_matrix(P, e, n) == expected
                sequence_checks += 1
            for a in range(9):
                for b in range(9):
                    assert v_binary(v[b], a, n) == v[a*b]
                    composition_checks += 1
    primes = [p for p in range(3, 100, 2) if prime(p)]
    for p in primes:
        signs = Counter()
        for P in range(p):
            delta = (P*P-4) % p
            value = pow(delta, (p-1)//2, p)
            sign = -1 if value == p-1 else value
            signs[sign] += 1
            if sign == -1:
                assert v_binary(P, p+1, p) == 2 % p
            elif sign == 1:
                assert v_binary(P, p-1, p) == 2 % p
            character_checks += 1
        assert signs[0] == 2 and signs[-1] == (p-1)//2
        assert signs[1] == (p-3)//2
    # Deterministic nonzero integer M is represented modulo each target p.
    for D in range(1, 101):
        for p in primes:
            if D % (p+1) == 0:
                assert prod(v_binary(P, D, p)-2 for P in range(3, D+2)) % p == 0
                product_checks += 1
    return dict(sequence_checks=sequence_checks,
                composition_checks=composition_checks,
                discriminant_cases=character_checks,
                deterministic_product_cases=product_checks)


def pminus_probability():
    cases = samples = 0
    minimum = Fraction(1)
    for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
        for r in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
            if p == r:
                continue
            for multiplier in [1, 2, 3, 5, 8]:
                E = (p-1)*multiplier
                K, s = odd_part(E)
                n, good, total = p*r, 0, 0
                for a in range(1, n):
                    if gcd(a, n) != 1:
                        continue
                    x = pow(a, K, n)
                    found = False
                    for j in range(s+1):
                        found |= 1 < gcd(x-1, n) < n
                        x = x*x % n
                    good += found
                    total += 1
                assert total == (p-1)*(r-1) and 2*good >= total
                minimum = min(minimum, Fraction(good, total))
                cases += 1
                samples += total
    return dict(instances=cases, uniform_unit_samples=samples,
                minimum_success=str(minimum))


def pplus_probability():
    # Exhaust the actual quadratic-algebra sampling construction, not random P.
    samples = trace_checks = 0
    rows = []
    for p, r in [(3, 5), (3, 7), (5, 7), (5, 11), (7, 11)]:
        n = p*r
        deltas = [d for d in range(1, n) if gcd(d, n) == 1]
        probabilities = [Fraction(0) for _ in range(3)]
        for delta in deltas:
            fibers = Counter()
            for a in range(n):
                for b in range(n):
                    h = (a*a-delta*b*b) % n
                    if gcd(h, n) != 1:
                        continue
                    inverse = pow(h, -1, n)
                    gamma = ((a*a+delta*b*b)*inverse % n, 2*a*b*inverse % n)
                    assert (gamma[0]**2-delta*gamma[1]**2) % n == 1
                    fibers[gamma] += 1
                    samples += 1
            cp = -1 if pow(delta, (p-1)//2, p) == p-1 else 1
            cr = -1 if pow(delta, (r-1)//2, r) == r-1 else 1
            assert len(fibers) == (p-cp)*(r-cr)
            assert set(fibers.values()) == {(p-1)*(r-1)}
            for i, multiplier in enumerate([1, 2, 5]):
                E = (p+1)*multiplier
                K, s = odd_part(E)
                good = 0
                for gamma in fibers:
                    z = qp(gamma, K, delta, n)
                    P = 2*gamma[0] % n
                    assert (2*z[0]) % n == v_matrix(P, K, n)
                    found = False
                    for j in range(s+1):
                        found |= 1 < gcd(2*z[0]-2, n) < n
                        for t in [p, r]:
                            assert ((2*z[0]-2) % t == 0) == (
                                z[0] % t == 1 and z[1] % t == 0)
                        z = qm(z, z, delta, n)
                        trace_checks += 1
                    good += found
                if cp == -1:
                    assert 2*good >= len(fibers)
                probabilities[i] += Fraction(good, len(fibers)*len(deltas))
        assert all(value >= Fraction(1, 4) for value in probabilities)
        rows.append(dict(p=p, r=r, uniform_delta_count=len(deltas),
                         success_probabilities=[str(v) for v in probabilities]))
    return dict(norm_unit_samples=samples, trace_identity_checks=trace_checks,
                cases=rows)


def main():
    result = json.loads(OUT.read_text()) if OUT.exists() else {}
    for name, fn in [('book_example', book_example), ('lucas_identities', lucas_identities),
                     ('pminus_probability', pminus_probability),
                     ('pplus_probability', pplus_probability)]:
        if name in result:
            print('REUSE', name, flush=True)
            continue
        started = time.monotonic()
        data = fn()
        data['seconds'] = time.monotonic()-started
        data['passed'] = True
        result[name] = data
        temporary = OUT.with_suffix('.tmp')
        temporary.write_text(json.dumps(result, indent=2)+'\n')
        os.replace(temporary, OUT)
        print(name, json.dumps(data), flush=True)


if __name__ == '__main__':
    main()
