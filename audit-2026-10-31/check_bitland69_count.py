#!/usr/bin/env python3
"""Independent F119 certificate: enumerate all 9-subsets of a 4x4 square."""
from collections import Counter
from datetime import datetime,timezone
import gzip
from itertools import combinations
import json
from dlx1_audit_tools import ROOT,sha

OUT=ROOT/'results/convex68'
MANUAL='BBLBLLLLB/LLLBLLLBL/BBLBLBBLB/LLLLLLLLL/BBBLLBLLB/LBLBBBBBB/BBLBBBBBL/LBLLLLBLL/LLBLLBBLL'


def main():
    board=list(MANUAL.replace('/',''))
    diagrams=json.loads((OUT/'bitland69.json').read_text())['diagrams']
    assert all(d['cells']==board for d in diagrams.values())
    shapes=[];count=0
    for choice in combinations(range(16),9):
        count+=1;s=set(choice)
        if not any(v<4 for v in s) or not any(v%4==0 for v in s):continue
        connected={choice[0]};front=[choice[0]]
        for v in front:
            for w in s-connected:
                if abs(v//4-w//4)+abs(v%4-w%4)==1:connected.add(w);front.append(w)
        if connected!=s:continue
        if any(any(4*r+c not in s for c in range(a%4+1,b%4))
               for r in range(4) for a in s for b in s if a//4==b//4==r and a<b):continue
        if any(any(4*r+c not in s for r in range(a//4+1,b//4))
               for c in range(4) for a in s for b in s if a%4==b%4==c and a<b):continue
        shapes.append(choice)
    assert count==11440 and len(shapes)==325
    placements={tuple(sorted((r+v//4)*9+c+v%4 for v in shape))
                for shape in shapes for r in range(9-max(v//4 for v in shape))
                for c in range(9-max(v%4 for v in shape))}
    other=set(map(tuple,json.loads(gzip.decompress((OUT/'n9.json.gz').read_bytes()))))
    assert placements==other and len(placements)==12097
    counts=Counter(sum(board[v]=='B' for v in t) for t in placements)
    assert dict(counts)=={0:2,1:163,2:1363,3:2785,4:2771,5:2362,6:1647,7:753,8:230,9:21}
    witnesses=sorted(t for t in placements if sum(board[v]=='B' for v in t)==6)
    assert len(set(witnesses))==1647
    (OUT/'F119-six-B-placements.json').write_text(json.dumps(witnesses,indent=2)+'\n')
    result=dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
       source_sha256=sha(__file__),manual_rows=MANUAL.split('/'),subsets_examined=count,
       normalized_shapes=len(shapes),complete_placements=len(placements),complete_sets_equal=True,
       B_count_histogram=dict(sorted(counts.items())),six_B_witnesses=len(witnesses),
       witnesses_sha256=sha(OUT/'F119-six-B-placements.json'),
       original_diagrams_sha256=sha(OUT/'bitland69.json'),prior_options_sha256=sha(OUT/'n9.json.gz'),
       printed=1467,correct=1647,
       scope='Exhaustive geometric count, independent of growth, perimeter filter and both exact-cover solvers.')
    (OUT/'F119-count.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:11440 subsets,325 shapes,12097 identical placements;1647 with six B')


if __name__=='__main__':main()
