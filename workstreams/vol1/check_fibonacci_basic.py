"""Exact finite checks supplementing the proofs for TAOCP 1.2.8.

Matrix multiplication, direct recurrence iteration, and integer polynomial
arithmetic are independent of the binary-doubling production routine.
"""
from fractions import Fraction as R
from math import comb, gcd, prod
from pathlib import Path
import hashlib
import json

from sympy import Matrix, factorint, primerange
from fibonacci_tools import fib, sequence
import check_gamma_constants as interval

ROOT = Path(__file__).resolve().parent
COUNTS = {}


def check(name, assertion):
    assert assertion, name
    COUNTS[name] = COUNTS.get(name, 0) + 1


def matmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def matpow(n):
    a = ((1, 1), (1, 0)) if n >= 0 else ((0, 1), (1, -1))
    n, result = abs(n), ((1, 0), (0, 1))
    while n:
        if n & 1:
            result = matmul(result, a)
        a, n = matmul(a, a), n // 2
    return result


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def iterate(u, last=30, initial=(0, 1)):
    result = list(initial)
    for n in range(last-1):
        result.append(result[-1]+result[-2]+u(n))
    return result


def fibonomial(n, k):
    if not 0 <= k <= n:
        return R(0)
    return prod((R(fib(n-k+j), fib(j)) for j in range(1, k+1)), start=R(1))


def prime_certificate(n, certificates):
    if str(n) in certificates:
        return
    if n == 2:
        certificates['2'] = {'base': True}
        return
    factors = {int(q): int(e) for q, e in factorint(n-1).items()}
    witnesses = {}
    for q in factors:
        prime_certificate(q, certificates)
        for a in range(2, 10000):
            if pow(a, n-1, n) == 1 and gcd(pow(a, (n-1)//q, n)-1, n) == 1:
                witnesses[str(q)] = a
                break
        else:
            raise AssertionError(('no certificate witness', n, q))
    certificates[str(n)] = {'factors': {str(q): e for q, e in factors.items()},
                            'witnesses': witnesses}


def validate_prime(n, certificates, verified):
    if n in verified:
        return
    cert = certificates[str(n)]
    if n == 2:
        assert cert == {'base': True}
    else:
        factors = {int(q): e for q, e in cert['factors'].items()}
        assert all(q >= 2 and isinstance(e, int) and e > 0 for q, e in factors.items())
        assert prod(q**e for q, e in factors.items()) == n-1
        for q in factors:
            validate_prime(q, certificates, verified)
            a = cert['witnesses'][str(q)]
            assert pow(a, n-1, n) == 1
            assert gcd(pow(a, (n-1)//q, n)-1, n) == 1
    verified.add(n)


def main():
    values = list(sequence(1000))
    for n in range(-100, 1001):
        m = matpow(n)
        check('matrix_and_binary_doubling', m == ((fib(n+1), fib(n)), (fib(n), fib(n-1))))
    for n, value in enumerate(values, 1):
        check('iterative_sequence', value == matpow(n)[0][1])
    output = ''.join(f'{v}\n' for v in values)
    (ROOT / 'results/fibonacci-1-to-1000.txt').write_text(output)
    check('F1000_decimal', len(str(values[-1])) == 209 and str(values[-1])[0] == '4')
    log_binet = interval.add(interval.scalar(interval.log_interval(interval.constant('phi')), 1000),
                             interval.scalar(interval.log_point(5), R(-1, 2)))
    log_exact = interval.log_point(values[-1])
    decimal_log = interval.div(log_exact, interval.constant('ln10'))
    check('printed_logarithms', R('480.407105') < log_binet[0] <= log_binet[1] < R('480.407115'))
    check('printed_logarithms', R('208.635') < decimal_log[0] <= decimal_log[1] < R('208.645'))

    for n in range(-25, 26):
        check('Cassini', fib(n+1)*fib(n-1)-fib(n)**2 == (-1 if n % 2 else 1))
        for m in range(-25, 26):
            check('index_addition', fib(n+m) == fib(m)*fib(n+1)+fib(m-1)*fib(n))
            for k in range(-4, 5):
                check('exercise_17', fib(n+k)*fib(m-k)-fib(n)*fib(m) ==
                      (-1 if n % 2 else 1)*fib(m-n-k)*fib(k))
    for m in range(101):
        for n in range(101):
            check('gcd', gcd(fib(m), fib(n)) == fib(gcd(m, n)))
    for k in range(2, 15):
        for a in range(1, fib(k)+1):
            for b in range(1, fib(k)+1):
                x, y, steps = a, b, 0
                while y:
                    x, y, steps = y, x % y, steps+1
                check('Euclid_bound', steps <= k-1)
    check('fixed_points_initial_range', [n for n in range(15) if fib(n) == n] == [0, 1, 5])
    check('squares_initial_range', [n for n in range(15) if fib(n) == n*n] == [0, 1, 12])
    for n in range(81):
        check('convolution', 5*sum(fib(k)*fib(n-k) for k in range(n+1)) ==
              (n-1)*fib(n)+2*n*fib(n-1))
        check('tilings_binomial_sum', sum(comb(n-k, k) for k in range(n//2+1)) == fib(n+1))
        check('squares_identity', fib(n)**2+fib(n+1)**2 == fib(2*n+1))
        check('partial_sum', sum(fib(k) for k in range(n+1)) == fib(n+2)-1)
        check('odd_binomial_sum', 2**n*fib(n) == 2*sum(comb(n, k)*5**((k-1)//2)
                                                     for k in range(1, n+1, 2)))
        for x in [R(-3), R(-1), R(-1, 2), R(0), R(1, 3), R(1), R(2)]:
            check('finite_generating_polynomial', (x*x+x-1)*sum(fib(k)*x**k for k in range(n+1)) ==
                  x**(n+1)*fib(n+1)+x**(n+2)*fib(n)-x)
    for n, t in enumerate(iterate(fib)):
        check('second_order', 5*t == (3*n+3)*fib(n)-n*fib(n+1))
    for r in range(-3, 4):
        for s in range(-3, 4):
            for n, t in enumerate(iterate(lambda _: 0, initial=(r, s))):
                check('homogeneous_initial_values', t == r*fib(n-1)+s*fib(n))
    for c in range(-4, 5):
        for n, t in enumerate(iterate(lambda _: c)):
            check('constant_forcing', t == c*fib(n-1)+(c+1)*fib(n)-c)
    for m in range(1, 13):
        for n, a in enumerate(iterate(lambda j: choose(j, m))):
            check('binomial_forcing', a == fib(m+n+1)+fib(n)-sum(choose(n+j, m-j) for j in range(m+1)))
    u, v = lambda n: n*n-2, lambda n: (-3)**n
    a, b = iterate(u), iterate(v)
    for x in range(-3, 4):
        for y in range(-3, 4):
            for n, c in enumerate(iterate(lambda j: x*u(j)+y*v(j))):
                check('linearity', c == x*a[n]+y*b[n]+(1-x-y)*fib(n))
    for n in range(13):
        for m in range(-8, 9):
            for t in range(-4, 5):
                check('binomial_index_sum', sum(comb(n, k)*fib(t)**k*fib(t-1)**(n-k)*fib(m+k)
                                                for k in range(n+1)) == fib(m+t*n))
    for n in range(1, 21):
        matrix = Matrix(n, n, lambda i, j: 1 if i == j or i == j+1 else (-1 if j == i+1 else 0))
        check('tridiagonal_determinant', matrix.det() == fib(n+1))
    for p in primerange(2, 2000):
        p = int(p)
        if p > 2:
            check('prime_congruence', fib(p) % p == pow(5, (p-1)//2, p))
        if p != 5:
            check('one_adjacent_multiple', (fib(p-1) % p == 0)+(fib(p+1) % p == 0) == 1)
    for a in range(-3, 4):
        for b in range(-3, 4):
            t = 0
            for n in range(21):
                check('geometric_recurrence', t == sum(a**(n-1-j)*b**j for j in range(n)))
                t = a*t+b**n
    for n in range(31):
        for k in range(n+3):
            value = fibonomial(n, k)
            check('fibonomial_integrality', value.denominator == 1)
            if n:
                check('fibonomial_recurrence', value == fib(k-1)*fibonomial(n-1, k)+
                      fib(n-k+1)*fibonomial(n-1, k-1))
    table = [[int(fibonomial(n, k)) for k in range(7)] for n in range(7)]
    check('printed_fibonomial_table', table == [[1,0,0,0,0,0,0],[1,1,0,0,0,0,0],
          [1,1,1,0,0,0,0],[1,2,2,1,0,0,0],[1,3,6,3,1,0,0],
          [1,5,15,15,5,1,0],[1,8,40,60,40,8,1]])
    for m in range(1, 13):
        for n in range(-20, 21):
            check('powers_recurrence', sum(fibonomial(m, k)*(-1)**((m-k+1)//2)*fib(n+k)**(m-1)
                                           for k in range(m+1)) == 0)
    for n in range(1, 51):
        for r in range(n):
            for m in range(17):
                cases = [fib(r), (-1)**(r+1)*fib(n-r), (-1)**n*fib(r),
                         (-1)**(n+r+1)*fib(n-r)]
                check('four_remainder_classes', (fib(m*n+r)-cases[m % 4]) % fib(n) == 0)
    a, b = 0, 1
    for n in range(101):
        check('roots_3_minus2', 5*a == 3**n-(-2)**n)
        a, b = b, b+6*a

    certificates = {}
    mersenne = 2**127-1
    prime_certificate(mersenne, certificates)
    verified = set()
    validate_prime(mersenne, certificates, verified)
    (ROOT / 'results/mersenne127-prime-certificate.json').write_text(json.dumps(certificates, indent=2)+'\n')
    result = {'status': 'passed', 'arithmetic': 'exact integers and rational outward intervals',
              'checks': COUNTS, 'total_cases': sum(COUNTS.values()),
              'F1000': str(values[-1]), 'sequence_sha256': hashlib.sha256(output.encode()).hexdigest(),
              'log_phi1000_over_sqrt5': interval.serialize(log_binet),
              'log_F1000': interval.serialize(log_exact), 'log10_F1000': interval.serialize(decimal_log),
              'fibonomial_table': table, 'prime_certificate_nodes': len(verified),
              'limits': 'Finite checks supplement the general proofs; no historical priority is inferred.'}
    (ROOT / 'results/fibonacci-basic.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
