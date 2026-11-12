#!/usr/bin/env python3
"""DLX37–38: literal mex recurrence, independent greedy queens, Algorithm G."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json

from dlx1_audit_tools import ROOT, sha

OUT = ROOT/'results/greedy_queens'
PREFIX = [1, 3, 5, 2, 4, 9, 11, 13, 15, 6, 8, 19, 7, 22, 10, 25,
          27, 29, 31, 12, 14, 35, 37, 39, 41, 16, 18, 45]


def mex(values):
    answer = 0
    while answer in values:
        answer += 1
    return answer


def literal_array(limit):
    a = {}
    for total in range(2, limit+1):
        for j in range(1, total):
            i = total-j
            forbidden = {0}
            for k in range(1, max(i, j)+1):
                for x, y in [(i, j-k), (i-k, j), (i-k, j-k), (i+k, j-k)]:
                    if x > 0 and y > 0:
                        assert (x, y) in a, (i, j, x, y)
                        forbidden.add(a[x, y])
            a[i, j] = mex(forbidden)
    return a


def four_line_array(limit):
    lines = [defaultdict(set) for _ in range(4)]
    a = {}
    for total in range(2, limit+1):
        for j in range(1, total):
            i = total-j
            keys = [i, j, i-j, i+j]
            value = mex({0}.union(*(lines[h][key] for h, key in enumerate(keys))))
            a[i, j] = value
            for h, key in enumerate(keys):
                assert value not in lines[h][key]
                lines[h][key].add(value)
    return a


def direct_greedy(count):
    """Definition only: try every positive row; no G frontier bounds."""
    rows, plus, minus = set(), set(), set()
    q = []
    for n in range(1, count+1):
        k = 1
        while k in rows or k+n in plus or k-n in minus:
            k += 1
        rows.add(k); plus.add(k+n); minus.add(k-n)
        q.append(k)
    return q


def algorithm_g(count):
    a, b, c = set(), set(), set()
    r, s, t = 0, 1, 0
    q, histogram = [], Counter()
    for n in range(1, count+1):
        if n <= 250:
            assert len(a) == len(b) == len(c) == n-1
            assert all(k in a for k in range(1, s)) and s not in a
            assert all(k in c for k in range(1-r, t+1))
            assert -r not in c and t+1 not in c
        k = s
        reads = 0
        while k <= n-r:
            # The book's equality test permits this order. It matches the
            # author's infty-queens source for the empirical access statistic.
            reads += 1
            if k+n not in b:
                reads += 1
                if k-n not in c:
                    reads += 1
                    if k not in a:
                        break
            k += 1
        if k > n-r:
            t += 1
            k = n+t
            assert k not in a and k+n not in b and t not in c
            a.add(k); b.add(k+n); c.add(t)
        else:
            a.add(k); b.add(k+n); c.add(k-n)
            if k == s:
                while True:
                    s += 1
                    reads += 1
                    if s not in a:
                        break
            if k == n-r:
                while True:
                    r += 1
                    reads += 1
                    if -r not in c:
                        break
        histogram[reads+3] += 1  # exactly three bit writes
        q.append(k)
    return q, histogram


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    a = literal_array(160)
    assert a == four_line_array(160)
    q = direct_greedy(10000)
    actual, histogram = algorithm_g(10000)
    assert actual == q
    assert q[:len(PREFIX)] == PREFIX
    matches = 0
    for j, value in enumerate(q, 1):
        if j+value <= 160:
            assert a[value, j] == 1
            matches += 1
    assert a[2, 3] == 5 and a[3, 2] == 1 and q[1] == 3
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), mex_cells=len(a),
                  mex_algorithms='Literal four-set recurrence and independent four-line color sets',
                  greedy_terms=len(q), book_prefix=PREFIX,
                  corrected_index_checks=matches,
                  counterexample={'i': 2, 'q_i': 3, 'a_i_qi': 5, 'a_qi_i': 1,
                                  'top_left_4x4': [[a[i, j] for j in range(1, 5)]
                                                   for i in range(1, 5)]},
                  bit_accesses={'histogram': dict(sorted(histogram.items())),
                                'max': max(histogram),
                                'average': sum(k*v for k, v in histogram.items())/len(q)},
                  finding='F111: answer37(a) needs a[q_i,i]=1, not a[i,q_i]=1.',
                  scope='Exact finite checks supplement the general proofs in GREEDY_QUEENS_NOTES.md; '
                        'the 2026 external computer-assisted theorem is not independently certified here.')
    (OUT/'small.json').write_text(json.dumps(result, indent=2)+'\n')
    (OUT/'first-10000.json').write_text(json.dumps(q)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
