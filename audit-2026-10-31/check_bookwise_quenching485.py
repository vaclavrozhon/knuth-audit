"""Check a five-vertex witness and its fixed card variant; no graph census."""
import json
from pathlib import Path
from time import perf_counter
start=perf_counter()
root=Path(__file__).resolve().parent
edges={frozenset(e) for e in [(1,5),(2,3),(2,5),(4,5)]}
def adjacent(a,b):return frozenset((a,b)) in edges
def moves(v):
 for k in range(len(v)-1):
  if adjacent(v[k],v[k+1]):yield ('q',k+1),v[:k]+v[k+1:]
 for k in range(len(v)-3):
  if adjacent(v[k],v[k+3]):yield ('s',k+1),v[:k]+(v[k+3],)+v[k+1:k+3]+v[k+4:]
def wins(v,path=()):
 if len(v)==1:return [path]
 return [p for m,w in moves(v) for p in wins(w,path+(m,))]
def forbidden(path,guarded):
 v=(1,2,3,4,5)
 for t,m in enumerate(path):
  if t+1<len(path) and m[0]=='q' and path[t+1][0]=='s':
   l=path[t+1][1]
   if m[1]==l+3 and (not guarded or adjacent(v[l-1],v[l+2])):return True
  v=next(w for move,w in moves(v) if move==m)
 return False
paths=wins((1,2,3,4,5))
assert paths==[(('q',4),('s',1),('q',1),('q',1))]
assert all(forbidden(p,False) for p in paths)
assert not any(forbidden(p,True) for p in paths)
out={'scope':'Two fixed five-vertex graphs only','edges':sorted(sorted(e) for e in edges),'initial_moves':[list(m) for m,v in moves((1,2,3,4,5))],'winning_sequences':paths,'survivors_with_printed_unconditional_clause':sum(not forbidden(p,False) for p in paths),'survivors_with_missing_edge_guard':sum(not forbidden(p,True) for p in paths)}
cards=[('A','H'),('K','H'),('K','C'),('Q','D'),('Q','H')]
edges={frozenset((i+1,j+1)) for i in range(5) for j in range(i+1,5) if cards[i][0]==cards[j][0] or cards[i][1]==cards[j][1]}
card_paths=wins((1,2,3,4,5))
assert card_paths==paths
assert all(forbidden(p,False) and not forbidden(p,True) for p in card_paths)
out['card_variant']={'cards':[''.join(c) for c in cards],'edges':sorted(sorted(e) for e in edges),'winning_sequences':card_paths,'printed_clause_eliminates_all':True,'guarded_clause_preserves_solution':True}
out['seconds']=perf_counter()-start
(root/'results/bookwise-quenching485-fixed-graph.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
