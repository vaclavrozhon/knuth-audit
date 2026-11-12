"""Exact checks of 3.2.1, with iteration independent of closed formulas."""
from fractions import Fraction
from math import gcd
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    forward = backward = images = cycles = powers_two = 0
    wrong_integer = wrong_fractional = 0
    for m in range(1, 21):
        for a in range(m):
            d = gcd(a, m)
            for c in range(m):
                im = {(a*x+c) % m for x in range(m)}
                assert im == {x for x in range(m) if (x-c) % d == 0}
                images += 1
                for x0 in range(m):
                    xs, ys = [x0], [0]
                    for _ in range(6):
                        xs.append((a*xs[-1]+c) % m)
                        ys.append((a*ys[-1]+1) % m)
                    for k in range(7):
                        s = sum(a**j for j in range(k))
                        assert xs[k] == (a**k*x0+c*s) % m
                        assert xs[k] == (((a-1)*x0+c)*ys[k]+x0) % m
                        if a >= 2:
                            assert (a**k-1) % (a-1) == 0
                            assert s == (a**k-1)//(a-1)
                        forward += 1
                    if d == 1:
                        seen = set()
                        x = x0
                        while x not in seen:
                            seen.add(x)
                            x = (a*x+c) % m
                        assert x == x0
                        cycles += 1
                    if a >= 2 and d == 1:
                        b = a-1
                        ap = pow(a, -1, m)
                        lifted = pow(a, -1, m*b)
                        for k in range(1, 7):
                            correct = (ap**k*xs[k]-c*sum(ap**j for j in range(1,k+1))) % m
                            assert correct == x0
                            assert (lifted**k-1) % b == 0
                            repair = (lifted**k*xs[k]+c*((lifted**k-1)//b)) % m
                            assert repair == x0
                            printed = (ap**k*xs[k]+Fraction((ap**k-1)*c,b)) % m
                            if printed != x0:
                                if printed.denominator == 1:
                                    wrong_integer += 1
                                else:
                                    wrong_fractional += 1
                            backward += 1
    for e in range(1, 8):
        m = 2**e
        for a in range(0, m, 2):
            for c in range(m):
                fixed = (-c*pow(a-1, -1, m)) % m
                for x0 in [0, 1, m-1, fixed]:
                    x = x0
                    for _ in range(e):
                        x = (a*x+c) % m
                    assert x == fixed
                    powers_two += 1
    example = dict(m=8, a=3, c=1, b=2, a_prime=3, x0=0, x1=1, k=1,
                   printed_result=4, correct_result=0, lifted_inverse=11)
    assert (3*1+(3-1)//2) % 8 == 4
    assert (3*1-3) % 8 == 0
    assert (11*1+(11-1)//2) % 8 == 0
    report = dict(status='all assertions passed', modulus_range=[1,20],
                  forward_formula_checks=forward, backward_formula_checks=backward,
                  image_checks=images, pure_cycle_checks=cycles,
                  power_of_two_checks=powers_two,
                  printed_wrong_integral=wrong_integer,
                  printed_wrong_fractional=wrong_fractional,
                  counterexample=example)
    (ROOT/'results/lcg-intro.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
