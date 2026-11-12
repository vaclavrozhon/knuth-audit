#!/usr/bin/env python3
"""Literal Algorithm O, independent circular dip factorization, exact counts."""
from collections import Counter
from itertools import product
from math import comb, log
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/commafree'


def primitive(x):
    return all(x != x[k:]+x[:k] for k in range(1,len(x)))


def eastman(x):
    n = len(x)
    assert n > 1 and n % 2 and primitive(x)
    xx = x+x
    b = list(range(2*n))
    history = []
    while True:
        t = len([v for v in b if v < n])
        def less(i):
            u, v = xx[b[i-1]:b[i]], xx[b[i]:b[i+1]]
            return (len(u),u) < (len(v),v)
        i = next(i for i in range(1,t+1) if not less(i))
        j = next(j for j in range(i+2,t+3) if less(j-1))
        i = i0 = j % t
        new = []
        while True:
            j = i+2
            while not less(j-1):
                j += 1
            if (j-i) % 2:
                if i < t:
                    new.append(b[i])
                else:
                    new.insert(0,b[i-t])
            if j >= i0+t:
                break
            i = j
        history.append(new.copy())
        assert len(new) % 2 and len(new)*3 <= t
        if len(new) == 1:
            return xx[new[0]:new[0]+n], history
        b = new.copy()
        k, t = len(b), len(b)
        while b[k-t] < 2*n:
            b.append(b[k-t]+n)
            k += 1


def circular_oracle(x):
    """Try every cut of each circular sequence; retain the odd dip boundaries."""
    n = len(x)
    b = list(range(n))
    history = []
    while len(b) > 1:
        t = len(b)
        xx = x+x
        extended = b+[b[0]+n]
        y = [xx[extended[i]:extended[i+1]] for i in range(t)]
        y = [(len(v),v) for v in y]
        partitions = set()
        for start in range(t):
            i, boundaries = start, []
            while i < start+t:
                j = i+2
                while y[(j-2)%t] >= y[(j-1)%t]:
                    j += 1
                    assert j <= i+t+1
                if j > start+t:
                    break
                boundaries.append((i%t,j-i))
                i = j
            if i == start+t:
                partitions.add(tuple(sorted(boundaries)))
        assert len(partitions) == 1
        b = [b[i] for i,k in next(iter(partitions)) if k % 2]
        history.append(b.copy())
    return (x+x)[b[0]:b[0]+n], history


def fast_commafree(code):
    n = len(next(iter(code)))
    p = [set(w[:i] for w in code) for i in range(n+1)]
    s = [set(w[n-i:] for w in code) for i in range(n+1)]
    return all(w[:i] not in s[i] or w[i:] not in p[n-i]
               for w in code for i in range(1,n))


def gf(m, maxn):
    f = [-1,0]+[(k-1)*comb(m+k-2,k) for k in range(2,maxn+1)]
    num = [((-1)**k-1)*f[k] for k in range(maxn+1)]
    den = [((-1)**k+1)*f[k] for k in range(maxn+1)]
    g = []
    for k in range(maxn+1):
        value = Fraction(num[k]-sum(den[i]*g[k-i] for i in range(1,k+1)),den[0])
        assert value.denominator == 1
        g.append(int(value))
    return g


def main():
    results = {'counts':[], 'dips':[]}
    x = tuple(map(int,'3141592653589793238'))
    y,h = eastman(x)
    assert h == [[5,8,15],[15]] and y == x[15:]+x[:15]
    assert (y,h) == circular_oracle(x)
    results['example37a'] = {'input':x,'output':y,'boundaries':h}
    a,b = (0,),(1,)
    for e in range(1,7):
        a,b = a+a+b,b+a+b
        for x in [a,b]:
            y,h = eastman(x)
            assert len(h) == e
    results['worst_case_exponents'] = list(range(1,7))
    for m in [2,3,4]:
        for k in range(2,8):
            count = sum(all(x[i] >= x[i+1] for i in range(k-2)) and x[-2]<x[-1]
                        for x in product(range(m),repeat=k))
            expected = (k-1)*comb(m+k-2,k)
            assert count == expected
            results['dips'].append({'m':m,'k':k,'count':count})
    for m,maxn in [(2,13),(3,9),(4,9)]:
        g = gf(m,maxn)
        for n in range(3,maxn+1,2):
            code = set()
            rounds = Counter()
            checked_rotations = 0
            for x in product(range(m),repeat=n):
                rotations = [x[k:]+x[:k] for k in range(n)]
                if len(set(rotations)) < n or x != min(rotations):
                    continue
                y,h = eastman(x)
                assert (y,h) == circular_oracle(x)
                assert len(h) <= int(log(n,3)+1e-10)
                code.add(y)
                rounds[len(h)] += n
                if m == 2 or n <= 7:
                    for z in rotations:
                        yz,hz = eastman(z)
                        assert yz == y and len(hz) == len(h)
                        checked_rotations += 1
            assert sum(rounds.values()) == n*len(code)
            assert rounds[1] == n*g[n]
            assert fast_commafree(code)
            result={'m':m,'n':n,'aperiodic_words':n*len(code),'round_histogram':dict(rounds),
                    'probability':str(Fraction(rounds[1],n*len(code))),
                    'gf_one_round':n*g[n],'codeword_count':len(code),
                    'rotations_checked':checked_rotations}
            if n == 9:
                result['printed_probability'] = str(1-Fraction(3,comb(m**3-1,3)))
                result['correct_probability'] = str(Fraction(rounds[1],n*len(code)))
            results['counts'].append(result)
            print(result,flush=True)
    OUT.mkdir(exist_ok=True)
    (OUT/'eastman-verified.json').write_text(json.dumps(results,indent=2)+'\n')


if __name__ == '__main__':
    main()
