#!/usr/bin/env python3
"""TAOCP2 4.3.2-14: exact cyclic coefficients and certified weight intervals.

This is not a benchmark or a verification of a hardware floating FFT.
The independent output oracle is Python's full integer product and remainder.
"""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
from itertools import product
from sympy import integer_nthroot
import argparse, hashlib, json, random, time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/modular-convolution.json'


def layout(q, n):
    assert q >= 1 and n >= 1
    e = [k*q//n for k in range(n+1)]
    return e, [k*q % n for k in range(n)]


def split(x, e):
    return [(x >> a) % (1 << (b-a)) for a, b in zip(e, e[1:])]


def coefficients(u, v, q, n):
    e, r = layout(q, n)
    a, b = split(u, e), split(v, e)
    t = [0]*n
    for i in range(n):
        for j in range(n):
            k = (i+j) % n
            delta = (r[i]+r[j]-r[k])//n
            assert delta in (0, 1)
            assert r[i]+r[j]-r[k] == delta*n
            t[k] += (a[i]*b[j]) << (1-delta)
    return t


def reconstruct(t, q, n):
    e, _ = layout(q, n)
    M = (1 << q)-1
    S = sum(x << e[k] for k, x in enumerate(t))
    R = S % M
    # Division in Z/MZ. Works for M=1 as well.
    w = (R + M*(R % 2))//2
    assert 0 <= w < M
    # Equivalent end-around treatment of the bit at position -1.
    cyclic = (S//2 + (S % 2)*(1 << (q-1))) % M
    assert cyclic == w == (S*(1 << (q-1))) % M
    return w, S


def witness():
    q, n, u, v = 3, 2, 6, 6
    t = coefficients(u, v, q, n)
    w, S = reconstruct(t, q, n)
    assert t == [9, 0] and S == 9 and w == u*v % 7 == 1
    printed = Fraction(S, 2)
    assert printed % 7 == Fraction(9, 2) != w
    return dict(q=q,n=n,u=u,v=v,chunks=[0,3],weights=['1','1/sqrt(2)'],
                exact_convolution=['9/2','0'],exact_rounded_t=t,
                printed_2020_sum=str(printed),ordinary_real_remainder=str(printed % 7),
                correct_integer_remainder=w,
                assessment='candidate wording gap; modular inverse of2 repairs the formula')


def exhaustive():
    cases = odd = half_integral = 0
    per_q = []
    digest = hashlib.sha256()
    for q in range(1, 8):
        count = 0
        M = (1 << q)-1
        for n in range(1, q+3):
            e, r = layout(q,n)
            vectors = [split(x,e) for x in range(1 << q)]
            terms = [(i,j,(i+j)%n,1-(r[i]+r[j])//n)
                     for i in range(n) for j in range(n)]
            for u, v in product(range(1 << q), repeat=2):
                a,b = vectors[u],vectors[v]
                t = [0]*n
                for i,j,k,s in terms:
                    t[k] += (a[i]*b[j]) << s
                w,S = reconstruct(t,q,n)
                assert S % M == (2*u*v) % M
                assert w == u*v % M
                odd += S % 2
                half_integral += any(x % 2 for x in t)
                digest.update(f'{q},{n},{u},{v},{w},{S}\n'.encode())
                count += 1
        cases += count
        per_q.append([q,count])
    return dict(cases=cases,per_q=per_q,odd_S_cases=odd,
                original_z_over_a_nonintegral_cases=half_integral,sha256=digest.hexdigest(),
                domain='q1..7,n1..q+2,all u,v in[0,2^q),including leading zeroes and empty chunks')


def large_exact():
    rng = random.Random(43214)
    cases = odd = 0
    sizes = [8,9,15,16,31,32,63,64,127,128,511,512,1024,4096,16384]
    for q in sizes:
        M = (1 << q)-1
        for n in [1,2,3,7,8,15,32,65]:
            for trial in range(6):
                u,v = (M,M) if trial==0 else (rng.getrandbits(q),rng.getrandbits(q))
                t = coefficients(u,v,q,n)
                w,S = reconstruct(t,q,n)
                assert w == (u*v) % M
                assert S % M == (2*u*v) % M
                odd += S % 2
                cases += 1
    return dict(cases=cases,odd_S_cases=odd,q_values=sizes,
                n_values=[1,2,3,7,8,15,32,65],seed=43214)


@lru_cache(maxsize=None)
def weight_bounds(qmod, n, p):
    scale = 1 << p
    lo,hi = [],[]
    for k in range(n):
        r = k*qmod % n
        A,exact = integer_nthroot(1 << (p*n-r), n)
        # Integer-root certificates, independent of the root routine's flag.
        target = 1 << (p*n-r)
        assert A**n <= target < (A+1)**n
        assert exact == (A**n == target)
        lo.append(int(A));hi.append(int(A if exact else A+1))
    return scale,lo,hi


def interval_coefficients(u,v,q,n,initial=4):
    e,_ = layout(q,n)
    a,b = split(u,e),split(v,e)
    p = initial
    refinements = 0
    while True:
        scale,lo,hi = weight_bounds(q % n,n,p)
        lower,upper = [0]*n,[0]*n
        for i in range(n):
            for j in range(n):
                k = (i+j) % n
                c = a[i]*b[j]
                lower[k] += c*lo[i]*lo[j]
                upper[k] += c*hi[i]*hi[j]
        t = []
        success = True
        for k in range(n):
            # 2 z_k/a_k lies in this closed rational interval.
            lnum,lden = 2*lower[k],scale*hi[k]
            hnum,hden = 2*upper[k],scale*lo[k]
            first = (lnum+lden-1)//lden
            last = hnum//hden
            assert first <= last  # A true integer exists, by the general proof.
            if first != last:
                success=False
                break
            t.append(first)
        if success:
            return t,p,refinements
        p *= 2
        refinements += 1
        assert p <= 32768, 'precision cap is not a proof of failure'


def intervals():
    rng = random.Random(20201102)
    cases = refined = max_p = total_refinements = 0
    histogram = {}
    params = [(q,n) for q in range(1,17) for n in [1,2,3,5,8,17]]
    params += [(q,n) for q,n in [(31,8),(64,7),(127,16),(256,15),
                               (512,32),(1023,64),(1024,63),(4096,65)]]
    for q,n in params:
        M = (1 << q)-1
        for j in range(4):
            u,v = [(0,M),(M,M),(1 << (q-1),1 << (q-1)),
                   (rng.getrandbits(q),rng.getrandbits(q))][j]
            # Interval routine never uses the exact convolution coefficients.
            got,p,r = interval_coefficients(u,v,q,n)
            assert got == coefficients(u,v,q,n)
            assert reconstruct(got,q,n)[0] == u*v % M
            cases += 1; refined += bool(r); total_refinements += r
            max_p = max(max_p,p)
            histogram[p] = histogram.get(p,0)+1
    return dict(cases=cases,forced_refinement_cases=refined,
                total_refinements=total_refinements,max_precision_bits=max_p,
                precision_histogram=histogram,seed=20201102,
                scope='Exact interval direct convolution, no floating-FFT error/performance claim')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--block',choices=['all','witness','exhaustive','large','intervals'],default='all')
    args=ap.parse_args()
    result=json.loads(OUT.read_text()) if OUT.exists() else {}
    blocks={'witness':witness,'exhaustive':exhaustive,'large':large_exact,'intervals':intervals}
    for name,fn in blocks.items():
        if args.block not in ('all',name) or name in result:
            continue
        t=time.monotonic(); data=fn(); data['seconds']=round(time.monotonic()-t,3)
        result[name]=data; OUT.write_text(json.dumps(result,indent=2)+'\n')
        print(json.dumps({'block':name,**data}),flush=True)

if __name__=='__main__': main()
