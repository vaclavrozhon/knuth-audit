"""Exact counterexamples to MPR 134(b) and a local error in answer 137(d)."""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import json
import mpmath as mp


def two_sample_error_probability(m,epsilon,p):
    weights=[F(comb(m,k))*p**k*(1-p)**(m-k) for k in range(m+1)]
    return sum(weights[a]*weights[b] for a in range(m+1) for b in range(m+1)
               if abs(F(a-b,m))>epsilon)


def main():
    mp.mp.dps=60
    epsilon=F(9,10)
    prob=two_sample_error_probability(1,epsilon,F(1,2))
    assert prob==F(1,2)
    exponent=2*epsilon**2
    exp_lower=sum(exponent**j/F(factorial(j)) for j in range(4))
    assert exp_lower>4  # Therefore 2*exp(-exponent)<1/2, exactly.
    # A larger sample shows the failure is not confined to m=1.
    large=2*sum(F(comb(200,k),2**200) for k in range(80))
    assert large==two_sample_error_probability(100,F(1,5),F(1,2))
    assert float(large)>2*mp.exp(-8)
    corrected_checks=0
    for m in range(1,21):
        for p in (F(1,4),F(1,2),F(3,4)):
            for epsilon in (F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)):
                actual=two_sample_error_probability(m,epsilon,p)
                ee=mp.mpf(epsilon.numerator)/epsilon.denominator
                stronger_bound=2*mp.exp(-m*ee**2)
                assert mp.mpf(actual.numerator)/actual.denominator<=stronger_bound
                corrected_checks+=1
    # The error in the median proof is pointwise, even in an admissible
    # distribution having unique median m=1.
    x,c,median=-1,0,1
    actual_delta=abs(x-c)-abs(x-median)
    printed_delta=c-median+2*(x-c)
    corrected_delta=c-median+2*max(0,x-c)
    assert actual_delta==-1 and printed_delta==-3 and corrected_delta==actual_delta
    report={
        'F014_two_sample_bound':{
            'pages':[27,394],'exercise':'MPR 134(b)',
            'm':1,'event_probability':'1/2','epsilon':'9/10',
            'actual_tail_probability':str(prob),
            'printed_bound':'2*exp(-81/50)',
            'printed_bound_numeric':mp.nstr(2*mp.exp(-mp.mpf(81)/50),30),
            'exact_certificate':'exp(81/50)>sum_(j=0)^3 (81/50)^j/j! = '+str(exp_lower)+' > 4.',
            'larger_example':{'m':100,'epsilon':'1/5','actual':float(large),'printed':float(2*mp.exp(-8))},
            'proof_error':'|k-K/2| must exceed epsilon*m/2, not epsilon*m.',
            'correction_following_book_hint':'Use 2*exp(-epsilon^2*m/2), which also proves the stated bound in (c).',
            'stronger_unconditional_bound':'Independence of all 2m Bernoulli trials gives 2*exp(-epsilon^2*m).',
            'source_scope':'Visually verified in PDF. Exercise not present in retrieved author Pre-Fascicle 5A.'},
        'corrected_bound_finite_checks':corrected_checks,
        'F015_median_difference':{
            'page':395,'answer':'MPR 137(d)',
            'example':'X=-1 with probability 1/4 and X=1 with probability 3/4; median m=1,c=0. At x=-1, actual Delta=-1, printed Delta=-3.',
            'printed':'c-m+2*(x-c) for x<m',
            'corrected':'c-m+2*max(0,x-c) for x<m',
            'scope':'The median-minimizes-absolute-deviation theorem and the subsequent lower bound are correct; this intermediate identity is not.',
            'source_scope':'PDF only; not in retrieved 2019 Pre-Fascicle 5A.'}}
    (Path(__file__).parent/'results/two_sample_bound.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
