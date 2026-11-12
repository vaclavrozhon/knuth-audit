"""Small measured DLX implementation for independently checking book formulas.

An update is one deletion from a doubly linked list: one for a covered item
header, and one for every hidden option node. Restoring links does not count.
All items are primary. Nonempty options only. Columns keep their supplied order;
MRV ties use that order. A zero-length chosen column is still covered (X4).
Horizontal option links replace Knuth's spacer layout but delete the same nodes.
"""
from collections import Counter


class DLX:
    def __init__(self, items, options):
        self.items = list(items)
        self.options = [tuple(row) for row in options]
        assert len(set(self.items)) == len(self.items)
        n = len(items)
        col = {x:i+1 for i,x in enumerate(items)}
        self.L = [(i-1) % (n+1) for i in range(n+1)]
        self.R = [(i+1) % (n+1) for i in range(n+1)]
        self.U = list(range(n+1))
        self.D = list(range(n+1))
        self.C = list(range(n+1))
        self.S = [0]*(n+1)
        self.row = [-1]*(n+1)
        for ri, option in enumerate(self.options):
            assert option and len(set(option)) == len(option)
            nodes = []
            for name in option:
                c = col[name]
                j = len(self.L)
                self.L.append(j)
                self.R.append(j)
                self.U.append(self.U[c])
                self.D.append(c)
                self.C.append(c)
                self.S.append(0)
                self.row.append(ri)
                self.D[self.U[c]] = j
                self.U[c] = j
                self.S[c] += 1
                nodes.append(j)
            for i, j in enumerate(nodes):
                self.L[j] = nodes[i-1]
                self.R[j] = nodes[(i+1) % len(nodes)]

    def cover(self, c, depth):
        self.R[self.L[c]] = self.R[c]
        self.L[self.R[c]] = self.L[c]
        self.updates_by_depth[depth] += 1
        r = self.D[c]
        while r != c:
            j = self.R[r]
            while j != r:
                self.D[self.U[j]] = self.D[j]
                self.U[self.D[j]] = self.U[j]
                self.S[self.C[j]] -= 1
                self.updates_by_depth[depth] += 1
                j = self.R[j]
            r = self.D[r]

    def uncover(self, c):
        r = self.U[c]
        while r != c:
            j = self.L[r]
            while j != r:
                self.S[self.C[j]] += 1
                self.D[self.U[j]] = j
                self.U[self.D[j]] = j
                j = self.L[j]
            r = self.U[r]
        self.R[self.L[c]] = c
        self.L[self.R[c]] = c

    def solve(self, mrv=True, collect=True):
        before = tuple(tuple(v) for v in (self.L,self.R,self.U,self.D,self.S))
        self.nodes_by_depth = Counter()
        self.updates_by_depth = Counter()
        self.first_branch_by_depth = {}
        self.solution_count = 0
        self.solutions = set()
        chosen = []

        def visit(depth):
            self.nodes_by_depth[depth] += 1
            c = self.R[0]
            if c == 0:
                self.solution_count += 1
                if collect:
                    self.solutions.add(tuple(sorted(chosen)))
                return
            if mrv:
                j = self.R[c]
                while j:
                    if self.S[j] < self.S[c]:
                        c = j
                    j = self.R[j]
            self.first_branch_by_depth.setdefault(depth, self.items[c-1])
            self.cover(c, depth)
            r = self.D[c]
            while r != c:
                chosen.append(self.row[r])
                j = self.R[r]
                while j != r:
                    self.cover(self.C[j], depth)
                    j = self.R[j]
                visit(depth+1)
                j = self.L[r]
                while j != r:
                    self.uncover(self.C[j])
                    j = self.L[j]
                chosen.pop()
                r = self.D[r]
            self.uncover(c)

        visit(0)
        assert before == tuple(tuple(v) for v in (self.L,self.R,self.U,self.D,self.S))
        if collect:
            assert self.solution_count == len(self.solutions)
        self.updates = sum(self.updates_by_depth.values())
        return self


def brute_exact_cover(items, options):
    """Oracle: inspect every subset of options, with no search pruning."""
    out = set()
    target = Counter(items)
    for mask in range(1 << len(options)):
        rows = tuple(i for i in range(len(options)) if mask >> i & 1)
        if Counter(x for i in rows for x in options[i]) == target:
            out.add(rows)
    return out


def validate():
    from itertools import combinations
    from pathlib import Path
    import json
    import time
    start = time.monotonic()
    cases = 0
    by_n = {}
    for n in range(5):
        items = list(range(n))
        all_options = [tuple(i for i in items if mask >> i & 1)
                       for mask in range(1,1 << n)]
        count = 0
        for size in range(min(5,len(all_options))+1):
            for options in combinations(all_options,size):
                expected = brute_exact_cover(items,options)
                for mrv in (True,False):
                    observed = DLX(items,options).solve(mrv=mrv)
                    assert observed.solutions == expected, (items,options,mrv)
                count += 1
        by_n[n] = count
        cases += count
    # Single edge: two item headers plus one option node are deleted.
    assert DLX([0,1],[(0,1)]).solve().updates == 3
    complete_graphs = []
    expected_updates = [0,1]
    from math import prod
    for n in range(12):
        if n >= 2:
            expected_updates.append(1+(n-1)+(n-1)**2+(n-1)*expected_updates[n-2])
        run = DLX(list(range(n)),list(combinations(range(n),2))).solve(collect=False)
        assert run.updates == expected_updates[n], (n,run.updates)
        assert run.solution_count == (0 if n % 2 else prod(range(1,n,2)))
        complete_graphs.append({'vertices':n,'updates':run.updates,'solutions':run.solution_count})
    report = {'status':'pass','distinct_incidence_matrices':cases,
              'matrices_by_item_count':by_n,
              'policies':['first remaining item','MRV with first-item tie break'],
              'oracle':'All subsets of options independently checked; exact solution sets match. Link restoration asserted after every solve.',
              'limitations':'Nonempty distinct options; at most four items and five options. Operation counts additionally calibrated against hand counts and complete-graph recurrences.',
              'complete_graph_calibration':complete_graphs,
              'seconds':round(time.monotonic()-start,3)}
    (Path(__file__).parent/'results/algorithm_x_validation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    validate()
