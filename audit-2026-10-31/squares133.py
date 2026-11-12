"""DLX133: cyclic square tiles and the exact white-boundary rectangle.

Cells (x,y),0<=x<6,0<=y<4. Edge colors are bottom,right,top,left.
No import-time search; existing live jobs and modules remain unchanged.
"""
from collections import Counter
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import difflib,json,shutil,subprocess,tempfile
from puzzle_xcc import sha,save

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/squares133'
CELLS=tuple(product(range(6),range(4)))
WORDS=tuple(''.join(c) for c in product('abc',repeat=4))
def tile(s):return min(s[i:]+s[:i] for i in range(4))
TILES=tuple(sorted({tile(s) for s in WORDS}))
ANCHOR=((0,0),(1,0),(2,0),(0,1))
def edges(x,y):return (('h',x,y),('v',x+1,y),('h',x,y+1),('v',x,y))
EDGES=tuple(sorted({e for x,y in CELLS for e in edges(x,y)}))
BOUNDARY=tuple(e for e in EDGES if (e[0]=='h' and e[2] in (0,4)) or (e[0]=='v' and e[1] in (0,6)))
def edge_name(e):return ''.join(map(str,e))
def swapped(s):return s.translate(str.maketrans('bc','cb'))
def color_key(s):return min(s,swapped(s))

def problem(anchor=True,white=True):
 rows=[]; placements=[]
 for x,y in CELLS:
  for cs in WORDS:
   name=tile(cs)
   if anchor and name=='aaaa' and (x,y) not in ANCHOR:continue
   if white and any(e in BOUNDARY and c!='a' for e,c in zip(edges(x,y),cs)):continue
   rows.append([f'{x}{y}',name]+[edge_name(e)+':'+c for e,c in zip(edges(x,y),cs)])
   placements.append((x,y,cs))
 header=[f'{x}{y}' for x,y in CELLS]+list(TILES)+['|']+[edge_name(e) for e in EDGES]
 return dict(header=header,rows=rows,placements=placements,anchored=anchor,white=white)

def text(enc):return ' '.join(enc['header'])+'\n'+'\n'.join(' '.join(r) for r in enc['rows'])+'\n'

def validate(vector):
 """Geometric endpoint matching and inventory, independent of XCC item names."""
 assert len(vector)==len(EDGES) and set(vector)<=set('abc')
 colors=dict(zip(EDGES,vector)); inventory=[]; cells={}; geometric={}
 for x,y in CELLS:
  cs=''.join(colors[e] for e in edges(x,y));inventory.append(tile(cs));cells[x,y]=cs
  vertices=((x,y),(x+1,y),(x+1,y+1),(x,y+1))
  for j,c in enumerate(cs):
   e=tuple(sorted((vertices[j],vertices[(j+1)%4])))
   assert e not in geometric or geometric[e]==c
   geometric[e]=c
   if all(v[0] in (0,6) for v in e) or all(v[1] in (0,4) for v in e):assert c=='a'
 assert Counter(inventory)==Counter(TILES)
 assert all(colors[e]=='a' for e in BOUNDARY)
 assert len(geometric)==58
 return cells

def transform(vector,flipx=False,flipy=False,swap=False):
 colors={}
 for e,c in zip(EDGES,vector):
  typ,x,y=e
  if flipx:x=(5-x if typ=='h' else 6-x)
  if flipy:y=(4-y if typ=='h' else 3-y)
  colors[typ,x,y]=swapped(c) if swap else c
 return ''.join(colors[e] for e in EDGES)

def build():
 """Fresh122 derivative sets CTH for four-letter square tile items."""
 target=OUT/'build';target.mkdir(parents=True,exist_ok=True)
 manifest=target/'build.json'
 assert not manifest.exists(),'No rebuild without inspecting existing evidence.'
 base=ROOT/'results/symmetry121_123/native/dlx2-symmetry122.w'
 old=base.read_text();needle='  @<Input the options@>;'
 assert old.count(needle)==1
 code=old.replace(needle,needle+'''
  for (i=1;i<second;i++) {
    if (strlen(cl[i].name)==4 && strspn(cl[i].name,"abc")==4) {
      cl[i].cth='a';
      for (j=0;j<4;j++) if (cl[i].name[j]>=cl[i].cth)
        cl[i].cth=cl[i].name[j]+1;
    }
  }''')
 source=target/'dlx2-squares133.w';source.write_text(code)
 (target/'dlx2-squares133.patch').write_text(''.join(difflib.unified_diff(old.splitlines(True),code.splitlines(True),fromfile=base.name,tofile=source.name)))
 directory=Path(tempfile.mkdtemp(prefix='knuth-vol4b-squares133-native-'))
 sources={}
 for p in [source,*[ROOT/'sources/knuth-programs'/n for n in ['gb_flip.w','gb_flip.ch','boilerplate.w']]]:
  shutil.copy2(p,directory/p.name);sources[str(p.relative_to(ROOT))]=sha(p)
 commands=[['ctangle','gb_flip.w','gb_flip.ch'],['ctangle',source.name],['cc','-O2','-Wno-implicit-int','-Wno-implicit-function-declaration','dlx2-squares133.c','gb_flip.c','-o','dlx2-squares133']]
 with (target/'build.log').open('w') as f:
  for cmd in commands:subprocess.run(cmd,cwd=directory,stdout=f,stderr=f,check=True)
 binary=directory/'dlx2-squares133'
 result=dict(at_utc=datetime.now(timezone.utc).isoformat(),base=str(base.relative_to(ROOT)),base_sha256=sha(base),source=str(source),source_sha256=sha(source),builder_sha256=sha(__file__),sources=sources,commands=commands,binary=str(binary),binary_sha256=sha(binary))
 save(manifest,result);return result
