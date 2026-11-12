"""Exact finite checks for TAOCP2 4.5.4-36/37, with resumable blocks.

Asymptotic statements are proved in the notes.  Decimal logarithms here
illustrate those proofs; integer comparisons certify all finite floors.
"""
from pathlib import Path
from math import isqrt, factorial
from fractions import Fraction
from collections import Counter
import hashlib
import json
import time
import mpmath as mp
from verify_factoring_contfrac import algorithm_e, algorithm_f, relations, full_convergents

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/factoring-refinement.json'


def save(data):
    tmp = OUT.with_suffix('.tmp'); tmp.write_text(json.dumps(data, indent=2)+'\n'); tmp.replace(OUT)


def symmetry():
    cases = []; states_checked = 0
    for D in range(2, 10001):
        R = isqrt(D)
        if R*R == D: continue
        P, Q = R, 1; states = []; digits = []; A, B, C, E = 1, 0, 0, 1
        while not states or (P, Q) != (R, 1):
            assert (P, Q) not in states
            states.append((P, Q)); a = (R+P)//Q; digits.append(a)
            A, B, C, E = A*a+B, A, C*a+E, C
            P = a*Q-P
            assert (D-P*P) % Q == 0
            Q = (D-P*P)//Q
            assert Q > 0
        ell = len(digits); states_checked += ell
        assert digits[0] == 2*R and digits[1:] == digits[:0:-1]
        assert A*E-B*C == (-1)**ell
        assert A-E == 2*R*C and B == C*(D-R*R)
        for j, (P, Q) in enumerate(states):
            assert P == states[(1-j) % ell][0]
            assert Q == states[-j % ell][1]
        cases.append(dict(D=D, period=ell, digits=digits))
    examples = []
    for corrected, k, base, expected_cut, expected_factor in [
            (False, 1, [2, 7, 11], 1, 17), (True, 2, [2, 3, 5, 7, 13], 1, 19)]:
        N = 323; init, rows, done = algorithm_e(N, k, base, corrected=corrected)
        u, v = init['U'], init['V']; cut = len(rows)
        for j, row in enumerate(rows):
            if row['U'] == u or row['V'] == v: cut = j+1; break
            u, v = row['U'], row['V']
        oracle = full_convergents(N, k, base, len(rows)+int(corrected))[int(corrected):]
        for row, alt in zip(rows, oracle):
            for key in ['U', 'V', 'A', 'P', 'S', 'T', 'e']: assert row[key] == alt[key]
        complete = algorithm_f(N, base, relations(rows)); early = algorithm_f(N, base, relations(rows[:cut]))
        assert done and cut == expected_cut and complete[0] == expected_factor and early[0] is None
        examples.append(dict(N=N, k=k, base=base, corrected_E1=corrected,
                             initial=init, rows=rows, cut=cut, full_F=complete, early_F=early))
    return dict(cases=cases, states_checked=states_checked, early_stop_examples=examples)


def million_quotients():
    D = 10**18+314159; R = isqrt(D); C, V = R, 1
    U = Up = 2*R; VV, Vp, A = 1, D-R*R, 0
    counts = Counter(); digest = hashlib.sha256(); prefix = None
    for j in range(1, 1000001):
        assert (D-C*C) % V == 0
        V = (D-C*C)//V; a = (R+C)//V; C = a*V-C
        VV, Vp = A*(Up-U)+Vp, VV
        A = U//VV; Up, U = U, 2*R-U % VV
        assert (A, VV, U-R) == (a, V, C)
        counts[a] += 1; digest.update(f'{a},{C},{V}\n'.encode())
        if j == 999999: prefix = [counts[t] for t in range(1, 5)]
    first_million = [counts[t] for t in range(1, 5)]
    expected = [415236, 169719, 93180, 58606]
    assert expected in [prefix, first_million], (prefix, first_million)
    return dict(D=D, nonconstant_quotients=1000000, counts_1_to_4=first_million,
                counts_if_including_integer_part=prefix, printed_counts=expected,
                last_quotient=A, last_state=[C, V], sha256=digest.hexdigest(),
                distinct_quotients=len(counts), total=sum(counts.values()))


def primes_to(limit):
    sieve = bytearray(b'\x01')*(limit+1); sieve[:2] = b'\x00\x00'
    for q in range(2, isqrt(limit)+1):
        if sieve[q]: sieve[q*q::q] = b'\x00'*((limit-q*q)//q+1)
    return [q for q in range(2, limit+1) if sieve[q]]


def floor_ratio(N, p):
    # Equivalent to p^(2r)<=4N<p^(2r+2), with no real arithmetic.
    r = 0; power = 1
    while power*p*p <= 4*N: power *= p*p; r += 1
    assert power <= 4*N < power*p*p
    return r


def refinement():
    mp.mp.dps = 70; primes = primes_to(1300000); floors = []
    for m in [100, 1000, 10000, 100000]:
        p = primes[m-1]; h = mp.log(m); k = int(h/mp.log(h)); N = p**(2*k+1)//4
        r = floor_ratio(N, p); assert r == k
        L = mp.log(N); l = mp.log(L); c = 2*h/mp.sqrt(L*l)
        real = mp.log(2*mp.sqrt(N))/mp.log(p)
        expansion = mp.sqrt(L/l)/c-(1+mp.log(l)/l+2*mp.log(c/2)/l)/c**2
        penalty = (real-r)*h+mp.loggamma(r+1)-mp.loggamma(real+1)
        floors.append(dict(m=m, p=p, k=k, N=N, r=r,
                           unrounded=str(real), c=str(c), printed_expansion=str(expansion),
                           proposed_error_scale=str(mp.sqrt(l/L)),
                           log_rounding_penalty=str(penalty)))
    optima = []
    for digits in [6, 12, 18, 24, 30, 36]:
        N = 10**digits; best = Fraction(2); best_m = None; best_r = None
        tested = 0
        for m, p in enumerate(primes, 1):
            r = floor_ratio(N, p)
            if r <= 2: break
            value = Fraction(factorial(r), m**(r-2)); tested += 1
            if value < best: best, best_m, best_r = value, m, r
        assert r <= 2 and best_m is not None
        # All subsequent r=2,1,0 give normalized costs 2,m,m^2.
        H = mp.log(2*mp.sqrt(N)); proposed_r = int(mp.nint(mp.sqrt(2*H/(mp.log(H)-1))))
        proposed_m = sum(p**(2*proposed_r) <= 4*N for p in primes)
        assert primes[-1]**(2*proposed_r) > 4*N and proposed_m > 0
        actual_r = floor_ratio(N, primes[proposed_m-1])
        proposed = Fraction(factorial(actual_r), proposed_m**(actual_r-2))
        ratio = proposed/best
        optima.append(dict(N=N, tested_m=tested, optimal_m=best_m, optimal_r=best_r,
                           proposed_r=proposed_r, proposed_m=proposed_m,
                           exact_ratio=[ratio.numerator, ratio.denominator]))
    L = 50*mp.log(10); epsilon = 2*mp.sqrt((mp.log(L)-1-mp.log(2))/L)
    return dict(floor_examples=floors, exact_finite_optima=optima, epsilon_10_50=str(epsilon))


def main():
    result = json.loads(OUT.read_text()) if OUT.exists() else dict(status='running', blocks={})
    for name, fn in [('symmetry', symmetry), ('million_quotients', million_quotients), ('refinement', refinement)]:
        if name in result['blocks']: continue
        start = time.perf_counter(); data = fn(); data['seconds'] = time.perf_counter()-start
        result['blocks'][name] = data; save(result)
        print(name, 'passed', data['seconds'], 's', flush=True)
    result['status'] = 'passed'; save(result)


if __name__ == '__main__': main()
