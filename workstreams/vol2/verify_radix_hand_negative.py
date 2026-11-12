#!/usr/bin/env python3
"""Exact checks of 4.4C, exercises6,11,12, including published replacements."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse, json, random, time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/radix-hand-negative.json'


def fmt(n,b):
    if n==0:return '0'
    ds=[]
    while n:n,r=divmod(n,b);ds.append(str(r))
    return ''.join(ds[::-1])


def hand(text,b,B):
    digits=list(map(int,text));v=digits[0]
    prefixes=[text[0]];corrections=[]
    for d in digits[1:]:
        correction=(b-B)*v
        corrections.append(('-' if correction<0 else '+')+fmt(abs(correction),B))
        v=B*v+d+correction
        prefixes.append(fmt(v,B))
    assert v==int(text,b)
    return {'prefixes':prefixes,'corrections':corrections,'value':v}


def manual_block():
    examples={}
    rows=[('original_octal','5325121',8,10,['5','43','346','2773','22185','177482','1419857']),
          ('replacement_octal','1234567',8,10,['1','10','83','668','5349','42798','342391']),
          ('original_decimal','1419857',10,8,['1','16','215','2613','33566','425241','5325121']),
          ('replacement_decimal','342391',10,8,['3','42','526','6537','102677','1234567']),
          ('exercise11_original','57721',8,10,['5','47','383','3066','24529']),
          ('exercise11_new','21446',8,10,['2','17','140','1124','8998']),
          ('exercise11_back','8998',10,8,['8','131','1603','21446']),
          ('exercise12','1764723',9,10,['1','16','150','1354','12193','109739','987654']),
          ('exercise12_back','987654',10,9,['9','118','1316','14483','160428','1764723'])]
    for name,text,b,B,expected in rows:
        got=hand(text,b,B);assert got['prefixes']==expected,(name,got)
        examples[name]=got
    assert int('1212011210210',3)==int('1764723',9)==987654
    # Every printed intermediate fraction, not only final truncated outputs.
    t=14159;den=100000;remainders=[];digits=[];doubles=[]
    for _ in range(6):
        doubles.append(str(2*t));q,t=divmod(10*t-2*t,den)
        digits.append(q);remainders.append(f'{t:05d}')
    assert digits==[1,1,0,3,7,4]
    assert remainders==['13272','06176','49408','95264','62112','96896']
    assert doubles==['28318','26544','12352','98816','190528','124224']
    t=int('110374',8);den=8**6;remainders2=[];digits2=[];doubles2=[]
    for _ in range(6):
        doubles2.append(fmt(2*t,8));q,t=divmod(8*t+2*t,den)
        digits2.append(q);remainders2.append(fmt(t,8).zfill(6))
    assert digits2==[1,4,1,5,8,6]
    assert remainders2==['324730','121160','454140','671700','502600','233400']
    assert doubles2==['220770','651660','242340','1130300','1563600','1205400']
    checksum=0
    for n in range(10000):
        dec=sum(map(int,str(n)));octal=fmt(n,8)
        alt=sum((-1)**j*int(d) for j,d in enumerate(octal[::-1]))
        assert (dec-alt)%9==0;checksum+=1
    # Replaced text's explicit intermediate check.
    assert (6+6+8-(4-3+2-1))%9==0
    return {'integer_examples':examples,'fraction3_digits':digits,
            'fraction3_remainders':remainders,'fraction4_digits':digits2,
            'fraction4_remainders':remainders2,'checksum_cases':checksum}


def negencode(u):
    if u==0:return [0]
    ds=[]
    while u:
        r=u%2;u=(u-r)//(-2);ds.append(r)
        assert len(ds)<10000
    return ds


def negvalue(ds):return sum(d*(-2)**j for j,d in enumerate(ds))


def negmuladd(ds,m,a):
    carry=a;out=[]
    for d in ds:
        t=m*d+carry;r=t%2;carry=(t-r)//(-2);out.append(r)
    while carry:
        r=carry%2;carry=(carry-r)//(-2);out.append(r)
    while len(out)>1 and out[-1]==0:out.pop()
    return out


def fracdigits(u,M):
    assert F(-2,3)<=u<=F(1,3)
    ds=[];r=u
    for _ in range(M):
        d=int(r<F(-1,6));r=-2*r-d;ds.append(d)
        assert F(-2,3)<=r<=F(1,3)
        value=sum((F(d,(-2)**j) for j,d in enumerate(ds,1)),F(0))
        assert u==value+F(r,(-2)**len(ds))
    return ds,r


def negative_block():
    integer_cases=0
    for u in range(-10000,10001):
        ds=negencode(u)
        assert all(d in [0,1] for d in ds) and negvalue(ds)==u
        if len(ds)>1:assert ds[-1]==1
        integer_cases+=1
    rng=random.Random(4406);horner=0
    for b in [-2,2,3,8,10,16,36]:
        for _ in range(300):
            ds=[rng.randrange(abs(b)) for _ in range(rng.randrange(1,35))]
            out=[0];v=0
            for d in ds:
                out=negmuladd(out,b,d);v=b*v+d
                assert negvalue(out)==v
            assert out==negencode(v);horner+=1
    fractions=0
    for m in range(13):
        for ds in product([0,1],repeat=m):
            u=sum((F(d,(-2)**j) for j,d in enumerate(ds,1)),F(0))
            got,r=fracdigits(u,m)
            assert got==list(ds) and r==0
            x=F(0)
            for d in reversed(ds):x=(x+d)/(-2)
            assert x==u
            fractions+=1
    endpoints={}
    for u in [F(-2,3),F(-1,6),F(1,3)]:
        ds,r=fracdigits(u,16);endpoints[str(u)]={'digits':ds,'remainder':str(r)}
    rounding=0;general=0
    for den in range(1,32):
        for num in range(-3*den,3*den+1):
            u=F(num,den)
            # Choose an integer part making a legitimate negabinary fraction.
            z=u-F(1,3);a=-((-z.numerator)//z.denominator)
            assert F(-2,3)<u-a<=F(1,3)
            ds,r=fracdigits(u-a,12)
            prefix=a+sum((F(d,(-2)**j) for j,d in enumerate(ds,1)),F(0))
            assert abs(prefix-u)<=F(2,3*2**12);general+=1
            for M in [0,1,2,5,10]:
                scaled=u*2**M+F(1,2);k=scaled.numerator//scaled.denominator
                ds=negencode((-1)**M*k)
                v=F(negvalue(ds),(-2)**M)
                assert abs(v-u)<=F(1,2**(M+1))
                assert abs(v-u)<=abs(v+F(1,2**M)-u)
                assert abs(v-u)<=abs(v-F(1,2**M)-u)
                rounding+=1
    return {'signed_integer_cases':integer_cases,'horner_cases':horner,
            'finite_fraction_words':fractions,'endpoint_examples':endpoints,
            'general_rational_cases':general,'rounded_cases':rounding}


BLOCKS={'manual':manual_block,'negative':negative_block}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--resume',action='store_true');args=parser.parse_args()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'scope':'4.4C,6,11,12','blocks':{}}
    for name,fun in BLOCKS.items():
        if name in data['blocks']:continue
        t=time.monotonic();result=fun();data['blocks'][name]={'status':'passed','seconds':time.monotonic()-t,'result':result}
        OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'checkpoint':name,**data['blocks'][name]},ensure_ascii=False),flush=True)

if __name__=='__main__':main()
