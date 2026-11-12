"""Unit-cost arithmetic programs for TAOCP2 4.5.4-40.

Only +,-,*,floor division and equality are used by the modeled algorithms.
Python factorial, comb, gcd, comparisons and bit lengths are independent
validation/instrumentation, not unit-cost primitives of those algorithms.
"""
from pathlib import Path
from math import factorial, comb, gcd, prod, isqrt
from collections import Counter
import json
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/shamir-factor.json'


class Machine:
    def __init__(self): self.ops = Counter(); self.peak_bits = 0
    def keep(self, x): self.peak_bits = max(self.peak_bits, abs(x).bit_length()); return x
    def add(self, x, y): self.ops['add'] += 1; return self.keep(x+y)
    def sub(self, x, y): self.ops['subtract'] += 1; return self.keep(x-y)
    def mul(self, x, y): self.ops['multiply'] += 1; return self.keep(x*y)
    def div(self, x, y):
        assert y != 0
        self.ops['floor_divide'] += 1; return self.keep(x//y)
    def eq(self, x, y): self.ops['equality'] += 1; return x == y
    def positive(self, x):
        if self.eq(x, 1): return True
        return not self.eq(self.div(x, self.sub(x, 1)), 0)
    def mod(self, x, y): return self.sub(x, self.mul(y, self.div(x, y)))
    def gcd(self, x, y):
        while not self.eq(y, 0): x, y = y, self.mod(x, y)
        return x
    def setup(self, n, initial):
        z, k, A = n, 1, initial
        while not self.eq(z, 1):
            z = self.div(z, 2); k = self.mul(k, 2); A = self.mul(A, A)
        return k, A


def fast_factorial(n):
    M = Machine(); k, A = M.setup(n, 4); Ap = M.add(A, 1)
    m, t, u, v = 1, A, Ap, 1; stages = 0
    while not M.eq(k, 1):
        k = M.div(k, 2); m = M.mul(m, 2); u = M.mul(u, u)
        coefficient = M.mod(M.div(u, t), A)
        assert coefficient == comb(m, m//2)
        v = M.mul(coefficient, M.mul(v, v)); t = M.mul(t, t)
        bit = M.mod(M.div(n, k), 2)
        if not M.eq(bit, 0):
            m = M.add(m, 1); t = M.mul(A, t); u = M.mul(Ap, u); v = M.mul(v, m)
        assert v == factorial(m) and t == A**m and u == Ap**m
        stages += 1
    assert m == n and v == factorial(n)
    return dict(n=n, value=v, stages=stages, operations=dict(M.ops), peak_bits=M.peak_bits)


def threshold(n):
    product = 1
    for j in range(1, n+1):
        product = product*j % n
        if product == 0: return j
    raise AssertionError(n)


def factor_one(n):
    M = Machine(); _, A = M.setup(n, 16); Ap = M.add(A, 1)
    b, T, U, f = 1, A, Ap, 1; doubled = 0
    while True:
        UU = M.mul(U, U); coefficient = M.mod(M.div(UU, T), A)
        assert coefficient == comb(2*b, b)
        ff = M.mul(coefficient, M.mul(f, f)); doubled += 1
        if M.eq(M.mod(ff, n), 0): break
        b = M.mul(b, 2); T = M.mul(T, T); U, f = UU, ff
        assert f == factorial(b)
    assert factorial(b) % n != 0 and factorial(2*b) % n == 0
    g = M.gcd(n, f)
    data = dict(n=n, lower_power=b, doubling_steps=doubled)
    if not M.eq(g, 1):
        assert 1 < g < n and n % g == 0
        data.update(branch='gcd', factor=g)
    else:
        s = sp = 1; t = tp = A; u = up = M.mul(Ap, Ap); ascent = 0
        while not M.positive(M.sub(sp, b)):
            s, sp = sp, M.add(s, sp)
            t, tp = tp, M.mul(t, tp); u, up = up, M.mul(u, up); ascent += 1
        # s<=b<sp and m=b-s.  The known upper endpoint is b.
        m = M.sub(b, s); v = M.div(T, t); w = M.div(M.mul(U, U), u)
        target = (threshold(n)+1)//2; states = []
        assert 0 <= m < target <= b
        def check_state():
            assert t == A**s and tp == A**sp
            assert u == Ap**(2*s) and up == Ap**(2*sp)
            assert v == A**m and w == Ap**(2*m)
            assert m < target <= min(m+s, b)
        check_state()
        while not M.eq(s, 1):
            s, sp = M.sub(sp, s), s
            t, tp = M.div(tp, t), t; u, up = M.div(up, u), u
            probe = M.add(m, s)
            if not M.positive(M.sub(b, probe)):
                zero = True; coefficient = None
            else:
                coefficient = M.mod(M.div(M.mul(w, u), M.mul(v, t)), A)
                assert coefficient == comb(2*probe, probe)
                zero = M.eq(M.mod(coefficient, n), 0)
            if not zero:
                m = probe; w = M.mul(w, u); v = M.mul(v, t)
            check_state(); states.append(dict(s=s, sp=sp, m=m, probe=probe, zero=zero))
        assert m+1 == target
        g = M.gcd(M.add(M.mul(2, m), 1), n)
        if M.eq(g, 1): g = M.gcd(M.add(M.mul(2, m), 2), n)
        data.update(branch='fibonacci', factor=g, threshold=threshold(n),
                    ascent=ascent, descent_states=states, final_m=m)
    prime = all(n % d for d in range(2, isqrt(n)+1))
    assert (g == n) if prime else (1 < g < n and n % g == 0)
    assert sum(M.ops.values()) <= 500*n.bit_length()
    data.update(operations=dict(M.ops), peak_bits=M.peak_bits)
    return data


def identity_checks():
    robinson = []
    for n in range(2, 41):
        B = (2*n)**(n+1)+1; numerator = B**n; denominator = comb(B, n)
        assert numerator//denominator == factorial(n)
        assert factorial(n)*denominator <= numerator < (factorial(n)+1)*denominator
        robinson.append(dict(n=n, B=B, numerator=numerator, denominator=denominator))
    M = Machine()
    for x in range(-200, 201): assert M.positive(x) == (x > 0)
    n = 35; A = 1 << 128; s, sp, m = 5, 8, 8
    t, tp = A**s, A**sp; u, up = (A+1)**(2*s), (A+1)**(2*sp)
    v, w = A**m, (A+1)**(2*m)
    assert factorial(4) % n != 0 and factorial(8) % n == 0 and gcd(factorial(4), n) == 1
    before = [comb(2*m, m) % n, comb(2*(m+s), m+s) % n]
    assert before == [25, 0] and A > 2**(2*(m+s))
    s, sp = sp-s, s; t, tp = tp//t, t; u, up = up//u, u
    coefficient = (w*u//(v*t)) % A
    assert coefficient == comb(22, 11) and coefficient % n == 7
    if coefficient % n: m += s; w *= u; v *= t
    after = [comb(2*m, m) % n, comb(2*(m+s), m+s) % n]
    assert (s, sp, m) == (3, 5, 11) and after == [7, 20]
    return dict(robinson=robinson, sign_tests=401,
                printed_invariant_failure=dict(n=n, A_bits=A.bit_length(),
                    before=dict(s=5, sp=8, m=8, residues=before),
                    probe_coefficient=coefficient, after=dict(s=s, sp=sp, m=m, residues=after),
                    after_upper_coefficient=comb(28, 14)))


def save(data):
    tmp = OUT.with_suffix('.tmp'); tmp.write_text(json.dumps(data, indent=2)+'\n'); tmp.replace(OUT)


def main():
    result = json.loads(OUT.read_text()) if OUT.exists() else dict(status='running', blocks={})
    jobs = [('identities', identity_checks),
            ('factorials', lambda: [fast_factorial(n) for n in range(2, 161)]),
            ('factors', lambda: [factor_one(n) for n in list(range(2, 161))+
                [181, 191, 193, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 289, 323, 437, 527]])]
    for name, fn in jobs:
        if name in result['blocks']: continue
        start = time.perf_counter(); data = fn()
        result['blocks'][name] = dict(data=data, seconds=time.perf_counter()-start); save(result)
        print(name, 'passed', result['blocks'][name]['seconds'], 's', flush=True)
    result['status'] = 'passed'; save(result)


if __name__ == '__main__': main()
