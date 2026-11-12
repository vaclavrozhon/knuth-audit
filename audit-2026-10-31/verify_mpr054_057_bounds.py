"""Exact arithmetic for MPR54–57; no graph enumeration or BDD construction.

Checks the two derived bounds and the printed fractions as numerical objects.
It does NOT verify that the printed fractions are true graph probabilities.
Run: nice -n 15 python3 audit-2026-10-31/verify_mpr054_057_bounds.py
"""
from fractions import Fraction
from math import comb
from pathlib import Path
from datetime import datetime, timezone
import json
import time

ROOT = Path(__file__).parent

def main():
    start = time.perf_counter()
    cases = []
    for p, printed, lower, upper, rounded_lower, rounded_printed in [
        (Fraction(1, 2), Fraction(35165158461687, 2**45),
         Fraction(30, 37), Fraction(15), 811, 999),
        (Fraction(1, 10),
         Fraction(4180246784470862526910349589019919032987399, 4*10**43),
         Fraction(10, 109), Fraction(3, 25), 92, 105),
    ]:
        mu = comb(10, 3)*p**3
        second = (comb(10, 3)*p**3 + 12*comb(10, 4)*p**5
                  + 30*comb(10, 5)*p**6 + 20*comb(10, 6)*p**6)
        conditional = 1 + 3*7*p**2 + (3*comb(7, 2) + comb(7, 3))*p**3
        assert mu == upper
        assert mu**2/second == lower == mu/conditional
        assert second == mu*conditional
        assert lower < printed < upper
        intervals = []
        for label, value, rounded in [
            ("derived lower bound", lower, rounded_lower),
            ("unverified printed probability fraction", printed, rounded_printed),
        ]:
            lo = Fraction(2*rounded-1, 2000)
            hi = Fraction(2*rounded+1, 2000)
            assert lo < value < hi
            intervals.append(dict(
                label=label, value=str(value), decimal_to_3_places=rounded,
                rounding_interval=[str(lo), str(hi)],
                positive_lower_cross_product=value.numerator*lo.denominator-lo.numerator*value.denominator,
                positive_upper_cross_product=hi.numerator*value.denominator-value.numerator*hi.denominator,
            ))
        cases.append(dict(p=str(p), first_moment=str(mu), second_moment=str(second),
                          conditional_mean=str(conditional), lower_bound=str(lower),
                          upper_bound=str(upper), printed_fraction=str(printed),
                          printed_fraction_is_true_probability_verified=False,
                          rounding=intervals))
    out = dict(
        checked_at_utc=datetime.now(timezone.utc).isoformat(),
        purpose="Two exact rational-bound calculations and numerical comparisons only",
        cases=cases, graph_enumerations=0, bdd_constructions=0,
        historical_node_count_verified=False, elapsed_seconds=time.perf_counter()-start,
    )
    path = ROOT/"results/sequential/mpr-054-057-bounds-arithmetic.json"
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

