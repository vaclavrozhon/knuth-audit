"""Independent finite checks of SAT 351 and commutation of resampling logs.

Events are truth tables, not clauses; supports are derived from truth tables.
The general proofs are in LOPSIDEPENDENCY_NOTES.md. No Monte Carlo is used.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json


def support(event, n):
    return sum(1 << j for j in range(n)
               if any(((event >> x) ^ (event >> (x ^ (1 << j)))) & 1
                      for x in range(1 << n)))


def possible(event, mask, n):
    return sum(1 << x for x in range(1 << n)
               if any((event >> y) & 1 and not ((x ^ y) & ~mask)
                      for y in range(1 << n)))


def edge(a, b, sa, sb, can, full):
    return bool((a & (full ^ b) & can[b, sa]) or
                (b & (full ^ a) & can[a, sb]))


def run(word, events, supports, stack, n):
    cursor = [0] * n
    for i in word:
        state = sum(stack[j][cursor[j]] << j for j in range(n))
        if not ((events[i] >> state) & 1):
            return False, None
        for j in range(n):
            if supports[i] & (1 << j):
                cursor[j] += 1
    return True, tuple((cursor[j], stack[j][cursor[j]]) for j in range(n))


def audit_pairs(n, counts):
    m = 1 << n
    full = (1 << m) - 1
    supp = [support(a, n) for a in range(1 << m)]
    can = {(a, mask): possible(a, mask, n)
           for a in range(1 << m) for mask in range(1 << n)}
    stacks = [tuple(tuple(bits[3*j:3*j+3]) for j in range(n))
              for bits in product(range(2), repeat=3*n)]
    for a in range(1 << m):
        for b in range(a, 1 << m):
            counts['event_pairs'] += 1
            sa, sb = supp[a], supp[b]
            if edge(a, b, sa, sb, can, full):
                continue
            counts['nonadjacent_pairs'] += 1
            assert (a & b).bit_count() * m >= a.bit_count() * b.bit_count()
            counts['positive_correlation_checks'] += 1
            legal = 0
            for stack in stacks:
                ab = run((0, 1), (a, b), (sa, sb), stack, n)
                ba = run((1, 0), (a, b), (sa, sb), stack, n)
                assert ab == ba, (n, a, b, stack, ab, ba)
                legal += ab[0]
                counts['commutation_tables'] += 1
            assert Q(legal, len(stacks)) == Q(a.bit_count()*b.bit_count(), m*m)
            counts['word_probability_checks'] += 1
    print('pairs complete', n, dict(counts), flush=True)
    return supp, can


def audit_joint_conditioning(counts):
    n = 2
    m = 1 << n
    full = (1 << m) - 1
    supp = [support(a, n) for a in range(1 << m)]
    can = {(a, mask): possible(a, mask, n)
           for a in range(1 << m) for mask in range(1 << n)}
    for probabilities in [(Q(1, 2), Q(1, 2)), (Q(1, 3), Q(3, 4)),
                          (Q(0), Q(2, 3)), (Q(1), Q(1))]:
        masses = [Q(1)] * m
        for x in range(m):
            for j, p in enumerate(probabilities):
                masses[x] *= p if (x >> j) & 1 else 1-p
        prob = [sum(masses[x] for x in range(m) if (a >> x) & 1)
                for a in range(1 << m)]
        for a, b, c in product(range(1 << m), repeat=3):
            if (edge(a, b, supp[a], supp[b], can, full) or
                    edge(a, c, supp[a], supp[c], can, full)):
                continue
            avoid = full ^ (b | c)
            assert prob[a & avoid] <= prob[a] * prob[avoid]
            counts['joint_conditioning_checks'] += 1


def audit_words(counts):
    # Three overlapping monotone conjunctions: all are nonadjacent under 351.
    # This also tests arbitrarily ordered words, with repeated event labels.
    n = 3
    events = [sum(1 << x for x in range(8) if (x & mask) == mask)
              for mask in (3, 6, 5)]
    supports = [3, 6, 5]
    for word in product(range(3), repeat=3):
        need = [1 + sum(bool(supports[i] & (1 << j)) for i in word)
                for j in range(n)]
        legal = 0
        for bits in product(range(2), repeat=sum(need)):
            offset = 0
            stack = []
            for size in need:
                stack.append(bits[offset:offset+size])
                offset += size
            actual = run(word, events, supports, stack, n)
            sorted_word = tuple(sorted(word))
            assert actual == run(sorted_word, events, supports, stack, n)
            legal += actual[0]
            counts['three_letter_tables'] += 1
        assert Q(legal, 1 << sum(need)) == Q(1, 4) ** 3
        counts['three_letter_probabilities'] += 1


def main():
    counts = Counter()
    for n in (1, 2, 3):
        audit_pairs(n, counts)
    audit_joint_conditioning(counts)
    audit_words(counts)
    result = {'scope': 'All pairs of Boolean events on at most three variables; '
              'joint avoidance of two nonneighbors on two variables under four '
              'product laws; three-letter logs for three overlapping conjunctions',
              'counts': dict(counts),
              'identical_fair_bit_example': {
                  'simultaneous_occurrence': '1/2',
                  'product_of_marginals': '1/4',
                  'legal_two_step_resampling_log': '1/4'},
              'status': 'all assertions passed'}
    (Path(__file__).parent / 'results/lopsidependencies.json').write_text(
        json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
