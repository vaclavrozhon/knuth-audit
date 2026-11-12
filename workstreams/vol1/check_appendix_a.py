"""Certify the printed Appendix A tables, preserving their original conventions.

Requires python-flint==0.9.0 and mpmath. FLINT/Arb supplies enclosing balls;
mpmath is an independent numerical cross-check, not the error certificate.
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import json

import flint
from flint import arb, arb_series, ctx, fmpq
import mpmath as mp

ROOT = Path(__file__).resolve().parent


def arb_constants():
    pi = arb.pi()
    gamma = arb.const_euler()
    phi = (1 + arb(5).sqrt()) / 2
    return dict(zip(
        ['sqrt2', 'sqrt3', 'sqrt5', 'sqrt10', 'cbrt2', 'cbrt3',
         'fourthroot2', 'ln2', 'ln3', 'ln10', 'invln2', 'invln10',
         'pi', 'degree', 'invpi', 'pi_squared', 'sqrtpi',
         'gamma_one_third', 'gamma_two_thirds', 'e', 'inve', 'e_squared',
         'euler_gamma', 'lnpi', 'golden_ratio', 'exp_gamma', 'exp_pi_over4',
         'sin1', 'cos1', 'negative_zeta_prime2', 'zeta3', 'lnphi',
         'invlnphi', 'negative_lnln2'],
        [arb(2).sqrt(), arb(3).sqrt(), arb(5).sqrt(), arb(10).sqrt(),
         arb(2).root(3), arb(3).root(3), arb(2).root(4),
         arb(2).log(), arb(3).log(), arb(10).log(), 1/arb(2).log(),
         1/arb(10).log(), pi, pi/180, 1/pi, pi*pi, pi.sqrt(),
         arb('1/3').gamma(), arb('2/3').gamma(), arb(1).exp(),
         arb(-1).exp(), arb(2).exp(), gamma, pi.log(), phi, gamma.exp(),
         (pi/4).exp(), arb(1).sin(), arb(1).cos(),
         -arb_series([2, 1], prec=2).zeta()[1], arb(3).zeta(),
         phi.log(), 1/phi.log(), -arb(2).log().log()]))


def mpmath_constants():
    phi = (1 + mp.sqrt(5))/2
    return dict(zip(
        arb_constants(),
        [mp.sqrt(2), mp.sqrt(3), mp.sqrt(5), mp.sqrt(10), mp.root(2, 3),
         mp.root(3, 3), mp.root(2, 4), mp.log(2), mp.log(3), mp.log(10),
         1/mp.log(2), 1/mp.log(10), mp.pi, mp.pi/180, 1/mp.pi, mp.pi**2,
         mp.sqrt(mp.pi), mp.gamma(mp.mpf(1)/3), mp.gamma(mp.mpf(2)/3),
         mp.e, mp.exp(-1), mp.exp(2), mp.euler, mp.log(mp.pi), phi,
         mp.exp(mp.euler), mp.exp(mp.pi/4), mp.sin(1), mp.cos(1),
         -mp.diff(mp.zeta, 2), mp.zeta(3), mp.log(phi), 1/mp.log(phi),
         -mp.log(mp.log(2))]))


def certify_row(row, radix, places, values):
    raw = row['printed'].replace(' ', '')
    sign = raw[-1]
    integer, fractional = raw[:-1].split('.')
    assert len(fractional) == places, row
    denominator = radix**places
    numerator = int(integer, radix)*denominator + int(fractional, radix)
    printed = arb(fmpq(numerator, denominator))
    delta = values[row['quantity']] - printed
    signed = delta if sign == '+' else -delta
    # Strict comparisons mean that the complete enclosing ball has this sign
    # and lies below half of one unit in the last printed place.
    assert signed > 0, (row, delta)
    assert signed < arb(fmpq(1, 2*denominator)), (row, delta)
    return dict(quantity=row['quantity'], radix=radix, places=places,
                printed=row['printed'], exact_minus_printed=str(delta),
                rounding_and_direction_certified=True)


def exact_table3(rows):
    h = Fraction(0)
    b = []
    f0, f1 = 0, 1
    for n, row in enumerate(rows):
        assert row['n'] == n
        if n:
            h += Fraction(1, n)
            b.append(-sum(comb(n+1, k)*b[k] for k in range(n))/(n+1))
        else:
            b.append(Fraction(1))
        assert Fraction(row['harmonic']) == h, row
        assert Fraction(row['bernoulli']) == b[n], row
        assert int(row['fibonacci']) == f0, row
        f0, f1 = f1, f0+f1
    assert len(rows) == 31
    return dict(rows=31, exact_equalities=93,
                bernoulli_original_convention='z/(exp(z)-1), B1=-1/2',
                bernoulli_2021_convention='z/(1-exp(-z)), B1=+1/2',
                convention_change_identity='z/(1-exp(-z)) = z + z/(exp(z)-1)')


def harmonic_specializations():
    pi, r3, r5 = arb.pi(), arb(3).sqrt(), arb(5).sqrt()
    l2, l3, l5 = arb(2).log(), arb(3).log(), arb(5).log()
    phi = (1+r5)/2
    lp = phi.log()
    a = phi**arb('3/2') / arb(5).root(4)
    b = phi**arb('-3/2') / arb(5).root(4)
    formulas = {
        (1, 2): 2-2*l2,
        (1, 3): 3-pi/(2*r3)-3*l3/2,
        (2, 3): arb('3/2')+pi/(2*r3)-3*l3/2,
        (1, 4): 4-pi/2-3*l2,
        (3, 4): arb('4/3')+pi/2-3*l2,
        (1, 5): 5-pi*a/2-5*l5/4-r5*lp/2,
        (2, 5): arb('5/2')-pi*b/2-5*l5/4+r5*lp/2,
        (3, 5): arb('5/3')+pi*b/2-5*l5/4+r5*lp/2,
        (4, 5): arb('5/4')+pi*a/2-5*l5/4-r5*lp/2,
        (1, 6): 6-pi*r3/2-2*l2-3*l3/2,
        (5, 6): arb('6/5')+pi*r3/2-2*l2-3*l3/2,
    }
    results = []
    for (p, q), value in formulas.items():
        direct = (1+arb(fmpq(p, q))).digamma() + arb.const_euler()
        delta = value-direct
        assert delta.contains(0) and abs(delta) < arb('1e-85'), (p, q, delta)
        results.append(dict(p=p, q=q, difference=str(delta)))
    # This finite calculation is supplemental. The general Gauss identity
    # and the exact reductions for q=2,...,6 are proved in the audit notes.
    return results


def main():
    ctx.dps = 100
    mp.mp.dps = 90
    data = json.loads((ROOT/'results/appendix-a-transcription.json').read_text())
    values = arb_constants()
    numerical = mpmath_constants()
    for key, value in values.items():
        approximation = mp.mpf(value.mid().str(90, radius=False))
        assert abs(approximation-numerical[key]) < mp.mpf('1e-80'), key
    for n in range(1, 11):
        values[f'ten_power_minus{n}'] = arb(fmpq(1, 10**n))
    rows = [certify_row(r, 10, 40, values) for r in data['table1']]
    rows += [certify_row(r, 8, 45, values) for r in data['table2']]
    exact = exact_table3(data['table3'])
    harmonic = harmonic_specializations()
    result = dict(passed=True, flint_version=flint.__version__,
                  arb_decimal_precision=ctx.dps,
                  mpmath_version=mp.__version__, mpmath_decimal_precision=90,
                  independent_constant_comparisons=len(numerical),
                  certified_rounded_values=len(rows), rounded_values=rows,
                  table3=exact, harmonic_specializations=harmonic,
                  physical_copy_verified=False)
    (ROOT/'results/appendix-a.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('rounded_values', 'harmonic_specializations')}))


if __name__ == '__main__':
    main()
