#!/usr/bin/env python3
"""Exact 499-row certificate for the count in answer 1.3.1'-19.

The proof reduces all 2**64 dividends to one necessary and sufficient
integer inequality per divisor. This is not a search over dividends.
"""
from pathlib import Path
import json
import os

BASE = Path(__file__).resolve().parent


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Use nice -n 15."
    B = 1 << 64
    rows = []
    for z in range(3, 1000, 2):
        e = z.bit_length() - 1
        assert (1 << e) < z < (1 << (e + 1))
        D = B << e
        r = D % z
        assert 0 < r < z
        a = (D + z - 1) // z
        y = B - 1 - B % z
        assert 0 <= y < B and y % z == z - 1 and y + z >= B
        margin = (z - r) * y - D
        bad = margin >= 0
        exact = y // z
        computed = a * y // D
        assert computed - exact == int(bad)
        rows.append(dict(z=z, e=e, remainder=r, witness=y, multiplier=a,
                         criterion_margin=margin, fails=bad,
                         exact_quotient=exact, reciprocal_quotient=computed))
    failures = [row["z"] for row in rows if row["fails"]]
    prefix = [7, 21, 23, 25, 29, 31, 39, 47, 49, 53, 55, 61, 63, 71, 81, 89]
    assert failures[:len(prefix)] == prefix
    assert len(failures) == 189
    result = {
        "scope": "Every odd z with 3 <= z < 1000. Divisor 1 is exact and has no admissible strict exponent interval. Each row decides all unsigned 64-bit dividends by the proved maximum-residue criterion.",
        "proof": "notes/recovery-pages-024-033.md#answer-19-complete-finite-census",
        "tested_divisors": len(rows), "failure_count": len(failures),
        "printed_prefix_agrees": True, "failures": failures, "rows": rows,
    }
    (BASE / "results/reciprocal-divisor-census.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"divisors": len(rows), "failures": len(failures),
                      "printed_prefix_agrees": True}))


if __name__ == "__main__":
    main()
