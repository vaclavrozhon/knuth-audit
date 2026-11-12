"""Decode thick center-path strokes and piece outlines, preserving crossings."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
import math, xml.etree.ElementTree as ET
import paths151 as h
from extract_chain150 import paths, points

def strokes(path):
    result=[]
    for e in ET.parse(path).getroot().find('page'):
        if e.tag!='stroke_path':continue
        color=tuple(map(float,e.get('color','').split()))
        if color not in [(0.,0.,0.),(0.,0.,0.,1.)]:continue
        a,b,c,d,*_=map(float,e.get('transform').split())
        width=float(e.get('linewidth'))*math.sqrt(abs(a*d-b*c))
        if width<.5:continue
        start=last=None;control=[]
        for q in e:
            ps=points(e,q)
            if q.tag=='moveto':
                assert start is None,'Expected one open subpath per thick stroke'
                start=last=ps[0];control+=ps
            elif ps:last=ps[-1];control+=ps
            elif q.tag=='closepath':raise AssertionError('Unexpected closed thick stroke')
        assert start and last
        result.append(dict(start=start,end=last,control=control,width=width))
    return result

def piece(rect,curves):
    x0,x1,y0,y1=rect;unit=min(x1-x0,y1-y0);vertical=y1-y0>x1-x0
    assert abs(max(x1-x0,y1-y0)/unit-2)<.001
    ports=[(2-y,x) for x,y in h.PORTS] if vertical else h.PORTS
    actual=[(x0+x*unit/2,y0+y*unit/2) for x,y in ports]
    pairs=[];selected=[]
    for i,c in enumerate(curves):
        ps=c['control'];tol=.005
        if not all(x0-tol<=x<=x1+tol and y0-tol<=y<=y1+tol for x,y in ps):continue
        ids=[]
        for p in [c['start'],c['end']]:
            ds=[math.dist(p,q) for q in actual];j=min(range(6),key=ds.__getitem__)
            assert ds[j]<.005,(rect,p,ds)
            ids.append(j)
        assert ids[0]!=ids[1]
        pairs.append(tuple(sorted(ids)));selected.append(i)
    p=tuple(sorted(pairs));assert len(set(h.mask(p)))==2*len(p),(rect,p)
    return dict(bounds=rect,unit=unit,vertical=vertical,ports=actual,pattern=p,canonical=h.canonical(p),stroke_indices=selected)

def region(path,x0,y0,w,height,unit,expected):
    rects,_=paths(path);curves=strokes(path)
    rs=[r for r in rects if x0-.01<=r[0]<r[1]<=x0+w*unit+.01 and y0-.01<=r[2]<r[3]<=y0+height*unit+.01]
    assert len(rs)==expected,(path,len(rs),expected)
    decoded=[piece(r,curves) for r in rs];used=set();edges=[];models=[];stroke_ids=[]
    for p in decoded:
        x1,x2,y1,y2=p['bounds'];v=[(x1-x0)/unit,(x2-x0)/unit,(y1-y0)/unit,(y2-y0)/unit]
        assert max(abs(x-round(x)) for x in v)<.002
        a,b,c,d=map(round,v);cells={(x,y) for x in range(a,b) for y in range(c,d)}
        assert len(cells)==2 and not used&cells;used|=cells
        pts=[(round((x-x0)*2/unit),round((y-y0)*2/unit)) for x,y in p['ports']]
        for u,v in p['pattern']:edges.append((pts[u],pts[v]))
        models.append(dict(bounds=(a,b,c,d),pattern=p['pattern'],canonical=p['canonical'],ports=pts))
        stroke_ids+=p['stroke_indices']
    assert len(stroke_ids)==len(set(stroke_ids))
    assert used=={(x,y) for x in range(w) for y in range(height)}
    # A crossing is NOT a junction: each stroke connects only its two ends.
    graph=defaultdict(list)
    for a,b in edges:graph[a].append(b);graph[b].append(a)
    assert all(len(v)==2 for v in graph.values())
    assert all(0<x<2*w and 0<y<2*height for x,y in graph)
    unseen=set(graph);components=[]
    while unseen:
        todo=[unseen.pop()];size=0
        while todo:
            p=todo.pop();size+=1
            for q in graph[p]:
                if q in unseen:unseen.remove(q);todo.append(q)
        components.append(size)
    expected_types=set().union(*(h.catalogue(k)[1] for k in ([1,2] if expected==36 else range(4))))
    counts=Counter(p['canonical'] for p in decoded)
    assert set(counts)==expected_types and set(counts.values())=={1}
    assert len(components)==1
    return dict(pieces=models,horizontal=sum(not p['vertical'] for p in decoded),vertical=sum(p['vertical'] for p in decoded),
        all_types_once=True,single_loop=True,subpaths=len(edges),loop_components=components,board=(w,height),
        checked_subpaths=len(stroke_ids),edges=edges)

def extras(path,y0,y1):
    rs,_=paths(path);cs=strokes(path);rs=sorted(r for r in rs if y0<r[2]<r[3]<y1)
    assert len(rs)==12
    ps=[piece(r,cs)['canonical'] for r in rs]
    assert len(set(ps))==12 and set(ps)==h.catalogue(0)[1]|h.catalogue(3)[1]
    return ps

def main():
    configs=[('original-question','results/bricks147/original-163.xml',326.74,427.276,9,8,86/9,36),
        ('draft-question','results/bricks147/draft-85.xml',348.82,535.935,9,8,86/9,36),
        ('original-a','results/chain150/original-479.xml',61.18,470.071,9,8,86/9,36),
        ('draft-a','results/chain150/draft-169.xml',83.26,578.776,9,8,86/9,36),
        ('original-b','results/chain150/original-479.xml',165.88,470.07,9,8,86/9,36),
        ('draft-b','results/chain150/draft-169.xml',188.02,578.776,9,8,86/9,36),
        ('original-152','results/chain150/original-479.xml',270.64,470.048,12,8,114.7/12,48),
        ('draft-152','results/chain150/draft-169.xml',292.66,578.753,12,8,114.7/12,48)]
    figures={};traces={}
    for name,filename,*args in configs:
        print('Checking',name,flush=True);p=h.ROOT/filename;traces[filename]=h.sha(p)
        figures[name]=region(p,*args)
    for n in ['question','a','b','152']:
        assert figures['original-'+n]==figures['draft-'+n],n
    assert [figures['original-'+n]['horizontal'] for n in ['question','a','b']]==[2,18,32]
    ex1=extras(h.ROOT/'results/bricks147/original-163.xml',560,592)
    ex2=extras(h.ROOT/'results/bricks147/draft-85.xml',670,701)
    assert ex1==ex2
    h.save(h.OUT/'figures-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=h.sha(__file__),
        catalogue_sha256=h.sha(h.__file__),path_parser_sha256=h.sha(h.ROOT/'extract_chain150.py'),trace_sha256=traces,
        figures=figures,all_original_draft_equal=True,twelve_extra_types=ex1,
        note='Center-path endpoints read directly from thick black vector strokes. Crossing interiors are not graph junctions.'))
    print('PASS151/152:all inventories and single loops, H counts2/18/32; twelve extras; original and draft agree.')

if __name__=='__main__':main()
