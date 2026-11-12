"""Exact supplementary checks for the first part of TAOCP 1.2.6.

Includes negative indices, removable singularities and polynomial identities.
Universal proofs and the limitations of these finite checks are in the notes.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial, prod
from pathlib import Path
import json
import sympy as sp


def choose(r, k):
    if k < 0:
        return Q(0)
    return prod((Q(r-j, j+1) for j in range(k)), start=Q(1))


def ichoose(n, k):
    if k < 0 or 0 <= n < k:
        return 0
    return comb(n, k) if n >= 0 else (-1)**k * comb(k-n-1, k)


def apoly(r, t, k):
    if k < 0:
        return Q(0)
    if k == 0:
        return Q(1)
    return Q(r, factorial(k)) * prod((r-t*k-j for j in range(1, k)), start=Q(1))


def schoose(r, k):
    return sp.Integer(0) if k < 0 else prod((r-j for j in range(k)), start=sp.Integer(1))/factorial(k)


def sapoly(r, t, k):
    if k == 0:
        return sp.Integer(1)
    return r * prod((r-t*k-j for j in range(1, k)), start=sp.Integer(1))/factorial(k)


def carries(a, b, p):
    carry = total = 0
    while a or b or carry:
        a, x = divmod(a, p)
        b, y = divmod(b, p)
        carry = (x+y+carry)//p
        total += carry
    return total


def vp(n, p):
    assert n > 0
    answer = 0
    while n % p == 0:
        n //= p
        answer += 1
    return answer


def main():
    counts = Counter()
    values = [Q(-3), Q(-1), Q(-1,2), Q(0), Q(1,2), Q(2), Q(4)]
    triangle = [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1],
                [1,5,10,10,5,1], [1,6,15,20,15,6,1],
                [1,7,21,35,35,21,7,1], [1,8,28,56,70,56,28,8,1],
                [1,9,36,84,126,126,84,36,9,1]]
    for n, row in enumerate(triangle):
        assert row + [0]*(9-n) == [ichoose(n,k) for k in range(10)]
    assert comb(52,13) == 635013559600 == 2**4*5**2*7**2*17*23*41*43*47
    for r, k in product(values, range(-3,10)):
        assert k*choose(r,k) == r*choose(r-1,k-1)
        assert (r-k)*choose(r,k) == r*choose(r-1,k)
        assert choose(r,k) == choose(r-1,k)+choose(r-1,k-1)
        assert choose(r,k) == Q((-1)**k)*choose(k-r-1,k)
        counts['basic_parameter_pairs'] += 1
    for r,m,k in product(values,range(-2,9),range(-2,9)):
        assert choose(r,m)*choose(m,k) == choose(r,k)*choose(r-k,m-k)
        counts['product_rule'] += 1
    for r,n in product(values,range(-3,16)):
        assert sum((choose(r+k,k) for k in range(n+1)),Q()) == choose(r+n+1,n)
        assert sum(((-1)**k*choose(r,k) for k in range(n+1)),Q()) == Q((-1)**n)*choose(r-1,n)
        counts['prefix_sums'] += 1
    for r,s,n in product(values,values,range(-2,11)):
        assert sum((choose(r,k)*choose(s,n-k) for k in range(n+1)),Q()) == choose(r+s,n)
        counts['chu_vandermonde'] += 1
    for r,s,m,n in product(range(7),values,range(-3,6),range(-3,6)):
        assert sum((choose(r,m+k)*choose(s,n+k) for k in range(-m,r-m+1)),Q()) == choose(r+s,r-m+n)
        counts['shifted_convolution'] += 1
    for r,s,n in product(range(8),values,range(-2,11)):
        assert sum((choose(r,k)*choose(s+k,n)*(-1)**(r-k) for k in range(r+1)),Q()) == choose(s,n-r)
        counts['finite_difference'] += 1
    for r,t,m,s in product(range(8),range(6),range(6),values):
        lhs = sum((choose(r-k,m)*choose(s,k-t)*Q((-1)**(k-t)) for k in range(r+1)),Q())
        assert lhs == choose(r-t-s,r-t-m)
        counts['alternating_convolution'] += 1
    for r,m,n,s in product(range(7),range(7),range(7),values):
        lhs = sum((choose(r-k,m)*choose(s+k,n) for k in range(r+1)),Q())
        rhs = choose(r+s+1,m+n+1)-sum((choose(r+1,j)*choose(s,m+n+1-j) for j in range(m+1)),Q())
        assert lhs == rhs
        counts['corrected_general_equation25'] += 1
    small = [Q(-2),Q(0),Q(1,2),Q(1),Q(3)]
    for r,s,t,n in product(small,small,small,range(-1,9)):
        lhs = sum((apoly(r,t,k)*choose(s-t*(n-k),n-k) for k in range(n+1)),Q())
        assert lhs == choose(r+s-t*n,n)
        if n >= 0:
            conv = sum((apoly(r,t,k)*apoly(s,t,n-k) for k in range(n+1)),Q())
            assert conv == apoly(r+s,t,n)
        counts['rothe_exact_parameters'] += 1
    for n in range(31):
        ans = sum((Q(ichoose(n+k,2*k)*comb(2*k,k)*(-1)**k,k+1) for k in range(n+1)),Q())
        assert ans == (n == 0)
        counts['example2'] += 1
    for n,m in product(range(16),range(-8,26)):
        ans = sum((Q(ichoose(n+k,m+2*k)*comb(2*k,k)*(-1)**k,k+1) for k in range(max(0,n-m+1))),Q())
        assert ans == ichoose(n-1,n-m)
        counts['example3_extended'] += 1
    for n in range(51):
        assert sum(k**4 for k in range(n+1)) == Q(n*(n+1)*(2*n+1)*(3*n*n+3*n-1),30)

    r,s,t = sp.symbols('r s t')
    for n in range(7):
        rothe = sum(sapoly(r,t,k)*schoose(s-t*(n-k),n-k) for k in range(n+1))
        convolution = sum(sapoly(r,t,k)*sapoly(s,t,n-k) for k in range(n+1))
        assert sp.Poly(sp.expand(rothe-schoose(r+s-t*n,n)),r,s,t).is_zero
        assert sp.Poly(sp.expand(convolution-sapoly(r+s,t,n)),r,s,t).is_zero
        shifted = sum(schoose(r+t*k,k)*schoose(s-t*k,n-k) for k in range(n+1))
        target = sum(schoose(r+s-k,n-k)*t**k for k in range(n+1))
        assert sp.Poly(sp.expand(shifted-target),r,s,t).is_zero
        abel = sum(comb(n,k)*(1 if k == 0 else r*(r-k*t)**(k-1))*(s+k*t)**(n-k) for k in range(n+1))
        assert sp.Poly(sp.expand(abel-(r+s)**n),r,s,t).is_zero
        counts['three_variable_polynomial_identities'] += 4
    for m,n in product(range(5),range(5)):
        lhs = sum(schoose(m-r+s,k)*schoose(n+r-s,n-k)*schoose(r+k,m+n) for k in range(n+1))
        assert sp.Poly(sp.expand(lhs-schoose(r,m)*schoose(s,n)),r,s).is_zero
        counts['pfaff_polynomial_identities'] += 1
    for p,n,k in product([2,3,5,7,11],range(-70,71),range(-3,71)):
        assert ichoose(n,k) % p == (ichoose(n//p,k//p)*ichoose(n%p,k%p)) % p
        counts['lucas_integer_cases'] += 1
    for p,a,b in product([2,3,5,7,11,13],range(65),range(65)):
        assert vp(comb(a+b,a),p) == carries(a,b,p)
        counts['kummer_integer_cases'] += 1
    for p,n in product([2,3,5,7,11,13],range(129)):
        reduced = n+1
        while reduced % p == 0:
            reduced //= p
        assert all(comb(n,k)%p for k in range(n+1)) == (reduced < p)
        counts['all_entries_nonzero_mod_p'] += 1
    result = dict(status='passed',arithmetic='Fraction, integers, exact SymPy polynomials',
                  sympy_version=sp.__version__,counts=dict(counts),
                  scope='First-part identities, examples and congruences. No checks of Stirling-number extensions, q-identities or historical claims. Polynomial tests certify only the stated finite degrees; general proofs are in the notes.')
    root=Path(__file__).resolve().parent
    (root/'results/binomial-base.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__ == '__main__':
    main()
