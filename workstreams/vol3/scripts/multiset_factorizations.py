"""Construct the factorizations in TAOCP 5.1.2 exercise9.

The word uses the ordinary sorted top row. reverse_priority changes only
the choice of the least cycle element, preserving that fixed two-line array.
The mathematical invariants are recorded in multisets-proof-01-11.md.
"""

from collections import deque
import json


def queues(word):
    result = {}
    for top, bottom in zip(sorted(word), word):
        result.setdefault(top, deque()).append(bottom)
    return result


def canonical(word, *, reverse_priority=False):
    pending = queues(word)
    priority = sorted(pending, reverse=reverse_priority)
    factors = []
    while any(pending.values()):
        start = next(x for x in priority if pending[x])
        at = start
        cycle = []
        while True:
            at = pending[at].popleft()
            cycle.append(at)
            if at == start:
                break
        factors.append(tuple(cycle))
    return factors


def primes(word):
    pending = queues(word)
    priority = sorted(pending)
    factors = []
    while any(pending.values()):
        at = next(x for x in priority if pending[x])
        positions = {}
        path = []
        # Follow the functional graph of first queue entries without consuming.
        while at not in positions:
            positions[at] = len(path)
            path.append(at)
            at = pending[at][0]
        cycle = path[positions[at]:]
        for x in cycle:
            pending[x].popleft()
        # Simple cycles may be rotated; print their least letter first.
        cut = cycle.index(min(cycle))
        cycle = cycle[cut:] + cycle[:cut]
        factors.append(tuple(cycle))
    return factors


def intercalate_cycles(factors):
    result = {}
    for cycle in factors:
        if not cycle:
            raise ValueError("Cycles must be nonempty")
        for i, top in enumerate(cycle):
            result.setdefault(top, []).append(cycle[(i + 1) % len(cycle)])
    return tuple(y for x in sorted(result) for y in result[x])


if __name__ == "__main__":
    word = "dbcbcacdaddbbbd"
    expected = {
        "canonical": ["ddbcdbbca", "ba", "cdb", "d"],
        "reverse_priority": ["d", "bcd", "bbcad", "babcd", "d"],
        "primes": ["d", "bcd", "b", "adbc", "ab", "bcd", "d"],
    }
    computed = {
        "canonical": canonical(word),
        "reverse_priority": canonical(word, reverse_priority=True),
        "primes": primes(word),
    }
    for kind, factors in computed.items():
        assert ["".join(c) for c in factors] == expected[kind], kind
        assert intercalate_cycles(factors) == tuple(word), kind
    assert canonical(()) == primes(()) == []
    print(json.dumps({
        "scope": "One printed15-letter example; no enumeration",
        "input": word,
        "factorizations": expected,
        "reconstruction": "All three products equal the printed input",
        "empty_input": "Both factorizations return the empty list",
        "status": "passed",
    }, ensure_ascii=False, indent=2))
