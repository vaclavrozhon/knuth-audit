"""Independent permutation DP and Goldstein--Moews partition formulas."""
from pathlib import Path
from math import comb,factorial,isqrt
from functools import lru_cache
from collections import Counter
import json,argparse
P=Path(__file__).resolve().parent;out=P/'results/exchange-validation.json'
a=argparse.ArgumentParser();a.add_argument('--resume',action='store_true');args=a.parse_args()
r=json.loads(out.read_text()) if args.resume and out.exists() else {}
def save():out.write_text(json.dumps(r,indent=2)+'\n')
def catalan(n):return comb(2*n,n)//(n+1)
Q=[1,1]
for n in range(2,101):Q.append(Q[-1]+(n-1)*Q[-2])
if 'permutation_dp' not in r:
 rows=[]
 raw=[json.loads(s) for s in (P/'results/exchange-census.jsonl').read_text().splitlines()]
 for row in raw:
  n=row['n'];ident=tuple(range(1,n+1));d={ident:1};states=0
  for j in range(n):
   e=Counter()
   for p,c in d.items():
    for k in range(n):
     pp=list(p);pp[j],pp[k]=pp[k],pp[j];e[tuple(pp)]+=c
   d=e;states+=len(d)
  assert sum(d.values())==n**n and len(d)==factorial(n)
  assert d[(n,)+tuple(range(1,n))]==row['right']==2**(n-1)
  assert d[ident]==row['identity']==Q[n]
  assert d[tuple(range(2,n+1))+(1,)]==row['left']==catalan(n)
  lo,hi=min(d.values()),max(d.values())
  assert lo==row['min'] and hi==row['max']
  assert sum(c==lo for c in d.values())==row['minimizers']
  assert sum(c==hi for c in d.values())==row['maximizers']
  rows.append(dict(n=n,states=states,histories=n**n,min=lo,max=hi));print('PASS DP',rows[-1],flush=True)
 r['permutation_dp']=rows;save()

@lru_cache(None)
def G(m,p):
 num=comb(2*m,m)*comb(2*p,p)*(m+p+4*m*p)-(m+p)*comb(2*m+2*p,m+p)
 den=2*(m+p)*(m+p+1);q,rem=divmod(num,den);assert rem==0 and q>0;return q
@lru_cache(None)
def best(lens):
 if not lens:return 1
 a=lens[0];rest=lens[1:];v=catalan(a)*best(rest)
 for b,c in Counter(rest).items():
  tail=list(rest);tail.remove(b);v+=c*G(a,b)*best(tuple(tail))
 return v

def partitions(n,low=1):
 if not n:yield ();return
 for x in range(low,n+1):
  for y in partitions(n-x,x):yield (x,)+y

if 'partition_maxima' not in r:
 rows=[];cases=0
 for n in range(1,29):
  values=[(best(q),q) for q in partitions(n)];cases+=len(values);mx=max(v for v,_ in values);qs=[q for v,q in values if v==mx]
  expected=[(1,)*n] if n==1 or n>=18 else ([(1,1),(2,)] if n==2 else ([(1,2),(3,)] if n==3 else [(n//2,n-n//2)]))
  assert qs==expected,(n,qs,expected)
  assert best((1,)*n)==Q[n]
  if n<=8:assert mx==r['permutation_dp'][n-1]['max']
  rows.append(dict(n=n,partitions=len(values),maximum=mx,winning_partitions=qs));print('PASS partitions',n,len(values),qs,flush=True)
 assert all(Q[n]**2>=factorial(n) for n in range(101))
 assert all(4*Q[n]<=4**n for n in range(1,15)) and 4*Q[29]>4**29
 # Reproduce the finite prefix of Lemma5's large-n estimate.
 W={n:max(G(m,n-m) for m in range(1,n)) for n in range(2,10)}
 for n in range(10,22):
  W[n]=(n-1)*catalan(n-1)+sum(catalan(j)*W[n-j-1] for j in range(n-2))
 assert all(W[n]<=4**(n-2) for n in W),W
 r['partition_maxima']=dict(cases=cases,rows=rows,Q_29=Q[29],lemma5_bounds=W,dependency='Corollary15 and Lemma14 of primary paper; numerical reproduction is not independent proof of their general structural theorem.');save()
 print('PASS partition total',cases,flush=True)
