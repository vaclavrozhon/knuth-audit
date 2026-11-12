"""Reconcile the archived129 counts and their geometric multiplicities.

This performs arithmetic and checks completed logs; it does not repeat any
enumeration. The new fixed-branch queue provides its own independent counts.
"""
from collections import defaultdict
from datetime import datetime, timezone
from itertools import product
import json
import re

import symmetries129 as s
from run_symmetry129_literal import problem


def main():
    old = s.ROOT/'results/macmahon'
    used = {}

    def read(name):
        p = old/name
        used[str(p.relative_to(s.ROOT))] = s.sha(p)
        return json.loads(p.read_text())

    def terminal(name, count):
        p = old/name
        log = p.read_text()
        m = re.search(r'Altogether (\d+) solutions?', log)
        assert m and int(m[1]) == count, name
        used[str(p.relative_to(s.ROOT))] = s.sha(p)

    independent = {(d['kind'], d['periodic']): d['solutions'] for d in read('strong-bitset-counts.json')}
    native = {(d['kind'], d['periodic']): d['solutions'] for d in read('strong-counts.json')}
    assert native == independent
    strong = [independent[i, False] for i in range(1, 7)]
    periodic = [independent[i, True] for i in range(1, 7)]
    assert strong == [80768, 164964, 77660, 819832, 88772, 185172]
    assert periodic == [0, 5219, 2426, 24918, 2426, 5219]
    for (i, p), n in native.items():
        terminal(f'strong-{i}{"-periodic" if p else ""}.dlx2.txt', n)
    more = {d['label']: d['solutions'] for d in read('additional-bitset-counts.json')}
    assert more['strong-0'] == 68024064 == 48*sum(strong)
    assert more['strong-0-periodic'] == 1929984 == 48*sum(periodic)
    native_weak = [d['solutions'] for d in sorted(read('weak-counts.json'), key=lambda d: d['kind'])]
    weak_raw = [more[f'weak-{i}'] for i in range(1, 7)]
    assert native_weak == weak_raw
    for i, n in enumerate(weak_raw, 1):
        terminal(f'weak-{i}.dlx2.txt', n)
    weak = [(n-a)//2 for n, a in zip(weak_raw, strong)]
    assert all(n == a+2*b for n, a, b in zip(weak_raw, strong, weak))
    assert weak == [24516, 45818, 22202, 341301, 44690, 130676]

    reflection = {d['label']: d['solutions'] for d in read('reflection-bitset-counts.json')}
    tb_strong = [sum(reflection[f'tb-{i}-strong-{p}.xcc'] for p in ('badc', 'cdab', 'dcba')) for i in range(1, 7)]
    tb_raw = [reflection[f'tb-{i}.xcc'] for i in range(1, 7)]
    tb_weak = [(n-a)//2 for n, a in zip(tb_raw, tb_strong)]
    assert tb_strong == [88, 0, 0, 98, 0, 75]
    assert tb_weak == [1108, 12827, 8086, 3253, 12145, 4189]
    assert all(n == a+2*b for n, a, b in zip(tb_raw, tb_strong, tb_weak))

    geometry = read('lr/metadata.json')
    fixed_by_pair = defaultdict(lambda: dict(raw=0, indices=[]))
    free_raw, fixed_raw = 0, 0
    for d in geometry:
        n = reflection[f'lr/{d["index"]:03d}.xcc']
        if not d['fixed']:
            free_raw += n
            continue
        fixed_raw += n
        mono = [tuple(t) for t in d['mono']]
        assert {s.g.opposite(t) for t in mono} != set(mono)
        fixed = tuple(t for t in mono if s.g.reflect(t, 'lr') == t)
        key = min(tuple(sorted(fixed)), tuple(sorted(s.g.opposite(t) for t in fixed)))
        label = ','.join(s.g.name(t) for t in key)
        fixed_by_pair[label]['raw'] += n
        fixed_by_pair[label]['indices'].append(d['index'])
    for group in fixed_by_pair.values():
        assert group['raw'] % 4 == 0
        group['orbits'] = group['raw']//4
    assert sorted(d['orbits'] for d in fixed_by_pair.values()) == [25261, 35375, 46975]
    assert fixed_raw == 430444 and free_raw == 747906
    canonical = read('lr-canonical-models.json')
    assert canonical['raw_models'] == free_raw
    assert canonical['weak_not_strong'] == 186846 and canonical['strong_rotational'] == 261
    assert free_raw == 4*186846+2*261
    lr_weak = 186846+fixed_raw//4
    assert lr_weak == 294457
    both_raw = sum(n for name, n in reflection.items() if '-both.' in name)
    assert both_raw == 1298
    both = (both_raw-2*261)//4
    assert both == 194 and both_raw == 4*both+2*261
    total = sum(strong)+sum(weak)+sum(tb_weak)+lr_weak-2*both
    assert total == 2362048

    # Check the actual printed example option and the six mask labels. Our
    # old mask labels exchange bits0 and1; this is an injective relabeling,
    # not a discrepancy in the encoded equality relation.
    enc = problem()
    row = "02 abc -02:a /02:b \\02:c 31' bdc -32:d /41:c \\31:b".split()
    assert tuple(sorted(row)) in {tuple(sorted(r)) for r in enc['rows']}
    bookmask = lambda cs: (cs[1] != cs[2])+2*(cs[0] != cs[1])+4*(cs[2] != cs[0])
    mask_table = []
    for cs in product('abcd', repeat=3):
        oldmask = s.g.patchmask(cs)
        value = ((oldmask & 1) << 1) | ((oldmask & 2) >> 1) | (oldmask & 4)
        assert value == bookmask(cs)
        mask_table.append(dict(colors=''.join(cs), encoded_mask=oldmask, printed_mask=value))
    for cs, expected in [('aad', 5), ('ada', 3), ('daa', 6), ('abc', 7), ('cbd', 7), ('ccd', 5)]:
        assert bookmask(cs) == expected

    def monos(a, b):
        return dict(zip('abcd', (a, b, s.g.opposite(b), s.g.opposite(a))))

    def move_monos(positions, label, cp):
        action = s.BY[label]
        return {cp[ord(c)-97]: s.TS[action['cells'][s.TI[t]]] for c, t in positions.items()}

    # The two parenthetical equivalences printed in the canonical-type list.
    m1 = monos((0, 2, 0), (0, 3, 0))
    assert move_monos(m1, 'f4', 'badc') == m1
    assert s.BY['f4']['reflected'] and s.BY['f4']['edges'][s.EI['/', 1, 2]] == s.EI['/', 1, 2]
    assert {dict(zip('abcd', 'badc'))[c] for c in 'bd'} == set('ac')
    m2 = monos((0, 2, 0), (2, 3, 0))
    assert move_monos(m2, 'r2', 'cadb') == monos((0, 2, 0), (0, 3, 1))

    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=s.sha(__file__),
                  dependencies_sha256={p: s.sha(s.ROOT/p) for p in ['symmetries129.py', 'check_macmahon.py', 'run_symmetry129_literal.py']},
                  reused_evidence_sha256=used, strong_types=strong, periodic_types=periodic,
                  weak_rotation_raw=weak_raw, weak_not_strong_rotation_types=weak,
                  tb_strong_types=tb_strong, tb_raw=tb_raw, tb_weak_not_strong_types=tb_weak,
                  fixed_lr_types=dict(fixed_by_pair), free_lr_raw=free_raw, fixed_lr_raw=fixed_raw,
                  free_lr_weak_not_strong=186846, total_lr_weak_not_strong=lr_weak,
                  both_axes_raw=both_raw, both_axes_weak_not_strong=both,
                  totals=dict(strong_rotation=sum(strong), weak_not_strong_rotation=sum(weak),
                              weak_not_strong_tb=sum(tb_weak), weak_not_strong_lr=lr_weak,
                              strong_periodic=sum(periodic), special_strong=261,
                              any_symmetry_essentially_distinct=total),
                  printed_lr_total=281618, corrected_lr_difference=lr_weak-281618,
                  printed_option=row, mask_relabeling=mask_table,
                  canonical_parentheses=dict(type1=dict(action='f4', colors='badc', selector_edge=['/', 1, 2], swaps_allowed_and_excluded=True),
                                             type2=dict(action='r2', colors='cadb', source_bbb=[2, 3, 0], target_bbb=[0, 3, 1])),
                  union_proof='Among nonstrong colorings, any two of halfturn/TB/LR imply the third. Each pairwise and the triple intersection has194 orbits, so add the four disjoint-strong/class counts and subtract2*194.',
                  limitation='Arithmetic reuses completed searches. Old DLX2 terminal logs establish exhaustion but some old C builds returned arbitrary positive exit codes; their counts agree with independent bitset searches. New literal and fixed-branch runs have separately recorded zero-exit acceptance. No complete enumeration is repeated here.')
    (s.OUT/'counts-reconciled.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS129 archived counts, three fixed-LR types, masks; corrected total', total)


if __name__ == '__main__':
    main()
