"""Complete normalized deltas and two-piece exchanges for exercise217."""
from pathlib import Path
from itertools import combinations,product
from collections import Counter,defaultdict
import json,time
ROOT=Path(__file__).parent;OUT=ROOT/'results/pentomino_bipairs';OUT.mkdir(exist_ok=True)
# Knuth's O,Q,R,S correspond respectively to I,L,F,N in the common notation.
SHAPES={
 'O':[(0,i) for i in range(5)],'P':[(0,0),(0,1),(1,0),(1,1),(2,0)],
 'Q':[(0,0),(0,1),(0,2),(0,3),(1,0)],'R':[(0,1),(0,2),(1,0),(1,1),(2,1)],
 'S':[(0,0),(0,1),(1,1),(1,2),(1,3)],'T':[(0,0),(0,1),(0,2),(1,1),(2,1)],
 'U':[(0,0),(0,2),(1,0),(1,1),(1,2)],'V':[(0,0),(1,0),(2,0),(2,1),(2,2)],
 'W':[(0,0),(1,0),(1,1),(2,1),(2,2)],'X':[(0,1),(1,0),(1,1),(1,2),(2,1)],
 'Y':[(0,0),(0,1),(0,2),(0,3),(1,1)],'Z':[(0,0),(0,1),(1,1),(2,1),(2,2)]}

def transform(cells,g):
    out=[]
    for r,c in cells:
        if g>=4:c=-c
        for _ in range(g%4):r,c=c,-r
        out.append((r,c))
    return set(out)

def shift(cells,r,c):return frozenset((x-r,y-c) for x,y in cells)

def normalized(cells):return tuple(sorted(shift(cells,min(r for r,c in cells),min(c for r,c in cells))))

def orientations(cells):return {normalized(transform(cells,g)) for g in range(8)}

def delta_images(P,N,I):
    values=[]
    for g in range(8):
        p,n,i=transform(P,g),transform(N,g),transform(I,g);r=min(x for x,y in p|n);c=min(y for x,y in p|n)
        p,n,i=tuple(sorted(shift(p,r,c))),tuple(sorted(shift(n,r,c))),shift(i,r,c)
        values.extend([((p,n),i),((n,p),i)])
    key=min(d for d,i in values);return key,{i for d,i in values if d==key}

def deltas(shape):
    out=defaultdict(set);ors=orientations(shape)
    for a in ors:
        a=set(a)
        for b in ors:
            # Every overlapping relative translation aligns at least one cell.
            offsets={(r-u,c-v) for r,c in a for u,v in b}
            for r,c in offsets:
                bb={(u+r,v+c) for u,v in b};P=a-bb;N=bb-a
                if not P:continue
                key,intersections=delta_images(P,N,a&bb);out[key].update(intersections)
    return out

def hole_free(region):
    r0=min(r for r,c in region)-1;r1=max(r for r,c in region)+1;c0=min(c for r,c in region)-1;c1=max(c for r,c in region)+1
    free={(r,c) for r in range(r0,r1+1) for c in range(c0,c1+1)}-region;seen={(r0,c0)};todo=list(seen)
    while todo:
        r,c=todo.pop()
        for q in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if q in free and q not in seen:seen.add(q);todo.append(q)
    return seen==free

def canonical_pair(a,b,c,d):
    images=[]
    for g in range(8):
        aa,bb,cc,dd=[transform(s,g) for s in [a,b,c,d]];region=aa|bb;r=min(x for x,y in region);c0=min(y for x,y in region)
        parts=[tuple(sorted(shift(s,r,c0))) for s in [aa,bb,cc,dd]]
        first=(parts[0],parts[1]);second=(parts[2],parts[3]);images.append(tuple(sorted((first,second))))
    return min(images)

def main():
    start=time.monotonic();ds={};summary={}
    expected=[10,64,81,73,78,25,23,24,22,3,78,24];ones=[1,7,3,3,2,0,1,0,1,0,4,0]
    for name,shape in SHAPES.items():
        d=deltas(shape);ds[name]=d;summary[name]=dict(deltas=len(d),single_changes=sum(len(k[0])==1 for k in d),orientations=len(orientations(shape)))
        print(name,summary[name],flush=True)
    allkeys=set().union(*(set(d) for d in ds.values()));shared=Counter(sum(k in d for d in ds.values()) for k in allkeys)
    catalog=[];with_holes=[]
    for a,b in combinations(SHAPES,2):
        clean=set();holed=set()
        for key in ds[a].keys()&ds[b].keys():
            P,N=map(set,key)
            for I,J in product(ds[a][key],ds[b][key]):
                if I&J:continue
                aa=P|I;bb=N|J;cc=N|I;dd=P|J;region=aa|bb
                assert len(region)==10 and not aa&bb and not cc&dd and region==cc|dd
                assert normalized(aa) in orientations(SHAPES[a]) and normalized(cc) in orientations(SHAPES[a])
                assert normalized(bb) in orientations(SHAPES[b]) and normalized(dd) in orientations(SHAPES[b])
                pair=canonical_pair(aa,bb,cc,dd)
                (clean if hole_free(region) else holed).add(pair)
        for pair in sorted(clean):catalog.append(dict(pieces=[a,b],covers=pair))
        for pair in sorted(holed):with_holes.append(dict(pieces=[a,b],covers=pair))
    result=dict(shape_counts=summary,shared_delta_multiplicity=dict(shared),catalog_count=len(catalog),catalog=catalog,
                excluded_hole_count=len(with_holes),excluded_with_holes=with_holes,seconds=time.monotonic()-start)
    (OUT/'catalog.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['catalog','excluded_with_holes','shape_counts']}),flush=True)
    assert [summary[k]['deltas'] for k in SHAPES]==expected
    assert [summary[k]['single_changes'] for k in SHAPES]==ones

if __name__=='__main__':main()
