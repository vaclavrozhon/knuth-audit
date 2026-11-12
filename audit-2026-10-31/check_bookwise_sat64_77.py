"""Small fixed witnesses for two printed encodings; no network/Life census."""
import itertools
import json
from pathlib import Path

layers = [None, (1, 2), None, (0, 2)]
x = (1, 1, 0)
trace = [(1, 1, 0), (1, 1, 1), (1, 1, 1), (1, 1, 0), (0, 1, 1)]
clauses = []
for t, edge in enumerate(layers, 1):
    c = {(i, j): edge == (i, j) for i in range(3) for j in range(i + 1, 3)}
    b = [edge is not None and k in edge for k in range(3)]
    for k in range(3):
        a, d = [v for ij, v in c.items() if k in ij]
        clauses.extend([(not a, not d), (not a, b[k]),
                        (not d, b[k]), (a, d, not b[k])])
    p, v = trace[t - 1], trace[t]
    for (i, j), gate in c.items():
        clauses.extend([(not gate, not v[i], p[i]),
                        (not gate, not v[i], p[j]),
                        (not gate, v[i], not p[i], not p[j]),
                        (not gate, not v[j], p[i], p[j]),
                        (not gate, v[j], not p[i]),
                        (not gate, v[j], not p[j]),
                        (b[i], not v[i], p[i]),
                        (b[i], v[i], not p[i])])
assert len(clauses) == 144 and all(any(c) for c in clauses)
actual = x
actual_trace = [x]
for edge in layers:
    a = list(actual)
    if edge:
        i, j = edge
        a[i], a[j] = min(a[i], a[j]), max(a[i], a[j])
    actual = tuple(a)
    actual_trace.append(actual)
assert actual == (1, 0, 1) and trace[-1] == tuple(sorted(x))
violations = [t for t, e in enumerate(layers, 1)
              if (e is None or 2 not in e) and trace[t - 1][2] != trace[t][2]]
assert violations == [1, 3]

# The only unsorted outputs of the prefix [1:2] are 010 and 110.
# The former follows the real circuit to 001, and the latter uses the
# displayed false trace. Already sorted inputs use their constant traces.
prefix_outputs = set()
for a, b, c in itertools.product((0, 1), repeat=3):
    prefix_outputs.add((min(a, b), max(a, b), c))
assert {v for v in prefix_outputs if v != tuple(sorted(v))} == {(0, 1, 0), x}

mismatch = []
for f, g, h, i in itertools.product((0, 1), repeat=4):
    sums = f + g + h != 2 and g + h + i != 2 and h + i != 2
    printed = (not f or not g) and (not f or not h) and (not g or not i) and (not h or not i)
    repaired = printed and (not g or not h)
    assert repaired == sums
    if printed != sums:
        mismatch.append([f, g, h, i])
assert mismatch == [[0, 1, 1, 0]]

# This boundary tuple is compatible with a still life in the gray region:
# a 2x2 block in rows 6,7 and columns 5,6 of the book's 8x8 board.
block = {(6, 5), (6, 6), (7, 5), (7, 6)}
def life(s):
    cells = {(a + u, b + v) for a, b in s for u in (-1, 0, 1) for v in (-1, 0, 1)}
    def n(a, b):
        return sum((a + u, b + v) in s for u in (-1, 0, 1)
                   for v in (-1, 0, 1) if u or v)
    return {p for p in cells if n(*p) == 3 or (p in s and n(*p) == 2)}
assert life(block) == block
assert [int((r, 5) in block) for r in range(5, 9)] == mismatch[0]

result = {'sat64': {'n': 3, 'layers_one_based': [None, [2, 3], None, [1, 3]],
                    'input': x, 'false_trace': trace, 'actual_trace': actual_trace,
                    'printed_clauses_satisfied': len(clauses),
                    'missing_idle_clause_violations_at_steps': violations,
                    'compatible_prefix': '[1:2]'},
          'sat77': {'four_bit_assignments_checked': 16, 'sole_extra_assignment': mismatch[0],
                    'repair': 'add (not g or not h)',
                    'compatible_still_life': sorted(block),
                    'scope': 'Local inequality/CNF equivalence, not a claim that this block is a four-step eater.'}}
out = Path(__file__).parent / 'results/bookwise-sat64-77.json'
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
