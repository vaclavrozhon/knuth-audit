"""Exact arithmetic checks for the elementary block of TAOCP2 section4.1.

The proofs are in notes/positional-basic.md. Blocks are checkpointed, so
successful work is retained when a later source transcription needs repair.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from functools import lru_cache
import json
import math

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/positional-basic.json'


def value(word, base):
    v = 0
    for d in word:
        v = v * base + d
    return v


def expand(n, base, balanced=False):
    digits = []
    while n:
        d = n % abs(base)
        if balanced and d == 2:
            d = -1
        n = (n-d)//base
        digits.append(d)
    return list(reversed(digits or [0]))


def periodic(integer, fraction, base):
    return F(value(integer, base)) + F(value(fraction, base), base**len(fraction)-1)


def atan_bounds(q, n):
    s = sum((F((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(n)), F(0))
    next_term = F((-1)**n, (2*n+1)*q**(2*n+1))
    return min(s, s+next_term), max(s, s+next_term)


def pi_bounds():
    a, b = atan_bounds(5, 70)
    c, d = atan_bounds(239, 24)
    return 16*a-4*d, 16*b-4*c


def fraction_interval(integer, digits, base, balanced=False):
    prefix = F(value(integer, base)) + F(value(digits, base), base**len(digits))
    if balanced:
        lo, hi = F(-1, 2), F(1, 2)
    elif base < 0:
        b = -base
        lo, hi = F(-b, b+1), F(1, b+1)
    else:
        lo, hi = F(0), F(1)
    tail = sorted((lo/F(base**len(digits)), hi/F(base**len(digits))))
    return prefix+tail[0], prefix+tail[1]


def add_negative(left, right, sign=1):
    n = max(len(left), len(right))
    a = list(reversed(left)) + [0]*(n-len(left)+2)
    b = list(reversed(right)) + [0]*(n-len(right)+2)
    carry = 0
    result = []
    for x, y in zip(a, b):
        z = x + sign*y + carry
        if z >= 2:
            carry, z = -1, z-2
        elif z < 0:
            carry, z = 1, z+2
        else:
            carry = 0
        assert z in (0, 1)
        result.append(z)
    assert carry == 0
    return list(reversed(result))


def cadd(a, b):
    return a[0]+b[0], a[1]+b[1]


def cmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def complex_value(word, radix=(0, 2)):
    v = (0, 0)
    for d in word:
        v = cadd(cmul(v, radix), (d, 0))
    return v


def quater_product(a, b):
    raw = [0]*(len(a)+len(b))
    for i, x in enumerate(reversed(a)):
        for j, y in enumerate(reversed(b)):
            raw[i+j] += x*y
    i = 0
    while i < len(raw):
        q, raw[i] = divmod(raw[i], 4)
        if q:
            while len(raw) <= i+2:
                raw.append(0)
            raw[i+2] -= q
        i += 1
        assert i < 100
    while len(raw) > 1 and raw[-1] == 0:
        raw.pop()
    return list(reversed(raw))


def mixed_value(digits, radices):
    # dictionaries use the index of the place; w0=1, w_(j+1)=b_j*w_j.
    lo, hi = min(digits), max(digits)
    weights = {0: F(1)}
    for j in range(hi):
        weights[j+1] = weights[j]*radices[j]
    for j in range(-1, lo-1, -1):
        weights[j] = weights[j+1]/radices[j]
    return sum((digits[j]*weights[j] for j in digits), F(0))


def naf(n):
    out = []
    while n:
        d = 0 if n % 2 == 0 else 2-(n % 4)
        out.append(d)
        n = (n-d)//2
    return list(reversed(out))


def reversing(n):
    if n == 0:
        return []
    if n % 2 == 0:
        return [x+1 for x in reversing(n//2)]
    return [0] + [x+1 for x in reversing((1-n)//2)]


def pattern_weight(n):
    # E,A,B,C are the four suffix states explained in the note.
    transitions = {'E': ('E', 'A'), 'A': ('E', 'B'),
                   'B': ('C', 'B'), 'C': ('E', 'B')}
    state = 'E'
    count = 0
    for bit in bin(n)[2:]:
        count += bit == '1' and state != 'B'
        state = transitions[state][int(bit)]
    return count


def main():
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    def save(key, result):
        data[key] = result
        OUT.write_text(json.dumps(data, indent=2) + '\n')
        print('PASS', key, flush=True)

    if 'printed_numbers' not in data:
        records = []
        def equal(label, actual, expected):
            assert actual == expected, (label, actual, expected)
            records.append({'label': label, 'value': str(actual)})
        equal('p195 base6', F(value([5,2,0,3],6),6), F(385,2))
        equal('p196 reciprocal81 with scale60^4', F(value([44,26,40],60),60**4), F(1,81))
        equal('p196 reciprocal81 squared with scale60^8', F(value([32,55,18,31,6,40],60),60**8), F(1,81**2))
        root_digits = [1,22,7,42,33,4,38,30,50,15,43]
        root = F(value(root_digits,60),60**10)
        def polynomial(x):return x**3+2*x*x+10*x-20
        assert polynomial(root) < 0 < polynomial(root+F(1,60**10))
        records.append({'label':'p197 unique real root (strictly increasing polynomial)', 'lower':str(root),'upper':str(root+F(1,60**10))})
        equal('p198 Turkish multiplication',F(1535,10)*F(1625,100),F(2494375,1000))
        equal('p200 binary314',value([int(c) for c in '100111010'],2),314)
        equal('p203 tens complement',10**10-1234567890,8765432110)
        equal('p203 nines complement',10**10-1-1234567890,8765432109)
        equal('p204 positive negadecimal',value([int(c) for c in '19375573910'],-10),1234567890)
        equal('p204 negative negadecimal',value([int(c) for c in '2846648290'],-10),-1234567890)
        for word, expected in [('T11TT',-49),('10T',8),('TT10',-33)]:
            equal('balanced '+word,value([-1 if c=='T' else int(c) for c in word],3),expected)
        equal('answer2 binary -49',-value([1,1,0,0,0,1],2),-49)
        equal('answer2 binary -22/7',-periodic([1,1],[0,0,1],2),F(-22,7))
        equal('answer2 negabinary -49',value([int(c) for c in '11010011'],-2),-49)
        equal('answer2 negabinary -22/7',periodic([1,1,0,1],[0,0,1,0,1,1],-2),F(-22,7))
        equal('answer2 balanced -22/7',periodic([-1,0],[0,-1,-1,0,1,1],3),F(-22,7))
        equal('answer2 reciprocal-base -49',-(F(9)+4/F(1,10)),-49)
        equal('answer2 reversed decimal cycle',-periodic([3],[1,4,2,8,5,7],10),F(-22,7))
        equal('p207 ordinary ternary 208.3',periodic([2,1,2,0,1],[0,2,2,0],3),F(2083,10))
        equal('p207 balanced ternary 208.3',periodic([1,0,-1,-1,0,1],[1,0,-1,0],3),F(2083,10))
        equal('answer13 first ambiguity',periodic([1],[9,0],-10),F(1,11))
        equal('answer13 second ambiguity',periodic([0],[0,9],-10),F(1,11))
        equal('p207 positive table fraction',F(value([1,1,-1,0,-1,-1],3),9),F(293,9))
        equal('p207 negative table fraction',F(value([-1,-1,1,0,1,1],3),9),F(-293,9))
        for octal, expected in zip(['12','5655','2550276','76545336','3726755'],['A','BAD','AD0BE','FACADE','FADED']):
            equal('answer9 '+octal,format(int(octal,8),'X'),expected)
        pi_lo, pi_hi = pi_bounds()
        for label, integer, fraction, base, balanced in [
            ('answer2 binary pi','11','00100100001111110110101',2,False),
            ('answer2 negabinary pi','111','0110010001000000101',-2,False),
            ('answer2 balanced pi','10','011T111T000T011T1101T1111110',3,True),
            ('answer2 reversed decimal pi','3','141592653589793238462643',10,False)]:
            decode=lambda s:[-1 if c=='T' else int(c) for c in s]
            lo, hi = fraction_interval(decode(integer),decode(fraction),base,balanced)
            assert lo < pi_lo < pi_hi < hi, (label, float(lo), float(hi))
            records.append({'label':label,'lower':str(lo),'upper':str(hi)})
        assert abs(2*pi_lo-F(62831853071795865,10**16)) < F(1,10**16)
        assert abs(2*pi_hi-F(62831853071795865,10**16)) < F(1,10**16)
        records.append({'label':'p198 2pi accurate to16 decimal places','absolute_error_bound':'1/10^16'})
        save('printed_numbers',{'checks':len(records),'records':records,'pi_certificate':'Machin identity; alternating rational arctangent bounds'})
    if 'complements_and_scaling' not in data:
        shifts = additions = scaling = 0
        for base in (2, 10):
            for length in range(1, 5):
                m = base**length
                values = range(-m//2, m//2)
                for x in values:
                    encoded = x % m
                    lead = (base-1)*base**(length-1) if x < 0 else 0
                    shifted = encoded//base+lead
                    decoded = shifted if shifted < m//2 else shifted-m
                    assert decoded == x//base
                    shifts += 1
                # Entire small tables, targeted boundaries for larger words.
                selected = list(values) if m <= 100 else [-m//2,-m//2+1,-1,0,1,m//2-2,m//2-1]
                for x,y in product(selected,repeat=2):
                    encoded_sum = (x % m + y % m) % m
                    assert encoded_sum == (x+y) % m
                    additions += 1
        for base in (64,100):
            m=base**5
            for a,b in product((0,1,base-1,base,base**2+1,m//2,m-1),repeat=2):
                hi,lo=divmod(a*b,m)
                assert F(a,base**2)*F(b,base**3) == hi+F(lo,m)
                if b:
                    q,r=divmod(a,b)
                    assert F(a,base**2) == (q*base)*F(b,base**3)+F(r,base**2)
                scaling+=1
        save('complements_and_scaling',{'signed_shifts':shifts,'modular_additions':additions,'MIX_radix_point_cases':scaling})

    if 'negative_and_balanced' not in data:
        conversions=additions=0
        for base in range(2,17):
            for n in range(-512,513):
                digits=expand(n,-base)
                assert value(digits,-base)==n
                assert all(0<=d<base for d in digits)
                conversions+=1
        for length in range(1,8):
            words=list(product((0,1),repeat=length))
            for a,b in product(words,repeat=2):
                for sign in (1,-1):
                    c=add_negative(a,b,sign)
                    assert value(c,-2)==value(a,-2)+sign*value(b,-2)
                    assert len(c)==length+2
                    additions+=1
        # Convert by separating odd/even powers, as in answer12, independently
        # of the repeated-division converter used above.
        bit_conversions=0
        for n in range(2048):
            ordinary=[int(c) for c in bin(n)[2:]]
            a=list(reversed(ordinary))
            even=sum(d*2**i for i,d in enumerate(a) if i%2==0)
            odd=sum(d*2**i for i,d in enumerate(a) if i%2==1)
            assert even+odd==n
            for sign in (-1,1):
                out=add_negative(expand(sign*even,-2),expand(-sign*odd,-2),-1)
                assert value(out,-2)==sign*n
                assert len(expand(sign*n,-2))<=len(ordinary)+2
                bit_conversions+=1
            assert value(ordinary,-2)==even-odd
        table=['T0','T1','T','T1','T','0','T','0','1',
               'T1','T','0','T','0','1','0','1','1T',
               'T','0','1','0','1','1T','1','1T','10']
        for inputs,out in zip(product((-1,0,1),repeat=3),table):
            assert sum(inputs)==value([-1 if c=='T' else int(c) for c in out],3)
        balanced_count=0
        for n in range(-2048,2049):
            digits=expand(n,3,True)
            assert value(digits,3)==n
            assert all(d in (-1,0,1) for d in digits)
            assert n==0 or (digits[0]>0)==(n>0)
            balanced_count+=1
        partials=[-17,-17*9,17*27]
        assert sum(partials)==289==value([0,1,1,-1,-1,0,1],3)
        save('negative_and_balanced',{'negative_conversions':conversions,'complete_add_sub_pairs':additions,
                                     'bit_separation_conversions':bit_conversions,'balanced_conversions':balanced_count,
                                     'printed_ternary_addition_columns':27,'p208_corrected_partial_products':partials,
                                     'errata_applied':['p210 exercise12 output n+2 (1999)','p208 redundant zero (2000)']})

    if 'quater_imaginary' not in data:
        count=0
        words=list(product(range(4),repeat=3))
        for a,b in product(words,repeat=2):
            got=quater_product(a,b)
            assert complex_value(got)==cmul(complex_value(a),complex_value(b))
            count+=1
        examples=[]
        for word,product_word,expected,partials in [
            ('12231','021333121',(9,-10),['12231','10320213','13022','13022','12231']),
            ('11321','010311201',(5,-4),['11321','11202','12123','11321','11321'])]:
            digits=[int(c) for c in word]
            assert complex_value(digits)==expected
            assert complex_value([int(c) for c in product_word])==cmul(expected,expected)
            for d,row in zip(reversed(digits),partials):
                assert complex_value([int(c) for c in row])==cmul((d,0),expected)
            assert complex_value(quater_product(digits,digits))==cmul(expected,expected)
            examples.append({'word':word,'value':list(expected),'square':product_word,'all_partial_products_checked':True})
        # Fractional locations are handled by exact rational scaling.
        assert complex_value([1,0,1,0,1,1,3])==(-49,2)
        answer3=cadd(complex_value([1,0,1,0,1,1,3]),(0,-1))
        assert answer3==(-49,1)
        v=complex_value([1,1,2,1,0,3,1])
        assert (F(v[0],-4),F(v[1],-4))==(F(31,4),F(-15,2))
        save('quater_imaginary',{'complete_three_digit_products':count,'printed_squares':examples,
                                'answer3':list(answer3),'fundamental_rectangle':['-4/5','1/5','-8/5','2/5']})

    if 'mixed_and_factorial' not in data:
        count=0
        for trial in range(400):
            digits={j:((trial+3)*(j+8)%11)-5 for j in range(-6,7)}
            radices={j:(-1 if (trial+j)%3==0 else 1)*(2+(trial+2*j)%7) for j in range(-6,7)}
            cuts={-2:-6,-1:-2,0:0,1:1,2:4,3:7}
            grouped={};group_bases={}
            for j in range(-2,3):
                start,end=cuts[j],cuts[j+1]
                group_bases[j]=math.prod(radices[k] for k in range(start,end))
                acc=0
                for k in range(end-1,start-1,-1):
                    if k==end-1:acc=digits[k]
                    else:acc=acc*radices[k]+digits[k]
                grouped[j]=acc
            assert mixed_value(digits,radices)==mixed_value(grouped,group_bases)
            count+=1
        factorial_count=0
        for n in range(10001):
            x=n; k=1; terms=[]
            while x:
                x,d=divmod(x,k+1)
                terms.append(d)
                k+=1
            assert sum(d*math.factorial(j+1) for j,d in enumerate(terms))==n
            assert all(0<=d<=j+1 for j,d in enumerate(terms))
            factorial_count+=1
        time=F(3*7*24*3600+2*24*3600+9*3600+22*60+57)+F(492,1000)
        assert mixed_value({4:3,3:2,2:9,1:22,0:57,-1:492},{3:7,2:24,1:60,0:60,-1:1000})==time
        assert mixed_value({2:10,1:6,0:3,-1:1},{1:20,0:12,-1:2})==F(4951,2)
        save('mixed_and_factorial',{'mixed_groupings':count,'factorial_integers':factorial_count,'p209_seconds':str(time),'p209_pence':'4951/2'})

    if 'minimal_signed_and_reversing' not in data:
        words=0;best={}
        for ds in product((-1,0,1),repeat=10):
            n=value(ds,2);w=sum(d!=0 for d in ds);canonical=naf(n)
            assert value(canonical,2)==n
            assert all(not(a and b) for a,b in zip(canonical,canonical[1:]))
            assert sum(d!=0 for d in canonical)<=w
            best[n]=min(best.get(n,11),w)
            words+=1
        for n,w in best.items():
            canonical=naf(n)
            if len(canonical)<=10:assert sum(d!=0 for d in canonical)==w
        for n in range(65536):
            w=sum(d!=0 for d in naf(n))
            assert w==pattern_weight(n)==((3*n)^n).bit_count()
        rev=0
        for n in range(-2048,2049):
            es=reversing(n)
            assert sum((-1)**j*2**e for j,e in enumerate(es))==n
            assert all(x<y for x,y in zip(es,es[1:]))
            rev+=1
        save('minimal_signed_and_reversing',{'all_ten_digit_signed_words':words,'pattern_formula_cases':65536,
                                           'reversing_integers':rev,'proof_scope':'General optimality and the pattern automaton are proved separately in the note.'})

if __name__=='__main__':
    main()
