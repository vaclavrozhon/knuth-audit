#!/usr/bin/env python3
"""Exact native networks28–29 and two explicit spatial witnesses for29."""
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import combinations
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT,sub,dot,geometric_visibility
from check_cubie_junctions import path_points
from check_hc_drawings26_27 import network
from check_polyhedra_fixed import encode,triangulate,convex,check_intersections,normal
from check_line_csp22 import TABLE,global_symbol,propagate,ORDER

def point(x,y):return(F(x),F(y))

def fit(pairs):
    n=len(pairs);sx=sum(x for x,y in pairs);sy=sum(y for x,y in pairs)
    u=(n*sum(x*y for x,y in pairs)-sx*sy)/(n*sum(x*x for x,y in pairs)-sx*sx)
    v=(sy-u*sx)/n
    assert u>0
    return u,v

def native(paths,tag,start,points,words):
    pairs=[[],[]];raw={}
    for i,word in enumerate(words,start):
        ps=path_points(paths[i]);assert len(ps)==len(word)
        raw[i]=ps
        for p,j in zip(ps,word):
            for k in (0,1):pairs[k].append((points[j][k],p[k]))
    transforms=[fit(p) for p in pairs]
    errors=[]
    for i,word in enumerate(words,start):
        for p,j in zip(raw[i],word):errors.append(sum((p[k]-(transforms[k][0]*points[j][k]+transforms[k][1]))**2 for k in (0,1)))
    assert max(errors)<F(1,10000),(tag,float(max(errors)))
    mapped={i:[points[j] for j in word] for i,word in enumerate(words,start)}
    p,ns,rs,lines,faces,boundary=network(mapped,paths)
    assert len(p)==len(points)
    oldnames={v:j for j,v in points.items()};names={j:oldnames[v] for j,v in p.items()}
    junctions={names[j]:{'type':x['type'],'neighbors':[names[k] for k in x['neighbors']]} for j,x in ns.items()}
    relations={}
    for j,x in junctions.items():
        vs=[''.join(sorted((j,k))) for k in x['neighbors']]
        ts=[''.join(global_symbol(s,j,k) for s,k in zip(row,x['neighbors'])) for row in TABLE[x['type']]]
        relations[j]=(vs,ts)
    b=[names[j] for j in boundary];edges=sorted({v for vs,ts in relations.values() for v in vs})
    ds={e:set(ORDER) for e in edges}
    for u,v in zip(b,b[1:]+b[:1]):ds[''.join(sorted((u,v)))]={'>' if u<v else '<'}
    fixed,proof=propagate(relations,ds);assert fixed is not None
    return dict(name=tag,source_path_range=[start,start+len(words)],source_coordinate_affine=transforms,
                source_maximum_residual_squared=max(errors),points=points,junctions=junctions,
                relations=relations,edges=edges,faces=[{'walk':[names[j] for j in f['walk']],'area_twice':f['area_twice']} for f in faces],
                boundary=b,standard_domains={e:''.join(s for s in ORDER if s in v) for e,v in fixed.items()},
                standard_propagation=proof)

def canonical_junction(r):
    ns=r['neighbors']
    return(r['type'],min(tuple(ns[k:]+ns[:k]) for k in range(3)) if r['type']=='Y' else tuple(ns))

def spatial(pic,raw,face_words,project,q,expected_counts=(12,18,8)):
    names=sorted(raw);index={j:i for i,j in enumerate(names)}
    vertices=[tuple(map(F,raw[j])) for j in names]
    faces=[[index[j] for j in word] for word in face_words]
    occurrences=defaultdict(list)
    for fi,f in enumerate(faces):
        for a,b in zip(f,f[1:]+f[:1]):occurrences[tuple(sorted((a,b)))].append((fi,a,b))
    assert all(len(r)==2 and r[0][1:]==r[1][1:][::-1] for r in occurrences.values())
    degrees=Counter(v for e in occurrences for v in e);assert set(degrees.values())=={3}
    assert (len(vertices),len(occurrences),len(faces))==expected_counts
    tiles=[]
    for f in faces:tiles.extend(triangulate(f,vertices))
    polygons=[[vertices[k] for k in t] for t in tiles];normals=[convex(poly) for poly in polygons]
    checks=check_intersections(polygons,tiles,normals)
    projected=[project(v) for v in vertices]
    assert all(projected[index[j]]==p for j,p in pic['points'].items())
    q=tuple(map(F,q));assert all(dot(normal([vertices[k] for k in f]),q)!=0 for f in faces)
    model={'vertices':vertices,'edges':sorted(occurrences),'faces':faces,'convex_tiles':tiles}
    intervals,atoms=geometric_visibility(model,vertices,projected,q)
    shown={};hidden=[]
    for k,(a,b) in enumerate(model['edges']):
        key=''.join(sorted((names[a],names[b])))
        if intervals[k]:assert intervals[k]==[[0,1]],(pic['name'],key,intervals[k]);shown[key]=intervals[k]
        else:hidden.append(key)
    assert set(shown)==set(pic['edges']),(pic['name'],set(shown)^set(pic['edges']))
    return dict(vertex_order=names,vertices=vertices,faces=face_words,edges=[''.join((names[a],names[b])) for a,b in model['edges']],
                triangulated_faces=tiles,all_spatial_tile_intersections=checks,projection=projected,view_towards_camera=q,
                every_edge_visibility=shown,hidden_edges=hidden,visible_atom_count=len(atoms),
                vertex_degrees={names[v]:deg for v,deg in degrees.items()})

def main():
    paths=[p.attrib for p in ET.parse(ROOT/'sources/file-030.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    left28=dict(zip('abcdefghijk',[point(0,F(27,2)),point(29,F(27,2)),point(29,0),point(F(29,2),-F(87,14)),point(0,0),point(4,F(9,2)),point(4,9),point(25,9),point(25,F(9,2)),point(F(29,2),0),point(F(29,2),F(9,2))]))
    left29=dict(zip('abcdefghijk',[point(0,9),point(29,9),point(29,0),point(F(29,2),-F(261,26)),point(0,0),point(8,0),point(8,F(9,2)),point(21,F(9,2)),point(21,0),point(F(29,2),-F(9,2)),point(F(29,2),0)]))
    right28=dict(zip('abcdefghijk',[point(0,F(18,5)),point(5,F(18,5)),point(7,F(9,5)),point(7,-F(9,5)),point(2,-F(9,5)),point(0,0),point(2,0),point(F(5,2),F(27,10)),point(3,F(27,20)),point(5,-F(9,10)),point(5,F(27,20))]))
    right29=dict(zip('abcdefghijk',[point(0,F(27,10)),point(5,F(27,10)),point(7,0),point(7,-F(27,10)),point(2,-F(27,10)),point(0,0),point(2,0),point(4,F(9,5)),point(3,0),point(4,-F(9,5)),point(5,0)]))
    leftwords=['abcdea','efghic','fji','jkg','kh'];rightwords=['abcdefa','ghijg','fg','ikd','bk']
    pics=[native(paths,'28-left',18,left28,leftwords),native(paths,'28-right',23,right28,rightwords),
          native(paths,'29-left',28,left29,leftwords),native(paths,'29-right',33,right29,rightwords)]
    for x,y in [(pics[0],pics[2]),(pics[1],pics[3])]:
        assert {j:canonical_junction(r) for j,r in x['junctions'].items()}=={j:canonical_junction(r) for j,r in y['junctions'].items()}
    for pic,shared in [(pics[0],['ef','ci']),(pics[1],['fg','ik'])]:
        assert all(pic['standard_domains'][e]=='+' for e in shared)
        pic['A_B_shared_forced_convex_lines']=shared
    rawleft={'a':(0,0,0),'b':(29,0,0),'c':(29,0,9),'d':(F(29,2),F(29,2),9),'e':(0,0,9),
             'f':(8,0,9),'g':(8,0,F(9,2)),'h':(21,0,F(9,2)),'i':(21,0,9),
             'j':(F(29,2),F(13,2),9),'k':(F(29,2),F(13,2),F(9,2)),'l':(F(29,2),F(29,2),0)}
    fl=['efjicd','abcihgfe','aedl','bldc','alb','fgkj','ijkh','ghk']
    pics[2]['spatial_witness']=spatial(pics[2],rawleft,fl,lambda p:(p[0],9-p[2]-F(9,13)*p[1]),(0,-1,F(9,13)))
    H=F(27,10)
    rawright={'a':(0,0,0),'b':(5,0,0),'c':(5,2,0),'d':(5,2,H),'e':(0,2,H),'f':(0,0,H),
              'g':(2,0,H),'h':(4,0,F(9,10)),'i':(3,0,H),'j':(F(8,3),F(4,3),H),'k':(5,0,H),'l':(0,2,0)}
    fr=['fgjikde','abkihgf','bcdk','ledc','afel','alcb','ghj','ijh']
    pics[3]['spatial_witness']=spatial(pics[3],rawright,fr,lambda p:(p[0]+p[1],H-p[2]-F(27,20)*p[1]),(1,-1,F(27,20)))
    (ROOT/'results/hc-realizability28-29.json').write_text(json.dumps({'pictures':pics},indent=2,default=encode)+'\n')
    print(json.dumps([{'name':p['name'],'vertices':len(p['points']),'lines':len(p['edges']),
                       'native_residual_squared':str(p['source_maximum_residual_squared']),
                       'hidden_spatial_edges':p.get('spatial_witness',{}).get('hidden_edges'),
                       'forced_common_edges':p.get('A_B_shared_forced_convex_lines')} for p in pics],indent=2))

if __name__=='__main__':main()
