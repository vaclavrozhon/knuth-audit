#!/usr/bin/env python3
"""Exact rational rounding and round-trip certificates for 4.4-17/18."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from bisect import bisect_left
import argparse,json,math,random,time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/radix-round.json'


@lru_cache(None)
def power(B,e):return B**e if e>=0 else F(1,B**(-e))


def floorlog(n,d,B):
    # Floating approximation is only a seed; exact inequalities certify e.
    e=math.floor((n.bit_length()-d.bit_length())*math.log(2,B))
    while F(n,d)<power(B,e):e-=1
    while F(n,d)>=power(B,e+1):e+=1
    assert power(B,e)<=F(n,d)<power(B,e+1)
    return e


def round_fp(x,B,p):
    x=F(x)
    if x==0:return x,0,0,False
    sign=1 if x>0 else -1;x=abs(x);e=floorlog(x.numerator,x.denominator,B)+1
    scaled=x*power(B,p-e);q,r=divmod(scaled.numerator,scaled.denominator)
    tie=2*r==scaled.denominator
    if 2*r>scaled.denominator or (tie and q%2):q+=1
    if q==B**p:q//=B;e+=1
    assert B**(p-1)<=q<B**p
    return sign*q*power(B,e-p),sign*q,e,tie


def neighbours(q,e,B,p):
    # Positive canonical significand q with exponent e.
    v=q*power(B,e-p)
    if q==B**(p-1):lo=(B**p-1)*power(B,e-p-1)
    else:lo=(q-1)*power(B,e-p)
    hi=(q+1)*power(B,e-p)
    return lo,v,hi


def rounding_block():
    rng=random.Random(4417);cases=0;ties=0;boundaries=0
    for B in [2,3,4,5,8,10,16]:
        for p in [1,2,3]:
            grid=sorted({F(q)*power(B,e-p) for e in range(-6,8) for q in range(B**(p-1),B**p)})
            for _ in range(250):
                x=F(rng.randrange(10000,10000*B),10000)*power(B,rng.randrange(-4,5))
                v,q,e,tie=round_fp(x,B,p);j=bisect_left(grid,x)
                assert 0<j<len(grid)
                distance=min(abs(grid[j-1]-x),abs(grid[j]-x))
                assert abs(v-x)==distance
                lo,mid,hi=neighbours(q,e,B,p)
                assert (lo+mid)/2<=x<=(mid+hi)/2
                assert round_fp(-x,B,p)[0]==-v
                cases+=1;ties+=tie
            for e in range(-4,5):
                for q in sorted({B**(p-1),B**(p-1)+1,B**p-2,B**p-1}):
                    if not B**(p-1)<=q<B**p:continue
                    lo,v,hi=neighbours(q,e,B,p)
                    for x in [F(lo+v,2),v,F(v+hi,2)]:
                        z,qq,ee,tie=round_fp(x,B,p)
                        assert min(abs(x-lo),abs(x-v),abs(x-hi))==abs(x-z)
                        if x!=v:assert tie
                        ties+=tie;boundaries+=1
    return {'enumerated_grid_oracles':cases,'boundary_cases':boundaries,'ties':ties}


def roundtrip_block():
    count=0;fails=[]
    for b,B in [(2,10),(10,2),(2,3),(3,2),(4,5),(5,4),(8,10),(10,16)]:
        for p in [1,2,3,4]:
            if b**p>20000:continue
            P=1
            while B**(P-1)<=b**p:P+=1
            for e in range(-5,6):
                for q in range(b**(p-1),b**p):
                    u=q*power(b,e-p);v=round_fp(round_fp(u,B,P)[0],b,p)[0]
                    assert u==v,(b,B,p,P,q,e);count+=1
            # Below-threshold precision is not assumed to fail on every input.
            for e in range(-30,31):
                found=False
                for q in range(b**(p-1),b**p):
                    u=q*power(b,e-p);v=round_fp(round_fp(u,B,P-1)[0],b,p)[0]
                    if u!=v:
                        fails.append({'b':b,'B':B,'p':p,'P':P-1,'q':q,'e':e});found=True;break
                if found:break
    return {'sufficient_roundtrips':count,'below_threshold_examples':fails}


def examples_block():
    u=F(2**6408);v,q,e,t=round_fp(u,10,4);w,a,f,tt=round_fp(v,2,10)
    assert (q,e)==(1000,1930) and v==10**1929
    assert w==2**6408-2**6398 and not t and not tt
    original={'input_binary_exponent':6408,'decimal_significand':q,'decimal_exponent':e,
              'binary_result_significand':a,'binary_result_exponent':f}
    u=F(1017*2**774);v,q,e,t=round_fp(u,10,4);w,a,f,tt=round_fp(v,2,10)
    assert (q,e)==(1011,237) and (a,f)==(1018,784)
    assert not t and not tt and v==1011*10**233 and w==1018*2**774
    # Integer comparisons independently certify both strict midpoint choices.
    assert 2*u>2021*10**233 and 2*u<2023*10**233
    assert 2*v>2035*2**774 and 2*v<2037*2**774
    printed_first=1011*10**232;printed_second=1011*10**231
    printed_binary=F(int('11111110010',2),2**11)*2**784
    assert printed_binary==u and printed_first!=v
    assert round_fp(printed_second,2,10)[0]!=printed_binary
    revised={'input_significand':1017,'input_exponent':784,
             'correct_decimal_significand':q,'correct_decimal_exponent':e,
             'correct_binary_significand':a,'correct_binary_digits':bin(a)[2:],
             'correct_binary_exponent':f,'published_11_digit_value_equals_input':True}
    return {'book_example':original,'erratum1999':revised}


def minimum_block():
    # Search all positive integer inputs with at most 10 significant binary
    # digits, using the ordering by exponent and then significand.
    count=0;first=None
    for e in range(1,785):
        step=1 if e>=10 else 2**(10-e)
        for q in range(512,1024,step):
            u=q*power(2,e-10)
            assert u.denominator==1 if isinstance(u,F) else True
            if round_fp(round_fp(u,10,4)[0],2,10)[0]!=u:
                first={'q':q,'e':e,'checked_before':count};break
            count+=1
        if first:break
    assert first and (first['q'],first['e'])==(1017,784)
    # A counterexample below one disproves a literal unrestricted minimum.
    small=None
    for e in range(0,-1201,-1):
        for q in range(512,1024):
            u=q*power(2,e-10)
            if round_fp(round_fp(u,10,4)[0],2,10)[0]!=u:
                small={'q':q,'e':e};break
        if small:break
    assert small
    return {'first_positive_integer_failure':first,'counterexample_below_one':small}


BLOCKS={'rounding':rounding_block,'roundtrip':roundtrip_block,'examples':examples_block,'minimum':minimum_block}


def main():
    p=argparse.ArgumentParser();p.add_argument('--resume',action='store_true');args=p.parse_args()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'scope':'4.4-D,17,18','blocks':{}}
    for name,fun in BLOCKS.items():
        if name in data['blocks']:continue
        t=time.monotonic();got=fun();data['blocks'][name]={'status':'passed','seconds':time.monotonic()-t,'result':got}
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({'checkpoint':name,**data['blocks'][name]}),flush=True)


if __name__=='__main__':main()
