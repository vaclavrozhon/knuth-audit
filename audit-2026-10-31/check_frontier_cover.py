#!/usr/bin/env python3
"""DLX40/42: literal descending array operations, counts and all solution sets."""
from collections import Counter
from datetime import datetime, timezone
from itertools import combinations, combinations_with_replacement
import json

from dlx1_audit_tools import ROOT, sha

OUT = ROOT/'results/frontier_cover'


class Database:
    def __init__(self):
        self.entries = [[0, 1]]
        self.index = {0: 0}
        self.peak = 1

    def insert(self, key, count):
        if key in self.index:
            self.entries[self.index[key]][1] += count
        else:
            self.index[key] = len(self.entries)
            self.entries.append([key, count])
            self.peak = max(self.peak, len(self.entries))

    def delete(self, j):
        del self.index[self.entries[j][0]]
        last = self.entries.pop()
        if j < len(self.entries):
            self.entries[j] = last
            self.index[last[0]] = j

    def mapping(self):
        assert len(self.entries) == len(self.index)
        assert all(self.index[key] == j for j, (key, _) in enumerate(self.entries))
        return dict(self.entries)


def row_subset_oracle(rows, primary, future=0, normalize=False):
    prefix = 0
    for row in rows:
        prefix |= row
    ended = prefix & ~future
    out = {}
    for bits in range(1 << len(rows)):
        used = 0
        for j, row in enumerate(rows):
            if bits >> j & 1:
                if used & row:
                    break
                used |= row
        else:
            if normalize:
                if used & (ended & primary) != ended & primary:
                    continue
                used &= ~(ended & ~primary)
            out.setdefault(used, set()).add(bits)
    return out


def count_frontier(rows, primary, verify=True, trace=False):
    assert all(row and row & primary for row in rows)
    future = [0]*(len(rows)+1)
    for k in range(len(rows)-1, -1, -1):
        future[k] = future[k+1] | rows[k]
    db = Database()
    families = {0: {0}} if verify else None
    past = 0
    stats = dict(peak=1, peak_after_compression=1, frontier_max=0,
                 checkpoint_bound_checks=0, transient_bound_violations=0,
                 factor_two_bound_checks=0, prefix_family_checks=0)
    details = []
    for k, row in enumerate(rows):
        f = future[k+1]
        frontier = (past & row) | (past & f) | (row & f)
        nu = frontier.bit_count()
        bound = 1 << nu
        assert len(db.entries) <= bound
        stats['checkpoint_bound_checks'] += 1
        before = len(db.entries)
        for j in range(len(db.entries)-1, -1, -1):
            key, count = db.entries[j]
            if not key & row:
                db.insert(key+row, count)
        transient = len(db.entries)
        assert transient <= 2*bound
        stats['factor_two_bound_checks'] += 1
        stats['transient_bound_violations'] += transient > bound
        if verify:
            added = {key: values.copy() for key, values in families.items()}
            for key, values in families.items():
                if not key & row:
                    extensions = {value | (1 << k) for value in values}
                    target = added.setdefault(key | row, set())
                    assert not target.intersection(extensions)
                    target.update(extensions)
            assert db.mapping() == {key: len(values) for key, values in added.items()}
        u = row & ~f
        up = u & primary
        us = u & ~primary
        if u:
            for j in range(len(db.entries)-1, -1, -1):
                key, count = db.entries[j]
                if key & up != up:
                    db.delete(j)
                elif key & us:
                    db.delete(j)
                    db.insert((key & ~u) | up, count)
        if verify:
            families = {}
            for key, values in added.items():
                if key & up == up:
                    target = families.setdefault((key & ~u) | up, set())
                    assert not target.intersection(values)
                    target.update(values)
            expected = row_subset_oracle(rows[:k+1], primary, f, normalize=True)
            assert families == expected
            assert db.mapping() == {key: len(values) for key, values in expected.items()}
            stats['prefix_family_checks'] += 1
        assert len(db.entries) <= bound
        stats['checkpoint_bound_checks'] += 1
        stats['peak_after_compression'] = max(stats['peak_after_compression'], len(db.entries))
        stats['frontier_max'] = max(stats['frontier_max'], nu)
        if trace:
            details.append(dict(k=k+1, row=row, past=past, future=f, frontier=frontier,
                                nu=nu, bound=bound, before=before,
                                after_N3=transient, after_N4=len(db.entries)))
        past |= row
    stats['peak'] = db.peak
    assert len(db.entries) <= 1
    solutions = sum(count for key, count in db.entries if key & primary == primary)
    if verify:
        expected = row_subset_oracle(rows, primary)
        expected_models = set().union(*(values for key, values in expected.items()
                                       if key & primary == primary))
        actual_models = set().union(*(values for key, values in families.items()
                                     if key & primary == primary))
        assert actual_models == expected_models and solutions == len(expected_models)
    return dict(solutions=solutions, **stats, trace=details)


def main():
    OUT.mkdir(exist_ok=True, parents=True)
    totals = Counter()
    for n in range(1, 5):
        for primary_count in range(1, n+1):
            primary = (1 << primary_count)-1
            universe = [row for row in range(1, 1 << n) if row & primary]
            for size in range(min(4, len(universe))+1):
                for rows in combinations(universe, size):
                    for order in ([rows, rows[::-1]] if size > 1 else [rows]):
                        result = count_frontier(order, primary)
                        totals['distinct_option_runs'] += 1
                        for key in ['checkpoint_bound_checks', 'factor_two_bound_checks',
                                    'prefix_family_checks', 'transient_bound_violations']:
                            totals[key] += result[key]
            if n <= 3:
                for rows in combinations_with_replacement(universe, 4):
                    result = count_frontier(rows, primary)
                    totals['repeated_option_runs'] += 1
                    for key in ['checkpoint_bound_checks', 'factor_two_bound_checks',
                                'prefix_family_checks', 'transient_bound_violations']:
                        totals[key] += result[key]
    empty = count_frontier([], 0, trace=True)
    assert empty['solutions'] == 1
    singleton = count_frontier([1], 1, trace=True)
    assert singleton['peak'] == 2 and singleton['frontier_max'] == 0
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), totals=dict(totals),
                  singleton=singleton, empty_problem=empty,
                  scope='Literal descending array insertion and swap deletion; '
                        'all row-index solution families compared after every compressed prefix. '
                        'The bound 2^nu holds at the iteration checkpoints; transient size needs a factor two.')
    (OUT/'small.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
