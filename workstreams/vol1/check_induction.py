"""Exact independent checks for §1.2.1; universal proofs are in notes/induction.md.

The quadratic arithmetic uses integer coefficient pairs, never floating point.
The finite checks certify their stated domains, not all possible inputs.
"""
from fractions import Fraction
from itertools import product
from math import gcd
from pathlib import Path
import json


def extended(m, n):
    # Execute the assignments in their printed order, including the temporary.
    clock = 1
    ap = b = 1
    a = bp = 0
    c, d = m, n
    trace = []
    assert clock == 1 and c == m and d == n
    while True:
        assert ap*m+bp*n == c and a*m+b*n == d and d > 0
        assert gcd(c, d) == gcd(m, n)
        assert clock <= 3*(n-d)+1
        clock += 1
        q, r = divmod(c, d)
        assert c == q*d+r and 0 <= r < d
        assert clock <= 3*(n-d)+2
        trace.append([ap, a, bp, b, c, d, q, r])
        clock += 1
        assert clock <= 3*(n-d)+3 <= 3*n
        if r == 0:
            assert d == gcd(m, n) and a*m+b*n == d
            return a, b, d, clock, trace
        clock += 1
        c = d
        d = r
        t = ap
        ap = a
        a = t-q*a
        t = bp
        bp = b
        b = t-q*b


ZERO, ONE = (0, 0), (1, 0)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[0], -x[1]


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0]


def norm(x):
    return x[0]**2-2*x[1]**2


def sign(x):
    u, v = x
    if u == 0:
        return (v > 0)-(v < 0)
    if v == 0:
        return (u > 0)-(u < 0)
    if u*v > 0:
        return (u > 0)-(u < 0)
    # Opposite signs: compare the squared absolute magnitudes.
    delta = u*u-2*v*v
    assert delta != 0  # irrationality of sqrt(2)
    return ((u > 0)-(u < 0))*((delta > 0)-(delta < 0))


def ordinary_divmod(c, d):
    assert sign(c) > 0 and sign(d) > 0
    q, r = 0, c
    while sign(sub(r, d)) >= 0:
        q += 1
        r = sub(r, d)
    assert sign(r) >= 0 and sign(sub(d, r)) > 0
    return q, r


def quotient(c, d):
    denominator = norm(d)
    assert denominator != 0
    num = mul(c, (d[0], -d[1]))
    return Fraction(num[0], denominator), Fraction(num[1], denominator)


def nearest(x):
    # Deterministic choice at ties; either choice satisfies the proof.
    return (x+Fraction(1, 2)).numerator//(x+Fraction(1, 2)).denominator


def ring_extended(m, n):
    c, d = m, n
    ap, bp, a, b = ONE, ZERO, ZERO, ONE
    steps = 0
    while d != ZERO:
        assert add(mul(ap, m), mul(bp, n)) == c
        assert add(mul(a, m), mul(b, n)) == d
        x, y = quotient(c, d)
        q = nearest(x), nearest(y)
        r = sub(c, mul(q, d))
        assert abs(norm(r)) < abs(norm(d))
        ap, a = a, sub(ap, mul(q, a))
        bp, b = b, sub(bp, mul(q, b))
        c, d = d, r
        steps += 1
    assert add(mul(ap, m), mul(bp, n)) == c
    for value in (m, n):
        assert all(t.denominator == 1 for t in quotient(value, c))
    return steps


def partitions(total, smallest=1):
    if total == 0:
        yield ()
    for first in range(smallest, total+1):
        for tail in partitions(total-first, first):
            yield (first,)+tail


def main():
    cases = 0
    max_clock = 0
    for m, n in product(range(1, 129), repeat=2):
        a, b, d, clock, trace = extended(m, n)
        expected = max(k for k in range(1, min(m, n)+1) if m % k == n % k == 0)
        assert d == expected
        max_clock = max(max_clock, clock)
        cases += 1
    example = extended(1769, 551)
    assert example[:3] == (5, -16, 29)
    assert example[4] == [[1, 0, 0, 1, 1769, 551, 3, 116],
                          [0, 1, 1, -3, 551, 116, 4, 87],
                          [1, -4, -3, 13, 116, 87, 1, 29],
                          [-4, 5, 13, -16, 87, 29, 3, 0]]
    rational_sum = Fraction(0)
    for n in range(257):
        x = 2*n+1
        rational_sum += Fraction((-1)**n*x**3, x**4+4)
        assert rational_sum == Fraction((-1)**n*(n+1), 4*(n+1)**2+1)
    for n in range(1, 101):
        assert sum((-1)**(n-k)*k*k for k in range(1, n+1)) == n*(n+1)//2
        assert sum(n*n-n+2*k+1 for k in range(n)) == n**3
        assert sum(k**3 for k in range(1, n+1)) == (n*(n+1)//2)**2
    bernoulli = 0
    for denominator in range(2, 21):
        for numerator in range(1, denominator):
            a = Fraction(numerator, denominator)
            for n in range(-30, 31):
                assert (1-a)**n >= 1-n*a
                bernoulli += 1
    small_counts = [len(list(partitions(n))) for n in range(8)]
    assert small_counts == [1, 1, 2, 3, 5, 7, 11, 15]
    # The numerical example in the text is an ordinary Euclidean run scaled
    # by 4-2sqrt(2). Its quotients are checked using exact comparisons.
    c, d = (12, -6), (20, -10)
    qs = []
    while d != ZERO:
        q, r = ordinary_divmod(c, d)
        qs.append(q)
        c, d = d, r
    assert c == (4, -2) and qs == [0, 1, 1, 2]
    assert add(mul((2, 0), (12, -6)), mul((-1, 0), (20, -10))) == c
    # Prefix of the nonterminating ordinary algorithm: proof is in the note.
    c, d = ONE, (0, 1)
    unending_qs = []
    for i in range(80):
        q, r = ordinary_divmod(c, d)
        unending_qs.append(q)
        assert r != ZERO
        c, d = d, r
    assert unending_qs == [0, 1]+[2]*78
    elements = list(product(range(-5, 6), repeat=2))
    ring_cases, max_ring_steps = 0, 0
    for m, n in product(elements, repeat=2):
        if n == ZERO:
            continue
        max_ring_steps = max(max_ring_steps, ring_extended(m, n))
        ring_cases += 1
    result = dict(status='passed', integer_inputs=cases, maximum_clock=max_clock,
                  printed_example_rows=example[4], alternating_rational_sums=257,
                  sum_identity_indices=100, bernoulli_rational_cases=bernoulli,
                  partition_counts_0_to_7=small_counts, quadratic_scaled_example_quotients=qs,
                  ordinary_quadratic_nontermination_prefix_length=len(unending_qs),
                  quadratic_ring_input_pairs=ring_cases, maximum_ring_steps=max_ring_steps,
                  limitation='Finite checks supplement, not replace, the general proofs.')
    target = Path(__file__).resolve().parent/'results/induction.json'
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
