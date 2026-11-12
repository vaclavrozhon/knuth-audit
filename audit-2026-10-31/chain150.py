"""Strip paths, forced special join, and multiplicity exact cover for DLX150."""
from collections import Counter
from pathlib import Path
import json
from puzzle_xcc import encode,native_text,save,sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/chain150'
DIRS=((0,-1),(1,0),(0,1),(-1,0))
SIDES='NESW'


def key(cells):return tuple(sorted((x,y,*v) for (x,y),v in cells.items()))
def from_key(k):return {(x,y):tuple(v) for x,y,*v in k}


def rotate(cells,k):
    result={}
    for (x,y),v in cells.items():
        vv=[0]*4
        for i,c in enumerate(v):vv[(i+k)%4]=c
        for _ in range(k):x,y=-y,x
        result[x,y]=tuple(vv)
    a=min(x for x,y in result);b=min(y for x,y in result)
    return {(x-a,y-b):v for (x,y),v in result.items()}


def canonical(cells):return min(key(rotate(cells,k)) for k in range(4))


def strip(record):
    n=record['length'];cells={(x,0):[0]*4 for x in range(n)}
    for c in record['contacts']:cells[c['cell'],0][SIDES.index(c['side'])]=2 if c['kind']=='special' else 1
    for x in range(n-1):
        total=sum(bool(c) for c in cells[x,0]);assert total<=2
        if total==1:cells[x,0][1]=cells[x+1,0][3]=1
    assert all(sum(bool(c) for c in v) in [0,2] for v in cells.values())
    return {p:tuple(v) for p,v in cells.items()}


def inventory(corrected=False):
    data=json.loads((OUT/'strips-extracted.json').read_text());pieces=[strip(r) for r in data['pieces']]
    # Explicit alternative inventory: one of the two identical S-dominoes is
    # replaced by a second copy of the single L-domino (original index2).
    if corrected:pieces[9]=dict(pieces[2])
    original=Counter(canonical(p) for p in pieces);assert len(original)==14 and Counter(original.values())=={1:10,2:4}
    assert sum(len(p) for p in pieces)==64
    assert sum(sum(any(v) for v in p.values()) for p in pieces)==34
    assert sum(sum(c==2 for c in v) for p in pieces for v in p.values())==2
    superpiece=dict(pieces[17]);superpiece.update({(x,y+1):v for (x,y),v in pieces[16].items()})
    assert len(superpiece)==11 and superpiece[0,0][2]==superpiece[0,1][0]==2
    for (x,y),v in superpiece.items():
        for i,(dx,dy) in enumerate(DIRS):
            if (x+dx,y+dy) in superpiece:assert v[i]==superpiece[x+dx,y+dy][(i+2)%4]
    reduced=Counter(canonical(p) for p in pieces[:16]);assert len(reduced)==12
    types=[dict(name='p'+str(i),count=count,cells=from_key(k)) for i,(k,count) in enumerate(sorted(reduced.items()))]
    types.append(dict(name='sup',count=1,cells=superpiece))
    return pieces,types


def edge(p,q):
    a,b=sorted([p,q]);return 'e'+''.join(map(str,(*a,*b)))


def placements(corrected=False):
    pieces,types=inventory(corrected);options=[]
    for t in types:
        orientations={key(rotate(t['cells'],k)) for k in range(4)} if t['name']!='sup' else {key(t['cells'])}
        for kk in sorted(orientations):
            p=from_key(kk);w=max(x for x,y in p)+1;h=max(y for x,y in p)+1
            for y in range(9-h):
                for x in range(9-w):
                    # Eighteen candidate anchors: x=0..2,y=1..6. Border rules
                    # subsequently reject three dangling-path placements at y=6.
                    if t['name']=='sup' and y==0:continue
                    moved={(a+x,b+y):v for (a,b),v in p.items()};boundary={};valid=True
                    for (a,b),v in moved.items():
                        for i,(dx,dy) in enumerate(DIRS):
                            q=(a+dx,b+dy)
                            if q in moved:continue
                            if not (0<=q[0]<8 and 0<=q[1]<8):
                                if v[i]:valid=False
                                continue
                            assert v[i]!=2;boundary[edge((a,b),q)]=v[i]
                    if valid:options.append(dict(type=t['name'],cells=moved,boundary=boundary))
    assert sum(p['type']=='sup' for p in options)==15
    return types,options


def problem(corrected=False):
    types,ps=placements(corrected);primary=[t['name'] for t in types]+['c'+str(x)+str(y) for y in range(8) for x in range(8)]
    secondary=sorted({edge((x,y),(x+dx,y+dy)) for x in range(8) for y in range(8) for dx,dy in [(1,0),(0,1)] if x+dx<8 and y+dy<8})
    assert len(secondary)==112
    rows=[[(p['type'],0)]+[('c'+str(x)+str(y),0) for x,y in sorted(p['cells'])]+[(e,c+1) for e,c in sorted(p['boundary'].items())] for p in ps]
    enc=encode(primary,secondary,rows);lines=native_text(enc).splitlines()
    counts={t['name']:t['count'] for t in types}
    lines[0]=' '.join((str(counts[n])+'|'+n if counts.get(n,1)>1 else n) for n in primary)+' | '+' '.join(secondary)
    return enc,'\n'.join(lines)+'\n',ps


def validate(ps,corrected=False):
    _,types=inventory(corrected);counts=Counter(p['type'] for p in ps);assert counts=={t['name']:t['count'] for t in types}
    board={}
    for p in ps:
        for xy,v in p['cells'].items():assert xy not in board;board[xy]=v
    assert set(board)=={(x,y) for x in range(8) for y in range(8)}
    graph={p:set() for p,v in board.items() if any(v)}
    for p,v in board.items():
        assert sum(bool(c) for c in v) in [0,2]
        for i,(dx,dy) in enumerate(DIRS):
            q=(p[0]+dx,p[1]+dy)
            if q not in board:assert not v[i];continue
            assert bool(v[i])==bool(board[q][(i+2)%4])
            if v[i]:graph[p].add(q)
    assert len(graph)==34 and all(len(v)==2 for v in graph.values())
    components=[];rest=set(graph)
    while rest:
        seen={min(rest)};stack=list(seen)
        while stack:
            for q in graph[stack.pop()]-seen:seen.add(q);stack.append(q)
        components.append(len(seen));rest-=seen
    return graph,components


def path_key(graph):
    cells={p:tuple(int((p[0]+dx,p[1]+dy) in ns) for dx,dy in DIRS) for p,ns in graph.items()}
    return canonical(cells)
