"""Audit interpreter for the color-threshold extension in answer DLX122.

Uses the previously validated literal spacer primitives, with new search code.
Secondary CTH entries are undo caches, not restored values. Primary CTH values
are supplied explicitly; the default zero is the ordinary color-only action.
"""
from collections import Counter
from colored_dlx import ColoredDLX


class _NoEvents:
    def append(self, value):
        pass


class SymmetryDLX(ColoredDLX):
    def __init__(self, n, primary, rows, *, v=1, thresholds=None, trace=False):
        super().__init__(n, primary, rows)
        self.v = self.theta = v
        self.cth = [0] * (n + 1)
        for i, value in (thresholds or {}).items():
            assert 1 <= i <= primary
            self.cth[i] = value
        self.trace = trace
        if not trace:
            self.events = _NoEvents()

    def purify(self, p, undo=False):
        i, c = self.T[p], self.C[p]
        if undo:
            self.theta = self.cth[i]
        else:
            self.cth[i] = self.theta
            if c == self.theta:
                self.theta += 1
        super().purify(p, undo)

    def solve(self, *, mrv=True, collect=True, check_each_node=False):
        before = self.snapshot()
        self.solutions, self.count, self.profile = set(), 0, Counter()
        self.rejections = Counter()
        chosen = []

        def visit(depth):
            saved_theta = self.theta
            saved = self.snapshot() if check_each_node else None
            self.profile[depth] += 1
            if self.R[0] == 0:
                self.count += 1
                if collect:
                    model = tuple(sorted(self.owner[q] for q in chosen))
                    assert model not in self.solutions
                    self.solutions.add(model)
                return
            active = []
            i = self.R[0]
            while i:
                if self.cth[i] <= self.theta:
                    active.append(i)
                i = self.R[i]
            if not active:
                self.rejections['no_eligible_primary'] += 1
                return
            i = min(active, key=lambda x: self.T[x]) if mrv else active[0]
            self.events.append(('choose', depth, i, self.theta))
            self.cover(i)
            x = self.D[i]
            while x != i:
                self.events.append(('try', depth, x, self.theta))
                committed = []
                p = x + 1
                while p != x:
                    if self.T[p] <= 0:
                        p = self.U[p]
                        continue
                    if self.C[p] > self.theta:
                        self.rejections[len(committed)] += 1
                        self.events.append(('reject', p, self.C[p], self.theta))
                        break
                    self.commit(p)
                    committed.append(p)
                    p += 1
                else:
                    chosen.append(x)
                    visit(depth + 1)
                    chosen.pop()
                # Exactly the already committed prefix, in reverse order.
                # In the native variant this is the book's jump into C6.
                for p in reversed(committed):
                    self.commit(p, True)
                assert self.theta == saved_theta
                x = self.D[x]
            self.cover(i, True)
            if saved is not None:
                after = self.snapshot()
                saved['C'][1:self.n+1] = after['C'][1:self.n+1]
                assert saved == after

        visit(0)
        after = self.snapshot()
        before['C'][1:self.n+1] = after['C'][1:self.n+1]
        assert before == after
        assert self.theta == self.v
        return self


def toy(m, n):
    return [((k, 0), (n+k, c)) for k in range(1, n+1)
            for c in range(1, m+1)]


def canonical_model(model, rows, v=1):
    """Independent orbit key: minimize a colored set of sets over renamings.

    First appearance is in a fixed global item order, not the solver's input
    node order. Labels below v and every uncolored item are held fixed.
    """
    from itertools import permutations
    colors = sorted({c for r in model for _, c in rows[r] if c >= v})
    best = None
    for target in permutations(range(v, v+len(colors))):
        renaming = dict(zip(colors, target))
        value = tuple(sorted(tuple(sorted((i, renaming.get(c, c))
                                          for i, c in rows[r])) for r in model))
        best = value if best is None or value < best else best
    return best
