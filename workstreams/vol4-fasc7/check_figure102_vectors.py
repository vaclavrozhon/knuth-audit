#!/usr/bin/env python3
"""Finite extraction of the original PDF's straight polygon boundaries."""
from collections import Counter,defaultdict
from fractions import Fraction as F
from pathlib import Path
import json, re, xml.etree.ElementTree as E
from check_polyhedra_fixed import ROOT, source, encode

def solve(a,b):
    a=[list(row)+[v] for row,v in zip(a,b)];n=len(a)
    for k in range(n):
        r=next(r for r in range(k,n) if a[r][k]);a[k],a[r]=a[r],a[k]
        t=a[k][k];a[k]=[x/t for x in a[k]]
        for r in range(n):
            if r!=k:
                t=a[r][k];a[r]=[x-t*y for x,y in zip(a[r],a[k])]
    return [row[-1] for row in a]

def read():
    root=E.parse(ROOT/'sources/file-025.svg').getroot();groups=defaultdict(list)
    by_path={}
    for i,p in enumerate(root.findall('.//{http://www.w3.org/2000/svg}path')):
        if p.get('stroke')!='rgb(0%, 0%, 0%)':continue
        t=list(map(F,re.findall(r'[-+]?(?:\d*\.\d+|\d+)',p.get('transform',''))))
        if len(t)!=6:continue
        a,b,c,d,e,f=t; assert (a,b,c,d)==(1,0,0,-1)
        assert not re.search('[CQASTHV]',p.get('d',''))
        pts=[(F(x)+e,-F(y)+f) for x,y in re.findall(r'[ML] ([-\d.]+) ([-\d.]+)',p.get('d',''))]
        if not pts or max(y for x,y in pts)>160:continue
        assert p.get('d').count('Z')==1 and pts[0]==pts[-1]
        pts=pts[:-1];cx=sum(x for x,y in pts)/len(pts)
        group='a' if cx<240 else 'b' if cx<300 else 'c' if cx<370 else 'd'
        groups[group].append((i,pts));by_path[i]=pts
    result={}
    for group,polys in groups.items():
        vertices=[];boundaries=[];max_displacement2=F(0)
        for path,poly in polys:
            cycle=[]
            for p in poly:
                near=[i for i,v in enumerate(vertices) if sum((x-y)**2 for x,y in zip(p,v))<F(1,10000)]
                assert len(near)<=1
                if near:
                    i=near[0];max_displacement2=max(max_displacement2,sum((x-y)**2 for x,y in zip(p,vertices[i])))
                else:i=len(vertices);vertices.append(p)
                cycle.append(i)
            assert len(cycle)==len(set(cycle))
            boundaries.append({'source_path':path,'cycle':cycle})
        ec=Counter(tuple(sorted((a,b))) for q in boundaries for a,b in zip(q['cycle'],q['cycle'][1:]+q['cycle'][:1]))
        assert all(c==2 for c in ec.values())
        assert set(Counter(v for edge in ec for v in edge).values())=={3}
        separation2=min(sum((x-y)**2 for x,y in zip(a,b)) for i,a in enumerate(vertices) for b in vertices[i+1:])
        assert separation2>100*max_displacement2
        result[group]={'vertices':vertices,'edges':sorted(ec),'boundaries':boundaries,
                       'counts':{'vertices':len(vertices),'edges':len(ec),'boundary_polygons':len(boundaries)},
                       'maximum_endpoint_merge_squared_distance':max_displacement2,
                       'minimum_distinct_vertex_squared_separation':separation2}
    # Explicit reference correspondences identify the depicted objects. These
    # affine fits identify rounded drawing vertices; they do not assert exact
    # orthogonality of a reconstructed camera or exact equality of renderings.
    for group,name,den,refs in [
        ('a','Sphinx',100000,[(0,18,0),(1,18,1),(16,18,3),(4,22,0)]),
        ('c','Clasp',22,[(0,63,0),(1,63,1),(2,63,2),(3,64,1)])]:
        data,vs,error=source(name,den)
        mat=[list(vs[i])+[F(1)] for i,_,_ in refs]
        rows=[solve(mat,[by_path[path][j][k] for _,path,j in refs]) for k in range(2)]
        mapping=[];residuals=[];points=result[group]['vertices']
        for v in vs:
            predicted=[sum(x*y for x,y in zip(row,(*v,F(1)))) for row in rows]
            distances=[sum((x-y)**2 for x,y in zip(predicted,p)) for p in points]
            j=min(range(len(points)),key=distances.__getitem__)
            mapping.append(j);residuals.append(distances[j])
        original_edges={tuple(sorted(e)) for e in result[group]['edges']}
        differing=[i for i,d in enumerate(residuals) if d>=F(1,100)]
        if name=='Sphinx':
            assert differing==[47,51,62,66]
            known={i:mapping[i] for i in range(len(vs)) if i not in differing}
            for i in differing:
                neighbors=[b if a==i else a for a,b in data['edge'] if i in (a,b)]
                candidates=[j for j in range(len(points)) if j not in known.values() and all(
                    tuple(sorted((j,known[n]))) in original_edges for n in neighbors if n in known)]
                assert len(candidates)==1
                known[i]=candidates[0]
            mapping=[known[i] for i in range(len(vs))]
        else: assert not differing
        assert len(set(mapping))==len(vs)
        assert {tuple(sorted((mapping[a],mapping[b]))) for a,b in data['edge']}==original_edges
        inv={j:i for i,j in enumerate(mapping)}
        result[group].update({'primary_model':name,'source_to_drawing_vertex':mapping,
                             'affine_identification_rows':rows,'maximum_identification_residual_squared':max(residuals),
                             'public_model_coordinates_differ_from_drawing_at_vertices':differing,
                             'boundary_cycles_in_primary_vertex_numbers':[[inv[j] for j in q['cycle']] for q in result[group]['boundaries']]})
    return result

if __name__=='__main__':
    result=read()
    (ROOT/'results/figure102-vectors.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=encode)+'\n')
    print(json.dumps({k:v['counts'] for k,v in result.items()}))
