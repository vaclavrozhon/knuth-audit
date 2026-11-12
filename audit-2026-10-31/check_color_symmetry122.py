"""Independent orbit, rollback and complete-set checks for DLX122--123."""
from collections import Counter
from datetime import datetime, timezone
from itertools import permutations, product
from random import Random
import hashlib
import json
import math
import re
from color_symmetry122 import SymmetryDLX, canonical_model, toy
from colored_dlx import brute
from native_symmetry122 import OUT, encode, run, save, sha


def native_models(label, data):
    lookup = {tuple(sorted(line.split())): k for k, line in enumerate(data.splitlines()[1:])}
    assert len(lookup) == len(data.splitlines())-1
    result = set()
    current = None
    for line in (OUT/'native'/f'{label}.stdout').read_text().splitlines():
        if re.fullmatch(r'\d+:\s*', line):
            if current is not None:
                value = tuple(sorted(current))
                assert value not in result
                result.add(value)
            current = []
        elif line.strip():
            tokens = re.sub(r'\s*\(\d+ of \d+\)\s*$', '', line).split()
            assert current is not None
            current.append(lookup[tuple(sorted(tokens))])
    if current is not None:
        value = tuple(sorted(current))
        assert value not in result
        result.add(value)
    return result


def orbit_closure(seeds, v, d):
    return sorted({tuple((i, p[c-v] if c >= v else c) for i, c in row)
                   for p in permutations(range(v, v+d)) for row in seeds})


def rgs(n, m):
    result = set()
    def rec(a, largest):
        if len(a) == n:
            result.add(tuple(a))
        else:
            for c in range(1, min(m, largest+1)+1):
                rec(a+[c], max(largest, c))
    rec([], 0)
    return result


def stirling(n, k):
    row = [1]+[0]*k
    for _ in range(n):
        row = [0]+[j*row[j]+row[j-1] for j in range(1, k+1)]
    return row[k]


def vectors(models, rows, n):
    result = set()
    for model in models:
        values = [None]*n
        for r in model:
            (p, zero), (q, c) = rows[r]
            assert zero == 0 and q == p+n and values[p-1] is None
            values[p-1] = c
        assert None not in values
        result.add(tuple(values))
    assert len(result) == len(models)
    return result


def main():
    rng = Random(122123)
    cases, rejection_totals = [], Counter()
    # Symmetry is literal at the node-order level in these instances: every
    # option uses the same item ordering as all its color-permuted companions.
    for number in range(200):
        primary, secondary = rng.randint(1, 3), rng.randint(1, 3)
        v, d = rng.choice((1, 2)), rng.choice((2, 3))
        seeds = []
        for _ in range(rng.randint(1, 4)):
            support = sorted(rng.sample(range(1, primary+1), rng.randint(1, primary)))
            support += sorted(rng.sample(range(primary+1, primary+secondary+1), rng.randint(0, secondary)))
            seeds.append(tuple((i, 0 if i <= primary else rng.randrange(v+d)) for i in support))
        rows = orbit_closure(seeds, v, d)
        if len(rows) > 16:
            # Bound the independent every-subset oracle, not the XCC solver.
            rows = orbit_closure(seeds[:2], v, d)
        assert len(rows) <= 16
        all_models = brute(primary, rows)
        expected = {canonical_model(model, rows, v) for model in all_models}
        solver = SymmetryDLX(primary+secondary, primary, rows, v=v).solve(check_each_node=True)
        actual = [canonical_model(model, rows, v) for model in solver.solutions]
        assert len(actual) == len(set(actual)) and set(actual) == expected
        rejection_totals.update(solver.rejections)
        data = encode(primary+secondary, primary, rows)
        label = f'oracle122-{number:03d}'
        native = run(label, 'symmetry122', data, threshold=48+v)
        native_set = native_models(label, data)
        assert native['solutions'] == solver.count and native_set == solver.solutions
        free = all(all(any(c == j for r in model for _, c in rows[r])
                       for j in range(v, v+d)) for model in all_models)
        if free:
            assert len(all_models) == math.factorial(d)*len(actual)
        cases.append(dict(number=number, n=primary+secondary, primary=primary, v=v, d=d,
                          rows=rows, all_models=sorted(all_models), representatives=sorted(native_set),
                          orbits=len(expected), free_color_action=free))
    # Force rejections after an uncolored secondary, a second primary and a
    # purification, including a wrapped row and a repeated color.
    stress_seeds = [((4, 0), (2, 0), (5, 1), (1, 0), (6, 3), (7, 1), (8, 2)),
                    ((3, 0), (5, 1), (6, 2))]
    stress = orbit_closure(stress_seeds, 1, 3)
    all_models = brute(3, stress)
    solver = SymmetryDLX(8, 3, stress).solve(check_each_node=True)
    expected = {canonical_model(m, stress) for m in all_models}
    assert len(solver.solutions) == len(expected)
    assert {canonical_model(m, stress) for m in solver.solutions} == expected
    rejection_totals.update(solver.rejections)
    data = encode(8, 3, stress)
    native = run('rollback122', 'symmetry122', data)
    assert native_models('rollback122', data) == solver.solutions
    assert native['solutions'] == solver.count
    stress_record = dict(rows=stress, all_models=sorted(all_models),
                         representatives=sorted(solver.solutions), rejections=dict(solver.rejections))
    # Explicit C3 path with no eligible item, and a valid delayed primary:
    # p1 chooses a new color before p2 is permitted to branch.
    blocked = SymmetryDLX(1, 1, [((1, 0),)], thresholds={1:2}).solve(check_each_node=True)
    assert blocked.count == 0 and blocked.rejections['no_eligible_primary'] == 1
    delayed_rows = toy(2, 2)
    delayed = SymmetryDLX(4, 2, delayed_rows, thresholds={2:2}).solve(check_each_node=True)
    assert delayed.count == 2

    small = []
    for m in range(1, 5):
        for n in range(1, 7):
            rows = toy(m, n)
            solver = SymmetryDLX(2*n, n, rows).solve(check_each_node=True)
            values = vectors(solver.solutions, rows, n)
            assert values == rgs(n, m)
            assert len(values) == sum(stirling(n, k) for k in range(1, m+1))
            assert m**n == sum(stirling(n, k)*math.prod(range(m-k+1, m+1))
                              for k in range(1, min(m, n)+1))
            plain = set(product(range(1, m+1), repeat=n))
            keys = set()
            for a in plain:
                relabel = {}
                keys.add(tuple(relabel.setdefault(x, len(relabel)+1) for x in a))
            assert keys == values
            small.append(dict(m=m, n=n, labeled=len(plain), partitions=len(values)))
    rows = toy(4, 10)
    data = encode(20, 10, rows)
    large = {variant:run('toy123-m4-n10-'+variant, variant, data,
                        spacing=1 if variant == 'symmetry122' else 10000)
             for variant in ['original', 'symmetry122']}
    full = native_models('toy123-m4-n10-symmetry122', data)
    values = vectors(full, rows, 10)
    assert values == rgs(10, 4)
    assert len(values) == 43947 == sum(stirling(10, k) for k in range(1, 5))
    assert large['original']['solutions'] == 4**10 == 1048576
    sampled = native_models('toy123-m4-n10-original', data)
    sample_vectors = vectors(sampled, rows, 10)
    assert len(sample_vectors) == 104
    assert all(all(1 <= c <= 4 for c in value) for value in sample_vectors)
    assert round(large['original']['search_mems']/10**6) == 49
    assert round(large['symmetry122']['search_mems']/10**6) == 2
    histogram = Counter(max(value) for value in values)
    assert histogram == {k:stirling(10, k) for k in range(1, 5)}
    save(OUT/'symmetry122-checked.json', dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
         source_sha256=sha(__file__), interpreter_sha256=sha(SymmetryDLX.__module__+'.py'),
         oracle_cases=cases, rollback_case=stress_record, rejection_totals=dict(rejection_totals),
         c3_cases=dict(no_eligible_primary=blocked.count, delayed_primary=delayed.count),
         conclusion='Every finite oracle orbit has exactly one representative with equivariant node order. Both native and independent spacer interpreter restore state after rejected prefixes. Arbitrarily reordered input companions are separate counterexamples, not claimed to pass.'))
    save(OUT/'partitions123-checked.json', dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
         source_sha256=sha(__file__), small_complete_cases=small, m4n10_runs=large,
         m4n10_partition_histogram=dict(histogram), complete_rgs_sha256=hashlib.sha256(json.dumps(sorted(values)).encode()).hexdigest(),
         complete_native_model_set_equal_to_independent_rgs=True, original_samples_validated=len(sample_vectors),
         erratum='Answer123 refers to equation7.2.1.5–(4), not exercise7.2.1.5–4; correction26Nov2024.',
         scope='General counting proof is in SYMMETRY121_123_NOTES.md. Counts and quoted rounded mems verified; both gross and secondary-LEN-subtracted mems recorded.'))
    print('PASS:200 complete orbit cases, rollback and C3 checks,24 toy grids;43947 complete native models equal independent RGS.')


if __name__ == '__main__':
    main()
