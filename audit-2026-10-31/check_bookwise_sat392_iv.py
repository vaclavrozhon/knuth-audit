"""Check the fixed printed grid and its one-cell correction; no puzzle search."""
import json
from pathlib import Path
root=Path(__file__).resolve().parent
grid='''GGGGGHAAAAAAACCCCC
GFFFGHACCCCCCCEEEC
GFBFGHACEEEEEEEDEC
GFBFGHAAEAAAAAADEE
GFBFGHHAAAGHHHADDD
GFBFGGHHHHHHGHAAAD
FFBFFGGGGGGGGHHHAD
FBBJFFFFFFFFFFFHAD
BBJJ.HHHHHHHHHHHAD
BIIIIHIIIIIIAAAAAD
BBB.IIIDDDDDDDDDDD'''.splitlines()
givens=[(1,6,'H'),(1,13,'A'),(3,3,'B'),(3,8,'C'),(3,16,'D'),(3,18,'C'),(4,9,'E'),(4,18,'E'),(6,1,'G'),(6,13,'G'),(8,1,'F'),(8,4,'J'),(8,15,'F'),(9,3,'J'),(10,2,'I'),(10,6,'H'),(10,12,'I'),(10,13,'A'),(11,3,'B'),(11,8,'D')]
def inspect(g):
 assert len(g)==11 and all(len(row)==18 for row in g)
 mismatches=[(r,c,ch,g[r-1][c-1])for r,c,ch in givens if g[r-1][c-1]!=ch]
 comps={}
 for ch in 'ABCDEFGHIJ':
  todo={(r,c)for r in range(11)for c in range(18)if g[r][c]==ch};parts=[]
  while todo:
   seed=min(todo);todo.remove(seed);stack=[seed];part=[seed]
   while stack:
    r,c=stack.pop()
    for v in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
     if v in todo:todo.remove(v);stack.append(v);part.append(v)
   parts.append(sorted([r+1,c+1]for r,c in part))
  comps[ch]=parts
 return {'givens_mismatches':mismatches,'component_sizes':{ch:list(map(len,ps))for ch,ps in comps.items()},'components':comps}
before=inspect(grid)
assert not before['givens_mismatches']
assert len(before['components']['G'])==2
assert all(len(parts)==1 for ch,parts in before['components'].items() if ch!='G')
assert before['components']['G'][1]==[[5,11]]
corrected=grid.copy();corrected[4]=corrected[4][:10]+'A'+corrected[4][11:]
after=inspect(corrected)
assert not after['givens_mismatches'] and all(len(p)==1 for p in after['components'].values())
out={'source':'4B answer SAT392(a)(iv), printed627/file647; givens printed354/file374','coordinate_convention':'Rows from top, columns from left, both 1-based. Dot means an unfilled cell.','printed_grid':grid,'givens':givens,'printed':before,'correction':{'row':5,'column':11,'from':'G','to':'A'},'corrected_grid':corrected,'corrected':after}
(root/'results/bookwise-sat392-iv.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'before':before['component_sizes'],'after':after['component_sizes'],'givens_preserved':not after['givens_mismatches']}))
