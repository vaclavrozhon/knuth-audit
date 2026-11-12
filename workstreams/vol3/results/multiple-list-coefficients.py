"""Three direct, rational Taylor enclosures; no sampling or enumeration."""
from fractions import Fraction as Q
from math import factorial
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
import json
from pathlib import Path


def decimal(q, rounding):
    with localcontext() as context:
        context.prec = 35
        context.rounding = rounding
        return str(Decimal(q.numerator) / Decimal(q.denominator))


def interval(lo, hi):
    return {"lower": decimal(lo, ROUND_FLOOR), "upper": decimal(hi, ROUND_CEILING),
            "exact_width": str(hi - lo)}


rows = []
for a in [1, 2, 10]:
    # After term 60 the positive magnitudes are decreasing. J_60 is
    # a lower bound, whereas the even exponential partial sum is upper.
    j_lo = sum(((-1) ** (k + 1) * Q(a ** k, k * factorial(k))
                for k in range(1, 61)), Q(0))
    j_hi = j_lo + Q(a ** 61, 61 * factorial(61))
    e_hi = sum(((-1) ** k * Q(a ** k, factorial(k))
                for k in range(61)), Q(0))
    e_lo = e_hi - Q(a ** 61, factorial(61))
    t0 = Q(31) + Q(7 * a, 4) + Q(4, a)
    t_lo, t_hi = t0 - Q(3, a) * j_hi, t0 - Q(3, a) * j_lo
    s0 = Q(4) + Q(7, a)
    s_lo, s_hi = s0 - Q(2, a) * e_hi, s0 - Q(2, a) * e_lo
    rows.append({"alpha": a,
                 "A_per_N": interval(j_lo / a, j_hi / a),
                 "M_time_per_N": interval(t_lo, t_hi),
                 "join_time_per_N": interval(s_lo, s_hi),
                 "combined_time_per_N": interval(t_lo + s_lo, t_hi + s_hi)})

out = {"method": "60-term exact rational alternating Taylor sums with next-term bounds",
       "scope": "alpha=1,2,10 only; coefficients of N as N tends to infinity",
       "rows": rows}
destination = Path(__file__).with_suffix('.json')
destination.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
