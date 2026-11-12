"""Small exact finite certificate for MPR1, no random search or solver.

Every six-face multiset over the conventional spot values1..6 occurs once.
Three-cycles in the strict-win graph certify the printed uniqueness claim.
General Fibonacci/asymptotic statements have separate symbolic arguments.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path
import json
import math
import time


def wins(a, b):
    return sum(x > y for x in a for y in b)


def audit_displayed(dice):
    rows = []
    for i in range(3):
        a, b = dice[i], dice[(i + 1) % 3]
        per_face = [sum(x > y for y in b) for x in a]
        rows.append({"winner": "ABC"[i], "loser": "ABC"[(i+1) % 3],
                     "per_face_wins": per_face,
                     "wins": sum(per_face),
                     "probability": str(Fraction(sum(per_face), 36))})
    return {"faces_in_printed_order": dict(zip("ABC", dice)), "comparisons": rows}


def main():
    started = time.perf_counter()
    question = audit_displayed([[5, 1, 5, 5, 1, 5],
                               [4, 3, 4, 4, 3, 6],
                               [3, 2, 3, 6, 2, 6]])
    answer = audit_displayed([[3, 3, 3, 3, 3, 6],
                             [2, 2, 2, 5, 5, 5],
                             [1, 4, 4, 4, 4, 4]])
    assert [x["per_face_wins"] for x in question["comparisons"]] == [
        [5, 0, 5, 5, 0, 5], [4, 2, 4, 4, 2, 4], [2, 2, 2, 6, 2, 6]]
    assert all(x["wins"] == 20 for x in question["comparisons"])
    assert [x["wins"] for x in answer["comparisons"]] == [21, 21, 25]

    dice = list(combinations_with_replacement(range(1, 7), 6))
    assert len(dice) == math.comb(11, 6) == 462
    counts = [Counter(d) for d in dice]
    prefix = [[sum(d[v] for v in range(1, x)) for x in range(1, 7)]
              for d in counts]
    out = [0] * len(dice)
    incoming = [0] * len(dice)
    edge_count = 0
    for a, hist in enumerate(counts):
        for b, cumulative in enumerate(prefix):
            # Exact number of winning ordered face pairs. Each pair is equiprobable.
            score = sum(hist[x] * cumulative[x-1] for x in range(1, 7))
            if score >= 21:  # equivalent to probability strictly greater than5/9
                out[a] |= 1 << b
                incoming[b] |= 1 << a
                edge_count += 1

    triples = []
    all_bits = (1 << len(dice)) - 1
    for a in range(len(dice)):
        greater = all_bits ^ ((1 << (a + 1)) - 1)
        bs = out[a] & greater
        while bs:
            bit = bs & -bs
            b = bit.bit_length() - 1
            bs ^= bit
            cs = out[b] & incoming[a] & greater
            while cs:
                bit = cs & -cs
                c = bit.bit_length() - 1
                cs ^= bit
                # a is the unique minimum index: one representative per cyclic labeling.
                triples.append([dice[a], dice[b], dice[c]])

    assert len(triples) == 1, triples
    expected = [tuple(answer["faces_in_printed_order"][k]) for k in "ABC"]
    assert any(list(map(tuple, triples[0])) == expected[j:] + expected[:j]
               for j in range(3))
    result = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Complete finite claim1(b) over six equiprobable faces with values1..6; face permutations ignored and die labels identified only under cyclic rotation.",
        "question_1a": question,
        "answer_1b": answer,
        "dice_count": len(dice),
        "directed_pairs_examined": len(dice) ** 2,
        "strict_win_edges": edge_count,
        "cycles_modulo_cyclic_relabeling": triples,
        "cyclic_orbit_count": len(triples),
        "labeled_cycle_count": 3 * len(triples),
        "method": "Complete weakly increasing face tuples, exact histogram pair scores, bit intersections for every directed triangle; no stochastic sampling.",
        "elapsed_seconds": time.perf_counter() - started,
        "long_search": False,
        "old_tests_repeated": 0,
    }
    root = Path(__file__).resolve().parent
    (root / "results/sequential/mpr-001-dice.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["dice_count", "strict_win_edges",
                                            "cyclic_orbit_count", "elapsed_seconds"]}))


if __name__ == "__main__":
    main()
