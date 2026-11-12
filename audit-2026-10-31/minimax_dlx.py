"""Literal ordered-list cutoff variants in answers DLX84 and DLX85.

Memory layout and ordinary Algorithm C are inherited from colored_dlx.
All model row numbers returned here are zero-based; book option ranks are +1.
"""
from collections import Counter
from colored_dlx import ColoredDLX


class MinimaxDLX(ColoredDLX):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cutoff = len(self.T)
        self.cut_events = []
        self.repaired_successors = 0

    def trim(self, i):
        p = self.U[i]
        while p > self.cutoff:
            self.T[i] -= 1
            p = self.U[p]
        self.U[i], self.D[p] = p, i

    def hide(self, p, undo=False):
        if not undo:
            return super().hide(p)
        q = p-1
        while q != p:
            if self.C[q] < 0:
                q -= 1
                continue
            x, u, d = self.T[q], self.U[q], self.D[q]
            if x <= 0:
                q = d
            else:
                if d > self.cutoff:
                    self.D[q] = d = x
                    self.repaired_successors += 1
                self.D[u], self.U[d] = q, q
                self.T[x] += 1
                q -= 1

    def cover(self, i, undo=False):
        if undo:
            self.trim(i)
        return super().cover(i, undo)

    def purify(self, p, undo=False):
        if undo:
            self.trim(self.T[p])
        return super().purify(p, undo)

    def check_live(self):
        """Check every active primary and every eligible reachable column entry."""
        active = []
        i = self.R[0]
        while i:
            assert i not in active and self.L[self.R[i]] == i
            active.append(i)
            i = self.R[i]
        for i in active:
            nodes = []
            p = self.D[i]
            while p != i:
                assert p not in nodes and p <= self.cutoff, (i, p, self.cutoff)
                assert self.T[p] == i and self.D[self.U[p]] == p and self.U[self.D[p]] == p
                nodes.append(p)
                p = self.D[p]
            assert nodes == sorted(nodes) and len(nodes) == self.T[i]

    def solve_minimax(self, *, one=False, mrv=True):
        self.solutions, self.profile = set(), Counter()
        chosen = []
        self.incumbents = []

        def visit(depth):
            self.check_live()
            self.profile[depth] += 1
            if self.R[0] == 0:
                # The empty problem is handled explicitly: max(empty)=0 by convention.
                model = tuple(sorted(self.owner[q] for q in chosen))
                if not chosen:
                    self.solutions = {model}
                    return None
                k = max(range(depth), key=lambda t: chosen[t])
                x = chosen[k]
                end = self.ends[x]+1
                start = self.U[end]
                cutoff = start-1 if one else end
                assert cutoff <= self.cutoff
                if cutoff != self.cutoff:
                    self.cutoff = cutoff
                    self.solutions.clear()
                    self.cut_events.append(dict(depth=depth, k=k, node=x,
                                               cutoff=cutoff, option=self.owner[x]+1))
                    for node in chosen:
                        self.trim(self.T[node])
                self.solutions.add(model)
                self.incumbents.append(model)
                return k if one else None
            active = []
            i = self.R[0]
            while i:
                active.append(i)
                i = self.R[i]
            i = min(active, key=lambda j: self.T[j]) if mrv else active[0]
            self.cover(i)
            x = self.D[i]
            while x != i:
                p = x+1
                while p != x:
                    if self.T[p] <= 0:
                        p = self.U[p]
                    else:
                        self.commit(p)
                        p += 1
                chosen.append(x)
                jump = visit(depth+1)
                chosen.pop()
                p = x-1
                while p != x:
                    if self.T[p] <= 0:
                        p = self.D[p]
                    else:
                        self.commit(p, True)
                        p -= 1
                if jump is not None and depth >= jump:
                    self.cover(i, True)
                    return jump
                x = self.D[x]
            self.cover(i, True)
            return None

        visit(0)
        self.check_live()
        return self
