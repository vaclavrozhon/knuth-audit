"""Face geometry for colored-cube bricks. Axes: front/back, top/bottom, left/right."""
from itertools import product,permutations
from pathlib import Path
import cubes146 as cubes
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/bricks147'
OFFSETS=((0,-1,0),(0,1,0),(-1,0,0),(1,0,0),(0,0,-1),(0,0,1))


def positions(dims):return list(product(*(range(d) for d in dims)))


def faces(pos):
    center=tuple(2*x+1 for x in pos)
    return [tuple(a+b for a,b in zip(center,d)) for d in OFFSETS]


def boundary(face,dims):
    found=[2*i+(face[i]>0) for i in range(3) if face[i] in [0,2*dims[i]]]
    assert len(found)<=1
    return found[0] if found else None


def validate(dims,model):
    assert len(model)==len(positions(dims))
    cells=dict(zip(positions(dims),model));colors={};bounds={}
    assert len(set(cubes.NAME[w] for w in model))==len(model)
    for pos,word in cells.items():
        assert sorted(word)==list(cubes.COLORS)
        for face,color in zip(faces(pos),word):
            if face in colors:assert colors[face]==color,(pos,face)
            colors[face]=color;b=boundary(face,dims)
            if b is not None:
                if b in bounds:assert bounds[b]==color,(pos,b)
                bounds[b]=color
    assert len(bounds)==6
    for i in range(6):
        for j in range(i+1,6):
            if bounds[i]==bounds[j]:assert i//2==j//2
    return colors,[bounds[i] for i in range(6)]


def decode_tensor(dims,tensor):
    assert len(tensor)==2*dims[0]+1
    face_colors={}
    for x,plane in enumerate(tensor):
        assert len(plane)==2*dims[1]+1
        for y,row in enumerate(plane):
            assert len(row)==2*dims[2]+1
            for z,c in enumerate(row):
                if (x%2+y%2+z%2)==2:
                    assert c in cubes.COLORS;face_colors[(x,y,z)]=c
                else:assert c=='.',(x,y,z,c)
    models=[''.join(face_colors[f] for f in faces(p)) for p in positions(dims)]
    checked,bounds=validate(dims,models);assert checked==face_colors
    return dict(dims=dims,model=models,names=[cubes.NAME[w] for w in models],boundary=bounds,
                face_count=len(face_colors),characters=sum(len(row) for plane in tensor for row in plane))


def group(dims):
    result=[]
    for p in permutations(range(3)):
        if any(dims[i]!=dims[p[i]] for i in range(3)):continue
        for signs in product([-1,1],repeat=3):
            perm=tuple(OFFSETS.index(tuple(signs[j]*v[p[j]] for j in range(3))) for v in OFFSETS)
            result.append((p,signs,perm))
    return result


def transform(dims,model,operation):
    p,signs,perm=operation;new={}
    for pos,word in zip(positions(dims),model):
        q=tuple(pos[p[j]] if signs[j]>0 else dims[j]-1-pos[p[j]] for j in range(3))
        new[q]=cubes.orient(word,perm)
    return tuple(new[q] for q in positions(dims))


def orbit(dims,model):return [cubes.normalize(transform(dims,model,g)) for g in group(dims)]


def direct_case(dims):
    # Boundary facets are represented by one shared color variable per outer face.
    variables={};cells=[]
    for pos in positions(dims):
        row=[]
        for f in faces(pos):
            b=boundary(f,dims);key=('boundary',b) if b is not None else ('interior',*f)
            if key not in variables:variables[key]=len(variables)
            row.append(variables[key])
        cells.append(row)
    ids={t:i for i,t in enumerate(cubes.TYPES)}
    return f'{len(cells)} {len(variables)}\n'+''.join(f'{w} {ids[cubes.NAME[w]]}\n' for w in cubes.WORDS)+''.join(' '.join(map(str,row))+'\n' for row in cells)


def native_problem(dims):
    # Literal book encoding: separate physical facet variables and six face selectors.
    cells=positions(dims);facet=sorted({f for p in cells for f in faces(p)})
    label=lambda f:''.join(map(str,f))
    primary=[f'p{i}' for i in range(len(cells))]+[f'b{i}' for i in range(6)]
    secondary=cubes.TYPES+[label(f) for f in facet];rows=[];placements=[]
    for i,pos in enumerate(cells):
        for word in cubes.WORDS:
            if i==0 and word!=cubes.COLORS:continue
            rows.append([f'p{i}',cubes.NAME[word]]+[label(f)+':'+c for f,c in zip(faces(pos),word)])
            placements.append(dict(position=i,word=word))
    for b in range(6):
        ff=[f for f in facet if boundary(f,dims)==b]
        for c in cubes.COLORS:
            rows.append([f'b{b}']+[label(f)+':'+c for f in ff]);placements.append(dict(boundary=b,color=c))
    return dict(header=primary+['|']+secondary,rows=rows,placements=placements)
