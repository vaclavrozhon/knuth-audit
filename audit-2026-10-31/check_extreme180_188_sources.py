"""Printed tree and triangle details, reusing accepted mathematical results."""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from datetime import datetime, timezone
import json
import math
import xml.etree.ElementTree as ET
from extract_chain150 import points
from extract_jigsaw import transform
from puzzle_xcc import save, sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/extreme180_188'


def tree(path):
    nodes=[];blacks=[];lines=[];before=True
    for t in ET.parse(path).getroot().find('page'):
        if t.tag not in ['fill_path','stroke_path']:continue
        ps=[p for q in t for p in points(t,q)]
        if not ps:continue
        color=list(map(float,t.get('color','').split()))
        bounds=[min(x for x,y in ps),max(x for x,y in ps),min(y for x,y in ps),max(y for x,y in ps)]
        green=len(color)==3 and all(abs(a-b)<.002 for a,b in zip(color,[.8,1,.8]))
        if t.tag=='fill_path' and green:
            before=False;assert len(ps)==4
            nodes.append(dict(bounds=bounds))
        elif t.tag=='fill_path' and color==[0,0,0] and len(ps)==4:
            blacks.append(bounds)
        elif t.tag=='stroke_path' and before:
            prev=None
            for q in t:
                qq=points(t,q)
                if q.tag=='moveto':prev=qq[0]
                elif q.tag=='lineto':lines.append((prev,qq[0]));prev=qq[0]
    assert len(nodes)==16
    unit=min(q['bounds'][1]-q['bounds'][0] for q in nodes)
    for q in nodes:
        x0,x1,y0,y1=q['bounds']
        rows,cols=round((y1-y0)/unit)-1,round((x1-x0)/unit)-1
        assert rows>=0 and cols>=0
        assert abs((y1-y0)/unit-rows-1)<.002 and abs((x1-x0)/unit-cols-1)<.002
        q['shape']=[rows,cols];q['center']=[(x0+x1)/2,(y0+y1)/2]
        q['matrix']=[[int(any(a<x0+(j+1)*unit<b and c<y0+(i+1)*unit<d for a,b,c,d in blacks))
                      for j in range(cols)] for i in range(rows)]
    edges=[]
    for a,b in lines:
        pair=[]
        for p in [a,b]:
            near=[i for i,q in enumerate(nodes) if math.dist(p,q['center'])<.02]
            if len(near)!=1:break
            pair.append(near[0])
        if len(pair)==2:
            pair.sort(key=lambda i:nodes[i]['center'][1])
            assert nodes[pair[0]]['center'][1]<nodes[pair[1]]['center'][1]
            edges.append(pair)
    assert len(edges)==15 and len({b for a,b in edges})==15 and {b for a,b in edges}==set(range(1,16))
    children=defaultdict(list)
    for a,b in edges:children[a].append(b)
    depths={0:0};front=[0];leaves=0
    for i in front:
        q=nodes[i];a=q['matrix'];rr,cc=q['shape']
        kids=sorted(children[i],key=lambda j:nodes[j]['center'][0])
        if not cc:
            assert not a and not kids;leaves+=1;continue
        counts=[sum(row[j] for row in a) for j in range(cc)]
        pivot=min(range(cc),key=lambda j:counts[j])
        choices=[row for row in a if row[pivot]]
        assert len(kids)==len(choices)
        for kid,selected in zip(kids,choices):
            keep=[j for j in range(cc) if not selected[j]]
            expected=[[row[j] for j in keep] for row in a if not any(x*y for x,y in zip(row,selected))]
            assert nodes[kid]['matrix']==expected,(i,kid,expected,nodes[kid]['matrix'])
            assert nodes[kid]['shape']==[len(expected),len(keep)]
            depths[kid]=depths[i]+1;front.append(kid)
    assert len(front)==16 and leaves==7
    assert nodes[0]['matrix']==[[int(c) for c in s] for s in ['1000','0100','0010','0001','1100','0110','0011','1001']]
    assert sum(r*c for r,c in (q['shape'] for q in nodes))==69
    return dict(nodes=nodes,edges=edges,leaves=leaves,matrix_cells=69,depths=depths)


def triangle(path,bounds):
    x0,x1,y0,y1=bounds;lines=defaultdict(list)
    for t in ET.parse(path).getroot().find('page'):
        if t.tag!='fill_text':continue
        for s in t:
            for g in s:
                c=g.get('unicode','')
                if not c.isdigit():continue
                x,y=transform(t,float(g.get('x')),float(g.get('y')))
                if x0<x<x1 and y0<y<y1:lines[round(y,2)].append((x,c))
    result=[]
    for y,values in sorted(lines.items()):
        groups=[];prev=-1e9
        for x,c in sorted(values):
            if x-prev>8:groups.append(c)
            else:groups[-1]+=c
            prev=x
        result.append(list(map(int,groups)))
    assert result==[[0],[1,1],[3,2,1],[9,6,4,3],[31,22,16,12,9],[121,90,68,52,40,31]],result
    for n in range(2,6):
        assert result[n][-1]==result[n-1][0]
        for k in range(n):assert result[n][k]==result[n][k+1]+result[n-1][k]
    return result


def main():
    assert not (OUT/'source-checked.json').exists()
    trees={version:tree(OUT/(version+'-'+str(page)+'.xml')) for version,page in [('original',488),('draft',178)]}
    assert [q['matrix'] for q in trees['original']['nodes']]==[q['matrix'] for q in trees['draft']['nodes']]
    assert trees['original']['edges']==trees['draft']['edges']
    tris={version:triangle(ROOT/'results/mcc175_179'/(version+'-'+str(page)+'.xml'),bounds)
        for version,page,bounds in [('original',167,(165,290,550,609)),('draft',89,(190,310,659,718))]}
    assert tris['original']==tris['draft']
    old=json.loads((ROOT/'results/doomsday.json').read_text())
    constants=[Fraction(old['original_recurrence_first_26'][15+r]*3+1,3*64) for r in range(5)]
    assert constants==[Fraction(q,96) for q in [188,248,320,425,566]]
    ext=json.loads((ROOT/'results/extreme_cover.json').read_text())
    small=ext['measured_DLX'][:6]
    assert [q['root_updates'] for q in small]==[0,1,3,12,57,294]
    assert [q['total_updates'] for q in small]==[0,1,4,18,90,484]
    bell=[q['solutions'] for q in ext['measured_DLX']]
    printed_digits=[1,0,0,2,7,1,6,1] # coefficients B1,...,B8, exactly as printed
    assert sum(a*b for a,b in zip(printed_digits,bell[1:]))==10000
    assert all(a<=math.comb(8,j) for j,a in enumerate([0]+printed_digits))
    # Every accepted multi-copy count is only read and checked for its stated formula.
    for q in ext['cycle_lower_bound']:
        assert q['solutions']==7**q['copies'] and q['nodes']==(5*7**q['copies']-3)//2
    save(OUT/'source-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
        dependencies={p:sha(ROOT/p) for p in ['extract_chain150.py','extract_jigsaw.py','results/doomsday.json','results/extreme_cover.json']},
        trace_hashes={str(p.relative_to(ROOT)):sha(p) for p in [OUT/'original-488.xml',OUT/'draft-178.xml',
            ROOT/'results/mcc175_179/original-167.xml',ROOT/'results/mcc175_179/draft-89.xml']},
        trees=trees,triangles=tris,printed_tree_cells_per_version=69,printed_triangle_entries_per_version=21,
        original181_constants=[str(q) for q in constants],printed184_Bell_digits_B0_to_B8=[0]+printed_digits,
        accepted_old_enumerations_rerun=0,solver_calls=0,new_long_searches=0))
    print('PASS180–188:all16 tree nodes/15edges/69cells and21 triangle entries per version;old counts reused, no solver.')


if __name__=='__main__':main()
