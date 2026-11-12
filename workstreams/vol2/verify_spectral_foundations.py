"""Finite independent checks for TAOCP2 3.3.4 A--D and exercises1--15.

The accompanying notes supply general proofs. Each block checkpoints so that
--resume does not repeat completed work.
"""
import argparse
from fractions import Fraction as Q
from itertools import product
import json
from math import gcd, ceil, floor
from pathlib import Path
import time

from spectral import spectral_s, shortest_direct, dot

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/spectral-foundations.json'


def euclidean_candidates(a, m):
    h, hp, p, pp = a, m, 1, 0
    qs, candidates = [], [m*m]
    while h:
        candidates.append(h*h+p*p)
        q = hp//h
        qs.append(q)
        hp, h, pp, p = h, hp-q*h, p, pp-q*p
    return qs, min(candidates)


def small_s():
    models = dimensions = direct_points = largest_box = 0
    bound_exceptions = []
    pairs = [(a,m) for m in range(2,61) for a in range(1,m) if gcd(a,m)==1]
    pairs += [(97,131),(151,405)]
    for a,m in pairs:
            result = spectral_s(a, m, 6)
            qs, euclidean = euclidean_candidates(a, m)
            assert result['values'][2]['squared'] == euclidean
            A = max(qs)
            if Q(euclidean)*(A+1+Q(1,A)) <= 2*m:
                bound_exceptions.append(dict(a=a,m=m,quotients=qs,squared=euclidean,
                                             printed_denominator=str(A+1+Q(1,A))))
            assert euclidean*(A+2) > 2*m
            for t, data in result['values'].items():
                witness = (min(data['U'], key=lambda row: dot(row,row))
                           if t == 2 else data['minimum_vectors'][0])
                assert dot(witness,witness) == data['squared']
                assert sum(u*pow(a,j,m) for j,u in enumerate(witness)) % m == 0
                best, vectors, n = shortest_direct(a,m,t,data['squared'])
                assert best == data['squared'], (a,m,t,best,data)
                if t > 2:
                    actual = {tuple(v) for v in data['minimum_vectors']}
                    actual |= {tuple(-x for x in v) for v in data['minimum_vectors']}
                    assert actual == set(vectors), (a,m,t)
                    largest_box = max(largest_box, data['searched'])
                dimensions += 1
                direct_points += n
            models += 1
    example = spectral_s(41,100,3,trace=True)
    assert example['values'][2]['squared'] == 50
    v = example['values'][3]
    assert v['U'] == [[-3,1,2],[-5,-8,-7],[1,-2,1]]
    assert v['V'] == [[-22,-2,18],[-5,-5,-5],[9,-31,29]]
    assert v['z'] == [0,0,1] and v['squared'] == 6
    return dict(models=models,dimensions=dimensions,direct_admissible_points=direct_points,
                largest_search_half_box=largest_box,example14=example,
                exercise6_exceptions=bound_exceptions,
                scope='All coprime1<=a<m<=60 plus97/131 and151/405, t2..6; literal S versus original-coordinate sphere enumeration; all minimizers checked in dimensions3..6. Printed bound6 exceptions recorded; repaired A+2 denominator checked.')


def prime_divisors(m):
    ps = []
    p = 2
    while p*p <= m:
        if m % p == 0:
            ps.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        ps.append(m)
    return ps


def potency_two():
    short = {t: sorted((sum(x*x for x in u),u)
                       for u in product(range(-2,3),repeat=t)
                       if 0 < sum(x*x for x in u) <= bound)
             for t,bound in [(3,6),(4,4)]}
    models = binary = ternary = 0
    errors_2003 = []
    for m in range(2,513):
        ps = prime_divisors(m)
        for a in range(2,m):
            b = a-1
            if b*b % m or any(b % p for p in ps) or (m % 4 == 0 and b % 4):
                continue
            actual = {t: next(n for n,u in short[t]
                              if sum(x*pow(a,j,m) for j,x in enumerate(u)) % m == 0)
                      for t in (3,4)}
            first = m % 8 == 0 and a == m//2+1
            second = m % 9 == 0 and a in (m//3+1,2*m//3+1)
            proposed = {3: 2 if first else (5 if m == 9 else 6),
                        4: 2 if first or second else 4}
            assert actual == proposed, (a,m,actual,proposed)
            errata = {3: 5 if m == 9 else 6, 4: 2 if second else 4}
            if actual != errata:
                errors_2003.append(dict(a=a,m=m,actual=actual,errata=errata))
            models += 1
            binary += first
            ternary += second
    orbit = [];x=0
    while x not in orbit:
        orbit.append(x);x=(5*x+1)%8
    assert x == 0 and len(orbit) == 8
    return dict(models=models,binary_cases=binary,ternary_cases=ternary,
                errors_after_2003=len(errors_2003),first_errors=errors_2003[:6],
                counterexample_orbit=orbit,
                scope='All full-period potency-two multipliers m<=512; exhaustive short vectors, independent of S. Corrected binary family m=8q,a=4q+1.')


def hyperplane_count(u,rho):
    neg = sum(x for x in u if x<0)
    pos = sum(x for x in u if x>0)
    lo, hi = Q(neg)-rho, Q(pos)-rho
    # The lower endpoint is included precisely when there is no negative
    # coefficient; the upper endpoint iff there is no positive coefficient.
    first = ceil(lo) if neg == 0 else floor(lo)+1
    last = floor(hi) if pos == 0 else ceil(hi)-1
    return max(0,last-first+1)


def planes():
    cases = 0
    for t in range(1,6):
        for u in product(range(-2,3),repeat=t):
            if not any(u):
                continue
            norm = sum(abs(x) for x in u)
            mixed = min(u)<0<max(u)
            for rho in (Q(0),Q(1,7),Q(1,2),Q(6,7)):
                count = hyperplane_count(u,rho)
                corrected = norm-int(mixed and rho == 0)
                assert count == corrected, (u,rho,count,corrected)
                cases += 1
    examples = []
    for m,a,c,u in [(4,1,0,(1,-1)),(4,1,1,(1,-1))]+[
            (256,137,c,u) for u in [(18,-2),(7,-15),(11,13)] for c in [0,1,187,255]]:
        rho = Q(c*u[1],m)
        occupied = sorted({Q(u[0]*x+u[1]*((a*x+c)%m),m) for x in range(m)})
        assert all((q-rho).denominator == 1 for q in occupied)
        examples.append(dict(m=m,a=a,c=c,normal=u,offset=str(rho%1),
                             intersecting=hyperplane_count(u,rho),occupied=len(occupied),
                             levels=[str(v) for v in occupied]))
    accuracy = spectral_s(137,256,3)['values']
    assert accuracy[2]['squared'] == 274 and accuracy[3]['squared'] == 30
    return dict(interval_cases=cases,examples=examples,
                figure8_squared_accuracies={t:d['squared'] for t,d in accuracy.items()},
                scope='Exact open/closed image endpoints of [0,1)^t; occupied levels counted separately. Three c187 line counts20/21/24 match Fig8 text.')


def rational_reductions():
    import random
    import sympy as sp
    rng=random.Random(332026)
    count=0
    for t in range(2,6):
        for sample in range(12):
            while True:
                U=sp.Matrix([[rng.randrange(-5,6) for _ in range(t)] for _ in range(t)])
                if U.det():break
            V=U.inv().T
            j=sample%t
            q=[sp.S(0) if i==j else V.row(i).dot(V.row(j))/V.row(j).dot(V.row(j)) for i in range(t)]
            Up,Vp=U.copy(),V.copy()
            Up[j,:]=U.row(j)+sum((q[i]*U.row(i) for i in range(t) if i!=j),sp.zeros(1,t))
            for i in range(t):
                if i!=j:Vp[i,:]=V.row(i)-q[i]*V.row(j)
            assert Up*Vp.T==sp.eye(t)
            for i in range(t):
                if i==j:continue
                assert Up.row(j).dot(Up.row(i))==0
                assert Vp.row(j).dot(Vp.row(i))==0
            assert Up.row(j).dot(Up.row(j))<=U.row(j).dot(U.row(j))
            count+=1
    return dict(cases=count,scope='Exact rational real minimizers satisfy both24/26 and preserve duality, dimensions2..5. General proof in notes.')


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    result=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}
    for name,fun in [('small_s',small_s),('potency_two',potency_two),('planes',planes),('rational_reductions',rational_reductions)]:
        if name in result:continue
        start=time.monotonic();result[name]=fun();result[name]['seconds']=time.monotonic()-start
        OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
        print(name,{k:v for k,v in result[name].items() if k not in ['example14','examples']},flush=True)
