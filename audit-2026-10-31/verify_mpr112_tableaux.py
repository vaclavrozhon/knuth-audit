#!/usr/bin/env python3
"""Exact bounded check of six printed twelve-row tableaux and local repairs.

Zero denotes a blank/infinity. A row whose selected images are all zero
chooses uniformly among the selected positions, as the exercise specifies.
No construction search, general-n enumeration, or old-run restart.
"""
from datetime import datetime, timezone
from fractions import Fraction
from itertools import combinations
from collections import Counter
from pathlib import Path
from time import perf_counter
import json
import os

BASE = Path(__file__).resolve().parent
START = perf_counter()
TABLES = {
    "initial_m1": "1000 1000 1000 0100 0100 0100 0010 0010 0010 0001 0001 0001",
    "after_2": "1200 1020 1002 0120 0102 2100 0012 2010 0210 2001 0201 0021",
    "first_A34_branch": "1230 1020 1302 0123 0102 2103 3012 2010 0213 2301 0201 3021",
    "second_A34_branch": "1203 1020 1302 3120 0102 2130 0312 2010 0213 2031 0201 3021",
    "first_A24_branch": "1230 1320 1302 0123 0132 2103 3012 2013 0213 2301 3201 3021",
    "second_A24_branch": "1230 1023 1302 0123 3102 2103 3012 2310 0213 2301 0231 3021",
}
BAD = {"first_A34_branch", "first_A24_branch", "second_A24_branch"}

def check(words):
    rows = [tuple(map(int, w)) for w in words]
    assert len(rows) == 12 and all(len(r) == 4 for r in rows)
    for row in rows:
        finite = sorted(x for x in row if x)
        assert finite == list(range(1, len(finite) + 1))
    conditions = []
    for k in range(1, 5):
        for subset in combinations(range(1, 5), k):
            counts = {a: Fraction(0) for a in subset}
            for row in rows:
                minimum = min((row[a - 1] for a in subset if row[a - 1]), default=0)
                if minimum:
                    winner = next(a for a in subset if row[a - 1] == minimum)
                    counts[winner] += 1
                else:
                    for a in subset:
                        counts[a] += Fraction(1, k)
            probabilities = {a: count / 12 for a, count in counts.items()}
            conditions.append({"subset": list(subset),
                               "probabilities": {a: str(v) for a, v in probabilities.items()},
                               "valid": all(v == Fraction(1, k) for v in probabilities.values())})
    multiset = Counter(rows)
    rotated = Counter(r[-1:] + r[:-1] for r in rows)
    fixed_orbits = all(rows[j + 3 * t] == rows[j][-t:] + rows[j][:-t]
                       for j in range(3) for t in range(1, 4))
    return {"rows": words, "minwise": all(x["valid"] for x in conditions),
            "cyclic_multiset": multiset == rotated, "indexed_cyclic_orbits": fixed_orbits,
            "distinct_rows": len(multiset), "conditions": conditions}

results = {}
for name, text in TABLES.items():
    words = text.split()
    result = check(words)
    assert result["minwise"] == (name not in BAD)
    assert result["cyclic_multiset"] == (name not in BAD)
    assert result["indexed_cyclic_orbits"] == (name not in BAD)
    results[name] = result
    if name in BAD:
        witness = next(x for x in result["conditions"] if x["subset"] == [2, 3])
        assert witness["probabilities"] == {2: "7/12", 3: "5/12"}
        corrected = words.copy()
        for index, old, new in [(2, "1302", "1032"), (8, "0213", "3210"), (11, "3021", "0321")]:
            assert corrected[index] == old
            corrected[index] = new
        repair = check(corrected)
        assert repair["minwise"] and repair["cyclic_multiset"] and repair["indexed_cyclic_orbits"]
        results[name + "_repaired"] = repair
        if "A24" in name:
            final_bad = check([w.replace("0", "4") for w in words])
            final_good = check([w.replace("0", "4") for w in corrected])
            assert not final_bad["minwise"] and final_bad["distinct_rows"] == 12
            assert final_good["minwise"] and final_good["distinct_rows"] == 12
            results[name + "_completed_as_printed"] = final_bad
            results[name + "_completed_after_repair"] = final_good

result = {"at_utc": datetime.now(timezone.utc).isoformat(),
          "scope": "Six printed tableaux, three exact local repairs, four final completions; all15nonempty subsets per tableau",
          "nice": os.getpriority(os.PRIO_PROCESS, 0), "seconds": perf_counter() - START,
          "tableau_checks": len(results), "all_expected_results_passed": True,
          "results": results}
assert result["nice"] >= 15
destination = BASE / "results/sequential/mpr-112-tableaux-certificate.json"
assert not destination.exists(), "Do not overwrite or rerun a successful certificate."
destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "results"}))
