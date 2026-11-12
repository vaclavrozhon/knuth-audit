"""Bounded independent comparison of Pratt's basis with literal deque operations.

This does not prove that the infinite basis is complete. The inherited
operation model does not use forbidden patterns or reduced histories.
"""
from itertools import permutations
from pathlib import Path
import json
import resource
import time
from check_deques import obtainable


def book_basis(length):
    if length < 5 or length % 2 == 0:
        return set()
    p = tuple(x for odd in range(5, length+1, 2) for x in (odd, odd-3))
    p += (3, length-1, 1) if length % 4 == 1 else (1, length-1, 3)
    assert sorted(p) == list(range(1, length+1))
    result = set()
    for swap_tail in (False, True):
        q = p[:-2]+p[-2:][::-1] if swap_tail else p
        for swap_values in (False, True):
            result.add(tuple(3-x if swap_values and x in (1, 2) else x for x in q))
    return result


def pratt_rotation_basis(length):
    # Pratt p. 273: rotate odd entries two places to the left, then swap
    # values 1 and 3 when (length-5)/2 is even.
    odds = list(range(1, length+1, 2))
    p = list(range(1, length+1))
    p[::2] = odds[2:]+odds[:2]
    if (length-5)//2 % 2 == 0:
        p = [4-x if x in (1, 3) else x for x in p]
    result = set()
    for tail in (False, True):
        q = p[:-2]+p[-2:][::-1] if tail else p
        for values in (False, True):
            result.add(tuple(3-x if values and x in (1, 2) else x for x in q))
    return result


def delete_value(p, value):
    return tuple(x-(x > value) for x in p if x != value)


def main():
    started = time.monotonic()
    for length in range(5, 102, 2):
        assert book_basis(length) == pratt_rotation_basis(length)
    previous = {()}
    rows = []
    for n in range(10):
        basis = book_basis(n)
        if n:
            avoid = {p for p in permutations(range(1, n+1))
                     if p not in basis and all(delete_value(p, value) in previous
                                               for value in range(1, n+1))}
        else:
            avoid = {()}
        actual, states = obtainable(n, 'general')
        assert actual == avoid, (n, next(iter(actual ^ avoid)))
        assert all(all(delete_value(p, v) in previous for v in range(1, n+1))
                   for p in basis)
        previous = avoid
        row = dict(n=n, count=len(actual), operation_states=states,
                   minimal_basis_patterns=[list(p) for p in sorted(basis)])
        rows.append(row)
        print(json.dumps(row), flush=True)
    result = dict(status='passed', rows=rows,
                  book_vs_pratt_pattern_constructions_checked_odd_lengths=[5, 101],
                  elapsed_seconds=round(time.monotonic()-started, 3),
                  peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  scope='All permutations up to length 9; no claim of an independent proof of the infinite basis.')
    dest = Path(__file__).resolve().parent/'results/deque-basis.json'
    dest.write_text(json.dumps(result, indent=2)+'\n')
    print('All bounded basis checks passed.', flush=True)


if __name__ == '__main__':
    main()
