"""Independent nearest-neighbor checks and exact exercise calculations, 4.2.1.

Completed blocks are checkpointed; a later invocation skips them automatically.
"""
import bisect
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
from float_model import power, value, normalize, add, multiply, divide, round_integer

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/single-precision.json'


def oracle_table(b,p):
    out=[]
    for e in range(-14,15):
        for f in range(b**(p-1),b**p):
            for sign in [-1,1]:
                u=(e,sign*f);out.append((value(u,b,p),u))
    out.append((Q(0),(0,0)));out.sort()
    return [a for a,u in out], [u for a,u in out]


def oracle(x,b,p,table,mode='nearest'):
    vs,us=table;j=bisect.bisect_left(vs,x)
    assert 0<j<len(vs)-1 or x==vs[j]
    if vs[j]==x:return us[j]
    if mode=='down':return us[j-1]
    if mode=='up':return us[j]
    dl,dr=x-vs[j-1],vs[j]-x
    if dl<dr:return us[j-1]
    if dr<dl:return us[j]
    if b%2:return us[j] if x>0 else us[j-1]
    e=min(us[j-1][0],us[j][0]);unit=power(b,e-p)
    assert (vs[j]/unit).denominator==1
    return us[j] if (int(vs[j]/unit)+b//2)%2 else us[j-1]


def algorithms():
    cases=directed=0;by=[]
    for b,p in [(b,p) for b in range(2,7) for p in [1,2]]+[(2,3)]:
        tab=oracle_table(b,p)
        inputs=[(0,0)]+[(e,s*f) for e in [-1,0,1] for f in range(b**(p-1),b**p) for s in [-1,1]]
        ct=0
        for u,v in product(inputs,repeat=2):
            x,y=value(u,b,p),value(v,b,p)
            for fn,exact in [(add,x+y),(multiply,x*y)]+([(divide,x/y)] if y else []):
                got,tr=fn(u,v,b,p)
                assert got==oracle(exact,b,p,tab),(b,p,u,v,fn.__name__,got,oracle(exact,b,p,tab))
                if fn is divide: assert not tr['rounding_overflow']
                ct+=1
            for mode in ['down','up']:
                got,_=add(u,v,b,p,mode=mode)
                assert got==oracle(x+y,b,p,tab,mode)
                directed+=1
        cases+=ct;by.append(dict(radix=b,precision=p,inputs=len(inputs),operations=ct))
    return dict(operations=cases,directed_additions=directed,formats=by,
                method='Algorithms A/N/M versus independently enumerated neighboring representable values; directed A disables its small-addend shortcut.')


def equivalence(x,y,b):
    def cls(z):
        k=z//b;r=z-k*b
        return k, (0 if r==0 else 1 if 2*r<b else 2 if 2*r==b else 3)
    return cls(x)==cls(y)


def compress(x,b):
    k=x//b;r=x-k*b
    r1=Q(0) if r==0 else Q(b,4) if 2*r<b else Q(b,2) if 2*r==b else Q(3*b,4)
    return k*b+r1


def guard_digits():
    ct=identities=0
    for b in range(2,10):
        for i in range(-8*b,8*b+1):
            x=Q(i,4);y=compress(x,b)
            assert equivalence(x,y,b)
            assert equivalence(x/b,y/b,b)
            assert equivalence(x+7*b,y+7*b,b)
            if equivalence(b*x,b*y,b):assert round_integer(x,b)==round_integer(y,b)
            identities+=1
        for p in [1,2,3]:
            fs=range(b**(p-1),b**p) if p<3 else sorted({b**2,b**2+1,b**3//2,b**3-2,b**3-1})
            for fu,fv,s,d in product(fs,fs,[-1,1],range(p+2)):
                f=Q(s*fv,b**(p+d));c=compress(f*b**(p+2),b)/b**(p+2)
                assert equivalence(f*b**(p+2),c*b**(p+2),b)
                a,_=normalize(0,Q(fu,b**p)+f,b,p)
                z,_=normalize(0,Q(fu,b**p)+c,b,p)
                assert a==z,(b,p,fu,fv,s,d,f,c,a,z)
                ct+=1
    return dict(relation_checks=identities,compressed_additions=ct,
                known_erratum='Answer5 requires bx~by for equality after integer rounding.')


def printed_examples():
    out={};b=10;p=8
    tests=[((50,98765432),(49,33333333),(51,10209877)),
           ((53,-99987654),(54,10000000),(50,12346000)),
           ((45,-50000001),(54,10000000),(53,99999999)),
           ((45,-50000000),(54,10000000),(54,10000000))]
    for u,v,w in tests:assert add(u,v,b,p)[0]==w
    out['exercise4']=[list(x[2]) for x in tests]
    tests8=[((6,12345679),(6,-12345678),-1),((1,10345678),(0,-94000000),-1),
            ((99,87654321),(99,87654321),100),((99,99999999),(91,50000000),100)]
    for u,v,e in tests8:assert add(u,v,b,p)[0][0]==e
    out['exercise8_exponents']=[x[2] for x in tests8]
    for name,fn,u,v in [('addition',add,(50,99999000),(55,99999000)),
                        ('multiplication',multiply,(50,10000001),(50,99999990))]:
        w,tr=fn(u,v,b,p,50);assert tr['rounding_overflow'];out['overflow_'+name]=dict(result=w,trace=tr)
    # Underflow-to-zero model of exercise9; equality of the denominators is exact.
    a=(-50,10000000);c=a;bb=(-41,20000000);d=(-41,80000000);y=(11,10000000)
    def op(fn,u,v):
        w,_=fn(u,v,b,p)
        return (-50,0) if not w[1] or w[0]<-50 else w
    first=op(divide,op(add,op(multiply,a,y),bb),op(add,op(multiply,c,y),d))
    second=op(divide,op(add,a,op(divide,bb,y)),op(add,c,op(divide,d,y)))
    assert value(first,b,p)==Q(66666667,10**8)
    assert value(second,b,p)==1
    out['exercise9']={'first':str(value(first,b,p)),'second':str(value(second,b,p))}
    # Source(3), as requested in exercise1, already rounds the SI constants.
    for e,f,ee,ff in [(74,60225200,62,60225200),(24,66256000,37,66256000),
                     (74,60221408,62,60221408),(17,66260702,34,6626070)]:
        x=value((e,f),10,8,50)
        ans,_=normalize(ee,x/power(100,ee-50),100,4)
        assert ans==(ee,ff)
    out['exercise1_note']='2020 answer converts the already rounded decimal values of (3). Direct rounding of exact10h in base100 would instead give66260701 at the tie; this is not classified as a book error.'
    # Range endpoints (exercise2) checked by independent enumeration.
    ranges=0
    for bb,pp,E,q in product(range(2,6),[1,2],[0,1,2],[-1,0,2]):
        vs=[value((e,f),bb,pp,q) for e in range(E+1) for f in range(1,bb**pp)]
        ns=[value((e,f),bb,pp,q) for e in range(E+1) for f in range(bb**(pp-1),bb**pp)]
        assert (max(vs),min(vs),max(ns),min(ns))==(power(bb,E-q)*(1-power(bb,-pp)),power(bb,-q-pp),power(bb,E-q)*(1-power(bb,-pp)),power(bb,-q-1))
        ranges+=1
    out['range_cases']=ranges
    return out


def twos_complement():
    # Direct signed fractions; field zero after rounding encodes -1, not real0.
    def neg_normalize(e,f,p):
        assert -1<=f<0
        while f>=Q(-1,2):f*=2;e+=1
        k=round_integer(f*2**p,2)
        if k==-2**p:k//=2;e-=1
        return e,k%2**p
    out=[]
    for tail,expected in [('01',(int('575',8),int('400000000',8))),
                          ('05',(int('576',8),1))]:
        field=int('740000000'+tail,8); f=Q(field,2**33)-1
        got=neg_normalize(int('572',8),f,27);assert got==expected
        # Independent ordinary magnitude normalization.
        x=f*power(2,511-int('572',8)-128)
        w,_=normalize(0,x,2,27)
        mag=value(w,2,27)
        encoded=(511-(w[0]+128), (w[1]+2**27)%2**27)
        assert got==encoded
        out.append(dict(input='572|740000000|'+tail,output=[oct(z) for z in got],value=str(mag)))
    ct=0
    for p in range(2,9):
        for k in range(1,2**(p+3)):
            f=-Q(k,2**(p+3));ec,field=neg_normalize(384,f,p)
            exact=f*power(2,511-384-128)
            w,_=normalize(-1,f,2,p)
            assert (ec,field)==(511-(w[0]+128),(w[1]+2**p)%2**p)
            assert value(w,2,p)!=0
            ct+=1
    return dict(printed=out,negative_normalizations=ct)


def balanced_and_auxiliary():
    # Balanced ternary: fixed-place rounding and nearest floating value differ.
    def norm(e,f,p):
        if f==0:return (0,0)
        while abs(f)>=Q(1,2):f/=3;e+=1
        while abs(f)<Q(1,6):f*=3;e-=1
        return e,round_integer(f*3**p,3)
    u=(0,2);v=(-2,-4);x=value(u,3,2)+value(v,3,2)
    assert x==Q(14,81)
    got=norm(0,x,2);assert got==(0,2)
    alternatives=sorted({value((e,k),3,2) for e in range(-5,3) for k in [2,3,4]})
    best=min(alternatives,key=lambda z:abs(z-x))
    assert best==Q(4,27) and abs(best-x)==Q(2,81)
    assert abs(value(got,3,2)-x)==Q(4,81)
    # For a fixed radix position, all finite balanced tails are <half an ulp.
    ct=0
    for p in range(1,6):
        for k in range(-(3**(p+3)-1)//2,(3**(p+3)-1)//2+1):
            quotient=(k+(3**3-1)//2)//3**3
            remainder=k-quotient*3**3
            assert abs(remainder)<Q(3**3,2)
            assert round_integer(Q(k,3**3),3)==quotient
            ct+=1
    # Smith's two branches, independently checked by cross multiplication.
    import sympy as S
    a,b,c,d=S.symbols('a b c d', real=True)
    expected=((a*c+b*d)/(c*c+d*d),(b*c-a*d)/(c*c+d*d))
    branches=[((a+b*d/c)/(c+d*d/c),(b-a*d/c)/(c+d*d/c)),
              ((a*c/d+b)/(d+c*c/d),(b*c/d-a)/(d+c*c/d))]
    for branch in branches:
        for got1,want in zip(branch,expected):assert S.cancel(got1-want)==0
    # Gradual underflow: fixed grid below the minimum normal value.
    gradual=0
    for b,p in product(range(2,7),[1,2]):
        grid=power(b,-p);normal=power(b,-1)
        vals={Q(0)}|{value((e,s*f),b,p) for e in range(3) for f in range(1,b**p) for s in [-1,1]}
        for a,c in product(vals,repeat=2):
            z=a+c
            if abs(z)<normal:
                assert (z/grid).denominator==1
                assert z in vals
                gradual+=1
    return dict(balanced_fixed_grid_cases=ct,balanced_boundary=dict(precision=2,u=str(value(u,3,2)),v=str(value(v,3,2)),exact=str(x),normalized_truncation=str(value(got,3,2)),nearest=str(best),error_truncation='4/81',error_nearest='2/81'),smith_symbolic_identities=4,gradual_exact_tiny_sums=gradual)


def tapered():
    # Our explicit16-bit example; not a transcription of Morris's36-bit format.
    lens=[1,2,4,8];words={};values=set();by={}
    for e in range(-128,128):
        j=next(j for j,k in enumerate(lens) if -2**(k-1)<=e<2**(k-1))
        k=lens[j];t=13-k
        for sign,f in product([0,1],range(2**t)):
            word=(sign<<15)|(j<<13)|((e%(2**k))<<t)|f
            decoded_sign=word>>15;dj=(word>>13)&3;dk=lens[dj];dt=13-dk
            de=(word>>dt)&(2**dk-1)
            if de>=2**(dk-1):de-=2**dk
            df=word&(2**dt-1)
            assert (decoded_sign,de,df,dt)==(sign,e,f,t)
            val=(-1 if sign else 1)*(1+Q(f,2**t))*power(2,e)
            assert word not in words and val not in values
            words[word]=(sign,e,f,t);values.add(val);by[k]=by.get(k,0)+1
    zero_word=(1<<13)  # j1,k2,e0,f0; nonminimal exponent width, hence unused.
    assert zero_word not in words
    pos=[x for x in values if x>0]
    assert min(pos)==power(2,-128) and max(pos)==Q(63,32)*power(2,127)
    return dict(canonical_nonzero_words=len(words),zero_word=zero_word,word_counts_by_exponent_bits=by,near_one_significant_bits=13,extreme_significant_bits=6,min_positive=str(min(pos)),max_positive=str(max(pos)),scope='Explicit research-exercise example, with canonical encoding and exact range, not a claim of optimality or a transcription of the1971 article.')


def main():
    data=json.loads(OUT.read_text()) if OUT.exists() else {}
    for name,fn in [('algorithms',algorithms),('guard_digits',guard_digits),('printed_examples',printed_examples),('twos_complement',twos_complement),('balanced_and_auxiliary',balanced_and_auxiliary),('tapered',tapered)]:
        if name in data:continue
        data[name]=fn();OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,'PASS',flush=True)

if __name__=='__main__':main()
