"""Read USA graph figures from both source versions, without any search."""
from pathlib import Path
from datetime import datetime, timezone
import json
import math
import os
import re
import time
import xml.etree.ElementTree as ET
from extract_jigsaw import transform, paths
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/usa239_246'
SRC = ROOT/'sources/usa239_246'


def sgb():
    text = (SRC/'contiguous-usa.gb').read_text()
    vertices = re.findall(r'^"([A-Z]{2})",(A\d+),"([^"]+)",(\d+)$', text, re.M)
    arcs = re.findall(r'^V(\d+),(A\d+|0),1$', text, re.M)
    assert len(vertices) == 49 and len(arcs) == 214
    result, used = set(), set()
    for i, (name, link, fullname, pop) in enumerate(vertices):
        while link != '0':
            j = int(link[1:]); assert j not in used
            used.add(j)
            v, link = arcs[j]
            result.add((name, vertices[int(v)][0]))
    assert len(used) == 214
    assert all((b,a) in result for a,b in result)
    edges = sorted({tuple(sorted(e)) for e in result})
    return dict(population={q[0]:int(q[3]) for q in vertices},
                fullnames={q[0]:q[2] for q in vertices}, edges=edges)


def circles(tree):
    out = []
    for e in tree.iter('fill_path'):
        if e.get('color') not in ['1 1 1', '1 .5 0']:
            continue
        points = []
        for q in e:
            for suffix in ['', '1','2','3']:
                if q.get('x'+suffix) is not None:
                    points.append(transform(e,float(q.get('x'+suffix)),float(q.get('y'+suffix))))
        x0,x1 = min(x for x,y in points),max(x for x,y in points)
        y0,y1 = min(y for x,y in points),max(y for x,y in points)
        if e.get('color') == '1 .5 0':
            assert abs(x1-x0-y1+y0) < .02
        out.append(dict(x=(x0+x1)/2, y=(y0+y1)/2, radius=(x1-x0+y1-y0)/4, color=e.get('color')))
    return out


def components(names, edges):
    unseen = set(names); result = []
    while unseen:
        q = [min(unseen)]; unseen.remove(q[0])
        for a in q:
            for x,y in edges:
                b = y if x==a else x if y==a else None
                if b in unseen:
                    unseen.remove(b); q.append(b)
        result.append(sorted(q))
    return sorted(result)


def extract(trace, rowbreaks, layout, expected, pop):
    tree = ET.parse(trace).getroot()
    cc = circles(tree)
    split = (min(q['x'] for q in cc)+max(q['x'] for q in cc))/2
    groups = {}
    for q in cc:
        r = sum(q['y'] > t for t in rowbreaks)
        c = 0 if len(expected)==1 else int(q['x'] > split)
        groups.setdefault((r,c),[]).append(q)
    assert len(groups) == len(expected), (trace,len(groups))
    out = {}
    for (r,c), pts in sorted(groups.items()):
        title, dc = expected[2*r+c if len(expected)>1 else 0]
        assert len(pts) == 48+dc, (trace,title,len(pts))
        x0,x1 = min(q['x'] for q in pts), max(q['x'] for q in pts)
        y0,y1 = min(q['y'] for q in pts), max(q['y'] for q in pts)
        step = (x1-x0)/12
        assert abs((y1-y0)/6-step) < .005
        names = {}
        ll = layout | ({(9,4):'DC'} if dc else {})
        for p in pts:
            ij = (round((p['x']-x0)/step),round((p['y']-y0)/step))
            assert max(abs((p['x']-x0)/step-ij[0]),abs((p['y']-y0)/step-ij[1])) < .003
            assert ij in ll, (trace,title,ij)
            name=ll[ij]; assert name not in names
            names[name]=p
        def nearest(point):
            name=min(names,key=lambda s:math.dist(point,(names[s]['x'],names[s]['y'])))
            return name,math.dist(point,(names[name]['x'],names[name]['y']))
        solid, dashed = set(),set()
        for e in tree.iter('stroke_path'):
            if e.get('color') not in ['0 0 0','0 0 1']:
                continue
            for pp in paths(e):
                for a,b in zip(pp,pp[1:]):
                    na,da=nearest(a); nb,db=nearest(b)
                    if min(da,db)>.03:
                        continue
                    assert max(da,db)<.03,(trace,title,a,b,da,db)
                    assert na!=nb
                    edge=tuple(sorted([na,nb]))
                    (solid if e.get('color')=='0 0 0' else dashed).add(edge)
        assert not solid & dashed
        labeltext = {}
        if pts[0]['color'] == '1 1 1':
            labels = {s:[] for s in names}
            for e in tree.iter('fill_text'):
                for span in e:
                    for g in span:
                        ch=g.get('unicode','')
                        if ch not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or len(ch)!=1: continue
                        xy=transform(e,float(g.get('x')),float(g.get('y')))
                        name,dist=nearest(xy)
                        if dist<3.3: labels[name].append((xy[0],ch))
            labeltext={s:''.join(ch for x,ch in sorted(q)) for s,q in labels.items()}
            assert all(s==v for s,v in labeltext.items()),(trace,title,labeltext)
        sets=components(names,solid)
        membership={s:i for i,q in enumerate(sets) for s in q}
        internal_dashed = sorted(e for e in dashed if membership[e[0]]==membership[e[1]])
        edges=solid|dashed
        assert len(edges)==105+2*dc,(trace,title,len(edges))
        sizes=[len(q) for q in sets]
        populations=[sum(pop[s] for s in q) for q in sets]
        internal_count = len(solid)+len(internal_dashed)
        exterior = 2*(len(edges)-internal_count)
        interior=sum(n*(n-1) for n in sizes)-2*internal_count
        area=[]
        if pts[0]['color']=='1 .5 0':
            ratios={s:q['radius']**2/pop[s] for s,q in names.items()}
            avg=sum(ratios.values())/len(ratios)
            area={s:v/avg-1 for s,v in ratios.items()}
        out[title]=dict(sets=sets,solid=sorted(solid),dashed=sorted(dashed),sizes=sizes,
                       populations=populations,exterior=exterior,interior=interior,
                       internal_dashed=internal_dashed,twice_drawn_dashed=2*len(dashed),
                       sum_squares=sum(x*x for x in populations),labels=labeltext,
                       circle_geometry=names,relative_area_errors=area)
    return out


def main():
    assert os.nice(0)>=15
    assert not (OUT/'figures.json').exists()
    start=time.monotonic()
    data=sgb()
    old=json.loads((ROOT/'results/usa_partitions/graph.json').read_text())
    assert set(map(tuple,old['edges'])) == {e for e in data['edges'] if 'DC' not in e}
    xy=old['coordinates']; x0=xy['CA'][0];y0=xy['ND'][1]
    layout={(round((x-x0)/13.28003),round((y0-y)/13.28003)):s for s,(x,y) in xy.items()}
    versions={}; trace_hashes={}
    for version, main, answer, delta in [('original',135,499,0),('draft',57,189,108.6)]:
        specs=[(main,[],[('115-left',False),('115-right',False)]),
               (main+1,[],[('116-left',False),('116-right',False)]),
               (answer,[180+delta,280+delta],[('245a',True),('245b',True),('246-ext-left',False),('246-ext-right',False),('246-int-left',False),('246-int-right',False)])]
        result={}
        for page, breaks, expected in specs:
            p=OUT/f'{version}-{page}.xml'
            result.update(extract(p,breaks,layout,expected,data['population']))
            trace_hashes[str(p.relative_to(ROOT))]=sha(p)
        p=ROOT/'results/words_primes231_238'/f'{version}-{main-1}.xml'
        result.update(extract(p,[],layout,[('113',False)],data['population']))
        trace_hashes[str(p.relative_to(ROOT))]=sha(p)
        for title,q in result.items():
            wanted={e for e in data['edges'] if len(q['circle_geometry'])==49 or 'DC' not in e}
            assert set(map(tuple,q['solid']+q['dashed']))==wanted
        versions[version]=result
    for title,a in versions['original'].items():
        b=versions['draft'][title]
        for key in ['sets','solid','dashed','sizes','populations','exterior','interior','sum_squares','labels','internal_dashed','twice_drawn_dashed']:
            assert a[key]==b[key],(title,key)
    save(OUT/'figures.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),nice=os.nice(0),wall_seconds=time.monotonic()-start,
        extractor_sha256=sha(__file__),dependency_hashes={p:sha(ROOT/p) for p in ['extract_jigsaw.py','puzzle_xcc.py']},
        source_hashes={str(p.relative_to(ROOT)):sha(p) for p in [SRC/'contiguous-usa.gb',ROOT/'results/usa_partitions/graph.json']},
        trace_hashes=trace_hashes,data=data,versions=versions,global_optimality_repeated=False))
    for title,q in versions['original'].items():
        print(title,q['sizes'],q['exterior'],q['interior'],q['populations'],'internal_dashed',q['internal_dashed'])


if __name__=='__main__':main()
