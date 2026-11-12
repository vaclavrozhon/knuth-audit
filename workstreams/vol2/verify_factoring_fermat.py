#!/usr/bin/env python3
"""Exact checks for TAOCP2 4.5.4C/D and exercises5/7."""
from pathlib import Path
from math import isqrt, gcd, lcm, prod
import argparse
import json
import os
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/factoring-fermat.json'


def largest_small_factor(n):
    for d in range(isqrt(n), 0, -1):
        if n % d == 0:
            return d
    raise AssertionError(n)


def algorithm_c(n):
    a0 = isqrt(n)
    a, b, r = 2*a0+1, 1, a0*a0-n
    increments_a = increments_b = 0
    while r:
        assert r < 0
        r += a
        a += 2
        increments_a += 1
        assert r > 0
        while True:
            r -= b
            b += 2
            increments_b += 1
            assert r == ((a-1)//2)**2-((b-1)//2)**2-n
            assert abs(r) < a and b < a
            if r <= 0:
                break
    u, v = (a-b)//2, (a+b-2)//2
    assert increments_a+increments_b == v-a0
    return u, v, increments_a, increments_b


def c_check():
    total_a = total_b = 0
    for n in range(1, 8192, 2):
        u, v, a, b = algorithm_c(n)
        assert u == largest_small_factor(n) and u*v == n
        total_a += a
        total_b += b
    return dict(inputs=4096, x_increments=total_a, y_increments=total_b,
                example377=algorithm_c(377))


def sieve_table(n, m):
    squares = {y*y % m for y in range(m)}
    return [int((x*x-n) % m in squares) for x in range(m)]


def algorithm_d(n, moduli):
    ts = [sieve_table(n, m) for m in moduli]
    x = isqrt(n)
    x += x*x < n
    ks = [(-x) % m for m in moduli]
    examined = []
    while True:
        assert all(k == (-x) % m for k, m in zip(ks, moduli))
        if all(t[k] for t, k in zip(ts, ks)):
            examined.append(x)
            y = isqrt(x*x-n)
            if y*y == x*x-n:
                return x-y, x+y, examined
        x += 1
        ks = [(k-1) % m for k, m in zip(ks, moduli)]


def d_check():
    checks = 0
    for n in range(1, 4096, 2):
        mods = [m for m in (3, 5, 7, 8, 11) if gcd(m, n) == 1]
        u, v, _ = algorithm_d(n, mods)
        assert u == largest_small_factor(n) and u*v == n
        checks += 1
    examples = {}
    for n in (11111, 8616460799):
        u, v, examined = algorithm_d(n, (3, 5, 7, 8, 11))
        examples[str(n)] = dict(factors=[u, v], examined=examined)
    assert examples['11111'] == dict(factors=[41, 271], examined=[144, 156])
    assert examples['8616460799'] == dict(factors=[89681, 96079], examined=[92880])
    assert 144**2-11111 == 9625
    assert 156**2-11111 == 115**2 == 13225
    assert 92880**2-8616460799 == 3199**2 == 10233601
    assert (8616460799-11111) % (3*7*8*11) == 0
    return dict(inputs=checks, examples=examples)


def residue_check():
    n = 8616460799
    printed = {3:[0], 5:[0, 2, 3], 7:[2, 3, 4, 5],
               8:[0, 4], 11:[1, 2, 4, 7, 9, 10],
               25:[0, 5, 7, 10, 15, 18, 20]}
    for m, xs in printed.items():
        assert [x for x, bit in enumerate(sieve_table(n, m)) if bit] == xs
    sq100 = {x*x % 100 for x in range(100)}
    pattern = {0, 25}
    pattern |= {10*e+u for e in range(0, 10, 2) for u in [1, 4, 9]}
    pattern |= {10*o+6 for o in range(1, 10, 2)}
    assert sq100 == pattern
    powers = 0
    for p in (3, 5, 7, 11, 13, 17, 19):
        for n in range(1, p*p):
            if n % p == 0:
                continue
            t, tt = sieve_table(n, p), sieve_table(n, p*p)
            qr = any(x*x % p == n % p for x in range(p))
            want = (p*p-3*p+4)//2 if qr else p*(p-1)//2
            assert sum(tt) == want
            assert sum(tt) < p*sum(t) if qr else sum(tt) == p*sum(t)
            powers += 1
    assert all(sieve_table(9, 3)) and all(sieve_table(9, 9))
    for n in range(1, 73, 2):
        if n % 3 == 2:
            assert [x for x in range(3) if sieve_table(n, 3)[x]] == [0]
        if n % 9 in (1, 4, 7):
            a = {1:1, 4:2, 7:4}[n % 9]
            assert [x for x in range(9) if sieve_table(n, 9)[x]] == sorted([a, 9-a])
        if n % 4 == 1:
            assert [x for x in range(4) if sieve_table(n, 4)[x]] == [1, 3]
        else:
            a = 2 if n % 8 == 3 else 0
            assert {x % 4 for x in range(8) if sieve_table(n, 8)[x]} == {a}
    return dict(printed_allowed_residues=printed, square_endings=sorted(sq100),
                prime_power_models=powers, coprimality_qualification='N9,p3 gives no extra information')


def pairing_check():
    checks = 0
    for r in (2, 3, 4):
        ms = [3, 5, 7, 11][:r]
        paired = [ms[k]*ms[r-1-k] for k in range(r//2)]
        if r % 2:
            paired.append(ms[r//2])
        for n in range(1, 42, 2):
            if gcd(n, prod(ms)) != 1:
                continue
            ts = [sieve_table(n, m) for m in ms]
            ps = [sieve_table(n, m) for m in paired]
            for x in range(prod(ms)):
                assert all(t[x % m] for t, m in zip(ts, ms)) == all(t[x % m] for t, m in zip(ps, paired))
                checks += 1
    n, x = 31, 7
    assert sieve_table(n, 9)[x % 9] == 1
    assert sieve_table(n, 3)[x % 3] == 1
    assert sieve_table(n, 5)[x % 5] == 0
    assert sieve_table(n, 15)[x % 15] == 0
    return dict(paired_predicates=checks,
                printed_index_counterexample={'r':2,'m':[3,5],'N':n,'x':x,'printed_modulus':9,'correct_modulus':15})


def word_checks():
    compact = shifted = wraps = 0
    for w in (2, 5, 8, 30, 31):
        mask = (1 << w)-1
        for m in range(1, 68):
            W = lcm(m, w)//w
            for n in (1, 5, 31):
                t = sieve_table(n, m)
                # Guard bits make every length-w circular window contiguous.
                bits = [t[j % m] for j in range(m+w-1)]
                storage = [sum(bit << b for b, bit in enumerate(bits[i:i+w]))
                           for i in range(0, len(bits), w)]
                storage.append(0)  # harmless second load for aligned final word
                for x in range(m):
                    q, s = divmod(x, w)
                    got = ((storage[q] >> s) | (storage[q+1] << (w-s))) & mask
                    want = sum(t[(x+b) % m] << b for b in range(w))
                    assert got == want
                    shifted += 1
                for x0 in sorted({0, 1, m-1}):
                    a = -x0
                    words = [sum(t[(a+w*q-b) % m] << b for b in range(w))
                             for q in range(W)]
                    q, x = 0, x0
                    for _ in range(2*W+3):
                        got = words[q]
                        want = sum(t[(x+b) % m] << b for b in range(w))
                        assert got == want
                        q -= 1
                        if q < 0:
                            q += W
                            wraps += 1
                        x += w
                        compact += 1
    w, m = 30, 7
    W = lcm(w, m)//w
    wrong = -1+lcm(w, m)
    right = -1+W
    assert W == 7 and wrong == 209 and right == 6 and wrong >= W
    return dict(compact_blocks=compact, shifted_windows=shifted, corrected_wraps=wraps,
                printed_wrap_counterexample={'word_bits':w,'modulus':m,'stored_words':W,
                                              'printed_next_index':wrong,'correct_next_index':right})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--resume', action='store_true')
    args = parser.parse_args()
    result = json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'checkpoints':{}}
    result['pid'] = os.getpid()
    start = time.monotonic()
    for name, fn in [('C', c_check), ('D', d_check), ('residues', residue_check),
                     ('pairing', pairing_check), ('words', word_checks)]:
        if name in result['checkpoints']:
            print('reuse', name, flush=True)
            continue
        t = time.monotonic()
        result['checkpoints'][name] = {'result':fn(), 'seconds':time.monotonic()-t}
        OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
        print('passed', name, flush=True)
    result['status'] = 'passed'
    result['elapsed_this_run'] = time.monotonic()-start
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print('ALL PASSED', result['pid'], result['elapsed_this_run'], flush=True)
