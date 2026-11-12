"""Direct construction for TAOCP 4A, 7.1.1 exercise 84.

The proof is in notes/proof-079-five-variable-median-algebra.md.
This program has not been run as a census. Variables v,w,x,y,z
are bits 0,1,2,3,4 of an input mask. Truth tables use masks 0..31.
"""

from itertools import combinations
import json


NAMES = "vwxyz"
FULL = 31
PAIRS = tuple((1 << i) | (1 << j) for i, j in combinations(range(5), 2))
COORDINATES = tuple(1 << i for i in range(5)) + PAIRS


def vertex_specs():
    """Yield each structural class exactly once, in the printed type order."""
    for center in range(5):
        yield 1, center, frozenset()
    for center in range(5):
        others = [j for j in range(5) if j != center]
        yield 2, None, frozenset((1 << center) | (1 << j) for j in others)
    for center in range(5):
        others = [j for j in range(5) if j != center]
        for leaves in combinations(others, 3):
            yield 3, None, frozenset((1 << center) | (1 << j) for j in leaves)
    for center in range(5):
        others = [j for j in range(5) if j != center]
        for leaves in combinations(others, 2):
            yield 4, None, frozenset((1 << center) | (1 << j) for j in leaves)
    for pair in PAIRS:
        yield 5, None, frozenset((pair,))
    yield 6, None, frozenset()
    for triple in combinations(range(5), 3):
        yield 7, None, frozenset(
            (1 << i) | (1 << j) for i, j in combinations(triple, 2)
        )


def value(mask, dictator, pairs):
    if dictator is not None:
        return (mask >> dictator) & 1
    size = mask.bit_count()
    if size <= 1:
        return 0
    if size == 2:
        return int(mask in pairs)
    if size == 3:
        return int((FULL ^ mask) not in pairs)
    return 1


def construct():
    vertices = []
    labels = []
    for kind, dictator, pairs in vertex_specs():
        label = sum(
            value(mask, dictator, pairs) << k
            for k, mask in enumerate(COORDINATES)
        )
        labels.append(label)
        vertices.append({
            "id": len(vertices),
            "type": kind,
            "dictator": None if dictator is None else NAMES[dictator],
            "winning_pairs": [
                "".join(NAMES[j] for j in range(5) if mask & (1 << j))
                for mask in sorted(pairs)
            ] if dictator is None else None,
            "label": "".join(str((label >> k) & 1) for k in range(15)),
            "truth_table": "".join(
                str(value(mask, dictator, pairs)) for mask in range(32)
            ),
        })
    index = {label: i for i, label in enumerate(labels)}
    edges = []
    for i, label in enumerate(labels):
        for k in range(15):
            j = index.get(label ^ (1 << k))
            if j is not None and i < j:
                edges.append([i, j])
    return {"variables": NAMES, "vertices": vertices, "edges": edges}


if __name__ == "__main__":
    print(json.dumps(construct(), indent=2))
