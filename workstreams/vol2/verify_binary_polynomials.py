"""Exact binary polynomial checks for TAOCP 3.2.2.

Bit i is the coefficient of x^i. Integer addition is NOT polynomial
addition: all polynomial sums use xor. Squaring spreads coefficient bits.
The reference multiplication below instead uses coefficient convolution.
"""
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import random
import sys
import time

ROOT=Path(__file__).resolve().parent
LAGS=[(24,55),(38,89),(37,100),(30,127),(83,258),(107,378),
      (273,607),(1029,2281),(576,3217),(4187,9689),(7083,19937),(9739,23209)]
SPREAD=[sum(((b>>j)&1)<<(2*j) for j in range(8)).to_bytes(2,'little') for b in range(256)]


def remainder(a,f):
    while a.bit_length()>=f.bit_length():
        a^=f<<(a.bit_length()-f.bit_length())
    return a


def gcd(a,b):
    while b:a,b=b,remainder(a,b)
    return a


class Quotient:
    def __init__(self,k,tail,lag=None):
        self.k=k;self.tail=tail;self.f=(1<<k)|tail;self.mask=(1<<k)-1;self.lag=lag

    def reduce(self,a):
        if self.lag is None:return remainder(a,self.f)
        while a>>self.k:
            high=a>>self.k
            a=(a&self.mask)^high^(high<<self.lag)
        return a

    def square(self,a):
        raw=int.from_bytes(b''.join(SPREAD[b] for b in a.to_bytes((a.bit_length()+7)//8,'little')),'little')
        return self.reduce(raw)

    def times_x(self,a):
        a<<=1
        return a^self.f if a>>self.k else a

    def power_x(self,n):
        a=1
        for bit in bin(n)[2:]:
            a=self.square(a)
            if bit=='1':a=self.times_x(a)
        return a

    def primitive(self,factors):
        order=(1<<self.k)-1
        return self.power_x(order)==1 and all(self.power_x(order//q)!=1 for q in factors)


def reference_product(a,b,f):
    # Independent coefficient-by-coefficient convolution and long division.
    aa=[(a>>j)&1 for j in range(a.bit_length())]
    bb=[(b>>j)&1 for j in range(b.bit_length())]
    if not aa or not bb:return 0
    cc=[0]*(len(aa)+len(bb)-1)
    for i,x in enumerate(aa):
        for j,y in enumerate(bb):cc[i+j]^=x&y
    ff=[(f>>j)&1 for j in range(f.bit_length())]
    for j in range(len(cc)-1,len(ff)-2,-1):
        if cc[j]:
            for i,x in enumerate(ff):cc[j-(len(ff)-1)+i]^=x
    return sum(c<<j for j,c in enumerate(cc))


def reference_power_x(n,f):
    result=1;x=2
    while n:
        if n&1:result=reference_product(result,x,f)
        n>>=1
        if n:x=reference_product(x,x,f)
    return result


def prime_factors_small(n):
    out=[];q=2
    while q*q<=n:
        if n%q==0:
            out.append(q)
            while n%q==0:n//=q
        q+=1
    if n>1:out.append(n)
    return out


def mersenne_prime(k):
    assert k>=3 and all(k%d for d in range(2,isqrt(k)+1))
    m=(1<<k)-1;s=4
    for j in range(k-2):s=(s*s-2)%m
    assert s==0,('Lucas-Lehmer failed',k)
    return dict(exponent=k,iterations=k-2,residue=s,method='Lucas-Lehmer')


def sparse_degree35(factors):
    ring=Quotient(35,5)
    M=(1<<35)-1
    assert ring.primitive(factors)
    assert reference_power_x(M,ring.f)==1
    for q in factors:assert reference_power_x(M//q,ring.f)!=1
    from math import gcd as integer_gcd
    assert integer_gcd(35,M)==1
    return dict(degree=35,mask=5,primitive=True,block_stride_coprime_to_period=True)


def main():
    start=time.monotonic();rng=random.Random(3222026)
    factors=json.loads((ROOT/'results/binary-period-factors.json').read_text())
    assert factors['status']=='passed'
    factormap={row['exponent']:[q for q,e in row['factors']]
               for row in factors['large_composite_exponent_rows']+factors['small_exponent_rows']}
    resume='--resume' in sys.argv
    result=(json.loads((ROOT/'results/binary-polynomials.partial.json').read_text()) if resume
            else dict(status='running',arithmetic_checks=0,lag_table=[],masks=[]))
    prior_elapsed=result.get('elapsed_seconds',0)
    def save(final=False):
        name='binary-polynomials.json' if final else 'binary-polynomials.partial.json'
        result['elapsed_seconds']=prior_elapsed+time.monotonic()-start
        (ROOT/'results'/name).write_text(json.dumps(result,indent=2)+'\n')

    for k in ([] if resume else range(2,129)):
        for j in range(8):
            tail=rng.randrange(1<<k)|1;a=rng.randrange(1<<k)
            ring=Quotient(k,tail)
            assert ring.square(a)==reference_product(a,a,ring.f)
            n=rng.randrange(512)
            assert ring.power_x(n)==reference_power_x(n,ring.f)
            result['arithmetic_checks']+=2
    print('independent arithmetic checks',result['arithmetic_checks'],flush=True)

    for l,k in LAGS:
        if any(row['degree']==k and row['lag']==l for row in result['lag_table']):continue
        ring=Quotient(k,(1<<l)|1,l)
        checkpoints={k//q for q in prime_factors_small(k)}
        value=2;gcds=[]
        for j in range(1,k+1):
            value=ring.square(value)
            if j in checkpoints:
                g=gcd(value^2,ring.f);assert g==1
                gcds.append(dict(frobenius_steps=j,gcd=g))
        assert value==2
        row=dict(lag=l,degree=k,rabin_final=value,rabin_gcds=gcds)
        if k in factormap:
            order=(1<<k)-1
            assert ring.power_x(order)==1
            witnesses=[dict(prime_divisor=q,residue=ring.power_x(order//q)) for q in factormap[k]]
            assert all(w['residue']!=1 for w in witnesses)
            row['order_witnesses']=witnesses
        else:
            row['mersenne_prime_certificate']=mersenne_prime(k)
        result['lag_table'].append(row);save()
        print('lag',l,k,'proved primitive',round(time.monotonic()-start,2),'seconds',flush=True)

    for k in range(2,65):
        if any(row['degree']==k for row in result['masks']):continue
        # An even number of mask bits is necessary: f(1) must be nonzero.
        weight=min(range(2,k+1,2),key=lambda w:(abs(2*w-k),w))
        for trial in range(10000):
            positions=sorted(range(1,k),key=lambda j:sha256(f'vol2-mask-{k}-{trial}-{j}'.encode()).digest())[:weight-1]
            tail=1+sum(1<<j for j in positions)
            ring=Quotient(k,tail)
            if ring.primitive(factormap[k]):break
        else:raise AssertionError(('mask search exhausted',k))
        order=(1<<k)-1
        # Different arithmetic and exponentiation model, for EVERY selected mask.
        assert reference_power_x(order,ring.f)==1
        for q in factormap[k]:assert reference_power_x(order//q,ring.f)!=1
        result['masks'].append(dict(degree=k,mask_hex=hex(tail),ones=tail.bit_count(),trials=trial+1))
        print('balanced mask',k,hex(tail),'independently verified',flush=True)
        save()

    pi_mask=0x243F6A8885A308D3
    ring=Quotient(64,pi_mask)
    # The original assertion that this published mask is primitive failed.
    # Check the counterexample rather than silently dropping that assertion.
    assert pi_mask.bit_count()==27 and remainder(ring.f,3)==0
    assert not ring.primitive(factormap[64])
    residue=ring.power_x((1<<64)-1)
    assert reference_power_x((1<<64)-1,ring.f)==residue!=1
    fixed=0xE3EAD987836107B1
    assert 0<fixed<1<<64
    assert ((fixed<<1)&((1<<64)-1))^pi_mask==fixed
    assert reference_product(2,fixed,ring.f)==fixed
    repair=pi_mask^(1<<4);repaired=Quotient(64,repair)
    assert repaired.primitive(factormap[64])
    assert reference_power_x((1<<64)-1,repaired.f)==1
    witnesses=[]
    for q in factormap[64]:
        value=reference_power_x(((1<<64)-1)//q,repaired.f)
        assert value!=1
        witnesses.append(dict(prime_divisor=q,residue_hex=hex(value)))
    result['published_pi_mask']=dict(mask_hex=hex(pi_mask),ones=pi_mask.bit_count(),primitive=False,
        factor='x+1',nonzero_fixed_state_hex=hex(fixed),order_test_residue_hex=hex(residue),
        one_bit_repair=dict(mask_hex=hex(repair),ones=repair.bit_count(),order_witnesses=witnesses))
    result['published_degree35']=sparse_degree35(factormap[35])

    # Exercise 18: state coefficients as formal linear forms in 35 seed bits.
    seq=[1<<j for j in range(35)]
    for n in range(35,70):seq.append(seq[n-33]^seq[n-35])
    assert seq[35]==seq[0]^seq[2]
    forms=[seq[j] for j in [0,1,2,35,36,37]]
    relevant=sorted({j for f in forms for j in range(35) if (f>>j)&1})
    pairs=set()
    for values in range(1<<len(relevant)):
        seed=sum(((values>>i)&1)<<j for i,j in enumerate(relevant))
        bits=[(f&seed).bit_count()%2 for f in forms]
        pairs.add((4*bits[0]+2*bits[1]+bits[2],4*bits[3]+2*bits[4]+bits[5]))
    assert len(pairs)==32 and all(((b>>2)&1)==((a>>2)^(a&1)) for a,b in pairs)
    result['exercise18']=dict(possible_pairs=sorted(pairs),count=32,
                              identity='most significant bit of U_(n+1) = first xor third bit of U_n')
    assert len(result['lag_table'])==12 and len(result['masks'])==63
    result['status']='passed'
    result['initial_run_note']='Initial run passed all lag rows and generated masks, then failed on the published pi mask. Source image confirmed the transcription. Resume preserved completed checks and verified the counterexample and a one-bit repair.'
    save(final=True)
    print('ALL binary polynomial checks passed',flush=True)


if __name__=='__main__':main()
