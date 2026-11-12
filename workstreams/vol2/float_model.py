"""Exact mathematical model for TAOCP 2, 4.2.1, Algorithms A, N and M.

This is the third edition's fraction convention. Exponents are unbounded here;
range exceptions are handled explicitly by callers. Odd-radix ties are rounded
away from zero, an allowed choice where Algorithm N does not prescribe one.
"""
from fractions import Fraction as Q


def power(b, e):
    return Q(b**e) if e >= 0 else Q(1, b**(-e))


def round_integer(x, b):
    sign = -1 if x < 0 else 1
    k, r = divmod(abs(x).numerator, abs(x).denominator)
    twice = 2*r-abs(x).denominator
    if twice > 0 or (twice == 0 and (b % 2 or (k+b//2) % 2 == 0)):
        k += 1
    return sign*k


def value(u, b, p, q=0):
    e, f = u
    return f * power(b, e-q-p)


def normalize(e, f, b, p, zero_e=0, mode='nearest'):
    """Raw fraction f is exact; return ((e, integer significand), trace)."""
    f = Q(f)
    assert abs(f) < b
    tr = dict(left=0, right=0, fraction_overflow=abs(f)>=1,
              rounding_overflow=False, rounded_up=False, tie=False)
    if f == 0:
        return (zero_e, 0), tr
    if abs(f) >= 1:
        f /= b; e += 1; tr['right'] += 1
    while abs(f) < Q(1,b):
        f *= b; e -= 1; tr['left'] += 1
    scaled = f*b**p
    if mode == 'nearest':
        k = round_integer(scaled, b)
    elif mode == 'down':
        k = scaled.numerator//scaled.denominator
    elif mode == 'up':
        k = -((-scaled.numerator)//scaled.denominator)
    else:
        raise ValueError(mode)
    tr['tie'] = (scaled % 1 == Q(1,2))
    tr['rounded_up'] = abs(k)>abs(scaled)
    if abs(k) == b**p:
        k //= b; e += 1
        tr['right'] += 1; tr['rounding_overflow'] = True
    return (e, k), tr


def add(u, v, b, p, q=0, mode='nearest'):
    # As in A, input zero must carry the minimum exponent of the format.
    if u[0] < v[0]:
        u, v = v, u
    diff = u[0]-v[0]
    f = Q(u[1], b**p)
    if diff < p+2 or mode != 'nearest':
        f += Q(v[1], b**p)*power(b, -diff)
    return normalize(u[0], f, b, p, mode=mode)


def multiply(u, v, b, p, q=0):
    return normalize(u[0]+v[0]-q, Q(u[1]*v[1], b**(2*p)), b, p)


def divide(u, v, b, p, q=0):
    if not v[1]:
        raise ZeroDivisionError
    return normalize(u[0]-v[0]+q+1, Q(u[1], b*v[1]), b, p)
