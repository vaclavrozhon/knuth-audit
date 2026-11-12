"""Check only the printed short numerical data in MPR19.

Eight exact rational terms and a proved analytic tail bound suffice.
This is not a search or census. The general proofs are in the notes.
Run once under nice15; preserve the JSON instead of rerunning.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import time

start = time.perf_counter()
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15
terms = 8
a = [2 ** (2 ** j) for j in range(terms)]
p = [Q(1, v + 1) for v in a]
mean_low = sum(p, Q(0))
variance_low = sum((v * (1 - v) for v in p), Q(0))
tail_seed = Q(1, 2 ** (2 ** terms))
tail_bound = tail_seed / (1 - tail_seed)
mean_high = mean_low + tail_bound
variance_high = variance_low + tail_bound
product = Q(1)
for v in a:
    product *= Q(v - 1, v)
parity_low = Q(1, 2) - product / 4
parity_high = parity_low + product * tail_bound / 4
assert 0 < parity_low < parity_high < Q(1, 2)
parity_variance_low = parity_low * (1 - parity_low)
parity_variance_high = parity_high * (1 - parity_high)
next_variance_low = 2 * variance_low - 2 * mean_high ** 2
next_variance_high = 2 * variance_high - 2 * mean_low ** 2

def decimal(q):
    with localcontext() as ctx:
        ctx.prec = 95
        return str(Decimal(q.numerator) / Decimal(q.denominator))

def interval(name, low, high, printed, digits, below_printed=False):
    shown = Q(printed)
    half_unit = Q(1, 2 * 10 ** digits)
    assert shown - half_unit < low < high < shown + half_unit
    if below_printed:
        assert high < shown
    return {
        "name": name,
        "lower": str(low),
        "upper": str(high),
        "lower_decimal": decimal(low),
        "upper_decimal": decimal(high),
        "printed": printed,
        "digits_after_point": digits,
        "rounding_certified": True,
        "trailing_minus_certified": below_printed,
    }

checks = [
    interval("E S", mean_low, mean_high, "0.59606", 5),
    interval("var S", variance_low, variance_high, "0.44148", 5),
    interval("E R", parity_low, parity_high,
             "0." + "".join(["41245", "40336", "40107", "59778",
                            "33613", "68258", "45528", "30895"]),
             40, True),
    interval("var R", parity_variance_low, parity_variance_high,
             "0.242336", 6),
    interval("var T", next_variance_low, next_variance_high,
             "0.17237", 5),
]
bits = ["".join(str((x >> n) & 1) for x in range(16))
        for n in range(3)]
assert bits == ["0101010101010101", "0011001100110011",
                "0000111100001111"]
parity_bits = "".join(str(x.bit_count() & 1) for x in range(16))
assert parity_bits == "0110100110010110"
result = {
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "method": "Exact Fraction intervals; Decimal is display only.",
    "scope": "Five printed numerical values and four printed16-bit prefixes.",
    "terms": terms,
    "tail_bound": str(tail_bound),
    "tail_proof": "For r=2^(-2^8), sum_(j>=8)2^(-2^j) <= r/(1-r).",
    "intervals": checks,
    "marginal_binary_prefixes": bits,
    "parity_binary_prefix": parity_bits,
    "nice_priority": priority,
    "elapsed_seconds": time.perf_counter() - start,
    "new_searches": 0,
    "old_runs_repeated": 0,
}
root = Path(__file__).resolve().parent
(root / "results/sequential/mpr-019-numeric.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({
    "values": {x["name"]: x["lower_decimal"][:54] for x in checks},
    "all_rounding_checks": True,
    "trailing_minus": True,
    "terms": terms,
    "priority": priority,
    "elapsed_seconds": result["elapsed_seconds"],
}, indent=2))
