#!/usr/bin/env python3
"""Reuse closed geometry26; certify signs, Fano incidence and printed graph36."""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter,defaultdict
import json,re,xml.etree.ElementTree as E
from check_polyhedra_fixed import ROOT,sub,dot,cross,normal,edges,encode

def check():
    d=json.loads((ROOT/'results/szilassi-exact.json').read_text())
    vertices={n:tuple(F(t) for t in v) for n,v in d['vertices'].items()}
    cycles={f['face']:f['cycle'][:] for f in d['faces']}
    for k,c in cycles.items():
        if d['consistent_cycle_orientation_signs'][str(k)]<0:c.reverse()
    volume6=sum(dot(vertices[c[0]],cross(vertices[c[i]],vertices[c[i+1]])) for c in cycles.values() for i in range(1,len(c)-1))
    assert volume6
    orientation=1 if volume6>0 else -1
    normals={k:normal([vertices[n] for n in c]) for k,c in cycles.items()}
    incidence=defaultdict(list)
    for k,c in cycles.items():
        for a,b in edges(c):incidence[tuple(sorted((a,b)))].append((k,a,b))
    signs={}
    for edge,((i,a,b),(j,_,_)) in incidence.items():
        value=orientation*dot(normals[j],cross(normals[i],sub(vertices[b],vertices[a])))
        assert value
        signs[edge]='concave' if value>0 else 'convex'
    positive='023 134 245 356 460 501 612'.split()
    negative='054 165 206 310 421 532 643'.split()
    assert set(incidence)=={tuple(sorted((positive[i],negative[j]))) for i in range(7) for j in range(7) if (j-i)%7 in (2,3,5)}
    point_vectors=[1,2,4,5,7,3,6]
    line_vectors=[]
    parity=lambda a,b:(a&b).bit_count()%2
    for j in range(7):
        pts=[point_vectors[i] for i in range(7) if (j-i)%7 in (2,3,5)]
        ns=[n for n in range(1,8) if all(parity(n,p)==0 for p in pts)]
        assert len(ns)==1;line_vectors.extend(ns)
    assert len(set(line_vectors))==7
    # Half-turn about the z axis, with the induced permutation of seven planes.
    permutation={0:0,1:6,6:1,2:5,5:2,3:4,4:3}
    rotation={}
    for name,p in vertices.items():
        target=next(n for n in vertices if set(n)=={str(permutation[int(i)]) for i in name})
        assert vertices[target]==(-p[0],-p[1],p[2]);rotation[name]=target
    # Read every solid/dashed segment of the original diagram (not a redraw).
    root=E.parse(ROOT/'sources/file-181.svg').getroot();points=[];draw={}
    for p in root.findall('.//{http://www.w3.org/2000/svg}path'):
        if p.get('stroke')!='rgb(0%, 0%, 0%)' or re.search('[CQASTHV]',p.get('d','')):continue
        t=list(map(F,re.findall(r'[-+]?(?:\d*\.\d+|\d+)',p.get('transform',''))))
        if len(t)!=6:continue
        a,b,c,d,e,f=t
        pp=[(a*F(x)+c*F(y)+e,b*F(x)+d*F(y)+f) for x,y in re.findall(r'[ML] ([-\d.]+) ([-\d.]+)',p.get('d',''))]
        if not pp or not all(350<x<425 and 365<y<432 for x,y in pp):continue
        ids=[]
        for q in pp:
            match=[i for i,v in enumerate(points) if sum((x-y)**2 for x,y in zip(q,v))<F(1,10000)]
            assert len(match)<=1
            if match:i=match[0]
            else:i=len(points);points.append(q)
            ids.append(i)
        for i,j in zip(ids,ids[1:]):
            edge=tuple(sorted((i,j)));assert edge not in draw
            draw[edge]='concave' if 'stroke-dasharray' in p.attrib else 'convex'
    assert len(points)==14 and len(draw)==21
    neighbors={v:{} for v in vertices}; dn={v:{} for v in range(14)}
    for (a,b),s in signs.items():neighbors[a][b]=s;neighbors[b][a]=s
    for (a,b),s in draw.items():dn[a][b]=s;dn[b][a]=s
    count=0
    def match(mapping):
        nonlocal count
        count+=1
        if len(mapping)==14:return mapping
        a=max((v for v in vertices if v not in mapping),key=lambda v:sum(n in mapping for n in neighbors[v]))
        for b in dn:
            if b in mapping.values() or Counter(neighbors[a].values())!=Counter(dn[b].values()):continue
            if all(neighbors[a].get(v)==dn[b].get(w) for v,w in mapping.items()):
                got=match({**mapping,a:b})
                if got:return got
    mapping=match({});assert mapping
    return {'edge_signs':[{'edge':list(e),'sign':s} for e,s in sorted(signs.items())],
            'concave_edges':[list(e) for e,s in sorted(signs.items()) if s=='concave'],
            'oriented_volume6':volume6,'positive_vertices':positive,'negative_vertices':negative,
            'point_vectors_in_F2_3':point_vectors,'line_normal_vectors_in_F2_3':line_vectors,
            'half_turn_vertex_permutation':rotation,'half_turn_plane_permutation':permutation,
            'printed_graph_points':points,'printed_graph_edges':[{'edge':list(e),'sign':s} for e,s in sorted(draw.items())],
            'source_vertex_to_printed_graph_vertex':mapping,'small_isomorphism_nodes_visited':count,
            'scope':'Signs and graph only. The complete geometry proof26 is reused, never rerun. Automorphism count336 has the separate general Fano-space argument.'}

if __name__=='__main__':
    r=check();(ROOT/'results/szilassi-signature.json').write_text(json.dumps(r,ensure_ascii=False,indent=2,default=encode)+'\n')
    print(json.dumps({'concave_edges':r['concave_edges'],'printed_graph_matches':True,'mapping_nodes':r['small_isomorphism_nodes_visited']}))
