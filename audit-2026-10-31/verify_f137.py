"""A standalone counterexample to TAOCP 4B, answer 7.2.2.1-143, p.455.

Run: python3 verify_f137.py. No solver, input files or third-party modules.
Coordinates (x,y) use two unit vectors at an angle of 60 degrees.
The 12-by-1 parallelogram contains two unit triangles in each of 12 cells.
Only rotations identify tile types; reflected triples remain distinct.
"""
from itertools import product

BOTTOM = "aabcabaddccdb"
TOP = "abbadccabcddb"


def cyclic_type(word):
    return min(word, word[1:] + word[:1], word[2:] + word[:2])


def verify():
    assert len(BOTTOM) == len(TOP) == 13
    assert set(BOTTOM + TOP) == set("abcd")
    inventory = {cyclic_type("".join(t)) for t in product("abcd", repeat=3)}
    actual = []
    for x in range(12):
        # Both triples are in counterclockwise order in the same plane.
        actual.append(cyclic_type(BOTTOM[x] + BOTTOM[x + 1] + TOP[x]))
        actual.append(cyclic_type(TOP[x + 1] + TOP[x] + BOTTOM[x + 1]))
    assert len(inventory) == len(actual) == len(set(actual)) == 24
    assert set(actual) == inventory
    return actual


if __name__ == "__main__":
    verify()
    print("PASS: 24 distinct rotational tile types, each used exactly once.")
    print("All shared vertices agree; the convex 12-by-1 strip is tileable.")
