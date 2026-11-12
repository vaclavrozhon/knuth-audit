#!/usr/bin/env python3
"""Small follow-up certificates; reuses64 union/visibility caches."""
from fractions import Fraction as F
import json
from collections import Counter,defaultdict
from check_clasp_projection import ROOT,sub,cross,cross2,dot,at
from check_polyhedra_fixed import encode


def main():
    out={}
    for n,L,tag in ((2,F(84),'hint'),(4,F(92),'full')):
        p=json.loads((ROOT/f'results/twisted-bars64-{tag}-native.json').read_text())
        m=json.loads((ROOT/f'results/twisted-bars64-{tag}-union.json').read_text())
        v=json.loads((ROOT/f'results/twisted-bars64-{tag}-visibility.json').read_text())
        vertices=[tuple(map(F,x)) for x in m['vertices']]
        center=(L/2+2*n,F(2*n),F(2*n))
        margins=[-(dot(tuple(map(F,a)),center)+F(d)) for a,d in m['planes']]
        assert min(margins)>0
        crossings=[]
        for r in v['junction_stability']:
            if r['type']!='T':continue
            pt=tuple(map(F,p['points'][r['junction']]))
            z=[];directions=[]
            for ei in r['relevant_physical_edges']:
                a,b=[vertices[i] for i in m['edges'][ei]];k=next(k for k in(0,1) if a[k]!=b[k])
                t=(pt[k]-a[k])/(b[k]-a[k]);assert 0<t<1
                z.append(at(a,b,t)[2]);directions.append(sub(b[:2],a[:2]))
            assert abs(z[0]-z[1])==2 and cross2(*directions)
            crossings.append({'junction':r['junction'],'depths':z,'gap':abs(z[0]-z[1]),'crossing_determinant':cross2(*directions)})
        assert all(F(a[2])!=0 for a,d in m['planes'])
        assert all(vertices[a][:2]!=vertices[b][:2] for a,b in m['edges'])
        face_components=[]
        for pid in range(len(m['planes'])):
            tiles=[t for t,q in enumerate(m['tile_owners']) if q==pid]
            points=sorted({j for t in tiles for j in m['convex_tiles'][t]})
            atoms=defaultdict(set)
            for t in tiles:
                cell=m['convex_tiles'][t]
                for a,b in zip(cell,cell[1:]+cell[:1]):
                    d=sub(vertices[b],vertices[a]);k=next(k for k in range(3) if d[k]);cuts=[]
                    for j in points:
                        if cross(sub(vertices[j],vertices[a]),d)!=(0,0,0):continue
                        s=(vertices[j][k]-vertices[a][k])/d[k]
                        if 0<=s<=1:cuts.append((s,j))
                    cuts.sort()
                    for (_,a),(_,b) in zip(cuts,cuts[1:]):atoms[tuple(sorted((a,b)))].add(t)
            adj={t:set() for t in tiles}
            for ts in atoms.values():
                assert len(ts) in(1,2)
                for t in ts:adj[t].update(ts-{t})
            remaining=set(tiles);components=[]
            while remaining:
                c={min(remaining)};todo=list(c)
                while todo:
                    for t in adj[todo.pop()]-c:c.add(t);todo.append(t)
                remaining-=c;boundary=defaultdict(set)
                for (a,b),ts in atoms.items():
                    if len(ts)==1 and ts<=c:boundary[a].add(b);boundary[b].add(a)
                assert boundary and all(len(ns)==2 for ns in boundary.values())
                reached={min(boundary)};todo=list(reached)
                while todo:
                    for j in boundary[todo.pop()]-reached:reached.add(j);todo.append(j)
                assert reached==set(boundary)
                physical=set(boundary)&set(m['physical_vertices'])
                matches=[f for f,q in zip(m['faces'],m['face_planes']) if q==pid and set(f)==physical]
                assert len(matches)==1
                components.append({'tiles':sorted(c),'physical_boundary':matches[0],'single_boundary_cycle':True})
            face_components.append({'plane':pid,'components':components})
        assert sum(len(x['components']) for x in face_components)==len(m['faces'])
        out[tag]={'strict_common_interior_point':center,'all_support_margins':margins,'T_crossings':crossings,
                  'all_face_view_normals_nonzero':True,'all_projected_edges_nondegenerate':True,
                  'standard_label_counts':dict(Counter(p['domains'].values())),
                  'every_coplanar_face_component':face_components}
    p=json.loads((ROOT/'results/twisted-bars64-full-native.json').read_text())
    q=json.loads((ROOT/'results/hc-drawings26-27.json').read_text())['pictures'][0]
    rx,ry=map(F,q['source_transform']['right_origin']);unit=F(q['source_transform']['right_unit'])
    copies=[]
    for old,new in zip(range(47,54),(3089,3091,3093,3095,3097,3099,3101)):
        normalized=[((F(x)-rx)/unit,(F(y)-ry)/unit) for x,y in q['source_path_canonical_vertices'][str(old)]]
        target=[(F(x)-94,2*F(y)) for x,y in p['source_paths'][str(new)]]
        assert normalized==target
        rotated=[(108-F(x),16-F(y)) for x,y in p['source_paths'][str(new)]]
        left=[tuple(map(F,x)) for x in p['source_paths'][str(new+1)]]
        assert rotated==left
        copies.append({'original26_path':old,'64_right_path':new,'64_left_path':new+1})
    out['two_exact_copies_of_right26']={'canonical_map_to26':'(x,y)->(x-94,2y)','half_turn':'(x,y)->(108-x,16-y)','all_seven_paths':copies}
    (ROOT/'results/twisted-bars64-small-certificates.json').write_text(json.dumps(out,indent=2,default=encode)+'\n')
    print(json.dumps({'pictures':2,'T_gaps':'all exactly2','copied_paths':len(copies),'geometry_rerun':False}))


if __name__=='__main__':main()
