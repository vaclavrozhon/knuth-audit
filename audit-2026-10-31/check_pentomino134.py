"""Exact134 component census on the complete133 solution representatives."""
from collections import Counter
from datetime import datetime,timezone
import gzip,json
import squares133 as s
from check_pentomino_bipairs import SHAPES,orientations,normalized
LOOKUP={q:k for k,v in SHAPES.items() for q in orientations(v)}

def regions(vector):
 # Midpoint lattice rotated45 degrees: every matched nonwhite edge is one square.
 cells={}
 for (kind,x,y),color in zip(s.EDGES,vector):
  if color=='a':continue
  u,v=(x+y,x-y) if kind=='h' else (x+y,x-y-1)
  assert (u,v) not in cells;cells[u,v]=color
 assert Counter(cells.values())==Counter(b=16,c=16)
 unseen=set(cells);result=[]
 while unseen:
  start=min(unseen);unseen.remove(start);todo=[start];component={start};color=cells[start]
  while todo:
   x,y=todo.pop()
   for q in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
    if q in unseen and cells[q]==color:unseen.remove(q);component.add(q);todo.append(q)
  result.append(dict(color=color,size=len(component),type=LOOKUP[normalized(component)] if len(component)==5 else None,cells=sorted(component)))
 return result

def half_wedge_regions(vector):
 # A separate graph on individual triangular quarters. Internal tile adjacencies
 # and shared rectangle sides are united directly, before collapsing pairs.
 colors=dict(zip(s.EDGES,vector));nodes={}
 for x,y in s.CELLS:
  for d,e in enumerate(s.edges(x,y)):
   if colors[e]!='a':nodes[x,y,d]=colors[e]
 parent={n:n for n in nodes}
 def find(a):
  while parent[a]!=a:parent[a]=parent[parent[a]];a=parent[a]
  return a
 def union(a,b):
  if b in nodes and nodes[a]==nodes[b]:parent[find(a)]=find(b)
 for x,y,d in nodes:
  a=(x,y,d);union(a,(x,y,(d+1)%4));union(a,(x,y,(d-1)%4))
  dx,dy=((0,-1),(1,0),(0,1),(-1,0))[d];union(a,(x+dx,y+dy,(d+2)%4))
 groups={}
 for a in nodes:groups.setdefault(find(a),[]).append(a)
 result=[]
 for group in groups.values():
  squares=set()
  for x,y,d in group:
   kind,u,v=s.edges(x,y)[d]
   squares.add((u+v,u-v) if kind=='h' else (u+v,u-v-1))
  assert len(group)==2*len(squares)
  result.append((nodes[group[0]],tuple(sorted(squares))))
 return sorted(result)

def main():
 path=s.OUT/'native/canonical-colors.txt.gz'
 with gzip.open(path,'rt') as f:vectors=f.read().splitlines()
 assert len(vectors)==len(set(vectors))==13328
 counts=Counter();distribution=Counter();duplicates=Counter();examples=[];presence=Counter();color_presence=Counter();same_color_duplicates=Counter();duplicate_witnesses={}
 for v in vectors:
  regs=regions(v);cs=Counter(r['type'] for r in regs if r['type'])
  counts.update(cs);presence.update(cs.keys());distribution[sum(cs.values())]+=1
  alternate=half_wedge_regions(v)
  assert sorted((r['color'],tuple(r['cells'])) for r in regs)==alternate
  for color in ['b','c']:
   each=Counter(r['type'] for r in regs if r['color']==color and r['type']);color_presence.update(each.keys())
   for name,n in each.items():
    if n>1:
     same_color_duplicates[name]+=1
     duplicate_witnesses.setdefault(name,dict(colors=v,color=color,type=name,regions=regs))
  for k,n in cs.items():
   if n>1:duplicates[k]+=1
  if sum(cs.values())==4:examples.append(dict(colors=v,regions=regs))
 expected=dict(zip('OPQRSTUVWXYZ',[0,1672,22,729,402,61,36,48,174,259,242,0]))
 actual={k:counts[k] for k in expected}
 assert actual==dict(expected,P=1685,Y=243)
 assert dict(same_color_duplicates)==dict(P=54)
 assert max(distribution)==4 and distribution[4]==1
 structure=json.loads((s.OUT/'structure-checked.json').read_text());figure=regions(structure['figure']['colors'])
 assert sorted(r['type'] for r in figure if r['color']=='b' and r['type'])==['S']
 assert sorted(r['type'] for r in figure if r['color']=='c' and r['type'])==['P','V']
 result=dict(at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=s.sha(__file__),shape_source_sha256=s.sha(s.ROOT/'check_pentomino_bipairs.py'),model_sha256=s.sha(s.__file__),colors_sha256=s.sha(path),solutions=13328,counts=actual,book_counts=expected,per_color_presence={k:color_presence[k] for k in expected},per_solution_presence={k:presence[k] for k in expected},same_color_repeats=dict(same_color_duplicates),duplicate_witnesses=duplicate_witnesses,independent_half_wedge_components_checked=True,number_of_pentominoes_distribution=dict(sorted(distribution.items())),solutions_with_repeated_type=dict(duplicates),four_pentomino_witness=examples[0],original_figure_regions=figure,structure_sha256=s.sha(s.OUT/'structure-checked.json'))
 s.save(s.OUT/'pentomino134-checked.json',result)
 print('PASS134 independent component census: occurrence P1685/Y243 vs book P1672/Y242. Presence conventions also differ; printed S/P/V verified.')

if __name__=='__main__':main()
