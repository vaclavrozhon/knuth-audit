#!/usr/bin/env python3
"""Exact checks for TAOCP 4B 7.2.2--70 (NES paths and moments).

The literal walk enumerator never uses the column transfer formula.  Polynomial
and asymptotic identities are checked separately.  General proofs are in
NES_NOTES.md; finite checks alone are not an asymptotic proof.
"""
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parent
z = sp.Symbol('z')


def transfer(m):
    def entry(i, j):
        h = 2 if i in (0, m - 1) else 3
        if i == j:
            return h
        b = 1 if j in (0, m - 1) else 2
        return h * b * 2 ** (abs(i - j) - 1)
    return sp.Matrix(m, m, entry)


def folded(t):
    m = t.rows
    return sp.Matrix((m + 1) // 2, (m + 1) // 2,
                     lambda i, j: sum(t[i, k] for k in {j, m - 1 - j}))


def literal_walks(m, n):
    target = (m - 1, n - 1)

    def adjacent(p):
        r, c = p
        for rr, cc in ((r - 1, c), (r + 1, c), (r, c + 1)):
            if 0 <= rr < m and 0 <= cc < n:
                yield rr, cc

    def reachable(start, seen):
        todo = [start]
        reached = {start}
        while todo:
            u = todo.pop()
            if u == target:
                return True
            for v in adjacent(u):
                if v not in seen and v not in reached:
                    reached.add(v)
                    todo.append(v)
        return False

    def visit(u, seen, product):
        if u == target:
            return 1, product, Fraction(1, product)
        choices = [v for v in adjacent(u)
                   if v not in seen and reachable(v, seen)]
        count, second, mass = 0, 0, Fraction(0)
        for v in choices:
            a, b, c = visit(v, seen | {v}, product * len(choices))
            count += a
            second += b
            mass += c
        return count, second, mass

    return visit((0, 0), {(0, 0)}, 1)


def moments(t, n):
    v = sp.ones(t.rows, 1)
    out = []
    for _ in range(n):
        out.append(int(v[0]))
        v = t * v
    return out


def polynomials(limit):
    p = {2: sp.Integer(1), 3: 1 + z, 4: 1 + 3*z,
         5: 1 + 10*z + 9*z*z}
    q = {2: 1 - 4*z, 3: 1 - 9*z - 6*z*z,
         4: 1 - 19*z - 18*z*z, 5: 1 - 36*z - 99*z*z - 54*z**3}
    for m in range(6, limit + 1):
        p[m] = sp.expand((5 + 9*z)*p[m-2] - 4*p[m-4])
        q[m] = sp.expand((5 + 9*z)*q[m-2] - 4*q[m-4])
    return p, q


def exact_horner(coeff, x):
    v = Fraction(0)
    for a in coeff:
        v = v*x + a
    return v


def main():
    out = {'status': 'RUNNING', 'literal': [], 'polynomials': [], 'roots': []}
    p, q = polynomials(100)
    for m in range(2, 7):
        t = transfer(m)
        values = moments(t, 6)
        for n in range(1, 6):
            count, second, mass = literal_walks(m, n)
            assert count == m**(n-1)
            assert second == values[n-1]
            assert mass == 1
            out['literal'].append({'m': m, 'n': n, 'count': count,
                                   'second_moment': second})
    assert moments(transfer(3), 5) == [1, 10, 96, 924, 8892]

    for m in range(2, 23):
        t = transfer(m)
        c = folded(t)
        a = sp.eye(c.rows) - z*c
        # charpoly avoids expensive generic rational Gaussian elimination.
        coeff = c.charpoly().all_coeffs()
        det = sp.Add(*(v*z**i for i, v in enumerate(coeff)))
        assert sp.expand(det - q[m]) == 0
        # Multiplying the rational series by its exact characteristic
        # denominator determines all numerator coefficients (degree < r).
        seq = moments(c, c.rows + 3)
        qc = [q[m].coeff(z, i) for i in range(c.rows + 1)]
        pc = [sum(qc[j]*seq[i-j] for j in range(min(i, c.rows)+1))
              for i in range(len(seq))]
        assert sp.expand(sum(v*z**i for i, v in enumerate(pc)) - p[m]) == 0
        if m <= 10:
            ac = a.copy()
            ac[:, 0] = sp.ones(c.rows, 1)
            assert sp.expand(ac.det() - p[m]) == 0
        if m >= 3:
            b = c.inv()
            assert all(b[i,j] == 0 for i in range(b.rows)
                       for j in range(b.cols) if abs(i-j) > 1)
            assert b[0,0] == -sp.Rational(1,2)
            # Inertia proof: L=K+diag(1,0,...,0,1) has one positive
            # and m-1 negative LDL pivots. The matrices are congruent.
            ell = sp.Matrix(m,m,lambda i,j: 2**abs(i-j)
                            + int(i == j and i in (0,m-1)))
            expected = [2, -1] + [-3]*(m-3) + [-2]
            pivots = []
            prev = 1
            for j in range(1,m+1):
                d = ell[:j,:j].det()
                pivots.append(d/prev)
                prev = d
            assert pivots == expected, (m,pivots)
        assert sp.Poly(q[m],z).count_roots(0,sp.oo) == 1
        assert sp.Poly(q[m],z).count_roots(-sp.oo,0) == sp.degree(q[m])-1
        out['polynomials'].append({'m':m, 'P':str(p[m]), 'Q':str(q[m])})

    # Verify the closed denominator representation symbolically at its four
    # initial values. It satisfies the same recurrence for all subsequent m.
    s = sp.Symbol('s', nonzero=True)
    zz = -(2*s-1)*(2/s-1)/9
    pp = lambda a: 1+2*zz-2*a*(1-zz)
    for k in range(1,5):
        r = k//2
        if k % 2 == 0:
            closed = -sp.Rational(2)**r/3*(pp(1/s)*s**r+pp(s)*s**(-r))
        else:
            closed = -sp.Rational(2)**r/(1+s)*(pp(1/s)*s**(r+1)+pp(s)*s**(-r))
        assert sp.factor(closed-q[k+1].subs(z,zz)) == 0

    d, e, m, a = sp.symbols('d e m a')
    ss = sp.Rational(1,2)-d
    rr = -(2*ss-1)*(2*ss**2-11*ss-4)/((2-ss)*(2-11*ss-4*ss**2))
    xx = -(2*ss-1)*(2/ss-1)/9
    rs = sp.series(rr,d,0,3).removeO()
    xs = sp.series(xx,d,0,3).removeO()
    assert rs == 8*d/3+40*d**2/9
    assert xs == 2*d/3+16*d**2/9
    delta = sp.Rational(3,2)*e+a*e**2
    residue = sp.series(rs.subs(d,delta)
                        -4*e*(1-2*(m-2)*delta),e,0,3).removeO().expand()
    aa = sp.solve(residue.coeff(e,2),a)[0]
    assert aa == sp.Rational(21,4)-9*m/2
    pole = sp.series(xs.subs(d,delta.subs(a,aa)),e,0,3).removeO().expand()
    assert sp.expand(pole - e-(sp.Rational(15,2)-3*m)*e**2) == 0
    out['symbolic_asymptotic'] = {'delta_e2':str(aa), 'pole':str(pole),
        'rho':'2**m + 3*m - 15/2 + O(m**2 / 2**m)'}

    mp.mp.dps = 160
    scale = 10**20
    for m in [2,3,4,5,6,8,10,15,20,30,40,60,80,100]:
        coeff = [int(v) for v in sp.Poly(q[m],z).all_coeffs()]
        # Newton on lambda/2**m keeps the variable close to 1 even at m=100.
        fn = lambda u: mp.polyval(coeff,1/(u*mp.mpf(2)**m))
        u = mp.findroot(fn,(mp.mpf('0.9'),mp.mpf('1.1')),
                        tol=mp.mpf('1e-140'),maxsteps=100)
        lam = u*mp.mpf(2)**m
        lo = Fraction(int(mp.floor(lam*scale))-1,scale)
        hi = lo+Fraction(3,scale)
        assert exact_horner(coeff,1/lo) < 0
        assert exact_horner(coeff,1/hi) > 0
        out['roots'].append({'m':m,'rho':mp.nstr(lam,120),
            'rho_minus_2m':mp.nstr(lam-2**m,70),
            'remainder':mp.nstr(lam-2**m-3*m+mp.mpf('7.5'),70),
            'certified_interval':[str(lo),str(hi)]})

    out['status'] = 'PASS'
    target = ROOT/'results/estimation/nes-verified.json'
    target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('PASS',len(out['literal']),'literal grids;',len(out['polynomials']),
          'exact polynomial pairs;',len(out['roots']),'certified roots',flush=True)
    for item in out['roots']:
        print(item['m'],item['rho_minus_2m'],flush=True)


if __name__ == '__main__':
    main()
