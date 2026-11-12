"""Exact cross-checks for TAOCP 3.4.1 F and exercises 17--33 (selected).

General proofs, limits, and excluded exercises are in discrete-distributions.md.
Uses independent polynomial integration and finite-state probability models.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial
from pathlib import Path
import json
import sys
import mpmath as mp
import sympy as s

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/discrete-distributions.json'
mp.mp.dps=80


def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def power_linear(c,d,n):
    return [comb(n,k)*c**(n-k)*d**k for k in range(n+1)]


def integrate(poly,lo,hi):
    return sum(c*(hi**(k+1)-lo**(k+1))/Q(k+1) for k,c in enumerate(poly))


def binomial_split():
    count=0
    for t in range(1,13):
        for a in range(1,t+1):
            b=t+1-a
            constant=Q(factorial(t),factorial(a-1)*factorial(b-1))
            for p in [Q(1,7),Q(1,2),Q(5,7)]:
                total=Q(0)
                for n in range(t+1):
                    if n<a:
                        poly=mul(power_linear(-p,Q(1),a-1-n),power_linear(Q(1),Q(-1),b-1))
                        value=constant*comb(a-1,n)*p**n*integrate(poly,p,Q(1))
                    else:
                        poly=[Q(0)]*(a-1)+power_linear(p,Q(-1),n-a)
                        value=constant*comb(b-1,n-a)*(1-p)**(t-n)*integrate(poly,Q(0),p)
                    assert value==comb(t,n)*p**n*(1-p)**(t-n)
                    total+=value;count+=1
                assert total==1
    # Continuous binomial CDF: integrate its integer-shape beta polynomial.
    count_cdf=0
    for t in range(1,21):
        for k in range(1,t+1):
            for p in [Q(1,5),Q(1,2),Q(4,5)]:
                poly=[Q(0)]*(k-1)+power_linear(Q(1),Q(-1),t-k)
                v=Q(factorial(t),factorial(k-1)*factorial(t-k))*integrate(poly,p,Q(1))
                assert v==sum(comb(t,j)*p**j*(1-p)**(t-j) for j in range(k))
                count_cdf+=1
    return dict(split_branch_probabilities=count,continuous_binomial_cdf_values=count_cdf,
                C0056=dict(t=1,p='1/2',x=1,extraneous_n=2,printed='1/8',correct='1/2'))


def bit_binomial():
    models=0;transitions=0
    for t in range(11):
        for digits in range(1,7):
            den=2**digits
            for numerator in range(den):
                states={(t,0):Q(1)}
                for j in range(digits):
                    bit=(numerator>>(digits-1-j))&1
                    nxt=defaultdict(Q)
                    for (m,N),prob in states.items():
                        for M in range(m+1):
                            nxt[m-M,N+bit*M]+=prob*Q(comb(m,M),2**m)
                            transitions+=1
                    states=nxt
                masses=defaultdict(Q)
                for (m,N),prob in states.items():masses[N]+=prob
                p=Q(numerator,den)
                assert all(masses[n]==comb(t,n)*p**n*(1-p)**(t-n) for n in range(t+1))
                models+=1
    # Independent recurrence for max of geometric waiting times.
    A=[Q(0)]
    for n in range(1,81):
        value=(2**n+sum(comb(n,k)*A[k] for k in range(n)))/Q(2**n-1)
        explicit=1+sum(Q((-1)**(k+1)*comb(n,k),2**k-1) for k in range(1,n+1))
        assert value==explicit
        A.append(value)
    # Numerically check the explicitly defined periodic term, not a bare symbol.
    examples=[]
    for n in [10**3,10**5,10**7,10**9]:
        exact=sum(-mp.expm1(n*mp.log1p(-mp.mpf(2)**(-j))) for j in range(1,350))+1
        delta=2/mp.log(2)*sum(mp.re(mp.gamma(-2j*mp.pi*k/mp.log(2))*mp.exp(2j*mp.pi*k*mp.log(n,2))) for k in range(1,8))
        approximation=mp.log(n,2)+mp.euler/mp.log(2)+mp.mpf('.5')-delta
        error=exact-approximation
        assert abs(error)*n<1
        examples.append(dict(n=n,mean=mp.nstr(exact,40),periodic_f0=mp.nstr(-delta,35),scaled_remainder=mp.nstr(n*error,30)))
    return dict(exact_dyadic_models=models,state_transitions=transitions,mean_recurrence_cases=80,
                A1=str(A[1]),A2=str(A[2]),asymptotic_examples=examples,
                note='p=1 has the direct deterministic result N=t, or the all-one nonterminating expansion. The explicit periodic series corresponds to minus delta_0 in Vol.3 edition2.')


def elementary_and_geometry():
    # Enumerate all nested AND/OR expressions, not just the printed one.
    expressions=0;truth_rows=0
    for depth in range(1,7):
        for ops in product([0,1],repeat=depth):
            ones=0
            for bits in product([0,1],repeat=depth+1):
                result=bits[-1]
                for op,left in reversed(list(zip(ops,bits[:-1]))):
                    result=(left|result) if op else (left&result)
                ones+=result;truth_rows+=1
            expected=Q(int(''.join(map(str,ops))+'1',2),2**(depth+1))
            assert Q(ones,2**(depth+1))==expected
            expressions+=1
    # Ellipsoid extremum: numerator s^(n+1), denominator (M+m)s-Mm.
    z,M,m=s.symbols('z M m',positive=True)
    extrema=[]
    for n in range(2,13):
        obj=z**(n+1)/((M+m)*z-M*m)
        numerator=s.factor(s.diff(obj,z)*((M+m)*z-M*m)**2/z**n)
        assert s.expand(numerator-(n*(M+m)*z-(n+1)*M*m))==0
        for lower in range(1,5):
            for upper in range(lower,41):
                star=Q((n+1)*upper*lower,n*(upper+lower))
                location=max(Q(lower),star)
                value=location**(n+1)/((upper+lower)*location-upper*lower)
                expected=Q(lower)**(n-1) if n*lower>=upper else Q(n+1,upper+lower)**(n+1)*Q(upper*lower,n)**n
                assert value==expected
                weight=(location-lower)/Q(upper-lower) if upper>lower else Q(0)
                assert 0<=weight<=1
                extrema.append(dict(n=n,a_min=lower,a_max=upper,s=str(location),K2=str(value)))
    # Independent exponential bits: all lower bits of a truncated geometric.
    bit_words=0
    for width in range(1,9):
        for q in [Q(1,3),Q(1,2),Q(3,4)]:
            for value in range(2**width):
                mass=Q(1)
                for j in range(width):
                    r=q**(2**j)
                    mass*=r/(1+r) if (value>>j)&1 else 1/(1+r)
                expected=(1-q)*q**value/(1-q**(2**width))
                assert mass==expected
                bit_words+=1
    return dict(boolean_expressions=expressions,boolean_truth_rows=truth_rows,
                ellipsoid_extrema_cases=len(extrema),ellipsoid_extrema=extrema,
                independent_exponential_bit_words=bit_words)


def main():
    out=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('binomial_split',binomial_split),('bit_binomial',bit_binomial),('elementary_and_geometry',elementary_and_geometry)]:
        if name in out:continue
        print('START',name,flush=True)
        out[name]=fn();OUT.write_text(json.dumps(out,indent=2)+'\n')
        print('PASS',name,flush=True)


if __name__=='__main__':main()
