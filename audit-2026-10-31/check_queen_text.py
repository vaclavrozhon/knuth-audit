"""Reproduce every numerical restriction on p.94 and quadrant cases X159."""
from pathlib import Path
from collections import Counter,defaultdict
from itertools import product
import json
from check_queen_domination import squares,attack,OUT

def quadrant_images(q):
    answer=set()
    for fr,fc,swap in product(range(2),repeat=3):
        image=[0]*4
        for r,c in product(range(2),repeat=2):
            rr,cc=(c,r) if swap else (r,c)
            if fr:rr=1-rr
            if fc:cc=1-cc
            image[2*rr+cc]=q[2*r+c]
        answer.add(tuple(image))
    return answer


def main():
    masks=list(map(int,(OUT/'solutions.txt').read_text().splitlines()));stats=Counter()
    for mask in masks:
        vv=squares(mask);rc=[divmod(v,8) for v in vv]
        stats['no_boundary']+=all(1<=r<=6 and 1<=c<=6 for r,c in rc)
        stats['no_central16']+=all(not(2<=r<=5 and 2<=c<=5) for r,c in rc)
        stats['avoid_middle_rows_columns']+=all(r not in (3,4) and c not in (3,4) for r,c in rc)
        stats['black_only']+=all((r+c)%2==0 for r,c in rc)
        stats['avoid_TL_BR']+=all((r<4)!=(c<4) for r,c in rc)
        stats['top_half']+=all(r<4 for r,c in rc)
        count=[sum(attack(v,w) for v in vv) for w in range(64)]
        stats['bottom_once']+=all(count[w]==1 for w in range(56,64))
        stats['center_twice']+=all(count[8*r+c]>=2 for r in range(2,6) for c in range(2,6))
        stats['atmost4']+=max(count)<=4;stats['atmost3']+=max(count)<=3
    expected=dict(no_boundary=284,no_central16=880,avoid_middle_rows_columns=88,black_only=200,avoid_TL_BR=90,top_half=2,bottom_once=18,center_twice=48,atmost4=3248,atmost3=96)
    assert dict(stats)==expected
    cases=['2012','2111','2120','3002','3011','3020','3110','4010','4001','5000']
    groups=[quadrant_images(tuple(map(int,c))) for c in cases]
    assert [len(g) for g in groups]==[4,4,8,4,8,8,4,8,4,4]
    allq={q for q in product(range(6),repeat=4) if sum(q)==5}
    assert len(set.union(*groups))==sum(map(len,groups))==len(allq)==56
    assert set.union(*groups)==allq
    figs=[[(1,3),(2,4),(3,1),(5,0),(6,7)],[(0,3),(2,2),(3,5),(5,2),(6,5)],[(2,2),(2,3),(2,4),(3,5),(4,3)],[(0,2),(2,7),(3,3),(5,0),(7,5)]]
    figm=[sum(1<<(8*r+c) for r,c in f) for f in figs];assert all(m in masks for m in figm)
    bins=defaultdict(list)
    for i,m in enumerate(masks):
        for v in squares(m):bins[m^(1<<v)].append(i)
    adj=[set() for _ in masks]
    for group in bins.values():
        for i in group:adj[i].update(set(group)-{i})
    remaining=set(range(len(masks)));size={}
    while remaining:
        seed=remaining.pop();todo=[seed];seen={seed}
        while todo:
            for j in adj[todo.pop()]:
                if j not in seen:seen.add(j);remaining.remove(j);todo.append(j)
        for i in seen:size[i]=len(seen)
    sizes=[size[masks.index(m)] for m in figm];assert sizes==[3804,3804,3804,20]
    out=dict(page94_counts=dict(stats),fig65=figs,fig65_component_sizes=sizes,quadrant_compositions=56,quadrant_classes=10)
    (OUT/'main-text.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

if __name__=='__main__':main()
