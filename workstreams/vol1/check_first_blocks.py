"""Exact, bounded checks for TAOCP 1, §§1.2.4, 1.3.3, and 2.2.1.

No OCR is executed. The formulas and algorithms were read from page images.
General proofs, scope, and errata are in notes/. Run from any directory.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import permutations
from math import ceil, comb, factorial, floor, gcd
from pathlib import Path
import json


def floor_sums():
    xs = sorted({Q(a, b) for a in range(-20, 21) for b in range(1, 9)})
    count37 = 0
    for m in range(-12, 13):
        for n in range(1, 25):
            d = gcd(m, n)
            for x in xs:
                terms = [(m*k + x)/n for k in range(n)]
                expected_floor = Q((m-1)*(n-1) + d-1, 2) + d*floor(x/d)
                expected_ceil = Q((m+1)*(n-1) - d+1, 2) + d*ceil(x/d)
                assert sum(map(floor, terms)) == expected_floor, (m, n, x)
                assert sum(map(ceil, terms)) == expected_ceil, (m, n, x)
                count37 += 1

    def check38(x, y):
        left = sum(floor(x + Q(k)/y) for k in range(ceil(y)))
        right = floor(x*y + floor(x+1)*(ceil(y)-y))
        assert left == right, (str(x), str(y), left, right)

    ys = sorted({Q(a, b) for a in range(1, 33) for b in range(1, 11)})
    for y in ys:
        for x in xs:
            check38(x, y)
    boundary_count = 0
    epsilon = Q(1, 1000003)
    for y in ys:
        for k in range(ceil(y)):
            for shift in [-2, 0, 1]:
                for side in [-epsilon, Q(0), epsilon]:
                    check38(shift + 1 - Q(k)/y + side, y)
                    boundary_count += 1
    # Known erratum: 0 <= k <= n is NOT a symmetric ceiling-sum range.
    def inclusive(m, n, x):
        return sum(ceil(Q(m*k+x, n)) for k in range(n+1))
    assert (inclusive(1, 2, 2), inclusive(2, 1, 2)) == (5, 6)
    symmetry_count = 0
    for m in range(1, 13):
        for n in range(1, 13):
            d = gcd(m, n)
            for x in xs:
                left = sum(ceil((m*k+x)/n) for k in range(1, n+1))
                expected = Q(m*n+m+n-d, 2) + d*ceil(x/d)
                assert left == expected
                symmetry_count += 1
    return dict(ex37_floor_and_ceiling_cases=count37,
                ex37_m_range=[-12, 12], ex37_n_range=[1, 24],
                rational_x_count=len(xs), rational_y_count=len(ys),
                ex38_grid_cases=len(xs)*len(ys),
                ex38_threshold_cases=boundary_count,
                corrected_ceiling_symmetry_cases=symmetry_count,
                old_symmetry_counterexample=dict(m=1, n=2, x=2, sums=[5, 6]))


def inverse_i(p):
    # Literal sequential assignments from I1--I6, not Python negative indexing.
    x = [None] + list(p)
    n = len(p)
    m, j = n, -1
    counts = Counter()
    while True:
        assert 1 <= m <= n
        counts['I2'] += 1
        i = x[m]
        if i > 0:
            while True:
                counts['I3'] += 1
                assert j < 0 and i == x[m]
                x[m] = j
                j = -m
                m = i
                assert 1 <= m <= n
                i = x[m]
                counts['I4'] += 1
                if i < 0:
                    i = j
                    counts['cycle_ends'] += 1
                    break
        # Corrected I5 comment: ORIGINAL p[-i] = m.
        assert i < 0 and p[-i-1] == m
        x[m] = -i
        counts['I5'] += 1
        m -= 1
        if m == 0:
            break
        assert counts['I3'] <= n
    for step in ['I2', 'I3', 'I4', 'I5']:
        assert counts[step] == n
    return tuple(x[1:]), counts['cycle_ends']


def expected_j_state(p, inv, m):
    """Build the corrected answer-13 invariant from the ORIGINAL permutation."""
    answer = []
    for v in range(1, len(p)+1):
        if inv[v-1] > m:
            answer.append(inv[v-1])
        else:
            t = v
            seen = set()
            while t > m:
                assert t not in seen
                seen.add(t)
                t = p[t-1]
            answer.append(-p[t-1])
    return answer


def inverse_j(p, inv):
    x = [None] + [-v for v in p]
    n, visits = len(p), 0
    for m in range(n, 0, -1):
        assert x[1:] == expected_j_state(p, inv, m), (p, m, x)
        j, visited = m, set()
        while True:
            assert 1 <= j <= n and j not in visited
            visited.add(j)
            visits += 1
            i = x[j]
            if i < 0:
                break
            j = i
        assert -i == p[m-1]
        # Sequential assignments matter when j == -i.
        x[j] = x[-i]
        x[-i] = m
    return tuple(x[1:]), visits


def permutation_checks():
    rows = []
    for n in range(1, 9):
        total_a, total_cycles, cases = 0, 0, 0
        for p in permutations(range(1, n+1)):
            # Independent inverse by searching the original image list.
            inv = tuple(p.index(v)+1 for v in range(1, n+1))
            got_i, cycles = inverse_i(p)
            got_j, a = inverse_j(p, inv)
            assert got_i == inv == got_j
            # Independent cycle count by orbit traversal in the input.
            unseen, c = set(p), 0
            while unseen:
                v = next(iter(unseen))
                while v in unseen:
                    unseen.remove(v)
                    v = p[v-1]
                c += 1
            assert cycles == c
            total_cycles += c
            total_a += a
            cases += 1
        harmonic = sum((Q(1, k) for k in range(1, n+1)), Q(0))
        assert Q(total_a, cases) == (n+1)*harmonic - n
        assert Q(total_cycles, cases) == harmonic
        assert cases == factorial(n)
        rows.append(dict(n=n, permutations=cases, j_mean_visits=str(Q(total_a, cases)),
                         mean_cycles=str(Q(total_cycles, cases))))
    # Known answer-13 flaw already occurs for (1 2), before m=1.
    assert expected_j_state((2, 1), (2, 1), 1) == [2, -2]
    return dict(rows=rows, total_permutations=sum(r['permutations'] for r in rows),
                old_j_invariant_counterexample=dict(permutation=[2, 1], m=1,
                                                    actual_x=[2, -2],
                                                    old_negative_clause_at_i1=-2),
                scope='Pseudocode and invariants; no MIX emulator or machine limits.')


def stack_outputs(n):
    # Enumerate operational histories, WITHOUT testing the forbidden pattern.
    output_to_word = {}
    histories = 0

    def visit(next_input, stack, output, word):
        nonlocal histories
        if len(output) == n:
            histories += 1
            assert output not in output_to_word, (output, word, output_to_word[output])
            output_to_word[output] = word
            return
        if next_input <= n:
            visit(next_input+1, stack+(next_input,), output, word+'S')
        if stack:
            visit(next_input, stack[:-1], output+(stack[-1],), word+'X')
    visit(1, (), (), '')
    return output_to_word, histories


def avoids_312(p):
    return not any(p[j] < p[k] < p[i]
                   for i in range(len(p)) for j in range(i+1, len(p))
                   for k in range(j+1, len(p)))


def stack_checks():
    rows = []
    for n in range(9):
        outputs, histories = stack_outputs(n)
        avoiders = {p for p in permutations(range(1, n+1)) if avoids_312(p)}
        assert set(outputs) == avoiders
        assert len(outputs) == histories == comb(2*n, n)//(n+1)
        rows.append(dict(n=n, histories=histories, distinct_outputs=len(outputs),
                         all_permutations=factorial(n)))
    # Ballot-prefix coefficients in the answer to §2.2.1-4, independently
    # counted by legal stack-height transitions and by the reflection formula.
    def binom(n, k):
        return comb(n, k) if 0 <= k <= n else 0
    heights = Counter({0: 1})
    prefix_cases = 0
    for length in range(41):
        for height in range(length+2):
            expected = 0 if (length-height) % 2 else (
                binom(length, (length-height)//2) -
                binom(length, (length-height)//2-1))
            assert heights[height] == expected, (length, height)
            prefix_cases += 1
        new = Counter()
        for h, count in heights.items():
            new[h+1] += count
            if h > 0:
                new[h-1] += count
        heights = new
    return dict(rows=rows, prefix_coefficients_checked=prefix_cases,
                prefix_max_length=40, total_permutations=sum(r['all_permutations'] for r in rows))


def main():
    result = dict(floor_sums=floor_sums(), permutations=permutation_checks(),
                  stacks=stack_checks(), status='passed')
    path = Path(__file__).resolve().parent/'results'/'first-blocks.json'
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
