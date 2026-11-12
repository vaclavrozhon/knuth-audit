"""Independent finite checks of SAT 442--444: propagation, UC/PC and SLUR.

Two implementations are compared: a fixed-point reduction and literal-sequence
enumeration from the exercise definition. Semantic claims use truth tables.
"""
from functools import lru_cache
from itertools import product, combinations
from collections import Counter
from pathlib import Path
import json


def canon(F):
    return tuple(sorted(set(tuple(sorted(set(c))) for c in F)))


@lru_cache(None)
def variables(F):
    return tuple(sorted({abs(l) for c in F for l in c}))


@lru_cache(None)
def restrict(F, l):
    return canon(tuple(x for x in c if x != -l) for c in F if l not in c)


@lru_cache(None)
def reduction(F, k):
    if () in F:
        return ((),), ()
    if k == 0:
        return F, ()
    for v in variables(F):
        for l in (v, -v):
            if reduction(restrict(F, -l), k - 1)[0] == ((),):
                G, forced = reduction(restrict(F, l), k)
                return G, tuple(sorted(set(forced) | {l}))
    return F, ()


def derived(F, k, universe):
    G, forced = reduction(F, k)
    return frozenset(l for v in universe for l in (v, -v)) if G == ((),) else frozenset(forced)


@lru_cache(None)
def sequence_definition(F, k, universe):
    """Literally enumerate all consistent, distinct-variable derivation sequences."""
    if k == 0:
        return frozenset(l for v in universe for l in (v, -v)) if () in F else frozenset()
    out = set()

    def walk(G, remaining):
        for v in remaining:
            for l in (v, -v):
                lower = sequence_definition(restrict(G, -l), k - 1, universe)
                if any(-a in lower for a in lower):
                    out.add(l)
                    walk(restrict(G, l), tuple(w for w in remaining if w != v))

    walk(F, universe)
    return frozenset(out)


@lru_cache(None)
def models(F, universe):
    return tuple(frozenset(v * s for v, s in zip(universe, row))
                 for row in product((-1, 1), repeat=len(universe))
                 if all(any(v * s in c for v, s in zip(universe, row)) for c in F))


def clauses_on(n, include_empty=True):
    return tuple(tuple((i + 1) * s for i, s in enumerate(row) if s)
                 for row in product((-1, 0, 1), repeat=n)
                 if include_empty or any(row))


@lru_cache(None)
def semantic_indices(F):
    U = variables(F)
    uc = pc = 0
    restrictions = 0
    for row in product((-1, 0, 1), repeat=len(U)):
        G = F
        for v, s in zip(U, row):
            if s:
                G = restrict(G, v * s)
        free = tuple(v for v, s in zip(U, row) if not s)
        M = models(G, free)
        restrictions += 1
        if not M:
            level = next(k for k in range(len(U) + 1) if reduction(G, k)[0] == ((),))
            uc = max(uc, level)
            # For zero remaining variables, truth is vacuous but contradiction
            # is explicitly part of PC, as in the exercise's implication rule.
            pc = max(pc, level)
        else:
            forced = frozenset.intersection(*M)
            level = next(k for k in range(len(U) + 1) if forced <= derived(G, k, free))
            pc = max(pc, level)
    return uc, pc, restrictions


def contains_primes(F):
    U = variables(F)
    M = models(F, U)
    for row in product((-1, 0, 1), repeat=len(U)):
        c = frozenset(v * s for v, s in zip(U, row) if s)
        if all(c & a for a in M):
            prime = all(not all((c - {l}) & a for a in M) for l in c)
            if prime and tuple(sorted(c)) not in F:
                return False
    return True


@lru_cache(None)
def slur_outcomes(F, k, occurring_only=False):
    G = reduction(F, k)[0]
    if G == ((),):
        return frozenset({'unsat'})

    @lru_cache(None)
    def step(G):
        if not G:
            return frozenset({'sat'})
        choices = {l for c in G for l in c} if occurring_only else {l for v in variables(G) for l in (v, -v)}
        out = set()
        for l in choices:
            A = reduction(restrict(G, l), k)[0]
            if A != ((),):
                out.update(step(A))
                continue
            B = reduction(restrict(G, -l), k)[0]
            if B != ((),):
                out.update(step(B))
            else:
                out.add('maybe')
        return frozenset(out)

    return step(G)


def renamed_horn(F):
    U = variables(F)
    return any(all(sum(l * flip[abs(l)] > 0 for l in c) <= 1 for c in F)
               for signs in product((-1, 1), repeat=len(U))
               for flip in [dict(zip(U, signs))])


def main():
    totals = Counter()
    spectrum = Counter()
    definition_mismatches = []

    def audit(F, direct=False):
        F = canon(F)
        U = variables(F)
        uc, pc, count = semantic_indices(F)
        assert uc <= pc <= uc + 1 and pc <= len(U)
        assert (pc == 0) == (not F or () in F)
        assert (uc == 0) == contains_primes(F)
        spectrum[f'{uc},{pc}'] += 1
        totals['formulas'] += 1
        totals['restrictions'] += count
        for k in range(len(U) + 1):
            L = derived(F, k, U)
            if direct:
                # Use two declared variables even if one is absent.
                literal = sequence_definition(F, k, (1, 2))
                operational = derived(F, k, (1, 2))
                if literal != operational:
                    # The printed definition does NOT automatically explode
                    # after contradiction; record rather than silently fix it.
                    assert reduction(F, k)[0] == ((),)
                    assert any(-a in literal for a in literal)
                    definition_mismatches.append({'F': F, 'k': k,
                                                  'definition': sorted(literal),
                                                  'procedure': sorted(operational)})
                totals['sequence_comparisons'] += 1
            assert L <= derived(F, k + 1, U)
            if all(len(c) > k for c in F):
                assert not L
            for l in (a for v in U for a in (v, -v)):
                if -l in L:
                    assert reduction(restrict(F, l), k)[0] == ((),)
                totals['restriction_lemmas'] += 1
            outcome = slur_outcomes(F, k)
            assert ('maybe' not in outcome) == (uc <= k), (F, k, uc, outcome)
            if models(F, U):
                assert 'unsat' not in outcome
            else:
                assert 'sat' not in outcome
            totals['slur_levels'] += 1
        if renamed_horn(F):
            assert 'maybe' not in slur_outcomes(F, 1)
            totals['renamed_horn'] += 1
        return uc, pc

    C = clauses_on(2)
    for mask in range(1 << len(C)):
        audit([c for i, c in enumerate(C) if mask >> i & 1], direct=True)
    C = clauses_on(3, False)
    for size in range(5):
        for F in combinations(C, size):
            audit(F)

    examples = [[], [(1,)], [(1,), (-1, 2)], [(1, 2), (-1, 2)],
                [(1, 2), (-1, 2), (1, -2), (-1, -2, 3)],
                [(1, 2, 3), (-1, 2, 3), (1, -2, 3), (-1, -2, 3)],
                [(1, 2, 3), (-1, 2, 3), (1, -2, 3), (-1, -2, 3),
                 (1, 2, -3), (-1, 2, -3), (1, -2, -3), (-1, -2, -3, 4)]]
    example_indices = [semantic_indices(canon(F))[:2] for F in examples]
    assert example_indices == [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]
    cubes = []
    for n in range(1, 6):
        F = canon(tuple((i + 1) * s for i, s in enumerate(row)) for row in product((-1, 1), repeat=n))
        indices = semantic_indices(F)[:2]
        assert indices == (n, n)
        cubes.append({'n': n, 'uc': indices[0], 'pc': indices[1]})
    R = canon([(1, 2, -3), (2, 3, -4), (3, 4, 1), (4, -1, 2),
               (-1, -2, 3), (-2, -3, 4), (-3, -4, -1)])
    assert semantic_indices(R)[:2] == (2, 3)
    assert all(not derived(R, k, (1, 2, 3, 4)) for k in range(3))
    assert all(derived(R, k, (1, 2, 3, 4)) == {-1, 2, 4} for k in (3, 4, 5))
    B = canon([(1, 2), (-2, 3), (1, -2, -3), (-1, 2, 3)])
    assert not renamed_horn(B) and slur_outcomes(B, 1) == {'sat'}
    pure_guard = canon([(1, 2, 3), (1, 2, -3), (1, -2, 3), (1, -2, -3)])
    assert semantic_indices(pure_guard)[:2] == (2, 3)
    assert slur_outcomes(pure_guard, 1) == {'sat', 'maybe'}
    assert slur_outcomes(pure_guard, 1, True) == {'sat'}
    result = {'counts': dict(totals), 'spectrum_uc_pc': dict(sorted(spectrum.items())),
              '442_definition_procedure_mismatches': definition_mismatches,
              '443a_examples_uc_pc': example_indices, 'full_cube_counterexamples_443e': cubes,
              'R_uc_pc': [2, 3], 'R_L0_L1_L2': [], 'R_L3_and_above': [-1, 2, 4],
              '444b_nonrenamed_horn_always_sat': True,
              '444c_polarity_ambiguity': {'F': pure_guard, 'uc': 2, 'pc': 3,
                                        'both_polarities': ['maybe', 'sat'], 'occurring_only': ['sat']},
              'status': 'all assertions passed'}
    path = Path(__file__).parent / 'results/hardness.json'
    path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
