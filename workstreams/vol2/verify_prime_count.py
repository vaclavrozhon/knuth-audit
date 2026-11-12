"""TAOCP2 4.5.4-41: truncated recursion and a linear-space implementation.

The tested algorithm uses only primes <= N and sieved integers <= N**2.
The separate validator may use a full sieve to N**3, trace sets and big tables;
none of these belong to the claimed algorithm's working storage.
"""
from pathlib import Path
from math import isqrt, comb, gcd, prod
from bisect import bisect_right
from collections import Counter
from functools import lru_cache
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/prime-count.json'


def full_sieve(limit):
    flags = bytearray(b'\x01')*(limit+1)
    flags[:2] = b'\x00\x00'
    for p in range(2, isqrt(limit)+1):
        if flags[p]:
            flags[p*p::p] = b'\x00'*((limit-p*p)//p+1)
    return flags


def tables(N):
    least = [0]*(N+1); mu = [1]*(N+1); primes = []
    least[1] = N+1
    for p in range(2, N+1):
        if least[p]: continue
        primes.append(p)
        for k in range(p, N+1, p):
            if not least[k]: least[k] = p
            mu[k] = -mu[k]
        for k in range(p*p, N+1, p*p): mu[k] = 0
    return primes, least, mu


class SumTree:
    def __init__(self, length, stats, values=None):
        self.length = length; self.size = 1 << (length-1).bit_length()
        self.a = [0]*(2*self.size); self.stats = stats
        self.a[self.size:self.size+length] = [1]*length if values is None else values
        for i in range(self.size-1, 0, -1): self.a[i] = self.a[2*i]+self.a[2*i+1]
        stats['peak_tree_cells'] = max(stats['peak_tree_cells'], len(self.a))

    def remove(self, index):
        self.stats['mark_attempts'] += 1
        i = self.size+index
        if not self.a[i]: return
        while i:
            self.a[i] -= 1; i //= 2; self.stats['tree_decrements'] += 1

    def prefix(self, length):
        assert 0 <= length <= self.length
        l = self.size; r = l+length; result = 0
        while l < r:
            if l & 1: result += self.a[l]; l += 1
            if r & 1: r -= 1; result += self.a[r]
            l //= 2; r //= 2; self.stats['query_levels'] += 1
        return result


def sieve_block(left, right, primes):
    flags = bytearray(b'\x01')*(right-left+1)
    for p in primes:
        if p*p > right: break
        first = max(p*p, (left+p-1)//p*p)
        for t in range(first, right+1, p): flags[t-left] = 0
    for t in range(left, min(right, 1)+1): flags[t-left] = 0
    return flags


def segmented(N, check_query=None):
    assert N >= 2
    X = N**3; primes, least, mu = tables(N); a = len(primes)
    stats = Counter(); totals = [0]*(a+1)
    ordinary = sum(mu[k]*(X//k) for k in range(1, N))
    special = 0
    for left in range(1, N*N+1, N):
        right = min(left+N-1, N*N); tree = SumTree(right-left+1, stats)
        for j, p in enumerate(primes):
            # Query x=floor(X/(k*p)) belongs to [left,right] exactly here.
            lo = max((N+p-1)//p, X//(p*(right+1))+1)
            hi = min(N-1, X//(p*left))
            stats['segment_prime_visits'] += 1
            for k in range(lo, hi+1):
                stats['candidate_pairs'] += 1
                if mu[k] and least[k] > p:
                    x = X//(k*p); value = totals[j]+tree.prefix(x-left+1)
                    special -= mu[k]*value; stats['special_queries'] += 1
                    if check_query is not None: check_query(j, k, x, value)
            # totals[j] refers to BEFORE removing prime p.
            totals[j] += tree.a[1]
            for t in range((left+p-1)//p*p, right+1, p): tree.remove(t-left)
        totals[a] += tree.a[1]
    survivor = ordinary+special
    pi_square = a+totals[a]-1

    # Stream the smaller semiprime factor upward and its quotient downward.
    # Only two O(N)-sized sieve blocks and the primes <=N are retained.
    at = N*N; pi_at = pi_square; qleft = qright = 0; qflags = None
    b = a; sum_pi = 0; pair_rows = [] if N == 10 else None
    for left in range(N+1, isqrt(X)+1, N):
        right = min(left+N-1, isqrt(X)); flags = sieve_block(left, right, primes)
        for i, flag in enumerate(flags):
            if not flag: continue
            p = left+i; q = X//p
            assert N < p <= q <= N*N
            while at > q:
                if qflags is None or not qleft <= at <= qright:
                    qright = at; qleft = max(1, at-N+1)
                    qflags = sieve_block(qleft, qright, primes)
                    stats['quotient_blocks'] += 1
                pi_at -= qflags[at-qleft]; at -= 1
            sum_pi += pi_at; b += 1; stats['semiprime_queries'] += 1
            if pair_rows is not None: pair_rows.append(dict(p=p, q=q, pi_q=pi_at))
    pairs = sum_pi-comb(b, 2)+comb(a, 2)
    result = a+survivor-1-pairs
    # These are modeled storage counts, excluding validator traces and Python
    # object overhead.  No array of length N**2 is used by this implementation.
    stats['working_cells_bound'] = stats['peak_tree_cells']+5*(N+1)+2*(a+1)
    assert stats['working_cells_bound'] <= 12*(N+1)
    assert stats['candidate_pairs'] <= N*a
    return dict(N=N, X=X, pi=result, ordinary=ordinary, special=special,
                f=survivor, f2=pairs, pi_N=a, pi_square=pi_square,
                stats=dict(stats), example_pair_rows=pair_rows)


def recursion_checks():
    rows = []
    for N in range(2, 81):
        primes, least, mu = tables(N); X = N**3
        leaves = Counter(); ordinary = Counter(); special = Counter(); internal = 0
        def walk(k, j, sign):
            nonlocal internal
            if k >= N or j == 0:
                leaves[k, j] += sign
                (special if k >= N else ordinary)[k, j] += sign
            else:
                internal += 1
                walk(k, j-1, sign); walk(k*primes[j-1], j-1, -sign)
        walk(1, len(primes), 1)
        expected_ordinary = Counter({(k, 0): mu[k] for k in range(1, N) if mu[k]})
        expected_special = Counter()
        for j, p in enumerate(primes):
            for k in range((N+p-1)//p, N):
                if mu[k] and least[k] > p: expected_special[k*p, j] -= mu[k]
        assert dict(ordinary) == dict(expected_ordinary)
        assert dict(special) == dict(expected_special)
        @lru_cache(None)
        def phi(x, j):
            return x if j == 0 else phi(x, j-1)-phi(x//primes[j-1], j-1)
        leaf_sum = sum(c*phi(X//k, j) for (k, j), c in leaves.items())
        # Direct removal all the way to X is an independent, slower oracle.
        alive = bytearray(b'\x01')*(X+1); alive[0] = 0
        for p in primes: alive[p::p] = b'\x00'*(X//p)
        assert leaf_sum == sum(alive) == phi(X, len(primes))
        rows.append(dict(N=N, internal_nodes=internal, ordinary_leaves=len(ordinary),
                         special_leaves=len(special), f=leaf_sum))
    return dict(cases=len(rows), rows=rows,
                total_internal=sum(x['internal_nodes'] for x in rows),
                total_special=sum(x['special_leaves'] for x in rows))


def segmented_checks():
    inputs = list(range(2, 130))+[200, 255, 256, 257, 1000]
    oracle_flags = full_sieve(257**3)
    oracle_primes = [n for n, flag in enumerate(oracle_flags) if flag]
    rows = []; digest = hashlib.sha256(); all_queries = 0; oracle_queries = 0
    for N in inputs:
        primes, least, mu = tables(N); seen = set()
        primorials = [1]
        for p in primes: primorials.append(primorials[-1]*p)
        def check(j, k, x, value):
            nonlocal all_queries, oracle_queries
            assert (j, k) not in seen; seen.add((j, k)); all_queries += 1
            assert x == N**3//(k*primes[j]) and x <= N*N
            if N <= 32:
                assert value == sum(gcd(t, primorials[j]) == 1 for t in range(1, x+1))
                oracle_queries += 1
            digest.update(f'{N},{j},{k},{x},{value}\n'.encode())
        row = segmented(N, check)
        expected = {(j, k) for j, p in enumerate(primes)
                    for k in range(1, N) if k*p >= N and mu[k] and least[k] > p}
        assert seen == expected
        if N <= 257:
            assert row['pi'] == bisect_right(oracle_primes, N**3)
        else:
            # Primary table in Oliveira e Silva, 2006, p766 (external exact value).
            assert N == 1000 and row['pi'] == 50847534
        assert row['pi_square'] == bisect_right(oracle_primes, N*N)
        if N == 10:
            assert (row['ordinary'], row['special'], row['f'], row['f2'], row['pi']) == (-9, 237, 228, 63, 168)
            assert [x['pi_q'] for x in row['example_pair_rows']] == [24, 21, 16, 15, 14, 11, 11]
        rows.append(row)
    return dict(cases=len(rows), oracle_limit=257**3,
                externally_compared_N=[1000], special_queries=all_queries,
                direct_coprimality_queries=oracle_queries, query_sha256=digest.hexdigest(), rows=rows)


def shifted_leaf_checks():
    checked = 0; stats = Counter()
    for N in range(2, 25):
        primes = tables(N)[0]; tree = SumTree(N*N, stats); primorial = 1
        for j in range(len(primes)+1):
            for x in range(N*N+1):
                # Book leaf n stores the integer n+1; 1 is added separately.
                value = 0 if x == 0 else 1+tree.prefix(x-1)
                assert value == sum(gcd(t, primorial) == 1 for t in range(1, x+1))
                checked += 1
            if j < len(primes):
                p = primes[j]; primorial *= p
                for t in range(p, N*N+2, p): tree.remove(t-2)
    return dict(N_range=[2, 24], prefix_checks=checked,
                interpretation='for x>=1: f(x,p_j)=1+prefix(floor(x)-1)')


def main():
    data = json.loads(OUT.read_text()) if OUT.exists() else dict(blocks={})
    for label, function in [('recursion', recursion_checks), ('segmented', segmented_checks),
                            ('shifted_leaves', shifted_leaf_checks)]:
        if data['blocks'].get(label, {}).get('status') == 'passed':
            print('skip completed', label, flush=True); continue
        start = time.perf_counter(); result = function()
        result.update(status='passed', elapsed_seconds=time.perf_counter()-start)
        data['blocks'][label] = result
        temp = OUT.with_suffix('.json.tmp'); temp.write_text(json.dumps(data, indent=2)+'\n'); temp.replace(OUT)
        print(label, 'passed', result['elapsed_seconds'], flush=True)


if __name__ == '__main__': main()
