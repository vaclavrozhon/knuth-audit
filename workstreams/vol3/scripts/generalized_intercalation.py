"""Targeted constructive check of TAOCP 5.1.2-24, corrected conventions."""

import json


def transpose(columns, index, preserves):
    w, y = columns[index]
    x, z = columns[index + 1]
    if w != x and y != z and preserves(frozenset((w, x)), frozenset((y, z))):
        columns[index:index + 2] = [(x, y), (w, z)]
    else:
        columns[index:index + 2] = [(x, z), (w, y)]


def sort_columns(columns, preserves):
    columns = list(columns)
    while True:
        index = next((i for i in range(len(columns) - 2, -1, -1)
                      if columns[i][0] > columns[i + 1][0]), None)
        if index is None:
            return columns
        transpose(columns, index, preserves)


def expose(columns, top, preserves):
    columns = list(columns)
    index = next(i for i, column in enumerate(columns) if column[0] == top)
    for i in range(index - 1, -1, -1):
        transpose(columns, i, preserves)
    return columns[0][1], columns[1:]


def factor(columns, preserves):
    columns = list(columns)
    factors = []
    while columns:
        start = columns[0][0]
        at = start
        cycle = []
        while True:
            at, columns = expose(columns, at, preserves)
            cycle.append(at)
            if at == start:
                break
        factors.append(tuple(cycle))
    return factors


def raw_cycle(cycle):
    # Corrected exercise24 associates this unsorted array with cycle notation.
    return list(zip(cycle[-1:] + cycle[:-1], cycle))


def reconstruct(factors, preserves):
    result = []
    for cycle in reversed(factors):
        result = sort_columns(raw_cycle(cycle) + result, preserves)
    return result


if __name__ == "__main__":
    word = "dbcbcacdaddbbbd"
    columns = list(zip(sorted(word), word))
    disjoint_pairs = lambda top, bottom: len(top | bottom) == 4
    factors = factor(columns, disjoint_pairs)
    expected = ["ddbca", "cbba", "cdb", "db", "d"]
    assert ["".join(c) for c in factors] == expected
    assert reconstruct(factors, disjoint_pairs) == columns

    # A separate explicit mathematical witness, not a search over relations.
    unequal_pairs = lambda top, bottom: top != bottom
    a = [(1, 3), (3, 1)]
    b = [(2, 2)]
    c = [(1, 1)]
    product = lambda left, right: sort_columns(left + right, unequal_pairs)
    left = product(product(a, b), c)
    right = product(a, product(b, c))
    assert left == [(1, 3), (1, 2), (2, 1), (3, 1)]
    assert right == [(1, 3), (1, 1), (2, 1), (3, 2)]
    print(json.dumps({
        "scope": "One printed factorization and one explicit associativity witness; no enumeration",
        "printed_word": word,
        "printed_factorization": expected,
        "reconstruction": "passed",
        "nonassociativity": {
            "relation": "The unordered top pair differs from the unordered bottom pair",
            "a": a, "b": b, "c": c,
            "left": left, "right": right,
        },
        "status": "passed",
    }, ensure_ascii=False, indent=2))
