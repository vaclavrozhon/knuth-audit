"""Standalone closure check, without the list of all dominating sets."""
from pathlib import Path
from collections import Counter
from itertools import combinations
import json
ROOT=Path(__file__).parent;OUT=ROOT/'results/queen_domination'
BOARD=set((r,c) for r in range(8) for c in range(8))

def covers(queens):
    return all(any(r==s or c==t or abs(r-s)==abs(c-t) for s,t in queens) for r,c in BOARD)

def component(seed):
    seed=tuple(sorted(seed));assert covers(seed)
    todo=[seed];seen={seed};edges=set()
    while todo:
        old=todo.pop()
        for removed in old:
            kept=set(old)-{removed}
            for added in BOARD-set(old):
                nxt=tuple(sorted(kept|{added}))
                if covers(nxt):
                    edges.add(tuple(sorted((old,nxt))))
                    if nxt not in seen:seen.add(nxt);todo.append(nxt)
    return dict(seed=seed,size=len(seen),edges=len(edges),members=sorted(seen))

if __name__=='__main__':
    # Last diagram in (65), independently transcribed from p. 94.
    last=component([(0,2),(2,7),(3,3),(5,0),(7,5)])
    # Find a 20-vertex component by grouping known solutions, then certify its
    # closure with the independent geometric relocation search above.
    masks=list(map(int,(OUT/'solutions.txt').read_text().splitlines()));bins={}
    for i,m in enumerate(masks):
        for v in range(64):
            if m>>v&1:bins.setdefault(m^(1<<v),[]).append(i)
    adj=[set() for _ in masks]
    for group in bins.values():
        for i,j in combinations(group,2):adj[i].add(j);adj[j].add(i)
    remaining=set(range(len(masks)));seed20=None
    while remaining:
        i=remaining.pop();todo=[i];seen={i}
        while todo:
            for j in adj[todo.pop()]:
                if j not in seen:seen.add(j);remaining.remove(j);todo.append(j)
        if len(seen)==20:seed20=[divmod(v,8) for v in range(64) if masks[i]>>v&1];break
    assert seed20 is not None;twenty=component(seed20);assert twenty['size']==20
    out=dict(last_printed_diagram=last,component20=twenty)
    (OUT/'components-direct.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:{q:v for q,v in d.items() if q!='members'} for k,d in out.items()}))
