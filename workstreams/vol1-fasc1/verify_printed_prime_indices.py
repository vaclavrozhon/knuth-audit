#!/usr/bin/env python3
"""Small exact sieve for the forty printed entries on file 40 / page 32.

This does not execute Program P or reproduce its historical timing totals.
The finite domain 2..3571 is fixed by the last printed entry.
"""
import json
import os
from pathlib import Path

BASE = Path(__file__).resolve().parent


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Use nice -n 15."
    limit = 3571
    divisor = [0] * (limit + 1)
    for p in range(2, 60):
        if divisor[p] == 0:
            for n in range(p * p, limit + 1, p):
                if divisor[n] == 0:
                    divisor[n] = p
    primes = [n for n in range(2, limit + 1) if divisor[n] == 0]
    printed = {
        1: [2, 233, 547, 877, 1229, 1597, 1993, 2371, 2749, 3187],
        2: [3, 239, 557, 881, 1231, 1601, 1997, 2377, 2753, 3191],
        3: [5, 241, 563, 883, 1237, 1607, 1999, 2381, 2767, 3203],
        50: [229, 541, 863, 1223, 1583, 1987, 2357, 2741, 3181, 3571],
    }
    checks = []
    for row, values in printed.items():
        for column, expected in enumerate(values):
            index = 50 * column + row
            actual = primes[index - 1]
            assert actual == expected, (index, expected, actual)
            checks.append(dict(row=row, column=column, index=index, value=actual))
    assert len(primes) == 500 and primes[-1] == limit
    composite_witnesses = [[n, divisor[n]] for n in range(2, limit + 1) if divisor[n]]
    assert all(2 <= p < n and n % p == 0 for n, p in composite_witnesses)
    result = {
        "scope": "All forty displayed prime values and their exact ranks in file40/page32; no Program P execution or timing reproduction.",
        "proof": "notes/recovery-pages-037-040.md",
        "method": "Eratosthenes sieve through 3571; every composite has a prime factor at most 59 since 60^2 > 3571.",
        "domain": [2, limit], "prime_count": len(primes),
        "displayed_entries_checked": len(checks), "entries": checks,
        "all_primes_through_last_entry": primes,
        "composite_divisor_witnesses": composite_witnesses,
    }
    (BASE / "results/printed-prime-indices.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"limit": limit, "primes": len(primes),
                      "displayed_entries_checked": len(checks),
                      "composite_witnesses": len(composite_witnesses)}))


if __name__ == "__main__":
    main()
