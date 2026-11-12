"""Exact supplementary checks for TAOCP 1.2.4; not a substitute for proofs."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb, gcd, isqrt
from pathlib import Path
import json


def floor(x):
    x = Q(x)
    return x.numerator // x.denominator


def ceil(x):
    return -floor(-x)


def mod(x, y):
    return x - y * floor(x / y) if y else x


def congruent(a, b, m):
    return a == b if not m else (a - b) % m == 0


def factor(n):
    result = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            result[d] = result.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        result[n] = 1
    return result


def totient(n):
    value = n
    for p in factor(n):
        value = value // p * (p - 1)
    return value


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def ilog(n, b):
    answer = 0
    while n >= b:
        n //= b
        answer += 1
    return answer


def binomial(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def main():
    counts = Counter()
    rationals = sorted({Q(a, d) for a in range(-12, 13) for d in range(1, 9)})
    for x, y in product(rationals, repeat=2):
        frac_sum = x - floor(x) + y - floor(y)
        assert floor(x) + floor(y) <= floor(x + y)
        assert (floor(x) + floor(y) == floor(x + y)) == (frac_sum < 1)
        assert ceil(x) + ceil(y) >= ceil(x + y)
        assert (ceil(x) + ceil(y) == ceil(x + y)) == (
            x.denominator == 1 or y.denominator == 1 or frac_sum > 1)
        counts['floor_ceiling_pairs'] += 1
    small = sorted({Q(a, d) for a in range(-4, 5) for d in range(1, 4)})
    for x, y, z in product(small, repeat=3):
        assert z * mod(x, y) == mod(z * x, z * y)
        counts['mod_homogeneity_triples'] += 1
    for x, m, n in product(rationals, range(-6, 7), range(1, 10)):
        assert floor((x + m) / n) == floor(Q(floor(x) + m, n))
        assert ceil((x + m) / n) == ceil(Q(ceil(x) + m, n))
        counts['nested_rounding_triples'] += 1

    ints = range(-4, 5)
    for a, b, x, y, m in product(ints, repeat=5):
        if congruent(a, b, m) and congruent(x, y, m):
            assert congruent(a + x, b + y, m)
            assert congruent(a - x, b - y, m)
            assert congruent(a * x, b * y, m)
            counts['law_A_instances'] += 1
        if congruent(a * x, b * y, m) and congruent(a, b, m) and gcd(a, m) == 1:
            assert congruent(x, y, m)
            counts['law_B_instances'] += 1
    for a, b, m, n in product(ints, repeat=4):
        if n:
            assert congruent(a, b, m) == congruent(a * n, b * n, m * n)
            counts['law_C_instances'] += 1
        if gcd(m, n) == 1:
            assert congruent(a, b, m * n) == (congruent(a, b, m) and congruent(a, b, n))
            counts['law_D_instances'] += 1
    primes = [p for p in range(2, 102) if len(divisors(p)) == 2]
    for p, a in product(primes, range(-200, 201)):
        assert pow(a, p, p) == a % p
        assert pow(a, p - 1, p) == int(a % p != 0)
        if p > 2:
            assert pow(a, (p - 1) // 2, p) in (0, 1, p - 1)
        counts['Fermat_instances'] += 1
    for m in range(1, 81):
        phi = sum(gcd(x, m) == 1 for x in range(m))
        assert phi == totient(m)
        for a in range(-80, 81):
            if gcd(a, m) == 1:
                assert pow(a, phi, m) == 1 % m
                counts['Euler_instances'] += 1
    assert totient(10**6) == 400000
    for r, s in product(range(1, 21), repeat=2):
        if gcd(r, s) != 1:
            continue
        u = [x for x in range(r) if gcd(x, r) == 1]
        v = [y for y in range(s) if gcd(y, s) == 1]
        outputs = [(s * x + r * y) % (r * s) for x, y in product(u, v)]
        assert len(set(outputs)) == len(outputs)
        assert set(outputs) == {z for z in range(r * s) if gcd(z, r * s) == 1}
        assert totient(r * s) == totient(r) * totient(s)
        counts['CRT_totient_pairs'] += 1
    for n in range(1, 101):
        left = [(c, d) for d in divisors(n) for c in divisors(d)]
        right = [(c, c * d) for c in divisors(n) for d in divisors(n // c)]
        assert Counter(left) == Counter(right)
        counts['divisor_bijections'] += 1

    for m, n in product(range(-30, 31), repeat=2):
        assert floor(Q(n + m, 2)) + floor(Q(n - m + 1, 2)) == n
        assert ceil(Q(n + m, 2)) + ceil(Q(n - m + 1, 2)) == n + 1
        counts['parity_pairs'] += 1
    floor_half_sum = ceiling_half_sum = sqrt_sum = 0
    for n in range(0, 10001):
        floor_half_sum += n // 2
        ceiling_half_sum += (n + 1) // 2
        sqrt_sum += isqrt(n)
        assert floor_half_sum == n * n // 4
        assert ceiling_half_sum == ceil(Q(n * (n + 2), 4))
        h = isqrt(n)
        assert sqrt_sum == h * (n - Q((2 * h + 5) * (h - 1), 6))
        if n:
            k = (isqrt(8 * n - 7) + 1) // 2
            assert k * (k - 1) < 2 * n <= k * (k + 1)
            assert (2 * k - 1)**2 < 8 * n < (2 * k + 1)**2
            counts['triangular_sequence_values'] += 1
        counts['floor_sums_36_43'] += 1
    for b in range(2, 17):
        direct = 0
        for n in range(1, 1001):
            ell = ilog(n, b)
            direct += ell
            assert direct == (n + 1) * ell - (b**(ell + 1) - b) // (b - 1)
            counts['logarithm_sums'] += 1
    for b, n in product(range(2, 17), range(-200, 201)):
        power, total = 1, 0
        # At power>|n| all later inner sums vanish, for either sign of n.
        while power <= abs(n):
            total += sum((n + j * power) // (b * power) for j in range(1, b))
            power *= b
        assert sum((n + j * power) // (b * power) for j in range(1, b)) == 0
        assert total == (n if n >= 0 else n + 1)
        counts['base_telescoping_sums'] += 1

    alphas = sorted({Q(p, d) for p in range(1, 13) for d in range(1, 7)})
    for m, n, alpha in product(range(1, 17), range(1, 17), alphas):
        N, R = ceil(alpha * n), ceil(alpha * m)
        left = Counter((m * j) // n for j in range(N))
        right = Counter()
        for r in range(1, R):
            c = ceil(Q(r * n, m))
            right[r - 1] += c
            right[r] -= c
        right[R - 1] += N
        assert left == right
        assert all(c >= 0 for c in right.values())
        counts['general_reciprocity_coefficient_vectors'] += 1
    for m, n in product(range(1, 17), repeat=2):
        for k in range(m + 3):
            left = sum(binomial((m * j) // n + 1, k) for j in range(n))
            left += sum(ceil(Q(j * n, m)) * binomial(j, k - 1) for j in range(m))
            assert left == n * binomial(m, k)
            counts['binomial_reciprocity_instances'] += 1

    def legendre(q, p):
        residue = pow(q, (p - 1) // 2, p)
        return -1 if residue == p - 1 else residue

    odd_primes = primes[1:]
    for p, q in product(odd_primes, range(-200, 201)):
        h = (p - 1) // 2
        if q % p:
            sigma = sum((2 * k * q) // p for k in range(1, h + 1))
            residues = [((-1 if ((2 * k * q) // p) % 2 else 1) * (2 * k * q % p)) % p
                        for k in range(1, h + 1)]
            assert sorted(residues) == list(range(2, p, 2))
            assert legendre(q, p) == (1 if sigma % 2 == 0 else -1)
            if q % 2:
                assert sigma % 2 == sum(k * q // p for k in range(1, h + 1)) % 2
            counts['Legendre_parity_instances'] += 1
        assert legendre(2, p) == (1 if p % 8 in (1, 7) else -1)
    for p, q in product(odd_primes, repeat=2):
        if p != q:
            exponent = (p - 1) * (q - 1) // 4
            assert legendre(q, p) * legendre(p, q) == (1 if exponent % 2 == 0 else -1)
            counts['quadratic_reciprocity_prime_pairs'] += 1
    for n in range(-10000, 10001):
        assert (n + 2 - n // 25) // 3 == (8 * n + 24) // 25
        counts['identity_48b_values'] += 1
    for m, n in product(range(-100, 101), range(1, 101)):
        assert (m + n - 1) // n == ceil(Q(m, n))
        counts['identity_48a_positive_denominators'] += 1
    for beta, m in product([Q(1, 3), Q(1, 2), Q(1), Q(3, 2), Q(22, 7)], range(-100, 101)):
        if beta >= 1:
            n = ceil(m * beta)
            assert floor(n / beta) == m
        else:
            n = m
            assert ceil(floor(n / beta) * beta) == n
        counts['added_exercise_50_instances'] += 1
    # Reuse the existing certified decimal interval, not another constants run.
    source = Path(__file__).resolve().parent / 'results/elementary-constants.json'
    prefix = json.loads(source.read_text())['constants']['pi']['truncated_40_places']
    pi_lo, pi_hi = Q(prefix), Q(prefix) + Q(1, 10**40)
    assert ceil(1000 * pi_lo) == ceil(1000 * pi_hi) == 3142
    for numerator in (3142, 3143):
        assert floor(numerator / pi_lo) == floor(numerator / pi_hi) == 1000

    # Published corrections and transcription mistakes have exact witnesses.
    assert sum((2 * k * 3) // 3 for k in range(1, 2)) % 2 != sum(k * 3 // 3 for k in range(1, 2)) % 2
    assert floor(Q(0 - 1 - 1, -1)) == 2 and ceil(Q(0, -1)) == 0
    result = dict(status='passed', arithmetic='integers and fractions.Fraction only',
                  counts=dict(counts),
                  scope='Finite supplementary checks for proofs in integer-functions.md; no repetition of exercises 37–38; analytic classification is proved separately.')
    out = Path(__file__).resolve().parent / 'results/integer-functions.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
