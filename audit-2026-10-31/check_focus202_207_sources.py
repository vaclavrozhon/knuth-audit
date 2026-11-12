"""Decode printed trees and check two tiny exact-cover inputs and one-step scores."""
from collections import defaultdict,Counter
from datetime import datetime,timezone
from fractions import Fraction
from pathlib import Path
import json,math,re,time,xml.etree.ElementTree as ET
from extract_chain150 import points
from extract_jigsaw import transform
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/focus202_207'


def tree(path,bounds,labels=False):
    root=ET.parse(path);nodes=[];squares=[];lines=[]
    x0,x1,y0,y1=bounds
    inside=lambda x,y:x0<x<x1 and y0<y<y1
    for t in root.getroot().find('page'):
        if t.tag not in ['fill_path','stroke_path']:continue
        ps=[p for q in t for p in points(t,q)]
        if not ps:continue
        a,b=min(x for x,y in ps),max(x for x,y in ps)
        c,d=min(y for x,y in ps),max(y for x,y in ps)
        cx,cy=(a+b)/2,(c+d)/2
        if t.tag=='fill_path' and set(t.get('color','').split())=={'0'} and inside(cx,cy):
            if 2.8<b-a<3.1 and 2.8<d-c<3.1 and any(q.tag=='curveto' for q in t):
                nodes.append(dict(center=[cx,cy],solved=False))
            elif 3.3<b-a<3.6 and 3.3<d-c<3.6 and not any(q.tag=='curveto' for q in t):squares.append((cx,cy))
        if t.tag=='stroke_path':
            prev=None
            for q in t:
                psq=points(t,q)
                if q.tag=='moveto':prev=psq[0]
                elif q.tag=='lineto':
                    if inside(*prev) and inside(*psq[0]):lines.append((prev,psq[0]))
                    prev=psq[0]
    assert nodes,path
    for p in squares:
        near=[i for i,q in enumerate(nodes) if math.dist(p,q['center'])<.02]
        assert len(near)==1;(nodes[near[0]])['solved']=True
    edges=[]
    for a,b in lines:
        dx,dy=b[0]-a[0],b[1]-a[1];norm=dx*dx+dy*dy
        if not norm:continue
        on=[]
        for i,q in enumerate(nodes):
            x,y=q['center'];z=((x-a[0])*dx+(y-a[1])*dy)/norm
            if -.002<z<1.002 and abs((x-a[0])*dy-(y-a[1])*dx)/norm**.5<.025:on.append((z,i))
        on.sort()
        if len(on)>=2 and abs(on[0][0])<.002 and abs(on[-1][0]-1)<.002:
            # The source sometimes draws two collinear tree edges as one line.
            for (_,i),(_,j) in zip(on,on[1:]):
                pair=sorted([i,j],key=lambda k:nodes[k]['center'][1]);assert pair not in edges;edges.append(pair)
    assert len(edges)==len(nodes)-1,(path,bounds,len(nodes),len(edges))
    children=defaultdict(list)
    for i,j in edges:children[i].append(j)
    roots=set(range(len(nodes)))-{j for i,j in edges};assert len(roots)==1
    rt=roots.pop();assert rt==min(range(len(nodes)),key=lambda i:nodes[i]['center'][1])
    for i in range(len(nodes)):
        children[i].sort(key=lambda j:nodes[j]['center'][0]);nodes[i]['children']=children[i]
        assert not nodes[i]['solved'] or not children[i]
    label_glyphs=0
    if labels:
        glyph_rows=defaultdict(list)
        for t in root.iter('fill_text'):
            for span in t:
                for g in span:
                    x,y=transform(t,float(g.get('x')),float(g.get('y')));c=g.get('unicode','')
                    if inside(x,y) and c in 'abcdefghiABCDEFG':glyph_rows[round(y,2)].append((x,c));label_glyphs+=1
        grouped=defaultdict(list)
        levels=sorted({round(q['center'][1],2) for q in nodes})
        for y,gs in glyph_rows.items():
            lev=min(levels,key=lambda v:abs(v-y));assert abs(lev-y)<5
            groups=[];prev=-1e9
            for x,c in sorted(gs):
                if x-prev>8:groups.append([x,c])
                else:groups[-1][1]+=c
                prev=x
            grouped[lev]+=groups
        for lev in levels:
            ns=sorted([i for i,q in enumerate(nodes) if round(q['center'][1],2)==lev],key=lambda i:nodes[i]['center'][0])
            gs=sorted(grouped[lev]);assert len(ns)==len(gs),(path,lev,ns,gs)
            for i,(x,label) in zip(ns,gs):nodes[i]['label']=label
    def shape(i):return nodes[i]['solved'],tuple(shape(j) for j in children[i])
    seen=[]
    def walk(i):
        seen.append(i)
        for j in children[i]:walk(j)
    walk(rt);assert len(seen)==len(set(seen))==len(nodes)
    return dict(nodes=nodes,edges=edges,root=rt,shape=shape(rt),label_glyphs=label_glyphs)


def immutable(items,options):
    if not items:return True,()
    c=min(items,key=lambda i:sum(i in row for row in options))
    children=[]
    for row in options:
        if c in row:
            children.append(immutable([i for i in items if i not in row],[r for r in options if set(r).isdisjoint(row)]))
    return False,tuple(children)


def named_sum(left,right):
    result={}
    def rec(a,b):
        la,rb=left['nodes'][a],right['nodes'][b];label=la['label']+rb['label']
        da=math.inf if la['solved'] else len(la['children'])
        db=math.inf if rb['solved'] else len(rb['children'])
        kids=[]
        if da!=math.inf or db!=math.inf:
            kids=[rec(c,b) for c in la['children']] if da<=db else [rec(a,c) for c in rb['children']]
        assert label not in result;result[label]=dict(solved=la['solved'] and rb['solved'],children=kids)
        return label
    root=rec(left['root'],right['root']);assert root=='aA'
    return result


def nodes_by_label(t):
    return {q['label']:dict(solved=q['solved'],children=[t['nodes'][i]['label'] for i in q['children']]) for q in t['nodes']}


def plus(a,b):
    if a[0]:return b
    if b[0]:return a
    if len(a[1])<=len(b[1]):return False,tuple(plus(c,b) for c in a[1])
    return False,tuple(plus(a,c) for c in b[1])


def options_from_text(path,equation):
    text=path.read_text().translate({0xf730+i:str(i) for i in range(10)})
    line=next(l for l in text.splitlines() if l.rstrip().endswith('('+str(equation)+')'))
    return [tuple(map(int,s.split())) for s in re.findall('‘([0-6 ]+)’',line)]


def main():
    assert not (OUT/'source-checked.json').exists();start=time.monotonic()
    data={};traces=[];texts=[]
    for version,mainpage,qpath,apath,dx,dy in [
        ('book','original-124','results/matching193_198/original-169.xml','results/matching199_201/original-491.xml',0,0),
        ('draft','draft-46','results/matching193_198/draft-91.xml','results/matching199_201/draft-181.xml',22.1,108.64)]:
        main=OUT/(mainpage+'.xml');traces += [str(main.relative_to(ROOT)),qpath,apath]
        mp=ROOT/'sources/focus202_207'/(mainpage+'.txt');texts.append(str(mp.relative_to(ROOT)))
        off=0 if version=='book' else 108.64
        t91=tree(main,(150,325,170+off,211+off))
        t93=tree(main,(180,290,380+off,412+off))
        left=tree(ROOT/qpath,(125+dx,225+dx,535+dy,585+dy),True)
        right=tree(ROOT/qpath,(260+dx,325+dx,535+dy,585+dy),True)
        answer=tree(ROOT/apath,(70+dx,255+dx,294+dy,365+dy),True)
        assert nodes_by_label(answer)==named_sum(left,right)
        assert len(answer['nodes'])==21 and sum(q['solved'] for q in answer['nodes'])==2
        assert set(nodes_by_label(left))==set('abcdefghi') and set(nodes_by_label(right))==set('ABCDEFG')
        tiny203=[tree(ROOT/apath,(x+dx-2,x+dx+2,377+dy,395+dy)) for x in [108.62,127.46,145.28,164.12,182,200.84]]
        sh=[t['shape'] for t in tiny203]
        assert sh[0]==plus(sh[1],sh[2]) and sh[5]==plus(sh[3],sh[4]) and sh[0]!=sh[5]
        tiny204=[tree(ROOT/apath,(lo+dx,hi+dx,450+dy,468+dy)) for lo,hi in [(310,325),(334,341),(353,360)]]
        assert plus(tiny204[0]['shape'],tiny204[1]['shape'])==tiny204[2]['shape']
        opts={eq:options_from_text(mp,eq) for eq in [90,92]}
        assert len(opts[90])==13 and len(opts[92])==11
        assert t91['shape']==immutable(list(range(7)),opts[90])
        assert t93['shape']==immutable(list(range(6)),opts[92])
        assert {(1,4),(1,5),(4,5)}<=set(opts[90]) # odd cycle refutes bipartiteness
        remaining=[r for r in opts[92] if set(r).isdisjoint([0,1])]
        degree={i:sum(i in r for r in remaining) for i in [2,3,4,5]}
        assert degree=={2:3,3:4,4:5,5:4}
        trees=[t91,t93,left,right,answer]+tiny203+tiny204
        assert len(trees)==14 and sum(len(t['nodes']) for t in trees)==89
        assert sum(len(t['edges']) for t in trees)==75 and sum(t['label_glyphs'] for t in trees)==58
        data[version]=dict(tree91=t91,tree93=t93,question202=[left,right],answer202=answer,
            answer203=tiny203,answer204=tiny204,options=opts,remaining_after01=remaining,degrees_after01=degree)
    assert data['book']['options']==data['draft']['options']
    mu=Fraction(5,4)
    priorities={i:Fraction(1)+Fraction(d)/(1+mu) for i,d in data['book']['degrees_after01'].items() if i!=2}
    assert priorities=={3:Fraction(25,9),4:Fraction(29,9),5:Fraction(25,9)}
    assert priorities[4]>3 and priorities[3]<3
    part_a=[]
    for d in range(5):
        i=Fraction(d+1) if d+1<=1 else Fraction(1)+Fraction(d+1,2)
        j=Fraction(d) if d<=1 else Fraction(1)+Fraction(2*d,3)
        part_a.append(dict(len_j=d,score_i=str(i),score_j=str(j),preferred='i' if i<j else 'j' if j<i else 'tie'))
    assert [q['preferred'] for q in part_a]==['j','j','j','tie','i']
    deps=['extract_chain150.py','extract_jigsaw.py','puzzle_xcc.py','results/focus_theory/verified.json']
    save(OUT/'source-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
        dependencies={p:sha(ROOT/p) for p in deps},source_hashes={p:sha(ROOT/p) for p in traces+texts},
        data=data,trees_per_version=14,nodes_per_version=89,edges_per_version=75,label_glyphs_per_version=58,
        part_a=part_a,item04_counterexample=dict(rho='1/2',mu='5/4',priority04='29/9',priority03='25/9',fresh_priority='3'),
        small_source_searches=4,distinct_toy_inputs=2,old_tree_censuses_rerun=0,new_long_searches=0,
        wall_seconds=time.monotonic()-start))
    print('PASS: 14 source trees/89 nodes/75 edges/58 label glyphs per version; 04 has five options, and (90) contains a triangle.')


if __name__=='__main__':main()
