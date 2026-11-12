"""Isolate two omissions in SAT175 using fixed local lookahead traces.

Signed integers denote literals (1=a,...,5=e), independent of the book's
encoded storage values. This is a local queue/count model, not a full solver.
"""
import json
from pathlib import Path


def trace(clause, implications, looks, preserve_prefix, decrement_unit):
    vals = {}
    stack = []
    size = len(clause)
    history = []
    for lit, degree in looks:
        restored = []
        while stack and vals[abs(stack[-1])][0] < degree:
            u = stack.pop()
            if -u in clause:
                size += 1
            restored.append(u)
        inherited = stack.copy()
        if not preserve_prefix:
            stack.clear()  # unchanged first line of (72), F=0
        cursor = len(stack)

        def status(u):
            old_degree, old_sign = vals.get(abs(u), (0, False))
            return None if old_degree < degree else old_sign == (u > 0)

        def add(u):
            state = status(u)
            assert state is not False
            if state is None:
                vals[abs(u)] = (degree, u > 0)
                stack.append(u)
                for v in implications.get(u, []):
                    add(v)

        add(lit)
        decisions = []
        while cursor < len(stack):
            u = stack[cursor]
            cursor += 1
            if -u not in clause:
                continue
            s = size - 1
            if decrement_unit or s >= 2:
                size = s
            free = [v for v in clause if status(v) is None]
            true = [v for v in clause if status(v) is True]
            decisions.append({'processed': u, 'candidate_size': s,
                              'stored_size': size, 'unfixed': free, 'true': true})
            if s < 2 and not true and len(free) == 1:
                add(free[0])
        history.append({'literal': lit, 'degree': degree, 'restored': restored,
                        'retained_before_reset': inherited, 'stack': stack.copy(),
                        'stored_size': size, 'decisions': decisions})
    return history

# Valid forest pieces: a <- b and not-d <- not-c. Higher offsets retire roots.
big = [-1, 3, 4, 5]
bimp = {2: [1], -1: [-2], -3: [-4], 4: [3]}
looks = [(1, 4), (2, 2), (-4, 8), (-3, 6)]
bad_prefix = trace(big, bimp, looks, False, True)
good_prefix = trace(big, bimp, looks, True, True)
assert bad_prefix[-1]['decisions'][-1]['candidate_size'] == 1
assert bad_prefix[-1]['decisions'][-1]['unfixed'] == [-1, 5]
assert good_prefix[-1]['stored_size'] == 2

# Isolate count restoration with the prefix issue already repaired.
# not-a implies not-b; the ternary clause then forces c.
ternary = [1, 2, 3]
bad_count = trace(ternary, {-1: [-2], 2: [1]}, [(-1, 2), (4, 4)], True, False)
good_count = trace(ternary, {-1: [-2], 2: [1]}, [(-1, 2), (4, 4)], True, True)
assert bad_count[0]['stored_size'] == 2
assert bad_count[1]['stored_size'] == 4
assert good_count[1]['stored_size'] == 3
result = {'prefix': {'printed': bad_prefix, 'corrected': good_prefix},
          'unit_count': {'printed': bad_count, 'corrected': good_count},
          'scope': 'Two local state invariants, tested independently. The prefix case uses unconditional decrement to isolate that omission; the count case preserves the prefix.'}
(Path(__file__).parent / 'results/bookwise-sat175.json').write_text(json.dumps(result, indent=2) + '\n')
print('Prefix witness: candidate size 1 but two unfixed literals; corrected size 2.')
print('Unit-count witness: restored size 4 versus original/correct size 3.')
