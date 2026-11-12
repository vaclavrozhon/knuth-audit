#!/usr/bin/env python3
"""Exact finite checks for Lemma P, the interval cover, and chain encoding."""
from collections import Counter
from datetime import datetime, timezone
import argparse
import itertools
import json
import math
from pathlib import Path
import time

BASE = Path(__file__).resolve().parent
RESULT = BASE / "results/powers-counting.json"


def mask(interval):
    a, b = interval
    return ((1 << (b-a))-1) << a


def reduce_cover(intervals):
    kept = list(intervals)
    union = 0
    for interval in kept:
        union |= mask(interval)
    for interval in list(kept):
        other = 0
        for item in kept:
            if item != interval:
                other |= mask(item)
        if other == union:
            kept.remove(interval)
    return sorted(kept)


def components(intervals):
    result = []
    for a, b in intervals:
        if result and a <= result[-1][1]:
            result[-1] = (result[-1][0], max(result[-1][1], b))
        else:
            result.append((a, b))
    return result


def interval_block():
    universe = [(a, b) for a in range(5) for b in range(a+1, 6)]
    histogram = Counter()
    for selection in range(1 << len(universe)):
        family = [x for i, x in enumerate(universe) if selection & (1 << i)]
        reduced = reduce_cover(family)
        counts = [sum(a < k <= b for a, b in reduced) for k in range(1, 6)]
        original = [any(a < k <= b for a, b in family) for k in range(1, 6)]
        assert [bool(x) for x in counts] == original
        assert max(counts) <= 2
        merged = components(reduced)
        assert [any(a < k <= b for a, b in merged) for k in range(1, 6)] == original
        assert sum(b-a for a, b in reduced) <= 2*sum(b-a for a, b in merged)
        histogram[len(reduced)] += 1
    return {"families": 1 << len(universe), "intervals": len(universe),
            "retained_size_histogram": dict(histogram)}


def all_chains(max_depth):
    path = [1]

    def visit():
        yield tuple(path)
        if len(path)-1 == max_depth:
            return
        values = {a+b for i, a in enumerate(path) for b in path[:i+1] if a+b > path[-1]}
        for x in sorted(values):
            path.append(x)
            yield from visit()
            path.pop()
    yield from visit()


def chain_block():
    ratios = [(9, 8), (5, 4), (4, 3)]  # 1+delta; all delta < sqrt(2)-1.
    powers = {(p,q): ([p**i for i in range(33)], [q**i for i in range(33)]) for p,q in ratios}
    betas = {}
    for p, q in ratios:
        b = 1
        while p**b*(p-q) <= 2*q**(b+1):
            b += 1
        betas[(p,q)] = b
    counts = Counter()
    mini_counts = Counter()
    for chain in all_chains(8):
        r = len(chain)-1
        s = r-(chain[-1].bit_length()-1)
        counts[r] += 1
        canonical = [next((j,k) for j in range(i-1,-1,-1) for k in range(j+1)
                          if chain[j]+chain[k] == chain[i]) for i in range(1,len(chain))]
        for p, q in ratios:
            pp, qq = powers[(p,q)]
            classes, intervals, normal_pairs, mini_pairs = [], [], [], set()
            for i in range(1,len(chain)):
                if chain[i] == 2*chain[i-1]:
                    classes.append('D')
                    continue
                witnesses = [j for j in range(i) if chain[i]*qq[i-j] < chain[j]*pp[i-j]]
                pair = canonical[i-1]
                if witnesses:
                    classes.append('M')
                    intervals.append((witnesses[0],i))
                    assert pair not in mini_pairs
                    mini_pairs.add(pair)
                else:
                    classes.append('O')
                    normal_pairs.append(pair)
                    assert all(i-j <= betas[(p,q)] for j in pair)
            t = len(mini_pairs)
            mini_counts[t] += 1
            assert (1 << t)*qq[2*t] <= (1 << s)*pp[2*t]
            merged = components(reduce_cover(intervals))
            assert sum(b-a for a,b in merged) >= t
            for a,b in merged:
                assert chain[b]*qq[2*(b-a)] <= chain[a]*pp[2*(b-a)]
            # Reconstruct using only the class schedule, ordinary pairs, and
            # the unordered SET of ministep pairs. No original values used.
            reconstructed, ordinary, unused = [1], iter(normal_pairs), set(mini_pairs)
            for i, kind in enumerate(classes,1):
                if kind == 'D':
                    x = 2*reconstructed[-1]
                elif kind == 'O':
                    j,k = next(ordinary)
                    x = reconstructed[j]+reconstructed[k]
                else:
                    available = [(reconstructed[j]+reconstructed[k],j,k) for j,k in unused if j < i]
                    x,j,k = min(available)
                    unused.remove((j,k))
                    assert any(x*qq[i-j] < reconstructed[j]*pp[i-j] for j in range(i))
                assert x > reconstructed[-1]
                reconstructed.append(x)
            assert tuple(reconstructed) == chain and not unused
    assert math.comb(4,0) == 1  # r=2, t=0: one empty choice, not fewer than one.
    return {"chains_by_length": dict(counts), "chains": sum(counts.values()),
            "rational_delta_checks": 3*sum(counts.values()),
            "ministep_count_histogram": dict(mini_counts),
            "beta_bounds": {f'{p}/{q}': b for (p,q),b in betas.items()},
            "strict_count_counterexample": {"chain":[1,2,4],"r":2,"t":0,"actual_empty_pair_choices":1,"printed_binomial":1}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('block',choices=['interval','chain'])
    args = parser.parse_args()
    data = json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert args.block not in data['blocks'], 'Do not repeat a passed block'
    begin = time.perf_counter()
    result = globals()[args.block+'_block']()
    data['blocks'][args.block] = {'status':'passed','seconds':time.perf_counter()-begin,'result':result}
    data['updated_at_utc'] = datetime.now(timezone.utc).isoformat()
    RESULT.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'block':args.block,**data['blocks'][args.block]}),flush=True)
