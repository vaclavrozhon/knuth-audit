#!/usr/bin/env python3
"""Historical order and storage rules, compared with whole-integer oracles."""
from pathlib import Path
import json
import random

OUT = Path(__file__).with_name('results') / 'classical-history.json'


def digits(n):
    return [int(x) for x in str(n)[::-1]]


def value(a):
    return sum(x * 10**i for i, x in enumerate(a))


def add_at(a, i, t):
    """Add t units of position i, propagating towards higher positions."""
    while t:
        if i == len(a):
            a.append(0)
        t, a[i] = divmod(a[i] + t, 10)
        i += 1


def kh_add(u, v):
    a, b = digits(u), digits(v)
    a += [0] * max(0, len(b) - len(a))
    for i in range(len(b)-1, -1, -1):
        add_at(a, i, b[i])
    return value(a)


def kh_sub(u, v):
    assert u >= v
    a, b = digits(u), digits(v)
    for i in range(len(b)-1, -1, -1):
        if a[i] < b[i]:
            j = i + 1
            while a[j] == 0:
                a[j] = 9
                j += 1
            a[j] -= 1
            a[i] += 10
        a[i] -= b[i]
    return value(a)


def kh_mul(u, v):
    a, b = digits(u), digits(v)
    steps = []
    for i in range(len(a)-1, -1, -1):
        x = a[i]
        if not x:
            continue
        for j in range(len(b)-1, -1, -1):
            if j == 0:
                a[i] = 0  # erase the old digit only at the last inner product
            while len(a) <= i+j:
                a.append(0)
            add_at(a, i+j, x*b[j])
        assert value(a) == (u // 10**i) * 10**i * v + u % 10**i
        steps.append(value(a))
    return value(a), steps


def kh_half(u):
    a = digits(u)
    half_unit = a[0] % 2
    for i in range(len(a)):
        odd, a[i] = a[i] % 2, a[i] // 2
        if i and odd:
            a[i-1] += 5
            assert a[i-1] < 10
    return value(a), half_unit


def sun_mul(u, v):
    a, b = digits(u), digits(v)
    middle = [0]
    steps = []
    for i in range(len(a)-1, -1, -1):
        for j in range(len(b)-1, -1, -1):
            while len(middle) <= i+j:
                middle.append(0)
            add_at(middle, i+j, a[i]*b[j])
            steps.append(value(middle))
        a[i] = 0
    return value(middle), steps


def board_divide(u, v):
    """Exact digit choice completes the verbal rule; ordered partial products."""
    assert v > 0
    r, q, trace = u, 0, []
    b = digits(v)
    for i in range(max(0, len(digits(u))-len(b)), -1, -1):
        d = 0
        # At most nine increments: no long-integer division in digit selection.
        while d < 9 and (d+1)*v*10**i <= r:
            d += 1
        parts = []
        for j in range(len(b)-1, -1, -1):
            r -= d*b[j]*10**(i+j)
            assert r >= 0
            parts.append(r)
        q += d*10**i
        assert u == q*v+r and r < v*10**i
        trace.append({'position': i, 'digit': d, 'partial_remainders': parts})
    return q, r, trace


def fib_mul(u, v):
    a, b = digits(u), digits(v)
    c, z, totals = 0, [], []
    for k in range(len(a)+len(b)-1):
        t = c
        for i in range(max(0, k-len(b)+1), min(k, len(a)-1)+1):
            t += a[i]*b[k-i]
        c, d = divmod(t, 10)
        z.append(d)
        totals.append(t)
        # The completed diagonals equal the written suffix plus the carry.
        diagonal_sum = sum(a[i]*b[j]*10**(i+j)
                           for i in range(len(a)) for j in range(len(b)) if i+j <= k)
        assert diagonal_sum == value(z)+c*10**(k+1)
    while c:
        c, d = divmod(c, 10)
        z.append(d)
    return value(z), totals


def main():
    count = 0
    for u in range(100):
        for v in range(100):
            assert kh_add(u, v) == u+v
            if u >= v:
                assert kh_sub(u, v) == u-v
            assert kh_mul(u, v)[0] == u*v
            assert sun_mul(u, v)[0] == u*v
            assert fib_mul(u, v)[0] == u*v
            if v:
                q, r, _ = board_divide(u, v)
                assert (q, r) == divmod(u, v)
            count += 1
    rng = random.Random(43101)
    for _ in range(500):
        u, v = rng.randrange(10**rng.randrange(1, 17)), rng.randrange(10**rng.randrange(1, 17))
        assert kh_add(u, v) == u+v
        assert kh_sub(max(u, v), min(u, v)) == abs(u-v)
        assert kh_mul(u, v)[0] == sun_mul(u, v)[0] == fib_mul(u, v)[0] == u*v
        q, r, _ = board_divide(u, v+1)
        assert (q, r) == divmod(u, v+1)
    for u in range(10000):
        q, h = kh_half(u)
        assert 2*q+h == u
    assert sun_mul(81, 81)[1] == [6400, 6480, 6560, 6561]
    assert kh_mul(2326, 214)[0] == 497764
    assert fib_mul(98, 98)[1] == [64, 150, 96]
    assert fib_mul(345, 345)[1] == [25, 42, 50, 29, 11]
    assert 497773 != 2326*214 and 497773 % 9 == (2326 % 9)*(214 % 9) % 9
    data = {'status': 'passed', 'complete_pairs_0_to_99': count,
            'random_pairs_up_to_16_digits': 500, 'halving_cases': 10000,
            'sunzi_81_squared_trace': sun_mul(81, 81)[1],
            'sunzi_6561_by_9': board_divide(6561, 9),
            'khwarizmi_2326_times_214_rows': kh_mul(2326, 214)[1],
            'khwarizmi_46468_by_324': board_divide(46468, 324),
            'fibonacci_98_squared_totals': fib_mul(98, 98)[1],
            'fibonacci_345_squared_totals': fib_mul(345, 345)[1],
            'casting_out_nines_wrong_product': 497773}
    OUT.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if not isinstance(v,list)}))


if __name__ == '__main__':
    main()
