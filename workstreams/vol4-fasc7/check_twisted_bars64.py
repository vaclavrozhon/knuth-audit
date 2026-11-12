#!/usr/bin/env python3
"""Exact finite union witness for both64 drawings; no spatial search.

The native normalization and the explicit solids are independently
specified. Planar boundary cells certify the union, then exact ray tests
compare every visible interval with the original source network.
"""
from fractions import Fraction as F
from itertools import product,combinations
from collections import defaultdict,Counter
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT,sub,add,scale,dot,cross,cross2,at,on,geometric_visibility
from check_cubie_junctions import path_points
from check_hc_drawings26_27 import network
from check_hc_realizability28_29 import fit
from check_polyhedra_fixed import encode
from check_line_csp22 import propagate,ORDER


def clean(poly):
    q=[]
    for p in poly:
        if not q or q[-1]!=p:q.append(p)
    if len(q)>1 and q[0]==q[-1]:q.pop()
    if len(q)<3:return []
    if all(cross(sub(q[i],q[0]),sub(q[i+1],q[0]))==(0,0,0) for i in range(1,len(q)-1)):return []
    return q


def split(poly,plane):
    n,d=plane
    ds=[dot(n,p)+d for p in poly]
    if min(ds)>=0:return [],poly
    if max(ds)<=0:return poly,[]
    sides=[[],[]]
    for a,b,da,db in zip(poly,poly[1:]+poly[:1],ds,ds[1:]+ds[:1]):
        for side in (0,1):
            if da<=0 if side==0 else da>=0:sides[side].append(a)
        if da*db<0:
            p=at(a,b,da/(da-db));sides[0].append(p);sides[1].append(p)
    return clean(sides[0]),clean(sides[1])


def native(tag):
    if tag=='full':page,start,stop,origin,units='134',3089,3112,(F('191.7559'),F('518.414')),(F('1.417323'),F('2.834646'))
    else:page,start,stop,origin,units='188',179,190,(F('351.125'),F('406.2734')),(F('0.7086615'),F('1.417323'))
    paths=[p.attrib for p in ET.parse(ROOT/('sources/file-'+page+'.svg')).findall('.//{http://www.w3.org/2000/svg}path')]
    raw={i:path_points(paths[i]) for i in range(start,stop)}
    mapped={i:[tuple(F(round((p[k]-origin[k])/units[k])) for k in (0,1)) for p in ps] for i,ps in raw.items()}
    affine=[fit([(q[k],p[k]) for i,ps in raw.items() for p,q in zip(ps,mapped[i])]) for k in (0,1)]
    residual=max(sum((p[k]-affine[k][0]*q[k]-affine[k][1])**2 for k in (0,1)) for i,ps in raw.items() for p,q in zip(ps,mapped[i]))
    assert residual<F(1,10000)
    p,ns,rs,es,fs,bound=network(mapped,paths)
    ds={e:set(ORDER) for e in es}
    for a,b in zip(bound,bound[1:]+bound[:1]):ds['_'.join(sorted((a,b)))]={'>' if a<b else '<'}
    d,trace=propagate(rs,ds);assert d is not None and all(len(v)==1 for v in d.values())
    result={'points':p,'junctions':ns,'relations':rs,'lines':es,'faces':fs,'boundary':bound,'source_paths':mapped,'source_affine':affine,
            'source_max_residual_squared':residual,'domains':{k:next(iter(v)) for k,v in d.items()},'propagation':trace}
    (ROOT/f'results/twisted-bars64-{tag}-native.json').write_text(json.dumps(result,indent=2,default=encode)+'\n')
    return result


def spatial(n,L,tag):
    boxes=[];allplanes=[];originalfaces=[]
    for i in range(n):
        c,U,V=F(4*i+2),F(6*n-2*i),F(-2-2*i)
        planes=[((0,-1,-1),c),((0,1,1),-U),((0,-1,1),V),((0,1,-1),-c),((-1,0,-1),c),((1,0,-1),-L-c)]
        vs={}
        for a,b,t in product((0,1),repeat=3):
            u=(c,U)[a];v=(V,c)[b];y,z=(u+v)/2,(u-v)/2;x=(c-z,L+c+z)[t]
            vs[a,b,t]=(x,y,z)
        for fixed in range(3):
            varying=[k for k in range(3) if k!=fixed]
            for side in (0,1):
                poly=[]
                for uv in ((0,0),(1,0),(1,1),(0,1)):
                    b=[None]*3;b[fixed]=side
                    for k,v in zip(varying,uv):b[k]=v
                    poly.append(vs[tuple(b)])
                plane=planes[2*fixed+side]
                if dot(cross(sub(poly[1],poly[0]),sub(poly[2],poly[0])),plane[0])<0:poly.reverse()
                assert all(dot(plane[0],p)+plane[1]==0 for p in poly)
                originalfaces.append((i,6*i+2*fixed+side,poly))
        assert all(all(dot(a,p)+d<=0 for a,d in planes) for p in vs.values())
        boxes.append({'planes':planes,'vertices':list(vs.values()),'c':c,'U':U,'V':V})
        allplanes.extend(planes)
    tiles=[];partition_counts=[]
    for owner,planeid,poly in originalfaces:
        cells=[poly]
        for q,plane in enumerate(allplanes):
            if q==planeid:continue
            cells=[r for cell in cells for r in split(cell,plane) if r]
            assert len(cells)<1000
        retained=[]
        for cell in cells:
            mid=tuple(sum(p[k] for p in cell)/len(cell) for k in range(3))
            if any(j!=owner and all(dot(a,mid)+d<0 for a,d in box['planes']) for j,box in enumerate(boxes)):continue
            # No other face is coplanar, so a full-dimensional cell midpoint
            # cannot lie on an unrelated supporting plane.
            assert all(dot(allplanes[q][0],mid)+allplanes[q][1]!=0 for q in range(len(allplanes)) if q!=planeid)
            retained.append(cell);tiles.append((planeid,cell))
        partition_counts.append({'plane':planeid,'cells':len(cells),'exposed_cells':len(retained)})
    vertices=sorted({p for _,cell in tiles for p in cell});idx={p:i for i,p in enumerate(vertices)}
    supports=defaultdict(set)
    for pid,cell in tiles:
        for a,b in zip(cell,cell[1:]+cell[:1]):
            diff=sub(b,a);k=next(k for k in range(3) if diff[k])
            points=[]
            for p in vertices:
                if cross(sub(p,a),diff)!=(0,0,0):continue
                t=(p[k]-a[k])/diff[k]
                if 0<=t<=1:points.append((t,idx[p]))
            points.sort()
            for (_,u),(_,v) in zip(points,points[1:]):supports[tuple(sorted((u,v)))].add(pid)
    physical={e:ps for e,ps in supports.items() if len(ps)>1}
    assert all(len(ps)==2 for ps in physical.values())
    adjacency=defaultdict(dict)
    for (a,b),ps in physical.items():adjacency[a][b]=ps;adjacency[b][a]=ps
    while True:
        victim=next((j for j,ns in adjacency.items() if len(ns)==2 and len({tuple(sorted(x)) for x in ns.values()})==1
                     and cross(*[sub(vertices[k],vertices[j]) for k in ns])==(0,0,0)),None)
        if victim is None:break
        a,b=adjacency[victim];ps=adjacency[victim][a]
        del adjacency[a][victim];del adjacency[b][victim];del adjacency[victim]
        adjacency[a][b]=ps;adjacency[b][a]=ps
    assert all(len(ns)==3 for ns in adjacency.values()),Counter(len(ns) for ns in adjacency.values())
    edges=sorted({tuple(sorted((a,b))) for a,ns in adjacency.items() for b in ns})
    faces=[];face_planes=[]
    for pid in range(len(allplanes)):
        graph=defaultdict(set)
        for a,b in edges:
            if pid in adjacency[a][b]:graph[a].add(b);graph[b].add(a)
        assert graph and all(len(ns)==2 for ns in graph.values())
        remaining=set(graph);walks=[]
        while remaining:
            start=min(remaining);walk=[start];prev=None;cur=start
            while True:
                nxt=next(k for k in graph[cur] if k!=prev)
                if nxt==start:break
                walk.append(nxt);prev,cur=cur,nxt
            remaining-=set(walk);walks.append(walk)
        faces.extend(walks);face_planes.extend([pid]*len(walks))
    # The boundary is connected, closed,and every point has a manifold
    # polygonal neighborhood. All support triples are independent.
    seen={min(adjacency)};todo=list(seen)
    while todo:
        for k in adjacency[todo.pop()]:
            if k not in seen:seen.add(k);todo.append(k)
    assert seen==set(adjacency)
    triples=[]
    for j,ns in adjacency.items():
        ps=sorted(set().union(*ns.values()));assert len(ps)==3
        det=dot(allplanes[ps[0]][0],cross(allplanes[ps[1]][0],allplanes[ps[2]][0]));assert det
        triples.append({'vertex':j,'faces':ps,'determinant':det})
    model={'vertices':vertices,'edges':edges,'faces':faces,'convex_tiles':[[idx[p] for p in cell] for _,cell in tiles]}
    model['physical_vertices']=sorted(adjacency)
    model['planes']=allplanes;model['face_planes']=face_planes;model['tile_owners']=[p for p,_ in tiles];model['partition_counts']=partition_counts
    model['boxes']=boxes;model['vertex_support_triples']=triples
    model['euler_characteristic']=len(adjacency)-len(edges)+len(faces)
    assert model['euler_characteristic']==2
    (ROOT/f'results/twisted-bars64-{tag}-union.json').write_text(json.dumps(model,indent=2,default=encode)+'\n')
    print(json.dumps({'phase':'union','picture':tag,'V':len(adjacency),'E':len(edges),'F':len(faces),'tiles':len(tiles)}),flush=True)
    return model


def compare(model,source,tag):
    vs=model['vertices'];pp=[p[:2] for p in vs]
    intervals,atoms=geometric_visibility(model,vs,pp,(0,0,-1))
    adjacency=defaultdict(set)
    for ei,s,t in atoms:
        a,b=model['edges'][ei];p,q=at(pp[a],pp[b],s),at(pp[a],pp[b],t)
        adjacency[p].add(q);adjacency[q].add(p)
    while True:
        victim=next((p for p,ns in adjacency.items() if len(ns)==2 and cross2(*[sub(k,p) for k in ns])==0),None)
        if victim is None:break
        a,b=adjacency.pop(victim);adjacency[a].remove(victim);adjacency[b].remove(victim);adjacency[a].add(b);adjacency[b].add(a)
    actual={tuple(sorted((a,b))) for a,ns in adjacency.items() for b in ns}
    expected={tuple(sorted(tuple(source['points'][j]) for j in e.split('_'))) for e in source['lines']}
    assert actual==expected,{'extra':sorted(actual-expected),'missing':sorted(expected-actual)}
    stability=[]
    # Each visible T is a transverse crossing of exactly two spatial
    # edges at distinct depths. Other junctions are a single visible vertex.
    for j,p in source['points'].items():
        physical=[k for k in model['physical_vertices'] if pp[k]==p]
        kind=source['junctions'][j]['type']
        containing=[]
        for ei,(a,b) in enumerate(model['edges']):
            if on(p,pp[a],pp[b]):containing.append(ei)
        if kind=='T':
            # Behind-surface edges may also project here; only edges whose
            # visible interval has this endpoint or interior matter.
            relevant=[]
            for ei in containing:
                a,b=model['edges'][ei];k=next(k for k in (0,1) if pp[a][k]!=pp[b][k]);t=(p[k]-pp[a][k])/(pp[b][k]-pp[a][k])
                if any(s<=t<=u for s,u in intervals[ei]):relevant.append(ei)
            assert len(relevant)==2 and not physical
            dirs=[sub(pp[model['edges'][ei][1]],pp[model['edges'][ei][0]]) for ei in relevant]
            assert cross2(*dirs)
        else:
            visible_vertices=[]
            for k in physical:
                if any((a==k and any(s==0 for s,t in intervals[ei])) or(b==k and any(t==1 for s,t in intervals[ei])) for ei,(a,b) in enumerate(model['edges'])):visible_vertices.append(k)
            assert len(visible_vertices)==1
            relevant=[ei for ei in containing if visible_vertices[0] in model['edges'][ei] and intervals[ei]]
            assert len(relevant)==len(source['junctions'][j]['neighbors'])
        stability.append({'junction':j,'type':kind,'physical_vertices':physical,'relevant_physical_edges':relevant})
    result={'every_native_segment_matches':True,'physical_edge_visible_intervals':intervals,'junction_stability':stability,
            'visible_junction_count':len(adjacency),'visible_line_count':len(actual),'source_native':'twisted-bars64-'+tag+'-native.json','source_union':'twisted-bars64-'+tag+'-union.json'}
    (ROOT/f'results/twisted-bars64-{tag}-visibility.json').write_text(json.dumps(result,indent=2,default=encode)+'\n')
    print(json.dumps({'phase':'visibility','picture':tag,'junctions':len(adjacency),'lines':len(actual),'all_native_segments_match':True}),flush=True)


def main():
    for n,L,tag in ((2,F(84),'hint'),(4,F(92),'full')):
        source=native(tag);model=spatial(n,L,tag);compare(model,source,tag)


if __name__=='__main__':main()
