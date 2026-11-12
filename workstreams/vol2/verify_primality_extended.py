#!/usr/bin/env python3
"""Two BLS certificates, validated by separate modular arithmetic models.

No primality oracle is used for the large targets. The proof using these
certificates is in notes/primality-extended.md.
"""
from math import gcd, isqrt, prod
from pathlib import Path
import json
import os
import time

BASE = Path(__file__).resolve().parent
OUT = BASE / "results/primality-extended.json"


def prime_trial(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def sieve(bound):
    a = bytearray(b"\x01") * bound
    a[:2] = b"\x00\x00"
    for d in range(2, isqrt(bound - 1) + 1):
        if a[d]:
            a[d * d:bound:d] = b"\x00" * ((bound - 1 - d * d) // d + 1)
    return [d for d in range(2, bound) if a[d]]


def modpower(a, e, n):
    # Left-to-right, separate from Python's built-in pow.
    v = 1
    for bit in bin(e)[2:]:
        v = v * v % n
        if bit == "1":
            v = v * a % n
    return v


def matmul(A, B, n):
    return tuple(sum(A[2 * i + k] * B[2 * k + j] for k in range(2)) % n
                 for i in range(2) for j in range(2))


def lucas_matrix(P, Q, k, n):
    A, M = (1, 0, 0, 1), (P % n, -Q % n, 1, 0)
    for bit in bin(k)[2:]:
        A = matmul(A, A, n)
        if bit == "1":
            A = matmul(A, M, n)
    return A[2]


def lucas_algebra(P, Q, k, n):
    # (a+b*t)(c+d*t), with t*t=P*t-Q.
    def mul(x, y):
        a, b = x
        c, d = y
        return ((a * c - Q * b * d) % n,
                (a * d + b * c + P * b * d) % n)
    a, b = (1, 0), (0, 1)
    while k:
        if k & 1:
            a = mul(a, b)
        b = mul(b, b)
        k >>= 1
    return a[1]


def jacobi(a, n):
    assert n > 0 and n % 2
    v = 1
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                v = -v
        if a % 4 == n % 4 == 3:
            v = -v
        a, n = n % a, a
    return v if n == 1 else 0


def certificate(e, removed, fm, fp, bound, Q):
    started = time.monotonic()
    mersenne = (1 << e) - 1
    assert mersenne % removed == 0
    N = mersenne // removed
    Fm = prod(p ** a for p, a in fm)
    Fp = prod(p ** a for p, a in fp)
    for p, a in fm + fp:
        assert a >= 1 and prime_trial(p)
    assert (N - 1) % Fm == (N + 1) % Fp == 0
    Rm, Rp = (N - 1) // Fm, (N + 1) // Fp
    assert Fm % 2 == Fp % 2 == 0 and Rm > 1 and Rp > 1
    assert gcd(Fm, Rm) == gcd(Fp, Rp) == 1
    assert gcd(Fm, Fp) == 2
    ps = sieve(bound)
    assert all(Rm % p and Rp % p for p in ps)
    # Independent direct enumeration covers every possible odd prime divisor.
    assert Rm % 2 and Rp % 2
    direct_divisors = 0
    for d in range(3, bound, 2):
        assert Rm % d and Rp % d
        direct_divisors += 1
    lhs = bound ** 3 * Fm * Fp * max(Fm, Fp)
    assert lhs > 2 * N
    assert Fm * Fm < N and Fp * Fp < N  # Full Pocklington bounds do not apply.
    minus = []
    initial_base = 13
    assert pow(13, N - 1, N) == modpower(13, N - 1, N) == 1
    for divisor in [p for p, _ in fm] + [Rm]:
        k = (N - 1) // divisor
        rejected = []
        for a in [13] + [a for a in range(2, 100) if a != 13]:
            assert pow(a, N - 1, N) == modpower(a, N - 1, N) == 1
            value = pow(a, k, N)
            g = gcd(value - 1, N)
            if g == 1:
                break
            assert g == N, (a, divisor, g)
            rejected.append(a)
        else:
            raise AssertionError(('No witness among selected bases', divisor))
        assert value == modpower(a, k, N)
        assert g == 1
        minus.append(dict(base=a, rejected_bases=rejected,
                          divisor=str(divisor), exponent=str(k),
                          residue=str(value), gcd=g))
    P, D = 1, 1 - 4 * Q
    assert gcd(N, 2 * Q * D) == 1 and jacobi(D, N) == -1
    assert lucas_matrix(P, Q, N + 1, N) == lucas_algebra(P, Q, N + 1, N) == 0
    plus = []
    for divisor in [p for p, _ in fp] + [Rp]:
        k = (N + 1) // divisor
        value = lucas_matrix(P, Q, k, N)
        assert value == lucas_algebra(P, Q, k, N)
        g = gcd(value, N)
        assert g == 1
        plus.append(dict(divisor=str(divisor), index=str(k),
                         residue=str(value), gcd=g))
    return dict(passed=True, N=str(N), digits=len(str(N)),
                mersenne_exponent=e, removed=str(removed),
                F_minus=str(Fm), F_plus=str(Fp), R_minus=str(Rm), R_plus=str(Rp),
                minus_factors=fm, plus_factors=fp, bound=bound,
                sieve_primes=len(ps), direct_odd_divisors=direct_divisors,
                inequality_lhs=str(lhs), inequality_rhs=str(2 * N),
                initial_base=initial_base, P=P, Q=Q, D=D, jacobi=-1,
                minus_tests=minus, plus_tests=plus,
                seconds=time.monotonic() - started)


def main():
    if OUT.exists():
        data = json.loads(OUT.read_text())
    else:
        data = {}
    examples = [
        ("M167_cofactor", (167, 2349023,
                          [(2, 5), (11, 1), (37, 1), (167, 1)],
                          [(2, 1), (3, 3), (5, 2), (1381, 1), (3167, 1)],
                          2000000, -13)),
        ("M241_cofactor", (241, 22000409,
                          [(2, 1), (241, 1), (21221, 1)],
                          [(2, 3), (3, 2), (5, 1), (23, 1), (643, 1),
                           (96763, 1), (4975177, 1), (17944799, 1)],
                          21221, -5)),
    ]
    print("pid", os.getpid(), flush=True)
    for name, args in examples:
        if name in data:
            assert data[name]["passed"]
            continue
        data[name] = certificate(*args)
        tmp = OUT.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, indent=2) + "\n")
        tmp.replace(OUT)
        print(name, "passed", data[name]["digits"], "digits",
              data[name]["seconds"], "seconds", flush=True)


if __name__ == "__main__":
    main()
