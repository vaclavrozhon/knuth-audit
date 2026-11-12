"""Certified base-2..36 prefixes for TAOCP exercise 3.3.2-6.

Integer arithmetic bounds e between A/K! and (K*A+1)/(K*K!),
where A/K! = sum_{j=0}^K 1/j!. Both endpoints give the same scaled floor.
"""
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import mpmath as mp
import sys

ROOT = Path(__file__).resolve().parent
DEST = ROOT/'results/e-digits.json'
ALPHABET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mp.mp.dps = 60


def digits(x,b,length=None):
    out = []
    while x:
        x,r = divmod(x,b)
        out.append(r)
    if length is not None:
        assert len(out) <= length
        out += [0]*(length-len(out))
    return list(reversed(out)) or [0]


def summarize(word,b):
    c = Counter(word)
    v = Q(b*sum(c[j]**2 for j in range(b)),len(word))-len(word)
    shape = mp.mpf(b-1)/2
    p = mp.gammainc(shape,0,mp.mpf(v.numerator)/v.denominator/2)/mp.gamma(shape)
    return dict(counts=[c[j] for j in range(b)],chi_square=str(v),
                decimal_chi_square=float(v),asymptotic_chi_square_CDF=mp.nstr(p,30))


def save(out):
    DEST.write_text(json.dumps(out,indent=2)+'\n')


def main():
    out = json.loads(DEST.read_text()) if '--resume' in sys.argv else {}
    length = 10000
    cap = 36**length * 10**12
    k = 0
    a = f = 1
    while f <= cap:
        k += 1
        f *= k
        a = k*a+1
    out.update(status='in_progress',terms_through_k=k,
               rigorous_interval='[sum(1/j!,j=0..K), sum(1/j!,j=0..K)+1/(K*K!)]',
               interpretation='Fixed prefix counts; chi-square CDF is asymptotic calibration, not a proof about normality of e.')
    out.setdefault('bases',{})
    for b in range(2,37):
        if str(b) in out['bases']:
            continue
        scale = b**length
        lower = a*scale//f
        upper = (a*k+1)*scale//(f*k)
        assert lower == upper
        word = digits(lower-2*scale,b,length)
        integer = digits(2,b)
        text = ''.join(ALPHABET[j] for j in word)
        row = dict(scaled_floor_certified=True,
                   fractional_sha256=hashlib.sha256(text.encode()).hexdigest(),
                   first32=text[:32],last32=text[-32:],samples={})
        for n in [2000,10000]:
            row['samples'][str(n)] = {
                'fractional_only':summarize(word[:n],b),
                'including_integer_part':summarize((integer+word)[:n],b)}
        out['bases'][str(b)] = row
        save(out)
        print('base',b,'2000',row['samples']['2000']['fractional_only']['chi_square'],
              '10000',row['samples']['10000']['fractional_only']['chi_square'],flush=True)
    if 'decimal_independent_check' not in out:
        # A separate standard-library decimal exponential implementation.
        with localcontext() as ctx:
            ctx.prec = length+30
            independent = str(Decimal(1).exp()).split('.')[1][:length]
        assert hashlib.sha256(independent.encode()).hexdigest() == out['bases']['10']['fractional_sha256']
        out['decimal_independent_check'] = dict(method='decimal.Decimal(1).exp()',
                                               precision=length+30,matching_digits=length)
        save(out)
    if 'book_threshold_1_15_upper_probability' not in out:
        out['book_threshold_1_15_upper_probability'] = mp.nstr(
            mp.gammainc(mp.mpf('4.5'),mp.mpf('1.15')/2,mp.inf)
            /mp.gamma(mp.mpf('4.5')),40)
    out['status'] = 'completed'
    save(out)


if __name__ == '__main__':
    main()
