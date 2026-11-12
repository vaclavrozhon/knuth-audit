"""Six distinct colors on cube faces, in order U,D,F,B,L,R."""
from itertools import permutations,product
from pathlib import Path
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/cubes146'
COLORS='abcdef'
DIRECTIONS=((0,0,1),(0,0,-1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0))


def spatial_group():
    result=[]
    for p in permutations(range(3)):
        parity=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        for signs in product([-1,1],repeat=3):
            transform=lambda v:tuple(signs[j]*v[p[j]] for j in range(3))
            perm=tuple(DIRECTIONS.index(transform(v)) for v in DIRECTIONS)
            result.append(dict(perm=perm,determinant=parity*signs[0]*signs[1]*signs[2],
                               row_axis_preserved=p[0]==0,reverse=p[0]==0 and signs[0]<0))
    return result


GROUP=spatial_group()
ROTATIONS=[r['perm'] for r in GROUP if r['determinant']==1]
ROW_GROUP=[r for r in GROUP if r['row_axis_preserved']]


def orient(word,perm):
    result=['']*6
    for i,j in enumerate(perm):result[j]=word[i]
    return ''.join(result)


def name(word):
    assert sorted(word)==list(COLORS)
    return min(orient(word,p) for p in ROTATIONS)


WORDS=[''.join(p) for p in permutations(COLORS)]
NAME={w:name(w) for w in WORDS}
TYPES=sorted(set(NAME.values()))


def normalize(row):
    rename=dict(zip(row[0],COLORS))
    return tuple(''.join(rename[c] for c in cube) for cube in row)


def validate(row,complete=True):
    assert len(row)==6 if complete else 1<=len(row)<=6
    assert all(sorted(w)==list(COLORS) for w in row)
    assert len({NAME[w] for w in row})==len(row)
    for face in range(4):assert len({w[face] for w in row})==len(row)
    assert all(a[5]==b[4] for a,b in zip(row,row[1:]))
    if complete:
        assert row[0][4]==row[-1][5]
        assert all(sorted(w[face] for w in row)==list(COLORS) for face in range(4))
    return True


def orbit(row):
    result=[]
    for transform in ROW_GROUP:
        changed=tuple(orient(w,transform['perm']) for w in row)
        if transform['reverse']:changed=changed[::-1]
        for k in range(6):result.append(normalize(changed[k:]+changed[:k]))
    assert len(result)==96
    return result


def problem():
    primary=[str(i+1) for i in range(6)]+[f+c for f in 'udfb' for c in COLORS]
    secondary=TYPES+[f'h{i}' for i in range(6)]
    rows=[];placements=[]
    for i in range(6):
        for word in WORDS:
            if i==0 and word!=COLORS:continue
            rows.append([str(i+1),NAME[word]]+[f+c for f,c in zip('udfb',word[:4])]+
                        [f'h{i}:'+word[4],f'h{(i+1)%6}:'+word[5]])
            placements.append(dict(position=i,word=word))
    return dict(header=primary+['|']+secondary,rows=rows,placements=placements)


def native_text(enc):
    return ' '.join(enc['header'])+'\n'+''.join(' '.join(r)+'\n' for r in enc['rows'])
