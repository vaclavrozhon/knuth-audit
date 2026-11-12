"""Barycentric geometry and colored exact-cover encoding for DLX149."""
from itertools import product, permutations, combinations
from pathlib import Path
import puzzle_xcc as xcc

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/tetra149'
VERTICES=sorted(p for p in product(range(4),repeat=4) if sum(p)==3)
CELLS=sorted(p for p in product(range(3),repeat=4) if sum(p)==2)
INDEX={p:i for i,p in enumerate(VERTICES)}
CORNERS=[tuple(INDEX[tuple(a+(i==j) for i,a in enumerate(p))] for j in range(4)) for p in CELLS]
EVEN=[p for p in permutations(range(4)) if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2==0]


def name(word): return min(''.join(word[i] for i in p) for p in EVEN)


WORDS=[''.join(p) for p in permutations('abcde',4)]
TYPES=sorted({name(w) for w in WORDS})


def validate(model):
    assert len(model)==20 and set(model)==set('abcde')
    types=[]
    for ids in CORNERS:
        word=''.join(model[i] for i in ids); assert len(set(word))==4
        types.append(name(word))
    assert sorted(types)==TYPES
    return types


def encoding():
    primary=['p'+''.join(map(str,c)) for c in CELLS]+TYPES
    secondary=['v'+''.join(map(str,v)) for v in VERTICES]
    options=[]
    for i,ids in enumerate(CORNERS):
        for w in WORDS:
            options.append([(primary[i],0),(name(w),0)]+[(secondary[v],ord(c)-96) for v,c in zip(ids,w)])
    return xcc.encode(primary,secondary,options)


def orbit(model):
    out=set()
    for p in permutations(range(4)):
        transformed=['?']*20
        for v,c in zip(VERTICES,model): transformed[INDEX[tuple(v[i] for i in p)]]=c
        for rename in permutations('abcde'):
            out.add(''.join(transformed).translate(str.maketrans('abcde',''.join(rename))))
    return out
