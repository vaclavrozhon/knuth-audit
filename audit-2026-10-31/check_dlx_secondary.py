#!/usr/bin/env python3
"""DLX16--19: queen traces, secondary items, and the second-death test."""
from collections import Counter
from datetime import datetime, timezone
from itertools import combinations_with_replacement, permutations
import json
import random

from dlx1_audit_tools import ROOT, sha
from spacer_algorithm_x import SpacerX

OUT = ROOT/'results/dlx_secondary'
TOY = [(3, 5), (1, 4, 7), (2, 3, 6), (1, 4, 6), (2, 7), (4, 5, 7)]


class TraceX(SpacerX):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trace = []

    def validate_state(self, chosen):
        super().validate_state(chosen)
        self.chosen_rows = tuple(self.row_of(x)[0] for x in chosen)

    def choose(self, policy):
        i = super().choose(policy)
        self.trace.append(dict(path=self.chosen_rows, item=self.names[i], length=self.T[i]))
        return i


def set_search(names, rows, primary):
    """Independent recursive set-intersection implementation, with ordered trace."""
    trace, solutions, profile = [], set(), Counter()
    sets = list(map(set, rows))
    def visit(used, path):
        profile[len(path)] += 1
        uncovered = set(range(1, primary+1))-used
        if not uncovered:
            solutions.add(tuple(sorted(path)))
            return
        allowed = [r for r, row in enumerate(sets) if not row & used]
        column = {i: [r for r in allowed if i in sets[r]] for i in uncovered}
        i = min(uncovered, key=lambda i: (len(column[i]), i))
        trace.append(dict(path=path, item=names[i-1], length=len(column[i])))
        for r in column[i]:
            visit(used | sets[r], path+(r,))
    visit(set(), ())
    return solutions, trace, profile


def queen_problem(slack, corners_first=False):
    n = 4
    diagonals = [f'a{s}' for s in range(2, 2*n+1)]+[f'b{d}' for d in range(1-n, n)]
    if slack:
        names = [f'r{i}' for i in range(1, n+1)]+[f'c{j}' for j in range(1, n+1)]+diagonals
        if corners_first:
            corners = ['a2', 'a8', 'b-3', 'b3']
            names = corners+[name for name in names if name not in corners]
        primary = len(names)
    else:
        names = ['r3', 'c3', 'r2', 'c2', 'r4', 'c4', 'r1', 'c1']+diagonals
        primary = 8
    index = {name: i+1 for i, name in enumerate(names)}
    # Match the printed order (23): columns outside, rows inside.
    named_rows = [[f'r{i}', f'c{j}', f'a{i+j}', f'b{i-j}']
                  for j in range(1, n+1) for i in range(1, n+1)]
    if slack:
        named_rows += [[name] for name in diagonals]
    return names, [tuple(index[name] for name in row) for row in named_rows], primary


class SecondDeathX(SpacerX):
    def __init__(self, names, rows, primary):
        # The original initializer rejects a purely secondary row. Set up its
        # unchanged vertical layout with all items primary, then make the two
        # header rings required by I1--I2 for the actual primary count.
        assert all(rows), 'The input convention requires nonempty options.'
        super().__init__(names, rows)
        self.primary = primary
        for ring in ([0]+list(range(1, primary+1)),
                     [self.N+1]+list(range(primary+1, self.N+1))):
            for j, i in enumerate(ring):
                self.L[i] = ring[j-1]
                self.R[i] = ring[(j+1) % len(ring)]
        self.accepted = set()

    def validate_state(self, chosen):
        super().validate_state(chosen)
        if self.R[0] == 0:
            i = self.R[self.N+1]
            lengths = []
            while i != self.N+1:
                lengths.append(self.T[i])
                i = self.R[i]
            if all(length == 0 for length in lengths):
                self.accepted.add(tuple(sorted(self.row_of(x)[0] for x in chosen)))
            self.checks['second_death_acceptance_tests'] += 1


def second_death_oracle(n, primary, rows):
    pure = [set(row) for row in rows if not any(i <= primary for i in row)]
    allowed = [r for r, row in enumerate(rows) if any(i <= primary for i in row)]
    out = set()
    for bits in range(1 << len(allowed)):
        chosen = tuple(r for j, r in enumerate(allowed) if bits >> j & 1)
        counts = Counter(i for r in chosen for i in rows[r])
        if not all(counts[i] == 1 for i in range(1, primary+1)):
            continue
        if any(count > 1 for count in counts.values()):
            continue
        if all(set(counts) & row for row in pure):
            out.add(chosen)
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    placements = {p for p in permutations(range(1, 5))
                  if len({i+j for i, j in enumerate(p, 1)}) == 4
                  and len({i-j for i, j in enumerate(p, 1)}) == 4}
    assert placements == {(2, 4, 1, 3), (3, 1, 4, 2)}
    queens = []
    for slack, corners in [(True, False), (True, True), (False, False)]:
        names, rows, primary = queen_problem(slack, corners)
        audit = TraceX(names, rows, primary).solve()
        expected, trace, profile = set_search(names, rows, primary)
        assert audit.solutions == expected and audit.trace == trace and audit.profile == profile
        decoded, details = set(), []
        for solution in sorted(audit.solutions):
            p = [None]*4
            slacks = []
            for r in solution:
                if r < 16:
                    p[r % 4] = r//4+1
                else:
                    slacks.append(names[rows[r][0]-1])
            decoded.add(tuple(p))
            if slack:
                assert set(slacks) == {'a2', 'a5', 'a8', 'b-3', 'b0', 'b3'}
            details.append(dict(placement=p, slacks=slacks))
        assert decoded == placements
        if corners:
            assert [(v['item'], v['length']) for v in trace[:4]] == [
                ('a2', 2), ('a8', 1), ('b-3', 1), ('b3', 1)]
            for node in trace:
                depth = len(node['path'])
                if depth < 4:
                    assert node['item'] == ['a2', 'a8', 'b-3', 'b3'][depth]
                    assert node['length'] <= 2
        if not slack:
            # Complete X3 trace, including both dead leaves and both solutions.
            assert [(v['item'], v['length']) for v in trace] == [
                ('r3', 4), ('c2', 1), ('c3', 1), ('r2', 1),
                ('c3', 1), ('r2', 0), ('r2', 1), ('c2', 0),
                ('c3', 1), ('r2', 1), ('c2', 1)]
        queens.append(dict(slacks=slack, corners_first=corners, primary_order=names[:primary],
                           solutions=details, trace=trace, profile=dict(profile)))
    toy18 = SpacerX(list('abcdefg'), TOY, 4).solve()
    assert toy18.solutions == {(0, 3, 4), (1, 2)}
    toy19 = SecondDeathX(list('abcdefg'), TOY, 2).solve()
    assert toy19.accepted == {(1, 2)}
    totals, by_n = Counter(), Counter()
    def audit_case(n, primary, rows):
        expected = second_death_oracle(n, primary, rows)
        audit = SecondDeathX([str(i) for i in range(1, n+1)], rows, primary).solve()
        assert audit.accepted == expected, (n, primary, rows, audit.accepted, expected)
        totals.update(audit.checks)
        totals['input_cases'] += 1
        by_n[n] += 1
    for n in range(5):
        all_rows = [tuple(i+1 for i in range(n) if bits >> i & 1)
                    for bits in range(1, 1 << n)]
        for size in range(4):
            for rows in combinations_with_replacement(all_rows, size):
                for primary in range(n+1):
                    audit_case(n, primary, rows)
    rng = random.Random(16192026)
    for _ in range(300):
        n = rng.randint(1, 7)
        rows = []
        for _ in range(rng.randrange(9)):
            row = {rng.randint(1, n)} | {i for i in range(1, n+1) if rng.randrange(3) == 0}
            row = list(row)
            rng.shuffle(row)
            rows.append(tuple(row))
        rng.shuffle(rows)
        audit_case(n, rng.randrange(n+1), rows)
    # Outside the nonempty-option convention the empty option needs an input
    # rejection before constructing the spacer layout; it cannot be hit.
    assert second_death_oracle(1, 1, [(1,), ()]) == set()
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=sha(__file__), core_sha256=sha(ROOT/'spacer_algorithm_x.py'),
        queen_cases=queens, toy18=sorted(toy18.solutions), toy19=sorted(toy19.accepted),
        second_death_checks=dict(totals), cases_by_n=dict(by_n),
        scope='Full queen solution sets and complete ordered traces under stated item orders; '
              'all multisets of at most3 nonempty options on at most4 items at every primary cut, '
              'plus300 reordered random cases. An empty option is outside the spacer input '
              'convention and must cause immediate rejection if explicitly admitted.')
    (OUT/'verified.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], second_death_checks=totals,
                          queen_solutions=2, toy18=sorted(toy18.solutions),
                          toy19=sorted(toy19.accepted)), indent=2), flush=True)


if __name__ == '__main__':
    main()
