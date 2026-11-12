"""Graph and independent geometric checks for TAOCP X159--161."""
from pathlib import Path
from collections import Counter,defaultdict
from itertools import combinations
import json
ROOT=Path(__file__).parent;OUT=ROOT/'results/queen_domination'

def squares(mask):return [v for v in range(64) if mask>>v&1]
def attack(v,w):return v//8==w//8 or v%8==w%8 or abs(v//8-w//8)==abs(v%8-w%8)

def graph(masks,kind):
    bins=defaultdict(list)
    for i,mask in enumerate(masks):
        for v in squares(mask):bins[mask^(1<<v)].append((i,v))
    adj=[set() for _ in masks]
    for common,group in bins.items():
        for (i,v),(j,w) in combinations(group,2):
            if kind!='relocation' and not attack(v,w):continue
            if kind=='legal_queen':
                r,c=v//8,v%8;dr=(w//8>r)-(w//8<r);dc=(w%8>c)-(w%8<c);r+=dr;c+=dc;blocked=False
                while (r,c)!=divmod(w,8):
                    if common>>(8*r+c)&1:blocked=True;break
                    r+=dr;c+=dc
                if blocked:continue
            adj[i].add(j);adj[j].add(i)
    remaining=set(range(len(masks)));sizes=[]
    while remaining:
        seed=remaining.pop();todo=[seed];seen={seed}
        while todo:
            for j in adj[todo.pop()]:
                if j not in seen:seen.add(j);remaining.remove(j);todo.append(j)
        sizes.append(len(seen))
    return dict(kind=kind,vertices=len(masks),edges=sum(map(len,adj))//2,
                components=len(sizes),component_histogram=dict(Counter(sizes)),
                degree_histogram=dict(Counter(map(len,adj))))


def main():
    data=json.loads((OUT/'counts.json').read_text());masks=list(map(int,(OUT/'solutions.txt').read_text().splitlines()));assert len(masks)==len(set(masks))==4860
    stats=Counter();quadrants=Counter();orbits=set();orbit_sizes=Counter()
    for mask in masks:
        vv=squares(mask);assert len(vv)==5
        assert all(any(attack(v,w) for v in vv) for w in range(64))
        degrees=[sum(v!=w and attack(v,w) for w in vv) for v in vv]
        stats['independent5']+=max(degrees)==0;stats['total5']+=min(degrees)>0;stats['clique5']+=min(degrees)==4
        q=[0]*4
        for v in vv:q[2*(v//8//4)+v%8//4]+=1
        quadrants[sum(x*10**(3-i) for i,x in enumerate(q))]+=1
        images=set()
        for fr in range(2):
            for fc in range(2):
                for swap in range(2):
                    image=0
                    for v in vv:
                        r,c=divmod(v,8)
                        if swap:r,c=c,r
                        if fr:r=7-r
                        if fc:c=7-c
                        image|=1<<(8*r+c)
                    assert image in set_masks
                    images.add(image)
        orbits.add(min(images));orbit_sizes[len(images)]+=1
    assert dict(stats)=={k:data[k] for k in stats}
    assert data['kernels']==[0,0,0,0,0,728,6912,2456,92]
    cases=[2012,2111,2120,3002,3011,3020,3110,4010,4001,5000]
    assert [quadrants[c] for c in cases]==[134,884,33,23,34,1,16,0,22,0]
    assert sum(quadrants[c]*factor for c,factor in zip(cases,[4,4,8,4,8,8,4,8,4,4]))==4860
    out=dict(verified_models=len(masks),variants=dict(stats),symmetry_classes=len(orbits),orbit_sizes=dict(orbit_sizes),graphs=[graph(masks,k) for k in ['relocation','queen_line','legal_queen']])
    (OUT/'verified.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

if __name__=='__main__':
    set_masks=set(map(int,(OUT/'solutions.txt').read_text().splitlines()));main()
