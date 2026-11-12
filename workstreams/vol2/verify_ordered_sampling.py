"""Finite exact ordered-hash sampling checks; no independence approximation."""
from pathlib import Path
from itertools import permutations,combinations
from fractions import Fraction as F
from math import comb
import argparse,json,time
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/ordered-sampling.json'
parser=argparse.ArgumentParser();parser.add_argument('--resume',action='store_true');args=parser.parse_args()
res=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}
def save(): OUT.write_text(json.dumps(res,indent=2)+'\n')
def insert(t,x,N):
    M=len(t);i=M*(x-1)//N;probes=0
    while True:
        probes+=1
        if t[i]==x:return probes,False
        if t[i]==0:t[i]=x;return probes,True
        if x>t[i]:x,t[i]=t[i],x
        i=(i-1)%M

def canonical(S,M,N):
    # Independent model: ordinary insertion, largest keys first.
    t=[0]*M
    for x in sorted(S,reverse=True):
        i=M*(x-1)//N
        while t[i]:i=(i-1)%M
        t[i]=x
    return t

def output(t):
    if not t[0]:return [x for x in t[1:] if x]
    return [x for x in t[1:] if 0<x<t[0]]+[x for x in t if x>=t[0]]

if 'histories' not in res:
    histories=states=queries=0
    for N in range(2,10):
      for n in range(1,N//2+1):
        M=2*n
        for seq in permutations(range(1,N+1),n):
          t=[0]*M;S=set();histories+=1
          for x in seq:
            probes,added=insert(t,x,N);assert added;S.add(x);states+=1
            assert t==canonical(S,M,N)
            assert output(t)==sorted(S)
          for x in range(1,N+1):
            if x in S:
              copy=t[:];_,added=insert(copy,x,N);assert not added and copy==t;queries+=1
    res['histories']=dict(complete_histories=histories,prefix_states=states,duplicate_queries=queries,N_max=9);save();print('PASS histories',res['histories'],flush=True)

if 'expected_probes' not in res:
    rows=[];states=queries=0;max_total=(F(0),None);max_stage=(F(0),None)
    for N in range(2,21):
      for n in range(1,min(N//2,7)+1):
        M=2*n;stages=[];total=F(0)
        for k in range(n):
          sums=0;cnt=0
          for S in combinations(range(1,N+1),k):
            t=canonical(S,M,N);assert output(t)==list(S);cnt+=1;states+=1
            for x in range(1,N+1):
              copy=t[:];probes,added=insert(copy,x,N);queries+=1;sums+=probes
              assert added==(x not in S)
          assert cnt==comb(N,k)
          # Retry duplicates, which do not mutate the state. Uniform k-subset.
          value=F(sums,comb(N,k)*(N-k));total+=value;stages.append(str(value))
          if value>max_stage[0]:max_stage=(value,(N,n,k))
        assert total<F(5,2)*n,(N,n,total)
        if total/n>max_total[0]:max_total=(total/n,(N,n))
        rows.append(dict(N=N,n=n,stage_costs=stages,total=str(total),total_per_output=str(total/n)))
      print('N',N,'states',states,'queries',queries,flush=True)
    res['expected_probes']=dict(models=len(rows),rows=rows,states=states,queries=queries,max_total_per_output=[str(max_total[0]),max_total[1]],max_stage=[str(max_stage[0]),max_stage[1]],scope='Exact finite N<=20,n<=min(N/2,7); general 5n/2 bound not inferred from census.');save();print('PASS expected probes',res['expected_probes']['max_total_per_output'],res['expected_probes']['max_stage'],flush=True)
