"""Targeted verification of TAOCP Vol3 Tables2 and root constants on pp.41–42.

Run lengths use exact rational interval arithmetic. Root brackets use
mpmath interval functions, after the scalar monotonicity proof in the notes.
No permutations or combinatorial objects are enumerated.
"""

from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction as F
from math import factorial
import json
import mpmath as mp


def decimal_bound(value, rounding):
    with localcontext() as ctx:
        ctx.prec = 60
        ctx.rounding = rounding
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def signed_rounding_check(lower, upper, printed, direction):
    value = F(printed)
    half_unit = F(1, 2 * 10**15)
    assert value - half_unit < lower <= upper < value + half_unit
    assert lower > value if direction == "+" else upper < value


table = [
    ("1.718281828459045", "+"), ("1.952492442012560", "-"),
    ("1.995791369084285", "-"), ("2.000038850476806", "-"),
    ("2.000057578589716", "+"), ("2.000005072755710", "-"),
    ("1.999999640144022", "+"), ("1.999999888904744", "+"),
    ("1.999999994843434", "-"), ("2.000000001205997", "+"),
    ("2.000000000193672", "+"), ("1.999999999999909", "+"),
    ("1.999999999997022", "-"), ("1.999999999999719", "+"),
    ("2.000000000000019", "+"), ("2.000000000000006", "+"),
    ("2.000000000000000", "+"), ("2.000000000000000", "-"),
]
e_lower = sum((F(1, factorial(j)) for j in range(91)), F(0))
e_upper = e_lower + F(92, 91 * factorial(91))
lower_powers = [e_lower**j for j in range(19)]
upper_powers = [e_upper**j for j in range(19)]
run_lengths = []
for k, (printed, direction) in enumerate(table, 1):
    lower = upper = F(-int(k == 1))
    for j in range(1, k + 1):
        power = F(j**(k - j - 1)) if j < k else F(1, j)
        coefficient = F(k * (-1)**(k-j), factorial(k-j)) * power
        if coefficient >= 0:
            lower += coefficient * lower_powers[j]
            upper += coefficient * upper_powers[j]
        else:
            lower += coefficient * upper_powers[j]
            upper += coefficient * lower_powers[j]
    signed_rounding_check(lower, upper, printed, direction)
    run_lengths.append({
        "k": k, "printed": printed + direction,
        "lower": decimal_bound(lower, ROUND_FLOOR),
        "upper": decimal_bound(upper, ROUND_CEILING),
    })

mp.mp.dps = mp.iv.dps = 90
iv = mp.iv
root_prints = [
    ("8.075566452889526", "-", "1.178303978474668", "+"),
    ("14.354566899762106", "-", "1.312685388387636", "+"),
    ("20.620731538180628", "-", "1.374279075791688", "-"),
    ("26.887952942454546", "-", "1.410497278651865", "-"),
]


def root_equation(y, ctx):
    return y * ctx.cos(y) / ctx.sin(y) - 1 - ctx.log(y / ctx.sin(y))


def check_interval(value, printed, direction):
    delta = value - iv.mpf(printed)
    assert delta > 0 if direction == "+" else delta < 0
    assert abs(delta) < iv.mpf("0.0000000000000005")


roots = []
for k, (r_print, r_sign, theta_print, theta_sign) in enumerate(root_prints, 1):
    seed = (2*k + mp.mpf("0.5")) * mp.pi - mp.mpf("0.3")
    center = mp.findroot(lambda y: root_equation(y, mp), seed)
    lo = mp.nstr(center - mp.mpf("1e-65"), 80)
    hi = mp.nstr(center + mp.mpf("1e-65"), 80)
    assert root_equation(iv.mpf(lo), iv) > 0
    assert root_equation(iv.mpf(hi), iv) < 0
    y = iv.mpf([lo, hi])
    assert y > 2*k*iv.pi and y < (2*k+iv.mpf("0.5"))*iv.pi
    radius = y / iv.sin(y)
    x = 1 + iv.log(radius)
    theta = y - 2*k*iv.pi
    check_interval(radius, r_print, r_sign)
    check_interval(theta, theta_print, theta_sign)
    if k == 1:
        check_interval(x, "3.088843015613044", "-")
        check_interval(y, "7.461489285654255", "-")
    roots.append({
        "k": k, "imaginary_bracket": [lo, hi],
        "radius_interval": str(radius), "argument_interval": str(theta),
        "real_interval": str(x),
        "printed_radius": r_print + r_sign,
        "printed_argument": theta_print + theta_sign,
    })

print(json.dumps({
    "scope": "18 run lengths and four root constants; no enumeration",
    "e_enclosure": "sum(j=0..90)1/j! < e < that sum +92/(91*91!)",
    "run_lengths": run_lengths,
    "roots": roots,
    "root_method": "A unique scalar root per band is proved analytically;90-digit interval evaluations certify the endpoint signs and all printed rounded constants with direction signs.",
    "status": "passed",
}, ensure_ascii=False, indent=2))
