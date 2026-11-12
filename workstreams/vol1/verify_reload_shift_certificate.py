"""Independently check a finite invariant for the reload/one-shift family.

Read the frozen certificate; do not run or import its state generator.
Each operation is a ten-coordinate selection map, not a string slice.
"""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERTIFICATE = ROOT / "parallel/mix-optimality/results/reload-shift-closure-states.json"


def coordinate_map(width, delta, circular):
    mapping = []
    for destination in range(10):
        if destination >= width:
            mapping.append(destination)
            continue
        source = destination + delta
        if circular:
            source %= width
        mapping.append(source if 0 <= source < width else 10)
    return tuple(mapping)


def main():
    raw = CERTIFICATE.read_bytes()
    certificate = json.loads(raw)
    alphabet = "0abcdevwxyz"
    assert certificate["alphabet"] == alphabet

    def decode(word, size):
        assert len(word) == size and set(word) <= set(alphabet)
        return tuple(alphabet.index(char) for char in word)

    states = {decode(word, 5) for word in certificate["reached_x"]}
    pairs = {decode(word, 10) for word in certificate["reached_pairs"]}
    assert len(states) == len(certificate["reached_x"])
    assert len(pairs) == len(certificate["reached_pairs"])
    initial = decode("vwxyz", 5)
    restored_a = decode("abcde", 5)
    target = decode("edcba", 5)
    assert initial in states and target not in states

    # Positive delta selects bytes on the right (left shift).
    # Coordinate10 is a permanent zero. Unchanged X has coordinates5..9.
    maps = [coordinate_map(width, delta, circular)
            for width, circular in [(5, False), (10, False), (10, True)]
            for direction in (1, -1)
            for distance in range(11)
            for delta in [direction * distance]]
    assert len(maps) == 66

    actual_pairs = set()
    graph = {}
    for state in states:
        source = restored_a + state + (0,)
        outputs = {tuple(source[index] for index in mapping) for mapping in maps}
        assert outputs <= pairs
        successors = {output[5:] for output in outputs}
        assert successors <= states
        graph[state] = successors
        actual_pairs.update(outputs)
    assert actual_pairs == pairs

    # Closure alone suffices for the negative result. This also verifies
    # the stronger reported claim that every listed state is reachable.
    reached = {initial}
    frontier = {initial}
    while frontier:
        following = set().union(*(graph[state] for state in frontier)) - reached
        reached.update(following)
        frontier = following
    assert reached == states

    for pair in pairs:
        assert pair[:5] != target
        source = pair + (0,)
        for mapping in maps:
            assert tuple(source[index] for index in mapping[:5]) != target

    result = {
        "result": "verified",
        "method": "independent coordinate selection maps; certificate closure and reachability",
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "states": len(states),
        "pairs": len(pairs),
        "transition_checks": len(states) * len(maps),
        "final_shift_checks": len(pairs) * len(maps),
        "generator_rerun": False,
        "global_space_minimum_claimed": False,
    }
    (ROOT / "results/reload-shift-independent-review.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
