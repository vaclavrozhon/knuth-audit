"""Exact GSR total variation via inverse stable radix sorting."""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial,prod
from collections import Counter
from itertools import product,permutations
import json
P=Path(__file__).resolve().parent

def eulerian(n):
 a=[1]
 for m in range(2,n+1):a=[(j+1)*(a[j] if j<len(a) else 0)+(m-j)*(a[j-1] if j else 0) for j in range(m)]
 return a

def ways(a,n,d):return comb(a+n-d-1,n) if a>d else 0
small=[];histories=0
for n in range(2,7):
 E=eulerian(n);assert sum(E)==factorial(n)
 hist=Counter(sum(p[i]>p[i+1] for i in range(n-1)) for p in permutations(range(n)));assert [hist[d] for d in range(n)]==E
 for a in [2,3,4]:
  d=Counter()
  for labels in product(range(a),repeat=n):
   p=tuple(sorted(range(n),key=lambda i:labels[i]));d[p]+=1;histories+=1
  for p in permutations(range(n)):
   desc=sum(p[i]>p[i+1] for i in range(n-1));assert d[p]==ways(a,n,desc)
  small.append(dict(n=n,a=a,histories=a**n))
N=52;E=eulerian(N);u=F(1,factorial(N));rows=[]
for k in range(1,15):
 a=2**k;ps=[F(ways(a,N,d),a**N) for d in range(N)];assert sum(E[d]*ps[d] for d in range(N))==1
 tv=sum(E[d]*abs(ps[d]-u) for d in range(N))/2
 collision=1-prod(F(a-i,a) for i in range(N)) if a>=N else F(1)
 assert tv<=collision
 rows.append(dict(k=k,tv=str(tv),tv_decimal=float(tv),collision_bound=str(collision),collision_decimal=float(collision)))
assert F(rows[5]['tv'])>F(1,10) and F(rows[13]['collision_bound'])<F(1,10)
assert F(rows[7]['tv'])>F(1,10) and F(rows[8]['tv'])<F(1,10)
r=dict(small_models=small,stable_label_histories=histories,rows=rows,scope='GSR binomial cut/proportional-drop model; not arbitrary human riffles or deterministic cut-and-riffle reachability.')
(P/'results/riffle-distance.json').write_text(json.dumps(r,indent=2)+'\n')
print('PASS',len(small),'small models',histories,'label histories')
for x in rows:print(x['k'],x['tv_decimal'],x['collision_decimal'])
