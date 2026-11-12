"""Exact matrix models independent of the closed formulas in TAOCP 1.2.3."""
from fractions import Fraction as F
from itertools import combinations
from math import prod, comb, factorial
from pathlib import Path
from random import Random
import json

ROOT = Path(__file__).resolve().parent


def det(a):
    a = [[F(x) for x in row] for row in a]
    n = len(a)
    d = F(1)
    for j in range(n):
        k = next((i for i in range(j, n) if a[i][j]), None)
        if k is None:
            return F(0)
        if k != j:
            a[k], a[j] = a[j], a[k]
            d = -d
        pivot = a[j][j]
        d *= pivot
        for i in range(j+1, n):
            multiplier = a[i][j]/pivot
            for k in range(j+1, n):
                a[i][k] -= multiplier*a[j][k]
    return d


def inverse(a):
    n = len(a)
    rows = [[F(x) for x in a[i]]+[F(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k = next((i for i in range(j, n) if rows[i][j]), None)
        if k is None:
            return None
        rows[j], rows[k] = rows[k], rows[j]
        pivot = rows[j][j]
        rows[j] = [x/pivot for x in rows[j]]
        for i in range(n):
            if i != j:
                t = rows[i][j]
                rows[i] = [x-t*y for x, y in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def multiply(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def binomial(n, k):
    if k < 0:
        return 0
    if n >= 0:
        return comb(n, k) if k <= n else 0
    return (-1)**k*comb(k-n-1, k)


def elementary(xs, k):
    return sum(prod(c) for c in combinations(xs, k))


def main():
    rng = Random(123036)
    counts = dict(combinatorial=0, vandermonde=0, cauchy=0,
                  hilbert_entries=0, binet_cauchy=0, krattenthaler=0)
    for n in range(1, 8):
        for x in range(-3, 4):
            for y in range(-3, 4):
                a = [[x*(i == j)+y for j in range(n)] for i in range(n)]
                assert det(a) == x**(n-1)*(x+n*y)
                inv = inverse(a)
                if inv is not None:
                    assert multiply(a, inv) == identity(n)
                    assert sum(map(sum, inv)) == F(n, x+n*y)
                    if x != 0:
                        b = [[F(-y+(i == j)*(x+n*y), x*(x+n*y))
                              for j in range(n)] for i in range(n)]
                        assert b == inv
                    else:
                        assert n == 1 and inv == [[F(1, y)]]
                counts['combinatorial'] += 1
    nonzero = [i for i in range(-9, 10) if i]
    for n in range(1, 8):
        for _ in range(30):
            xs = rng.sample(nonzero, n)
            a = [[x**(i+1) for x in xs] for i in range(n)]
            closed_det = prod(xs)*prod(xs[j]-xs[i] for i in range(n) for j in range(i+1, n))
            assert det(a) == closed_det
            inv = inverse(a)
            b = [[F((-1)**j*elementary(xs[:i]+xs[i+1:], n-j-1),
                      xs[i]*prod(xs[k]-xs[i] for k in range(n) if k != i))
                  for j in range(n)] for i in range(n)]
            assert inv == b and multiply(a, b) == identity(n)
            assert sum(map(sum, inv)) == 1-prod(1-F(1, x) for x in xs)
            counts['vandermonde'] += 1
            xs = rng.sample(range(-9, 10), n)
            ys = rng.sample([y for y in range(-19, 20) if all(x+y for x in xs)], n)
            a = [[F(1, x+y) for y in ys] for x in xs]
            numerator = prod((xs[j]-xs[i])*(ys[j]-ys[i])
                             for i in range(n) for j in range(i+1, n))
            denominator = prod(x+y for x in xs for y in ys)
            assert det(a) == F(numerator, denominator)
            inv = inverse(a)
            b = [[F(prod((xs[j]+ys[k])*(xs[k]+ys[i]) for k in range(n)),
                      (xs[j]+ys[i])*prod(xs[j]-xs[k] for k in range(n) if k != j)
                      *prod(ys[i]-ys[k] for k in range(n) if k != i))
                  for j in range(n)] for i in range(n)]
            assert inv == b and multiply(a, b) == identity(n)
            assert sum(map(sum, inv)) == sum(xs)+sum(ys)
            for j in range(n):
                assert sum(inv[i][j] for i in range(n)) == F(
                    prod(xs[j]+y for y in ys),
                    prod(xs[j]-xs[k] for k in range(n) if k != j))
            counts['cauchy'] += 1
    hilbert_bounds = {}
    for n in range(1, 13):
        a = [[F(1, i+j-1) for j in range(1, n+1)] for i in range(1, n+1)]
        inv = inverse(a)
        assert multiply(a, inv) == identity(n)
        assert sum(map(sum, inv)) == n*n
        for i in range(1, n+1):
            for j in range(1, n+1):
                entry = F((-1)**(i+j)*factorial(i+n-1)*factorial(j+n-1),
                          (i+j-1)*factorial(i-1)**2*factorial(j-1)**2
                          *factorial(n-i)*factorial(n-j))
                form1 = F((-1)**(i+j)*i*j, i+j-1)*binomial(-i, n)*comb(n, i)*binomial(-j, n)*comb(n, j)
                form2 = (-1)**(i+j)*j*comb(i+j-2, i-1)*comb(i+n-1, i-1)*comb(j+n-1, n-i)*comb(n, j)
                form3 = (i+j-1)*comb(i+j-2, i-1)**2*binomial(-i-j, n-i)*binomial(-i-j, n-j)
                assert entry == form1 == form2 == form3 == inv[i-1][j-1]
                assert entry.denominator == 1
                assert all(entry.numerator % d == 0 for d in
                           [i, j, n, i+j-1, i+n-1, j+n-1, n-i+1, n-j+1])
                counts['hilbert_entries'] += 1
        v = [(-1)**k*comb(n-1, k) for k in range(n)]
        quadratic = sum(v[i]*a[i][j]*v[j] for i in range(n) for j in range(n))
        assert quadratic == F(1, 2*n-1)
        assert sum(x*x for x in v) == comb(2*n-2, n-1)
        hilbert_bounds[n] = (2*n-1)*comb(2*n-2, n-1)
    for m in range(1, 5):
        for n in range(1, 7):
            for _ in range(15):
                a = [[rng.randrange(-3, 4) for _ in range(n)] for _ in range(m)]
                b = [[rng.randrange(-3, 4) for _ in range(m)] for _ in range(n)]
                rhs = sum(det([[row[j] for j in js] for row in a])*det([b[j] for j in js])
                          for js in combinations(range(n), m))
                assert det(multiply(a, b)) == rhs
                counts['binet_cauchy'] += 1
    for n in range(1, 8):
        for _ in range(50):
            xs, ps, qs = [[rng.randrange(-4, 5) for _ in range(k)] for k in [n, n-1, n-1]]
            a = [[prod(xs[i]+ps[k] for k in range(j)) *
                  prod(xs[i]+qs[k-1] for k in range(j+1, n))
                  for j in range(n)] for i in range(n)]
            rhs = prod((xs[i]-xs[j])*(ps[i]-qs[j-1])
                       for i in range(n) for j in range(i+1, n))
            assert det(a) == rhs
            counts['krattenthaler'] += 1
    result = {'arithmetic': 'Exact rational Gaussian elimination versus independent closed formulas.',
              'counts': counts, 'hilbert_condition_number_lower_bounds': hilbert_bounds,
              'bounds_status': 'Values of the general proven bound; not measured floating-point condition numbers.',
              'combinatorial_n1_x0': 'Inverse exists when y!=0; use the cancelled scalar formula 1/y.'}
    (ROOT/'results/matrices.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(counts))


if __name__ == '__main__':
    main()
