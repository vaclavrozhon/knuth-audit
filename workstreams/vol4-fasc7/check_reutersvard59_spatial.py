#!/usr/bin/env python3
"""A small explicit disjoint nine-chip strong witness for original32.

Each chip is an invertible affine image of a cube, preserving its exact
screen projection. The depth planes circulate around the central hole.
"""
from fractions import Fraction as F
from itertools import combinations,product
from collections import defaultdict
import json
from check_clasp_projection import ROOT,sub,cross2,at,geometric_visibility,dot,on
from check_polyhedra_fixed import clip,encode


def main():
    source=json.loads((ROOT/'results/reutersvard32-60.json').read_text())
    centers=[(F(x),F(y)) for x,y in [(4,20),(9,27),(14,34),(19,41),(20,30),(21,19),(22,8),(16,12),(10,16)]]
    origin=(F(15),F(23)); eps=F(1,100)
    offsets=[(0,-8),(4,-4),(4,4),(0,8),(-4,4),(-4,-4)]
    outlines=[[tuple(c[k]+o[k] for k in (0,1)) for o in offsets] for c in centers]
    def height(i,p): return -cross2(sub(centers[i],origin),sub(p,origin))
    separations=[]
    for i,j in combinations(range(9),2):
        overlap=clip(outlines[i],outlines[j])
        if not overlap:continue
        ds=[height(i,p)-height(j,p) for p in overlap]
        assert min(ds)>3*eps or max(ds)<-3*eps,(i,j,ds)
        separations.append({'boxes':[i,j],'overlap_polygon':overlap,'plane_depth_differences':ds,
                            'front_box':j if min(ds)>0 else i,'depth_gap_lower_bound':min(map(abs,ds))-3*eps})
    directions=[(-4,-4),(4,-4),(0,8)]; bits=list(product((0,1),repeat=3)); index={b:i for i,b in enumerate(bits)}
    vertices=[];projected=[];edges=[];faces=[]
    for i,c in enumerate(centers):
        for b in bits:
            p=tuple(c[k]+sum(b[j]*directions[j][k] for j in range(3)) for k in (0,1))
            projected.append(p);vertices.append((*p,height(i,p)+eps*sum(b)))
        for a,b in combinations(bits,2):
            if sum(x!=y for x,y in zip(a,b))==1:edges.append((8*i+index[a],8*i+index[b]))
        for fixed in range(3):
            varying=[k for k in range(3) if k!=fixed]
            for side in (0,1):
                f=[]
                for uv in [(0,0),(1,0),(1,1),(0,1)]:
                    b=[None]*3;b[fixed]=side
                    for k,v in zip(varying,uv):b[k]=v
                    f.append(8*i+index[tuple(b)])
                faces.append(f)
    model={'vertices':vertices,'edges':edges,'faces':faces,'convex_tiles':faces}
    intervals,atoms=geometric_visibility(model,vertices,projected,(0,0,-1))
    adjacency=defaultdict(set)
    for ei,s,t in atoms:
        a,b=edges[ei];p,q=at(projected[a],projected[b],s),at(projected[a],projected[b],t)
        adjacency[p].add(q);adjacency[q].add(p)
    while True:
        victim=next((p for p,ns in adjacency.items() if len(ns)==2 and cross2(sub(next(iter(ns)),p),sub(list(ns)[1],p))==0),None)
        if victim is None:break
        a,b=adjacency.pop(victim);adjacency[a].remove(victim);adjacency[b].remove(victim);adjacency[a].add(b);adjacency[b].add(a)
    actual={tuple(sorted((p,q))) for p,ns in adjacency.items() for q in ns}
    pp={j:tuple(map(F,p)) for j,p in source['points'].items()}
    expected={tuple(sorted((pp[a],pp[b]))) for a,b in (e.split('_') for e in source['lines'])}
    assert actual==expected,{'extra':sorted(actual-expected),'missing':sorted(expected-actual)}
    front_edges=[]
    for ei,(a,b) in enumerate(edges):
        ba,bb=bits[a%8],bits[b%8]
        fixed=[k for k in range(3) if ba[k]==bb[k]]
        if not all(ba[k]==1 for k in fixed):front_edges.append(ei)
    stability=[]
    for j,pt in pp.items():
        kind=source['junctions'][j]['type']
        pv=[k for k,p in enumerate(projected) if p==pt and bits[k%8]!=(1,1,1)]
        es=[ei for ei in front_edges if on(pt,projected[edges[ei][0]],projected[edges[ei][1]])]
        if kind=='T':
            assert not pv and len(es)==2
            a,b=[sub(projected[v],projected[u]) for u,v in (edges[ei] for ei in es)]
            assert cross2(a,b)
        else:
            assert len(pv)==1 and len(es)==len(source['junctions'][j]['neighbors'])
            assert all(pv[0] in edges[ei] for ei in es)
        stability.append({'junction':j,'type':kind,'front_physical_vertices':pv,'front_surface_edges_containing_projection':es})
    out={'centers':centers,'origin':origin,'epsilon':eps,'height_definition':'h_i(p)=-cross(c_i-origin,p-origin)',
         'cube_edge_screen_vectors':directions,'cube_bit_vertex_order':bits,'vertices':vertices,'edges':edges,'faces':faces,
         'all_overlap_depth_separations':separations,'every_spatial_edge_visible_intervals':intervals,
         'projected_junction_count':len(adjacency),'projected_line_count':len(actual),
         'every_native32_segment_matches':True,
         'all_visible_junction_stability_checks':stability,
         'scope':'One standard labeling realized by nine disjoint convex affine cubes. The seven variants with a concave center edge are not certified here.'}
    (ROOT/'results/reutersvard59-spatial.json').write_text(json.dumps(out,indent=2,default=encode)+'\n')
    print(json.dumps({'spatial_vertices':len(vertices),'spatial_edges':len(edges),'spatial_faces':len(faces),
                      'overlapping_pairs':len(separations),'junctions':len(adjacency),'lines':len(actual)}))


if __name__=='__main__':main()
