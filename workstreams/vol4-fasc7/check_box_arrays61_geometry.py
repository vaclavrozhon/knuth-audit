#!/usr/bin/env python3
"""Corrected barycentric map, every inter-box crossing and native layer orders."""
from fractions import Fraction as F
from itertools import combinations,product
from collections import Counter
import json
from check_clasp_projection import ROOT,sub,cross2,on
from check_polyhedra_fixed import clip,encode


def main():
    pics=json.loads((ROOT/'results/box-arrays61.json').read_text())['pictures']
    cells=list(product(range(6),repeat=2));centers={c:(F(-6*c[0]+5*c[1]),F(-c[0]+6*c[1])) for c in cells}
    dirs=[(F(4),F(0)),(F(-4),F(-4)),(F(0),F(4))];bits=list(product((0,1),repeat=3))
    vertices={c:{b:tuple(centers[c][k]+sum(b[j]*dirs[j][k] for j in range(3)) for k in (0,1)) for b in bits} for c in cells}
    full_edges=[];front_edges=[];front_vertices=[];formula=[]
    outlines={}
    for cell in cells:
        r,s=cell;i,j=s,5-r
        for b,p in vertices[cell].items():
            x,y,z=2*b[0]-1,2*b[1]-1,1-2*b[2]
            A=6*i+j-2*y-2*z;B=-i+5*j+2*x+2*z;C=-5*i-6*j-2*x+2*y
            assert A+B+C==0
            assert p==(A+B-30,A-5)
            formula.append({'cell':cell,'book_i_j':[i,j],'cube_vertex':[x,y,z],'barycentric':[A,B,C],'native_grid_point':p})
            if b!=(1,1,1):front_vertices.append((cell,b,p))
        for a,b in combinations(bits,2):
            if sum(x!=y for x,y in zip(a,b))!=1:continue
            row={'cell':cell,'bits':[a,b],'points':[vertices[cell][a],vertices[cell][b]]};full_edges.append(row)
            fixed=[k for k in range(3) if a[k]==b[k]]
            if not all(a[k]==1 for k in fixed):front_edges.append(row)
        # Positive polygon order in the integer screen grid.
        offsets=[(0,-4),(4,0),(4,4),(0,4),(-4,0),(-4,-4)]
        outlines[cell]=[tuple(centers[cell][k]+o[k] for k in (0,1)) for o in offsets]
    overlaps=[]
    for a,b in combinations(cells,2):
        polygon=clip(outlines[a],outlines[b])
        if polygon:overlaps.append({'cells':[a,b],'polygon':polygon})
    expected={tuple(sorted((a,(a[0]+dr,a[1]+ds)))) for a in cells for dr,ds in [(1,0),(0,1),(1,1)] if (a[0]+dr,a[1]+ds) in centers}
    assert {tuple(map(tuple,r['cells'])) for r in overlaps}==expected and len(overlaps)==85
    bycell={c:[(ei,e) for ei,e in enumerate(full_edges) if e['cell']==c] for c in cells}
    crossings={};crossing_list=[]
    for overlap in overlaps:
        a,b=overlap['cells']
        for ei,e in bycell[a]:
            p,q=e['points'];u=sub(q,p)
            for fi,f in bycell[b]:
                r,s=f['points'];v=sub(s,r);den=cross2(u,v)
                if not den:
                    assert not on(p,r,s) and not on(q,r,s) and not on(r,p,q) and not on(s,p,q)
                    continue
                t=cross2(sub(r,p),v)/den;w=cross2(sub(r,p),u)/den
                if not(0<=t<=1 and 0<=w<=1):continue
                assert 0<t<1 and 0<w<1
                hit=tuple(p[k]+t*u[k] for k in (0,1))
                assert hit not in crossings,(hit,crossings.get(hit),(ei,fi))
                assert not any(hit==p0 for c,b0,p0 in front_vertices)
                crossings[hit]=(ei,fi);crossing_list.append({'point':hit,'edges':[ei,fi],'parameters':[t,w]})
    output=[]
    for pic in pics:
        pp={j:tuple(map(F,p)) for j,p in pic['points'].items()};owner={};orders={};junction_checks=[]
        for j,r in pic['junctions'].items():
            p=pp[j];vs=[(cell,b) for cell,b,q in front_vertices if p==q]
            containing=[e for e in front_edges if on(p,*e['points'])]
            if r['type']=='T':
                assert not vs and len(containing)==2
                bar=sub(pp[r['neighbors'][0]],p)
                front=next(e for e in containing if cross2(bar,sub(e['points'][1],e['points'][0]))==0)
                back=next(e for e in containing if e is not front)
                pair=tuple(sorted((front['cell'],back['cell'])))
                assert pair not in orders or orders[pair]==front['cell']
                orders[pair]=front['cell']
                junction_checks.append({'junction':j,'front_cell':front['cell'],'back_cell':back['cell']})
            else:
                assert len(vs)==1 and len(containing)==len(r['neighbors']),(pic['picture'],j,vs,len(containing))
                owner[j]=vs[0][0]
        assert len([j for j,r in pic['junctions'].items() if r['type']=='Y'])==36
        assert {pp[j] for j,r in pic['junctions'].items() if r['type']=='Y'}==set(centers.values())
        # Every visible source segment belongs to exactly one original front
        # edge; thus the corrected map accounts for every stroke, not only Ys.
        source_edges=[]
        for line in pic['lines']:
            a,b=line.split('_');matches=[e for e in front_edges if on(pp[a],*e['points']) and on(pp[b],*e['points'])]
            assert len(matches)==1,(pic['picture'],line,len(matches))
            source_edges.append({'line':line,'cell':matches[0]['cell'],'cube_edge_bits':matches[0]['bits']})
        factor_owners=[]
        for c in pic['standard_certificate']['components']:
            js={r['junction'] for r in c['constraints'] if pic['junctions'][r['junction']]['type']!='T'}
            co={owner[j] for j in js};assert len(co)==1,(pic['picture'],c['count'],co)
            cell=next(iter(co));factor_owners.append({'cell':cell,'count':c['count'],'nonT_junctions':sorted(js),
                                                   'nonT_types':[pic['junctions'][j]['type'] for j in sorted(js)]})
        output.append({'picture':pic['picture'],'all_front_source_edges':source_edges,'nonT_vertex_owners':owner,
                       'T_depth_order_checks':junction_checks,'observed_pair_orders':[{'cells':pair,'front':front} for pair,front in sorted(orders.items())],
                       'factor_owners':factor_owners})
        print(pic['picture'],'observed pair orders',len(orders),'factors',dict(Counter(c['count'] for c in factor_owners)),flush=True)
    (ROOT/'results/box-arrays61-geometry.json').write_text(json.dumps({'corrected_formula_at_all288_corners':formula,
         'all432_projected_edges':full_edges,'all85_overlap_polygons':overlaps,'all_interbox_edge_crossings':crossing_list,
         'every_crossing_distinct_and_away_from_all_corners':True,'pictures':output},indent=2,default=encode)+'\n')
    print('unique transverse inter-box crossings',len(crossing_list))


if __name__=='__main__':main()
