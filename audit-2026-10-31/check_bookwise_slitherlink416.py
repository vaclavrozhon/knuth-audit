"""Check only two small counterexamples to the finite bounds in answer416."""
import json

def solve(n,clues):
 edges=[]
 for i in range(n+1):
  for j in range(n+1):
   if i<n:edges.append(((i,j),(i+1,j)))
   if j<n:edges.append(((i,j),(i,j+1)))
 vertices=[(i,j) for i in range(n+1) for j in range(n+1)]
 groups=[([k for k,e in enumerate(edges) if v in e],{0,2}) for v in vertices]
 borders={}
 for i in range(n):
  for j in range(n):
   corners={(i,j),(i+1,j),(i,j+1),(i+1,j+1)}
   borders[i,j]=[k for k,e in enumerate(edges) if set(e)<=corners]
 for cell,value in clues.items():groups.append((borders[cell],{value}))
 answers=[];visits=0
 def search(values):
  nonlocal visits
  visits+=1
  while True:
   forced={}
   for inds,allowed in groups:
    ones=sum(values[k]==1 for k in inds);unknown=[k for k in inds if values[k]<0]
    targets={x for x in allowed if ones<=x<=ones+len(unknown)}
    if not targets:return
    if not unknown:continue
    if targets=={ones}:value=0
    elif targets=={ones+len(unknown)}:value=1
    else:continue
    for k in unknown:
     if k in forced and forced[k]!=value:return
     forced[k]=value
   if not forced:break
   for k,v in forced.items():values[k]=v
  if -1 not in values:
   chosen=[e for k,e in enumerate(edges) if values[k]==1]
   if not chosen:return
   reached={chosen[0][0]}
   while True:
    new=reached|{v for e in chosen if set(e)&reached for v in e}
    if new==reached:break
    reached=new
   if reached==set(v for e in chosen for v in e):answers.append(chosen)
   return
  k=next(k for k,v in enumerate(values) if v<0)
  for value in [0,1]:
   nxt=values.copy();nxt[k]=value;search(nxt)
 search([-1]*len(edges))
 return {'n':n,'clues':[[*c,v] for c,v in clues.items()],'solutions':answers,'search_nodes':visits,'total_edges':len(edges)}

three=solve(3,{(i,j):3 for i in [0,2] for j in range(3)})
zero=solve(2,{(0,0):0})
assert len(three['solutions'])==len(zero['solutions'])==1
assert len(three['clues'])==6>3**2/2
zero['edges_removed_by_zero']=4
assert 4<2**2+2*2
print(json.dumps({'three_clue_counterexample':three,'zero_clue_counterexample':zero},indent=2))
