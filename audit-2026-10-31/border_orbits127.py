"""Exact boundary-word census, with abstract and geometric groups separated."""
from collections import Counter, defaultdict
from datetime import datetime,timezone
from itertools import permutations
from math import factorial
from pathlib import Path
import json
import check_macmahon as g
from dlx1_audit_tools import sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/borders127_128'


def endpoints(e):
    k,x,y=e
    return frozenset([(x,y),(x+1,y)] if k=='-' else [(x,y),(x,y+1)] if k=='/' else [(x+1,y),(x,y+1)])


def boundary():
    adj=defaultdict(list)
    for e,ts in g.EDGE_TRIANGLES.items():
        if len(ts)==1:
            u,v=sorted(endpoints(e));adj[u].append((v,e));adj[v].append((u,e))
    u,v=(2,0),(3,0);result=[]
    for _ in range(12):
        w,e=next((w,e) for w,e in adj[u] if w==v);result.append(e)
        u,v=v,next(w for w,e in adj[v] if w!=u)
    assert u==(2,0) and len(set(result))==12
    return result


def geometric_group():
    border=boundary();lookup={endpoints(e):i for i,e in enumerate(border)}
    all_cells={frozenset(g.vertices(t)) for t in g.TRIANGLES}
    def transform(v,k,flip):
        x,y=v[0]-2,v[1]-2
        if flip:x,y=y,x
        for _ in range(k):x,y=-y,x+y
        return x+2,y+2
    group=[]
    for flip in range(2):
        for k in range(6):
            assert {frozenset(transform(v,k,flip) for v in cell) for cell in all_cells}==all_cells
            group.append(tuple(lookup[frozenset(transform(v,k,flip) for v in endpoints(e))] for e in border))
    assert len(set(group))==12
    assert set(group)=={tuple((sgn*i+j)%12 for i in range(12)) for sgn in [-1,1] for j in range(12) if j%2==(sgn==-1)}
    return group


def normalize(word):
    names={};result=[]
    for c in word:
        if c not in names:names[c]=len(names)
        result.append(names[c])
    return tuple(result)


def partitions(n=12):
    w=[0]*n;counts=[0]*4
    def rec(i,used):
        if i==n:
            if all(c%2==0 for c in counts):yield tuple(w)
            return
        # An odd number of occupied odd classes requires at least that many slots.
        if sum(c%2 for c in counts)>n-i:return
        for c in range(min(4,used+1)):
            w[i]=c;counts[c]+=1
            yield from rec(i+1,max(used,c+1))
            counts[c]-=1
    yield from rec(0,0)


def fixed_even(position,color):
    seen=set();cycles=[]
    for i in range(12):
        if i in seen:continue
        q=[];j=i
        while j not in seen:q.append(j);seen.add(j);j=position[j]
        cycles.append(len(q))
    dp={0:1}
    for length in cycles:
        masks=[]
        for first in range(4):
            c=first;mask=0
            for _ in range(length):mask^=1<<c;c=color[c]
            if c==first:masks.append(mask)
        nxt=defaultdict(int)
        for mask,count in dp.items():
            for q in masks:nxt[mask^q]+=count
        dp=nxt
    return dp.get(0,0)


def main():
    OUT.mkdir(exist_ok=True)
    abstract=[tuple((sgn*i+j)%12 for i in range(12)) for sgn in [-1,1] for j in range(12)]
    groups={'abstract_D12':abstract,'geometric_D6':geometric_group()}
    representatives={k:set() for k in groups};labeled=0;part_count=0
    for w in partitions():
        part_count+=1;labeled+=factorial(4)//factorial(4-max(w)-1)
        for name,group in groups.items():representatives[name].add(min(normalize(w[i] for i in p) for p in group))
    assert labeled==2099200
    result={}
    for name,group in groups.items():
        reps=sorted(representatives[name]);hist=Counter();special=[];total=0
        for w in reps:
            stabilizer=sum(normalize(w[i] for i in p)==w for p in group)*factorial(4-max(w)-1)
            hist[stabilizer]+=1;total+=len(group)*24//stabilizer
            if stabilizer==3:special.append(''.join(map(str,w)))
        assert total==labeled
        burnside=sum(fixed_even(p,c) for p in group for c in permutations(range(4)))
        assert burnside==len(reps)*len(group)*24
        filename=name+'-representatives.txt';(OUT/filename).write_text(''.join(''.join(map(str,w))+'\n' for w in reps))
        result[name]=dict(position_permutations=group,group_size=len(group)*24,orbits=len(reps),
                          stabilizer_histogram=dict(sorted(hist.items())),stabilizer3_representatives=special,
                          burnside_fixed_sum=burnside,weighted_orbit_sum=total,representatives_file=filename,
                          representatives_sha256=sha(OUT/filename))
    assert result['abstract_D12']['orbits']==4054
    assert result['abstract_D12']['stabilizer3_representatives']==['001022021121']
    data=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
              boundary_edges=boundary(),color_partitions=part_count,labeled_even_borders=labeled,groups=result,
              scope='All even color-count boundary words, modulo color permutations and either actual hexagon isometries or abstract12-cycle permutations. Only geometric_D6 has been proved to act on the tile puzzle.')
    (OUT/'orbits127-checked.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PASS',labeled,'even borders;',part_count,'color partitions;',[(k,x['orbits']) for k,x in result.items()])


if __name__=='__main__':main()
