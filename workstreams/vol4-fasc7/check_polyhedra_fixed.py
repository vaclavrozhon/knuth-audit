#!/usr/bin/env python3
"""Exact certificates for fixed primary-source polyhedra, never a realization search."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent

def sub(a, b): return tuple(x-y for x, y in zip(a, b))
def add(a, b): return tuple(x+y for x, y in zip(a, b))
def scale(a, t): return tuple(x*t for x in a)
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def edges(c): return list(zip(c, c[1:]+c[:1]))
def normal(poly):
    return tuple(sum(cross(a,b)[k] for a,b in edges(poly)) for k in range(3))
def orient(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def area(poly): return sum(a[0]*b[1]-a[1]*b[0] for a,b in edges(poly))

def source(name, denominator):
    # The downloadable renderer rounds coordinates. The explicitly certified
    # rational reconstruction is a separate exact realization, with its error
    # reported; no floating point equality is used for geometry.
    match = re.search(r'^'+name+r'\s*:\s*(\{.*?\})', (ROOT/'sources/DEK.js').read_text(), re.M|re.S)
    # A few newer models supply exact a/b literals. Quote only those literals
    # and let the JSON parser read them; never evaluate downloaded JavaScript.
    body=re.sub(r'(?<![\w.])(-?\d+)/(\d+)(?![\w.])',r'"\1/\2"',match[1])
    data = json.loads(body, parse_float=str)
    raw = [tuple(F(x) for x in p) for p in data['vertex']]
    vertices = [tuple(x.limit_denominator(denominator) if denominator else x for x in p) for p in raw]
    error = max(abs(x-y) for p,q in zip(raw,vertices) for x,y in zip(p,q))
    assert error < F(1,100000)
    return data, vertices, error

def unique(poly):
    out=[]
    for p in poly:
        if p not in out: out.append(p)
    return out

def clip(poly, boundary):
    """Closed intersection of two convex planar polygons, exact arithmetic."""
    if area(boundary)<0: boundary=list(reversed(boundary))
    for a,b in edges(boundary):
        out=[]
        if not poly: break
        for p,q in edges(poly):
            s,t=orient(a,b,p),orient(a,b,q)
            if s>=0: out.append(p)
            if s*t<0: out.append(add(p,scale(sub(q,p),s/(s-t))))
        poly=unique(out)
    return poly

def convex(poly):
    n=normal(poly)
    assert n != (0,0,0)
    assert all(dot(n,sub(p,poly[0]))==0 for p in poly)
    omit=next(k for k in range(3) if n[k])
    pp=[tuple(x for k,x in enumerate(p) if k!=omit) for p in poly]
    a=area(pp)
    assert a and all(orient(x,y,z)*a>0 for x,y,z in zip(pp,pp[1:]+pp[:1],pp[2:]+pp[:2]))
    return n

def polygon_line(poly, other_n, other_d, coordinate):
    hits=[]
    for a,b in edges(poly):
        s,t=dot(other_n,a)-other_d,dot(other_n,b)-other_d
        if s==0: hits.append(a[coordinate])
        if s*t<0: hits.append((a[coordinate]*t-b[coordinate]*s)/(t-s))
    return None if not hits else (min(hits),max(hits))

def check_intersections(polys, indices, normals):
    checks=[]
    for i,j in combinations(range(len(polys)),2):
        a,b=polys[i],polys[j]; n,m=normals[i],normals[j]
        d,e=dot(n,a[0]),dot(m,b[0]); direction=cross(n,m)
        common=set(indices[i])&set(indices[j])
        if direction==(0,0,0):
            if dot(n,b[0])!=d:
                checks.append([i,j,'parallel_disjoint']); continue
            omit=next(k for k in range(3) if n[k])
            project=lambda p:tuple(x for k,x in enumerate(p) if k!=omit)
            hit=clip([project(p) for p in a],[project(p) for p in b])
            assert len(hit)<=2 and area(hit)==0, (i,j,'coplanar_area_overlap')
            expected={project(a[indices[i].index(v)]) for v in common}
            assert set(hit)==expected, (i,j,'unexpected_coplanar_contact',hit,expected)
            checks.append([i,j,'coplanar_expected_contact',len(hit)])
        else:
            k=next(k for k in range(3) if direction[k])
            x,y=polygon_line(a,m,e,k),polygon_line(b,n,d,k)
            hit=None if x is None or y is None or max(x[0],y[0])>min(x[1],y[1]) else (max(x[0],y[0]),min(x[1],y[1]))
            vals=[a[indices[i].index(v)][k] for v in common]
            expected=None if not vals else (min(vals),max(vals))
            assert hit==expected, (i,j,'unexpected_spatial_contact',hit,expected)
            checks.append([i,j,'nonparallel_expected_contact',len(common)])
    return checks

def triangulate(c,vertices):
    """Certify a simple polygon, then record a finite sequence of valid ears."""
    p=[vertices[i] for i in c];n=normal(p)
    assert n!=(0,0,0) and all(dot(n,sub(q,p[0]))==0 for q in p)
    omit=next(k for k in range(3) if n[k])
    pp={i:tuple(x for k,x in enumerate(vertices[i]) if k!=omit) for i in c}
    aa=area([pp[i] for i in c]);assert aa
    sign=1 if aa>0 else -1
    def on(p,a,b):return orient(a,b,p)==0 and all(min(x,y)<=z<=max(x,y) for z,x,y in zip(p,a,b))
    def intersect(a,b,c,d):
        x,y,z,w=orient(a,b,c),orient(a,b,d),orient(c,d,a),orient(c,d,b)
        return x*y<0 and z*w<0 or on(c,a,b) or on(d,a,b) or on(a,c,d) or on(b,c,d)
    for i,(a,b) in enumerate(edges(c)):
        for j,(u,v) in enumerate(edges(c)):
            if i<j and not {a,b}&{u,v}:assert not intersect(pp[a],pp[b],pp[u],pp[v])
    left=c[:];out=[]
    while len(left)>3:
        for k,b in enumerate(left):
            a,d=left[k-1],left[(k+1)%len(left)]
            if orient(pp[a],pp[b],pp[d])*sign<=0:continue
            if any(all(orient(pp[u],pp[v],pp[w])*sign>=0 for u,v in [(a,b),(b,d),(d,a)])
                   for w in left if w not in (a,b,d)):continue
            if any(intersect(pp[a],pp[d],pp[u],pp[v]) for u,v in edges(left) if not {a,d}&{u,v}):continue
            out.append([a,b,d]);left.pop(k);break
        else:raise AssertionError(('no certified ear',c,left))
    out.append(left)
    assert sum(area([pp[i] for i in t]) for t in out)==aa
    return out

def certify(name, denominator, triangulate_all=False, coordinate_overrides=None):
    data, vertices, reconstruction_error = source(name,denominator)
    original_vertices=vertices[:]
    if coordinate_overrides:
        for i,v in coordinate_overrides.items():vertices[i]=tuple(v)
    assert len(set(vertices))==len(vertices)
    original_tiles=data['face']
    tiles=[]
    for c in original_tiles:
        if triangulate_all:
            tiles.extend(triangulate(c,vertices));continue
        p=[vertices[i] for i in c]
        n=normal(p); omit=next(k for k in range(3) if n[k])
        pp=[tuple(x for k,x in enumerate(v) if k!=omit) for v in p]
        a=area(pp)
        reflex=[i for i in range(len(c)) if orient(pp[i-1],pp[i],pp[(i+1)%len(c)])*a<0]
        if reflex:
            assert len(c)==4 and len(reflex)==1
            r=reflex[0]; q=c[r:]+c[:r]
            tiles.extend([q[:3],[q[0],q[2],q[3]]])
        else: tiles.append(c)
    polys=[[vertices[i] for i in c] for c in tiles]
    normals=[convex(p) for p in polys]
    incidence=defaultdict(list)
    for i,c in enumerate(tiles):
        for a,b in edges(c): incidence[tuple(sorted((a,b)))].append((i,a,b))
    reoriented=[]
    if triangulate_all:
        assert all(len(v)==2 for v in incidence.values())
        adjacency=defaultdict(list)
        for entries in incidence.values():
            (i,a,b),(j,c,d)=entries
            factor=-1 if (a,b)==(c,d) else 1
            adjacency[i].append((j,factor));adjacency[j].append((i,factor))
        directions={}
        for root in range(len(tiles)):
            if root in directions:continue
            directions[root]=1;todo=[root]
            while todo:
                i=todo.pop()
                for j,factor in adjacency[i]:
                    wanted=directions[i]*factor
                    if j in directions:assert directions[j]==wanted
                    else:directions[j]=wanted;todo.append(j)
        reoriented=[i for i,s in directions.items() if s<0]
        for i in reoriented:tiles[i].reverse()
        polys=[[vertices[i] for i in c] for c in tiles]
        normals=[convex(p) for p in polys]
        incidence=defaultdict(list)
        for i,c in enumerate(tiles):
            for a,b in edges(c):incidence[tuple(sorted((a,b)))].append((i,a,b))
    assert all(len(v)==2 and v[0][1:]==v[1][1:][::-1] for v in incidence.values())
    physical={tuple(sorted(e)) for e in data['edge']}
    assert len(physical)==len(data['edge'])
    assert set(Counter(v for e in physical for v in e).values())=={3}
    assert physical<=incidence.keys()
    parent=list(range(len(polys)))
    def find(i):
        while parent[i]!=i:i=parent[i]
        return i
    for edge,entries in incidence.items():
        i,j=entries[0][0],entries[1][0]
        coplanar=cross(normals[i],normals[j])==(0,0,0)
        assert coplanar==(edge not in physical), (name,edge,coplanar)
        if coplanar:parent[find(i)]=find(j)
    groups=defaultdict(list)
    for i in range(len(polys)):groups[find(i)].append(i)
    volume6=sum(dot(p[0],cross(p[i],p[i+1])) for p in polys for i in range(1,len(p)-1))
    assert volume6
    orientation=1 if volume6>0 else -1
    signs={}
    for edge in sorted(physical):
        (i,a,b),(j,_,_)=incidence[edge]
        value=orientation*dot(normals[j],cross(normals[i],sub(vertices[b],vertices[a])))
        assert value
        signs[str(edge)]='concave' if value>0 else 'convex'
    intersections=check_intersections(polys,tiles,normals)
    cycles=[]
    for group_tiles in groups.values():
        boundary=[(a,b) for i in group_tiles for a,b in edges(tiles[i]) if tuple(sorted((a,b))) in physical]
        nxt=dict(boundary)
        assert len(nxt)==len(boundary) and set(nxt)==set(nxt.values())
        unseen=set(nxt); loops=[]
        while unseen:
            v=min(unseen); start=v; loop=[]
            while v in unseen:loop.append(v);unseen.remove(v);v=nxt[v]
            assert v==start
            loops.append(loop)
        cycles.append({'tiles':group_tiles,'boundary_cycles':loops})
    return {'name':name,'vertices':vertices,'source_coordinate_error_bound':reconstruction_error,
            'rational_reconstruction_max_denominator':denominator,'edges':data['edge'],
            'explicit_coordinate_overrides':coordinate_overrides or {},
            'original_overridden_coordinates':{i:original_vertices[i] for i in (coordinate_overrides or {})},
            'original_rendering_tiles':original_tiles,'convex_tiles':tiles,'merged_faces':cycles,'edge_signs':signs,
            'reoriented_tile_indices':reoriented,
            'counts':{'vertices':len(vertices),'edges':len(physical),'faces':len(groups),
                      'boundary_polygons':sum(len(x['boundary_cycles']) for x in cycles),
                      'concave_edges':list(signs.values()).count('concave')},
            'oriented_volume6':volume6,'pairwise_intersections':intersections}

def encode(x):
    if isinstance(x,F):return int(x) if x.denominator==1 else str(x)
    raise TypeError(type(x).__name__)

def add_topology_certificate(result):
    for name,obj in result.items():
        vv=[tuple(F(t) for t in v) for v in obj['vertices']]
        tiles=obj['convex_tiles']; adj={i:set() for i in range(len(vv))}
        for c in tiles:
            for a,b in edges(c):adj[a].add(b);adj[b].add(a)
        unseen=set(adj); comps=[]
        while unseen:
            co={unseen.pop()}; todo=list(co)
            while todo:
                for w in adj[todo.pop()]:
                    if w in unseen:unseen.remove(w);co.add(w);todo.append(w)
            vol=sum(dot(vv[c[0]],cross(vv[c[i]],vv[c[i+1]]))
                    for c in tiles if c[0] in co for i in range(1,len(c)-1))
            assert vol*F(obj['oriented_volume6'])>0
            comps.append({'vertices':sorted(co),'oriented_volume6':vol})
        obj['surface_components']=comps
        if name.startswith('C8'):
            assert {tuple(sorted(e)) for e in obj['edges']}=={
                (i,j) for i in range(8) for j in range(i+1,8) if i^j in (1,2,4)}
    obj=result['Clasp']; vs=[tuple(F(t) for t in v) for v in obj['vertices']]
    assert all(vs[i+10]==(-vs[i][0],vs[i][1],-vs[i][2]) for i in range(10))
    n=cross(sub(vs[1],vs[0]),sub(vs[2],vs[0])); d=dot(n,vs[0]); crossings=[]
    for a,b in [(10,11),(11,12),(12,10)]:
        x,y=dot(n,vs[a])-d,dot(n,vs[b])-d
        assert x and y
        if x*y<0:
            pt=add(vs[a],scale(sub(vs[b],vs[a]),x/(x-y)))
            omit=next(k for k in range(3) if n[k])
            pr=lambda p:tuple(t for k,t in enumerate(p) if k!=omit)
            tri=[pr(vs[i]) for i in [0,1,2]]; q=pr(pt)
            inside=all(orient(v,w,q)*area(tri)>0 for v,w in edges(tri))
            assert all(orient(v,w,q) for v,w in edges(tri))
            crossings.append({'edge':[a,b],'point':pt,'inside_spanning_triangle':inside})
    assert sum(x['inside_spanning_triangle'] for x in crossings)==1
    obj['linking_triangle']=[0,1,2];obj['other_closed_edge_cycle']=[10,11,12]
    obj['transverse_intersections']=crossings
    return result

if __name__=='__main__':
    result={name:certify(name,den) for name,den in [('Clasp',22),('C8A',40),('C8B',14),('C8C',10),('C8D',22)]}
    add_topology_certificate(result)
    (ROOT/'results/polyhedra-fixed.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=encode)+'\n')
    print(json.dumps({k:v['counts'] for k,v in result.items()}))
