"""One six-bit counterexample; enumerate only its seven auxiliary bits."""
import itertools
import json
from pathlib import Path

n, r = 6, 3
x = [0, 1, 1, 1, 1, 1]
ids = {(2, 1): 7, (2, 2): 8, (2, 3): 9,
       (3, 1): 10, (3, 2): 11, (4, 1): 12, (4, 2): 13}
def b(k, j): return ids[k, j]
def cnf(offset):
    cs = []
    for k in (3, 4):
        a = 2*k - n + 1 + offset
        cs += [[-a, -(a+1), b(k, 1)],
               [-(a+1), -(a+2), b(k, 1)],
               [-a, -(a+1), -(a+2), b(k, 2)]]
    cs += [[-b(4, 1), b(2, 1)], [-1, -2, b(2, 1)],
           [-b(4, 2), b(2, 2)], [-b(4, 1), -1, -2, b(2, 2)],
           [-b(4, 2), -1, -2, b(2, 3)],
           [-b(2, 2), -b(3, 2)], [-b(2, 3), -b(3, 1)]]
    return cs
def models(cs):
    out = []
    for aux in itertools.product((0, 1), repeat=7):
        values = [None] + x + list(aux)
        if all(any(values[abs(l)] == int(l > 0) for l in c) for c in cs):
            out.append(aux)
    return out
old, repaired = models(cnf(0)), models(cnf(1))
assert len(cnf(0)) == 13 and old and not repaired
assert sum(a*b for a, b in zip(x, x[1:])) == 4 > r
d = {'n_input_bits': n, 'leaf_count': n-1, 'bound': r, 'input': x,
     'actual_adjacent_11_count': 4, 'clauses_per_encoding': 13,
     'auxiliary_assignments_per_encoding': 128,
     'printed_models': old, 'repaired_models': repaired,
     'printed_cnf': cnf(0), 'repaired_cnf': cnf(1),
     'auxiliary_order': ['b2_1','b2_2','b2_3','b3_1','b3_2','b4_1','b4_2']}
p = Path(__file__).parent / 'results/bookwise-sat117.json'
p.write_text(json.dumps(d, indent=2)+'\n')
print(json.dumps({k:v for k,v in d.items() if 'cnf' not in k}))
