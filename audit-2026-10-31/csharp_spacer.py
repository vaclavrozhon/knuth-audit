"""Audit interpreter for the C$ changes on printed pp. 117--118 and 247--248.

Uses the already audited spacer input representation, with new thresholded
operations. Python integers avoid implementation-specific overflow. This is
an independent model of the book, not another invocation of native DLX5.
"""
from collections import Counter
from heapq import heapreplace
from math import inf
from colored_dlx import ColoredDLX


class CostDLX(ColoredDLX):
    def __init__(self, n, primary, rows, prices):
        super().__init__(n, primary, rows)
        assert len(prices) == len(rows) and all(c >= 0 for c in prices)
        self.original_prices = list(prices)
        self.prices = list(prices)
        self.taxes = [0] * (n + 1)
        self.unsat = False
        self.stats = Counter()
        self.undo_stack = []
        # Answer 247: one greedy pass over primary items only.
        for i in range(1, primary + 1):
            owners = [r for r, row in enumerate(rows) if i in dict(row)]
            if not owners:
                self.unsat = True
                return
            tax = min(self.prices[r] for r in owners)
            self.taxes[i] = tax
            for r in owners:
                self.prices[r] -= tax
        self.W = [0] * len(self.T)
        for i in range(1, n + 1):
            self.W[i] = self.taxes[i]
        for p, ri in self.owner.items():
            self.W[p] = self.prices[ri]
        # Global option order induces each item's order, as in answer 247.
        for i in range(1, n + 1):
            nodes = sorted((p for p in self.owner if self.T[p] == i),
                           key=lambda p: (self.W[p], self.owner[p]))
            cycle = [i] + nodes
            for k, p in enumerate(cycle):
                self.U[p], self.D[p] = cycle[k-1], cycle[(k+1) % len(cycle)]
            if i <= primary:
                assert self.W[self.D[i]] == 0
        assert min(self.prices, default=0) >= 0

    def memory(self):
        out = self.snapshot()
        # Header colors are diagnostic caches, not decision state.
        out['C'][1:self.n+1] = [None] * self.n
        return out

    def pair_start(self, kind, p, threshold, undo):
        if undo:
            q = self.undo_stack.pop()
            assert q[:3] == (kind, p, threshold)
            self.stats['cutoff_decreased_before_undo'] += self.cutoff < q[4]
            return q[3]
        self.undo_stack.append((kind, p, threshold, self.memory(), self.cutoff))

    def pair_end(self, kind, before, undo):
        if undo:
            assert self.memory() == before, kind
            self.stats[kind + '_exact_restorations'] += 1

    def hide_cost(self, p, undo):
        # Both directions now go left to right, including the spacer wrap.
        q = p + 1
        while q != p:
            if self.C[q] < 0:
                self.stats['negative_color_nodes_skipped'] += 1
                q += 1
                continue
            x, u, d = self.T[q], self.U[q], self.D[q]
            if x <= 0:
                q = u
            else:
                self.D[u], self.U[d] = (q, q) if undo else (d, u)
                self.T[x] += 1 if undo else -1
                q += 1

    def cover_cost(self, i, threshold, undo=False):
        before = self.pair_start('cover', i, threshold, undo)
        p = self.D[i]
        while p != i and self.W[p] < threshold:
            self.hide_cost(p, undo)
            p = self.D[p]
        self.stats['cover_stopped_at_cost'] += p != i
        l, r = self.L[i], self.R[i]
        self.R[l], self.L[r] = (i, i) if undo else (r, l)
        self.pair_end('cover', before, undo)

    def purify_cost(self, p, threshold, undo=False):
        before = self.pair_start('purify', p, threshold, undo)
        c, i = self.C[p], self.T[p]
        assert c > 0
        if not undo:
            self.C[i] = c
        q = self.D[i]
        while q != i and self.W[q] < threshold:
            if (self.C[q] < 0) if undo else (self.C[q] == c):
                self.C[q] = c if undo else -1
            else:
                self.hide_cost(q, undo)
            q = self.D[q]
        self.stats['purify_stopped_at_cost'] += q != i
        self.pair_end('purify', before, undo)

    def commit_cost(self, p, threshold, undo=False):
        if self.C[p] == 0:
            self.cover_cost(self.T[p], threshold, undo)
        elif self.C[p] > 0:
            self.purify_cost(p, threshold, undo)

    def choose(self, theta, lookahead):
        """Literal answer 248, operating directly on spacer pointers."""
        t, c, j, chosen = inf, 0, self.R[0], None
        while j > 0:
            p = self.D[j]
            cp = self.W[p]
            if p == j or cp >= theta:
                self.stats['C3_backtrack'] += 1
                return None
            s, p = 1, self.D[p]
            while True:
                if p == j or self.W[p] >= theta:
                    break
                if s == t:
                    s += 1
                    break
                if s >= lookahead:
                    s = self.T[j]
                    self.stats['LEN_estimate'] += 1
                    break
                s, p = s + 1, self.D[p]
            if s < t or (s == t and c < cp):
                t, chosen, c = s, j, cp
            j = self.R[j]
        return chosen

    def solve_cost(self, k, lookahead=10):
        assert k > 0 and lookahead > 0
        self.accepted = []
        self.heap = [-inf] * k
        self.cutoff = inf
        if self.unsat:
            return self
        initial = self.memory()
        chosen = []

        def visit(cost):
            self.stats['nodes'] += 1
            if self.R[0] == 0:
                assert cost < self.cutoff
                model = tuple(sorted(self.owner[p] for p in chosen))
                self.accepted.append((model, cost + sum(self.taxes)))
                heapreplace(self.heap, -cost)
                self.cutoff = -self.heap[0]
                return
            i = self.choose(self.cutoff - cost, lookahead)
            if i is None:
                return
            x = self.D[i]
            th0 = self.cutoff - cost - self.W[x]
            assert th0 > 0
            self.cover_cost(i, th0)
            while x != i:
                threshold = self.cutoff - cost - self.W[x]
                if threshold <= 0:
                    self.stats['C5_cutoff'] += 1
                    break
                self.stats['chosen_row_not_hidden_by_C4'] += self.W[x] >= th0
                p = x + 1
                while p != x:
                    if self.T[p] <= 0:
                        p = self.U[p]
                    else:
                        self.commit_cost(p, threshold)
                        p += 1
                chosen.append(x)
                visit(cost + self.W[x])
                chosen.pop()
                p = x - 1
                while p != x:
                    if self.T[p] <= 0:
                        p = self.D[p]
                    else:
                        self.commit_cost(p, threshold, True)
                        p -= 1
                x = self.D[x]
            self.cover_cost(i, th0, True)

        visit(0)
        assert not self.undo_stack and self.memory() == initial
        return self

    def best_costs(self):
        return sorted(-c + sum(self.taxes) for c in self.heap if c != -inf)
