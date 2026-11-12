"""Exact finite-support audit of MPR 125(b,f,g), with boundary cases."""
from itertools import product
from math import comb
from pathlib import Path
import json


def no_internal_zeros(a):
    support=[k for k,x in enumerate(a) if x]
    return not support or support==list(range(support[0],support[-1]+1))


def log_concave(a):
    return no_internal_zeros(a) and all(a[k]**2>=a[k-1]*a[k+1]
                                       for k in range(1,len(a)-1))


def convolve(a,b,binomial=False):
    return [sum((comb(n,k) if binomial else 1)*a[k]*b[n-k]
                for k in range(len(a)) if 0<=n-k<len(b))
            for n in range(len(a)+len(b)-1)]


def main():
    sequences=[a for a in product(range(4),repeat=5) if log_concave(a)]
    shifts=0
    failures=[]
    for a in sequences:
        for c in range(4):
            printed=c*a[1]<=a[0]**2
            actual=log_concave((c,)+a)
            # The adjacent inequalities alone are correct; the new support
            # must also stay an interval, as required in the exercise setup.
            corrected=printed and no_internal_zeros((c,)+a)
            assert corrected==actual
            if printed!=actual:
                failures.append({'a':a,'c':c,'first_positive_index':next(i for i,x in enumerate(a) if x)})
            shifts+=1
    pairs=0
    for a in sequences:
        for b in sequences:
            assert log_concave(convolve(a,b))
            assert log_concave(convolve(a,b,True))
            pairs+=1
    assert all(item['c']>0 and item['first_positive_index']>=2 for item in failures)
    assert failures
    report={'exercise':'MPR 125',
            'finite_sequences':len(sequences),
            'sequence_description':'Length 5; entries 0,1,2,3; extended by zeros to infinity; log-concave with no internal zeros.',
            'right_shifts_checked':shifts,
            'right_shift_discrepancies':len(failures),
            'small_example':{'a':[0,0,1,0,0],'c':1,
                             'printed_condition':'1*0 <= 0^2, true',
                             'shifted_sequence':[1,0,0,1,0,0],
                             'issue':'The shifted sequence has internal zeros, contrary to the exercise setup. Adjacent log-concavity inequalities still hold.'},
            'ordinary_and_binomial_convolution_pairs_checked':pairs,
            'classification':'C005: convention/scope issue, not included among definite new corrections.',
            'limitations':'Finite-support checks cover log-concave convolutions and shifts. Log-convex sums and binomial convolutions are not tested by this program.'}
    (Path(__file__).parent/'results/log_concavity.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
