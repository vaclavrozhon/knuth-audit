"""One direct arithmetic enclosure of the two printed M=9 coefficients."""
from decimal import Decimal, getcontext
from fractions import Fraction
import json
from pathlib import Path

getcontext().prec = 80

def dec(x):
    x = Fraction(x)
    return Decimal(x.numerator) / Decimal(x.denominator)

def harmonic(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction())

m = 9
f = (8*m - 70*harmonic(m+2) + 71
     - 36*harmonic(m+1)/(m+2) + Fraction(270, m+2)
     + Fraction(54, 2*m+3))
n = 100
# Euler--Maclaurin: gamma lies between g-1/(120*n^4) and g.
g = dec(harmonic(n)) - Decimal(n).ln() - dec(Fraction(1, 2*n)) + dec(Fraction(1, 12*n*n))
rounding_pad = Decimal('1e-60')
lo = g - dec(Fraction(1, 120*n**4)) - rounding_pad
hi = g + rounding_pad
beta_lo = dec(Fraction(35, 3))*lo + dec(f/6) - rounding_pad
beta_hi = dec(Fraction(35, 3))*hi + dec(f/6) + rounding_pad
out = {
    'method': 'Exact rational harmonic sums; 80-digit Decimal log; explicit Euler--Maclaurin remainder and 1e-60 rounding pad.',
    'f9_exact': str(f),
    'gamma_interval': [str(lo), str(hi)],
    'linear_coefficient_interval': [str(beta_lo), str(beta_hi)],
    'constant_coefficient_interval': [str(beta_lo-17), str(beta_hi-17)],
    'leading_coefficient_exact': '35/3',
    'rounded_printed_coefficients': ['11.667', '-1.74', '-18.74'],
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k: out[k] for k in ['f9_exact', 'linear_coefficient_interval', 'constant_coefficient_interval']}))
