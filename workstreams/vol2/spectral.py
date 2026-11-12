"""Exact implementations used by the TAOCP2 spectral audit.

spectral_s follows the printed S1--S10, with half-up rational rounding.
shortest_direct independently enumerates a Euclidean ball in the ORIGINAL
integer coordinates, eliminating u_1 by its congruence. It is intended for
small moduli; it does not reuse the book's basis reduction or its box search.
"""
from math import gcd, isqrt, prod


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def round_ratio(n, d):
    assert d > 0
    return (2*n+d)//(2*d)


def validate_basis(U, V, a, m):
    t = len(U)
    for i in range(t):
        assert sum(U[i][j]*pow(a, j, m) for j in range(t)) % m == 0
        for j in range(t):
            assert dot(U[i], V[j]) == m*(i == j), (U, V, i, j)


def spectral_s(a, m, T, trace=False, check=True, search_limit=10_000_000):
    assert 0 < a < m and gcd(a, m) == 1 and T >= 2
    t, h, hp, p, pp, r, s = 2, a, m, 1, 0, a, 1+a*a
    history = []
    euclidean = 0
    while True:  # S2
        assert h > 0
        assert (h-a*p) % m == (hp-a*pp) % m == 0
        assert abs(h*pp-hp*p) == m
        assert (hp+h)**2+(pp+p)**2 >= h*h+p*p
        q = hp//h
        u, v = hp-q*h, pp-q*p
        euclidean += 1
        if trace:
            history.append(dict(step='S2', h=h, hp=hp, p=p, pp=pp,
                                q=q, u=u, v=v, s=s))
        if u*u+v*v >= s:
            break
        s, hp, h, pp, p = u*u+v*v, h, u, p, v
    u, v = u-h, v-p  # S3
    if u*u+v*v < s:
        s, hp, pp = u*u+v*v, u, v
    sign = -1 if pp > 0 else 1
    U = [[-h, p], [-hp, pp]]
    V = [[sign*pp, sign*hp], [-sign*p, -sign*h]]
    if check:
        validate_basis(U, V, a, m)
    answer = {2: dict(squared=s, euclidean_steps=euclidean,
                      U=[x[:] for x in U], V=[x[:] for x in V])}
    while t < T:  # S4
        t += 1
        r = a*r % m
        for row in U:
            row.append(0)
        for row in V:
            row.append(0)
        U.append([-r]+[0]*(t-2)+[1])
        V.append([0]*(t-1)+[m])
        for i in range(t-1):
            q = round_ratio(V[i][0]*r, m)
            V[i][-1] = V[i][0]*r-q*m
            U[-1] = [x+q*y for x, y in zip(U[-1], U[i])]
        s = min(s, dot(U[-1], U[-1]))
        k, j = t-1, 0
        reductions = 0
        if check:
            validate_basis(U, V, a, m)
        if trace:
            history.append(dict(step='S4', t=t, U=[x[:] for x in U],
                                V=[x[:] for x in V], s=s))
        while True:  # S5/S6
            qs = [None]*t
            for i in range(t):
                if i == j:
                    continue
                val, norm = dot(V[i], V[j]), dot(V[j], V[j])
                qs[i] = 0
                if 2*abs(val) <= norm:
                    continue
                q = round_ratio(val, norm)
                old = dot(V[i], V[i])
                V[i] = [x-q*y for x, y in zip(V[i], V[j])]
                U[j] = [x+q*y for x, y in zip(U[j], U[i])]
                assert dot(V[i], V[i]) < old
                s, k = min(s, dot(U[j], U[j])), j
                qs[i] = q
                reductions += 1
                if check:
                    validate_basis(U, V, a, m)
            if trace:
                history.append(dict(step='S5', t=t, j=j+1, q=qs, s=s))
            j = (j+1) % t
            if j == k:
                break
        search_start_squared = s
        z = [isqrt(dot(row, row)*s//(m*m)) for row in V]  # S7
        X, Y, k = [0]*t, [0]*t, t-1
        expected = (prod(2*b+1 for b in z)-1)//2
        if expected > search_limit:
            raise RuntimeError(f'Search requires {expected} vectors, limit {search_limit}')
        searched = 0
        minimum_vectors = []
        while k >= 0:  # literal S8--S10
            if X[k] != z[k]:
                X[k] += 1
                Y = [u+v for u, v in zip(Y, U[k])]
                k += 1
                while k < t:
                    X[k] = -z[k]
                    Y = [u-2*z[k]*v for u, v in zip(Y, U[k])]
                    k += 1
                norm = dot(Y, Y)
                assert norm > 0
                if check:
                    assert Y == [sum(X[i]*U[i][j] for i in range(t)) for j in range(t)]
                searched += 1
                if norm < s:
                    s, minimum_vectors = norm, [Y[:]]
                elif norm == s:
                    minimum_vectors.append(Y[:])
            k -= 1
        assert searched == expected
        answer[t] = dict(squared=s, U=[x[:] for x in U], V=[x[:] for x in V],
                         z=z, searched=searched, reductions=reductions,
                         search_start_squared=search_start_squared,
                         minimum_vectors=minimum_vectors)
        if trace:
            history.append(dict(step='S10', t=t, s=s, z=z))
    return dict(values=answer, trace=history)


def shortest_direct(a, m, t, bound):
    """Exact sphere census, using a valid squared upper bound from ANY witness.

    Enumerate all tails with squared norm<=bound, then every admissible u_1
    within the remaining interval. Tests include equality, so all minimizers
    are returned. The caller must establish existence of a witness at bound.
    """
    powers = [pow(a, j, m) for j in range(t)]
    best, vectors, visited = bound, [], 0
    tail = [0]*(t-1)

    def visit(j, norm, residue):
        nonlocal best, vectors, visited
        if j == t-1:
            radius = isqrt(best-norm)
            base = -residue % m
            lo = (-radius-base+m-1)//m
            hi = (radius-base)//m
            for k in range(lo, hi+1):
                u = base+k*m
                if u == 0 and norm == 0:
                    continue
                n = norm+u*u
                visited += 1
                if n < best:
                    best, vectors = n, [(u, *tail)]
                elif n == best:
                    vectors.append((u, *tail))
            return
        radius = isqrt(best-norm)
        for u in range(-radius, radius+1):
            if norm+u*u > best:
                continue
            tail[j] = u
            visit(j+1, norm+u*u, (residue+powers[j+1]*u) % m)

    visit(0, 0, 0)
    assert vectors, (a, m, t, bound)
    return best, sorted(vectors), visited
