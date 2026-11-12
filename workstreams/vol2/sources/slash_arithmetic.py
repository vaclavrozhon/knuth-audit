"""Exact slash rounding model for TAOCP 4.5.1.

Pairs (numerator, denominator) are reduced, with a nonnegative denominator.
The two infinities are (+/-1, 0). This module rounds exact finite inputs;
it does not claim a hardware implementation or a particular running time.
"""
from fractions import Fraction
from math import gcd


def negate(x):
    return -x[0], x[1]


def as_pair(x):
    x = Fraction(x)
    return x.numerator, x.denominator


class SlashFormat:
    def __init__(self, kind="floating", size=27):
        if kind not in ("floating", "fixed") or size < (1 if kind == "floating" else 2):
            raise ValueError((kind, size))
        self.kind, self.size = kind, size
        self.coordinate_bound = 1 << size

    def fits(self, x):
        u, a = x
        if a < 0:
            return False
        if self.kind == "floating":
            return abs(u).bit_length() + a.bit_length() <= self.size
        # Signed numerator: the book's p=8 example has -128 < u < 128.
        return abs(u) < 1 << (self.size - 1) and a < 1 << self.size

    def _positive_bracket(self, x):
        A, B = x.numerator, x.denominator
        if self.fits((A, B)):
            return (A, B), (A, B)
        lo, hi = (0, 1), (1, 0)
        while True:
            u, a = lo
            v, b = hi
            med = (u + v, a + b)
            if not self.fits(med):
                return lo, hi
            cmp = (u + v) * B - (a + b) * A
            if cmp == 0:
                return med, med
            if cmp < 0:
                base, step = lo, hi
                distance = (A * a - B * u) // (B * v - A * b)
            else:
                base, step = hi, lo
                distance = (B * v - A * b) // (A * a - B * u)
            # Largest admissible run of identical Stern--Brocot steps.
            left, right = 1, min(distance, self.coordinate_bound)
            while left < right:
                mid = (left + right + 1) // 2
                trial = (base[0] + mid * step[0], base[1] + mid * step[1])
                if self.fits(trial):
                    left = mid
                else:
                    right = mid - 1
            new = (base[0] + left * step[0], base[1] + left * step[1])
            if new[0] * B == new[1] * A:
                return new, new
            if cmp < 0:
                lo = new
            else:
                hi = new

    def bracket(self, x):
        """Return the two nearest enclosing representables, or (x,x)."""
        x = Fraction(x)
        if x < 0:
            lo, hi = self._positive_bracket(-x)
            return negate(hi), negate(lo)
        return self._positive_bracket(x)

    def round(self, x):
        """Book's mediant rounding, including literal signed tie rule."""
        x = Fraction(x)
        lo, hi = self.bracket(x)
        if lo == hi:
            return lo
        median = Fraction(lo[0] + hi[0], lo[1] + hi[1])
        if x < median:
            return lo
        if x > median:
            return hi
        return min((lo, hi), key=lambda y: (y[1], y[0]))


def mobius_sieve(n):
    """mu(d): zero for a square factor, (-1)^r for r distinct primes."""
    mu = [1] * (n + 1)
    if n:
        mu[0] = 0
    prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if not prime[p]:
            continue
        for k in range(p, n + 1, p):
            prime[k] = False
            mu[k] *= -1
        for k in range(p * p, n + 1, p * p):
            mu[k] = 0
    return mu


def positive_rectangle(M1, M2, N1, N2, mu=None):
    """Count coprime pairs in (M1,M2] x (N1,N2], nonnegative lower bounds."""
    if not (0 <= M1 <= M2 and 0 <= N1 <= N2):
        raise ValueError("positive-rectangle domain")
    K = min(M2, N2)
    mu = mobius_sieve(K) if mu is None else mu
    return sum(mu[d] * (M2 // d - M1 // d) * (N2 // d - N1 // d)
               for d in range(1, K + 1))


def integer_rectangle(M1, M2, N1, N2):
    """Corrected finite formula for arbitrary integer intervals, including zero."""
    if M1 >= M2 or N1 >= N2:
        return 0
    K = max(abs(M1 + 1), abs(M2), abs(N1 + 1), abs(N2))
    origin = int(M1 < 0 <= M2 and N1 < 0 <= N2)
    mu = mobius_sieve(K)
    return sum(mu[d] * ((M2 // d - M1 // d) * (N2 // d - N1 // d) - origin)
               for d in range(1, K + 1))


def format_count(base, places):
    """Finite signed values; numerator/denominator digit lengths sum <= places."""
    K = max((min(base ** a - 1, base ** (places - a) - 1)
             for a in range(1, places)), default=0)
    mu = mobius_sieve(K)
    positive = sum(positive_rectangle(base ** (a - 1) - 1, base ** a - 1,
                                      0, base ** (places - a) - 1, mu)
                   for a in range(1, places))
    return 2 * positive + 1


def _canonical(x):
    u, a = x
    return a >= 0 and gcd(u, a) == 1


def pack_binary(x, q=27):
    """q=27 uses 32 bits; q=58 uses 64 bits. Infinity has tag 0/payload 1."""
    if q < 2 or not _canonical(x) or not SlashFormat(size=q).fits(x):
        raise ValueError(x)
    u, a = x
    size_bits = q.bit_length()
    d = a.bit_length()
    payload = abs(u) if d == 0 else (abs(u) << (d - 1)) | (a - (1 << (d - 1)))
    return (int(u < 0) << (q - 1 + size_bits)) | (d << (q - 1)) | payload


def unpack_binary(word, q=27):
    size_bits = q.bit_length()
    if q < 2 or not 0 <= word < 1 << (q + size_bits):
        raise ValueError(word)
    sign = -1 if word >> (q - 1 + size_bits) else 1
    d = (word >> (q - 1)) & ((1 << size_bits) - 1)
    payload = word & ((1 << (q - 1)) - 1)
    if d > q:
        raise ValueError(word)
    if d == 0:
        x = sign * payload, 0
    else:
        x = sign * (payload >> (d - 1)), (1 << (d - 1)) + (payload & ((1 << (d - 1)) - 1))
    if not _canonical(x) or (x[0] == 0 and sign < 0):
        raise ValueError(word)
    return x


def hex_length(a):
    return (abs(a).bit_length() + 3) // 4


def pack_hex(x, places=7):
    u, a = x
    if not _canonical(x) or hex_length(u) + hex_length(a) > places:
        raise ValueError(x)
    d, size_bits = hex_length(a), places.bit_length()
    return ((int(u < 0) << (4 * places + size_bits)) |
            (d << (4 * places)) | (abs(u) << (4 * d)) | a)


def unpack_hex(word, places=7):
    size_bits = places.bit_length()
    if not 0 <= word < 1 << (4 * places + size_bits + 1):
        raise ValueError(word)
    sign = -1 if word >> (4 * places + size_bits) else 1
    d = (word >> (4 * places)) & ((1 << size_bits) - 1)
    payload = word & ((1 << (4 * places)) - 1)
    if d > places:
        raise ValueError(word)
    x = sign * (payload >> (4 * d)), payload & ((1 << (4 * d)) - 1)
    if (not _canonical(x) or hex_length(x[1]) != d or
            (x[0] == 0 and sign < 0)):
        raise ValueError(word)
    return x
