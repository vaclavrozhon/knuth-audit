"""§1.2.2: exact rounding traces, certified constants and fixed-point models.

Integer state transitions are exact. Decimal comparisons below are diagnostic;
the accompanying notes give universal error bounds without numerical testing.
"""
from collections import Counter
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from fractions import Fraction
from pathlib import Path
import json


def ln_interval(x, terms=40):
    """Rational bounds from ln(x)=2*atanh((x-1)/(x+1)), for 1<=x<=2."""
    x = Fraction(x)
    assert 1 <= x <= 2
    z = (x-1)/(x+1)
    z2 = z*z
    power, total = z, Fraction(0)
    for j in range(terms):
        total += power/(2*j+1)
        power *= z2
    lower = 2*total
    upper = lower+2*power/((2*terms+1)*(1-z2))
    return lower, upper


def floor(x):
    return x.numerator//x.denominator


def ceil(x):
    return -floor(-x)


def decimal(x):
    x = Fraction(x)
    return Decimal(x.numerator)/Decimal(x.denominator)


def round_square_trace():
    # Four significant figures for normalized values in [1,10).
    current = 2000
    states, bits, seen = [], [], {}
    while current not in seen:
        seen[current] = len(bits)
        states.append(current)
        square = current*current
        bit = int(square >= 10_000_000)
        divisor = 10_000 if bit else 1000
        current = (square+divisor//2)//divisor
        assert 1000 <= current < 10000
        bits.append(bit)
    first = seen[current]
    period = len(bits)-first
    prefix = sum(Fraction(v, 2**(j+1)) for j, v in enumerate(bits[:first]))
    repeating = sum(v*2**(period-j-1) for j, v in enumerate(bits[first:]))
    limit = prefix+Fraction(repeating, 2**first*(2**period-1))
    expected = [2000, 4000, 1600, 2560, 6554, 4295, 1845, 3404, 1159, 1343, 1804]
    # The cycle may start before index 10, so replay via the periodic sequence.
    def state_at(k):
        return states[k] if k < len(states) else states[first+(k-first) % period]
    assert [state_at(k) for k in range(11)] == expected
    return states, bits, first, period, limit


def log_model(p, original, table):
    unit = 1 << p
    x, y, z, k = original, 0, original >> 1, 1
    counts = Counter()
    shifts = 0
    while x != unit:
        assert 1 <= k <= p and z == x >> k and z > 0
        if x-z < unit:
            z >>= 1
            k += 1
            shifts += 1
            continue
        x -= z
        z = x >> k
        y += table[k]
        counts[k] += 1
        assert unit <= x < 2*unit
    assert sum(counts.values()) <= 3*p
    assert not counts or max(counts.values()) <= 3
    assert shifts <= max(0, p-1)
    return y, counts


def exp_model(p, original, table, start_y):
    # An explicitly stated admissible rounding convention: round logarithm
    # entries upward, so a positive last entry of one unit guarantees progress.
    unit = 1 << p
    x, y, k = unit-1-original, start_y, 1
    steps = 0
    while x:
        while x < table[k]:
            k += 1
            assert k <= p+2
        assert table[k] > 0
        x -= table[k]
        y -= y >> k
        assert y >= unit
        steps += 1
        assert steps <= unit
    return y, steps


def main():
    ln2_lo, ln2_hi = ln_interval(2)
    ln125_lo, ln125_hi = ln_interval(Fraction(5, 4))
    ln10_lo, ln10_hi = 3*ln2_lo+ln125_lo, 3*ln2_hi+ln125_hi
    log_lo, log_hi = ln2_lo/ln10_hi, ln2_hi/ln10_lo
    true_prefix = []
    for k in range(1, 49):
        a, b = floor(log_lo*2**k), floor(log_hi*2**k)
        assert a == b
        true_prefix.append(a % 2)
    states, bits, start, period, rounded_limit = round_square_trace()
    def bit_at(k):
        return bits[k] if k < len(bits) else bits[start+(k-start) % period]
    first_wrong = next(k+1 for k, b in enumerate(true_prefix) if b != bit_at(k))
    assert first_wrong == 19
    assert ''.join(str(bit_at(k)) for k in range(19)) == '0100110100010000011'
    # Rational enclosing intervals prove the Hamming approximation's <1% claim.
    hamming_lo = 1-ln2_hi*(1+1/ln10_lo)
    hamming_hi = 1-ln2_lo*(1+1/ln10_hi)
    assert 0 < hamming_lo < hamming_hi < Fraction(1, 100)
    tables = {}
    for k in range(1, 15):
        lo, hi = ln_interval(Fraction(2**k, 2**k-1))
        tables[k] = lo/ln2_hi, hi/ln2_lo
    log_inputs, exp_inputs, max_steps_at_k = 0, 0, 0
    maximum_log_error = Decimal(0)
    maximum_exp_error = Decimal(0)
    by_precision = []
    with localcontext() as context:
        context.prec = 70
        ln2 = Decimal(2).ln()
        for p in range(1, 13):
            unit = 1 << p
            h = Decimal(1)/unit
            log_table, exp_table = {}, {}
            for k in range(1, p+3):
                lo, hi = tables[k]
                rounded_lo, rounded_hi = floor(unit*lo+Fraction(1, 2)), floor(unit*hi+Fraction(1, 2))
                assert rounded_lo == rounded_hi
                log_table[k] = rounded_lo
                # log_2(2)=1 exactly; outward interval straddles that integer.
                ceiling_lo, ceiling_hi = (unit, unit) if k == 1 else (ceil(unit*lo), ceil(unit*hi))
                assert ceiling_lo == ceiling_hi
                exp_table[k] = ceiling_lo
            assert exp_table[p+2] == 1
            p_max_log_steps, p_max_exp_steps = 0, 0
            log_bound = 3*p*(-(1-h).ln()/ln2+h/2)
            for original in range(unit, 2*unit):
                y, counts = log_model(p, original, log_table)
                error = abs(Decimal(y)/unit-(Decimal(original)/unit).ln()/ln2)
                assert error <= log_bound
                maximum_log_error = max(maximum_log_error, error)
                p_max_log_steps = max(p_max_log_steps, sum(counts.values()))
                max_steps_at_k = max(max_steps_at_k, max(counts.values(), default=0))
                log_inputs += 1
            start_y = int((unit*((1-h)*ln2).exp()).to_integral_value())
            for original in range(unit):
                y, steps = exp_model(p, original, exp_table, start_y)
                exact = ((Decimal(original)/unit)*ln2).exp()
                error = abs((Decimal(y)/unit/exact).ln())
                bound = -(1-h/2).ln()+steps*(h*ln2+(1+2*h).ln())
                assert error <= bound
                maximum_exp_error = max(maximum_exp_error, error)
                p_max_exp_steps = max(p_max_exp_steps, steps)
                exp_inputs += 1
            by_precision.append(dict(bits=p, log_steps=p_max_log_steps, exp_steps=p_max_exp_steps))
        rounded_limit_decimal = str(decimal(rounded_limit))
        ln_error = abs(decimal(rounded_limit)-(Decimal(2).ln()/Decimal(10).ln()))
        four_digit_bound = max(abs(2*Decimal('0.9995').ln()/Decimal(10).ln()),
                              abs(2*Decimal('1.0005').ln()/Decimal(10).ln()))
        assert ln_error < four_digit_bound < Decimal('0.00044')
        powers = [str((Decimal(x)*Decimal(10).ln()).exp()) for x in ['0.30102999','0.30103000']]
        assert powers[0].startswith('1.9999999739') and powers[1].startswith('2.0000000199')
        context.prec = 50
        context.rounding = ROUND_FLOOR
        hamming_lower_display = str(decimal(hamming_lo))
        context.rounding = ROUND_CEILING
        hamming_upper_display = str(decimal(hamming_hi))
    # The missing-base-precondition witness has exact dyadic x-updates.
    # b=1/2 makes the first logarithm table entry log_b(2)=-1.
    residual, entry = Fraction(1, 2), Fraction(-1)
    witness = []
    for _ in range(4):
        assert not residual < entry  # E3 never increments k.
        residual -= entry
        witness.append(str(residual))
    result = dict(status='passed', certified_log10_of_2_binary_bits=len(true_prefix),
                  first_wrong_bit=first_wrong, rounded_trace_first_states=states[:11],
                  rounded_cycle_start=start, rounded_cycle_length=period,
                  rounded_log_limit=rounded_limit_decimal, decimal_power_examples=powers,
                  four_figure_bound=str(four_digit_bound),
                  hamming_relative_error_bounds=[hamming_lower_display,hamming_upper_display],
                  fixed_point_log_inputs=log_inputs, fixed_point_exp_inputs=exp_inputs,
                  maximum_repetitions_of_log_shift_index=max_steps_at_k,
                  runs_by_precision=by_precision,
                  exponent_base_below_one_residuals=witness,
                  exact_parts='Integer transitions, rational log bounds, table rounding decisions, sign witness.',
                  diagnostic_parts='70-digit Decimal checks of observed algorithm errors; universal bounds proved in notes.',
                  exponential_model='Corrected E1, b=2, upward-rounded table, nearest initial y, no overflow.')
    (Path(__file__).resolve().parent/'results/logarithms.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
