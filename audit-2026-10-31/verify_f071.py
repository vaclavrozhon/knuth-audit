"""A short arithmetic certificate for the changed first branch in F071.

Run with standard Python. This does not enumerate a search tree or reproduce
memory-access counts; changing the first branch already refutes equivalence.
"""
from datetime import datetime, timezone
from hashlib import sha256
from math import comb
from pathlib import Path
import argparse
import json
import time


def verify():
    root = Path(__file__).resolve().parent
    start = time.monotonic()
    result = []
    hashes = {}
    for upper_a in [4, 5]:
        path = root / f'results/mcc_arithmetic/upper-bound-a{upper_a}.mcc'
        data = path.read_bytes()
        hashes[str(path.relative_to(root))] = sha256(data).hexdigest()
        lines = data.decode().splitlines()
        primary = {}
        for token in lines[0].split():
            if token == '|':
                break
            bounds, name = token.split('|')
            lo, hi = map(int, bounds.split(':'))
            primary[name] = (lo, hi)
        options = [line.split() for line in lines[1:] if line.strip()]
        assert primary == {'A': (1, upper_a), 'B': (2, 6)}
        assert options == [['A', 'X'], ['A', 'Y'], ['B', 'U'], ['B', 'V'], ['B', 'W']]
        choices = []
        for order, (name, (lo, hi)) in enumerate(primary.items()):
            length = sum(name in option for option in options)
            slack = hi-lo
            degree = max(length+1-max(hi-slack, 0), 0)
            assert hi >= length+2
            assert slack <= hi  # native clipped slack is the same at this root
            choices.append(dict(item=name, length=length, lower=lo, upper=hi, slack=slack,
                                degree=degree, key=(degree, slack, -length, order)))
        selected = min(choices, key=lambda x: x['key'])['item']
        expected = 'A' if upper_a == 4 else 'B'
        assert selected == expected
        # The two disjoint option groups give a direct product count.
        solution_count = sum(comb(2, k) for k in range(1, 3))*sum(comb(3, k) for k in range(2, 4))
        assert solution_count == 12
        result.append(dict(upper_A=upper_a, choices=choices, first_item=selected,
                           solutions_by_product_formula=solution_count))
    assert result[0]['first_item'] != result[1]['first_item']
    return dict(at_utc=datetime.now(timezone.utc).isoformat(), checker_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        witness_hashes=hashes, cases=result, different_first_branch=True, new_searches=0,
        historical_mems_reproduced=False, seconds=time.monotonic()-start)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = verify()
    if args.output:
        assert not args.output.exists(), 'Do not overwrite an accepted certificate.'
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS F071: upper_A=4 chooses A; upper_A=5 chooses B. Both bounds exceed M_A+1.')
    print('Both problems have 12 solutions by a product formula. No search or benchmark was run.')
