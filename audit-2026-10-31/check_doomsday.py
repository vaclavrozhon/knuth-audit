"""Doomsday recurrence, strict small matrices, and corrected exercise 180.

All arithmetic is integral. The independent bit-set search maximizes over all
MRV ties at every recursive call; DLX is used separately on explicit witnesses.
"""
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json
from algorithm_x import DLX


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit
        mask -= bit


def candidates(d, n):
    for t in range(1, n):
        if n-t-1 >= 0:
            yield (t, 0), 1+t*d[n-t-1]
        for u in range(1, t+1):
            a, b = n-t-u+1, n-t-u-1
            if a < 0 or (t > u and b < 0):
                continue
            yield (t, u), u+u*d[a]+((t-u)*d[b] if t > u else 0)


def recurrence(limit, base):
    d, maximizers = [1, base], [[], []]
    for n in range(2, limit+1):
        choices = list(candidates(d, n))
        value = max(v for _, v in choices)
        d.append(value)
        maximizers.append([pair for pair, v in choices if v == value])
    return d, maximizers


def certify_modified_recurrence(d):
    """Finite certificate for the proposed closed form; proof is in the notes.

    Define F by d[0:17] and F(n+5)=4F(n)+1 for n>=12. Large t>=15
    are dominated by F(n+5)>=4F(n)+1. For t<=14 and n>=41 all
    referenced indices are >=12, reducing induction to five residues.
    """
    def f(n):
        if n < 17:
            return d[n]
        q, r = divmod(n-12, 5)
        return (4**q*(3*d[12+r]+1)-1)//3
    assert all(f(n) == d[n] for n in range(201))
    assert all(f(n+1) > f(n) for n in range(17))
    assert all(f(n+5) >= 4*f(n)+1 for n in range(17))
    # For t=15..19, 4^floor(t/5)>=2t; t -> t+5 preserves this.
    assert all(4**(t//5) >= 2*t for t in range(15,20))
    checks = 0
    for n in range(41,46):
        for (t,u), value in candidates([f(j) for j in range(n)], n):
            if t > 14:
                continue
            gap = f(n)-value
            c = 4-t if not u else 1-t+3*u
            assert 3*gap+c >= 0
            assert gap == 0 if (t,u) == (4,0) else gap > 0
            checks += 1
    return {'small_t_residue_certificates': checks,
            'large_t_threshold': 15, 'periodic_index_threshold': 12,
            'unique_maximizer_from': 17,
            'formula': 'D(5k+r)=4^k*c_r-1/3 for k>=3',
            'c_r_numerators_over_96': [200,263,350,464,608]}


@lru_cache(None)
def worst_search(items, rows):
    if not items:
        return 1, 1
    counts = {b: sum(bool(r & b) for r in rows) for b in bits(items)}
    t = min(counts.values())
    scores = []
    for b, count in counts.items():
        if count != t:
            continue
        children = [worst_search(items ^ r, tuple(s for s in rows if not s & r))
                    for r in rows if r & b]
        scores.append((1+sum(x[0] for x in children), sum(x[1] for x in children)))
    assert len({s for _, s in scores}) == 1
    return max(scores)


def strict(items, rows):
    signatures = [tuple(bool(r & b) for r in rows) for b in bits(items)]
    return len(set(rows)) == len(rows) and len(set(signatures)) == len(signatures)


def structural_check(items, rows, pivot):
    branch = sorted((r for r in rows if r & pivot),
                    key=lambda r: sum(bool(r & s) for s in rows))
    t = len(branch)
    if not t:
        return 0, 0
    counts = [sum(bool(r & s) for s in rows) for r in branch]
    u = 0
    while u < t and counts[u] == t+u:
        u += 1
    if u < t:
        assert counts[u] >= t+u+1
    if u:
        previous = 0
        prefix_bits = []
        for p, r in enumerate(branch[:u], 1):
            assert r & previous == previous and r.bit_count() == p
            extra = r ^ previous
            assert extra.bit_count() == 1
            prefix_bits.append(extra)
            previous = r
        assert prefix_bits[0] == pivot
        # The first u rows are the nested singleton prefixes. For the other
        # t-1 rows meeting the last prefix, the 2026 erratum gives a staircase.
        remaining = [r for r in rows if r not in branch[:u] and r & previous]
        assert len(remaining) == t-1
        actual = Counter(sum(1 << j for j, b in enumerate(prefix_bits) if r & b)
                         for r in remaining)
        expected = Counter(sum(1 << (r-1) for r in range(1, u+1) if q < t+r-u)
                           for q in range(1, t))
        assert actual == expected
    return t, u


def main():
    old, oldmax = recurrence(200, 1)
    new, newmax = recurrence(200, 2)
    assert old[:22] == [1,1,2,4,5,6,10,13,17,22,31,41,53,69,94,125,165,213,283,377,501,661]
    assert all(x == [(4, 0)] for x in oldmax[19:])
    assert all(x == [(4, 0)] for x in newmax[17:])
    certificate = certify_modified_recurrence(new)
    counts = {}; maxima = {}; violations = Counter(); structures = Counter()
    for k in range(1, 5):
        items = (1 << k)-1
        count = 0
        for family in range(1 << items):
            rows = tuple(r for r in range(1, items+1) if family & (1 << (r-1)))
            if not strict(items, rows):
                continue
            count += 1
            nodes, solutions = worst_search(items, rows)
            n = len(rows)
            assert nodes <= new[n], (items, rows, nodes, new[n])
            maxima[n] = max(maxima.get(n, 0), nodes)
            if nodes > old[n]:
                violations[n] += 1
            deg = {b: sum(bool(r & b) for r in rows) for b in bits(items)}
            for pivot, degree in deg.items():
                if degree == min(deg.values()):
                    t, u = structural_check(items, rows, pivot)
                    structures[t, u] += 1
        counts[k] = count
    witnesses = []
    for k, rows in [(1, (1,)), (2, (1,2)), (3, (1,2,4,3,6))]:
        items = (1 << k)-1
        assert strict(items, rows)
        options = [tuple(j for j in range(k) if row & (1 << j)) for row in rows]
        dlx = DLX(list(range(k)), options).solve()
        nodes = sum(dlx.nodes_by_depth.values())
        assert nodes == worst_search(items, tuple(sorted(rows)))[0]
        assert nodes > old[len(rows)]
        witnesses.append({'item_count': k, 'options': options, 'nodes': nodes,
                          'solutions': dlx.solution_count, 'profile': dict(dlx.nodes_by_depth),
                          'printed_bound': old[len(rows)], 'modified_bound': new[len(rows)]})
    report = {'finding': 'F017: D(1)=1 fails to count the root and solution leaf.',
              'witnesses': witnesses, 'strict_families_by_item_count': counts,
              'total_strict_families': sum(counts.values()),
              'max_nodes_by_number_of_options': maxima,
              'printed_bound_violations_by_number_of_options': dict(violations),
              'structural_checks': sum(structures.values()),
              'structural_parameter_counts': {str(k): v for k,v in sorted(structures.items())},
              'original_recurrence_first_26': old[:26], 'modified_recurrence_first_26': new[:26],
              'recurrence_computed_through': 200,
              'modified_unique_4_0_range_checked': [17,200],
              'modified_recurrence_certificate': certificate,
              'scope': 'All nonempty-row families on up to four items with distinct columns; all MRV tie choices at every node. Corrected exercise 180 holds in every tested pivot. The certificate proves the modified numerical recurrence formula for all n with the reduction argument in the notes; a separate issue is its applicability to every Algorithm X tie choice.'}
    (Path(__file__).parent/'results/doomsday.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
