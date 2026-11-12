"""Check the specific n=6 counterexample to answer 7.2.1.7-27."""
from collections import Counter
from itertools import permutations
import json


def restricted_growth(prefix, n):
    if len(prefix) == n:
        yield prefix
        return
    for digit in range(max(prefix, default=-1) + 2):
        yield from restricted_growth(prefix + (digit,), n)


def crossings(blocks, order):
    # Block heights increase in order; each block has one horizontal bar.
    height = {block: rank for rank, block in enumerate(order)}
    return sum(
        sum(min(lower) < point < max(lower) for point in upper)
        for i, lower in enumerate(blocks)
        for j, upper in enumerate(blocks)
        if height[j] > height[i]
    )


counts = Counter()
single_by_blocks = Counter()
for word in restricted_growth((), 6):
    blocks = [tuple(i + 1 for i, digit in enumerate(word) if digit == block)
              for block in range(max(word) + 1)]
    minimum = min(crossings(blocks, order)
                  for order in permutations(range(len(blocks))))
    counts[minimum] += 1
    if minimum == 1:
        single_by_blocks[len(blocks)] += 1

print(json.dumps({
    "n": 6,
    "minimum_crossing_counts": dict(sorted(counts.items())),
    "single_crossing_by_number_of_blocks": dict(sorted(single_by_blocks.items())),
    "printed_single_crossing_count": 63,
    "actual_single_crossing_count": counts[1],
    "actual_at_most_one_crossing_count": counts[0] + counts[1],
    "omitted_partition": [[1, 6], [2, 4], [3, 5]],
    "omitted_partition_crossings_at_heights_3_1_2": crossings(
        [(1, 6), (2, 4), (3, 5)], (1, 2, 0)),
}, indent=2))
