"""Finite independent checks for TAOCP 1 section 2.3.3, excluding polynomials.

Trees are tuples of their children; a forest is a tuple of trees. This model
does not contain links. Linked representations are constructed separately.
The general arguments and source qualifications are in the audit notes.
"""

from collections import deque
from functools import lru_cache
from itertools import product, permutations
from pathlib import Path
import json
import random


@lru_cache(None)
def forests(n):
    if n == 0:
        return ((),)
    return tuple((children,) + tail for k in range(1, n + 1)
                 for children in forests(k - 1) for tail in forests(n - k))


def tables(forest):
    children, parent, post = {0: []}, {}, []

    def visit(tree, p):
        i = len(parent) + 1
        parent[i] = p
        children[p].append(i)
        children[i] = []
        for child in tree:
            visit(child, i)
        post.append(i)

    for t in forest:
        visit(t, 0)
    right = {i: 0 for i in parent}
    for row in children.values():
        for i, j in zip(row, row[1:]):
            right[i] = j
    return children, parent, post, right


def postorder_18(info, right):
    """Literal P1-P5 with the published INFO -> INFO1 correction."""
    n = len(info)
    r, d, items = [n + 1], [0], []
    j, out, degree = 0, [], []
    step = 2
    while True:
        if step == 2:
            step = 5 if r[-1] > j + 1 else 3
        elif step == 3:
            if not items:
                assert len(out) == n and r == [n + 1] and len(d) == 1
                return out, degree
            i = items.pop()
            out.append(info[i - 1])
            degree.append(d.pop())
            step = 4
        elif step == 4:
            if not right[i]:
                step = 3
            else:
                assert r.pop() == right[i]
                step = 5
        else:
            d[-1] += 1
            j += 1
            items.append(j)
            d.append(0)
            if right[j]:
                r.append(right[j])
            step = 2


def valid_desc(d):
    n = len(d)
    return all(0 <= x <= n - i - 1
               and all(j + d[j] <= i + x for j in range(i, i + x + 1))
               for i, x in enumerate(d))


def from_desc(d):
    """The constructive converse of exercise 19, using subtree intervals."""
    assert valid_desc(d)

    def block(first, stop):
        out = []
        while first < stop:
            end = first + d[first] + 1
            assert end <= stop
            out.append(block(first + 1, end))
            first = end
        return tuple(out)

    return block(0, len(d))


def check_forests():
    count = meets = conversions = parent_orders = sequences = 0
    by_n = {}
    for n in range(10):
        descs = set()
        for f in forests(n):
            count += 1
            ch, par, post, right = tables(f)
            ids = list(range(1, n + 1))
            degree = {i: len(ch[i]) for i in ids}
            descendant = {}
            values = {}
            for i in post:
                descendant[i] = sum(1 + descendant[j] for j in ch[i])
                values[i] = (i, tuple(values[j] for j in ch[i]))
            d = tuple(descendant[i] for i in ids)
            assert valid_desc(d) and from_desc(d) == f
            descs.add(d)
            positions = {i: k for k, i in enumerate(post)}
            for i in ids:
                assert descendant[i] == sum(j > i for j in post[:positions[i]])
            c = [descendant[i] for i in post]
            assert all(0 <= x <= k and all(j - c[j] >= k - x
                       for j in range(k - x, k + 1)) for k, x in enumerate(c))

            # LTAG from the targets of actual RLINKs; then RLINK from two tags.
            targets = set(right.values()) - {0}
            terminal = {i: i == n or i + 1 in targets for i in ids}
            assert all(terminal[i] == (not ch[i]) for i in ids)
            pending, rebuilt = [], {i: 0 for i in ids}
            for i in ids:
                if right[i]:
                    pending.append(i)
                if terminal[i] and pending:
                    rebuilt[pending.pop()] = i + 1
            assert not pending and rebuilt == right

            # Level-order LLINK from the two tags. Whole families are queued.
            level, queue = [], deque(ch[0])
            while queue:
                i = queue.popleft()
                level.append(i)
                queue.extend(ch[i])
            first_child, queue = {i: 0 for i in ids}, deque()
            for k, i in enumerate(level):
                if ch[i]:
                    queue.append(i)
                if not right[i] and queue:
                    first_child[queue.popleft()] = level[k + 1]
            assert not queue
            assert first_child == {i: ch[i][0] if ch[i] else 0 for i in ids}

            # F and exercise 2: an order-sensitive, symbolic local function.
            stack = []
            for i in post:
                k = degree[i]
                sub = stack[-k:] if k else []
                if k:
                    del stack[-k:]
                stack.append((i, tuple(sub)))
            assert stack == [values[i] for i in ch[0]]
            stack = []
            for i in reversed(ids):
                sub = [stack.pop() for _ in ch[i]]
                stack.append((i, tuple(sub)))
            assert stack[::-1] == [values[i] for i in ch[0]]

            # G on each tree: path to the node is sensitive to every parent.
            for root in ch[0]:
                block = [i for i in post if root <= i <= root + descendant[root]]
                stack, paths = [], {}
                for k, i in enumerate(reversed(block)):
                    path = () if not k else stack.pop()
                    paths[i] = path + (i,)
                    stack.extend([paths[i]] * degree[i])
                    if par[i]:
                        assert paths[i][:-1] == paths[par[i]]
                assert not stack

            # P1-P5, against the link-free recursive representation.
            actual, degrees = postorder_18(ids, right)
            assert actual == post and degrees == [degree[i] for i in post]
            conversions += 1

            # Exercise 6: original list order need not respect ancestors.
            orders = permutations(ids) if n <= 4 else [ids, ids[::-1]]
            for order in orders:
                order = list(order)
                link = {i: order[k + 1] if k + 1 < n else 0
                        for k, i in enumerate(order)}
                left = {i: 0 for i in ids}
                p, first = (order[0] if order else 0), 0
                while p:
                    q = link[p]
                    if par[p]:
                        link[p], left[par[p]] = left[par[p]], p
                    else:
                        link[p], first = first, p
                    p = q
                out = {}
                for i in [0] + ids:
                    p = left[i] if i else first
                    row = []
                    while p:
                        assert p not in row
                        row.append(p)
                        p = link[p]
                    out[i] = row
                assert all(sorted(out[i]) == sorted(ch[i]) for i in out)
                parent_orders += 1
        by_n[n] = len(descs)
        if n <= 6:
            # Test necessity and sufficiency on all bounded integer sequences,
            # not merely on representations already known to be valid.
            for d in product(*(range(n - k) for k in range(n))):
                sequences += 1
                assert valid_desc(d) == (d in descs)
            for d in descs:
                for e in descs:
                    assert tuple(min(a, b) for a, b in zip(d, e)) in descs
                    meets += 1
    return dict(forests=count, by_size=by_n, conversions=conversions,
                parent_list_orders=parent_orders, bounded_sequences=sequences,
                componentwise_meets=meets)


class Union:
    def __init__(self, n, weighted=False):
        self.parent = [-1 if weighted else 0 for _ in range(n)]
        self.weighted = weighted
        self.walks = 0

    def root(self, i):
        while self.parent[i] > 0:
            i = self.parent[i] - 1
            self.walks += 1
        return i

    def join(self, i, j):
        i, j = self.root(i), self.root(j)
        if i == j:
            return
        if self.weighted:
            if -self.parent[i] > -self.parent[j]:
                i, j = j, i
            self.parent[j] += self.parent[i]
        self.parent[i] = j + 1


class WeightedOffsets:
    """Literal answer 11: child coordinate t equals parent coordinate t+delta."""
    def __init__(self, bounds):
        self.parent = list(range(len(bounds)))
        self.delta = [0] * len(bounds)
        self.lo = [a for a, _ in bounds]
        self.hi = [b for _, b in bounds]

    def locate(self, p, j=0):
        while self.parent[p] != p:
            j += self.delta[p]
            p = self.parent[p]
        return p, j

    def add(self, p, j, q, k):
        p, j = self.locate(p, j)
        q, k = self.locate(q, k)
        if p == q:
            return j == k
        self.parent[q], self.delta[q] = p, j - k
        self.lo[p] = min(self.lo[p], self.lo[q] + j - k)
        self.hi[p] = max(self.hi[p], self.hi[q] + j - k)
        return True


def graph_offsets(n, edges):
    """Independent graph propagation of coordinate offsets; None = contradiction."""
    g = [[] for _ in range(n)]
    for p, j, q, k in edges:
        g[p].append((q, j - k))
        g[q].append((p, k - j))
    component, offset = {}, {}
    for start in range(n):
        if start in component:
            continue
        component[start], offset[start], pending = start, 0, [start]
        while pending:
            p = pending.pop()
            for q, delta in g[p]:
                if q in offset:
                    if offset[q] != offset[p] + delta:
                        return None
                else:
                    component[q] = start
                    offset[q] = offset[p] + delta
                    pending.append(q)
    return component, offset


def check_equivalence():
    unweighted_steps = weighted_steps = 0
    rng = random.Random(233)
    for n in range(1, 33):
        for _ in range(40):
            unions = [Union(n), Union(n, True)]
            labels = list(range(n))
            for _ in range(3 * n):
                i, j = rng.randrange(n), rng.randrange(n)
                a, b = labels[i], labels[j]
                labels = [b if x == a else x for x in labels]
                for u in unions:
                    u.join(i, j)
                    roots = [u.root(k) for k in range(n)]
                    assert all((roots[x] == roots[y]) == (labels[x] == labels[y])
                               for x in range(n) for y in range(n))
                unweighted_steps += 1
            u = unions[1]
            for k in range(n):
                start = u.walks
                r = u.root(k)
                depth = u.walks - start
                assert 2 ** depth <= -u.parent[r]
    for n in range(1, 17):
        for _ in range(40):
            bounds = [(rng.randint(-8, 0), rng.randint(0, 8)) for _ in range(n)]
            u, edges = WeightedOffsets(bounds), []
            for _ in range(3 * n):
                edge = (rng.randrange(n), rng.randint(-12, 12),
                        rng.randrange(n), rng.randint(-12, 12))
                independent = graph_offsets(n, edges + [edge])
                assert u.add(*edge) == (independent is not None)
                if independent is not None:
                    edges.append(edge)
                component, offsets = graph_offsets(n, edges)
                loc = [u.locate(i) for i in range(n)]
                for i in range(n):
                    r, off = loc[i]
                    group = [j for j in range(n) if component[j] == component[i]]
                    assert sorted(j for j in range(n) if loc[j][0] == r) == group
                    assert all(loc[j][1] - off == offsets[j] - offsets[i] for j in group)
                    assert u.lo[r] == min(bounds[j][0] + loc[j][1] for j in group)
                    assert u.hi[r] == max(bounds[j][1] + loc[j][1] for j in group)
                weighted_steps += 1
    u = WeightedOffsets([(0, 10), (3, 10), (1, 1), (-2, 0)])
    for edge in [(0, 7, 1, 3), (3, 0, 2, 0), (1, 1, 2, 8)]:
        assert u.add(*edge)
    assert u.lo[0] == -5 and u.hi[0] == 14
    v = Union(9)
    for a, b in [(1, 5), (6, 8), (7, 2), (9, 8), (3, 7), (4, 2), (9, 3)]:
        v.join(a - 1, b - 1)
    assert v.parent == [5, 0, 2, 2, 0, 8, 2, 2, 8]
    return dict(union_steps=unweighted_steps, weighted_offset_steps=weighted_steps,
                book_array_bounds=[-5, 14], book_parent=v.parent)


if __name__ == '__main__':
    result = {'status': 'pass', 'forests': check_forests(),
              'equivalence': check_equivalence(),
              'limits': 'Finite checks supplement general proofs; no historical attribution is inferred.'}
    p = Path(__file__).parent / 'results/other-trees.json'
    p.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))
