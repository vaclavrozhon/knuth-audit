from itertools import combinations
import json

def check(m,n,off):
 V=set(range(m*n));neigh={v:{w for w in (v-n,v+n,v-1,v+1) if 0<=w<m*n and abs(w//n-v//n)+abs(w%n-v%n)==1} for v in V}
 B={v for v in V if (v//n+2*(v%n)-off)%5==0};W=V-B
 cand=sorted(v for v in W if not (neigh[v]&B))
 def conn(S):
  if not S:return False
  seen={next(iter(S))};todo=list(seen)
  while todo:
   for w in neigh[todo.pop()]&S-seen:seen.add(w);todo.append(w)
  return len(seen)==len(S)
 initial_artics=[v for v in cand if not conn(W-{v})]
 for k in range(len(cand)+1):
  solutions=[]
  for add in combinations(cand,k):
   extra=set(add);bb=B|extra;ww=V-bb
   if any(neigh[v]&extra for v in extra) or not conn(ww):continue
   if all(neigh[v]&bb or not conn(ww-{v}) for v in ww):solutions.append(add)
  if solutions:return dict(m=m,n=n,offset=off,initial=len(B),candidate_count=len(cand),candidates=[divmod(v,n) for v in cand],initial_artics=initial_artics,extra=k,minimum=len(B)+k,claimed=m*n/5+2,witness=[divmod(v,n) for v in solutions[0]])
if __name__=='__main__':
 for off in range(5):print(json.dumps(check(7,7,off)),flush=True)
