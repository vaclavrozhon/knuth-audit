#!/usr/bin/env python3
"""Exact coefficients, root-free enclosures, and analytic CF cross-checks."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json, os, random, sys, time
import mpmath as mp
from verify_euclid_online import cf_value, C, matrix, multiply

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/euclid-analytic.json'


def A(n):
    return [factorial(n)*comb(2*n-k,n)//factorial(k) for k in range(n+1)]


def generalized_binomial(t,k):
    v = F(1)
    for j in range(k):
        v *= F(t-j,j+1)
    assert v.denominator == 1
    return v.numerator


def poly_add(a,b):
    return [(a[j] if j<len(a) else 0)+(b[j] if j<len(b) else 0)
            for j in range(max(len(a),len(b)))]


def exact_coefficients():
    polynomial_checks = exponential_coefficients = 0
    old_den,den = [1],[1]
    old_num,num = [0],[0,1]
    for n in range(1,41):
        an = A(n)
        if n>1:
            old_den,den = den,poly_add([(2*n-1)*x for x in den],[0,0]+old_den)
            old_num,num = num,poly_add([(2*n-1)*x for x in num],[0,0]+old_num)
        # z^n times the denominator/numerator continuants.
        even = [F(an[k])*F(2)**(k-n) if k%2==0 else F(0) for k in range(n+1)]
        odd = [F(an[k])*F(2)**(k-n) if k%2 else F(0) for k in range(n+1)]
        assert poly_add(den,[-x for x in even]) == [0]*max(len(den),len(even))
        assert poly_add(num,[-x for x in odd]) == [0]*max(len(num),len(odd))
        expected = poly_add([(4*n+2)*x for x in an],[0,0]+A(n-1))
        assert A(n+1) == expected
        # Definition of the terminating hypergeometric polynomial, independently.
        hyper = [F(0)]*(n+1)
        rising1,rising2 = 1,1
        for k in range(n+1):
            if k:
                rising1 *= n+k
                rising2 *= -n+k-1
            hyper[n-k] = F(rising1*rising2*(-1)**k,factorial(k))
        assert hyper == an
        polynomial_checks += 4
        for m in range(4*n+10):
            left = sum((-1)**k*comb(m,k)*comb(2*n-k,n)
                       for k in range(min(m,n)+1))
            assert left == generalized_binomial(2*n-m,n)
            coefficient = F(factorial(n)*left,factorial(m))
            if m<=n:
                assert coefficient == an[m]
            elif m<=2*n:
                assert coefficient == 0
            else:
                k = m-2*n-1
                assert coefficient == F((-1)**n*factorial(n+k),factorial(k)*factorial(m))
            exponential_coefficients += 1
    # f_n(z)=sum (-1)^k c[n,k] z^(2k+1); all c[n,k] are positive.
    rows = []
    for n in range(22):
        row = [F(1,2*n+1)]
        for k in range(1,25):
            row.append(sum(row[i]*row[k-1-i] for i in range(k))/F(2*n+2*k+1))
        rows.append(row)
    recurrence_checks = 0
    for n,row in enumerate(rows):
        for k,c in enumerate(row):
            assert c>0 and c <= rows[0][k]/(2*n+1)**(k+1)
            if n:
                assert c<=rows[n-1][k]
            if n+1<len(rows) and k:
                assert (2*n+1)*c == sum(row[i]*rows[n+1][k-1-i] for i in range(k))
                recurrence_checks += 1
    assert rows[0][:4] == [F(1),F(1,3),F(2,15),F(17,315)]
    return dict(polynomial_identities=polynomial_checks,
                exponential_coefficients=exponential_coefficients,
                riccati_coefficients=len(rows)*len(rows[0]),
                reciprocal_coefficient_identities=recurrence_checks)


def analytic_values():
    mp.mp.dps = 160
    points = [mp.mpc('.2','.3'),mp.mpc('-.4','.1'),mp.mpc(1),
              mp.mpc(2,'.5'),mp.mpc(-3,4),mp.mpc(10),mp.mpc(0,10),
              mp.mpc('1e-8',mp.pi/2)]
    cases = bounds = 0
    for z in points:
        for n in [1,2,3,5,10,20]:
            ap = mp.polyval(list(reversed(A(n))),2*z)
            am = mp.polyval(list(reversed(A(n))),-2*z)
            finite = mp.mpc(0)
            for j in range(n-1,-1,-1):
                finite = 1/((2*j+1)/z+finite)
            rational = (ap-am)/(ap+am)
            assert abs(finite-rational) < mp.mpf('1e-120')*(1+abs(rational))
            w = 2*z
            remainder = (-1)**n*w**(2*n+1)*mp.factorial(n)/mp.factorial(2*n+1) * \
                mp.hyp1f1(n+1,2*n+2,w)
            difference = 2*remainder/((ap+am)*(mp.exp(2*z)+1))
            assert abs(mp.tanh(z)-finite-difference)<mp.mpf('1e-110')*(1+abs(difference))
            if abs(w)<=1:
                assert abs(remainder)<=mp.e*mp.factorial(n)/mp.factorial(2*n+1)
                assert abs(ap+am)/2 >= mp.mpf(2)/3*mp.factorial(2*n)/mp.factorial(n)
                bounds += 1
            cases += 1
    fchecks = 0
    for z in [mp.mpc('.3'),mp.mpc('.7','.8'),mp.mpc(2,1)]:
        f = mp.tanh(z)
        for n in range(17):
            def oracle(w):
                return w/(2*n+1)*mp.hyp0f1(n+mp.mpf('1.5'),w*w/4)/ \
                    mp.hyp0f1(n+mp.mpf('.5'),w*w/4)
            assert abs(f-oracle(z))<mp.mpf('1e-100')
            assert abs(mp.diff(oracle,z)-(1-f*f-2*n*f/z))<mp.mpf('1e-95')
            if abs(z)<mp.pi*mp.sqrt(2*n+1)/2:
                assert abs(f)<=mp.tan(abs(z)/mp.sqrt(2*n+1))/mp.sqrt(2*n+1)
            f = 1/f-(2*n+1)/z
            fchecks += 1
    return dict(complex_remainder_cases=cases,printed_small_disk_bounds=bounds,
                bessel_ratio_and_ode_cases=fchecks,decimal_precision=mp.mp.dps)


def collapse_zeros(digits):
    digits = digits[:]
    j = 1
    while j+1<len(digits):
        if digits[j] == 0:
            digits[j-1:j+2] = [digits[j-1]+digits[j+1]]
            j = max(1,j-1)
        else:
            j += 1
    return digits


def certify_prefixes(digits,lower,upper):
    previous_p,p,previous_q,q = 0,1,1,0
    for a in digits:
        previous_p,p = p,a*p+previous_p
        previous_q,q = q,a*q+previous_q
        lo,hi = sorted([F(p,q),F(p+previous_p,q+previous_q)])
        assert lo<lower<upper<hi
    return len(digits)


def negative_exponential_enclosure(x,N=300):
    term = F(1)
    s = term
    for k in range(1,N+1):
        term *= x/k
        s += term
    tail = (term*x/(N+1))/(1-x/(N+2))
    return 1/(s+tail),1/s


def exponential_patterns():
    S = (1,1,1,-1)
    checks = prefixes = 0
    for r in range(1,101):
        assert multiply(S,matrix([2*r])) == multiply(matrix([1,r-1,1]),S)
        checks += 1
    for u in range(6):
        for b in range(1,8):
            for v in range(6):
                assert multiply(S,matrix([2*u+1,b,2*v+1])) == \
                    multiply(matrix([1,u,2*b,v,1]),S)
                checks += 1
    examples = []
    for n in range(1,11):
        digits = [0]
        for m in range(40):
            digits += [1,(2*m+1)*n-1,1]
        digits = collapse_zeros(digits)[:100]
        prefixes += certify_prefixes(digits,*negative_exponential_enclosure(F(1,n)))
        examples.append(dict(exponent=f'-1/{n}',first_20=digits[:20]))
    for n in range(1,16,2):
        digits = [0]
        for m in range(25):
            digits += [1,3*m*n+n//2,(12*m+6)*n,(3*m+2)*n+n//2,1]
        digits = collapse_zeros(digits)[:100]
        prefixes += certify_prefixes(digits,*negative_exponential_enclosure(F(2,n)))
        examples.append(dict(exponent=f'-2/{n}',first_20=digits[:20]))
    return dict(matrix_identities=checks,certified_prefixes=prefixes,examples=examples)


def continuant(digits):
    p,q = 1,0
    for a in digits:
        p,q = a*p+q,p
    return p


def signs_and_reversals():
    rng = random.Random(4531718)
    sign_checks = continuant_checks = reversal_checks = 0
    for n in range(1,11):
        for _ in range(100):
            xs = [rng.randrange(3,13) for _ in range(2*n)]
            signed = [(-1)**j*x for j,x in enumerate(xs)]
            positive = []
            for j,x in enumerate(xs):
                positive.append(x-(1 if j in [0,2*n-1] else 2))
                if j<2*n-1:
                    positive.append(1)
            assert C(*signed) == C(*positive)
            sign_checks += 1
    for m in range(1,6):
        for n in range(1,6):
            for _ in range(20):
                xs = [rng.randrange(-5,6) for _ in range(m)]
                ys = [rng.randrange(-5,6) for _ in range(n)]
                x = rng.randrange(-5,6)
                original = continuant(xs+[-x]+ys)
                first = xs[:-1]+[xs[-1]-1,1,x-1]+[-y for y in ys]
                second = xs[:-1]+[xs[-1]-1,1,x-2,1,ys[0]-1]+ys[1:]
                assert original == (-1)**(n-1)*continuant(first)
                assert original == -continuant(second)
                continuant_checks += 2
    for m in range(1,7):
        for _ in range(100):
            aa = [rng.randrange(1,9) for _ in range(m)]
            xs = [rng.randrange(1,16) for _ in range(12)]
            A0 = continuant(aa)
            B0 = continuant(aa[1:])
            C0 = continuant(aa[:-1])
            h = F(B0-C0,A0)
            forward = [v for x in xs for v in aa+[x]]
            reverse = [v for x in xs for v in aa[::-1]+[x]]
            f,r = C(*forward),C(*reverse)
            if h>=0:
                shifted = forward[:]
                shifted[-1] += h
                assert C(*shifted)-r == h
                assert abs(f-r-h)<=h/continuant(forward)**2
            else:
                shifted = reverse[:]
                shifted[-1] -= h
                assert f-C(*shifted) == h
                assert abs(f-r-h)<=(-h)/continuant(reverse)**2
            reversal_checks += 1
    # Independent alternating Taylor bounds for sin(1)/cos(1).
    N = 80
    sn = sum((F((-1)**k,factorial(2*k+1)) for k in range(N+1)),F(0))
    cn = sum((F((-1)**k,factorial(2*k)) for k in range(N+1)),F(0))
    sl,sh = sorted([sn,sn+F((-1)**(N+1),factorial(2*N+3))])
    cl,ch = sorted([cn,cn+F((-1)**(N+1),factorial(2*N+2))])
    tan_digits = [1]+[v for m in range(50) for v in [2*m+1,1]]
    certified = certify_prefixes(tan_digits,sl/ch,sh/cl)
    return dict(alternating_sign_identities=sign_checks,
                negative_continuant_identities=continuant_checks,
                exact_reversal_and_error_bounds=reversal_checks,
                tan_one_certified_prefixes=certified)


def main():
    print(f'PID {os.getpid()}',flush=True)
    result = json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    jobs = [('coefficients',exact_coefficients),('analytic',analytic_values),
            ('exponentials',exponential_patterns),('signs_reversals',signs_and_reversals)]
    for name,job in jobs:
        if name in result:
            continue
        start = time.monotonic()
        data = job()
        data['seconds'] = time.monotonic()-start
        result[name] = data
        OUT.write_text(json.dumps(result,indent=2)+'\n')
        print(name,'passed',round(data['seconds'],3),flush=True)


if __name__ == '__main__':
    main()
