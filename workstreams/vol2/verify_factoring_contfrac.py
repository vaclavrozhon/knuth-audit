#!/usr/bin/env python3
"""Exact, independent checks of TAOCP2 4.5.4 E/F and exercises 11--14.

The E recurrence is compared with full, unreduced convergents generated
by the division formula for quadratic surds. F is checked against all
subsets of short unit-relation streams. Durable checkpoints are not rerun.
"""
from pathlib import Path
from fractions import Fraction
from math import gcd, isqrt, prod, log, sqrt
import argparse
import json
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/factoring-contfrac.json'


def cast(v, sign, primes):
    e = [sign]
    for p in primes:
        a = 0
        while v % p == 0:
            v //= p
            a += 1
        e.append(a)
    return v, e


def algorithm_e(n, k, primes, corrected=True, limit=10000):
    d = n*k
    r = isqrt(d)
    assert d != r*r
    if corrected:
        up = 2*r
        v, vp = d-r*r, 1
        a = up//v
        u = 2*r-up % v
        pp, p, s = r, (a*r+1) % n, 1
    else:
        u = up = 2*r
        v, vp, p, pp, a, s = 1, d-r*r, r, 1, 0, 0
    initial = dict(U=u, V=v, A=a, P=p, S=s, T=None)
    rows = []
    for step in range(1, limit+1):
        v, vp = a*(up-u)+vp, v
        a = u//v
        up, u = u, 2*r-u % v
        s = 1-s
        residual, exponents = cast(v, s, primes)
        assert 0 < v <= u <= 2*r
        assert (p*p-(-1)**s*v) % n == 0
        rows.append(dict(U=u, V=v, A=a, P=p, S=s, T=residual,
                         e=exponents, step=step))
        if v == 1:
            return initial, rows, True
        p, pp = (a*p+pp) % n, p
    return initial, rows, False


def full_convergents(n, k, primes, count):
    """Independent recurrence: division (D-u*u)/v and full p/q."""
    d = n*k
    r = isqrt(d)
    u, v, a = 0, 1, r
    p2, p1, q2, q1 = 0, 1, 1, 0
    rows = []
    for i in range(count):
        p, q = a*p1+p2, a*q1+q2
        u = a*v-u
        assert (d-u*u) % v == 0
        v = (d-u*u)//v
        a = (r+u)//v
        s = (i+1) % 2
        assert p*p-d*q*q == (-1)**s*v
        assert gcd(p, q) == 1
        residual, exponents = cast(v, s, primes)
        rows.append(dict(U=r+a*v-u, V=v, A=a, P=p % n, S=s,
                         T=residual, e=exponents, numerator=p, denominator=q,
                         convergent=i))
        p2, p1, q2, q1 = p1, p, q1, q
    return rows


def root_from_exponents(n, primes, e):
    assert all(z % 2 == 0 for z in e)
    return (-1)**(e[0]//2)*prod(pow(p, z//2, n)
                              for p, z in zip(primes, e[1:])) % n


def relations(rows):
    return [(r['P'], r['e']) for r in rows if r['T'] == 1]


def algorithm_f(n, primes, stream):
    pivots = {}
    trace = []
    for index, (x, exponents) in enumerate(stream, 1):
        e = list(exponents)
        used = []
        for k in range(len(e)-1, -1, -1):
            if e[k] % 2 == 0:
                continue
            if k not in pivots:
                pivots[k] = (x, e[:])
                trace.append(dict(input=index, action='store', pivot=k,
                                  x=x, e=e[:], multiplied_pivots=used))
                break
            xi, ei = pivots[k]
            x = xi*x % n
            e = [a+b for a, b in zip(e, ei)]
            used.append(k)
        else:
            y = root_from_exponents(n, primes, e)
            assert (x*x-y*y) % n == 0
            trivial = x == y or x+y == n
            trace.append(dict(input=index, action='F5', x=x, y=y, e=e[:],
                              skip=trivial, gcd=gcd(x-y, n),
                              multiplied_pivots=used))
            if not trivial:
                factor = gcd(x-y, n)
                assert 1 < factor < n
                return factor, trace
    return None, trace


def subsets(n, primes, stream):
    """Enumerate combinations directly, without any row elimination."""
    states = [(1, (0,)*(len(primes)+1), 0)]
    for j, (x, e) in enumerate(stream):
        extra = []
        for a, b, mask in states:
            aa = a*x % n
            bb = tuple(s+t for s, t in zip(b, e))
            mm = mask | (1 << j)
            extra.append((aa, bb, mm))
            if all(z % 2 == 0 for z in bb):
                y = root_from_exponents(n, primes, bb)
                if 0 < aa < n and 0 < y < n and aa != y and aa+y != n:
                    return dict(mask=mm, x=aa, y=y, factor=gcd(aa-y, n))
        states += extra
    return None


def recurrence():
    pairs = row_checks = filter_checks = 0
    for n in range(2, 257):
        for k in range(1, 17):
            if isqrt(n*k)**2 == n*k:
                continue
            primes = [2, 3, 5, 7, 11, 13]
            initial, old, ended = algorithm_e(n, k, primes, False)
            assert ended
            _, new, ended = algorithm_e(n, k, primes, True)
            assert ended
            ref = full_convergents(n, k, primes, max(len(old), len(new)+1))
            for rows, offset in [(old, 0), (new, 1)]:
                for i, row in enumerate(rows):
                    rr = ref[i+offset]
                    for key in ['U', 'V', 'A', 'P', 'S', 'T', 'e']:
                        # The first original P was not reduced modulo N.
                        assert row[key] == rr[key] or (not offset and i == 0 and key == 'P'
                                                      and row[key] % n == rr[key]), (n,k,offset,i,key,row,rr)
                    for p in primes[1:]:
                        if row['V'] % p == 0:
                            assert pow(n*k, (p-1)//2, p) <= 1
                            filter_checks += 1
                    row_checks += 1
            pairs += 1
    return dict(parameter_pairs=pairs, exact_state_comparisons=row_checks,
                factor_base_checks=filter_checks, n_range=[2,256], k_range=[1,16])


def tables():
    n = 197209
    initial, rows, _ = algorithm_e(n, 1, [2,3,5], False, 101)
    printed = {
        'U':[888,876,882,857,751,852,681,863,883,821,877,875,490],
        'V':[1,73,145,37,720,143,215,656,33,136,405,24,477],
        'A':[0,12,6,23,1,5,3,1,26,6,2,36,1],
        'P':[444,444,5329,32418,159316,191734,131941,193139,127871,165232,133218,37250,93755],
        'S':[0,1,0,1,0,1,0,1,0,1,0,1,0],
        'T':[None,73,29,37,1,143,43,41,11,17,1,1,53],
    }
    for key, vals in printed.items():
        assert [r[key] for r in [initial]+rows[:12]] == vals
    assert sum(r['T'] == 1 for r in rows[:100]) == 24
    assert rows[25]['P'] == 197197 and rows[25]['e'] == [0,4,2,0]
    new_initial, new, _ = algorithm_e(n, 1, [2,3,5], True, 100)
    assert [new_initial[key] for key in ['U','V','A','P','S','T']] == [876,73,12,5329,1,None]
    assert sum(r['T'] == 1 for r in new[:100]) == 25
    first = relations(rows)[:2]
    assert first == [(159316,[0,4,2,1]), (133218,[0,0,4,1])]
    factor, trace = algorithm_f(n, [2,3,5], first)
    assert factor == 199
    assert trace[-1]['x'] == 126308 and trace[-1]['y'] == 540
    initial5, rows5, ended = algorithm_e(n, 5, [2], False)
    assert ended
    expected5 = {
        'U':[1984,1981,1983,1983,1981,1984,1984],
        'V':[1,1981,4,991,4,1981,1],
        'A':[0,1,495,2,495,1,1984],
        'P':[992,992,993,98109,2,99099,99101],
        'S':[0,1,0,1,0,1,0],
        'T':[None,1981,1,991,1,1981,1],
    }
    for key, vals in expected5.items():
        assert [r[key] for r in [initial5]+rows5] == vals
    out5 = relations(rows5)
    assert out5 == [(993,[0,2]),(2,[0,2]),(99101,[0,0])]
    assert gcd(993-2,n) == 991 and gcd(99101-1,n) == 991
    assert [r['A'] for r in rows5] == [1,495,2,495,1,1984]
    assert relations(algorithm_e(n,5,[2],True)[1]) == out5
    big_factors = [59649589127497217,5704689200685129054721]
    assert prod(big_factors) == (1 << 128)+1
    # This product check does not itself certify that both factors are prime.
    return dict(table1_rows=13, exercise11_rows=7, first100_outputs=24,
                corrected_first100_outputs=25, exercise11_outputs=out5,
                example_factor=factor, example_trace=trace,
                fermat7_product_factors=big_factors,
                asymptotic_illustrations={
                    'a_for_10^50':sqrt(50*log(10)/log(50*log(10)/log(2))),
                    'a_for_10^200':sqrt(200*log(10)/log(200*log(10)/log(2))),
                    'e_for_10^50':2*sqrt(log(50*log(10))/(50*log(10)))})


def unit_elimination():
    cases = prefixes = 0
    for n in range(3, 301, 2):
        if n % 3 == 0 or n % 5 == 0:
            continue
        for k in range(1, 9):
            if isqrt(n*k)**2 == n*k:
                continue
            primes = [2,3,5]
            _, rows, _ = algorithm_e(n, k, primes, True)
            stream = relations(rows)[:9]
            for end in range(1,len(stream)+1):
                current = stream[:end]
                f, _ = algorithm_f(n, primes, current)
                oracle = subsets(n, primes, current)
                assert (f is not None) == (oracle is not None)
                prefixes += 1
            cases += 1
    return dict(parameter_pairs=cases, independently_enumerated_prefixes=prefixes,
                max_relations=9, n_max=300, k_max=8, factor_base=[2,3,5])


def probability():
    moduli = fibers = roots = 0
    for n in range(3, 1024, 2):
        t=n;d=0;p=2
        while p*p <= t:
            if t % p == 0:
                d += 1
                while t % p == 0:t//=p
            p += 1
        d += t>1
        square_roots = {}
        for x in range(1,n):
            if gcd(x,n) == 1:
                square_roots.setdefault(x*x % n,[]).append(x)
        for a,xs in square_roots.items():
            assert len(xs) == 1 << d
            y=xs[0]
            fails=[x for x in xs if x==y or x+y==n]
            assert len(fails) == 2
            assert Fraction(len(fails),len(xs)) == Fraction(2,1 << d)
            fibers += 1; roots += len(xs)
        moduli += 1
    return dict(odd_moduli=moduli, unit_square_fibers=fibers, unit_roots=roots,
                largest_modulus=1023)


def counterexamples():
    n=197209;primes=[2,3,5]
    _, rows, _=algorithm_e(n,1,primes,True,4)
    row=next(r for r in rows if r['P']==159316)
    q2=(row['P']**2-row['V'])//n
    assert q2==128704 and 358**2 < q2 < 359**2
    ref=full_convergents(n,1,primes,4)[3]
    assert ref['numerator']==750943 and ref['denominator']==1691
    assert ref['numerator'] % n==159316
    # The complete six-output prefix is allowed to terminate at E4.
    n=155;k=29
    _,rows,_=algorithm_e(n,k,primes,True)
    stream=relations(rows)[:6]
    expected=[(80,[0,0,2,1]),(152,[0,0,2,0]),(30,[1,1,1,1]),
              (109,[1,1,3,0]),(25,[0,0,0,1]),(139,[1,1,3,0])]
    assert stream==expected
    ref=full_convergents(n,k,primes,10)
    assert relations(ref[1:])[:6]==stream
    f,trace=algorithm_f(n,primes,stream)
    assert f is None
    witness=subsets(n,primes,stream)
    assert witness==dict(mask=40,x=116,y=101,factor=5)
    assert pow(109,2,n)==pow(139,2,n)==101
    assert all(r['skip'] for r in trace if r['action']=='F5')
    bad_probability=[]
    for n,a,y,want in [(15,9,3,[3,12]),(8,1,1,[1,3,5,7])]:
        xs=[x for x in range(1,n) if x*x % n==a]
        assert xs==want
        fail=sum(x==y or x+y==n for x in xs)
        bad_probability.append(dict(N=n, square=a, roots=xs,
                                    failure_probability=str(Fraction(fail,len(xs)))))
    n=15
    assert relations(algorithm_e(n,9,[2,3],True)[1])[0]==(12,[0,0,2])
    return dict(E3=dict(N=197209,P=159316,V=720,S=0,forced_Q_squared=q2,
                       full_numerator=750943,full_denominator=1691),
                F=dict(N=155,k=29,primes=primes,outputs=stream,trace=trace,
                       independent_subset=witness),
                exercise13=bad_probability)


def expected_valuation(p, d):
    if d % (p*p) == 0:
        return Fraction(2,p+1)+expected_valuation(p,d//(p*p))/p
    if d % p == 0:
        return Fraction(1,p+1)
    if p != 2:
        return Fraction(2*p,p*p-1) if pow(d,(p-1)//2,p)==1 else Fraction(0)
    if d % 4 == 3:return Fraction(1,3)
    if d % 8 == 5:return Fraction(2,3)
    return Fraction(4,3)


def unit_roots(p, d, e):
    if p != 2:return 2 if pow(d,(p-1)//2,p)==1 else 0
    if e == 1:return 1
    if e == 2:return 2 if d % 4 == 1 else 0
    return 4 if d % 8 == 1 else 0


def predicted_roots(p,d,e):
    t=0;u=d
    while u % p==0:t+=1;u//=p
    if e<=t:return p**(e//2)
    if t % 2:return 0
    return p**(t//2)*unit_roots(p,u,e-t)


def valuations():
    pair_checks=tail_cases=means=0
    for p,max_e in [(2,7),(3,4),(5,3),(7,2),(11,2),(13,2)]:
        for e in range(1,max_e+1):
            m=p**e
            denominator=m*m-(m//p)**2
            for d in range(1,33):
                count=0
                for a in range(m):
                    for b in range(m):
                        if a % p==0 and b % p==0:continue
                        count+=(a*a-d*b*b) % m==0
                        pair_checks+=1
                roots=sum((x*x-d) % m==0 for x in range(m))
                assert roots==predicted_roots(p,d,e)
                assert Fraction(count,denominator)==Fraction(roots,p**(e-1)*(p+1))
                tail_cases+=1
        for d in range(1,257):
            t=0;u=d
            while u % p==0:t+=1;u//=p
            end=t+4
            tails=[Fraction(predicted_roots(p,d,e),p**(e-1)*(p+1))
                   for e in range(1,end+1)]
            total=sum(tails)+tails[-1]/(p-1)
            assert total==expected_valuation(p,d)
            means+=1
    return dict(primitive_residue_pairs=pair_checks,exact_tail_cases=tail_cases,
                rational_means=means,d_max_mean=256,
                base_cases_two={str(d):str(expected_valuation(2,d)) for d in [1,3,5,7]},
                scope='Exact local residue model; general proof and interpretation in notes.')


def fermat7_certificates():
    data=json.loads((ROOT/'results/contfrac-certificates.json').read_text())
    proved=set();checks=0
    def independent_pow(a,e,n):
        result=1
        while e:
            if e & 1:result=result*a % n
            a=a*a % n;e//=2
        return result
    for row in data['nodes']:
        n,fs,a=row['n'],row['factors'],row['witness']
        assert n not in proved and 1<=a<n
        assert len({p for p,e in fs})==len(fs)
        assert all(p in proved and isinstance(e,int) and e>0 for p,e in fs)
        assert prod(p**e for p,e in fs)==n-1
        for divisor in [1]+[p for p,e in fs]:
            value=pow(a,(n-1)//divisor,n)
            assert value==independent_pow(a,(n-1)//divisor,n)
            assert (value==1)==(divisor==1)
            checks+=1
        if not fs:assert n==2
        proved.add(n)
    assert data['targets']==[59649589127497217,5704689200685129054721]
    assert set(data['targets'])<=proved
    assert prod(data['targets'])==(1<<128)+1
    return dict(proved_nodes=len(proved),independently_checked_powers=checks,
                targets=data['targets'])


def main():
    funcs=[recurrence,tables,unit_elimination,probability,counterexamples,valuations,fermat7_certificates]
    parser=argparse.ArgumentParser()
    parser.add_argument('--block',choices=['all']+[f.__name__ for f in funcs],default='all')
    args=parser.parse_args()
    state=json.loads(OUT.read_text()) if OUT.exists() else {'checkpoints':{}}
    for fn in funcs:
        if args.block not in ('all',fn.__name__) or fn.__name__ in state['checkpoints']:
            continue
        start=time.monotonic();result=fn()
        checkpoint=dict(status='passed',seconds=time.monotonic()-start,result=result)
        state['checkpoints'][fn.__name__]=checkpoint
        OUT.write_text(json.dumps(state,indent=2)+'\n')
        print(json.dumps({fn.__name__:checkpoint}),flush=True)


if __name__=='__main__':main()
