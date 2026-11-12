#!/usr/bin/env python3
"""Certify only the sixteen specified remaining witnesses in amended answer37."""
from itertools import permutations
from pathlib import Path
import json
from check_polyhedra_fixed import ROOT,certify,encode,source,sub,cross,dot
from check_figure102_vectors import solve

SPECS=[('C4A1',4),('C4A2',4),('C4B11',10),('C4B12',6),('C4B13',16),
       ('C4B21',2),('C4B22',70),('C4B23',2),('C4B32',6),('C4B41',2),
       ('C4B42',14),('C4B51',8),('C4B52',2),('C4C1',None),('C8E',None),('C8F',None)]

def edge_set(obj):return {tuple(sorted(e)) for e in obj['edges']}
def signed(obj):
    # The stored keys are deliberately parsed as two comma-separated integers,
    # never with eval or an executable parser.
    return {tuple(int(x.strip()) for x in k.strip('()').split(',')) for k,v in obj['edge_signs'].items() if v=='concave'}
def image_edges(es,p):return {tuple(sorted((p[a],p[b]))) for a,b in es}

def one_isomorphism(a,b):
    na={v:{y if x==v else x for x,y in a if v in (x,y)} for v in range(8)}
    nb={v:{y if x==v else x for x,y in b if v in (x,y)} for v in range(8)}
    nodes=0
    def visit(mapping):
        nonlocal nodes
        nodes+=1
        if len(mapping)==8:return mapping
        x=max((v for v in range(8) if v not in mapping),key=lambda v:len(na[v]&mapping.keys()))
        for y in range(8):
            if y in mapping.values():continue
            if all((v in na[x])==(w in nb[y]) for v,w in mapping.items()):
                r=visit({**mapping,x:y})
                if r:return r
    p=visit({});assert p
    return p,nodes

def compare(result):
    canonical=edge_set(result['C4A1'])
    p=[0,2,1,4,3,5,7,6];q=[5,6,7,3,4,0,1,2]
    autos=[list(range(8)),p,q,[p[q[i]] for i in range(8)]]
    assert all(image_edges(canonical,a)==canonical for a in autos)
    classes={}
    for name,_ in SPECS:
        if not name.startswith('C4'):continue
        obj=result[name];iso,nodes=one_isomorphism(edge_set(obj),canonical)
        es=image_edges(signed(obj),iso)
        key=min(tuple(sorted(image_edges(es,a))) for a in autos)
        assert key not in classes
        classes[key]=name
        obj['canonical_graph_bijection']=iso;obj['bijection_nodes']=nodes
        obj['canonical_concave_edges_under_all_four_automorphisms']=key
    old=json.loads((ROOT/'results/polyhedra-fixed.json').read_text())
    cubes={k:v for k,v in old.items() if k.startswith('C8')}
    cubes.update({k:v for k,v in result.items() if k.startswith('C8')})
    ce={(i,j) for i in range(8) for j in range(i+1,8) if i^j in (1,2,4)}
    ca=[]
    for t in range(8):
        for perm in permutations(range(3)):
            ca.append([t^sum(((i>>k)&1)<<perm[k] for k in range(3)) for i in range(8)])
    assert len({tuple(a) for a in ca})==48 and all(image_edges(ce,a)==ce for a in ca)
    cc={}
    for name,obj in cubes.items():
        assert edge_set(obj)==ce
        key=min(tuple(sorted(image_edges(signed(obj),a))) for a in ca)
        assert key not in cc;cc[key]=name
        if name in result:result[name]['canonical_concave_edges_under_all48_automorphisms']=key
    return {'C4_nonisomorphic_witnesses':len(classes),'cube_nonisomorphic_witnesses':len(cc),
            'C4_all_automorphisms':autos,'cube_all_automorphisms':ca,
            'C4_signature_classes':[{'name':v,'canonical_concave_edges':k} for k,v in classes.items()],
            'cube_signature_classes':[{'name':v,'canonical_concave_edges':k} for k,v in cc.items()],
            'scope':'Lower bounds of14 and6 by specific verified witnesses, never completeness of all possible signatures.'}

if __name__=='__main__':
    path=ROOT/'results/known-signed-witnesses.json'
    result=json.loads(path.read_text()) if path.exists() else {}
    for name,den in SPECS:
        if name in result:continue
        override=None;repair=None
        if name=='C8E':
            data,v,_=source(name,None)
            defining=[[1,5,3],[2,3,6],[5,4,6]]
            normals=[cross(sub(v[b],v[a]),sub(v[c],v[a])) for a,b,c in defining]
            rhs=[dot(n,v[t[0]]) for n,t in zip(normals,defining)]
            override={7:solve(normals,rhs)}
            repair={'scope':'Explicit audit construction; not a claim that the downloaded coordinates are planar.',
                    'three_defining_face_triples':defining,'plane_normals':normals,'plane_rhs':rhs,
                    'unmodified_nonplanar_face_determinants':[
                        {'face':c,'scalar_triple':dot(cross(sub(v[c[1]],v[c[0]]),sub(v[c[2]],v[c[0]])),sub(v[c[3]],v[c[0]]))}
                        for c in [[1,5,7,3],[5,4,6,7]]]}
        obj=certify(name,den,triangulate_all=True,coordinate_overrides=override)
        if repair:obj['independent_repair_of_public_coordinate_discrepancy']=repair
        # These16 meshes each have a connected physical graph; global orientation
        # therefore selects the bounded side of a single connected surface.
        adj={i:set() for i in range(8)}
        for a,b in obj['edges']:adj[a].add(b);adj[b].add(a)
        seen={0};todo=[0]
        while todo:
            for w in adj[todo.pop()]:
                if w not in seen:seen.add(w);todo.append(w)
        assert len(seen)==8
        result[name]=obj
        path.write_text(json.dumps(result,ensure_ascii=False,indent=2,default=encode)+'\n')
        print(json.dumps({'name':name,'counts':obj['counts']}),flush=True)
    distinctions=compare(result)
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2,default=encode)+'\n')
    (ROOT/'results/known-signed-signatures.json').write_text(json.dumps(distinctions,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in distinctions.items() if k.endswith('witnesses')}))
