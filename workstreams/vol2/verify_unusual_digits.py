"""Exact finite certificates for section 4.1 exercises19–24.

General existence, uniqueness, density and measure arguments are in the note.
Successful blocks are checkpointed and skipped on continuation.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from math import ceil, floor, gcd
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/unusual-digits.json'


def value(ds,b):
    v=0
    for d in ds:v=b*v+d
    return v


def expansion(m,b,D):
    by_residue={d%b:d for d in D}
    assert len(by_residue)==b
    original=m;ds=[];seen=set()
    while m or not ds:
        if m in seen:return None
        seen.add(m);d=by_residue[m%b];ds.append(d);m=(m-d)//b
        if m==0:break
    ds.reverse()
    assert value(ds,b)==original
    return ds


def critical(b,D):return range(ceil(F(-max(D),b-1)),floor(F(-min(D),b-1))+1)


def main():
    data=json.loads(OUT.read_text()) if OUT.exists() else {}
    def save(k,v):
        data[k]=v;OUT.write_text(json.dumps(data,indent=2)+'\n');print('PASS',k,flush=True)
    if 'basic_digit_sets' not in data:
        table=[];long_cases=0;long_sets=0
        for b in range(2,13):
            passing=[]
            for choices in product((0,1),repeat=b-1):
                D=[0]+[r-b*choices[r-1] for r in range(1,b)]
                ok=all(expansion(m,b,D) is not None for m in critical(b,D))
                expect=(b>=3 and 1 in D and -1 in D)
                assert ok==expect,(b,D)
                if ok:passing.append(D)
            count=0 if b==2 else 2**(b-3)
            assert len(passing)==count
            table.append({'base':b,'all_residue_sets':2**(b-1),'valid_sets':count})
        for b in range(3,8):
            for n in range(1,5):
                for bits in product((0,1),repeat=b-3):
                    D=[0,1]+[r-e*b**n for r,e in zip(range(2,b-1),bits)]+[b-1-b**n]
                    long_sets+=1
                    for m in range(b**n):
                        ds=expansion(m,b,D);assert ds is not None and len(ds)<=2*n,(b,n,D,m)
                        long_cases+=1
        # General residue representatives, including examples without digit zero.
        general_sets=general_cases=invalid_sets=0
        for b in range(2,6):
            for offsets in product((-1,0,1),repeat=b):
                D=[r+b*h for r,h in enumerate(offsets)];general_sets+=1
                good=all(expansion(m,b,D) is not None for m in critical(b,D))
                if good:
                    for m in range(-50,51):
                        assert expansion(m,b,D) is not None
                        general_cases+=1
                else:invalid_sets+=1
        assert value([-3,7,7,-3],3)==0
        save('basic_digit_sets',{'bounded_digit_census':table,'long_family_sets':long_sets,
             'long_family_all_states':long_cases,'long_family_proved_bound':'at most2n digits for0<=m<b^n',
             'general_sets':general_sets,'invalid_general_sets':invalid_sets,'valid_general_integer_cases':general_cases,
             'nonzero_digit_zero_word':[-3,7,7,-3]})
    if 'decimal_multiplicity' not in data:
        D=[-1,0]+[8+9*j for j in range(8)]
        assert len(D)==10 and len({a%10 for a in D})==10
        paths={str(m):expansion(m,10,D) for m in critical(10,D)}
        assert all(v is not None for v in paths.values())
        nine=[]
        for j in range(9):
            prefix=expansion(-j,10,D);tail=9*j-1
            assert tail in D and value(prefix,10)+F(tail,9)==F(-1,9)
            nine.append({'prefix':prefix,'repeated_tail_digit':tail})
        comparisons=0;distinct=set()
        # Periodic rational members of the Cantor family; general cardinality is proved separately.
        for bits in product((0,1),repeat=10):
            word=[-1 if b==0 else 8 for b in bits]
            x=F(value(word,10),10**len(word)-1);distinct.add(x)
            for j in range(8):
                shifted=[a+9*j for a in word]
                assert all(a in D for a in shifted)
                assert -j+F(value(shifted,10),10**len(word)-1)==x
                comparisons+=1
        assert len(distinct)==2**10
        save('decimal_multiplicity',{'digits':D,'critical_integer_expansions':paths,
             'nine_expansions_of_minus_one_ninth':nine,'periodic_comparisons':comparisons,
             'distinct_periodic_examples':len(distinct),'fraction_interval':['-1/9','71/9'],
             'scope':'The at-most9 bound and uncountability use the general prefix/separation proofs.'})
    if 'half_integer_digits' not in data:
        zero=unit=0;rows=[]
        for n in range(-8,9):
            scale=F(10)**n
            for sign in (-1,1):
                assert sign*F(1,2)*scale-sign*F(9,2)*scale/9==0;zero+=1
        for n in range(9):
            for end,tail in [(F(3,2),F(-9,2)),(F(1,2),F(9,2))] if n==0 else [(F(-7,2),F(-9,2)),(F(-9,2),F(9,2))]:
                prefix=[end] if n==0 else [F(1,2)]+[F(-9,2)]*(n-1)+[end]
                assert value(prefix,10)+tail/9==1;unit+=1
                rows.append({'top_exponent':n,'digits':[str(a) for a in prefix],'tail':str(tail)})
        # At fixed top exponent n: subtracting9/2 from each ordinary digit translates by5*10^n.
        affine=0
        for length in range(1,5):
            for word in product(range(10),repeat=length):
                balanced=[F(a)-F(9,2) for a in word]
                # Complete the ordinary fraction by zeroes, hence the balanced fraction by-9/2.
                assert value(balanced,10)-F(1,2)==value(word,10)-5*10**(length-1)
                affine+=1
        save('half_integer_digits',{'zero_expansions':zero,'unit_expansions':unit,
             'unit_rows':rows,'finite_affine_checks':affine,
             'scope':'All representations follow from the ordinary decimal classification at each fixed top exponent.'})
    if 'sparse_constant_cancellation' not in data:
        rows=[]
        for old_n in range(6):
            for t in range(1,7):
                j=max(2,(old_n+t+1)//2+1)
                m=j*j-t
                while m<=old_n or 2*j-1-t<=old_n:j+=1;m=j*j-t
                positions=[m-r*r for r in range(1,j)]
                assert all(old_n<k<m for k in positions)
                assert len(set(positions))==len(positions)
                # Bound alpha by its first j+4 terms plus a geometric upper bound on the rest.
                J=j+4
                alpha_hi=-sum((F(10)**(-r*r) for r in range(1,J+1)),F(0))
                alpha_lo=alpha_hi-F(10)**(-(J+1)**2)*F(10,9)
                A=sum(10**k for k in positions);B=10**m
                lo,hi=A+B*alpha_lo,A+B*alpha_hi
                delta=F(10)**(-t)
                tail_bound=F(10)**(-t-2*j-1)*F(10,9)
                assert -delta-tail_bound<lo<=hi<-delta
                assert tail_bound<delta
                rows.append({'old_top':old_n,'target_negative_exponent':t,'chosen_square_index':j,
                             'new_top':m,'cancellation_positions':positions,'reduction_interval':[str(-hi),str(-lo)]})
        save('sparse_constant_cancellation',{'cases':len(rows),'rows':rows,
             'scope':'Exact single-step interval certificates. The potentially enormous full density construction is proved, not materialized.'})
    if 'nonnegative_families' not in data:
        cases=0;rows=[]
        for family in (0,1):
            for k in range(5):
                D=sorted({2*a*10**k+c if family==0 else 5*c*10**k+a for a in range(5) for c in range(2)})
                assert len(D)==10 and 0 in D and gcd(*D)==1
                rows.append({'family':family,'k':k,'digits':D})
                for numerator in range(1000):
                    ds={j-2:int(c) for j,c in enumerate(reversed(str(numerator)))}
                    shifted={}
                    for pos,d in ds.items():
                        if family==0:
                            a,c=divmod(d,2)
                            shifted[pos-k]=shifted.get(pos-k,0)+2*a*10**k
                            shifted[pos]=shifted.get(pos,0)+c
                        else:
                            c,a=divmod(d,5)
                            shifted[pos-k]=shifted.get(pos-k,0)+5*c*10**k
                            shifted[pos]=shifted.get(pos,0)+a
                    assert all(d in D for d in shifted.values())
                    got=sum((d*F(10)**pos for pos,d in shifted.items()),F(0))
                    assert got==F(numerator,100);cases+=1
        save('nonnegative_families',{'digit_sets':rows,'shifted_finite_examples':cases,
             'scope':'Verifies the two displayed families, not the advanced necessity/classification assertion.'})


    if 'nonzero_digit_counterexample' not in data:
        def merge(intervals):
            out=[]
            for a,b in sorted(intervals):
                if out and a<=out[-1][1]:out[-1]=(out[-1][0],max(b,out[-1][1]))
                else:out.append((a,b))
            return out
        rows=[]
        for h in (0,1,2):
            D=[a+h+50*c for a in range(5) for c in (0,1)]
            S=[(F(h,9),1+F(h,9)),(5+F(h,9),6+F(h,9))]
            image=merge([((a+d)/10,(b+d)/10) for d in D for a,b in S])
            assert image==S
            rows.append({'translation':h,'digits':sorted(D),'exact_fraction_set':[[str(a),str(b)] for a,b in S]})
        target=F(3,2)
        assert target < 2 # Any leading exponent n>=0, even if omitted zero tails are allowed.
        assert target > F(56,90) # Every n<=-2.
        assert F(6,10)+F(56,90)==F(11,9)<target<F(52,10) # n=-1, two leading-digit groups.
        # Independently, the exact two-interval fractional set excludes the target.
        assert not any(a<=target<=b for a,b in S)
        Dneg=[-1]+list(range(8))+[18]
        for m in range(2001):assert expansion(m,10,Dneg) is not None
        assert expansion(-2,10,Dneg) is None
        save('nonzero_digit_counterexample',{'target':'3/2','fixed_set_checks':rows,
             'leading_exponent_cases':{'n>=0':'x>=2','n<=-2':'x<=28/45','n=-1':'x<=11/9 or x>=26/5'},
             'negative_digit_context_positive_checks':2001,'negative_digit_context_finite_integer_failure':-2,
             'scope':'C0079: the translated-by2 nonnegative set fails even when finite tails of implicit zeroes are allowed.'})

if __name__=='__main__':main()
