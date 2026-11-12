#!/usr/bin/env python3
"""Exact independent checks for TAOCP 4.5.3-39/40 and C0138."""
from fractions import Fraction as F
from itertools import combinations
from math import gcd
from pathlib import Path
import json
import os
import time

ROOT = Path(__file__).resolve().parent


def cf(x):
    a, b = x.numerator, x.denominator
    word = []
    while b:
        q, r = divmod(a, b)
        word.append(q)
        a, b = b, r
    return word


def value(word):
    x = F(word[-1])
    for a in reversed(word[:-1]):
        x = a + 1 / x
    return x


def interval_cf(a, b, repair):
    x, y = cf(a)[1:], cf(b)[1:]
    k = 0
    while k < min(len(x), len(y)) and x[k] == y[k]:
        k += 1
    prefix = k == min(len(x), len(y))
    if repair and prefix:
        return (a if len(x) < len(y) else b), prefix
    # Book's j is one-based. Its parity selects the smaller complete quotient.
    w = y if (k + 1) % 2 else x
    assert k < len(w)
    z = w[k] + (k + 1 < len(w))
    return value([0] + x[:k] + [z]), prefix


def interval_tree(lo, hi):
    a, b, c, d = 0, 1, 1, 0
    path = ''
    while True:
        assert b * c - a * d == 1
        p, q = a + c, b + d
        assert gcd(p, q) == 1
        m = F(p, q)
        if m < lo:
            a, b = p, q
            path += 'R'
        elif m > hi:
            c, d = p, q
            path += 'L'
        else:
            return m, path


def denominator_oracle(lo, hi):
    # Direct integer lattice scan: independent of either tree or CF model.
    for q in range(1, min(lo.denominator, hi.denominator) + 1):
        p = (lo.numerator * q + lo.denominator - 1) // lo.denominator
        if p * hi.denominator <= hi.numerator * q:
            return F(p, q)
    raise AssertionError('Endpoint upper bound failed')


def target_path(p, q):
    a, b, c, d = 0, 1, 1, 0
    alpha, beta = q, p
    path = ''
    while True:
        assert b * c - a * d == 1
        assert alpha > 0 and beta > 0 and gcd(alpha, beta) == 1
        assert (p, q) == (alpha * a + beta * c, alpha * b + beta * d)
        m, n = a + c, b + d
        delta = p * n - q * m
        assert delta == beta - alpha
        if delta == 0:
            assert alpha == beta == 1
            return path
        old_sum = alpha + beta
        if delta < 0:
            c, d = m, n
            alpha -= beta
            path += 'L'
        else:
            a, b = m, n
            beta -= alpha
            path += 'R'
        assert alpha + beta < old_sum


def cf_path(p, q):
    word = cf(F(p, q))
    word[-1] -= 1
    return ''.join(('R' if i % 2 == 0 else 'L') * a for i, a in enumerate(word))


def finite_tree(depth, a=0, b=1, c=1, d=0):
    assert b * c - a * d == 1
    p, q = a + c, b + d
    assert gcd(p, q) == 1
    m = F(p, q)
    if depth == 0:
        return [m]
    return (finite_tree(depth - 1, a, b, p, q) + [m]
            + finite_tree(depth - 1, p, q, c, d))


def main():
    start = time.monotonic()
    print('pid', os.getpid(), flush=True)
    endpoints = sorted({F(p, q) for q in range(2, 25) for p in range(1, q)})
    intervals = failures = prefixes = 0
    examples = []
    for lo, hi in combinations(endpoints, 2):
        expected = denominator_oracle(lo, hi)
        tree, _ = interval_tree(lo, hi)
        repaired, prefix = interval_cf(lo, hi, True)
        raw, _ = interval_cf(lo, hi, False)
        assert tree == repaired == expected, (lo, hi, tree, repaired, expected)
        assert lo <= raw <= hi
        fails = raw.denominator != expected.denominator
        assert fails == prefix, (lo, hi, raw, expected, prefix)
        intervals += 1
        failures += fails
        prefixes += prefix
        if fails and len(examples) < 8:
            examples.append(dict(lo=str(lo), hi=str(hi), raw=str(raw), correct=str(expected)))
    print('all rational intervals passed', intervals, 'raw failures', failures, flush=True)

    families = 0
    for k in range(2, 33):
        for t in range(2, 33):
            lo, hi = F(t, k * t + 1), F(1, k)
            assert interval_cf(lo, hi, False)[0] == lo
            assert interval_cf(lo, hi, True)[0] == hi
            assert interval_tree(lo, hi)[0] == hi
            families += 1
    assert interval_cf(F(2, 5), F(1, 2), False)[0] == F(2, 5)

    lo, hi = F(667, 2000), F(669, 2000)
    baseball, path = interval_tree(lo, hi)
    assert baseball == denominator_oracle(lo, hi) == interval_cf(lo, hi, True)[0] == F(96, 287)
    assert lo < baseball < hi
    assert cf(lo) == [0, 2, 1, 666] and cf(hi) == [0, 2, 1, 94, 1, 1, 3]
    assert (667 * 287, 96 * 2000, 669 * 287) == (191429, 192000, 192003)
    assert [p for p in range(1, 287) if lo <= F(p, 287) <= hi] == [96]

    target_count = target_steps = 0
    for p in range(1, 129):
        for q in range(1, 129):
            if gcd(p, q) != 1:
                continue
            path_direct = target_path(p, q)
            assert path_direct == cf_path(p, q)
            target_count += 1
            target_steps += len(path_direct)
    tree = finite_tree(10)
    assert len(tree) == 2047 and all(x < y for x, y in zip(tree, tree[1:]))
    assert finite_tree(2) == [F(1, 3), F(1, 2), F(2, 3), F(1), F(3, 2), F(2), F(3)]
    result = dict(status='passed', pid=os.getpid(), endpoints=len(endpoints),
                  intervals=intervals, raw_rule_failures=failures, prefix_intervals=prefixes,
                  examples=examples, counterexample_family=families,
                  baseball=dict(result=str(baseball), path=path),
                  target_fractions=target_count, coordinate_steps=target_steps,
                  finite_tree_nodes=len(tree), seconds=time.monotonic() - start,
                  scope='Exact finite independent checks supplement the general written proofs; no historical claim tested.')
    (ROOT / 'results/euclid-stern-brocot.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
