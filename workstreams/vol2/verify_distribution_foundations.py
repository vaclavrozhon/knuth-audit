"""Exact finite checks supporting the proofs in distribution-foundations.md."""
from pathlib import Path
from fractions import Fraction as F
from math import floor,ceil,factorial,comb
from itertools import permutations,product
from collections import Counter
import argparse,json
P=Path(__file__).resolve().parent;out=P/'results/distribution-foundations.json'
a=argparse.ArgumentParser();a.add_argument('--resume',action='store_true');args=a.parse_args()
r=json.loads(out.read_text()) if args.resume and out.exists() else {}
def save():out.write_text(json.dumps(r,indent=2)+'\n')
def cyclic_counts(s,k):return Counter(tuple(s[(i+j)%len(s)] for j in range(k)) for i in range(len(s)))
if 'intervals' not in r:
 cases=0
 for b in range(2,33):
  for i in range(12):
   for j in range(i+1,13):
    u,v=F(i,12),F(j,12)
    il,ir=F(ceil(b*u),b),F(floor(b*v),b)
    ol,orr=F(floor(b*u),b),F(ceil(b*v),b)
    inner=max(F(0),ir-il);outer=orr-ol
    assert 0<=ol<=u<v<=orr<=1
    assert inner<=v-u<=outer and outer-inner<=F(2,b)
    cases+=1
 # Literal page153 uses signed side lengths even for an empty inner box.
 b=2;u=F(0);v=F(1,4);up=F(floor(b*u),b);vp=F(floor(b*v),b)
 literal_inner=(vp-up-F(1,b))**2
 assert up+F(1,b)>vp and literal_inner==F(1,4)
 # At the boundary v=1 its outer interval leaves the unit cube.
 literal_outer=F(floor(b*1),b)-up+F(1,b);assert literal_outer==F(3,2)
 r['intervals']=dict(repaired_one_dimensional_cases=cases,C0059=dict(empty_box_actual_probability='0',printed_inner_product=str(literal_inner),outer_unit_interval_actual_probability='1',printed_outer_product=str(literal_outer)));save();print('PASS interval repair',cases,flush=True)
if 'periodic' not in r:
 s=[0,0,1,1];assert cyclic_counts(s,1)==Counter({(0,):2,(1,):2});assert len(cyclic_counts(s,2))==4 and (1,1,1) not in cyclic_counts(s,3)
 x=list(map(int,'0001000111011101'));cs=cyclic_counts(x,3)
 assert len(cs)==8 and set(cs.values())=={2}
 assert x[::2]==[0,0,0,0,1,0,1,0]
 even=F(sum(x[::2]),8);assert even==F(1,4)
 y=[1-z for z in x];assert F(sum(y[::2]),8)==F(3,4) and cyclic_counts(y,3)==cs
 # Conditional on phase, every auxiliary real lies below1: the threshold
 # indicator of (X+U)/2 is exactly X, independently of U's distribution.
 for z in x:
  for v in [F(0),F(1,7),F(1,2),F(999,1000)]:assert ((z+v)/2>=F(1,2))==bool(z)
 r['periodic']=dict(example11=''.join(map(str,x)),triple_counts={''.join(map(str,w)):v for w,v in sorted(cs.items())},even_bits=x[::2],C0060=dict(printed_even_upper_probability=str(even),complemented_even_upper_probability='3/4'),earlier_ternary_evidence='results/complete-sequences.json; no successful earlier census repeated');save();print('PASS periodic examples and C0060',flush=True)
if 'density_oscillation' not in r:
 N=2**16;counts=[0];nu=0
 for n in range(N):
  e=(n+1).bit_length()-1;nu+=(e%2==0);counts.append(nu)
 rows=[]
 for k in range(1,9):
  n1,n2=2**(2*k-1)-1,2**(2*k)-1;expected=(2**(2*k)-1)//3
  assert counts[n1]==counts[n2]==expected
  rows.append(dict(k=k,n1=n1,n2=n2,count=expected,upper_ratio=str(F(expected,n1)),lower_ratio=str(F(expected,n2))))
 r['density_oscillation']=dict(prefix_length=N,rows=rows);save();print('PASS density oscillation',flush=True)
if 'run_patterns' not in r:
 rows=[];histories=0
 for k in range(1,7):
  count=0
  for w in permutations(range(k+2)):
   count+=(w[0]>w[1] and all(w[i]<w[i+1] for i in range(1,k)) and w[k]>w[k+1]);histories+=1
  p=F(count,factorial(k+2));assert p==F(k,factorial(k+1))-F(k+1,factorial(k+2))
  rows.append(dict(length=k,start_density=str(p),run_frequency=str(2*p),permutation_count=count))
 r['run_patterns']=dict(histories=histories,rows=rows);save();print('PASS run patterns',histories,flush=True)
if 'coupon_reset' not in r:
 states=0;rows=[]
 for b in range(2,9):
  full=(1<<b)-1;word=list(range(b-1,-1,-1))+list(range(b))
  for initial in range(full):
   state=initial;resets=[]
   for j,x in enumerate(word,1):
    state|=1<<x
    if state==full:state=0;resets.append(j)
   assert state==0 and resets[-1]==2*b;states+=1
  H=sum((F(1,j) for j in range(1,b+1)),F(0));pi={s:1/(H*(b-s.bit_count())*comb(b,s.bit_count())) for s in range(full)}
  assert sum(pi.values())==1
  dest=Counter()
  for s,p in pi.items():
   for x in range(b):
    ss=s|(1<<x);dest[0 if ss==full else ss]+=p/b
  assert dict(dest)==pi and pi[0]==1/(b*H)
  rows.append(dict(b=b,proper_states=full,start_density=str(pi[0]),mean_coupon_length=str(b*H)))
 # Independent enumeration of short complete coupon words vs Stirling counts.
 S={(0,0):1}
 for n in range(1,9):
  for k in range(1,n+1):S[n,k]=k*S.get((n-1,k),0)+S.get((n-1,k-1),0)
 words=0;checks=0
 for b in range(2,5):
  for k in range(b,9):
   count=0
   for w in product(range(b),repeat=k):
    count+=(len(set(w))==b and len(set(w[:-1]))==b-1);words+=1
   assert count==factorial(b)*S.get((k-1,b-1),0);checks+=1
 r['coupon_reset']=dict(reset_states=states,stationary_rows=rows,enumerated_words=words,distribution_checks=checks);save();print('PASS coupon reset',states,words,flush=True)
