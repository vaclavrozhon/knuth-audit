"""Rational outward intervals for TAOCP 1.2.5 numerical data.

The positive-real Stirling remainder bound is DLMF 5.11(ii), for both
log Gamma and psi. No binary floats or library Gamma evaluations are used.
"""
from fractions import Fraction as Q
from math import comb, factorial, isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
SCALE = 10**50
SOURCE = json.loads((ROOT / 'results/elementary-constants.json').read_text())


def floor(q):
    q = Q(q)
    return q.numerator // q.denominator


def ceil(q):
    return -floor(-q)


def outward(lo, hi=None):
    if hi is None:
        hi = lo
    assert lo <= hi
    return Q(floor(lo * SCALE), SCALE), Q(ceil(hi * SCALE), SCALE)


def constant(name):
    lo = Q(SOURCE['constants'][name]['truncated_40_places'])
    return lo, lo + Q(1, 10**40)


def add(a, b):
    return outward(a[0] + b[0], a[1] + b[1])


def neg(a):
    return -a[1], -a[0]


def mul(a, b):
    values = [x * y for x in a for y in b]
    return outward(min(values), max(values))


def div(a, b):
    assert b[0] > 0
    return mul(a, (1 / b[1], 1 / b[0]))


def scalar(a, q):
    return mul(a, (Q(q), Q(q)))


def log_point(q, terms=70):
    q = Q(q)
    assert q > 0
    k = q.numerator.bit_length() - q.denominator.bit_length()
    v = q / Q(2)**k
    if v < 1:
        v *= 2
        k -= 1
    assert 1 <= v < 2
    z = outward((v - 1) / (v + 1))
    z2, power, total = mul(z, z), z, (Q(0), Q(0))
    for j in range(terms):
        total = add(total, scalar(power, Q(1, 2 * j + 1)))
        power = mul(power, z2)
    tail = 2 * power[1] / ((2 * terms + 1) * (1 - z[1]**2))
    core = add(scalar(total, 2), (Q(0), tail))
    return add(core, scalar(constant('ln2'), k))


def log_interval(a):
    return log_point(a[0])[0], log_point(a[1])[1]


def exp_point(q, terms=60):
    q = Q(q)
    assert abs(q) <= 1
    if q < 0:
        lo, hi = exp_point(-q, terms)
        return outward(1 / hi, 1 / lo)
    term = total = (Q(1), Q(1))
    for j in range(1, terms + 1):
        term = scalar(term, q / j)
        total = add(total, term)
    next_term_hi = term[1] * q / (terms + 1)
    tail = next_term_hi / (1 - q / (terms + 2))
    return add(total, (Q(0), tail))


def exp_interval(a):
    return exp_point(a[0])[0], exp_point(a[1])[1]


def sqrt_interval(a):
    assert a[0] >= 0
    lo = isqrt(floor(a[0] * SCALE**2))
    hi = isqrt(floor(a[1] * SCALE**2)) + 1
    return Q(lo, SCALE), Q(hi, SCALE)


def bernoulli_numbers(last):
    values = [Q(1)]
    for n in range(1, last + 1):
        values.append(-sum((comb(n + 1, j) * values[j] for j in range(n)), Q()) / (n + 1))
    return values


B = bernoulli_numbers(36)


def psi_point(x, shift=64, omitted=18):
    y = x + shift
    answer = add(log_point(y), outward(-1 / (2 * y)))
    for k in range(1, omitted):
        answer = add(answer, outward(-B[2*k] / (2*k*y**(2*k))))
    error = abs(B[2*omitted] / (2*omitted*y**(2*omitted)))
    answer = add(answer, (-error, error))
    for j in range(shift):
        answer = add(answer, outward(-1 / (x + j)))
    return answer


def log_gamma_point(x, shift=64, omitted=18):
    y = x + shift
    answer = add(scalar(log_point(y), y - Q(1, 2)), outward(-y))
    answer = add(answer, scalar(log_interval(scalar(constant('pi'), 2)), Q(1, 2)))
    for k in range(1, omitted):
        answer = add(answer, outward(B[2*k] / (2*k*(2*k-1)*y**(2*k-1))))
    error = abs(B[2*omitted] / (2*omitted*(2*omitted-1)*y**(2*omitted-1)))
    answer = add(answer, (-error, error))
    for j in range(shift):
        answer = add(answer, neg(log_point(x + j)))
    return answer


def decimal_bound(q, upper=False, places=45):
    units = ceil(q * 10**places) if upper else floor(q * 10**places)
    digits = str(abs(units)).rjust(places + 1, '0')
    return ('-' if units < 0 else '') + digits[:-places] + '.' + digits[-places:]


def serialize(a):
    return {'lower': decimal_bound(a[0]), 'upper': decimal_bound(a[1], True)}


def prefix(a, places):
    units = floor(a[0] * 10**places)
    assert units == floor(a[1] * 10**places), serialize(a)
    assert units >= 0
    digits = str(units).rjust(places + 1, '0')
    return digits[:-places] + '.' + digits[-places:]


def main():
    printed_x = Q('1.4616321449683623412626595')
    left = printed_x + Q(4, 10**26)
    right = printed_x + Q(5, 10**26)
    psi_left, psi_right = psi_point(left), psi_point(right)
    assert psi_left[1] < 0 < psi_right[0]
    assert prefix((left, right), 25) == str(printed_x.numerator // printed_x.denominator) + '.4616321449683623412626595'
    # psi is strictly increasing, so the root is unique and lies in this interval.
    # The mean value theorem bounds the change of log Gamma from its left end.
    max_slope = max(abs(psi_left[0]), abs(psi_right[1]))
    log_value = log_gamma_point(left)
    log_minimum = log_value[0] - max_slope * (right - left), log_value[1]
    minimum = exp_interval(log_minimum)
    assert prefix(minimum, 25) == '0.8856031944108887002788159'

    exact_1000 = factorial(1000)
    log10_1000 = div(log_point(exact_1000), constant('ln10'))
    assert prefix(log10_1000, 5) == '2567.60464'
    root_pi = sqrt_interval(constant('pi'))
    ratio = div((Q(8), Q(8)), constant('e'))
    ratio_power = (Q(1), Q(1))
    for _ in range(8):
        ratio_power = mul(ratio_power, ratio)
    stirling_8 = scalar(mul(root_pi, ratio_power), 4)
    corrected_8 = scalar(stirling_8, Q(97, 96))
    assert floor(stirling_8[0] + Q(1, 2)) == floor(stirling_8[1] + Q(1, 2)) == 39902
    assert floor(corrected_8[0] + Q(1, 2)) == floor(corrected_8[1] + Q(1, 2)) == 40318
    assert prefix(root_pi, 5) == '1.77245'
    # exp(-8) is enclosed by eight reciprocal multiplications of certified e.
    exp_minus8 = scalar(ratio_power, Q(1, 8**8))
    assert floor(exp_minus8[0]*10**8+Q(1, 2)) == floor(exp_minus8[1]*10**8+Q(1, 2)) == 33546
    result = dict(status='passed', arithmetic='exact rational outward intervals on a 10^-50 grid',
                  reused_constants='results/elementary-constants.json, certified 40-place intervals',
                  analytic_remainder='DLMF 5.11(ii), first neglected term; shift 64, omit k=18',
                  root_interval=serialize((left, right)), psi_left=serialize(psi_left), psi_right=serialize(psi_right),
                  minimum_interval=serialize(minimum), minimum_prefix_25=prefix(minimum, 25),
                  log10_1000_factorial=serialize(log10_1000),
                  stirling_8=serialize(stirling_8), corrected_stirling_8=serialize(corrected_8),
                  scope='25 printed decimal places of both coordinates in Fig. 7, log10(1000!), and the numerical Stirling example; no claim about historical tables.')
    (ROOT / 'results/gamma-constants.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
