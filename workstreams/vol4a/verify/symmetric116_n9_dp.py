"""Exact arithmetic certificate for one exercise, n=9; no function census.

The recurrence and completeness proof are in proof-100.  This script only
evaluates its ten rows, retaining every candidate and a maximizing witness.
"""

import json
from math import comb
from pathlib import Path

n = 9
best = {-2: 0, -1: 0}
words = {-2: "", -1: ""}
rows = []
for m in range(n + 1):
    candidates = []
    for k in range(m + 1):
        run_count = comb(n, m) * comb(m, k)
        candidates.append({"k": k, "run_count": run_count,
                           "earlier": best[k - 2],
                           "total": run_count + best[k - 2]})
    best[m] = max(best[m - 1], *(c["total"] for c in candidates))
    choice = next((c for c in candidates if c["total"] == best[m]), None)
    if choice is None:
        words[m] = words[m - 1] + "0"
    else:
        k = choice["k"]
        prefix = (words[k - 2] + "0") if k else ""
        words[m] = prefix + "1" * (m - k + 1)
    rows.append({"m": m, "zero_last": best[m - 1],
                 "candidates": candidates, "maximum": best[m],
                 "prefix_witness": words[m]})

result = {"n": n, "method": "ten-row dynamic program; no truth-table enumeration",
          "rows": rows, "maximum": best[n], "witness": words[n]}
out = Path(__file__).resolve().parents[1] / "results" / "symmetric116-n9-dp.json"
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"n": n, "maxima": [best[m] for m in range(n + 1)],
                  "maximum": best[n], "witness": words[n]}))
