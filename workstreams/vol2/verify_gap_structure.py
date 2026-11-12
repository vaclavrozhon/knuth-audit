"""Exact multiplicative gap models and boundary checks for exercises3.5-20/21."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from itertools import product
from math import isqrt
import argparse,json
P=Path(__file__).resolve().parent;out=P/'results/gap-structure.json'
a=argparse.ArgumentParser();a.add_argument('--resume',action='store_true');args=a.parse_args();r=json.loads(out.read_text()) if args.resume and out.exists() else {}
def save():out.write_text(json.dumps(r,indent=2)+'\n')
def gaps(seq):
 s=sorted((v,i) for i,v in enumerate(seq));return [(s[(j+1)%len(s)][0]-x+(j==len(s)-1),i,s[(j+1)%len(s)][1]) for j,(x,i) in enumerate(s)]
def profile(seq):return sorted((x for x,i,j in gaps(seq)),reverse=True)
def logpoint(i):
 x=2*i+1;return F(x,2**(x.bit_length()-1))
def ratios(points):
 a=sorted(points);return sorted([y/x for x,y in zip(a,a[1:])]+[2*a[0]/a[-1]],reverse=True)
if 'log_profiles' not in r:
 cases=0;u=[];v=[]
 for N in range(1,513):
  z=logpoint(N-1);u.append(z);v.append(1 if z==1 else 2/z)
  expected=[F(N+j,N+j-1) for j in range(1,N+1)]
  assert ratios(u)==expected==ratios(v)
  prod=F(1)
  for k,t in enumerate(expected,1):prod*=t;assert prod==F(N+k,N);cases+=1
 assert u[1]==F(3,2) and v[1]==F(4,3)
 r['log_profiles']=dict(prefixes=512,gap_and_partial_product_checks=cases,C0064=dict(original_first_nonzero_log_argument=str(u[1]),reflected_first_nonzero_log_argument=str(v[1]),same_gap_multisets=True));save();print('PASS log profiles',cases,flush=True)
if 'interval_birth' not in r:
 seq=[F(0),F(1,2),F(1,4),F(1,8)];n=2;bad=[]
 for length,i,j in gaps(seq):
  old=max(i-n,j-n,1);new=max(i-n+1,j-n+1,1)
  if length<min(profile(seq[:n+old])):bad.append(dict(gap=str(length),endpoints=[i,j],printed_a=old,printed_comparison_min=str(min(profile(seq[:n+old]))),fixed_a=new))
 assert len(bad)==2
 histories=0;births=0;maxima=0
 for n in range(1,4):
  for rest in product(range(5),repeat=2*n-1):
   seq=[F(0)]+[F(x,5) for x in rest];states={m:profile(seq[:m]) for m in range(n,2*n+1)}
   counts=Counter();weight=F(0)
   for length,i,j in gaps(seq):
    aa=max(i-n+1,j-n+1,1);assert 1<=aa<=n
    assert length>=states[n+aa][-1]
    counts[aa]+=1;weight+=F(1,n+aa);births+=1
   assert all(counts[aa]<=2 for aa in range(2,n+1))
   assert weight>=2*sum((F(1,n+k) for k in range(1,n+1)),F(0))
   for k in range(1,n+1):assert states[n+k-1][0]>=states[n][k-1];maxima+=1
   histories+=1
 r['interval_birth']=dict(C0065=dict(sequence=list(map(str,[F(0),F(1,2),F(1,4),F(1,8)])),failing_gaps=bad),exhaustive_histories=histories,birth_checks=births,largest_gap_checks=maxima);save();print('PASS interval birth',histories,births,flush=True)
if 'oscillation' not in r:
 N=2**16;nu=[0]
 for j in range(N):
  x=2*j+1;den=2**(x.bit_length()-1);nu.append(nu[-1]+(x*x<2*den*den))
 rows=[]
 for m in range(1,17):
  # ceil(2^(m-1/2)) uses an exact integer square root, no floating log.
  a=isqrt(2**(2*m-1))+1;b=2**m
  assert nu[a]==nu[b]
  # Independently count odd integers in each binary magnitude band.
  count=1
  for h in range(1,m+1):
   last=isqrt(2**(2*h+1));first=2**h
   count+=(last+1)//2-first//2
  assert nu[b]==count
  rows.append(dict(m=m,upper_prefix=a,lower_prefix=b,count=count,upper_frequency=str(F(count,a)),lower_frequency=str(F(count,b))))
 r['oscillation']=dict(prefix_length=N,rows=rows);save();print('PASS oscillation',flush=True)
