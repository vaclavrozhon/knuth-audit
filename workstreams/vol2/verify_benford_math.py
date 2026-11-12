#!/usr/bin/env python3
"""Independent finite checks for TAOCP 4.2.4; proofs are in notes/benford-math.md.

Each block is checkpointed. Existing successful blocks are never rerun.
"""
import cmath
import json
import math
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/benford-math.json'
mp.mp.dps = 70


def coeffs(r, n):
    L = mp.log(10)
    A = mp.log(10 / r)
    c = [mp.mpf(0), (r - 10) / 9]
    for m in range(1, n):
        v = mp.fsum(c[m + 1 - k] * L**k / math.factorial(k)
                    for k in range(1, m + 1))
        v += r * mp.fsum(A**k / math.factorial(k) for k in range(m + 1)) - 10
        c.append(v / 9)
    return c


def qr(r, m, s, c):
    if m == 0:
        return mp.mpf(1), mp.mpf(-1)
    q = 1 + mp.fsum(c[m-k] * mp.log(s)**k / math.factorial(k)
                   for k in range(m)) / s
    rr = -1 + r / s * mp.fsum(mp.log(s/r)**k / math.factorial(k)
                              for k in range(m))
    return q, rr


def sm(r, m, s, c):
    q, rr = qr(r, m, s, c)
    return q + rr * (s > r)


def lead(n, r):
    p = 10 ** (len(str(n)) - 1)
    return int(F(n, p) < r)


def count_formula(N, r):
    # Count disjoint integer intervals [10^j, r 10^j), cut at N.
    total = 0
    p = 1
    while p <= N:
        ceil = -((-r.numerator*p) // r.denominator)
        total += max(0, min(N+1, ceil)-p)
        p *= 10
    return total


def exact_counts():
    rs = [F(1), F(11,10), F(6,5), F(4,3), F(2), F(7,3),
          F(5), F(37,5), F(999,100), F(10)]
    checks = 0
    for r in rs:
        count = 0
        for N in range(1,10001):
            count += lead(N,r)
            assert count_formula(N,r) == count
            checks += 1
    a,b = 0,1
    fib=[]
    for n in range(1,101):
        a,b=b,a+b
        fib.append(a)
    hist={name:dict(sorted(Counter(str(x)[0] for x in seq).items()))
          for name,seq in [('factorials',[math.factorial(n) for n in range(1,101)]),
                           ('powers_of_two',[2**n for n in range(1,101)]),
                           ('Fibonacci_F1_to_F100',fib)]}
    assert all(v['1']==30 for v in hist.values())
    # First equality (8), at r=s=2, n=1: its RHS counts the boundary 20.
    printed = (math.ceil(2)-1 + math.floor(20)+1-10)
    actual = count_formula(20,F(2))
    assert (actual,printed)==(11,12)
    return {'count_comparisons':checks,'first_100_histograms':hist,
            'equation_8_boundary':{'r':2,'s':2,'n':1,'true_P1':'11/20',
                                   'printed_P1':'12/20'},
            'factorial_iteration_start_2':[2,2,2,2,2]}


def qf():
    checks=0
    samples=[]
    for rs in ['1','1.2','2','3.14159','9.9','10']:
        r=mp.mpf(rs); c=coeffs(r,12)
        for m in range(1,7):
            # Independent integration of the preceding piecewise function.
            def prev(t): return sm(r,m-1,t,c)
            full=mp.quad(prev,sorted(set([mp.mpf(1),r,mp.mpf(10)])))
            for s in sorted(set([mp.mpf(1), (1+r)/2, r,(10+r)/2,mp.mpf(10)])):
                partial=mp.quad(prev, sorted(set([mp.mpf(1),min(r,s),s])))
                v=(full/9+partial)/s
                assert abs(v-sm(r,m,s,c))<mp.mpf('1e-60')
                checks+=1
        # Coefficients of C*D=N (25), independent of the c recurrence's form.
        L=mp.log(10); A=mp.log(10/r)
        D=[mp.mpf(9)]+[-L**k/math.factorial(k) for k in range(1,13)]
        # C(z)=(r exp(Az)-10)*z / ((1-z)*(10-exp(Lz))).
        numer=[mp.mpf(0)]
        for k in range(1,13):
            numer.append(r*mp.fsum(A**j/math.factorial(j) for j in range(k))-10)
        for k in range(1,13):
            assert abs(mp.fsum(c[j]*D[k-j] for j in range(1,k+1))-numer[k])<mp.mpf('1e-59')
            checks+=1
        if rs=='2':
            for m in range(1,4):
                samples.append({'m':m,'values':{str(s):mp.nstr(sm(r,m,mp.mpf(s),c),18)
                               for s in [1,2,3,5,10]}})
    # A second representation: Fourier coefficients on the log circle.
    fourier_checks=0
    max_error=0
    L=math.log(10)
    for r in [1.2,2,3.14159,9.9]:
        c=coeffs(mp.mpf(str(r)),8); alpha=math.log10(r)
        for m in [2,3,5,8]:
            K=3000 if m==2 else 400
            tail=2/math.pi*(L/(2*math.pi))**m/(m*K**m)
            for s in [1,r,3.5,10]:
                val=alpha+2*sum(((1-cmath.exp(-2j*math.pi*k*alpha))/(2j*math.pi*k)
                         *cmath.exp(2j*math.pi*k*math.log(s)/L)
                         /(1+2j*math.pi*k/L)**m).real for k in range(1,K+1))
                err=abs(val-float(sm(mp.mpf(str(r)),m,mp.mpf(str(s)),c)))
                assert err <= tail + 2e-13,(r,m,s,err,tail)
                fourier_checks+=1;max_error=max(max_error,err)
    return {'integral_and_generating_function_checks':checks,
            'Fourier_comparisons_with_tail_bound':fourier_checks,
            'max_Fourier_difference':max_error,'figure_5_samples':samples}


def diagonal_cesaro():
    checks=0
    # Binomial basis formula in answer9 versus direct repeated averages.
    for q in [[F((-1)**j*(j+1),j+2) for j in range(20)],
              [F(int(j%3==0)) for j in range(20)]]:
        a=[sum(q[j-1]*math.comb(n-1,j-1) for j in range(1,n+1))
           for n in range(1,21)]
        for m in range(9):
            for n in range(1,21):
                v=sum(q[j-1]*F(1,j**m)*math.comb(n-1,j-1) for j in range(1,n+1))
                assert v==a[n-1];checks+=1
            a=[sum(a[:n])/n for n in range(1,21)]
    return {'exact_rational_comparisons':checks}


def carries():
    rows=[];checks=0
    for b in [2,3,10,16,64]:
        L=mp.log(b); low=mp.mpf(1)/b
        vals=[]
        for k in range(11):
            if k==0:
                formula=(mp.pi**2/6-2*mp.polylog(2,low))/L**2
                split=1-low
                quad=mp.quad(lambda v:-mp.log(1-v)/v,[low,split])/L**2 if split>low else mp.mpf(0)
                quad+=mp.quad(lambda v:L/v,[split,1])/L**2
            else:
                t=mp.mpf(b)**(-k)
                formula=(mp.polylog(2,t)-mp.polylog(2,t/b))/L**2
                quad=mp.quad(lambda v:-mp.log(1-t*v)/v,[low,1])/L**2
            assert abs(formula-quad)<mp.mpf('1e-59');checks+=1
            vals.append(formula)
        rows.append({'base':b,'coefficients':[mp.nstr(x,35) for x in vals]})
    # Leading1 after decimal addition, independent interval integration.
    p=[];L=mp.log(10)
    for k in range(1,13):
        lo=mp.mpf(10)**(-k);hi=10*lo
        val=mp.quad(lambda y:(mp.log(2-y)-mp.log(1-y/10))/y,[lo,hi])/L**2
        assert val<mp.log10(2);p.append(mp.nstr(val,35))
    b2=[mp.mpf(x) for x in next(row['coefficients'] for row in rows if row['base']==2)]
    b10=[mp.mpf(x) for x in next(row['coefficients'] for row in rows if row['base']==10)]
    out={}
    for b,weights,ps,tail in [(2,['.33','.12','.09','.07','.07','.04'],b2,'.19'),
                              (10,['.47','.23','.11','.03','.01','.01'],b10,'.04')]:
        subtotal=mp.fsum(mp.mpf(w)*p for w,p in zip(weights,ps))/mp.mpf('.91')
        out[str(b)]={'using_printed_entries_as_exact_lower':mp.nstr(subtotal,18),
                     'upper_all_nonzero_tail_at_k6':mp.nstr(subtotal+mp.mpf(tail)*ps[6]/mp.mpf('.91'),18)}
    return {'quadrature_vs_dilogarithm_checks':checks,'rows':rows,
            'decimal_leading1_k1_to_k12':p,
            'table_1_prediction_using_rounded_entries':out,
            'exercise1':mp.nstr(mp.mpf('.07')/mp.mpf('.455'),20),
            'exercise3_percent':mp.nstr(100*mp.log10(mp.mpf(24)/23),25)}


def asymptotic_cm():
    rows=[]
    for rs in ['1.2','2','3.14159','9.9']:
        r=mp.mpf(rs);c=coeffs(r,50);L=mp.log(10);theta=mp.atan(2*mp.pi/L)
        rho2=mp.sqrt(1+(4*mp.pi/L)**2)
        samples=[]
        for m in [6,10,20,40,50]:
            leading=(mp.sin(m*theta+2*mp.pi*mp.log10(r))-mp.sin(m*theta))/(mp.pi*(1+(2*mp.pi/L)**2)**(mp.mpf(m)/2))
            scaled=abs(c[m]-(mp.log10(r)-1)-leading)*rho2**m
            # This is a sample corroboration, not a proof of the O term.
            assert scaled<2
            samples.append({'m':m,'remainder_times_next_pole_radius_to_m':mp.nstr(scaled,18)})
        rows.append({'r':rs,'samples':samples})
    return rows


if __name__=='__main__':
    state=json.loads(OUT.read_text()) if OUT.exists() else {'blocks':{}}
    for name,fn in [('exact_counts',exact_counts),('lemma_Q_theorem_F',qf),
                    ('Cesaro_binomial_basis',diagonal_cesaro),('arithmetic_probabilities',carries),
                    ('coefficient_asymptotic',asymptotic_cm)]:
        if name in state['blocks']:continue
        state['blocks'][name]=fn()
        OUT.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n')
        print(name,'PASS',flush=True)
