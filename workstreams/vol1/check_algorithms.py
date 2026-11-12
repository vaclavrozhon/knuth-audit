"""Exact checks for TAOCP Volume 1 §1.1, including the literal rewrite table.

General proofs are recorded separately. Successful finite checks do not
establish a universal assertion about all computational methods.
"""
from itertools import product
from math import gcd
from pathlib import Path
import json


def euclid_e(m, n):
    count = 0
    while True:
        r = m % n
        count += 1
        if not r:
            return n, count
        m, n = n, r


def euclid_f(m, n):
    count = 0
    while True:
        m %= n
        count += 1
        if not m:
            return n, count
        n %= m
        count += 1
        if not n:
            return m, count


# Table columns in the book are theta, phi, b (match), a (no match).
RULES = [('ab', '', 1, 2), ('', 'c', 0, 0), ('a', 'b', 2, 3),
         ('c', 'a', 3, 4), ('b', 'b', 0, 5)]


def rewriting(m, n):
    word, j, steps = 'a'*m+'b'*n, 0, 0
    seen = set()
    while j != 5:
        assert (word, j) not in seen
        seen.add((word, j))
        theta, phi, yes, no = RULES[j]
        pos = word.find(theta)
        if pos < 0:
            j = no
        else:
            word = word[:pos]+phi+word[pos+len(theta):]
            j = yes
        steps += 1
    return word, steps


def f1(q):
    if len(q) == 1:
        return q
    if len(q) == 2:
        return (*q, 0, 1)
    m, n, r, phase = q
    if phase == 1:
        return m, n, m % n, 2
    if phase == 2:
        return (n,) if r == 0 else (m, n, r, 3)
    assert phase == 3 and r > 0
    return n, r, r, 1


def f2(q):
    if len(q) == 2:
        m, n = q
        return m, n, m, n, 1
    if len(q) == 3:
        return q
    if len(q) == 5:
        m, n, a, b, phase = q
        assert phase in (1, 5) and b > 0
        return m, n, a, b, a % b, 2
    m, n, a, b, r, phase = q
    if phase == 2:
        return (m, n, b) if r == 0 else (m, n, a, b, r, 3)
    if phase == 3:
        return m, n, b, b, r, 4
    assert phase == 4 and r > 0
    return m, n, a, r, 5


def decode(q):
    if len(q) == 2:
        return q
    if len(q) == 3:
        return (q[2],)
    if len(q) == 5:
        m, n, a, b, phase = q
        return a, b, (0 if phase == 1 else b), 1
    m, n, a, b, r, phase = q
    return decode(f2(q)) if phase == 4 else (a, b, r, phase)


def steps_for(q):
    return 2 if len(q) == 6 and q[-1] in (3, 4) else 1


def check_simulated_state(q):
    following = q
    for _ in range(steps_for(q)):
        following = f2(following)
    assert f1(decode(q)) == decode(following), q
    # The 2025 form of condition (c) tests the sampled destination.
    assert (len(decode(following)) == 1) == (len(following) == 3), q


def finite_relation_witness():
    # All inputs and outputs are disjoint; all computations take one step.
    q1, i1, o1 = ('x', 'y'), {'x'}, {'y'}
    q2, i2, o2 = ('x0', 'x1', 'y0', 'y1'), {'x0', 'x1'}, {'y0', 'y1'}
    a = dict(x='y', y='y')
    b = dict(x0='y0', x1='y1', y0='y0', y1='y1')
    g = dict(x='x0')
    h = dict(x0='x', x1='x', y0='y', y1='y')
    assert all(h[g[x]] == x for x in i1)
    assert all(a[h[q]] == h[b[q]] for q in q2)
    assert all((h[q] in o1) == (q in o2) for q in q2)  # 2002
    assert all((h[b[q]] in o1) == (b[q] in o2) for q in q2)  # 2025
    assert all(b[q] == q for q in o2) and all(a[q] == q for q in o1)
    assert all(h[b[g[x]]] == a[x] for x in i1)  # original output clause
    assert len(i1) != len(i2) and len(o1) != len(o2)
    return dict(status='verified', original_1997_conditions=True,
                corrected_2002_conditions=True, corrected_2025_conditions=True,
                j_constant=1, input_sizes=[len(i1), len(i2)],
                output_sizes=[len(o1), len(o2)],
                reason_not_isomorphic='No bijection exists between the input sets (nor between the output sets).',
                novelty='The same finite construction was publicly posted in 2019.')


def main():
    cases = 0
    max_rewrite_steps = 0
    states = set()
    for m, n in product(range(1, 65), repeat=2):
        # Direct divisor maximization, independent of the remainder recurrence.
        expected = max(d for d in range(1, min(m, n)+1) if m % d == n % d == 0)
        e, count = euclid_e(m, n)
        assert e == expected
        assert euclid_f(m, n) == (e, count)
        assert euclid_e(m+7*n, n) == (e, count)
        word, steps = rewriting(m, n)
        assert word == 'a'*expected
        max_rewrite_steps = max(max_rewrite_steps, steps)
        q = (m, n)
        assert decode(q) == q  # g is identity on initial pairs
        while len(q) != 3:
            states.add(q)
            check_simulated_state(q)
            q = f2(q)
        check_simulated_state(q)
        states.add(q)
        assert q == (m, n, expected)
        cases += 1
    # Also check phase equations off the reachable traces, on well-defined
    # state domains: a,b>0; r>=0 in phase 2; r>0 in phases 3 and 4.
    off_trace = 0
    for a, b in product(range(1, 9), repeat=2):
        for phase in (1, 5):
            check_simulated_state((2, 7, a, b, phase))
            off_trace += 1
        for r in range(9):
            for phase in ((2,) if r == 0 else (2, 3, 4)):
                check_simulated_state((2, 7, a, b, r, phase))
                off_trace += 1
    assert [euclid_e(m, 5)[1] for m in range(1, 6)] == [2, 3, 4, 3, 1]
    assert euclid_e(2166, 6099)[0] == 57
    result = dict(status='passed', positive_input_pairs=cases,
                  maximum_literal_rewrite_steps=max_rewrite_steps,
                  retained_input_simulation_states=len(states),
                  additional_phase_equations=off_trace,
                  e1_counts_for_n5=[2, 3, 4, 3, 1], t5='13/5', u5='18/5',
                  equivalence_counterexample=finite_relation_witness())
    dest = Path(__file__).resolve().parent/'results/algorithms.json'
    dest.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
