"""Unnormalized exponent laws, associativity, truncation, and physical constants."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
import json,random
from unnormalized_model import Unnormalized
from accuracy_model import Arithmetic
from float_model import power
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/unnormalized.json'


def basic_format(b,p,after):
    a=Unnormalized(b,p,after);N=b**p;cases=trips=divcarry=0;witness=None
    vals=[(e,F) for e in [-1,0,1] for F in range(-N+1,N)]
    # Exhaustive operand digits, selected relative exponent values.
    for F,G,d in product(range(-N+1,N),range(-N+1,N),[0,1,3]):
        u=(0,F);v=(-d,G);U,V=a.val(u),a.val(v)
        lu,lv=a.leading(u),a.leading(v)
        add=a.add(u,v);mul=a.mul(u,v)
        assert add[0]-max(u[0],v[0]) in [0,1]
        assert mul[0]-(u[0]+v[0]-min(lu,lv)) in [0,-1]
        assert abs(a.val(add)-U-V)<=a.delta(add)
        assert abs(a.val(mul)-U*V)<=a.delta(mul)
        if after:assert a.leading(mul)==max(lu,lv)
        if F and G:
            div=a.div(u,v);base=u[0]-v[0]-lu+lv+max(lu,lv)
            extra=div[0]-base
            assert extra in ([0,1,2] if after else [0,1]),(b,p,after,u,v,div,base)
            assert abs(a.val(div)-U/V)<=a.delta(div)
            if after:assert a.leading(div)==max(lu,lv)
            if extra==2:
                divcarry+=1
                if witness is None:witness=dict(u=u,v=v,result=div,base_exponent=base)
        cases+=1
    rng=random.Random(4221400+b*10+p)
    triples=list(product([(0,F) for F in range(1,N)],repeat=3)) if N<=16 else [tuple(rng.choice(vals) for _ in range(3)) for _ in range(3000)]
    for u,v,w in triples:
        x=a.mul(a.mul(u,v),w);y=a.mul(u,a.mul(v,w))
        eps=Q((1+b)*(1+b*b),2)*power(b,-p)
        assert abs(a.val(x)-a.val(y))<=eps*power(b,min(x[0],y[0]))
        x=a.add(a.add(u,v),w);y=a.add(u,a.add(v,w))
        eps=(1+b*b)*power(b,-p)
        assert abs(a.val(x)-a.val(y))<=eps*power(b,min(x[0],y[0]))
        trips+=1
    return dict(pairs=cases,associativity_triples=trips,division_extra_carry_cases=divcarry,division_witness=witness,after_rounding=after)


def special_examples():
    a=Unnormalized(10,8);N=(26,602214);h=(-30,66261)
    assert a.mul(N,h)==(-6,39903)
    assert a.add(N,h)==(26,602214)
    wrong=Q('0.000602214')*10**26;correct=a.val(N)
    assert wrong*10==correct==602214*10**18
    u=(0,99);v=(0,1);small=Unnormalized(10,2);pre=Unnormalized(10,2,False)
    assert small.div(u,v)==(4,1) and pre.div(u,v)==(3,10)
    # Own truncation model: position exact x then truncate toward zero.
    def trunc(x):
        if not x:return Q(0)
        s=-1 if x<0 else 1;e=0;f=abs(Q(x))
        while f>=1:f/=10;e+=1
        while f<Q(1,10):f*=10;e-=1
        return s*(f*10**8//1)*power(10,e-8)
    def residual(u,v):
        w=trunc(u+v);up=trunc(w-v);vpp=trunc(w-up)
        corr=trunc(trunc(u-up)+trunc(v-vpp))
        return w,u+v-w,corr
    u=Q('0.10000001')*10**20;v=-Q('0.10000001')*10**10
    w,r,corr=residual(u,v)
    assert r==998999999900 and Arithmetic(10,8).R(r)!=r
    second=residual(Q(12345678),Q('0.012345678'))
    assert second[1]==Q('0.012345678') and second[2]==Q('0.01234568')
    return dict(avogadro=dict(printed=str(wrong),corrected=str(correct),printed_fraction_digits=9,corrected_pair=N),physical_product=a.mul(N,h),physical_sum=a.add(N,h),division_rounding=dict(post=small.div((0,99),(0,1)),pre=pre.div((0,99),(0,1))),truncation_first=list(map(str,[w,r,corr])),truncation_second=list(map(str,second)))


def distributive():
    count=0;maxima=[];family=[]
    for b,p in [(2,3),(3,2),(4,2),(10,2),(10,8)]:
        for after in [True,False]:
            a=Unnormalized(b,p,after);N=b**p;rng=random.Random(4221800+b+p);mx=Q(0)
            for _ in range(3000):
                u,v,w=[(rng.randrange(-2,3),rng.randrange(-N+1,N)) for _ in range(3)]
                x=a.mul(u,a.add(v,w));z=a.add(a.mul(u,v),a.mul(u,w))
                diff=abs(a.val(x)-a.val(z));scale=power(b,min(x[0],z[0]))
                lu=a.leading(u)
                eps=Q(1,2)*power(b,-p)*((1+b)*b**(lu+2)+3)
                assert diff<=eps*scale,(b,p,after,u,v,w,x,z,diff,eps)
                mx=max(mx,diff/scale);count+=1
            maxima.append(dict(b=b,p=p,after=after,maximum_observed=str(mx)))
    for p in range(2,13):
        for after in [True,False]:
            a=Unnormalized(10,p,after);h=power(10,-p)
            u=(0,1);v=(0,65*10**(p-2)+1);w=(0,-65*10**(p-2)+1)
            x=a.mul(u,a.add(v,w));z=a.add(a.mul(u,v),a.mul(u,w))
            assert x==(-p,2) and z==(-1,1)
            ratio=abs(a.val(x)-a.val(z))/power(10,min(x[0],z[0]))
            assert ratio==Q(1,10)-2*h
            family.append(dict(p=p,after=after,left=x,right=z,required_epsilon=str(ratio)))
    return dict(cases=count,maxima=maxima,lower_bound_family=family,scope='Conservative upper bound plus nonvanishing lower bound; no optimal epsilon claim.')


if __name__=='__main__':
    out=json.loads(OUT.read_text()) if OUT.exists() else {}
    def run(key,fn):
        if key not in out:
            out[key]=fn();OUT.write_text(json.dumps(out,indent=2)+'\n');print('PASS',key,flush=True)
    run('special_examples',special_examples)
    for b,p in [(2,2),(2,3),(3,2),(4,2),(5,2),(10,2)]:
        for after in [True,False]:run(f'b{b}_p{p}_after{after}',lambda b=b,p=p,after=after:basic_format(b,p,after))

    run('distributive',distributive)
