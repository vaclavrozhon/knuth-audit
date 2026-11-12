"""Exact golden-ratio geometry for DLX136; no live-job modules modified."""
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations,product
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/dodeca136'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,data):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
@dataclass(frozen=True)
class Phi:
 a:F=F(0)
 b:F=F(0)
 def __post_init__(self):object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
 def __add__(self,y):
  y=coerce(y);return Phi(self.a+y.a,self.b+y.b)
 __radd__=__add__
 def __neg__(self):return Phi(-self.a,-self.b)
 def __sub__(self,y):return self+-coerce(y)
 def __rsub__(self,y):return coerce(y)+-self
 def __mul__(self,y):
  y=coerce(y);return Phi(self.a*y.a+self.b*y.b,self.a*y.b+self.b*y.a+self.b*y.b)
 __rmul__=__mul__
 def __truediv__(self,n):return Phi(self.a/n,self.b/n)
 def sign(self):
  a,b=2*self.a+self.b,self.b
  sg=lambda x:(x>0)-(x<0)
  if not a:return sg(b)
  if not b or a*b>0:return sg(a)
  return sg(a)*sg(a*a-5*b*b)
 def __float__(self):return float(self.a)+float(self.b)*(1+5**.5)/2
def coerce(x):return x if isinstance(x,Phi) else Phi(x)
PHI=Phi(0,1);ZERO=Phi();ONE=Phi(1)
def rotate(v):return v[2],v[0],v[1]
def power(v,a):
 for _ in range(a):v=rotate(v)
 return v
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),ZERO)
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
FACES=tuple(''.join(map(str,t)) for t in product(range(3),range(2),range(2)))
COORD={f:power((ZERO,(-1)**int(f[1])*PHI,Phi((-1)**int(f[2]))),int(f[0])) for f in FACES}
ADJ={f:tuple(g for g in FACES if dot(sub(COORD[f],COORD[g]),sub(COORD[f],COORD[g]))==Phi(4)) for f in FACES}
EDGES=tuple(sorted({tuple(sorted((f,g))) for f in FACES for g in ADJ[f]}))
MID={e:tuple(x/2 for x in add(COORD[e[0]],COORD[e[1]])) for e in EDGES}
EDGE_COORD={str(a)+str(b):power((ZERO,(-1)**b*PHI,ZERO),a) for a,b in product(range(3),range(2))}
EDGE_COORD.update({''.join(map(str,(a,b,cc,d))):power(tuple(x/2 for x in (Phi((-1)**b),(-1)**cc*PHI,(-1)**d*(PHI+1))),a) for a,b,cc,d in product(range(3),range(2),range(2),range(2))})
EDGE_NAME={e:next(name for name,v in EDGE_COORD.items() if v==mid) for e,mid in MID.items()}
def face_cycle(f):
 neighbors=ADJ[f];start=min(neighbors);nexts=[x for x in neighbors if x in ADJ[start]]
 assert len(nexts)==2
 nxt=next(x for x in nexts if det(COORD[f],sub(COORD[start],COORD[f]),sub(COORD[x],COORD[f])).sign()>0)
 result=[start,nxt]
 while len(result)<5:
  choices=[x for x in neighbors if x in ADJ[result[-1]] and x!=result[-2] and x not in result]
  assert len(choices)==1;result.append(choices[0])
 assert result[-1] in ADJ[start]
 return tuple(result)
CYCLES={f:face_cycle(f) for f in FACES}
def edges(f):return tuple(tuple(sorted((f,g))) for g in CYCLES[f])
def tile(word):
 rev=word[::-1];return min(w[j:]+w[:j] for w in (word,rev) for j in range(5))
WORDS=tuple(''.join(w) for w in permutations('01234'))
TILES=tuple(sorted({tile(w) for w in WORDS}))
def problem(anchor=True):
 rows=[];placements=[]
 for f in FACES:
  for word in WORDS:
   t=tile(word)
   if anchor and t=='01234' and (f!='000' or word!='01234'):continue
   rows.append([f,t]+[EDGE_NAME[e]+':'+color for e,color in zip(edges(f),word)]);placements.append((f,word))
 header=list(FACES)+list(TILES)+['|']+sorted(EDGE_COORD)
 return dict(header=header,rows=rows,placements=placements)
def text(enc):return ' '.join(enc['header'])+'\n'+'\n'.join(' '.join(r) for r in enc['rows'])+'\n'
def validate(vector):
 assert len(vector)==30 and set(vector)<=set('01234')
 colors=dict(zip(EDGES,vector));words={f:''.join(colors[e] for e in edges(f)) for f in FACES}
 assert all(set(w)==set('01234') for w in words.values())
 assert Counter(tile(w) for w in words.values())==Counter(TILES)
 assert Counter(vector)==Counter({x:6 for x in '01234'})
 return words
def normalize(vector):
 colors=dict(zip(EDGES,vector));word=''.join(colors[e] for e in edges('000'));mapping=dict(zip(word,'01234'))
 assert len(mapping)==5;return ''.join(mapping[x] for x in vector)
def matvec(m,v):return tuple(dot(row,v) for row in m)
def matrix(rows):return tuple(tuple(coerce(x) for x in row) for row in rows)
D0=matrix([[-1,0,0],[0,1,0],[0,0,1]])
D1=matrix([[1,0,0],[0,-1,0],[0,0,1]])
D2=matrix([[1,0,0],[0,1,0],[0,0,-1]])
P=matrix([[0,0,1],[1,0,0],[0,1,0]])
Q=tuple(tuple(x/2 for x in row) for row in matrix([[1,-PHI,PHI-1],[PHI,PHI-1,-1],[PHI-1,1,PHI]]))
OLD_Q=tuple(tuple(x/2 for x in row) for row in matrix([[-1,-PHI,PHI-1],[-PHI,PHI-1,-1],[PHI-1,-1,-PHI]]))
def face_permutation(m):
 lookup={v:f for f,v in COORD.items()};return tuple(FACES.index(lookup[matvec(m,COORD[f])]) for f in FACES)
def generated_group(generators):
 todo=[tuple(range(12))];seen=set(todo)
 for p in todo:
  for q in generators:
   r=tuple(q[p[i]] for i in range(12))
   if r not in seen:seen.add(r);todo.append(r)
 return tuple(sorted(seen))
def transform(vector,p):
 d={tuple(sorted((FACES[p[FACES.index(a)]],FACES[p[FACES.index(b)]]))):color for (a,b),color in zip(EDGES,vector)}
 return ''.join(d[e] for e in EDGES)
assert len(EDGES)==len(EDGE_COORD)==30 and all(len(a)==5 for a in ADJ.values()) and len(TILES)==12
