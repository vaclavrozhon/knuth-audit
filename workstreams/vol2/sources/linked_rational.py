"""TAOCP 4.5.1-10: exact rationals backed by linked digit integers.

Arithmetic never reconstructs a whole integer in a host scalar. The explicit
from_ints/to_pair methods are test/input adapters. Every result owns fresh
nodes; caller-owned inputs remain unchanged, including on allocation failure.
"""
from linked_integer import (Number, Temps, clone, compare_abs, add as int_add,
                            multiply as int_multiply, divmod_trunc)


def magnitude_copy(x):
    y = clone(x)
    y.sign = 1 if y.length else 0
    return y


def gcd_linked(x, y):
    assert x.pool is y.pool
    with Temps() as t:
        a = t.own(magnitude_copy(x))
        b = t.own(magnitude_copy(y))
        while b.sign:
            q, r = divmod_trunc(a, b)
            q.close()
            t.own(r)
            t.keep(a).close()
            a, b = b, r
            p = x.pool
            p.stats['rational_gcd_steps'] = p.stats.get('rational_gcd_steps', 0) + 1
        return t.keep(a)


def exact_quotient(x, y):
    q, r = divmod_trunc(x, y)
    if r.sign:
        q.close()
        r.close()
        raise ValueError('nonexact quotient')
    r.close()
    return q


class Rational:
    def __init__(self, numerator, denominator):
        """Internal ownership transfer; operands must already be canonical."""
        assert numerator.pool is denominator.pool
        assert numerator is not denominator and denominator.sign == 1
        self.numerator, self.denominator = numerator, denominator
        self.pool = numerator.pool

    @classmethod
    def from_numbers(cls, numerator, denominator):
        assert numerator.pool is denominator.pool
        if not denominator.sign:
            raise ZeroDivisionError
        with Temps() as t:
            g = t.own(gcd_linked(numerator, denominator))
            u = t.own(exact_quotient(numerator, g))
            a = t.own(exact_quotient(denominator, g))
            if a.sign < 0:
                a.sign = 1
                u.sign = -u.sign
            return cls(t.keep(u), t.keep(a))

    @classmethod
    def from_ints(cls, pool, numerator, denominator=1):
        # Input/test adapters; all reduction itself uses linked operations.
        with Temps() as t:
            u = t.own(Number.from_int(pool, numerator))
            a = t.own(Number.from_int(pool, denominator))
            return cls.from_numbers(u, a)

    def to_pair(self):
        # Output/test adapter, never called by any arithmetic routine.
        return self.numerator.to_int(), self.denominator.to_int()

    def close(self):
        self.numerator.close()
        self.denominator.close()


def multiply(x, y):
    assert x.pool is y.pool
    u, a, v, b = x.numerator, x.denominator, y.numerator, y.denominator
    with Temps() as t:
        d = t.own(gcd_linked(u, b))
        e = t.own(gcd_linked(a, v))
        U = t.own(exact_quotient(u, d)); B = t.own(exact_quotient(b, d))
        A = t.own(exact_quotient(a, e)); V = t.own(exact_quotient(v, e))
        w = t.own(int_multiply(U, V)); c = t.own(int_multiply(A, B))
        return Rational(t.keep(w), t.keep(c))


def divide(x, y):
    assert x.pool is y.pool
    u, a, v, b = x.numerator, x.denominator, y.numerator, y.denominator
    if not v.sign:
        raise ZeroDivisionError
    with Temps() as t:
        d = t.own(gcd_linked(u, v))
        e = t.own(gcd_linked(a, b))
        U = t.own(exact_quotient(u, d)); V = t.own(exact_quotient(v, d))
        A = t.own(exact_quotient(a, e)); B = t.own(exact_quotient(b, e))
        w = t.own(int_multiply(U, B)); c = t.own(int_multiply(A, V))
        if c.sign < 0:
            c.sign = 1
            w.sign = -w.sign
        return Rational(t.keep(w), t.keep(c))


def add(x, y, subtract=False):
    assert x.pool is y.pool
    u, a, v, b = x.numerator, x.denominator, y.numerator, y.denominator
    with Temps() as t:
        d = t.own(gcd_linked(a, b))
        A = t.own(exact_quotient(a, d)); B = t.own(exact_quotient(b, d))
        U = t.own(int_multiply(u, B)); V = t.own(int_multiply(v, A))
        numerator = t.own(int_add(U, V, subtract))
        h = t.own(gcd_linked(numerator, d))
        w = t.own(exact_quotient(numerator, h))
        Bh = t.own(exact_quotient(b, h))
        c = t.own(int_multiply(A, Bh))
        return Rational(t.keep(w), t.keep(c))


def subtract(x, y):
    return add(x, y, True)


def compare(x, y):
    assert x.pool is y.pool
    with Temps() as t:
        U = t.own(int_multiply(x.numerator, y.denominator))
        V = t.own(int_multiply(y.numerator, x.denominator))
        if U.sign != V.sign:
            return 1 if U.sign > V.sign else -1
        return U.sign * compare_abs(U, V)
