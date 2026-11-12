"""Explicit XCC instances and independent geometry for DLX94--97.

Colors here are positive integers; 1 denotes the digit 0. A zero color means
an uncolored occurrence, as in colored_dlx.py. All coordinates are zero based.
"""
from itertools import product


def instance(primary, secondary, options, info):
    names = primary + secondary
    number = {name: i+1 for i, name in enumerate(names)}
    assert len(number) == len(names)
    rows = [tuple((number[x], c) for x, c in row) for row in options]
    assert all(len({i for i, c in row}) == len(row) for row in rows)
    return dict(names=names, primary=len(primary), rows=rows, info=info)


def native_text(enc):
    names, p = enc['names'], enc['primary']
    return ' '.join(names[:p]+['|']+names[p:])+'\n'+''.join(
        ' '.join(names[i-1]+(':'+str(c-1) if c else '') for i, c in row)+'\n'
        for row in enc['rows'])


def binary94():
    prim = [f't{k}' for k in range(16)]+[f'p{k}' for k in range(16)]
    sec = [f'x{k}' for k in range(16)]
    rows, info = [], []
    for j, bits in enumerate(product(range(2), repeat=4)):
        for k in range(16):
            rows.append([(f't{j}', 0), (f'p{k}', 0)]+
                        [(f'x{(k+d)%16}', b+1) for d, b in zip((0,1,3,4), bits)])
            info.append((j, k, bits))
    return instance(prim, sec, rows, info)


def words95(n, p, q):
    return [bits for bits in product(range(2), repeat=n) if p <= sum(bits) <= q]


def cycle95(n, p, q, variant='primary', symmetry=True):
    words = words95(n, p, q)
    m = len(words)
    assert n <= m
    a, b = [f'a{k}' for k in range(m)], [f'b{k}' for k in range(m)]
    primary = (a if variant in ('primary','b-secondary') else [])+b
    secondary = []
    if variant == 'b-secondary': primary, secondary = a, b
    if variant == 'a-secondary': secondary = a
    assert variant in ('primary','b-secondary','a-secondary','omit-a')
    secondary += [f'x{k}' for k in range(m)]
    rows, info = [], []
    for j in range(m):
        for k, bits in enumerate(words):
            if symmetry and ((j == 0) != (k == 0)): continue
            row = ([] if variant == 'omit-a' else [(f'a{j}',0)])+[(f'b{k}',0)]
            row += [(f'x{(j+d)%m}',t+1) for d,t in enumerate(bits)]
            rows.append(row); info.append((j,k,bits))
    return instance(primary, secondary, rows, info)


def torus96():
    # Use 32 complement classes, represented by six bits starting in zero.
    prim = [f't{k}' for k in range(32)]+[f'p{k}' for k in range(32)]
    sec = [f'd{r}.{c}' for r in range(4) for c in range(8)]
    rows, info = [], []
    for j, tail in enumerate(product(range(2), repeat=5)):
        bits = (0,)+tail
        for r,c in product(range(4), range(8)):
            slot = 8*r+c
            if (j == 0) != (slot == 0): continue
            for base in range(2):
                if slot == 0 and base: continue  # the unique all-zero window
                row = [(f't{j}',0),(f'p{slot}',0)]
                for (dr,dc), bit in zip(product(range(2),range(3)),bits):
                    rr, cc = r+dr, (c+dc)%8
                    row.append((f'd{rr%4}.{cc}', (base^bit^(rr//4))+1))
                rows.append(row); info.append((j,slot,base))
    return instance(prim,sec,rows,info)


def torus97():
    # Literal answer97, with jk encoded as 9*j+k and paired with p00.
    prim = [f't{k}' for k in range(27)]+[f'p{k}' for k in range(27)]
    sec = [f'd{r}.{c}' for r in range(3) for c in range(9)]
    rows, info = [], []
    for j,(a,b,c) in enumerate(product(range(3),repeat=3)):
        for rr,cc in product(range(3),range(9)):
            slot = 9*rr+cc
            if (j == 0) != (slot == 0): continue
            for base in range(3):
                row = [(f't{j}',0),(f'p{slot}',0),
                       (f'd{rr}.{cc}',base+1),(f'd{rr}.{(cc+1)%9}',(base+a)%3+1)]
                if rr < 2:
                    row += [(f'd{rr+1}.{cc}',(base+b)%3+1),
                            (f'd{rr+1}.{(cc+1)%9}',(base+c)%3+1)]
                else:
                    row += [(f'd0.{(cc-3)%9}',(base+b-1)%3+1),
                            (f'd0.{(cc-2)%9}',(base+c-1)%3+1)]
                rows.append(row); info.append((j,slot,base))
    return instance(prim,sec,rows,info)


def expand96(strip):
    assert len(strip)==32
    top = [list(map(int,strip[8*r:8*r+8])) for r in range(4)]
    return top+[[1-b for b in row] for row in top]


def expand97(strip):
    assert len(strip)==27
    return [[(int(strip[(r%3)*9+(c-3*(r//3))%9])+r//3)%3
             for c in range(9)] for r in range(9)]


def window_set(board,height,width):
    h,w=len(board),len(board[0])
    return {tuple(board[(r+dr)%h][(c+dc)%w] for dr in range(height)
                  for dc in range(width)) for r in range(h) for c in range(w)}


def fraction_free_det(matrix):
    """Bareiss elimination, with exact division checked at each pivot."""
    a=[row[:] for row in matrix]; n=len(a)
    if not n:return 1
    prev,sign=1,1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]


def euler_count95(n,p,q):
    """Last-exit arborescences times local orders; the first edge is fixed."""
    from math import factorial,prod
    words=words95(n,p,q)
    vertices=sorted({w[:-1] for w in words}|{w[1:] for w in words})
    number={v:i for i,v in enumerate(vertices)}
    size=len(vertices); adj=[[0]*size for _ in range(size)]
    for w in words:adj[number[w[:-1]]][number[w[1:]]]+=1
    degrees=list(map(sum,adj)); indegrees=list(map(sum,zip(*adj)))
    assert degrees==indegrees and all(degrees)
    # A root is the initial vertex of the distinguished first edge.
    root=number[words[0][:-1]]
    reach={root}; stack=[root]
    while stack:
        i=stack.pop()
        for j in range(size):
            if adj[i][j] and j not in reach:reach.add(j);stack.append(j)
    assert len(reach)==size
    lap=[[((degrees[i] if i==j else 0)-adj[i][j])
          for j in range(size) if j!=root] for i in range(size) if i!=root]
    trees=fraction_free_det(lap)
    local=prod(factorial(d-1) for d in degrees)
    return dict(n=n,p=p,q=q,edges=len(words),vertices=size,root=root,
                arborescences=trees,local_order_factor=local,cycles=trees*local,
                laplacian_minor=lap)
