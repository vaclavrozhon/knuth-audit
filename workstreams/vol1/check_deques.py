"""Independent exact checks for Volume 1, §2.2.1 exercises 7--11.

The unrestricted transition model does not use the canonical-word rules,
the grammar, or the generating function. All enumeration is bounded.
"""
from collections import Counter
from functools import cache
from itertools import permutations, product
from pathlib import Path
import json
import time


def obtainable(n, mode):
    @cache
    def solve(next_input, deque):
        if next_input == n+1 and not deque:
            return frozenset({()})
        results = set()
        if next_input <= n:
            # Input-restricted: insert only at the right; output-restricted
            # and general: both ends may be used for insertion.
            results.update(solve(next_input+1, deque+(next_input,)))
            if mode != 'input':
                results.update(solve(next_input+1, (next_input,)+deque))
        if deque:
            results.update((deque[0],)+suffix for suffix in solve(next_input, deque[1:]))
            if mode != 'output':
                results.update((deque[-1],)+suffix for suffix in solve(next_input, deque[:-1]))
        return frozenset(results)
    outputs = solve(1, ())
    states = solve.cache_info().currsize
    solve.cache_clear()
    return outputs, states


def canonical(n):
    outputs, words = {}, set()

    def visit(next_input, deque, output, word):
        if len(output) == n:
            assert output not in outputs, (output, word, outputs.get(output))
            outputs[output] = word
            words.add(word)
            return
        if next_input <= n:
            if deque:  # Rule (iii): an insertion at height zero must be Q.
                visit(next_input+1, (next_input,)+deque, output, word+'S')
            if not word.endswith('X'):  # Rule (iv): forbid XQ.
                visit(next_input+1, deque+(next_input,), output, word+'Q')
        if deque:
            visit(next_input, deque[1:], output+(deque[0],), word+'X')
    visit(1, (), (), '')
    return outputs, words


def reverse_inverse_reverse(p):
    q = p[::-1]
    return tuple(q.index(v)+1 for v in range(1, len(p)+1))[::-1]


def compositions(total, parts):
    if parts == 0:
        if total == 0:
            yield ()
    elif parts == 1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first, parts-1):
                yield (first,)+rest


@cache
def grammar_b(n):
    # B -> empty | S Q^k (B X)^(k+1) B, k >= 0.
    result = Counter({'': 1}) if n == 0 else Counter()
    for k in range(n):
        for sizes in compositions(n-k-1, k+2):
            for children in product(*(grammar_b(size).items() for size in sizes)):
                word = 'S'+'Q'*k+''.join(w+'X' for w, _ in children[:-1])+children[-1][0]
                ways = 1
                for _, count in children:
                    ways *= count
                result[word] += ways
    return result


def grammar_start(n):
    # A -> Q^k (B X)^k, k >= 0. A is the book's nonterminal S.
    result = Counter()
    for k in range(n+1):
        for sizes in compositions(n-k, k):
            for children in product(*(grammar_b(size).items() for size in sizes)):
                word = 'Q'*k+''.join(w+'X' for w, _ in children)
                ways = 1
                for _, count in children:
                    ways *= count
                result[word] += ways
    return result


def recurrence_counts(max_n):
    # Coefficients of F^2+(z-3)F+2=0 with F(0)=1.
    quadratic = [1]
    for n in range(1, max_n+1):
        quadratic.append(quadratic[n-1] + sum(quadratic[k]*quadratic[n-k] for k in range(1, n)))
    linear = [1, 1]
    for n in range(2, max_n+1):
        numerator = 3*(2*n-3)*linear[n-1]-(n-3)*linear[n-2]
        assert numerator % n == 0
        linear.append(numerator//n)
    assert quadratic == linear
    # Third count: literal canonical-prefix transition counts, whose states
    # record height and whether the last symbol was X.
    states = Counter({(0, False): 1})
    prefixes = [1]
    for length in range(1, 2*max_n+1):
        nxt = Counter()
        for (h, last_x), count in states.items():
            if h:
                nxt[h+1, False] += count  # S
                nxt[h-1, True] += count   # X
            if not last_x:
                nxt[h+1, False] += count  # Q
        states = nxt
        if length % 2 == 0:
            prefixes.append(states[0, True])
    assert quadratic == prefixes
    return quadratic


def main():
    start = time.monotonic()
    counts = recurrence_counts(100)
    rows = []
    excluded_general_5 = None
    for n in range(9):
        input_set, input_states = obtainable(n, 'input')
        output_set, output_states = obtainable(n, 'output')
        c_outputs, c_words = canonical(n)
        assert set(c_outputs) == output_set
        assert len(input_set) == len(output_set) == len(c_words) == counts[n]
        assert {reverse_inverse_reverse(p) for p in input_set} == output_set
        assert all(reverse_inverse_reverse(reverse_inverse_reverse(p)) == p for p in input_set)
        row = dict(n=n, restricted_count=len(output_set), canonical_words=len(c_words),
                   input_states=input_states, output_states=output_states)
        if n <= 7:
            generated = grammar_start(n)
            assert set(generated) == c_words
            assert all(value == 1 for value in generated.values())
            assert all(value == 1 for value in grammar_b(n).values())
            row['grammar_strings'] = len(generated)
        if n == 4:
            all_p = set(permutations(range(1, n+1)))
            assert input_set-output_set == {(4, 1, 3, 2)}
            assert output_set-input_set == {(4, 2, 1, 3)}
            assert all_p-(input_set | output_set) == {(4, 2, 3, 1)}
        if n <= 7:
            general, general_states = obtainable(n, 'general')
            row.update(general_count=len(general), general_states=general_states)
            all_p = set(permutations(range(1, n+1)))
            if n <= 4:
                assert set(general) == all_p
            if n == 5:
                excluded_general_5 = sorted(all_p-general)
                assert excluded_general_5 == [(5, 1, 3, 2, 4), (5, 1, 3, 4, 2),
                                               (5, 2, 3, 1, 4), (5, 2, 3, 4, 1)]
        rows.append(row)
        print(json.dumps(row), flush=True)
    result = dict(status='passed', rows=rows, restricted_counts_0_to_15=counts[:16],
                  recurrence_and_prefix_count_checked_through=100,
                  excluded_general_n5=excluded_general_5,
                  elapsed_seconds=round(time.monotonic()-start, 3),
                  scope='Exercises 7--11; general-deque counts are bounded checks, not a proof of the infinite basis in exercise 13.')
    path = Path(__file__).resolve().parent/'results/deques.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print('All deque checks passed.', flush=True)


if __name__ == '__main__':
    main()
