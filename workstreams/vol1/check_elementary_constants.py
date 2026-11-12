"""Certify decimal prefixes using rational intervals, without float arithmetic."""
from fractions import Fraction
from math import factorial, isqrt
from pathlib import Path
import json
from check_logarithms import ln_interval, floor


def atan_interval(x, terms=64):
    x = Fraction(x)
    total = sum(((-1)**j*x**(2*j+1)/Fraction(2*j+1) for j in range(terms)), Fraction())
    next_sum = total+(-1)**terms*x**(2*terms+1)/Fraction(2*terms+1)
    return min(total, next_sum), max(total, next_sum)


def main():
    a, b = atan_interval(Fraction(1, 5)), atan_interval(Fraction(1, 239))
    pi = 16*a[0]-4*b[1], 16*a[1]-4*b[0]
    e_lower = sum((Fraction(1, factorial(k)) for k in range(101)), Fraction())
    e = e_lower, e_lower+Fraction(1, 100*factorial(100))
    scale = 10**60
    root = isqrt(5*scale**2)
    phi = Fraction(scale+root, 2*scale), Fraction(scale+root+1, 2*scale)
    ln2 = ln_interval(2, terms=100)
    ln125 = ln_interval(Fraction(5, 4), terms=100)
    ln10 = 3*ln2[0]+ln125[0], 3*ln2[1]+ln125[1]
    log10_2 = ln2[0]/ln10[1], ln2[1]/ln10[0]
    intervals = dict(pi=pi, e=e, phi=phi, ln2=ln2, ln10=ln10, log10_2=log10_2)
    out = {}
    for name, (lower, upper) in intervals.items():
        assert lower < upper
        units = floor(lower*10**40)
        assert units == floor(upper*10**40)
        text = str(units)
        out[name] = dict(truncated_40_places=(text[:-40] or '0')+'.'+text[-40:])
    assert out['pi']['truncated_40_places'].startswith('3.14159265358979')
    assert out['phi']['truncated_40_places'].startswith('1.61803398874989')
    assert out['e']['truncated_40_places'].startswith('2.718281828459045')
    result = dict(status='passed', method='Rational series remainders and integer square root.',
                  constants=out, scope='Prefixes on pp. 21-23; Appendix A has not yet been compared.')
    (Path(__file__).resolve().parent/'results/elementary-constants.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
