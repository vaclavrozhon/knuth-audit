#!/usr/bin/env python3
"""Exact jump conventions and certified finite analytic checks for 4.5.4-25.

No truncation of the zeta-zero sum is presented as a proof of its limit.
Run with the recorded local python-flint installation on PYTHONPATH.
"""
from pathlib import Path
from fractions import Fraction
from math import factorial, isqrt
import json
import os
import time
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parent
ctx.prec = 256


def constant():
    log2 = arb(2).log()
    direct = log2.ei() - log2
    partial = arb.const_euler() + log2.log()
    m = 100
    for n in range(2, m + 1):
        partial += log2**n / (n * factorial(n))
    # Positive series; successive tail ratios are <1/(m+2), since log2<1.
    tail = log2**(m + 1) / ((m + 1) * factorial(m + 1)) / (1 - arb(1)/(m + 2))
    enclosure = partial.union(partial + tail)
    assert enclosure.overlaps(direct)
    lower = arb('0.3520165995575474754273567677364365684471')
    upper = lower + arb(10)**-40
    assert direct > lower and direct < upper
    assert enclosure > lower and enclosure < upper
    return {'status': 'passed', 'direct_Ei': direct.str(65),
            'series_enclosure': enclosure.str(65), 'series_terms_2_through': m,
            'tail_bound': tail.str(12), 'printed_digits_verified': 40}


def integer_root(n, k):
    lo, hi = 0, 1 << ((n.bit_length() + k - 1) // k)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**k <= n:
            lo = mid
        else:
            hi = mid
    return lo


def jumps():
    maximum = 20000
    sieve = bytearray(b'\1') * (maximum + 1)
    sieve[:2] = b'\0\0'
    for p in range(2, isqrt(maximum) + 1):
        if sieve[p]:
            sieve[p*p::p] = b'\0' * (((maximum-p*p)//p) + 1)
    pi = [0] * (maximum + 1)
    for n in range(1, maximum + 1):
        pi[n] = pi[n-1] + sieve[n]
    mass = {}
    for p in range(2, maximum + 1):
        if not sieve[p]:
            continue
        power, k = p, 1
        while power <= maximum:
            assert power not in mass
            mass[power] = Fraction(1, k)
            power *= p
            k += 1
    weighted = Fraction(0)
    prime_powers = 0
    examples = []
    for x in range(2, maximum + 1):
        left = weighted
        weighted += mass.get(x, 0)
        by_roots = sum((Fraction(pi[integer_root(x, k)], k)
                        for k in range(1, x.bit_length())), Fraction(0))
        assert weighted == by_roots
        midpoint = (left + weighted) / 2
        assert weighted - midpoint == mass.get(x, 0) / 2
        if x in mass:
            prime_powers += 1
            assert midpoint - mass[x]/2 == left
        if x in [2, 3, 4, 8, 9, 16, 27, 64, 81]:
            examples.append({'x': x, 'J_le': str(weighted), 'J_mid': str(midpoint),
                             'J_lt': str(left), 'correct_plus': str(mass[x]/2)})
    return {'status': 'passed', 'integers': maximum-1, 'prime_powers': prime_powers,
            'examples': examples, 'oracle': 'prime-power event sweep versus pi(integer_root(x,k))/k'}


def branch_integrals():
    rows = []
    a = 160
    tolerance = arb('1e-48')
    for x in [2, 4, 10, 100]:
        logarithm = arb(x).log()
        for sigma in [Fraction(1,4), Fraction(1,2), Fraction(3,4)]:
            beta = arb(sigma.numerator) / sigma.denominator
            for tau in [Fraction(1,2), Fraction(14), Fraction(100)]:
                gamma = arb(tau.numerator) / tau.denominator
                imaginary = acb(0, gamma)
                integral = acb.integral(lambda t, _: ((t + imaginary) * logarithm).exp() / (t + imaginary),
                                        -a, beta, abs_tol=tolerance, rel_tol=tolerance,
                                        eval_limit=100000)
                value = ((acb(beta, gamma)) * logarithm).ei() - acb(0, arb.pi())
                tail = (-a * logarithm).exp() / (gamma * logarithm)
                assert integral.is_finite()
                difference = abs(integral - value)
                assert difference < 2*tail + arb('1e-44')
                assert abs(integral - (value + acb(0, arb.pi()))) > 3
                rows.append({'x': x, 'sigma': str(sigma), 'tau': str(tau),
                             'integral': integral.str(35), 'Ei_minus_i_pi': value.str(35),
                             'difference_bound': difference.str(10), 'tail_bound': tail.str(10)})
    return {'status': 'passed', 'instances': len(rows), 'lower_limit': -a, 'rows': rows,
            'scope': 'Arbitrary points in the critical strip; does not assume these points are zeta zeros.'}


def trivial_zero_tail():
    rows = []
    m = 100
    for x in [2, 4, 10, 100]:
        logarithm = arb(x).log()
        partial = -sum(((-2*j*logarithm).ei() for j in range(1,m+1)), arb(0))
        tail = arb(x)**(-2*(m+1)) / (2*(m+1)*logarithm*(1-arb(x)**-2))
        enclosure = partial.union(partial+tail)
        # Substitution t=exp(y) in the original real integral.
        q = acb.integral(lambda y, _: (-2*y).exp() / ((1-(-2*y).exp())*y),
                         logarithm, 180, abs_tol=arb('1e-55'), rel_tol=arb('1e-55'))
        rest = arb(-360).exp() / (360*(1-arb(-360).exp()))
        qreal = q.real.union(q.real+rest)
        assert qreal.overlaps(enclosure)
        elementary = -((1-arb(x)**-2).log()) / (2*logarithm)
        assert enclosure > 0 and enclosure < elementary
        rows.append({'x': x, 'series': enclosure.str(40), 'quadrature': qreal.str(40),
                     'series_tail_bound': tail.str(12), 'elementary_upper_bound': elementary.str(20)})
    return {'status': 'passed', 'instances': len(rows), 'series_terms': m, 'rows': rows}


def main():
    start = time.monotonic()
    output = {'status':'running', 'pid':os.getpid(), 'precision_bits':ctx.prec, 'blocks':[]}
    print('pid',os.getpid(),flush=True)
    for fn in [constant, jumps, branch_integrals, trivial_zero_tail]:
        begin = time.monotonic()
        result = fn()
        result.update(name=fn.__name__,seconds=time.monotonic()-begin)
        output['blocks'].append(result)
        (ROOT/'results/riemann-explicit.json').write_text(json.dumps(output,indent=2)+'\n')
        print(fn.__name__,result['status'],result['seconds'],flush=True)
    output.update(status='passed',seconds=time.monotonic()-start)
    (ROOT/'results/riemann-explicit.json').write_text(json.dumps(output,indent=2)+'\n')


if __name__=='__main__':
    main()
