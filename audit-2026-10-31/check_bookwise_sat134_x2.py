"""Two fixed state witnesses; no SAT search or allocator census."""
import json
from pathlib import Path

# SAT134 explicitly stores K in addition to capacity.
state = {'ADDR': 0, 'CAP': 4, 'K': 2, 'BSIZE': 4}
first = dict(state, CAP=2 ** (state['K'] + 1))
assert first['CAP'] != 2 ** first['K']
second = dict(first, BSIZE=8)
printed_request = 2 ** (second['K'] + 1)
correct_request = 2 * second['CAP']
assert printed_request == 8 and correct_request == 16
assert second['BSIZE'] + 1 > printed_request

# Reachable X2 entry after input unit clauses x2 and x3, with (x1 or x2).
RT = 2**32 - 2
before = {1: 0, 2: RT, 3: RT}
free_variables = [1]
free_literals = [2*x+b for x in free_variables for b in [0, 1]]
printed = before.copy()
corrected = before.copy()
for literal in free_literals:
    printed[literal] = 0
    corrected[literal // 2] = 0
assert printed[2] == printed[3] == 0
assert corrected == before
result = {
    'sat134': {'initial': state, 'after_first_resize_as_printed': first,
               'next_full_size': second['BSIZE'],
               'printed_second_requested_capacity': printed_request,
               'correct_second_requested_capacity': correct_request},
    'x2': {'clauses': [[2], [3], [1, 2]], 'F': 2,
           'free_variables': free_variables, 'encoded_free_literals': free_literals,
           'before_VAL': before, 'printed_after_VAL': printed,
           'corrected_after_VAL': corrected,
           'effect': 'Both really true variables are erased; the free variable is not the addressed entry.'}
}
p = Path(__file__).parent / 'results/bookwise-sat134-x2.json'
p.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
