"""TAOCP 3.4.1-24: complete, independently validated fixed-point graphs.

The grid contains k/2**b for 0 <= k <= 2**b, including both endpoints.
Each product is exact before a single floor or ties-to-even rounding.
This is NOT a model of floating-point intermediate rounding.
"""
from pathlib import Path
import json
import math
import sys
import time
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/logistic-fixed.json'


def cdf_distance(values, weights):
    order = np.argsort(values)
    values, weights = values[order], weights[order]
    right = np.cumsum(weights)
    left = right - weights
    target = 2 / math.pi * np.arcsin(np.sqrt(values))
    return float(max(np.max(right - target), np.max(target - left)))


def census(b, mode):
    n = 1 << b
    k = np.arange(n + 1, dtype=np.int64)
    numerator = 4 * k * (n - k)
    q, r = numerator // n, numerator % n
    if mode == 'floor':
        nxt = q
    else:
        nxt = q + ((2 * r > n) | ((2 * r == n) & ((q & 1) != 0)))
    # Independent algebra: 4*k*(N-k)/N = N - (2*k-N)**2/N.
    square = (2 * k - n) ** 2
    if mode == 'floor':
        alternative = n - (square + n - 1) // n
    else:
        q2, r2 = square // n, square % n
        alternative = n - q2 - ((2*r2 > n) | ((2*r2 == n) & ((q2 & 1) != 0)))
    assert np.array_equal(nxt, alternative)
    assert np.array_equal(nxt, nxt[::-1])
    assert nxt[0] == nxt[n] == 0 and nxt[n//2] == n
    assert nxt[3*n//4] == 3*n//4

    indegree = np.bincount(nxt, minlength=n+1).astype(np.int32)
    queue = np.empty(n+1, dtype=np.int32)
    zero = np.flatnonzero(indegree == 0)
    tail = len(zero)
    queue[:tail] = zero
    for head in range(n+1):
        if head == tail:
            break
        j = nxt[queue[head]]
        indegree[j] -= 1
        if indegree[j] == 0:
            queue[tail] = j
            tail += 1

    component = np.full(n+1, -1, dtype=np.int32)
    depth = np.zeros(n+1, dtype=np.int32)
    cycles = []
    for start in np.flatnonzero(indegree > 0):
        if component[start] >= 0:
            continue
        cycle = []
        j = int(start)
        while component[j] < 0:
            component[j] = len(cycles)
            cycle.append(j)
            j = int(nxt[j])
        assert j == start and min(cycle) == start
        cycles.append(cycle)
    for pos in range(tail-1, -1, -1):
        j = queue[pos]
        component[j] = component[nxt[j]]
        depth[j] = depth[nxt[j]] + 1

    # Independent all-state certificate checks, not a second pruning run.
    # Strictly decreasing depth proves every off-cycle state reaches its label.
    assert np.all(component >= 0)
    assert np.array_equal(component, component[alternative])
    off = depth > 0
    assert np.array_equal(depth[off], depth[alternative[off]] + 1)
    assert np.count_nonzero(~off) == sum(map(len, cycles))
    seen = set()
    for cid, cyc in enumerate(cycles):
        assert len(cyc) == len(set(cyc))
        assert not seen.intersection(cyc)
        seen.update(cyc)
        for j, after in zip(cyc, cyc[1:]+cyc[:1]):
            assert int(alternative[j]) == after and component[j] == cid and depth[j] == 0
    basins = np.bincount(component, minlength=len(cycles))
    assert sum(basins) == n+1
    maximum_depth = np.zeros(len(cycles), dtype=np.int32)
    np.maximum.at(maximum_depth, component, depth)
    allvalues, allweights, rows = [], [], []
    for cid, cyc in enumerate(cycles):
        values = np.array(cyc, dtype=np.float64) / n
        basin = int(basins[cid])
        allvalues.extend(values)
        allweights.extend([basin / ((n+1)*len(cyc))] * len(cyc))
        rows.append(dict(states=cyc, period=len(cyc), basin=basin,
                         max_transient=int(maximum_depth[cid]),
                         mean=float(np.mean(values)), second_moment=float(np.mean(values**2)),
                         cdf_distance=cdf_distance(values, np.full(len(cyc), 1/len(cyc)))))
    return dict(bits=b, rounding=mode, states=n+1, edges_validated=n+1,
                cycles=rows, maximum_transient=int(np.max(depth)),
                uniform_seed_stationary_cdf_distance=cdf_distance(np.array(allvalues), np.array(allweights)),
                scope='Complete fixed-point graph; CDF distances are floating-point descriptive statistics.')


def main():
    result = json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for b in range(2, 21):
        for mode in ['floor', 'nearest_even']:
            key = f'{b}_{mode}'
            if key in result:
                continue
            before = time.monotonic()
            row = census(b, mode)
            row['elapsed_seconds'] = time.monotonic() - before
            result[key] = row
            OUT.write_text(json.dumps(result, indent=2)+'\n')
            print('PASS', key, 'states', row['states'], 'cycles', len(row['cycles']),
                  'max_period', max(c['period'] for c in row['cycles']), flush=True)


if __name__ == '__main__':
    main()
