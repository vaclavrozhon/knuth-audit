#!/usr/bin/env python3
"""Exact certificates used in the bounded historical audit of section 4.4."""
from fractions import Fraction as F
from pathlib import Path
import random,json

out={};u=11183445;st=[]
while u:
    q,r=divmod(u,64);st.append([u,q,r]);u=q
assert st==[[11183445,174741,21],[174741,2730,21],[2730,42,42],[42,0,42]]
assert int('101010101010010101010101',2)==11183445
out['legendre']=st
n=32;d=10;ell=3;m=3435973837
assert m*d==2**35+2
rng=random.Random(202644)
vals=list(range(65536))+[2**32-1-i for i in range(65536)]+[rng.randrange(2**32) for _ in range(10000)]
for x in vals:assert (m*x>>35)==x//10
out['division_by_10']={'N':n,'ell':ell,'m':m,'cases':len(vals),
    'scope':'Theorem proved in note; these are boundary/random checks only.'}
count=0
for k in range(1,11):
    for j in range(k):
        ds=[0]*k;ds[j]=1;t=F(0);y=F(0)
        for i in range(k-1,-1,-1):
            t=(ds[i]+t)/16
            a=F(8,5) if i==0 else F(3,80) if i==1 else F(1,10)
            y=a*(t+y)
        assert y==F(1,10**(j+1));count+=1
out['koons_lubkin']={'basis_vectors':count,
    'scope':'Exact rational algebra only, no EDVAC instruction or finite-rounding audit.'}
assert (2*60+46)*60+40==10000
assert F(376,1000)==F(22,60)+F(33,60**2)+F(36,60**3)
out['alkashi_examples']=2
dest=Path(__file__).resolve().parent/'results/radix-context.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
