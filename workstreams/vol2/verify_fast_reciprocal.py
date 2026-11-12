#!/usr/bin/env python3
"""4.3.3D: exact rational simulation of R1--R3 and quotient correction."""
from pathlib import Path
from fractions import Fraction as F
import json,random,time
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/fast-reciprocal.json'

def floor(x):return x.numerator//x.denominator
def ceil(x):return -((-x.numerator)//x.denominator)

def reciprocal(v,n,stats=None):
    assert F(1,2)<=v<1 and n>=1
    vp=floor(8*v);z=F(32//vp,4);k=0
    delta=1/v-z
    assert 0<z<=2 and abs(delta)<F(1,2)
    while True:
        assert (z*(1<<((1<<k)+1))).denominator==1
        assert abs(delta)<F(1,1<<(1<<k)) and 0<z<=2
        precision=(1<<(k+1))+3
        Vk=F(floor(v*(1<<precision)),1<<precision)
        zsq=z*z;raw=2*z-Vk*zsq;grid=1<<((1<<(k+1))+1)
        newz=F(ceil(raw*grid),grid);rounding=newz-raw
        assert 0<=rounding<F(1,grid)
        newdelta=1/v-newz
        assert newdelta==v*delta*delta-zsq*(v-Vk)-rounding
        # General range proof, including the endpoint z=2.
        assert raw==1/Vk-Vk*(z-1/Vk)**2
        assert raw<=1/Vk<=2 and newz<=2
        # The printed strict middle inequality fails exactly when delta=0.
        strict=(v*delta*delta<delta*delta)
        assert strict==(delta!=0)
        if stats is not None:
            stats['iterations']+=1
            stats['zero_error_strict_failures']+=not strict
        z,delta,k=newz,newdelta,k+1
        assert abs(delta)<F(1,1<<(1<<k)) and 0<z<=2
        if (1<<k)>=n:break
    assert abs(z-1/v)<=F(1,1<<n)
    return z

def quotient(u,v,n,z=None):
    assert 0<=u<1<<n and 0<v<1<<n
    d=v.bit_length();normalized=F(v,1<<d)
    if z is None:z=reciprocal(normalized,n+2)
    q=floor(F(u,1<<d)*z);initial=q;remainder=u-q*v
    if remainder<0:q-=1;remainder+=v
    elif remainder>=v:q+=1;remainder-=v
    assert (q,remainder)==divmod(u,v)
    return initial-q

def reciprocal_tests():
    stats=dict(iterations=0,zero_error_strict_failures=0);cases=0
    for width in range(1,15):
        for a in range(1<<(width-1),1<<width):
            reciprocal(F(a,1<<width),width+3,stats);cases+=1
    rng=random.Random(43354)
    for n in [1,2,3,4,5,7,8,9,15,16,17,31,32,33,63,64,127,256,1024,4096]:
        for v in [F(1,2),F(2,3),F(4,5),F((1<<n)-1,1<<n) if n>1 else F(1,2)]:
            reciprocal(v,n,stats);cases+=1
        for j in range(5):
            v=F((1<<n)+rng.getrandbits(n),1<<(n+1))
            reciprocal(v,n,stats);cases+=1
    assert reciprocal(F(1,2),1)==2
    return dict(cases=cases,exhaustive_input_width_max=14,max_target_bits=4096,
                seed=43354,**stats,strict_inequality_witness=dict(v='1/2',z0=2,delta0=0,left=0,right=0))

def quotient_tests():
    cases=0;adjust={-1:0,0:0,1:0}
    for n in range(1,9):
        for v in range(1,1<<n):
            z=reciprocal(F(v,1<<v.bit_length()),n+2)
            for u in range(1<<n):
                adjust[quotient(u,v,n,z)]+=1;cases+=1
    rng=random.Random(433312);large=0
    for n in [32,64,127,256,1024,4096,16384]:
        for j in range(30):
            u=rng.getrandbits(n)
            v=1 if j==0 else (1<<n)-1 if j==1 else rng.randrange(1,1<<n)
            adjust[quotient(u,v,n)]+=1;large+=1
    return dict(exhaustive_cases=cases,large_cases=large,max_bits=16384,
                initial_minus_final_quotient=adjust,seed=433312)

def main():
    d=json.loads(OUT.read_text()) if OUT.exists() else {}
    for name,fn in [('reciprocal',reciprocal_tests),('division',quotient_tests)]:
        if name in d:continue
        start=time.monotonic();r=fn();r['seconds']=round(time.monotonic()-start,3)
        d[name]=r;OUT.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'block':name,**r}),flush=True)
if __name__=='__main__':main()
