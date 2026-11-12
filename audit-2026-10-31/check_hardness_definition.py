"""Audit the non-explosive literal sequence in the printed SAT 442 definition.

Do not conflate raw derivability with the operational convention after conflict.
Also independently test a proposed repair allowing a terminal lower-level conflict.
"""
from check_hardness import *


@lru_cache(None)
def repaired_sequence(F, k, U):
    all_literals = frozenset(l for v in U for l in (v, -v))
    if k == 0:
        return all_literals if () in F else frozenset()
    out = set()

    def conflict(G):
        lower = repaired_sequence(G, k - 1, U)
        return any(-a in lower for a in lower)

    def walk(G, remaining):
        if conflict(G):
            out.update(all_literals)
            return
        for v in remaining:
            for l in (v, -v):
                if conflict(restrict(G, -l)):
                    out.add(l)
                    walk(restrict(G, l), tuple(w for w in remaining if w != v))

    walk(F, U)
    return frozenset(out)


def raw_pc(F, U):
    value = 0
    for row in product((-1, 0, 1), repeat=len(U)):
        G = F
        for v, s in zip(U, row):
            if s:
                G = restrict(G, v * s)
        free = tuple(v for v, s in zip(U, row) if not s)
        if not free:
            continue
        M = models(G, free)
        forced = frozenset.intersection(*M) if M else frozenset(l for v in free for l in (v, -v))
        value = max(value, next(k for k in range(len(U) + 1)
                               if forced <= sequence_definition(G, k, U)))
    return value


def level_two_witness():
    F = canon([(1, 2), (1, -2), (-1, 3, 4), (-1, 3, -4),
               (-1, -3, 4), (-1, -3, -4)])
    U = (1, 2, 3, 4)
    raw = sequence_definition(F, 2, U)
    operational = derived(F, 2, U)
    assert raw == {-4, -3, -2, 1, 2, 3, 4}
    assert operational == {-4, -3, -2, -1, 1, 2, 3, 4}
    assert repaired_sequence(F, 2, U) == operational
    first_choices = [l for v in U for l in (v, -v)
                     if reduction(restrict(F, -l), 1)[0] == ((),)]
    assert first_choices == [1]
    assert semantic_indices(F)[:2] == (2, 2)
    assert raw_pc(F, U) == 3
    return {'F': F, 'k': 2, 'raw': sorted(raw), 'operational': sorted(operational),
            'only_possible_first_literal': 1, 'raw_PC_index': 3,
            'operational_PC_index': 2, 'repair_verified': True}


def main():
    counts = Counter()
    mismatches = Counter()
    witnesses = {}
    U = (1, 2, 3)
    C = clauses_on(3, False)
    for size in range(5):
        for clauses in combinations(C, size):
            F = canon(clauses)
            counts['formulas'] += 1
            for k in range(4):
                A = sequence_definition(F, k, U)
                B = derived(F, k, U)
                repaired = repaired_sequence(F, k, U)
                assert repaired == B, (F, k, repaired, B)
                raw_conflict = any(-l in A for l in A)
                assert raw_conflict == (reduction(F, k)[0] == ((),))
                assert A <= sequence_definition(F, k + 1, U)
                if A != B:
                    assert raw_conflict
                    mismatches[k] += 1
                    witnesses.setdefault(k, {'F': F, 'raw': sorted(A), 'operational': sorted(B)})
                for l in (a for v in U for a in (v, -v)):
                    if raw_conflict or -l in A:
                        child = sequence_definition(restrict(F, l), k, U)
                        assert any(-x in child for x in child)
                        counts['442c_restriction_checks'] += 1
                counts['levels'] += 1
    F = canon([(1,), (-1, 2), (-1, -2)])
    assert sequence_definition(F, 1, (1, 2)) == {1, 2, -2}
    assert derived(F, 1, (1, 2)) == {1, -1, 2, -2}
    assert semantic_indices(F)[:2] == (1, 1)
    assert raw_pc(F, (1, 2)) == 2
    result = {'counts': dict(counts), 'raw_vs_operational_mismatches_by_k': dict(mismatches),
              'first_witness_by_k': witnesses,
              'minimal_explanatory_witness': {'F': F, 'L1_printed': [-2, 1, 2],
                                              'L1_procedure': [-2, -1, 1, 2],
                                              'raw_PC_index': 2, 'operational_PC_index': 1},
              'level_two_witness_442bf': level_two_witness(),
              'repair': 'Permit a valid forcing sequence to terminate at a lower-level contradiction, independently of target literal.',
              'status': 'all assertions passed; the printed definition differs from the procedure'}
    (Path(__file__).parent / 'results/hardness_definition.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
