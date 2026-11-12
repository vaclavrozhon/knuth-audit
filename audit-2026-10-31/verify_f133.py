"""Standalone lower-bound certificate for the P/Y discrepancy in DLX134.

Only Python's standard library is required. No enumeration solver, shared
geometry module, or pentomino classifier is imported. The certified legal,
inequivalent tilings already contain more P/Y components than the book allows.
"""
from collections import Counter
from pathlib import Path
from itertools import product
import gzip,hashlib,json

ROOT=Path(__file__).resolve().parent
PATH=ROOT/'results/squares133/f133-witnesses.json.gz'

def canonical_shape(cells):
 variants=[]
 for mirror in (1,-1):
  for r in range(4):
   q=[]
   for x,y in cells:
    x*=mirror
    for _ in range(r):x,y=-y,x
    q.append((x,y))
   mx=min(x for x,y in q);my=min(y for x,y in q)
   variants.append(tuple(sorted((x-mx,y-my) for x,y in q)))
 return min(variants)

P=canonical_shape([(0,0),(0,1),(1,0),(1,1),(2,0)])
Y=canonical_shape([(0,0),(1,0),(2,0),(3,0),(1,1)])
def neck(cs):return min(cs[i:]+cs[:i] for i in range(4))

def verify(data):
 edges=sorted([('h',x,y) for x in range(6) for y in range(5)]+[('v',x,y) for x in range(7) for y in range(4)])
 types={neck(cs) for cs in product('abc',repeat=4)}
 assert data['edge_order']==[list(e) for e in edges]
 keys=set();counts=Counter();per_tiling=[]
 for vector in data['vectors']:
  assert len(vector)==58 and set(vector)<=set('abc')
  color=dict(zip(edges,vector));pieces=[];graph={}
  for x in range(6):
   for y in range(4):
    cs=(color['h',x,y],color['v',x+1,y],color['h',x,y+1],color['v',x,y]);pieces.append(neck(cs))
  assert len(set(pieces))==24 and set(pieces)==types
  assert all(c=='a' for (t,x,y),c in color.items() if (t=='h' and y in (0,4)) or (t=='v' and x in (0,6)))
  # These transformations act on geometric endpoints, not tile names.
  orbit=[]
  for fx,fy,swap in product((False,True),repeat=3):
   transformed={}
   for (t,x,y),c in color.items():
    u,v=((x,y),(x+1,y)) if t=='h' else ((x,y),(x,y+1))
    u=tuple((6-u[0] if fx else u[0],4-u[1] if fy else u[1]));v=tuple((6-v[0] if fx else v[0],4-v[1] if fy else v[1]));u,v=sorted((u,v))
    e=('h',*u) if u[1]==v[1] else ('v',*u)
    transformed[e]=({'b':'c','c':'b'}.get(c,c) if swap else c)
   orbit.append(''.join(transformed[e] for e in edges))
  key=min(orbit);assert key not in keys;keys.add(key)
  # Individual half-diamonds are joined through shared sides and within tiles.
  for x in range(6):
   for y in range(4):
    local=[('h',x,y),('v',x+1,y),('h',x,y+1),('v',x,y)]
    for j,e in enumerate(local):
     if color[e]=='a':continue
     graph.setdefault(e,set())
     for k in [(j-1)%4,(j+1)%4]:
      f=local[k]
      if color[f]==color[e]:graph[e].add(f)
  unseen=set(graph);record=Counter()
  while unseen:
   first=min(unseen);unseen.remove(first);component={first};stack=[first]
   while stack:
    for q in graph[stack.pop()]:
     if q in unseen:unseen.remove(q);component.add(q);stack.append(q)
   if len(component)!=5:continue
   xy=[]
   for t,x,y in component:
    xx,yy=(2*x+1,2*y) if t=='h' else (2*x,2*y+1)
    xy.append(((xx+yy-1)//2,(xx-yy-1)//2))
   shape=canonical_shape(xy)
   if shape==P:record['P']+=1
   if shape==Y:record['Y']+=1
  counts.update(record);per_tiling.append(dict(record))
 assert counts==Counter(P=1685,Y=243),counts
 assert counts['P']>1672 and counts['Y']>242
 return dict(distinct_valid_tilings=len(keys),certified_occurrences=dict(counts),book_occurrences=dict(P=1672,Y=242),lower_bound_refutes_book=True,exhaustive_search_required_for_refutation=False)

def main():
 with gzip.open(PATH,'rt') as f:data=json.load(f)
 result=verify(data)
 result.update(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),certificate_sha256=hashlib.sha256(PATH.read_bytes()).hexdigest())
 (PATH.parent/'f133-lower-bound-checked.json').write_text(json.dumps(result,indent=2)+'\n')
 print('PASS F133 independent lower bound:',result['distinct_valid_tilings'],'legal inequivalent tilings contain1685 P and243 Y.')

if __name__=='__main__':main()
