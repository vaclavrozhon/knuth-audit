"""Exact checks of 3.2.2-15 and added 3.2.2-38; no floating point."""
from fractions import Fraction
from itertools import product
from math import gcd
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def least_period(a):
    n = len(a)
    for d in range(1, n + 1):
        if n % d == 0 and all(a[i] == a[i % d] for i in range(n)):
            return d
    raise AssertionError


def gaps(a):
    """One complete cyclic word of backward return times."""
    last = {}
    q = []
    for i, v in enumerate(a + a):
        if i >= len(a):
            q.append(i - last[v])
        last[v] = i
    return q


def lcg(a, c, m):
    x, out = 0, []
    while not out or x:
        out.append(x)
        x = (a*x + c) % m
        assert len(out) <= m
    assert len(out) == m
    return out


def main():
    ys = lcg(5, 1, 16)
    # Independent integer geometric sum, before any modular reductions.
    assert ys == [((5**n - 1)//4) % 16 for n in range(16)]
    js = [y//8 for y in ys]
    qs = gaps(js)
    # Independently search backwards in the cyclic word, rather than a last map.
    assert qs == [next(r for r in range(1, 17) if js[(n-r) % 16] == js[n])
                  for n in range(16)]
    assert least_period(qs) == 8 and max(qs) == 5 < 16/2
    table, out = [0, 1], []
    for n in range(64):
        j = js[n % 16]
        out.append(table[j])
        table[j] = (n+2) % 16  # X_n = n mod 16; first two fill the table.
        if n >= max(qs):
            assert out[-1] == (n+2-qs[n % 16]) % 16
    assert least_period(out[32:48]) == 16
    c7 = dict(m=16, e=4, a=5, c=1, k=2, Y=ys, j=js, q=qs,
              gap_period=8, claimed_bound=4, max_gap=5, X_period=16,
              output_period=16)

    bound_cases = 0
    k2_failures = 0
    for e in range(2, 8):
        m = 2**e
        for a in range(1, m, 4):
            for c in range(1, m, 2):
                y = lcg(a, c, m)
                for r in range(e+2):
                    k = 2**r
                    q = gaps([k*v//m for v in y])
                    p = least_period(q)
                    bound = m//2 if k == 2 else m//4
                    assert bound % p == 0, (e,a,c,k,p)
                    k2_failures += int(k == 2 and p > m//4)
                    bound_cases += 1

    digit_words = digit_transitions = 0
    exceptions = []
    for b in range(2, 7):
        for length in range(1, 6):
            modulus = b**length - 1
            for digits in product(range(b), repeat=length):
                value = 0
                for digit in digits:
                    value = b*value + digit
                d = gcd(value, modulus)
                m, X = modulus//d, value//d
                if value == modulus:
                    assert X == m == 1
                    error = abs(Fraction(X, m) - Fraction(digits[0], b))
                    assert error == Fraction(1, b)
                    exceptions.append(dict(b=b, length=length, X0=X, m=m))
                    continue
                rotation = list(digits)
                for n in range(2*length+1):
                    rotated_value = 0
                    for digit in rotation:
                        rotated_value = b*rotated_value + digit
                    assert Fraction(X, m) == Fraction(rotated_value, modulus)
                    following = b*X % m
                    assert b*X == m*digits[n % length] + following
                    error = Fraction(X, m) - Fraction(digits[n % length], b)
                    assert 0 <= error < Fraction(1, b)
                    assert error == Fraction(following, b*m)
                    X = following
                    rotation = rotation[1:] + rotation[:1]
                    digit_transitions += 1
                digit_words += 1
    result = dict(status='passed', C0007=c7,
                  corrected_gap_bounds_cases=bound_cases,
                  k2_original_bound_failures=k2_failures,
                  C0008=dict(b=2, digits=[1], d=1, m=1, X=[1,0,0],
                             error_at_n0='1/2', claimed_strict_bound='1/2'),
                  corrected_digit_words=digit_words,
                  corrected_digit_transitions=digit_transitions,
                  excluded_all_maximum_words=exceptions)
    (ROOT/'results/shuffling-boundaries.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items()
                      if k != 'excluded_all_maximum_words'}, indent=2))


if __name__ == '__main__':
    main()
