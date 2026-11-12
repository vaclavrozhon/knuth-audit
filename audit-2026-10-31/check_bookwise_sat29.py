"""Only the explicit six-bit counterexample to SAT answer 29."""
import itertools
import json
from pathlib import Path


def check(caps, x):
    n, r = len(caps), caps[-1]
    variables = {(j, k) for j in range(1, n-r+1)
                 for k in range(1, r+1)}
    units = {(i-cap, cap+1) for i, cap in enumerate(caps, 1)
             if i > cap and cap < r}
    outside = units - variables
    keys = sorted(variables | units)

    def valid(values):
        def s(j, k):
            if k == 0:
                return 1
            if k == r+1 or j == 0:
                return 0
            return values[j, k]
        return (
            all(not s(j, k) or s(j+1, k)
                for j in range(1, n-r) for k in range(1, r+1))
            and all(not x[j+k-1] or not s(j, k) or s(j, k+1)
                    for j in range(1, n-r+1) for k in range(r+1))
            and all(not values[u] for u in units)
        )

    witness = next((dict(zip(keys, bits))
                    for bits in itertools.product((0, 1), repeat=len(keys))
                    if valid(dict(zip(keys, bits)))), None)
    return {
        'caps': caps, 'x': x, 'declared_auxiliaries': len(variables),
        'out_of_range_units_j_k': sorted(outside),
        'violated_prefixes': [i for i, cap in enumerate(caps, 1)
                              if sum(x[:i]) > cap],
        'satisfying_auxiliaries': None if witness is None else
            {f's_{j}^{k}': v for (j, k), v in witness.items()},
    }


x = [1, 0, 1, 0, 0, 0]
original = check([1, 1, 1, 3, 4, 5], x)
normalized = check([1, 1, 1, 2, 3, 4], x)
assert original['out_of_range_units_j_k'] == [(2, 2)]
assert original['violated_prefixes'] == [3]
assert original['satisfying_auxiliaries'] is not None
assert normalized['out_of_range_units_j_k'] == []
assert normalized['satisfying_auxiliaries'] is None
result = {'printed_recipe': original, 'after_cap_normalization': normalized,
          'scope': 'Two encodings of one fixed six-bit assignment; no general census.'}
path = Path(__file__).parent / 'results/bookwise-sat29.json'
path.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
