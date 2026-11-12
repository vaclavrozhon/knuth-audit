#!/usr/bin/env python3
"""Exact checks of the Lucas rank criterion and Lucas-Lehmer test.

Independent models: linear recurrence, companion matrices, and a quadratic
algebra. General proofs, and the scope of the finite checks, are in the notes.
"""
from math import comb, gcd, isqrt, lcm
from pathlib import Path
import json
import os
import time

BASE = Path(__file__).resolve().parent
OUT = BASE / 'results/primality-lucas.json'


def factors(n):
    out = []
    for p in range(2, isqrt(n) + 1):
        if p * p > n:
            break
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
    if n > 1:
        out.append((n, 1))
    return out


def prime(n):
    return n >= 2 and all(n % p for p in range(2, isqrt(n) + 1))


def seq(P, Q, end, modulus=None):
    u, v = [0, 1], [2, P]
    for j in range(1, end):
        a, b = P * u[-1] - Q * u[-2], P * v[-1] - Q * v[-2]
        if modulus is not None:
            a, b = a % modulus, b % modulus
        u.append(a)
        v.append(b)
    return u, v


def mm(A, B, n):
    a, b, c, d = A
    e, f, g, h = B
    return ((a * e + b * g) % n, (a * f + b * h) % n,
            (c * e + d * g) % n, (c * f + d * h) % n)


def mat(P, Q, k, n):
    A, B = (1, 0, 0, 1), (P % n, -Q % n, 1, 0)
    while k:
        if k & 1:
            A = mm(A, B, n)
        B = mm(B, B, n)
        k >>= 1
    return A


def identities():
    exact = additions = liftings = 0
    for P in range(-6, 7):
        for Q in range(-6, 7):
            u, v = seq(P, Q, 65)
            D = P * P - 4 * Q
            for n in range(1, 33):
                assert (1 << (n - 1)) * u[n] == sum(
                    comb(n, 2 * k + 1) * P ** (n - 2 * k - 1) * D ** k
                    for k in range((n - 1) // 2 + 1))
                assert (1 << (n - 1)) * v[n] == sum(
                    comb(n, 2 * k) * P ** (n - 2 * k) * D ** k
                    for k in range(n // 2 + 1))
                assert v[n] == u[n + 1] - Q * u[n - 1]
                assert u[2 * n] == u[n] * v[n]
                assert v[2 * n] == v[n] ** 2 - 2 * Q ** n
                exact += 1
            for m in range(1, 17):
                for n in range(17):
                    assert u[m + n] == u[m] * u[n + 1] - Q * u[m - 1] * u[n]
                    additions += 1
    for p in range(2, 98):
        if not prime(p):
            continue
        chi = 0 if p in (2, 3) else (1 if pow(3, (p - 1) // 2, p) == 1 else -1)
        for e in range(1, 4):
            for k in range(1, 9):
                n = k * p ** (e - 1) * (p - chi)
                modulus = p ** (e + 1)
                un = mat(4, 1, n, modulus)[2]
                a = mat(4, 1, n + 1, modulus)[2]
                assert un % (p ** e) == 0
                assert mat(4, 1, p * n, modulus)[2] == 0
                for j in (1, 2, 3, p):
                    assert mat(4, 1, j * n, modulus)[2] == j * pow(a, j - 1, modulus) * un % modulus
                    assert mat(4, 1, j * n + 1, modulus)[2] == pow(a, j, modulus)
                liftings += 1
    return dict(exact_UV_indices=exact, addition_identities=additions,
                lifting_cases=liftings, scope='Includes negative and zero P,Q,D; special lifting includes primes2 and3.')


def criterion():
    cases = accepted = nonunit_Q = rank_cases = matrix_checks = 0
    for N in range(3, 512, 2):
        fs = factors(N)
        qs = [p for p, e in factors(N + 1)]
        for P in range(-5, 6):
            for Q in range(-5, 6):
                D = P * P - 4 * Q
                if gcd(P, Q) != 1 or gcd(N, 2 * D) != 1:
                    continue
                unit = gcd(Q, N) == 1
                if unit:
                    t = lcm(*(p ** (a - 1) * (p - (1 if pow(D, (p - 1) // 2, p) == 1 else -1))
                              for p, a in fs))
                    end = max(N + 1, 2 * t)
                else:
                    end = N + 1
                u, v = seq(P, Q, end, N)
                indices = [N + 1] + [(N + 1) // p for p in qs]
                for k in indices:
                    A = mat(P, Q, k, N)
                    assert A[2] == u[k] and (A[0] + A[3]) % N == v[k]
                    matrix_checks += 1
                good = u[N + 1] == 0 and all(u[(N + 1) // p] != 0 for p in qs)
                assert not good or prime(N), (N, P, Q)
                accepted += good
                if not unit:
                    assert u[N + 1] != 0
                    nonunit_Q += 1
                else:
                    assert u[t] == 0
                    rank = next(j for j in range(1, t + 1) if u[j] == 0)
                    assert t % rank == 0
                    assert all((u[j] == 0) == (j % rank == 0) for j in range(end + 1))
                    assert good == (rank == N + 1)
                    rank_cases += 1
                cases += 1
    fib = seq(1, -1, 24, 23)[0]
    assert fib == [0, 1, 1, 2, 3, 5, 8, 13, 21, 11, 9, 20, 6,
                   3, 9, 12, 21, 10, 8, 18, 3, 21, 1, 22, 0]
    assert seq(1, -1, 7, 13)[0][7] == 0
    assert seq(1, -1, 9, 17)[0][9] == 0
    return dict(cases=cases, prime_witnesses=accepted, nonunit_Q_rejections=nonunit_Q,
                full_rank_checks=rank_cases, independent_matrix_checks=matrix_checks,
                fibonacci_example=fib, N_range='all odd3..511', P_Q_range=[-5, 5])


def lucas_lehmer():
    small = []
    for q in range(3, 32):
        N = (1 << q) - 1
        L = 4
        for _ in range(q - 2):
            L = (L * L - 2) % N
        assert (L == 0) == prime(N)
        small.append(dict(q=q, residue=L, prime=(L == 0)))
    listed = [3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127,
              521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213]
    records = []
    for q in listed:
        assert prime(q)
        N = (1 << q) - 1
        L, a, b = 4, 2, 1  # a+b*sqrt3, whose norm is1 and trace is L.
        for j in range(q - 2):
            # Model1: scalar recurrence with Mersenne folding, no division.
            w = L * L - 2
            if w < 0:
                w += N
            L = (w & N) + (w >> q)
            L = (L & N) + (L >> q)
            if L >= N:
                L -= N
            # Model2: quadratic-algebra powering, ordinary remainder.
            a, b = (a * a + 3 * b * b) % N, (2 * a * b) % N
            assert L == 2 * a % N
        assert L == 0
        assert (a * a - 3 * b * b) % N == 1
        records.append(dict(q=q, squarings=q - 2, scalar_residue=L,
                            quadratic_trace=2 * a % N, quadratic_norm=1))
    return dict(all_exponents_3_to_31=small, listed_prime_certificates=records,
                scope='22 odd listed exponents through11213; exponent2 handled directly. Larger published primes not recomputed here.')


def precheck_counterexamples():
    rows = []
    for N, Q in [(5, -1), (3, 1), (3, 0)]:
        P = 1
        D = 1 - 4 * Q
        assert gcd(P, Q) == 1 and prime(N)
        assert gcd(N, Q * D) > 1
        assert not abs(Q * D) > N
        rows.append(dict(N=N, P=P, Q=Q, D=D, QD=Q * D,
                         gcd=gcd(N, Q * D), abs_QD_exceeds_N=False,
                         N_is_prime=True))
    return dict(counterexamples=rows,
                correction='Conclude composite only when 1<gcd(N,QD)<N.')


def main():
    data = json.loads(OUT.read_text()) if OUT.exists() else {'pid': os.getpid(), 'checkpoints': {}}
    for name, fn in [('identities', identities), ('criterion', criterion),
                     ('lucas_lehmer', lucas_lehmer), ('precheck', precheck_counterexamples)]:
        if name in data['checkpoints']:
            print('REUSE', name, flush=True)
            continue
        started = time.monotonic()
        result = fn()
        result.update(passed=True, seconds=time.monotonic() - started)
        data['checkpoints'][name] = result
        OUT.write_text(json.dumps(data, indent=2) + '\n')
        print(name, json.dumps(result), flush=True)
    data['passed'] = True
    OUT.write_text(json.dumps(data, indent=2) + '\n')
    print('ALL PASSED', flush=True)


if __name__ == '__main__':
    main()
