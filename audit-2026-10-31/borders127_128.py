"""Boundary and eleven-triangle models; separate from the completed126 runs."""
from collections import defaultdict
from itertools import product
from pathlib import Path
import gzip,re
import check_macmahon as g
import macmahon126 as mc
from border_orbits127 import boundary,endpoints

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/borders127_128'
CELLS128=[(x,y,z) for x in range(3) for y in range(2) for z in range(2)
          if (x,y,z)!=(2,1,1)]
PAIRS128=[(('-',0,0),('-',2,0)),(('/',0,1),('/',3,0)),(('-',0,2),('-',1,2))]


def problem127(word):
    assert len(word)==12 and set(word)<=set('0123')
    enc=mc.problem('full');enc['word']=word
    enc['rows'][-1]=['*']+[mc.edge_name(e)+':'+chr(97+int(c)) for e,c in zip(boundary(),word)]
    return enc


def problem128():
    pieces=sorted({g.piece(cs) for cs in product('abc',repeat=3)})
    edges=sorted({e for t in CELLS128 for e in g.edges(t)})
    mapping={e:e for e in edges}
    for a,b in PAIRS128:
        assert mapping[a]==a and mapping[b]==b;mapping[b]=a
    representatives=sorted(set(mapping.values()))
    primary=[g.name(t) for t in CELLS128]+pieces
    header=primary+['|']+[mc.edge_name(e) for e in representatives]
    rows=[];placements=[]
    for t in CELLS128:
        for tile in pieces:
            for cs in sorted({tile[i:]+tile[:i] for i in range(3)}):
                row=[g.name(t),tile]+[mc.edge_name(mapping[e])+':'+c for e,c in zip(g.edges(t),cs)]
                assert len(set(x.split(':')[0] for x in row))==5
                rows.append(row);placements.append(dict(cell=t,colors=cs,tile=tile))
    assert len(pieces)==11 and len(edges)==21 and len(representatives)==18 and len(rows)==297
    return dict(header=header,rows=rows,placements=placements,primary_names=primary,
                cells=CELLS128,pieces=pieces,edges=edges,representatives=representatives,mapping=mapping)


def selected_models(path,enc):
    lookup={tuple(sorted(row)):i for i,row in enumerate(enc['rows'])}
    assert len(lookup)==len(enc['rows']);model=None
    with gzip.open(path,'rt') as f:
        for line in f:
            if re.fullmatch(r'\d+:\s*',line):
                if model is not None:yield tuple(sorted(model))
                model=[]
            elif line.strip():
                tokens=re.sub(r'\s*\(\d+ of \d+\)\s*$','',line).split()
                assert model is not None;model.append(lookup[tuple(sorted(tokens))])
    if model is not None:yield tuple(sorted(model))


def geometric_colors(model,enc):
    """Check edge sharing by actual endpoints, independently of XCC names."""
    seen=set();colors={};tiles=[];forced=0
    for i in model:
        p=enc['placements'][i]
        if p is None:forced+=1;continue
        t=tuple(p['cell']);assert t not in seen;seen.add(t)
        cs=p['colors'];tiles.append(g.piece(cs))
        u,v,w=g.vertices(t)
        a,b=(v,u) if t[2] else (u,v)
        for pair,c in zip([(w,a),(w,b),(u,v)],cs):
            e=frozenset(pair);assert e not in colors or colors[e]==c;colors[e]=c
    expected_cells=enc.get('cells',g.TRIANGLES)
    assert seen==set(expected_cells) and sorted(tiles)==enc.get('pieces',g.PIECES)
    assert forced==int('word' in enc)
    return {e:colors[endpoints(e)] for e in enc['edges']}


def validate127(vector,enc):
    assert len(vector)==42 and set(vector)<=set('abcd')
    colors=dict(zip(map(tuple,enc['edges']),vector))
    pieces=[g.piece(''.join(colors[e] for e in g.edges(t))) for t in g.TRIANGLES]
    assert sorted(pieces)==g.PIECES
    assert ''.join(str(ord(colors[e])-97) for e in boundary())==enc['word']


def validate128(vector,enc):
    assert len(vector)==18 and set(vector)<=set('abc')
    values=dict(zip(enc['representatives'],vector))
    colors={e:values[enc['mapping'][e]] for e in enc['edges']}
    pieces=[g.piece(''.join(colors[e] for e in g.edges(t))) for t in CELLS128]
    assert sorted(pieces)==enc['pieces']
    assert all(colors[a]==colors[b] for a,b in PAIRS128)
    return colors


def plane_quotient128():
    """22 triangle cosets and33 edge cosets prove an infinite periodic tiling."""
    phi=lambda x,y:(x-8*y)%11
    rotation=lambda t:(2-t[0],-1-t[1],1-t[2])
    def rotate_edge(e):
        k,x,y=e
        return (k,2-x,-y) if k=='-' else (k,3-x,-1-y) if k=='/' else (k,2-x,-1-y)
    cosets={};incidences=defaultdict(list)
    for t in CELLS128:
        for halfturn in (False,True):
            u=rotation(t) if halfturn else t
            key=(phi(u[0],u[1]),u[2]);assert key not in cosets
            cosets[key]=dict(cell=u,source=t,halfturn=halfturn)
            for e in g.edges(t):
                moved=rotate_edge(e) if halfturn else e
                assert moved in g.edges(u)
                # Also check the half-turn on actual edge endpoints.
                if halfturn:assert endpoints(moved)==frozenset((3-x,-y) for x,y in endpoints(e))
                incidences[(moved[0],phi(moved[1],moved[2]))].append(e)
    assert set(cosets)==set(product(range(11),(0,1)))
    assert len(incidences)==33 and all(len(v)==2 for v in incidences.values())
    equalities={frozenset(v) for v in incidences.values() if v[0]!=v[1]}
    assert equalities=={frozenset(pair) for pair in PAIRS128}
    basis=[(3,-1),(2,3)]
    assert basis[0][0]*basis[1][1]-basis[0][1]*basis[1][0]==11
    assert all(phi(*v)==0 for v in basis)
    return dict(lattice_basis=basis,lattice_index=11,coset_function='(x-8y) mod11',
                halfturn_on_points='(x,y) -> (3-x,-y)',
                triangle_cosets=[dict(residue=k[0],orientation=k[1],**v) for k,v in sorted(cosets.items())],
                edge_cosets=[dict(kind=k[0],residue=k[1],source_edges=v) for k,v in sorted(incidences.items())],
                necessary_and_sufficient_equalities=PAIRS128)
