#!/usr/bin/env python3
"""Exact disjoint affine-cube witnesses for all four original arrays61.

The previously proved chip map converts strict whole-overlap depth orders
into spatial separation. Visibility is computed by interval clipping of
front edges against nearer projected hexagons, with no3D scene sampling.
"""
from fractions import Fraction as F
from itertools import product
import json
from check_clasp_projection import ROOT,sub,cross2,parameter,merge
from check_polyhedra_fixed import encode


def clip_interval(p,q,poly):
    lo,hi=F(0),F(1);d=sub(q,p)
    for a,b in zip(poly,poly[1:]+poly[:1]):
        v=sub(b,a);constant=cross2(v,sub(p,a));slope=cross2(v,d)
        if slope>0:lo=max(lo,-constant/slope)
        elif slope<0:hi=min(hi,-constant/slope)
        elif constant<0:return None
        if lo>=hi:return None
    return [lo,hi]


def complement(intervals):
    out=[];previous=F(0)
    for a,b in merge(intervals):
        if previous<a:out.append([previous,a])
        previous=b
    if previous<1:out.append([previous,F(1)])
    return out


def main():
    g=json.loads((ROOT/'results/box-arrays61-geometry.json').read_text())
    native=json.loads((ROOT/'results/box-arrays61-native-cache.json').read_text())['pictures']
    cells=list(product(range(6),repeat=2));centers={c:(F(-6*c[0]+5*c[1]),F(-c[0]+6*c[1])) for c in cells}
    offsets=[(0,-4),(4,0),(4,4),(0,4),(-4,0),(-4,-4)]
    outlines={c:[tuple(centers[c][k]+o[k] for k in (0,1)) for o in offsets] for c in cells}
    front=[]
    for ei,e in enumerate(g['all432_projected_edges']):
        a,b=e['bits'];fixed=[k for k in range(3) if a[k]==b[k]]
        if not all(a[k]==1 for k in fixed):
            front.append({'key':(tuple(e['cell']),tuple(a),tuple(b)),'points':[tuple(map(F,p)) for p in e['points']]})
    edges_by_key={e['key']:e for e in front};eps=F(1,100);origin=(F(-5,2),F(25,2));out=[]
    for pic,source in zip(g['pictures'],native):
        tag=pic['picture'];planes={};topo=[]
        if tag in ('i','ii'):
            adj={c:set() for c in cells};deg=dict.fromkeys(cells,0)
            for row in pic['observed_pair_orders']:
                a,b=map(tuple,row['cells']);f=tuple(row['front']);back=b if f==a else a
                if back not in adj[f]:adj[f].add(back);deg[back]+=1
            while len(topo)<36:
                ready=[c for c in cells if deg[c]==0 and c not in topo];assert ready
                v=min(ready);topo.append(v)
                for w in adj[v]:deg[w]-=1
            planes={c:(F(0),F(0),F(100*topo.index(c))) for c in cells}
        elif tag=='iii':planes={c:(F(0),F(0),F(100*(2-sum(c)%3))) for c in cells}
        else:
            assert tag=='iv'
            for cell in cells:
                r,s=cell;ring=min(r,s,5-r,5-s)
                def h(p):
                    if ring==2:return F(10000-100*(r+s))
                    value=cross2(sub(centers[cell],origin),sub(p,origin))
                    return value if ring==0 else -10000-value
                z=h((0,0));planes[cell]=(h((1,0))-z,h((0,1))-z,z)
        def height(cell,p):a,b,c=planes[cell];return a*p[0]+b*p[1]+c
        nearer={c:[] for c in cells};separations=[];orders={}
        for overlap in g['all85_overlap_polygons']:
            a,b=map(tuple,overlap['cells']);poly=[tuple(map(F,p)) for p in overlap['polygon']]
            values=[height(a,p)-height(b,p) for p in poly]
            assert min(values)>3*eps or max(values)<-3*eps,(tag,a,b,values)
            f,back=(b,a) if min(values)>0 else (a,b);nearer[back].append(f);orders[a,b]=f
            separations.append({'cells':[a,b],'front':f,'plane_difference_at_overlap_vertices':values,'solid_depth_gap_lower_bound':min(map(abs,values))-3*eps})
        for row in pic['observed_pair_orders']:
            a,b=map(tuple,row['cells']);assert orders[a,b]==tuple(row['front'])
        pp={j:tuple(map(F,p)) for j,p in source['points'].items()};expected={e['key']:[] for e in front}
        for row in pic['all_front_source_edges']:
            key=(tuple(row['cell']),*map(tuple,row['cube_edge_bits']));p,q=edges_by_key[key]['points'];a,b=row['line'].split('_')
            expected[key].append(sorted([parameter(pp[a],p,q),parameter(pp[b],p,q)]))
        visibility=[]
        for e in front:
            cell=e['key'][0];p,q=e['points'];hidden=[]
            for other in nearer[cell]:
                interval=clip_interval(p,q,outlines[other])
                if interval is not None:hidden.append(interval)
            visible=complement(hidden);wanted=merge(expected[e['key']])
            assert visible==wanted,(tag,e['key'],visible,wanted)
            visibility.append({'cell':cell,'bits':e['key'][1:],'visible_intervals':visible,'nearer_neighbor_cells':nearer[cell]})
        out.append({'picture':tag,'epsilon':eps,'depth_planes':[{'cell':c,'coefficients_x_y_1':planes[c]} for c in cells],
                    'topological_order_for_constant_planes':topo,'all85_solid_separations':separations,
                    'all324_front_edge_visibility_intervals':visibility,'every_native_line_matches':True})
        print('spatial',tag,'all324 front edges match; min gap',min(F(r['solid_depth_gap_lower_bound']) for r in separations),flush=True)
    (ROOT/'results/box-arrays61-spatial.json').write_text(json.dumps({'pictures':out,'same_chip_map_as':'notes/hc-reutersvard-032-059-060.md E59-1–3'},indent=2,default=encode)+'\n')


if __name__=='__main__':main()
