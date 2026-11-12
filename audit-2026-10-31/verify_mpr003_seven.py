"""Exact MPR3 optimum over seven spot values, using the every-roll condition.

The 126-support prepass was completed separately and saved. --resume-supports
uses that saved result without repeating it. A fresh authorized reproduction
can omit the flag. Neither mode starts an unrestricted triple census.
"""
from collections import defaultdict
from datetime import datetime, timezone
from itertools import combinations_with_replacement, product
from pathlib import Path
import argparse
import json
import math
import os
import time

ROOT = Path(__file__).resolve().parent


def profile_groups():
    groups = defaultdict(list)
    for die in combinations_with_replacement(range(1, 8), 6):
        mask = sum(1 << (x-1) for x in set(die))
        groups[mask].append(die)
    return groups


def support_prepass(groups):
    started = time.perf_counter()
    masks = sorted(groups)
    allowed_pair = {}
    for a in range(1, 8):
        for b in range(1, 8):
            mask = 0
            for c in range(1, 8):
                lo, mid, hi = sorted((a, b, c))
                if 2*mid > lo+hi:
                    mask |= 1 << (c-1)
            allowed_pair[a, b] = mask
    compatible, estimate = [], 0
    for ia, a in enumerate(masks):
        va = [v for v in range(1, 8) if a >> (v-1) & 1]
        for b in masks[ia:]:
            vb = [v for v in range(1, 8) if b >> (v-1) & 1]
            allowed = 127
            for x in va:
                for y in vb:
                    allowed &= allowed_pair[x, y]
            c = allowed
            while c:
                if c >= b and c in groups:
                    g = [len(groups[a]), len(groups[b]), len(groups[c])]
                    if a == b == c:
                        count = math.comb(g[0]+2, 3)
                    elif a == b:
                        count = math.comb(g[0]+1, 2)*g[2]
                    elif b == c:
                        count = g[0]*math.comb(g[1]+1, 2)
                    else:
                        count = math.prod(g)
                    compatible.append({"masks": [a, b, c], "profile_triples": count})
                    estimate += count
                c = (c-1) & allowed
    return {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Necessary and sufficient support-level condition that every possible roll has exactly two values above the arithmetic mean. No profile probabilities counted yet.",
        "dice_profiles": sum(map(len, groups.values())),
        "nonempty_supports": len(masks),
        "compatible_support_triples": compatible,
        "profile_triples_to_test": estimate,
        "elapsed_seconds": time.perf_counter()-started,
    }


def direct_counts(dice):
    above, below, equal = [0]*3, [0]*3, [0]*3
    multiplicities = [0]*4
    for roll in product(*dice):
        total = sum(roll)
        flags = [3*x > total for x in roll]
        for i, x in enumerate(roll):
            above[i] += flags[i]
            below[i] += 3*x < total
            equal[i] += 3*x == total
        multiplicities[sum(flags)] += 1
    return {"faces": dice, "above_counts": above, "below_counts": below,
            "equal_counts": equal, "rolls_by_number_above": multiplicities}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--resume-supports", action="store_true")
    args = parser.parse_args()
    started = time.perf_counter()
    groups = profile_groups()
    support_file = ROOT / "results/sequential/mpr-003-seven-supports.json"
    if args.resume_supports:
        support = json.loads(support_file.read_text())
    else:
        support = support_prepass(groups)
        support_file.write_text(json.dumps(support, indent=2)+"\n")
    assert support["dice_profiles"] == 924 and support["nonempty_supports"] == 126
    assert support["profile_triples_to_test"] <= 100000
    # P(D_i is below)=P(D_i is the unique minimum) on compatible supports.
    tails = {die: [sum(x > v for x in die) for v in range(1, 8)]
             for group in groups.values() for die in group}
    examined, solutions = 0, []
    for record in support["compatible_support_triples"]:
        a, b, c = record["masks"]
        before = examined
        for ia, da in enumerate(groups[a]):
            for ib, db in enumerate(groups[b]):
                if a == b and ib < ia:
                    continue
                for ic, dc in enumerate(groups[c]):
                    if b == c and ic < ib:
                        continue
                    examined += 1
                    below_a = sum(tails[db][v-1]*tails[dc][v-1] for v in da)
                    if below_a != 72:
                        continue
                    below_b = sum(tails[da][v-1]*tails[dc][v-1] for v in db)
                    if below_b != 72:
                        continue
                    below_c = sum(tails[da][v-1]*tails[db][v-1] for v in dc)
                    if below_c != 72:
                        continue
                    direct = direct_counts([da, db, dc])
                    assert direct["above_counts"] == [144]*3
                    assert direct["below_counts"] == [72]*3
                    assert direct["equal_counts"] == [0]*3
                    assert direct["rolls_by_number_above"] == [0, 0, 216, 0]
                    solutions.append(direct)
        assert examined-before == record["profile_triples"]
    assert examined == support["profile_triples_to_test"]
    printed_conventional = direct_counts([[3, 3, 3, 3, 3, 5],
                                         [4, 1, 4, 4, 1, 4],
                                         [4, 1, 4, 4, 1, 4]])
    printed_seven = direct_counts([[6, 6, 6, 6, 6, 6],
                                  [7, 1, 7, 7, 1, 7],
                                  [4, 4, 4, 7, 7, 7]])
    assert printed_conventional["above_counts"] == [136, 128, 128]
    assert printed_seven["above_counts"] == [144, 144, 144]
    result = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "All six-face dice over1..7 with all three above-average probabilities at least2/3, modulo arbitrary die-label permutations. Completeness uses the exact every-roll support condition.",
        "support_certificate": "results/sequential/mpr-003-seven-supports.json",
        "support_triples": len(support["compatible_support_triples"]),
        "profile_triples_examined": examined,
        "solutions": solutions,
        "solution_count": len(solutions),
        "printed_conventional": printed_conventional,
        "printed_seven": printed_seven,
        "elapsed_seconds": time.perf_counter()-started,
        "execution_nice": os.getpriority(os.PRIO_PROCESS, 0),
        "old_tests_repeated": 0,
    }
    (ROOT / "results/sequential/mpr-003-seven.json").write_text(
        json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: result[key] for key in ["support_triples",
        "profile_triples_examined", "solution_count", "elapsed_seconds", "execution_nice"]}))


if __name__ == "__main__":
    main()
