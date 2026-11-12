"""Exact checks of the half-gcd construction and compact Sturm/resultant data.

Schoolbook multiplication here checks algebraic correctness, not FFT timing.
SymPy division and Sylvester determinants are separate reference calculations.
Run blocks separately; successful results are checkpointed and not repeated.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import datetime
import json
import os
import random
import time

import sympy as sp

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / 'results/fast-sturm.json'
X = sp.Symbol('x')
STATS = Counter()


class Ring:
    def __init__(self, prime=None):
        self.p = prime
        self.zero = ()
        self.one = self.poly([1])
        self.identity = (self.one, (), (), self.one)

    def scalar(self, x):
        return x % self.p if self.p else Fraction(x)

    def poly(self, a):
        a = [self.scalar(x) for x in a]
        while a and not a[-1]:
            a.pop()
        return tuple(a)

    def add(self, a, b):
        return self.poly([(a[i] if i < len(a) else 0)
                          + (b[i] if i < len(b) else 0)
                          for i in range(max(len(a), len(b)))])

    def neg(self, a):
        return self.poly([-x for x in a])

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if not a or not b:
            return ()
        c = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                c[i+j] += x*y
        return self.poly(c)

    def ratio(self, a, b):
        assert b
        return a * pow(b, -1, self.p) % self.p if self.p else a / b

    def div(self, a, b):
        assert b
        r = list(a)
        q = [0] * max(0, len(a)-len(b)+1)
        while r and len(r) >= len(b):
            j = len(r)-len(b)
            t = self.ratio(r[-1], b[-1])
            q[j] = t
            for k, c in enumerate(b):
                r[j+k] = self.scalar(r[j+k] - t*c)
            while r and not r[-1]:
                r.pop()
        return self.poly(q), tuple(r)

    def matmul(self, a, b):
        return tuple(self.add(self.mul(a[2*i], b[j]),
                              self.mul(a[2*i+1], b[2+j]))
                     for i in range(2) for j in range(2))

    def apply(self, m, a, b):
        return (self.add(self.mul(m[0], a), self.mul(m[1], b)),
                self.add(self.mul(m[2], a), self.mul(m[3], b)))

    def invapply(self, m, count, a, b):
        # det(M) = (-1)^count, so inverse is signed adjugate.
        z = (m[3], self.neg(m[1]), self.neg(m[2]), m[0])
        if count % 2:
            z = tuple(self.neg(t) for t in z)
        return self.apply(z, a, b)

    def quotient_matrix(self, q):
        return q, self.one, self.one, ()

    def value(self, p, x):
        v = self.scalar(0)
        for c in reversed(p):
            v = self.scalar(v*x+c)
        return v

    def sympy(self, a):
        domain = sp.GF(self.p) if self.p else sp.QQ
        return sp.Poly.from_list(list(reversed(a)) or [0], X, domain=domain)

    def from_sympy(self, a):
        return self.poly([int(c) if self.p else Fraction(c)
                          for c in reversed(a.all_coeffs())])


def deg(a):
    # -1 suffices for comparisons against nonnegative thresholds in this code.
    return len(a)-1


def half(ring, a, b, depth=0):
    """Return M, quotients, A, B with (a,b)=M(A,B), deg A>=ceil(d/2)>deg B."""
    d = deg(a)
    assert d > deg(b)
    m = (d+1)//2
    STATS['half_calls'] += 1
    STATS['max_depth'] = max(STATS['max_depth'], depth)

    def finish(matrix, qs, A, B):
        assert deg(A) >= m > deg(B), (d, m, deg(A), deg(B))
        assert ring.apply(matrix, A, B) == (a, b)
        assert all(deg(q) >= 1 for q in qs)
        assert max(map(deg, matrix)) <= d//2
        STATS['half_certificates'] += 1
        return matrix, qs, A, B

    if deg(b) < m:
        return finish(ring.identity, [], a, b)
    R, left, _, _ = half(ring, a[m:], b[m:], depth+1)
    A, B = ring.invapply(R, len(left), a, b)
    assert deg(A) >= m + ((d-m)+1)//2
    assert deg(B) < m + ((d-m)+1)//2
    if deg(B) < m:
        return finish(R, left, A, B)
    q, D = ring.div(A, B)
    k = 2*m-deg(B)
    assert 0 <= k <= deg(B)
    assert deg(B[k:]) < d//2
    S, right, _, _ = half(ring, B[k:], D[k:], depth+1)
    C, E = ring.invapply(S, len(right), B, D)
    M = ring.matmul(ring.matmul(R, ring.quotient_matrix(q)), S)
    return finish(M, left+[q]+right, C, E)


def compact(ring, a, b):
    """Complete quotient list and last nonzero remainder, including final division."""
    assert a and deg(a) >= deg(b)
    original = a, b
    qs = []
    while b:
        if deg(a) > deg(b):
            _, prefix, a, b = half(ring, a, b)
            qs.extend(prefix)
        if not b:
            break
        q, c = ring.div(a, b)
        qs.append(q)
        a, b = b, c
    g = a
    reconstructed = g, ()
    for q in reversed(qs):
        reconstructed = (ring.add(ring.mul(q, reconstructed[0]), reconstructed[1]),
                         reconstructed[0])
    assert reconstructed == original
    assert sum(len(q) for q in qs)+len(g) <= 2*deg(original[0])+3
    STATS['compact_certificates'] += 1
    STATS['abnormal_quotients'] += sum(deg(q) > 1 for q in qs)
    return qs, g


def reference(ring, a, b):
    a, b = ring.sympy(a), ring.sympy(b)
    out = []
    while not b.is_zero:
        q, r = sp.div(a, b)
        out.append(ring.from_sympy(q))
        a, b = b, r
    return out, ring.from_sympy(a)


def metadata(ring, a, qs):
    ds, ls = [deg(a)], [a[-1]]
    for q in qs:
        ds.append(ds[-1]-deg(q))
        ls.append(ring.ratio(ls[-1], q[-1]))
    return ds, ls


def resultant(ring, a, b, qs, g):
    if not b:
        return ring.scalar(1 if deg(a) == 0 else 0)
    if deg(g) > 0:
        return ring.scalar(0)
    ds, ls = metadata(ring, a, qs)
    value = ring.scalar(ls[-1] ** ds[-2])
    for i in range(1, len(ds)-1):
        factor = (-1)**(ds[i-1]*ds[i]) * ls[i]**(ds[i-1]-ds[i+1])
        value = ring.scalar(value*factor)
    assert sum(ds[i-1]-ds[i+1] for i in range(1, len(ds)-1))+ds[-2] == ds[0]+ds[1]
    return value


def sylvester(ring, a, b):
    m, n = deg(a), deg(b)
    if m == n == 0:
        return ring.scalar(1)
    rows = []
    for i in range(n):
        rows.append([0]*i+list(reversed(a))+[0]*(n-1-i))
    for i in range(m):
        rows.append([0]*i+list(reversed(b))+[0]*(m-1-i))
    determinant = sp.Matrix(rows).det(method='bareiss')
    return ring.scalar(int(determinant) if ring.p else Fraction(determinant))


def check_pair(ring, a, b, determinant=False):
    qs, g = compact(ring, a, b)
    assert (qs, g) == reference(ring, a, b)
    ds, ls = metadata(ring, a, qs)
    assert ds[-1] == deg(g) and ls[-1] == g[-1]
    if determinant:
        assert b
        assert resultant(ring, a, b, qs, g) == sylvester(ring, a, b)
        STATS['sylvester_determinants'] += 1
    STATS['reference_pairs'] += 1


def modular():
    rng = random.Random(2026110401)
    for p, maximum in [(2, 4), (3, 3)]:
        r = Ring(p)
        polys = [[r.poly(list(c)+[1]) for c in product(range(p), repeat=d)]
                 for d in range(maximum+1)]
        for d in range(1, maximum+1):
            for e in range(d):
                for a in polys[d]:
                    for b in polys[e]:
                        check_pair(r, a, b, determinant=(d <= 3 and e <= 2))
    for p in [2, 3, 5, 101]:
        r = Ring(p)
        for n in [5, 6, 7, 8, 9, 15, 16, 17, 31, 32, 33, 64]:
            for _ in range(2):
                e = rng.randrange(n)
                a = r.poly([rng.randrange(p) for _ in range(n)]+[rng.randrange(1,p)])
                b = r.poly([rng.randrange(p) for _ in range(e)]+[rng.randrange(1,p)])
                check_pair(r, a, b)
        # Reverse construction forces arbitrary degree drops and nonconstant gcds.
        for _ in range(30):
            gd = rng.randrange(6)
            g = r.poly([rng.randrange(p) for _ in range(gd)]+[1])
            a, b = g, ()
            for _ in range(rng.randrange(1,7)):
                qd = rng.randrange(1,10)
                q = r.poly([rng.randrange(p) for _ in range(qd)]+[1])
                a, b = r.add(r.mul(q, a), b), a
            check_pair(r, a, b)


def rational():
    rng = random.Random(2026110402)
    r = Ring()
    for n in range(1, 9):
        for _ in range(3):
            e = rng.randrange(n+1)
            a = r.poly([rng.randint(-3,3) for _ in range(n)]+[rng.choice([-2,-1,1,2])])
            b = r.poly([rng.randint(-3,3) for _ in range(e)]+[rng.choice([-2,-1,1,2])])
            check_pair(r, a, b, determinant=True)
    for a, b in [([1], []), ([1,2], []), ([2], [3]),
                 ([0,0,0,1], [0,1]), ([0,0,1], [0,0,1]),
                 ([1,0,0,0,0,1], [1,0,1])]:
        check_pair(r, r.poly(a), r.poly(b), determinant=bool(b))


def variation(values):
    signs = [1 if x > 0 else -1 for x in values if x]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def sturm_values(r, qs, g, x):
    # Reconstruct scalar values backwards, then apply 1,1,-1,-1,... signs.
    values = [0, r.value(g, x)]
    for q in reversed(qs):
        values.append(r.value(q, x)*values[-1]+values[-2])
    ordinary = list(reversed(values[1:]))
    return [v * (1 if i % 4 < 2 else -1) for i, v in enumerate(ordinary)]


def sturm():
    r = Ring()
    rng = random.Random(2026110403)
    for case in range(70):
        roots = sorted(rng.sample(range(-4,5), rng.randrange(1,6)))
        a = r.one
        for root in roots:
            for _ in range(1 + (case % 3 == 0 and rng.randrange(2))):
                a = r.mul(a, r.poly([-root,1]))
        if case % 2:
            a = r.mul(a, r.poly([1+case,0,1]))
        b = r.poly([i*a[i] for i in range(1,len(a))])
        qs, g = compact(r, a, b)
        assert (qs,g) == reference(r,a,b)
        ds, ls = metadata(r,a,qs)
        # Independently construct signed Euclidean remainders with SymPy.
        sa, sb = r.sympy(a), r.sympy(b)
        serial = [sa,sb]
        while True:
            _, rem = sp.div(serial[-2], serial[-1])
            if rem.is_zero:
                break
            serial.append(-rem)
        assert [f.degree() for f in serial] == ds
        assert [Fraction(f.LC()) for f in serial] == [c*(1 if i%4<2 else -1) for i,c in enumerate(ls)]
        points = [Fraction(x,2) for x in range(-11,12) if Fraction(x,2) not in roots]
        counts = []
        for x in points:
            vals = sturm_values(r,qs,g,x)
            assert vals == [Fraction(f.eval(sp.Rational(x.numerator,x.denominator))) for f in serial]
            counts.append(variation(vals))
            STATS['endpoint_value_checks'] += 1
        for i,x in enumerate(points):
            for j in range(i+1,len(points)):
                y=points[j]
                assert counts[i]-counts[j] == sum(x<t<y for t in roots)
                STATS['root_intervals'] += 1
        plus = [c*(1 if i%4<2 else -1) for i,c in enumerate(ls)]
        minus = [c*(-1)**d for c,d in zip(plus,ds)]
        assert variation(minus)-variation(plus) == len(roots)
        STATS['sturm_polynomials'] += 1


def gaps():
    """Target signed chains with large degree gaps, absent in the random Sturm set."""
    r = Ring()
    for n in list(range(2,17))+[31,32,63,64]:
        minus = r.poly([-1]+[0]*(n-1)+[1])
        plus = r.poly([1]+[0]*(n-1)+[1])
        minus_x = r.poly([0,-1]+[0]*(n-2)+[1])
        unit_roots = [-1,1] if n%2 == 0 else [1]
        families = [(minus,unit_roots), (plus,[] if n%2 == 0 else [-1]),
                    (minus_x,[-1,0,1] if n%2 else [0,1]),
                    (r.mul(minus,minus),unit_roots)]
        for a, roots in families:
            b=r.poly([i*a[i] for i in range(1,len(a))])
            qs,g=compact(r,a,b)
            assert (qs,g)==reference(r,a,b)
            ds,ls=metadata(r,a,qs)
            points=[Fraction(j,2) for j in range(-7,8) if Fraction(j,2) not in roots]
            counts=[variation(sturm_values(r,qs,g,x)) for x in points]
            for i,x in enumerate(points):
                for j in range(i+1,len(points)):
                    assert counts[i]-counts[j]==sum(x<t<points[j] for t in roots)
                    STATS['root_intervals']+=1
            leading=[c*(1 if i%4<2 else -1) for i,c in enumerate(ls)]
            assert variation([c*(-1)**d for c,d in zip(leading,ds)])-variation(leading)==len(roots)
            STATS['sturm_polynomials']+=1
    assert STATS['abnormal_quotients']>0


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--block', choices=['modular','rational','sturm','gaps'], required=True)
    args=parser.parse_args()
    data=json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{},'scope':'Exact algebraic checks; schoolbook implementation is not a timing validation of FFT bounds.'}
    assert args.block not in data['blocks'], 'Successful block already exists; do not repeat.'
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    print(json.dumps({'block':args.block,'pid':os.getpid(),'started':started}),flush=True)
    t=time.monotonic()
    globals()[args.block]()
    result={'status':'passed','started_utc':started,'elapsed_seconds':time.monotonic()-t,'pid':os.getpid(),'counts':dict(STATS)}
    data['blocks'][args.block]=result
    RESULT.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(result),flush=True)


if __name__=='__main__':
    main()
