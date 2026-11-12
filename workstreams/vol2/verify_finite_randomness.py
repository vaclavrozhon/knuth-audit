"""Finite definitionsQ1/Q2: exhaustive tables and constructive certificates."""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as F
import argparse,json
P=Path(__file__).resolve().parent;OUT=P/'results/finite-randomness.json'
a=argparse.ArgumentParser();a.add_argument('--resume',action='store_true');args=a.parse_args()
r=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}
def save():OUT.write_text(json.dumps(r,indent=2)+'\n')
def q1(w,b):
 N=len(w);k=1
 while b**k<=N:
  c=Counter(tuple(w[j:j+k]) for j in range(N-k+1));den=b**k
  for x in product(range(b),repeat=k):
   if (c[x]*den-N)**2>N*den*den:return False
  k+=1
 return True
if 'tables' not in r:
 listed='''00000001111 10000000111 11000000011 11100000001 11110000000
00000001110 10000000110 11000000010 11100000000 11010000000
00000001101 10000000101 11000000001 10100000001 10110000000
00000001011 10000000011 01000000011 01100000001 01110000000
00000000111'''.split()
 comp=lambda w:''.join('1' if c=='0' else '0' for c in w)
 base=set(listed)|{'01010101010'}|{''.join(map(str,w)) for w in product((0,1),repeat=11) if sum(w)<=2}
 published=base|set(map(comp,base));actual={''.join(map(str,w)) for w in product((0,1),repeat=11) if not q1(w,2)}
 assert len(listed)==21 and len(actual)==178 and actual==published
 listed2='''00001011 00101001 01001110 01101000
00011010 00101100 01011011 01101100
00011011 00110010 01011110 01101101
00100011 00110011 01100010 01110010
00100110 00110110 01100011 01110110
00100111 00111001 01100110'''.split()
 good=[]
 for w in product((0,1),repeat=8):
  choices=[w,w[::2],tuple(w[j] for j in range(1,8) if w[j-1]==0),tuple(w[j] for j in range(1,8) if w[j-1]==1)]
  if all(len(v)<4 or abs(F(sum(v),len(v))-F(1,2))<=F(1,8) for v in choices):good.append(''.join(map(str,w)))
 assert set(good)==set(listed2)|set(map(comp,listed2)) and len(good)==46
 example=tuple(map(int,'00010001000'));N=len(example)
 assert abs(F(sum(example),N)-F(1,2))**2>F(1,N)
 assert all((F(Counter(example[j:j+2] for j in range(N-1))[x],N)-F(1,4))**2<=F(1,N) for x in product((0,1),repeat=2))
 r['tables']=dict(Q1_total_words=2048,Q1_nonrandom=178,Q1_printed=sorted(published),Q2_total_words=256,Q2_random=46,Q2_good=good,finite_distribution_nonmonotonic_example='00010001000')
 save();print('PASS Q1/Q2 tables',flush=True)
if 'q1_construction' not in r:
 def db(b,k):
  a=[0]*(b*k+1);out=[]
  def rec(t,p):
   if t>k:
    if k%p==0:out.extend(a[1:p+1])
   else:
    a[t]=a[t-p];rec(t+1,p)
    for j in range(a[t-p]+1,b):a[t]=j;rec(t+1,t)
  rec(1,1);return out
 periods={};cases=0;largest=0
 for b in range(2,11):
  for N in range(1,513):
   if N<b:assert q1([0]*N,b);cases+=1;continue
   k=0;period_length=1
   while period_length**2<N:k+=1;period_length*=b
   if (b,k) not in periods:
    cycle=db(b,k);L=len(cycle);assert L==b**k
    count=Counter(tuple(cycle[(i+j)%L] for j in range(k)) for i in range(L))
    assert len(count)==L and set(count.values())=={1};periods[b,k]=cycle
   cycle=periods[b,k];word=[cycle[i%len(cycle)] for i in range(N)]
   assert q1(word,b),(b,N,k)
   cases+=1;largest=max(largest,len(cycle))
 r['q1_construction']=dict(alphabet_range=[2,10],length_range=[1,512],words_checked=cases,periods_checked=len(periods),largest_period=largest,note='General proof uses any deBruijn period P with sqrt(N)<=P<b*sqrt(N). Generator here is FKM; Rees existence was proved in prior block.')
 save();print('PASS Q1 construction',cases,flush=True)
if 'q2_hitting' not in r:
 cases=0;rows=[]
 for N in range(1,11):
  for n in range(1,N+1):
   for eps in [F(0),F(1,8),F(1,4)]:
    def bad(m,h):return m>=n and abs(F(h,m)-F(1,2))>eps
    direct=sum(any(bad(m,sum(w[:m])) for m in range(n,N+1)) for w in product((0,1),repeat=N))
    alive={0:1};hit=0
    for m in range(1,N+1):
     new=Counter()
     for h,c in alive.items():
      for v in [0,1]:
       if bad(m,h+v):hit+=c*2**(N-m)
       else:new[h+v]+=c
     alive=new
    assert direct==hit
    rows.append(dict(N=N,n=n,epsilon=str(eps),rejecting_words=hit,total=2**N));cases+=1
 r['q2_hitting']=dict(cases=cases,rows=rows,meaning='Exact maximum rejection probability of one adaptive algorithm, by selected-fresh-bit coupling and first-hit stopping proof.')
 save();print('PASS Q2 exact stopping probabilities',cases,flush=True)
if 'q2_cover' not in r:
 from functools import lru_cache
 from math import comb
 rows=[];witness_checks=0
 for N in range(1,5):
  for n in range(1,N+1):
   for eps in [F(0),F(1,4)]:
    def bad(m,h):return m>=n and abs(F(h,m)-F(1,2))>eps
    @lru_cache(None)
    def lift(mask,q,i,v):
     out=0
     for x in range(1<<q):
      y=(x&((1<<i)-1))|((x>>(i+1))<<i)
      if (x>>i)&1==v and (mask>>y)&1:out|=1<<x
     return out
    @lru_cache(None)
    def rejection_sets(q,m,h):
     if bad(m,h):return {(1<<(1<<q))-1:None}
     if not q:return {0:None}
     candidates={}
     for i in range(q):
      for include in (0,1):
       left=rejection_sets(q-1,m+include,h)
       right=rejection_sets(q-1,m+include,h+include)
       for a in left:
        lo=lift(a,q,i,0)
        for b in right:
         mask=lo|lift(b,q,i,1)
         candidates.setdefault(mask,(i,include,a,b))
     maximal={}
     for mask in sorted(candidates,key=int.bit_count,reverse=True):
      if not any(mask&~sup==0 for sup in maximal):maximal[mask]=candidates[mask]
     return maximal
    masks=rejection_sets(N,0,0);full=(1<<(1<<N))-1
    for mask in masks:
     actual=0
     for x in range(1<<N):
      unread=list(range(N));m=h=0;current=mask
      while True:
       w=rejection_sets(len(unread),m,h)[current]
       if w is None:break
       i,include,a,b=w;v=(x>>unread.pop(i))&1
       m+=include;h+=include*v;current=(a,b)[v]
      if bad(m,h):actual|=1<<x
      witness_checks+=1
     assert actual==mask
    maxsize=max(map(int.bit_count,masks))
    direct=next(z['rejecting_words'] for z in r['q2_hitting']['rows'] if z['N']==N and z['n']==n and z['epsilon']==str(eps))
    assert maxsize==direct
    union=0
    for mask in masks:union|=mask
    possible=eps<min(F(1,2),F((N+1)//2,n)-F(1,2))
    assert (union==full)==possible
    solution=None;minimum=None
    if possible:
     bypoint=[[mask for mask in masks if (mask>>x)&1] for x in range(1<<N)]
     @lru_cache(None)
     def cover(uncovered,k):
      if uncovered==0:return ()
      if k==0 or uncovered.bit_count()>k*maxsize:return None
      pivot=min((x for x in range(1<<N) if (uncovered>>x)&1),key=lambda x:len(bypoint[x]))
      for mask in sorted(bypoint[pivot],key=lambda z:(z&uncovered).bit_count(),reverse=True):
       tail=cover(uncovered&~mask,k-1)
       if tail is not None:return (mask,)+tail
      return None
     for minimum in range(((1<<N)+maxsize-1)//maxsize,comb(N,n)+1):
      solution=cover(full,minimum)
      if solution is not None:break
     assert solution is not None
     union=0
     for z in solution:union|=z
     assert union==full
    rows.append(dict(N=N,n=n,epsilon=str(eps),maximal_rejection_sets=len(masks),maximum_rejected=maxsize,minimum_cover=minimum,cover_masks=solution,all_maximal_masks=sorted(masks)))
 r['q2_cover']=dict(cases=len(rows),independent_witness_checks=witness_checks,rows=rows,note='Complete adaptive query-tree recurrence with inclusion pruning; each retained witness evaluated independently on every input. None means no covering family exists.')
 save();print('PASS Q2 exact minimum covers',len(rows),witness_checks,flush=True)
