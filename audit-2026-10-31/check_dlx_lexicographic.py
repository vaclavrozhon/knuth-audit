#!/usr/bin/env python3
"""Literal answer36 LL rollback, checked against all row-subset solutions."""
from collections import Counter
from datetime import datetime, timezone
from itertools import combinations, combinations_with_replacement
import json

from dlx1_audit_tools import ROOT, sha
from spacer_algorithm_x import SpacerX

OUT = ROOT/'results/lexicographic'


class EmptyRootBoundary(Exception):
    pass


class LexSpacer(SpacerX):
    def unchoose(self, node):
        p = node-1
        while p != node:
            j = self.T[p]
            if j <= 0:
                p = self.D[p]
            else:
                self.uncover(j)
                p -= 1

    def solve_lex(self, empty_fix=False):
        original = self.snapshot()
        self.ordered = []
        self.witness_rollbacks = 0
        x = [None]*(self.primary+1)
        level = LL = 0
        step = 2
        while True:
            if step == 2:
                self.validate_state(x[:level])
                if self.R[0] == 0:
                    if level == LL+1 or (empty_fix and level == 0):
                        self.ordered.append(tuple((self.T[p], self.row_of(p)[0])
                                                  for p in x[:level]))
                        step = 8
                    else:
                        LL += 1
                        while level > LL:
                            level -= 1
                            i = self.T[x[level]]
                            self.unchoose(x[level])
                            self.uncover(i)
                        self.witness_rollbacks += 1
                        step = 3
                else:
                    step = 3
            elif step == 3:
                if self.R[0] == 0:
                    raise EmptyRootBoundary(dict(level=level, LL=LL, next_item=0))
                i = self.choose('first' if level == LL else 'mrv')
                step = 4
            elif step == 4:
                self.cover(i)
                x[level] = self.D[i]
                step = 5
            elif step == 5:
                if x[level] == i:
                    step = 7
                else:
                    p = x[level]+1
                    while p != x[level]:
                        j = self.T[p]
                        if j <= 0:
                            p = self.U[p]
                        else:
                            self.cover(j)
                            p += 1
                    level += 1
                    step = 2
            elif step == 6:
                self.unchoose(x[level])
                i = self.T[x[level]]
                x[level] = self.D[x[level]]
                step = 5
            elif step == 7:
                self.uncover(i)
                step = 8
            elif step == 8:
                if level == 0:
                    break
                level -= 1
                if level < LL:
                    LL = level
                step = 6
        assert self.snapshot() == original and not self.undo
        return self


def oracle(rows, nprimary):
    result = []
    for mask in range(1 << len(rows)):
        used = set()
        selected = []
        for j, row in enumerate(rows):
            if mask >> j & 1:
                if used.intersection(row):
                    break
                used.update(row)
                selected.append(j)
        else:
            if not set(range(1, nprimary+1)) <= used:
                continue
            remaining = set(range(1, nprimary+1))
            path = []
            while remaining:
                item = min(remaining)
                row_id = next(j for j in selected if item in rows[j])
                path.append((item, row_id))
                remaining.difference_update(rows[row_id])
            result.append(tuple(path))
    assert len(set(result)) == len(result)
    return sorted(result)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    counts = Counter()
    restoration_checks = Counter()
    for n in range(1, 5):
        names = [str(i) for i in range(1, n+1)]
        for primary in range(1, n+1):
            universe = [tuple(i+1 for i in range(n) if bits >> i & 1)
                        for bits in range(1, 1 << n) if bits & ((1 << primary)-1)]
            for size in range(min(len(universe), 4)+1):
                for rows in combinations(universe, size):
                    orders = [rows, rows[::-1]] if size > 1 else [rows]
                    for ordered_rows in orders:
                        test = LexSpacer(names, ordered_rows, primary).solve_lex()
                        assert test.ordered == oracle(ordered_rows, primary)
                        counts['distinct_option_runs'] += 1
                        counts['solutions'] += len(test.ordered)
                        counts['witness_rollbacks'] += test.witness_rollbacks
                        restoration_checks.update(test.checks)
            if n <= 3:
                for rows in combinations_with_replacement(universe, 4):
                    test = LexSpacer(names, rows, primary).solve_lex()
                    assert test.ordered == oracle(rows, primary)
                    counts['repeated_option_runs'] += 1
                    counts['solutions'] += len(test.ordered)
                    counts['witness_rollbacks'] += test.witness_rollbacks
                    restoration_checks.update(test.checks)
    empty = []
    for n in (0, 2):
        names = [str(i) for i in range(n)]
        ordinary = SpacerX(names, [], 0).solve()
        assert ordinary.solutions == {()}
        try:
            LexSpacer(names, [], 0).solve_lex()
        except EmptyRootBoundary as error:
            state = error.args[0]
        else:
            raise AssertionError('Expected the printed LL=0 empty-root boundary')
        corrected = LexSpacer(names, [], 0).solve_lex(empty_fix=True)
        assert corrected.ordered == [()]
        empty.append(dict(total_items=n, primary_items=0, options=0,
                          printed_state=state, corrected_solutions=[[]]))
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), spacer_sha256=sha(ROOT/'spacer_algorithm_x.py'),
                  counts=dict(counts), state_checks=dict(restoration_checks), empty_root=empty,
                  scope='All families of up to four distinct options on up to four items, '
                        'every positive primary prefix, both option orders; four-option multisets '
                        'on up to three items. All solutions and their canonical lexicographic order.',
                  interpretation='The answer X2 otherwise clause is nested under RLINK(0)=0. '
                                 'For an empty initial problem, explicitly visit the empty solution.')
    (OUT/'literal.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
