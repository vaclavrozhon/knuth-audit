"""Triangular cells with vertex colors; all vertex orders are counterclockwise."""
from itertools import product
from pathlib import Path
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/vertices140'
COLORS='abcd'


def piece(w):return min(w[i:]+w[:i] for i in range(3))
PIECES=sorted({piece(''.join(w)) for w in product(COLORS,repeat=3)})


def vertices(t):
    x,y,z=t
    return ((x,y),(x+1,y),(x,y+1)) if z==0 else ((x+1,y+1),(x,y+1),(x+1,y))


def cell(points):
    points=set(points);x=min(p[0] for p in points);y=min(p[1] for p in points)
    ts=[(x,y,z) for z in (0,1) if set(vertices((x,y,z)))==points]
    assert len(ts)==1,points
    return ts[0]


def transform(v,rot=0,flip=False):
    x,y=v
    if flip:x,y=y,x
    for _ in range(rot):x,y=-y,x+y
    return x,y


def normalize_shape(cells):
    points={v for t in cells for v in vertices(t)}
    x0=min(x for x,y in points);y0=min(y for x,y in points)
    return tuple(sorted((x-x0,y-y0,z) for x,y,z in cells))


def transform_shape(cells,rot,flip):
    return normalize_shape([cell([transform(v,rot,flip) for v in vertices(t)]) for t in cells])


def shape_key(cells):
    return min(transform_shape(cells,r,f) for r in range(6) for f in [False,True])


def neighbors(t):
    x,y,z=t
    return [(x,y,1),(x-1,y,1),(x,y-1,1)] if z==0 else [(x,y,0),(x+1,y,0),(x,y+1,0)]


def polyiamonds(n):
    shapes={((0,0,0),)};counts=[1]
    for size in range(2,n+1):
        shapes={shape_key(set(s)|{t}) for s in shapes for u in s for t in neighbors(u) if t not in s}
        counts.append(len(shapes))
    return sorted(shapes),counts


def scale(cells,k):
    result=set()
    for x,y,z in cells:
        for p,q,w in product(range(k),range(k),range(2)):
            if (p+q<k-w)==(z==0):result.add((k*x+p,k*y+q,w))
    assert len(result)==len(cells)*k*k
    return normalize_shape(result)


HEX_DIRECTIONS=((1,1),(-1,2),(-2,1),(-1,-1),(1,-2),(2,-1))
LATTICE_DIRECTIONS=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))


def center_key(points):
    results=[]
    for r,f in product(range(6),(False,True)):
        q=[transform(p,r,f) for p in points];x0=min(x for x,y in q);y0=min(y for x,y in q)
        results.append(tuple(sorted((x-x0,y-y0) for x,y in q)))
    return min(results)


def polyhexes(n):
    shapes={((0,0),)};counts=[1]
    for size in range(2,n+1):
        shapes={center_key(set(s)|{(x+dx,y+dy)}) for s in shapes for x,y in s for dx,dy in HEX_DIRECTIONS if (x+dx,y+dy) not in s}
        counts.append(len(shapes))
    result=[]
    for centers in sorted(shapes):
        cells=[]
        for x,y in centers:
            for i,(dx,dy) in enumerate(LATTICE_DIRECTIONS):
                ex,ey=LATTICE_DIRECTIONS[(i+1)%6]
                cells.append(cell([(x,y),(x+dx,y+dy),(x+ex,y+ey)]))
        assert len(set(cells))==6*n
        result.append(dict(centers=centers,cells=shape_key(cells)))
    return sorted(result,key=lambda x:x['cells']),counts


def canonical_colors(text):
    seen={}
    return ''.join(seen.setdefault(c,COLORS[len(seen)]) if c not in seen else seen[c] for c in text)


def vertex_list(cells):return sorted({v for t in cells for v in vertices(t)})


def validate(cells,word):
    vs=vertex_list(cells);assert len(word)==len(vs) and set(word)<=set(COLORS)
    coloring=dict(zip(vs,word))
    tiles=[piece(''.join(coloring[v] for v in vertices(t))) for t in cells]
    assert sorted(tiles)==PIECES
    return True


def symmetries(cells):
    cells=normalize_shape(cells);vs=vertex_list(cells);idx={v:i for i,v in enumerate(vs)}
    output=[]
    for rot,flip in product(range(6),(False,True)):
        vv=[transform(v,rot,flip) for v in vs];x0=min(x for x,y in vv);y0=min(y for x,y in vv)
        if transform_shape(cells,rot,flip)!=cells:continue
        perm=[idx[x-x0,y-y0] for x,y in vv]
        assert sorted(perm)==list(range(len(vs)))
        output.append(dict(rot=rot,flip=flip,perm=perm,halfturn=(rot==3 and not flip)))
    return output


def spatial_word(word,perm):
    out=['']*len(word)
    for i,j in enumerate(perm):out[j]=word[i]
    return ''.join(out)


def problem(cells):
    cells=normalize_shape(cells);vs=vertex_list(cells);idx={v:i for i,v in enumerate(vs)}
    primary=[f'p{i}' for i in range(len(cells))]+PIECES
    secondary=[f'v{i}' for i in range(len(vs))]
    rows=[];placements=[]
    for i,t in enumerate(cells):
        for cols in product(COLORS,repeat=3):
            w=''.join(cols)
            rows.append([f'p{i}',piece(w)]+[f'v{idx[v]}:{c}' for v,c in zip(vertices(t),w)])
            placements.append(dict(cell=i,colors=w))
    assert len(cells)==24 and len(rows)==1536
    return dict(cells=cells,vertices=vs,header=primary+['|']+secondary,rows=rows,placements=placements)


def native_text(enc):
    return ' '.join(enc['header'])+'\n'+'\n'.join(' '.join(row) for row in enc['rows'])+'\n'
