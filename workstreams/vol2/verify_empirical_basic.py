"""Exact checks for TAOCP 3.3.2 A--F and exercises 1--10,21,22.

Finished blocks are checkpointed; --resume avoids repeating them.
"""
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product, permutations
from math import factorial, comb, prod
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent
DEST = ROOT/'results/empirical-basic.json'


@lru_cache(None)
def stirling(n, r):
    if n == 0:
        return int(r == 0)
    if r <= 0 or r > n:
        return 0
    return r*stirling(n-1, r)+stirling(n-1, r-1)


def falling(d, r):
    return prod(d-j for j in range(r))


def gap_lengths(bits, n, cap):
    j = -1
    counts = [0]*(cap+1)
    lengths = []
    for _ in range(n):
        r = 0
        while True:
            j += 1
            if bits[j]:
                break
            r += 1
        lengths.append(r)
        counts[min(r, cap)] += 1
    return lengths, counts, j+1


def gaps():
    cases = 0
    for length in range(1, 13):
        completion = Counter()
        for bits in product(range(2), repeat=length):
            positions = [j for j, x in enumerate(bits) if x]
            if bits[-1]:
                completion[len(positions)] += 1
            if not positions:
                continue
            reference = [b-a-1 for a,b in zip([-1]+positions, positions)]
            for cap in range(5):
                got, counts, used = gap_lengths(bits, len(positions), cap)
                assert got == reference and used == positions[-1]+1
                assert counts == [sum(min(r,cap) == k for r in reference)
                                  for k in range(cap+1)]
                cases += 1
        assert completion == {n:comb(length-1,n-1) for n in range(1,length+1)}
    # Fixed-N cyclic gaps, t=1: independent position-count implementation.
    cyclic = []
    for n in range(5, 13):
        means = [Q(0),Q(0)]
        seconds = [[Q(0),Q(0)],[Q(0),Q(0)]]
        for bits in product(range(2), repeat=n):
            z0 = sum(bits[j] == bits[(j+1)%n] == 1 for j in range(n))
            z1 = sum(bits[j] == 1 and bits[(j+1)%n] == 0 for j in range(n))
            z = [z0,z1]
            for i in range(2):
                means[i] += z[i]
                for j in range(2):
                    seconds[i][j] += z[i]*z[j]
        means = [x/2**n for x in means]
        cov = [[seconds[i][j]/2**n-means[i]*means[j]
                for j in range(2)] for i in range(2)]
        assert means == [Q(n,4)]*2
        assert cov == [[Q(5*n,16),Q(-n,16)],[Q(-n,16),Q(n,16)]]
        cyclic.append(dict(N=n,mean=list(map(str,means)),
                           covariance=[[str(x) for x in row] for row in cov]))
    return dict(algorithm_cases=cases,negative_binomial_lengths=12,
                cyclic_t1_exact_moments=cyclic)


def coupon_lengths(word, d, w):
    j = -1
    out = []
    while j+1 < len(word):
        q = r = 0
        occurs = [0]*d
        while q < w:
            j += 1
            if j == len(word):
                return out
            r += 1
            if not occurs[word[j]]:
                occurs[word[j]] = 1
                q += 1
        out.append(r)
    return out


def coupons_poker():
    words = algo_cases = 0
    for d in range(1,5):
        for length in range(1,8):
            occupancy = Counter()
            first_completion = {w:Counter() for w in range(1,d+1)}
            for word in product(range(d),repeat=length):
                occupancy[len(set(word))] += 1
                words += 1
                for w in range(1,d+1):
                    reference = []
                    pos = 0
                    while pos < length:
                        ends = [j for j in range(pos+1,length+1)
                                if len(set(word[pos:j])) == w]
                        if not ends:
                            break
                        j = min(ends)
                        reference.append(j-pos)
                        pos = j
                    assert coupon_lengths(word,d,w) == reference
                    if reference:
                        first_completion[w][reference[0]] += 1
                    algo_cases += 1
            assert occupancy == {r:falling(d,r)*stirling(length,r)
                                 for r in range(1,min(d,length)+1)}
            for w in range(1,d+1):
                for r in range(1,length+1):
                    assert first_completion[w][r] == (
                        falling(d,w)*stirling(r-1,w-1)*d**(length-r))
    # A second model: Markov states = number of distinct coupons observed.
    dp_cases = 0
    moments = []
    for d in range(1,13):
        for w in range(1,d+1):
            state = [Q(1)]+[Q(0)]*w
            cumulative = Q(0)
            for r in range(1,25):
                nxt = [Q(0)]*(w+1)
                for j in range(w):
                    nxt[j] += state[j]*Q(j,d)
                    nxt[j+1] += state[j]*Q(d-j,d)
                first = nxt[w]
                nxt[w] = Q(0)
                assert first == Q(falling(d,w)*stirling(r-1,w-1),d**r)
                cumulative += first
                tail = sum(Q(falling(d,j)*stirling(r,j),d**r)
                           for j in range(w))
                assert cumulative+tail == 1
                state = nxt
                dp_cases += 1
            mean = second = Q(0)
            for j in reversed(range(w)):
                p = Q(d-j,d)
                mean += 1/p
                second += (2*mean-1)/p
            formula_mean = sum((Q(d,d-j) for j in range(w)),Q(0))
            formula_var = sum((Q(j*d,(d-j)**2) for j in range(w)),Q(0))
            assert mean == formula_mean and second-mean**2 == formula_var
            moments.append(dict(d=d,w=w,mean=str(mean),variance=str(formula_var)))
    # All seven poker patterns for an alphabet of five symbols.
    patterns = Counter(tuple(sorted(Counter(word).values(),reverse=True))
                       for word in product(range(5),repeat=5))
    d = 5
    expected = {(1,1,1,1,1):falling(d,5), (2,1,1,1):10*falling(d,4),
                (2,2,1):15*falling(d,3), (3,1,1):10*falling(d,3),
                (3,2):10*falling(d,2), (4,1):5*falling(d,2), (5,):d}
    assert patterns == expected
    example = coupon_lengths(tuple(map(int,'1101221022120202001212201010201121')),3,3)
    assert example == [5,3,5,6,5,5,4]
    return dict(enumerated_words=words,algorithm_cases=algo_cases,
                markov_formula_comparisons=dp_cases,moments=moments,
                poker_d5={str(k):v for k,v in patterns.items()},exercise7=example)


def permutation_rank(word):
    a = list(word)
    f = 0
    for r in range(len(a),1,-1):
        s = max(range(r),key=a.__getitem__)
        f = r*f+s
        a[r-1],a[s] = a[s],a[r-1]
    return f,a


def permutation_unrank(f,t):
    a = list(range(t))
    for r in range(2,t+1):
        f,s = divmod(f,r)
        a[r-1],a[s] = a[s],a[r-1]
    assert f == 0
    return a


def factorial_codes():
    cases = 0
    for t in range(1,9):
        values = set()
        for perm in permutations(range(t)):
            f,a = permutation_rank(perm)
            assert a == list(range(t))
            assert permutation_unrank(f,t) == list(perm)
            assert f not in values
            values.add(f)
            cases += 1
        assert values == set(range(factorial(t)))
    f,_ = permutation_rank([1,2,9,8,5,3,6,7,0,4])
    assert f == 886862
    perm = permutation_unrank(1024,10)
    assert perm == [9,6,5,2,3,4,0,1,7,8]
    return dict(exhaustive_permutations=cases,exercise21=f,exercise22=perm)


def main():
    out = json.loads(DEST.read_text()) if '--resume' in sys.argv else {}
    out['status'] = 'in_progress'
    for name,run in [('gaps',gaps),('coupons_poker',coupons_poker),
                     ('permutation_codes',factorial_codes)]:
        if name in out:
            continue
        out[name] = run()
        DEST.write_text(json.dumps(out,indent=2)+'\n')
        print(name,'completed',flush=True)
    out['status'] = 'completed'
    DEST.write_text(json.dumps(out,indent=2)+'\n')


if __name__ == '__main__':
    main()
