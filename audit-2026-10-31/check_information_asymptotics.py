"""Independent finite-sum checks of MPR 122 and corrected MPR 124.

No Monte Carlo: 122 uses 60-decimal binomial sums; 124 enumerates the
distribution of the number of ones among n binary samples exactly.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 60


def real(x):
    return mp.mpf(x.numerator)/x.denominator if isinstance(x, F) else mp.mpf(x)


def binomial_poisson(n, p):
    q = 1-p
    weight = q**n
    logfact = [mp.loggamma(k+1) for k in range(n+1)]
    mass, total = mp.mpf(0), mp.mpf(0)
    for k in range(n+1):
        # Cancellation of k! and p^k gives this log likelihood ratio.
        logrho = logfact[n]-logfact[n-k]-k*mp.log(n)+(n-k)*mp.log(q)+n*p
        mass += weight
        total += weight*logrho
        if k < n:
            weight *= mp.mpf(n-k)/(k+1)*p/q
    assert abs(mass-1) < mp.mpf('1e-50')
    return total/mp.log(2)


def importance_case(x, y, f, n):
    rho = [y[i]/x[i] for i in range(2)]
    d = sum(real(y[i])*mp.log(real(rho[i]), 2) for i in range(2) if y[i])
    scale = 2**d
    c = (n/scale)**mp.mpf('.25')
    m = mp.sqrt(n*scale)
    delta = sum(y[i] for i in range(2) if real(rho[i]) > m)
    true = sum(y[i]*f[i] for i in range(2))
    norm = mp.sqrt(real(sum(y[i]*f[i]**2 for i in range(2))))
    distribution = []
    for k in range(n+1):
        weight = comb(n,k)*x[1]**k*x[0]**(n-k)
        estimate = ((n-k)*rho[0]*f[0]+k*rho[1]*f[1])/n
        distribution.append((weight, estimate))
    assert sum(w for w, _ in distribution) == 1
    if c > 1 + mp.mpf('1e-40'):
        error = sum(w*abs(estimate-true) for w, estimate in distribution)
        bound = norm*(1/c+2*mp.sqrt(real(delta)))
        assert real(error) <= bound+mp.mpf('1e-50'), (x,y,f,n,error,bound)
        return 'upper'
    if c < 1 - mp.mpf('1e-40') and f == (F(1), F(1)):
        for a in (F(1,4), F(1,2), F(3,4)):
            probability = sum(w for w, estimate in distribution if estimate >= a)
            bound = c*c+real(1-delta)/real(a)
            assert real(probability) <= bound+mp.mpf('1e-50')
        return 'lower'
    return 'boundary_or_not_applicable'


def main():
    rows = []
    for text_p in ('.1','.25','.5','.75','.9'):
        p = mp.mpf(text_p)
        leading = (-mp.log(1-p)-p)/(2*mp.log(2))
        coefficient = p*p/(12*(1-p)*mp.log(2))
        for n in (20,50,100,200,500,1000,2000,10000):
            actual = binomial_poisson(n,p)
            scaled_error = n*(actual-leading)
            rows.append({'p':text_p,'n':n,'D_bits':mp.nstr(actual,30),
                         'leading':mp.nstr(leading,30),
                         'n_times_error':mp.nstr(scaled_error,30),
                         'predicted_limit':mp.nstr(coefficient,30)})
        assert abs(scaled_error/coefficient-1) < mp.mpf('.005')
    biases = (F(1,16),F(1,4),F(1,2),F(3,4),F(15,16))
    targets = (F(0),)+biases+(F(1),)
    functions = [(F(a),F(b)) for a in (-2,-1,0,1,2) for b in (-2,-1,0,1,2)]
    counts = {}
    for px in biases:
        for py in targets:
            for f in functions:
                for n in (1,2,3,4,8):
                    kind = importance_case((1-px,px),(1-py,py),f,n)
                    counts[kind] = counts.get(kind,0)+1
    # Two exact discrepancies in the answer, separate from the already
    # published correction to the exercise statement.
    # x=y=(1/2,1/2), f=(0,1), n=2. The squared sample error is 0 or 1/4,
    # whereas var(E_n(f)) is 1/8. Only its expectation equals the variance.
    assert F(1,4)/2 == F(1,8)
    # x=(15/16,1/16), y=(1/2,1/2), f=(0,-1), n=4.
    # 2^D=8/sqrt(15), c>1, and m=sqrt(32/sqrt(15)) lies between 8/15 and 8.
    # Thus g=0; on the positive-probability all-zero sample the claimed
    # triangle equality reads 1/2=-1/2.
    m = mp.sqrt(32/mp.sqrt(15))
    assert real(F(8,15)) < m < 8
    report = {
        'exercises':'MPR 122 and 124',
        'precision_decimal_digits':mp.mp.dps,
        'binomial_poisson_rows':rows,
        'asymptotic_conclusion':'Printed leading term agrees. Independently derived next coefficient is p^2/(12(1-p) ln(2)); finite sums converge to it.',
        'reverse_divergence':'Infinity: Poisson has positive mass at n+1, binomial has zero mass there.',
        'importance_sampling_checks':counts,
        'importance_known_erratum':'The exercise statement needs expectation, already published 2025-07-15.',
        'answer_followup_C004':{
            'page':390,
            'first_equality_counterexample':'x=(15/16,1/16), y=(1/2,1/2), f=(0,-1), n=4; g=0. All-zero sample has probability (15/16)^4; LHS=1/2, RHS=-1/2.',
            'variance_equality_counterexample':'x=y=(1/2,1/2), f=(0,1), n=2: squared error is 0 or 1/4; variance is 1/8.',
            'correction':'Use triangle inequality with three absolute values, then expectations. The last term is bounded only in expectation. Insert expectation in the squared-error identity.',
            'classification':'Follow-up to the already published statement correction, not counted as a new independent finding yet.'},
        'limitations':'Finite checks support the formulas; asymptotic and corrected importance-sampling proofs are recorded separately in mathematical notes.'}
    path = Path(__file__).parent/'results/information_asymptotics.json'
    path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'binomial_poisson_cases':len(rows),'importance_sampling_checks':counts,
                      'last_asymptotic_row':rows[-1],'result':str(path)},indent=2))


if __name__ == '__main__':
    main()
