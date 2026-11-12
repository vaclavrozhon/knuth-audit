"""Count only the nontrivial twiddle products in answer 4.6.4-14.

The printed convention treats multiplication by 1, -1, i, -i as free.
Integer exponents identify these roots exactly; no floating-point FFT is run.
"""
import json
from fractions import Fraction

rows = []
for n in range(2, 13, 2):
    size = 2**n
    stages = []
    for exponent in range(2, n + 1, 2):
        block = 2**exponent
        quarter = block // 4
        nontrivial = sum(
            (power * j) % quarter != 0
            for j in range(quarter)
            for power in (1, 2, 3)
        )
        stages.append((size // block) * nontrivial)
    printed = Fraction((3 * n - 2) * size, 8) - 5 * ((size // 2) // 3)
    corrected = Fraction((9 * n - 26) * size, 24) + Fraction(4, 3)
    assert corrected == sum(stages)
    assert printed - corrected == 2
    rows.append({"n": n, "points": size, "stage_products": stages,
                 "counted": sum(stages), "printed": int(printed)})
print(json.dumps({"convention": "Products by +1, -1, +i, -i are free", "rows": rows}, indent=2))
