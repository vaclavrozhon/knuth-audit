"""Exact checks of new §3.4.2 blocks; existing S/R checks are not rerun."""
from collections import Counter,deque
from fractions import Fraction as Q
from itertools import product
from math import comb,factorial
from pathlib import Path
import json,sys,time
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/sampling-extensions.json'

def binom(n,k):return comb(n,k) if 0<=k<=n else 0

def prefix_and_skips():
    prefixes=skips=0
    for N in range(1,33):
      for n in range(1,N+1):
        d={0:Q(1)}
        for t in range(N+1):
          for m in range(n+1):
            assert d.get(m,0)==Q(binom(t,m)*binom(N-t,n-m),comb(N,n))
            prefixes+=1
          if t<N:
            e=Counter()
            for m,p in d.items():
              take=Q(n-m,N-t);e[m]+=p*(1-take);e[m+1]+=p*take
            d={k:v for k,v in e.items() if v};assert sum(d.values())==1
    for N in range(1,41):
      for n in range(1,N+1):
        tails=[]
        for k in range(N-n+2):
          v=Q(1)
          for j in range(n):v*=Q(max(0,N-j-k),N-j)
          assert v==Q(binom(N-k,n),comb(N,n));tails.append(v)
        for x in range(N-n+1):
          mass=Q(comb(N-x-1,n-1),comb(N,n))
          assert mass==tails[x]-tails[x+1]
          U=(tails[x]+tails[x+1])/2;X=0;p=N-n;q=N;R=Q(p,q)
          while U<R:X+=1;p-=1;q-=1;R*=Q(p,q)
          assert X==x;skips+=1
    return dict(prefix_probabilities=prefixes,exact_skip_masses_and_inverse_intervals=skips)

def squeeze():
    probes=models=0;maxwork=Q(0)
    for N in range(2,49):
      for n in range(2,N+1):
        c=Q(N,N-n+1);work=Q(0)
        for k in range(N-n+1):
          f=Q(comb(N-k-1,n-1),comb(N,n))
          v=Q(n,N-k)
          for j in range(k):v*=Q(N-n-j,N-j)
          assert v==f
          eps=Q(k*n*(n-1),2*(N-n+1)*(N-k))
          L=max(Q(0),1-eps)/c
          for offset in [Q(0),Q(1,3),Q(2,3),Q(1)]:
            z=k+offset;g=Q(n,N)*(1-z/N)**(n-1)
            assert 0<=L<=f/(c*g)<=1,(N,n,k,z,L,f/(c*g))
            probes+=1
          pg=Q(N-k,N)**n-Q(N-k-1,N)**n
          work+=pg*k*(1-L)
        assert work < 2
        if 2*n<=N:
          assert c<2 and c*work<4;maxwork=max(maxwork,c*work)
        models+=1
    return dict(models=models,rational_squeeze_probes=probes,
                max_expected_expensive_product_factors=float(maxwork),
                note='Global inequalities proved in notes; probes independently confirm exact arithmetic at rational points.')

def shuffled(t,choices,reverse):
    p=list(range(t+1))
    for j in (range(t,1,-1) if reverse else range(2,t+1)):
        k=choices[j];p[j],p[k]=p[k],p[j]
    return tuple(p[1:])

def permutations_and_conversion():
    total=0;multisets=Counter()
    for t in range(1,9):
      seen=set();inside=set()
      for vals in product(*(range(1,j+1) for j in range(2,t+1))):
        a=[0,1]+list(vals);p=shuffled(t,a,True);assert p not in seen;seen.add(p)
        b=list(range(t+1))
        for j in range(2,t+1):b[j],b[a[j]]=b[a[j]],b[j]
        for j in range(t,1,-1):b[a[j]]=b[j]
        assert all(1<=b[j]<=j for j in range(1,t+1))
        assert shuffled(t,b,False)==p
        q=[0]*(t+1)
        for j in range(1,t+1):k=a[j];q[j]=q[k];q[k]=j
        assert tuple(q[1:]) not in inside;inside.add(tuple(q[1:]))
        if t==6:multisets[tuple((x-1)//2 for x in p)]+=1
        total+=1
      assert len(seen)==len(inside)==factorial(t)
    assert len(multisets)==90 and set(multisets.values())=={8}
    ratio=Q(factorial(13),2**32);assert Q(1445,1000)<ratio<Q(1455,1000)
    return dict(full_choice_vectors=total,largest_t=8,multiset_outputs=90,
                factorial13_over_2power32=str(ratio))

def dahl():
    vectors=steps=0
    for t in range(1,10):
      for n in range(1,t+1):
        if t>=8 and n>4:continue
        threshold=t-n
        for ks in product(*(range(1,j+1) for j in range(t,threshold,-1))):
          full=list(range(t+1));X={};Y={j:j for j in range(threshold+1,t+1)}
          for j,k in zip(range(t,threshold,-1),ks):
            assert all(full[h]==h or full[h]>j for h in range(1,j+1))
            if k>threshold:X[j]=Y[k];Y[k]=Y[j]
            else:
              prev=[i for i in X if i>j and X[i]==k];assert len(prev)<=1
              if prev:i=prev[0];X[j]=Y[i];Y[i]=Y[j]
              else:X[j]=k
            full[k],full[j]=full[j],full[k]
            assert X[j]==full[j]
            assert all(Y[h]==full[h] for h in range(threshold+1,j))
            for i in X:
              if X[i]<=threshold:assert Y[i]==full[X[i]]
            steps+=1
          assert tuple(X[h] for h in range(threshold+1,t+1))==tuple(full[threshold+1:])
          vectors+=1
    return dict(choice_vectors=vectors,invariant_checked_steps=steps)

def perfect_shuffle():
    total=0;rows=[]
    for m in range(3,32,2):
      n=(m+1)//2;initial=tuple(range(m));seen={initial};todo=deque([initial])
      while todo:
        d=todo.popleft();r=[]
        for i in range(n-1):r.extend([d[i],d[n+i]])
        r.append(d[n-1])
        for e in [tuple(r),d[1:]+d[:1]]:
          if e not in seen:seen.add(e);todo.append(e)
      powers=[];a=1
      while a not in powers:powers.append(a);a=2*a%m
      expected=set()
      for a in powers:
        for b in range(m):
          e=[0]*m
          for x in range(m):e[(a*x+b)%m]=x
          expected.add(tuple(e))
      assert seen==expected;assert len(seen)==m*len(powers)<=m*(m-1)
      total+=len(seen);rows.append([m,len(powers),len(seen)])
    return dict(groups=len(rows),arrangements=total,rows=rows)

def floyd():
    states=histories=0
    for N in range(1,13):
      for n in range(1,N+1):
        d={():1};r=0
        for j in range(N-n+1,N+1):
          e=Counter();r+=1
          for S,count in d.items():
            for k in range(1,j+1):
              new=tuple(sorted(S+((j if k in S else k),)))
              assert len(set(new))==r;e[new]+=count
          d=e
          assert len(d)==comb(j,r) and set(d.values())=={factorial(r)}
          states+=len(d)
        histories+=sum(d.values())
    return dict(intermediate_subsets=states,implicit_choice_histories=histories,max_N=12)

result=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
for name,fn in [('prefix_and_skips',prefix_and_skips),('squeeze',squeeze),('permutations_and_conversion',permutations_and_conversion),('dahl',dahl),('perfect_shuffle',perfect_shuffle),('floyd',floyd)]:
    if name in result:continue
    t=time.monotonic();r=fn();r['elapsed_seconds']=time.monotonic()-t;result[name]=r
    OUT.write_text(json.dumps(result,indent=2)+'\n');print('PASS',name,r,flush=True)
