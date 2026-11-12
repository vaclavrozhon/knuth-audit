#!/usr/bin/env python3
"""Exact Wirsing certificates and an outward enclosure of F_2(1/2)."""
from math import comb, lcm
from pathlib import Path
import json, os, sys, time
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/euclid-gauss.json'
x, c, k, t = sp.symbols('x c k t')


def identities():
    w = (1+x)/((k+x)*(k+1+x))
    assert sp.cancel(w-(k/(k+1+x)-(k-1)/(k+x))) == 0
    g = (1+t)/(1+(c-1)*t)-1/(1+c*t)
    phi = sp.diff(g, t)
    assert sp.cancel(phi-c/(1+c*t)**2-(2-c)/(1+(c-1)*t)**2) == 0
    assert sp.cancel(phi-(2+2*c*t+c*t*t)/((1+c*t)**2*(1+(c-1)*t)**2)) == 0
    term = w*g.subs(t, 1/(k+x))
    telescope = (1+x)*(1/((k+x)*(k+x+c-1))
                       -1/((k+1+x)*(k+x+c)))
    assert sp.cancel(term-telescope) == 0
    h = 1/(x+c)
    right = (1/(1+x)-1/(2+x))*g.subs(t, 1/(1+x))
    assert sp.cancel(h/(1+x)-h.subs(x, x+1)/(2+x)-right) == 0
    ratio = sp.cancel((x+c)**2*phi.subs(t, x))
    P = (c**4-3*c*c+c)*x**3 + (3*c**4-3*c**3-3*c)*x*x
    P += (6*c**3-6*c*c-3*c)*x+3*c*c-2*c-2
    derivative = -2*(x+c)*P/((1+c*x)**3*(1+(c-1)*x)**3)
    assert sp.cancel(sp.diff(ratio, x)-derivative) == 0
    assert sp.cancel(ratio.subs(x, 0)-2*c*c) == 0
    assert sp.cancel(ratio.subs(x, 1)-(3*c+2)/(c*c)) == 0
    return {'symbolic_identities': 8,
            'derivative_polynomial_coefficients': [str(q) for q in sp.Poly(P, x).all_coeffs()]}


def bernstein(poly, left, right):
    """Exact power-to-Bernstein conversion on a rational interval."""
    p = sp.Poly(poly.subs(x, left+(right-left)*t), t)
    d = p.degree()
    a = list(reversed(p.all_coeffs()))
    b = [sum(a[j]*sp.Rational(comb(i, j), comb(d, j)) for j in range(i+1))
         for i in range(d+1)]
    # Independent polynomial reconstruction certifies the coefficient conversion.
    reconstruction = sum(b[i]*comb(d, i)*t**i*(1-t)**(d-i) for i in range(d+1))
    assert sp.Poly(reconstruction-p.as_expr(), t).is_zero
    return b


def positive_certificate(poly):
    pending = [(sp.Rational(0), sp.Rational(1), 0)]
    leaves = []
    while pending:
        a, b, depth = pending.pop()
        coeff = bernstein(poly, a, b)
        if min(coeff)>0:
            leaves.append({'interval': [str(a), str(b)],
                           'bernstein_coefficients': [str(q) for q in coeff]})
        else:
            assert depth < 12
            mid = (a+b)/2
            pending.extend([(a, mid, depth+1), (mid, b, depth+1)])
    # Explicitly verify that the certificate intervals tile [0,1].
    leaves.sort(key=lambda z: sp.Rational(z['interval'][0]))
    assert leaves[0]['interval'][0] == '0' and leaves[-1]['interval'][1] == '1'
    for a, b in zip(leaves, leaves[1:]):
        assert a['interval'][1] == b['interval'][0]
    return leaves


def bounds():
    out = []
    for value in [sp.Rational(65633, 50000), sp.Rational(21, 16)]:
        numerator = ((x+value)**2*(2+2*value*x+value*x*x)).expand()
        denominator = ((1+value*x)**2*(1+(value-1)*x)**2).expand()
        item = {'c': str(value)}
        for name, polynomial in [('upper_U_ratio', 31*numerator-100*denominator),
                                 ('lower_U_ratio', 100*denominator-29*numerator)]:
            p = sp.Poly(polynomial, x)
            scale = lcm(*(int(q.q) for q in p.all_coeffs()))
            integral = (polynomial*scale).expand()
            item[name] = {'positive_scale': scale,
                          'polynomial_coefficients': list(map(int, sp.Poly(integral, x).all_coeffs())),
                          'positive_bernstein_partition': positive_certificate(integral)}
        out.append(item)
    return {'certificates': out,
            'conclusion': 'For both c: 29/100 < U(phi_c)/phi_c < 31/100 on [0,1].'}


def decimal_values():
    from flint import arb, ctx
    ctx.dps = 180
    J = 220
    half_harmonic = 2-2*arb(2).log()
    two_thirds_harmonic = arb(3)/2+arb.pi()/(2*arb(3).sqrt())-3*arb(3).log()/2
    result = 1-two_thirds_harmonic
    for j in range(1, J+1):
        if j == 1:
            difference = arb(5)/3-2*arb(2).log()
        else:
            difference = 1+(arb(2)/3)**j-(2**j-2)*(arb(j).zeta()-1)
        assert difference > 0
        result += (-1)**(j-1)*arb(j+1).zeta()*difference
    tail = 2*arb(2).zeta()*(arb(2)**(-J-1)+arb(2)**(-J)/J)
    enclosure = result+arb(0, tail.upper())
    printed = '5765593276999140841882618721222705592452'
    scale = 10**40
    # The displayed 40-place value is rounded, just like the five-place entries.
    assert int((enclosure*scale+arb(1)/2).floor().unique_fmpz()) == int(printed)
    assert str(int((half_harmonic*100000).floor().unique_fmpz())) == '61370'
    # The five-place book entry is rounded, not truncated.
    assert int((half_harmonic*100000+arb(1)/2).floor().unique_fmpz()) == 61371
    invariant = (arb(3)/2).log()/arb(2).log()
    assert int((invariant*100000+arb(1)/2).floor().unique_fmpz()) == 58496
    endpoints = []
    for end in [enclosure.lower(), enclosure.upper()]:
        m, e = end.man_exp()
        endpoints.append([str(m), int(e)])
    return {'J': J, 'working_decimal_precision': ctx.dps,
            'F2_half': enclosure.str(65), 'dyadic_endpoints': endpoints,
            'analytic_tail_bound': tail.str(15), 'printed_40_digits': printed,
            'printed_value_interpretation': 'Correctly rounded to 40 decimal places.',
            'F1_half': half_harmonic.str(45), 'invariant_half': invariant.str(45)}


def linear_combination():
    """Certify the answer's final claim with three explicit rational terms."""
    parameters = [(sp.Rational(1), -20), (sp.Rational(3, 2), 3410), (sp.Rational(2), -1581)]
    phi = sum(a*(c/(1+c*x)**2+(2-c)/(1+(c-1)*x)**2) for c, a in parameters)
    image = sum(a/(x+c)**2 for c, a in parameters)
    certificates = {}
    for name, expression in [('positive_phi', phi),
                             ('lower_ratio', 100*image-30*phi),
                             ('upper_ratio', 305*phi-1000*image)]:
        numerator, denominator = sp.cancel(expression).as_numer_denom()
        assert sp.Poly(denominator, x).LC() > 0
        certificates[name] = {
            'numerator_coefficients': list(map(int, sp.Poly(numerator, x).all_coeffs())),
            'denominator_coefficients': list(map(int, sp.Poly(denominator, x).all_coeffs())),
            'positive_numerator': positive_certificate(numerator),
            'positive_denominator': positive_certificate(denominator)}
    return {'parameters_c_a': [[str(c), a] for c, a in parameters],
            'certificates': certificates,
            'conclusion': 'phi > 0 and 0.30 < U(phi)/phi < 0.305 throughout [0,1].'}


def main():
    print('PID', os.getpid(), flush=True)
    data = json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {
        'scope': '4.5.3-19/20/21/23 and elementary Gauss-Wirsing formulas', 'checkpoints': {}}
    for name, function in [('identities', identities), ('bounds', bounds),
                           ('decimals', decimal_values), ('combination', linear_combination)]:
        if name in data['checkpoints']:
            print('SKIP', name, flush=True)
            continue
        start = time.monotonic()
        result = function()
        data['checkpoints'][name] = {'seconds': time.monotonic()-start, 'result': result}
        OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
        print('PASS', name, round(data['checkpoints'][name]['seconds'], 3), flush=True)
    print('ALL CHECKPOINTS PASSED', flush=True)


if __name__ == '__main__':
    main()
