#!/usr/bin/env python3
"""Exact independent checks for continuants and TAOCP 4.5.3-1--10/32/48/52.

General proofs are in notes/euclid-basic.md. Passed checkpoints are resumable.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product, permutations
from math import gcd
from pathlib import Path
import json, random, sys, time

from mix_float_machine import Machine, Word, word

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/euclid-basic.json'


def continuant(xs):
    a, b = 0, 1
    for x in xs:
        a, b = b, x*b+a
    return b


def matrix_product(xs):
    a, b, c, d = 1, 0, 0, 1
    for x in xs:
        a, b, c, d = a*x+b, a, c*x+d, c
    return a, b, c, d


def determinant(rows):
    """Independent exact Gaussian elimination, including row interchanges."""
    a = [[F(x) for x in row] for row in rows]
    out = F(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            out = -out
        v = a[j][j]
        out *= v
        for i in range(j+1, len(a)):
            factor = a[i][j] / v
            for k in range(j+1, len(a)):
                a[i][k] -= factor*a[j][k]
    return out


def matching_support(n):
    support = set()
    for edges in range(1 << max(0, n-1)):
        if edges & (edges << 1):
            continue
        removed = edges | (edges << 1)
        support.add(((1 << n)-1) ^ removed)
    return support


def cf(xs, tail=F(0)):
    # Homogeneous coordinates preserve a zero intermediate denominator.
    # Only a pole of the final rational expression is rejected.
    numerator, denominator = tail.numerator, tail.denominator
    for x in reversed(xs):
        numerator, denominator = denominator, F(x)*denominator+numerator
    if denominator == 0:
        raise ZeroDivisionError
    return F(numerator)/F(denominator)


def canonical(x):
    out = []
    while x:
        a = (1/x).__floor__()
        out.append(a)
        x = 1/x-a
    return out


def continuants():
    rng = random.Random(45302)
    count = cuts = extended_cuts = 0
    for n in range(1, 13):
        for _ in range(40):
            xs = [rng.randrange(-4, 6) for _ in range(n)]
            a,b,c,d = matrix_product(xs)
            assert (a,b,c,d) == (continuant(xs), continuant(xs[:-1]),
                                  continuant(xs[1:]),
                                  continuant(xs[1:-1]) if n > 1 else 0)
            assert a*d-b*c == (-1)**n
            assert a == continuant(xs[::-1])
            tridiag = [[xs[i] if i == j else 1 if j == i+1 else
                        -1 if i == j+1 else 0 for j in range(n)] for i in range(n)]
            assert determinant(tridiag) == a
            total = 0
            for mask in matching_support(n):
                term = 1
                for i,x in enumerate(xs):
                    if mask >> i & 1:
                        term *= x
                total += term
            assert total == a
            for m in range(1,n):
                assert a == continuant(xs[:m])*continuant(xs[m:]) + \
                    continuant(xs[:m-1])*continuant(xs[m+1:])
                cuts += 1
                for k in range(n-m):
                    assert a*continuant(xs[m:m+k]) == \
                        continuant(xs[:m+k])*continuant(xs[m:]) + \
                        (-1)**k*continuant(xs[:m-1])*continuant(xs[m+k+1:])
                    extended_cuts += 1
            count += 1
    groups = {}
    for n in range(1,9):
        support = matching_support(n)
        good = []
        for perm in permutations(range(n)):
            transformed = {sum(1 << perm[i] for i in range(n) if mask >> i & 1)
                           for mask in support}
            if transformed == support:
                good.append(perm)
        assert set(good) == {tuple(range(n)), tuple(reversed(range(n)))}
        fib = [0,1]
        for _ in range(n+1):
            fib.append(sum(fib[-2:]))
        assert len(support) == fib[n+1]
        for k in range(1,n+1):
            assert sum(mask >> (k-1) & 1 for mask in support) == fib[k]*fib[n+1-k]
        groups[n] = good
    return dict(signed_sequences=count, cut_identities=cuts,
                extended_cut_identities=extended_cuts, permutation_groups=groups)


def fractions():
    count = inverse_count = 0
    for den in range(2, 128):
        for num in range(1, den):
            x = F(num,den)
            aa = canonical(x)
            assert aa[-1] >= 2 and cf(aa) == x
            remainder = x
            for n,a in enumerate(aa,1):
                assert a == (1/remainder).__floor__()
                remainder = 1/remainder-a
                conv = cf(aa[:n])
                q = continuant(aa[:n])
                assert gcd(continuant(aa[1:n]),q) == 1
                if remainder:
                    assert cf(list(reversed(aa[:n]))+[-x]) == -1/remainder
                    exact = 1/(q*continuant(aa[:n]+[1/remainder]))
                    assert abs(x-conv) == exact
                    assert exact <= F(1, q*continuant(aa[:n+1]))
                    inverse_count += 1
            count += 1
    rng = random.Random(45309)
    identities = 0
    for n in range(1,13):
        for _ in range(40):
            xs = [rng.randrange(1,10) for _ in range(n)]
            x = cf(xs)
            for k in range(1,n+1):
                assert x == cf(xs[:k-1]+[F(xs[k-1])+cf(xs[k:])])
                identities += 1
            assert cf([0]+xs) == xs[0]+cf(xs[1:])
            assert 1-x == cf([1,xs[0]-1]+xs[1:])
            for k in range(n-1):
                assert cf(xs[:k+1]+[0]+xs[k+1:]) == \
                    cf(xs[:k]+[xs[k]+xs[k+1]]+xs[k+2:])
                identities += 1
    # A concrete nonconvergent positive sequence from the printed answer 5.
    xs = [F(1,2**n) for n in range(1,81)]
    for n in range(1,80):
        q,qn = continuant(xs[:n]),continuant(xs[:n+1])
        assert q <= 2-F(1,2**n)
        assert abs(cf(xs[:n])-cf(xs[:n+1])) == 1/(q*qn) > F(1,4)
    return dict(rational_expansions=count, reversed_tail_checks=inverse_count,
                elementary_identity_checks=identities, nonconvergence_prefix=80,
                strict_bound_exception={'partial_quotients':[1], 'value':1})


def reciprocal_prefix(a0, a):
    a1,a2,a3,a4 = a
    if a0 > 0:
        out = [0,a0,a1,a2,a3,a4]
    elif a0 == 0:
        out = [a1,a2,a3,a4]
    elif a0 == -1 and a1 == 1:
        out = [-(a2+2),1,a3-1,a4]
    elif a0 == -1:
        out = [-2,1,a1-2,a2,a3,a4]
    else:
        out = [-1,1,-a0-2,1,a1-1,a2,a3,a4]
    while 0 in out[1:]:
        i = out.index(0,1)
        assert i+1 < len(out)
        out[i-1:i+2] = [out[i-1]+out[i+1]]
    return out


def transformations():
    count = 0
    families = Counter()
    for a0 in [-7,-3,-2,-1,0,1,5]:
        for aa in product(range(1,5),repeat=4):
            out = reciprocal_prefix(a0,aa)
            assert all(x > 0 for x in out[1:])
            for tail in [F(1,7),F(3,7),F(6,7)]:
                x = a0+cf(aa,tail)
                y = out[0]+cf(out[1:],tail)
                assert y == 1/x, (a0,aa,tail,out)
                count += 1
            families[(a0,len(out)-1)] += 1
    # Check the matrix identity, as a polynomial identity in the unknown tail,
    # by comparing its integer Möbius matrices rather than more sample tails.
    symbolic = 0
    for a0 in [-4,-2,-1,0,1,3]:
        for aa in product(range(1,4),repeat=4):
            out = reciprocal_prefix(a0,aa)
            a,b,c,d = matrix_product([a0]+list(aa))
            e,f,g,h = matrix_product(out)
            # Matrix maps [1,tail], reciprocal swaps its two rows.
            assert e*a == g*c and f*b == h*d and e*b+f*a == g*d+h*c
            symbolic += 1
    return dict(value_checks=count, exact_mobius_identities=symbolic,
                prefix_lengths={str(k):v for k,v in families.items()})


def bezout():
    count = 0
    for u in range(1,160):
        for v in range(1,u+1):
            a,b = (1,0,u),(0,1,v)
            quotients, rows = [],[b]
            while b[2]:
                q = a[2]//b[2]
                quotients.append(q)
                a,b = b,tuple(x-q*y for x,y in zip(a,b))
                rows.append(b)
            n = len(quotients)
            d = gcd(u,v)
            for j,row in enumerate(rows,1):
                x = 0 if j == 1 else (-1)**j*continuant(quotients[1:j-1])
                y = (-1)**(j-1)*continuant(quotients[:j-1])
                z = 0 if j == n+1 else d*continuant(quotients[j:])
                assert row == (x,y,z)
            count += 1
    return dict(input_pairs=count)


def ostrowski():
    sequences = list(product(range(1,4),repeat=5))
    sequences.append((1,)*14)
    representations = 0
    for aa in sequences:
        q = [1]
        for i,a in enumerate(aa):
            q.append(a*q[-1]+(q[-2] if i else 0))
        counts = Counter()
        for digits in product(*(range(a+1) for a in aa)):
            if digits[0] == aa[0]:
                continue
            if any(digits[i] == aa[i] and digits[i-1] for i in range(1,len(aa))):
                continue
            n = sum(c*w for c,w in zip(digits,q))
            counts[n] += 1
            remaining = n
            greedy = [0]*len(aa)
            for i in reversed(range(len(aa))):
                greedy[i], remaining = divmod(remaining,q[i])
            assert remaining == 0 and tuple(greedy) == digits
            representations += 1
        assert counts == Counter({n:1 for n in range(q[-1])})
    return dict(prefixes=len(sequences), representations=representations,
                compared_with='all integers 0 <= n < q_next, multiplicity exactly one')


def mix():
    rng = random.Random(45301)
    count = 0
    order_edges = []
    for base in [64,100]:
        W = base**5
        cases = list(product(range(32),repeat=2))
        cases += [(rng.randrange(W),rng.randrange(W)) for _ in range(200)]
        cases += list(product([0,1,2,W//2,W-2,W-1],repeat=2))
        for u,v in cases:
            a,b = v,u
            T=Q=0
            while b:
                r = a-b
                if r < b:
                    r = abs(r)
                    Q += 1
                else:
                    r %= b
                a,b = b,r
                T += 1
                assert T < 200
            m = Machine(base,source=ROOT/'sources/euclid-unit.mix')
            m.memory[m.symbols['U']] = word(u)
            m.memory[m.symbols['V']] = word(v)
            for reg in m.reg:
                m.reg[reg] = Word(-1,base*base-1)
            m.ret = m.symbols['UNIT_END']
            m.max_steps = 10000
            m.execute('UNIT')
            assert m.halt is None and not m.ov
            assert m.reg['A'].val == gcd(u,v)
            assert m.visits['E03'] == T and m.visits['E08'] == T-Q
            assert m.time == 24*T-12*Q+6
            if u < 6 and v < 3 and base == 64:
                order_edges.append(dict(u=u,v=v,T=T,Q=Q,time=m.time))
            count += 1
    return dict(machine_runs=count, exact_time='24*T - 12*Q + 6',
                Q_definition='iterations that bypass DIV, including initial negative difference',
                initial_order_examples=order_edges)


def main():
    data = json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for fn in [continuants,fractions,transformations,bezout,ostrowski,mix]:
        if data.get(fn.__name__,{}).get('status') == 'passed':
            continue
        start = time.monotonic()
        result = fn()
        data[fn.__name__] = dict(status='passed',seconds=time.monotonic()-start,result=result)
        OUT.write_text(json.dumps(data,indent=2)+'\n')
        print(fn.__name__,data[fn.__name__]['seconds'],flush=True)


if __name__ == '__main__':
    main()
