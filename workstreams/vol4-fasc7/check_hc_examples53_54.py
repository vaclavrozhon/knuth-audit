#!/usr/bin/env python3
"""All native geometry53–54; five boundary states and every painted mark54."""
from fractions import Fraction as F
from collections import Counter
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT, sub, dot
from check_cubie_junctions import path_points
from check_hc_drawings26_27 import network
from check_boundary_matrices50 import CASE, STATES, PRINTED, word_product, matrices, trace
from check_line_csp22 import ORDER, propagate
from check_polyhedra_fixed import encode


def reverse(s):
    return {'>': '<', '<': '>', '+': '+', '-': '-'}[s]


def source(paths, indexes, width, height, names):
    raw = {i: path_points(paths[i]) for i in indexes}
    allpoints = [p for qs in raw.values() for p in qs]
    origin = tuple(min(p[k] for p in allpoints) for k in (0, 1))
    units = tuple((max(p[k] for p in allpoints)-origin[k])/n for k,n in enumerate((width,height)))
    mapped, errors = {}, []
    for i, qs in raw.items():
        mapped[i] = []
        for p in qs:
            q = tuple(F(round((p[k]-origin[k])/units[k])) for k in (0,1))
            errors.append(sum((p[k]-origin[k]-q[k]*units[k])**2 for k in (0,1)))
            mapped[i].append(q)
    assert max(errors) < F(1,10000)
    pts,ns,rs,lines,faces,boundary = network(mapped,paths)
    translate={j:names[p] for j,p in pts.items()}
    points={translate[j]:p for j,p in pts.items()}
    junctions={translate[j]:{'type':r['type'],'neighbors':[translate[k] for k in r['neighbors']]} for j,r in ns.items()}
    relations={}
    for j,r in junctions.items():
        # Recompute named orientation, not the vNN orientation used above.
        from check_line_csp22 import TABLE, global_symbol
        vs=[''.join(sorted((j,k))) for k in r['neighbors']]
        rows=[''.join(global_symbol(s,j,k) for s,k in zip(t,r['neighbors'])) for t in TABLE[r['type']]]
        relations[j]=(vs,rows)
    return {'source_indexes':indexes,'source_origin':origin,'source_units':units,
            'maximum_source_residual_squared':max(errors),'points':points,'junctions':junctions,
            'relations':relations,'lines':sorted({v for vs,ts in relations.values() for v in vs}),
            'faces':[dict(walk=[translate[j] for j in f['walk']],area_twice=f['area_twice']) for f in faces],
            'boundary':[translate[j] for j in boundary]}


def normalized_junction(r):
    ns=r['neighbors']
    return (r['type'],min(tuple(ns[k:]+ns[:k]) for k in range(3)) if r['type']=='Y' else tuple(ns))


def main():
    paths=[p.attrib for p in ET.parse(ROOT/'sources/file-185.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    a=source(paths,[18,19],16,12,dict(zip([(16,0),(13,3),(12,6),(13,9),(16,12),(8,8),(0,6),(8,4),(10,6)],'abcdefghi')))
    b=source(paths,[38,39],8,6,dict(zip([(7,1),(8,0),(0,3),(8,6),(7,5),(7,4),(6,3),(7,2),(8,3)],'abcdefghi')))
    assert a['lines']==b['lines']==['ab','ah','bc','cd','de','ef','fg','fi','gh','hi']
    assert {j:normalized_junction(r) for j,r in a['junctions'].items()}=={j:normalized_junction(r) for j,r in b['junctions'].items()}
    assert set(a['boundary'])==set('abcdefgh') and set(b['boundary'])==set('bcd efih a'.replace(' ',''))
    assert len(a['points'])==len(b['points'])==9
    assert Counter(r['type'] for r in a['junctions'].values())=={'V':7,'Y':2}
    # Explicit check of connectivity after each vertex deletion; the proof
    # in the note identifies the three internally disjoint f–h paths.
    connectivity={}
    for deleted in a['points']:
        remaining=set(a['points'])-{deleted}; seen={min(remaining)}
        while True:
            extended=seen|{k for j in seen for k in a['junctions'][j]['neighbors'] if k!=deleted}
            if extended==seen: break
            seen=extended
        assert seen==remaining
        connectivity[deleted]=sorted(seen)
    c=source(paths,[58,59,60],6,5,dict(zip([(0,0),(2,1),(4,1),(6,0),(6,4),(3,5),(0,4),(3,2),(2,3),(4,3)],'abcdefghij')))
    assert len(c['points'])==10 and len(c['lines'])==12
    assert Counter(r['type'] for r in c['junctions'].values())=={'V':6,'W':2,'Y':2}
    boundary=c['boundary']; k=boundary.index('a');boundary=boundary[k:]+boundary[:k]
    assert boundary==list('abcdefg')
    cases=[];ports=[]
    for k,j in enumerate(boundary):
        previous,following=boundary[k-1],boundary[(k+1)%len(boundary)]
        inner=[n for n in c['junctions'][j]['neighbors'] if n not in (previous,following)]
        which={'prev':previous,'next':following}
        if inner: which['inner']=inner[0]
        hits=[]
        for case,(kind,order) in CASE.items():
            if kind!=c['junctions'][j]['type'] or set(order)!=set(which):continue
            want=[which[t] for t in order];actual=c['junctions'][j]['neighbors']
            if actual==want or (kind=='Y' and any(actual==want[k:]+want[:k] for k in range(3))):hits.append(case)
        assert len(hits)==1
        cases.append(hits[0])
        if inner:ports.append((j,inner[0]))
    assert ''.join(cases)=='VYYVWVW' and ports==[('b','h'),('c','h'),('e','j'),('g','i')]
    p=word_product(cases,matrices());assert trace(p)=={'mmpp':4,'glpp':1}
    paths_by_start=[]
    for initial in range(4):
        frontier=[(initial,[],[])]
        for case in cases:
            next_frontier=[]
            for state,values,letters in frontier:
                for to,symbol in enumerate(PRINTED[case][state]):
                    if symbol!='0':next_frontier.append((to,values+[STATES[to]],letters+([] if symbol=='1' else [symbol])))
            frontier=next_frontier
        for final,values,letters in frontier:
            if final==initial:paths_by_start.append({'boundary_labels':''.join(values),'inner_word':''.join(letters)})
    assert Counter(x['inner_word'] for x in paths_by_start)=={'mmpp':4,'glpp':1}
    complete=[]
    for row in paths_by_start:
        ds={e:set(ORDER) for e in c['lines']}
        for u,v,s in zip(boundary,boundary[1:]+boundary[:1],row['boundary_labels']):
            ds[''.join(sorted((u,v)))]={s if u<v else reverse(s)}
        fixed,proof=propagate(c['relations'],ds)
        row['propagation']=proof
        row['extends']=fixed is not None
        if fixed is not None:
            assert all(len(t)==1 for t in fixed.values())
            values={e:next(iter(t)) for e,t in fixed.items()}
            assert all(''.join(values[e] for e in vs) in rows for vs,rows in c['relations'].values())
            complete.append(values);row['complete_labeling']=values
    assert len(complete)==1 and next(r for r in paths_by_start if r['extends'])['inner_word']=='glpp'
    ds={e:set(ORDER) for e in c['lines']}
    for u,v in zip(boundary,boundary[1:]+boundary[:1]):ds[''.join(sorted((u,v)))]={'>' if u<v else '<'}
    std,stdproof=propagate(c['relations'],ds);assert std is None
    # Every one of20 native marks. White gaps denote minus, red ticks plus;
    # arrow tip is the middle point, and its direction is tail→tip.
    original_points={j:tuple(c['source_origin'][k]+c['source_units'][k]*p[k] for k in (0,1)) for j,p in c['points'].items()}
    marks=[]
    for i in range(61,81):
        qs=path_points(paths[i])
        if len(qs)==2:
            anchor=tuple((qs[0][k]+qs[1][k])/2 for k in (0,1))
            symbol='-' if paths[i]['stroke']=='rgb(100%, 100%, 100%)' else '+'
        else:
            assert len(qs)==3
            anchor=qs[1]
            direction=sub(qs[1],tuple((qs[0][k]+qs[2][k])/2 for k in (0,1)))
            symbol=None
        hits=[]
        for edge in c['lines']:
            u,v=edge; x,y=original_points[u],original_points[v];d=sub(y,x)
            t=dot(sub(anchor,x),d)/dot(d,d)
            residual=sub(sub(anchor,x),tuple(t*z for z in d))
            if 0<t<1 and dot(residual,residual)<F(1,10000):hits.append(edge)
        assert len(hits)==1,(i,hits)
        edge=hits[0]
        if symbol is None:symbol='>' if dot(direction,sub(original_points[edge[1]],original_points[edge[0]]))>0 else '<'
        assert complete[0][edge]==symbol,(i,edge,symbol,complete[0][edge])
        marks.append({'native_path':i,'line':edge,'label':symbol})
    c.update(boundary=boundary,boundary_case_word=''.join(cases),ports=ports,
             complete_matrix_product=p,trace=trace(p),all_five_boundary_labelings=paths_by_start,
             unique_labeling=complete[0],standard_contradiction=stdproof,all_native_marks=marks)
    out={'figure53a':a,'figure53b':b,'connectivity_after_vertex_deletion':connectivity,'figure54':c}
    (ROOT/'results/hc-examples53-54.json').write_text(json.dumps(out,indent=2,default=encode)+'\n')
    print(json.dumps({'shared_junctions':{j:normalized_junction(r) for j,r in sorted(a['junctions'].items())},
                     'boundaries':[a['boundary'],b['boundary']], 'boundary54':paths_by_start,
                     'marks54':len(marks)},indent=2))


if __name__=='__main__':main()
