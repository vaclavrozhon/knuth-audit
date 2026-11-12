"""Read strip outlines and ink crossing each unit edge from vector source paths."""
from pathlib import Path
import xml.etree.ElementTree as ET
from extract_jigsaw import transform
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/chain150'


def points(t,q):
    if q.tag in ['moveto','lineto']:return [transform(t,float(q.get('x')),float(q.get('y')))]
    if q.tag=='curveto':return [transform(t,float(q.get('x'+str(i))),float(q.get('y'+str(i)))) for i in [1,2,3]]
    return []


def paths(path):
    clips=[];rectangles=[];segments=[]
    for t in ET.parse(path).getroot().find('page'):
        if t.tag=='clip_path':
            ps=[p for q in t for p in points(t,q)]
            clips.append((min(x for x,y in ps),max(x for x,y in ps),min(y for x,y in ps),max(y for x,y in ps)))
        elif t.tag=='pop_clip':clips.pop()
        elif t.tag=='stroke_path':
            first=prev=None;poly=[]
            for q in t:
                ps=points(t,q)
                if q.tag=='moveto':first=prev=ps[0];poly=[prev];continue
                if q.tag=='lineto':poly.append(ps[0])
                if q.tag=='curveto':poly.append(None)
                if q.tag=='closepath':
                    if len(poly)==4 and None not in poly:
                        xs=sorted({round(x,3) for x,y in poly});ys=sorted({round(y,3) for x,y in poly})
                        if len(xs)==len(ys)==2:rectangles.append((xs[0],xs[1],ys[0],ys[1]))
                    ps=[first]
                if ps:
                    segments.append(dict(points=[prev]+ps,clips=list(clips)));prev=ps[-1]
    return rectangles,segments


def at(ps,t):
    while len(ps)>1:ps=[tuple((1-t)*a+t*b for a,b in zip(x,y)) for x,y in zip(ps,ps[1:])]
    return ps[0]


def crossings(segments,axis,value,lo,hi):
    found=[]
    for s in segments:
        ps=s['points'];vs=[p[axis] for p in ps]
        if value<=min(vs) or value>=max(vs):continue
        # Source arcs here are monotone quarter-ellipses or straight segments.
        increasing=ps[0][axis]<ps[-1][axis]
        if not min(ps[0][axis],ps[-1][axis])<value<max(ps[0][axis],ps[-1][axis]):continue
        a,b=0.,1.
        for _ in range(40):
            m=(a+b)/2
            if (at(ps,m)[axis]<value)==increasing:a=m
            else:b=m
        x,y=at(ps,(a+b)/2);v=(x,y)[1-axis]
        if not lo<v<hi:continue
        if not all(x0-1e-5<=x<=x1+1e-5 and y0-1e-5<=y<=y1+1e-5 for x0,x1,y0,y1 in s['clips']):continue
        found.append(v)
    return sorted({round(v,6) for v in found})


def strips(path,y0,y1):
    rects,segs=paths(path);rects=[p for p in rects if y0<p[2]<p[3]<y1]
    rects.sort(key=lambda p:(round(p[2]/5),p[0]));result=[]
    assert len(rects)==18
    for k,(x0,x1,a,b) in enumerate(rects):
        unit=b-a;n=round((x1-x0)/unit);assert abs((x1-x0)/unit-n)<.002
        contacts=[]
        for side in ['N','S','W','E']:
            for j in range(n if side in 'NS' else 1):
                if side in 'NS':
                    values=crossings(segs,1,a+.07*unit if side=='N' else b-.07*unit,x0+(j+.1)*unit,x0+(j+.9)*unit)
                    values=[(v-x0)/unit-j for v in values]
                else:
                    values=crossings(segs,0,x0+.07*unit if side=='W' else x1-.07*unit,a+.1*unit,a+.9*unit)
                    values=[(v-a)/unit for v in values]
                if values:contacts.append(dict(side=side,cell=j if side in 'NS' else (0 if side=='W' else n-1),crossings=values,
                    kind='special' if max(values)-min(values)<.3 else 'normal'))
        result.append(dict(index=k,length=n,bounds=(x0,x1,a,b),contacts=contacts))
    return result


if __name__=='__main__':
    p=ROOT/'results/bricks147/original-163.xml';data=strips(p,350,380)
    save(OUT/'strips-extracted.json',dict(extractor_sha256=sha(__file__),trace_sha256=sha(p),pieces=data))
    for r in data:print(r['index'],r['length'],[(c['side'],c['cell'],c['kind'],[round(v,3) for v in c['crossings']]) for c in r['contacts']])
