#!/usr/bin/env python3
"""Prove every listed prime in TAOCP2 answer4.5.4-27, including2024erratum.

Two independent modular algorithms: FLINT modular powering, and explicit
repeated squaring with the book's special quotient/remainder reduction.
The exact Proth criterion is proved separately. Does not claim that the
historical lists below300000 are exhaustive. Resume completed methods.
"""
from pathlib import Path
import hashlib
import json
import time
from flint import fmpz
from verify_primality_jacobi import jacobi

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/proth-listed-primes.json'
EXPONENTS={
    3:[1,2,5,6,8,12,18,30,36,41,66,189,201,209,276,353,408,438,534,
       2208,2816,3168,3189,3912,20909,34350,42294,42665,44685,48150,
       54792,55182,59973,80190,157169,213321],
    5:[1,3,7,13,15,25,39,55,75,85,127,1947,3313,4687,5947,13165,
       23473,26607,125413,209787,240937]}


def save(state):
    temp=OUT.with_suffix('.json.tmp')
    temp.write_text(json.dumps(state,indent=2)+'\n')
    temp.replace(OUT)


def special_power(a,k,e,n):
    x=fmpz(pow(a,k,int(n)))
    for j in range(e-1):
        square=x*x
        high=square>>e
        low=square-(high<<e)
        quotient,remainder=divmod(high,k)
        x=low-quotient+(remainder<<e)
        if x<0:
            x+=n
        assert 0<=x<n
    return x


def main():
    state=json.loads(OUT.read_text()) if OUT.exists() else dict(
        scope='57 listed primes; includes3*2^54792+1 from29July2024erratum. No exhaustive gap census.',
        entries={},status='running')
    # Establish the corrected, previously omitted entry first.
    jobs=[(3,54792)]+sorted((k,e) for k,es in EXPONENTS.items() for e in es if (k,e)!=(3,54792))
    assert len(jobs)==57 and len(set(jobs))==57
    for k,e in jobs:
        key=f'{k}*2^{e}+1'
        n=fmpz(k)*(fmpz(1)<<e)+1
        a=3 if k==5 and e>=2 else next(a for a in range(2,10000) if jacobi(a,int(n))==-1)
        assert jacobi(a,int(n))==-1
        assert k<=2**e+1 or (k,e)==(5,1)
        rec=state['entries'].setdefault(key,dict(k=k,exponent=e,base=a,
            n_sha256=hashlib.sha256(int(n).to_bytes((int(n).bit_length()+7)//8,'big')).hexdigest()))
        assert rec['base']==a
        if 'modular_power' not in rec:
            start=time.monotonic()
            residue=pow(fmpz(a),fmpz(k)<<(e-1),n)
            assert residue==n-1,(key,'modular_power')
            rec['modular_power']=dict(passed=True,seconds=time.monotonic()-start)
            save(state);print(key,'modular_power',rec['modular_power'],flush=True)
        if 'special_reduction' not in rec:
            start=time.monotonic()
            residue=special_power(a,k,e,n)
            assert residue==n-1,(key,'special_reduction')
            rec['special_reduction']=dict(passed=True,squarings=e-1,seconds=time.monotonic()-start)
            save(state);print(key,'special_reduction',rec['special_reduction'],flush=True)
        # N=11 is below the Proth parameter range; it is directly prime.
        if (k,e)==(5,1):
            assert all(11%d for d in [2,3])
            rec['small_exception']='11 directly certified by trial division2,3'
            save(state)
    state['status']='passed'
    save(state)
    print('ALL57LISTEDPRIMESPROVEDBYBOTHMETHODS',flush=True)


if __name__=='__main__':main()
