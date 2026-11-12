"""Exact support for selection-randomness.md; each completed block is retained."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter,defaultdict
from itertools import product
from functools import lru_cache
import argparse,json,math
P=Path(__file__).resolve().parent;out=P/'results/selection-randomness.json'
a=argparse.ArgumentParser();a.add_argument('--resume',action='store_true');args=a.parse_args()
r=json.loads(out.read_text()) if args.resume and out.exists() else {}
def save():out.write_text(json.dumps(r,indent=2)+'\n')
@lru_cache(None)
def vdc(n):
 if n==0:return F(0)
 s=bin(n)[2:];return F(int(s[::-1],2),2**len(s))
if 'sparse_edit' not in r:
 N=16;k=2;u=[F(3,4)]*(N+k);v=u.copy()
 for j in range(math.isqrt(len(v)-1)+1):v[j*j]=0
 old=[n for n in range(N) if all(u[n+j]>=F(1,2) for j in range(k))]
 new=[n for n in range(N) if all(v[n+j]>=F(1,2) for j in range(k))]
 changed=sorted(set(old)-set(new));assert changed==[0,1,3,4,8,9,15]
 assert len(changed)>math.isqrt(N)
 r['sparse_edit']=dict(C0061=dict(N=N,k=k,old_count=len(old),new_count=len(new),changed_starts=changed,printed_bound=math.isqrt(N)),repair='At most k*(floor(sqrt(N+k-2))+1) changed windows, hence O(k*sqrt(N)) for fixed k.');save();print('PASS sparse edit',flush=True)
if 'dyadic_counts' not in r:
 checks=0
 for offset in range(8):
  for depth in range(1,7):
   b=2**depth;counts=[0]*b
   for N in range(1,129):
    counts[int(b*vdc(offset+N-1))]+=1
    for c in counts:assert abs(F(c)-F(N,b))<=1;checks+=1
 r['dyadic_counts']=dict(checks=checks,offsets=8,max_length=128,max_depth=6);save();print('PASS dyadic counts',checks,flush=True)
if 'wald' not in r:
 def rule(mode,j,u):
  n=len(u)
  if j==1 or mode==0:return 1
  if mode==1:return int(n%(j+1)==0)
  if mode==2:return int(n>0 and int((j+1)*u[-1])%2==0)
  return int(n>=j and all(u[n-t-1]<F(1,2) for t in range(j)))
 examples=[];steps=0
 for mode in range(4):
  for offset in [0,-1]:
   u=[];paths=[];counts=Counter();low=0
   for n in range(512):
    path=();depth=0
    while True:
     depth+=1;path+=(rule(mode,depth,u),)
     # Independent recount of previous assignments at this node.
     assert counts[path]==sum(x==path for x in paths)
     if counts[path]<3*4**(depth-1):break
    counts[path]+=1;z=vdc(counts[path]+offset);u.append(z);paths.append(path);low+=(z<F(1,2))
    assert low==sum((c+1)//2 if offset==-1 else c//2 for c in counts.values())
    if offset==-1:assert 2*low>=n+1
    else:assert 2*low<=n+1
    for depth0 in range(1,5):
     pref=tuple(rule(mode,j,u[:-1]) for j in range(1,depth0+1))
     # Structural path-capacity lower bound for every emitted node.
     if depth>=depth0:
      members=sum(p[:depth0]==path[:depth0] for p in paths if len(p)>=depth0)
      assert members>=4**(depth-1)-4**(depth0-1)+1
    steps+=1
   examples.append(dict(mode=mode,offset=offset,first_values=[str(z) for z in u[:8]],length=len(u),below_half=low,nodes=len(counts),max_depth=max(map(len,paths))))
 # All rules select everything: independent closed capacity formula.
 counts=Counter();depths=[]
 for n in range(4097):
  d=1
  while counts[d]>=3*4**(d-1):d+=1
  counts[d]+=1;depths.append(d)
  assert d==int(math.log(n+1,4))+1 or n+1 in [4**j for j in range(7)]
 witnesses=[]
 for q in range(1,6):
  N=4**(q+1);d=depths[N]
  assert 4<=4**q<N<=4**(q+1) and d==q+2
  witnesses.append(dict(r=1,q=q,N=N,depth_of_U_N=d,printed_max=q+1))
 r['wald']=dict(steps=steps,examples=examples,C0062=dict(printed_first_value='1/2',printed_first_below_half_count=0,repaired_first_value='0'),C0063=witnesses);save();print('PASS Wald',steps,flush=True)
if 'adaptive_cylinders' not in r:
 cases=0;rows=[];N=12;total=2**N
 for policy in range(4):
  prefixes=Counter()
  for word in product(range(2),repeat=N):
   remaining=list(range(N));seen=[];selected=[]
   for step in range(N):
    take=policy==0 or (policy==1 and (not seen or seen[-1]==1)) or (policy==2 and sum(seen)%3==0) or (policy==3 and step%3==0)
    index=remaining.pop(-1 if sum(seen)%2 else 0)
    bit=word[index]
    if take:selected.append(bit);prefixes[tuple(selected)]+=1
    seen.append(bit)
   cases+=1
  for w,c in prefixes.items():
   assert c*2**len(w)<=total
   assert prefixes[w+(0,)]==prefixes[w+(1,)]
  rows.append(dict(policy=policy,prefixes=len(prefixes),max_selected=max(map(len,prefixes))))
 r['adaptive_cylinders']=dict(histories=cases,source_length=N,rows=rows);save();print('PASS adaptive cylinders',cases,flush=True)
