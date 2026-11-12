"""Exact independent models for TAOCP2 3.3.3, plus labelled numerical checks.

Direct sawtooth sums are independent of the Euclidean recurrence/Algorithm D.
Completed blocks are checkpointed; --resume preserves successful work.
"""
import argparse
from fractions import Fraction as Q
from functools import lru_cache
import itertools
import json
from math import floor, ceil, gcd
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/dedekind.json'


def psi(x):
    x = Q(x)
    return Q(0) if x.denominator == 1 else x - floor(x) - Q(1, 2)


@lru_cache(None)
def sigma(h, k, c):
    """Definition (16), using integer-scaled sawtooth values."""
    assert k > 0
    return Q(3 * sum((2*j-k) * (2*r-k) for j in range(1, k)
                     if (r := (h*j+c) % k)), k*k)


def sigma_real(h, k, c):
    return 12 * sum(psi(Q(j, k)) * psi((h*j+c)/k) for j in range(k))


def reciprocity(h, k, c):
    """Right hand side of (19), including exercise15 for noninteger c."""
    e = int(c == 0) + int(c % h != 0)
    return Q(h, k) + Q(k, h) + Q(1, h*k) + Q(6*floor(c)*ceil(c), h*k) - 6*floor(c/h) - 3*e


def tableau(h, k, c):
    rows = []
    p, prev, sign = 1, 0, 1
    while h:
        a, b, rem = k//h, c//h, c % h
        rows.append(dict(k=k, h=h, c=c, a=a, b=b, rem=rem, p=p, prev=prev, sign=sign))
        k, h, c, p, prev, sign = h, k % h, rem, a*p+prev, p, -sign
    return rows


def algorithm_d(h, k, c):
    """Literal D1–D4; final denominator comes from p, not an input copy."""
    A, B, p, prev, sign = 0, h, 1, 0, 1
    while h:
        a, b, r = k//h, c//h, c % h
        A += (a-6*b)*sign
        B += 6*b*p*(c+r)*sign
        if r != 0 or c == 0:
            A -= 3*sign
        if h == 1:
            B += p*sign
        c, sign = r, -sign
        r, k = k-a*h, h
        h = r
        r, prev = a*p+prev, p
        p = r
    return Q(A) + Q(B, p)


def theorem_d(h, k, c):
    rows = tableau(h, k, c)
    hp = pow(h, -1, k) if k > 1 else 1
    s = next((j for j, row in enumerate(rows, 1) if row['c'] == 0), len(rows)+1)
    return (Q(h+hp, k) + sum(row['sign']*(row['a']-6*row['b']+Q(6*row['c']**2, row['k']*row['h'])) for row in rows)
            + 3*((-1)**s+int(s == 1))-2+(-1)**len(rows))


def floor_sawtooth():
    counts = dict(floor=0, replicate=0, fine=0)
    for k in range(1, 21):
        for h in range(-9, 20):
            g = gcd(h, k)
            for c in (Q(-13, 3), Q(-1), Q(0), Q(2, 7), Q(5), Q(91, 4)):
                expected = Q((h-1)*(k-1)+g-1, 2) + g*floor(c/g)
                assert sum(floor((h*j+c)/k) for j in range(k)) == expected
                counts['floor'] += 1
    for den in range(1, 25):
        for num in range(-den, 2*den+1):
            x = Q(num, den)
            for n in range(1, 13):
                assert sum(psi(x+Q(j, n)) for j in range(n)) == psi(n*x)
                counts['replicate'] += 1
                total = sum(psi(2**j*x+Q(1, 2)) for j in range(n))
                assert total == psi(2**n*x)-psi(x) and abs(total) < 1
                counts['fine'] += 1
    return counts


def basic_sums():
    counts = dict(integer_reciprocity=0, shifts=0, bezout=0, real_reciprocity=0, scale=0)
    for k in range(1, 51):
        for h in range(1, k+1):
            if gcd(h, k) != 1:
                continue
            hp = pow(h, -1, k) if k > 1 else 1
            kp = (1-h*hp)//k
            for c in range(k):
                val = sigma(h, k, c)
                assert val+sigma(k, h, c) == reciprocity(h, k, Q(c))
                assert val == sigma(h, k, -c) == -sigma(k-h, k, c)
                assert abs(val) <= Q((k-1)*(k-2), k)
                counts['integer_reciprocity'] += 1
                if k <= 14:
                    for theta in (Q(1, 7), Q(1, 2), Q(6, 7)):
                        real = sigma_real(h, k, Q(c)+theta)
                        assert real == val + 6*psi(Q(hp*c, k))
                        assert real+sigma_real(k, h, Q(c)+theta) == reciprocity(h, k, Q(c)+theta)
                        counts['real_reciprocity'] += 1
                    for d in (2, 3):
                        assert sigma(d*h, d*k, d*c) == val
                        counts['scale'] += 1
            if k <= 20:
                for c in range(2*k+1):
                    right = sigma(h, k, 0)+12*sum(psi(Q(hp*j, k)) for j in range(1, c))+6*psi(Q(hp*c, k))
                    assert sigma(h, k, c) == right
                    counts['shifts'] += 1
                for j in range(1, k):
                    assert psi(Q(hp*j, k))+psi(Q(kp*j, h)) == Q(j, h*k)-Q(int(j % h == 0), 2)
                    counts['bezout'] += 1
    assert sigma(2, 5, 0) == 0 and sigma(2, 5, 1) == Q(3, 5)
    return dict(counts=counts, printed_answer12_counterexample=dict(h=2,k=5,c=1,sigma_c='3/5',sigma_zero='0',correct_bound='12/5'))


def integer_algorithm():
    count = moment_count = 0
    for k in range(1, 81):
        for h in range(1, k+1):
            if gcd(h, k) != 1:
                continue
            for c in range(k):
                val = sigma(h, k, c)
                assert algorithm_d(h, k, c) == theorem_d(h, k, c) == val, (h,k,c)
                rows = tableau(h, k, c)
                for power in (1, 2, 3, 4):
                    # Divided difference is interpreted as a polynomial, also when c=rem.
                    lhs = sum(row['sign']*Q(row['c']**power, row['k']*row['h']) for row in rows)
                    rhs = sum(row['sign']*row['b']*row['p']*sum(row['c']**i*row['rem']**(power-1-i) for i in range(power)) for row in rows)/Q(k)
                    assert lhs == rhs
                    moment_count += 1
                count += 1
    return dict(algorithm_and_theorem_models=count, telescoping_power_models=moment_count)


def full_period():
    count = 0
    max_delta = Q(0)
    for m in range(2, 81):
        for a in range(m):
            for c in range(1, m):
                orbit, seen, x = [], set(), 0
                while x not in seen:
                    seen.add(x); orbit.append(x); x = (a*x+c) % m
                if len(orbit) != m or x != 0:
                    continue
                desc = sum(orbit[(i+1) % m] < orbit[i] for i in range(m))
                d = gcd(a-1, m)
                assert 2*desc == m+2*(c % d)-d
                assert abs(Q(desc, m)-Q(1, 2)) < Q(d, 2*m)
                # Independent moment formula on the actual orbit, including closing pair.
                sx, sx2 = sum(orbit), sum(t*t for t in orbit)
                cross = sum(t*orbit[(i+1) % m] for i,t in enumerate(orbit))
                corr = Q(m*cross-sx*sx, m*sx2-sx*sx)
                xp = (-pow(a, -1, m)*c) % m
                ds = algorithm_d(a, m, c)
                assert corr == Q(m*ds-3+6*(m-xp-c), m*m-1)
                assert abs(corr-ds/m) < Q(6,m)
                approx = (1-6*Q(c,m)+6*Q(c,m)**2)/a
                assert abs(corr-approx) < Q(a+6,m)
                max_delta = max(max_delta, abs(corr-ds/m)*m)
                count += 1
    # Potency10 modulo10^10: capped valuations i>=2,j>=1 with max(ceil(10/i),ceil(10/j))=10.
    admissible = [(i,j) for i in range(2,11) for j in range(1,11) if max(ceil(Q(10,i)),ceil(Q(10,j))) == 10]
    assert max(2**i*5**j for i,j in admissible) == 2**10*5
    return dict(full_period_orbits=count,max_scaled_correlation_error=str(max_delta),potency10_max_d=2**10*5)


def rademacher():
    count = 0
    def rho(p,q,r):
        return 12*sum(psi(Q(p*j,r))*psi(Q(q*j,r)) for j in range(r))
    for p,q,r in itertools.product(range(1,17),repeat=3):
        if gcd(p,q)*gcd(q,r)*gcd(r,p) != 1:
            continue
        assert rho(p,q,r)+rho(q,r,p)+rho(r,p,q) == Q(p,q*r)+Q(q,r*p)+Q(r,p*q)-3
        boxes = sum(sum((j*u//w)*(j*v//w) for j in range(w)) for u,v,w in ((p,q,r),(q,r,p),(r,p,q)))
        assert boxes == (p-1)*(q-1)*(r-1)
        count += 1
    import sympy as s
    p,q,r = s.symbols('p q r',positive=True)
    def m2(t):return (t-1)*(2*t-1)/(6*t)
    def recip(u,v):return u/v+v/u+1/(u*v)-3
    def weighted(u,v):return u*m2(v)+v*m2(u)-(u+v-2)/4-recip(u,v)/12
    # Expansion of the three products of sawtooths, using the box identity and ordinary reciprocity.
    result = (p-1)*(q-1)*(r-1)
    for u,v,w in ((p,q,r),(q,r,p),(r,p,q)):
        result += u*v*m2(w)-(w-1)/4
    result -= p*weighted(q,r)+q*weighted(r,p)+r*weighted(p,q)
    assert s.factor(12*result-recip(p,q)*0-(p/(q*r)+q/(r*p)+r/(p*q)-3)) == 0
    return dict(pairwise_coprime_triples=count,elementary_three_term_expansion='symbolically zero')


def examples_and_roots():
    import mpmath as mp
    mp.mp.dps = 90
    examples = []
    for a,m,c in ((2**34+1,2**35,1),(10001,10**10,2113248653),(2**18+1,2**35,1)):
        ds = algorithm_d(a,m,c); xp = (-pow(a,-1,m)*c) % m
        corr = (m*ds-3+6*(m-xp-c))/(m*m-1)
        examples.append(dict(a=a,m=m,c=c,sigma=str(ds),correlation=str(corr),decimal=mp.nstr(mp.mpf(corr.numerator)/corr.denominator,35),tableau=tableau(a,m,c)))
    assert Q(examples[0]['sigma']) == 2**33-3+Q(1,2**32)
    assert Q(examples[0]['correlation']) == Q(2**68+5,2**70-1)
    assert Q(examples[1]['sigma']) == Q('-31.6926653544')
    assert Q(examples[2]['correlation']) == Q(2**38-3*2**20+5,2**70-1)
    rows = tableau(3141592621,2**35,1)
    partial = [r['a'] for r in rows]
    assert partial == [10,1,14,1,7,1,1,1,3,3,3,5,2,1,8,7,1,4,1,2,4,2]
    lower = -Q(sum(partial[::2]),2)-sum(partial[1::2]); upper=sum(partial[::2])+Q(sum(partial[1::2]),2)-Q(1,2)
    assert lower == -55 and upper == Q(135,2)
    numeric_count = 0; max_error = mp.mpf(0)
    for k in range(2,17):
        omega = mp.exp(2j*mp.pi/k)
        for h in range(1,k):
            if gcd(h,k) != 1:continue
            hp = pow(h,-1,k)
            for c in sorted({0,1,k//2,k-1}):
                val = sigma(h,k,c); exact=mp.mpf(val.numerator)/val.denominator
                z=12/mp.mpf(k)*sum(omega**(-c*j)/((omega**(-h*j)-1)*(omega**j-1)) for j in range(1,k))
                z+=mp.mpf(6*c)/k-6*mp.mpf(psi(Q(hp*c,k)).numerator)/psi(Q(hp*c,k)).denominator-3*mp.mpf(k-1)/k
                error=abs(z-exact); assert error < mp.mpf('1e-75'); max_error=max(max_error,error); numeric_count += 1
    return dict(examples=examples,example4=dict(partial_quotients=partial,lower=str(lower),upper=str(upper)),root_formula13_numeric_cases=numeric_count,max_absolute_error=mp.nstr(max_error,6),root_scope='90-decimal arithmetic sanity check; proof is separate, not an interval certificate.')


def main():
    p=argparse.ArgumentParser();p.add_argument('--resume',action='store_true');args=p.parse_args()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'scope':'3.3.3 P, Dedekind identities, algorithms and examples; exact arithmetic unless labelled numerical.','blocks':{}}
    blocks=[floor_sawtooth,basic_sums,integer_algorithm,full_period,rademacher,examples_and_roots,continued_fraction_bounds]
    for f in blocks:
        if f.__name__ in data['blocks']:print('PRESERVED',f.__name__,flush=True);continue
        start=time.monotonic();print('START',f.__name__,flush=True)
        result=f();data['blocks'][f.__name__]=dict(result=result,elapsed_seconds=time.monotonic()-start)
        OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');print('PASS',f.__name__,flush=True)
    print('ALL BLOCKS PASSED',flush=True)


def continued_fraction_bounds():
    models = pairs = 0
    for k in range(2,81):
        for h in range(1,k):
            if gcd(h,k) != 1: continue
            partial = [r['a'] for r in tableau(h,k,0)]
            odd,even = sum(partial[::2]),sum(partial[1::2])
            lower,upper = -Q(odd,2)-even,odd+Q(even,2)-Q(1,2)
            # Knuth1977 Theorem1: subtractive remainders identify the
            # maximum among nonzero c. This is independent of direct sigma.
            rems=[k,h]
            while rems[-1]: rems.append((-rems[-2]) % rems[-1])
            maximizer=sum((-1)**(j+1)*rems[j] for j in range(1,len(rems)-1))
            vals=[sigma(h,k,c) for c in range(k)]
            assert sigma(h,k,maximizer) == max(vals[1:])
            assert lower <= min(vals) <= max(vals) <= upper
            # Exercise7: weighted lattice-point partition before expanding
            # into sawtooths; h,k are coprime, so no interior boundary ties.
            floors=sum((h*j//k)*(h*j//k+1) for j in range(1,k))
            floors+=2*sum(i*(k*i//h+1) for i in range(1,h))
            assert floors == k*h*(h-1)
            expanded=h*h*k-h*k-Q(h,2)+Q(h*h,6*k)+Q(k,12)+Q(1,4)-Q(h,6)*(sigma(h,k,0)+sigma(k,h,0))+sigma(1,k,0)/12
            assert expanded == floors
            pairs += 1; models += k
    return dict(coprime_pairs=pairs,bounded_values=models,scope='Direct definition vs subtractive maximizer, theoremK bounds, and weighted-floor proof7; complements earlier algorithm checks.')


if __name__=='__main__':main()
