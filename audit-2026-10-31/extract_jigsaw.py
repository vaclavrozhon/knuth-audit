#!/usr/bin/env python3
"""Extract glyphs and region boundaries from original PDF vectors, DLX59--63."""
from collections import defaultdict
import json
import math
import subprocess
import xml.etree.ElementTree as ET
from dlx1_audit_tools import ROOT, sha

OUT = ROOT/'results/jigsaw'
BOOK = ROOT.parent/'books/taocp-vol4b-ed1-print2-2022.pdf'


def trace(page):
    OUT.mkdir(exist_ok=True)
    path = OUT/f'page{page}-trace.xml'
    if not path.exists():
        subprocess.run(['mutool','draw','-q','-F','trace','-o',str(path),
                        str(BOOK),str(page+20)],check=True,
                       stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    return ET.parse(path)


def transform(element, x, y):
    a,b,c,d,e,f = map(float,element.get('transform').split())
    return a*x+c*y+e,b*x+d*y+f


def paths(element):
    result, current = [], []
    for p in element:
        if p.tag == 'moveto':
            if current: result.append(current)
            current = [transform(element,float(p.get('x')),float(p.get('y')))]
        elif p.tag == 'lineto':
            current.append(transform(element,float(p.get('x')),float(p.get('y'))))
        elif p.tag == 'closepath':
            if current and current[0] != current[-1]: current.append(current[0])
        else:
            # Curves are not part of any of these orthogonal box diagrams.
            return []
    if current: result.append(current)
    return result


def inside(x,y,polygon):
    parity = False
    for (x1,y1),(x2,y2) in zip(polygon,polygon[1:]+polygon[:1]):
        if (y1>y) != (y2>y) and x < x1+(y-y1)*(x2-x1)/(y2-y1):
            parity = not parity
    return parity


def extract(page, nr, nc, x0, y0, step, alphabet='', omit=()):
    tree = trace(page)
    glyphs, walls, colors = [], set(), {}
    cells = ['.']*(nr*nc)
    for text in tree.iter('fill_text'):
        for span in text:
            for g in span:
                ch = g.get('unicode','')
                if ch not in alphabet or len(ch)!=1: continue
                x,y = transform(text,float(g.get('x')),float(g.get('y')))
                c,r = math.floor((x-x0)/step),math.floor((y-y0)/step)
                if not (0<=r<nr and 0<=c<nc): continue
                # Baselines and left glyph origins lie strictly inside cells.
                assert .05<(x-x0)/step-c<.95 and .05<(y-y0)/step-r<.95
                u = r*nc+c
                assert cells[u] in ('.',ch),(page,r,c,cells[u],ch)
                cells[u] = ch
                glyphs.append(dict(cell=u,text=ch,origin=[x,y]))
    for p in tree.iter('stroke_path'):
        if p.get('color')!='0 0 0' or float(p.get('linewidth'))<.5: continue
        for points in paths(p):
            for a,b in zip(points,points[1:]):
                aa=((a[0]-x0)/step,(a[1]-y0)/step)
                bb=((b[0]-x0)/step,(b[1]-y0)/step)
                ca,ra,cb,rb=map(round,(*aa,*bb))
                if max(abs(v-round(v)) for v in (*aa,*bb))>.004: continue
                if not (0<=ca<=nc and 0<=cb<=nc and 0<=ra<=nr and 0<=rb<=nr): continue
                assert ca==cb or ra==rb
                if ca==cb:
                    for r in range(min(ra,rb),max(ra,rb)): walls.add(('v',r,ca))
                else:
                    for c in range(min(ca,cb),max(ca,cb)): walls.add(('h',ra,c))
    for p in tree.iter('fill_path'):
        if p.get('colorspace')!='DeviceRGB':continue
        polygons = paths(p)
        for r in range(nr):
            for c in range(nc):
                if sum(inside(x0+(c+.5)*step,y0+(r+.5)*step,q) for q in polygons)%2:
                    colors[r*nc+c]=p.get('color')
    omitted=set(omit)
    unseen=set(range(nr*nc))-omitted
    components=[]
    while unseen:
        q=[min(unseen)];unseen.remove(q[0])
        for u in q:
            r,c=divmod(u,nc)
            for rr,cc,w in [(r-1,c,('h',r,c)),(r+1,c,('h',r+1,c)),
                            (r,c-1,('v',r,c)),(r,c+1,('v',r,c+1))]:
                v=rr*nc+cc
                if 0<=rr<nr and 0<=cc<nc and v in unseen and w not in walls:
                    q.append(v);unseen.remove(v)
        components.append(sorted(q))
    # New York's Long Island is deliberately disconnected and identified by
    # the same pink fill as the rest of New York, in both printed diagrams.
    groups=defaultdict(list)
    for i,q in enumerate(components):
        filled={colors.get(u) for u in q}
        assert len(filled)==1,(page,q,filled)
        key=('color',filled.pop()) if q[0] in colors else ('component',i)
        groups[key].extend(q)
    regions=sorted(sorted(q) for q in groups.values())
    for u in omitted: assert cells[u]=='.'
    return dict(page=page,nrows=nr,ncols=nc,origin=[x0,y0],step=step,
                cells=cells,rows=[''.join(cells[r*nc:(r+1)*nc]) for r in range(nr)],
                glyphs=glyphs,walls=sorted(walls),components=components,
                regions=regions,colors=colors,omitted=sorted(omitted))


def main():
    d={}
    for label,x in [('34a',83.519),('34b',192.659),('34c',300.659)]:
        d[label]=extract(78,9,9,x,136.95899,80.601/9,
                         '123456789' if label=='34a' else 'GRANDTIMEWVYNLKF')
    for label,x in [('59a',101.100009),('59b',210.18),('59c',318.18)]:
        d[label]=extract(428,9,9,x,178.12,72.62/9,
                         '123456789' if label=='59a' else 'GRANDTIMEWVYNLKF')
    d['35a']=extract(78,5,5,105.240009,543.31997,44.8/5,'12345')
    d['35b']=extract(78,9,7,183.899,525.44497,62.701/7,'123456789')
    d['35c']=extract(78,9,9,279.419,525.459,80.601/9,'123456789')
    holes={'a':[0,5,14,15,32,33], 'b':[5,8,17,26,27,35],
           'c':[0,5,14,15,16,17,20,21,22,23,30,35]}
    for k,x,xx in [('a',107.879,120.29899),('b',202.259,214.67899),
                   ('c',295.679,308.099)]:
        d['60q'+k]=extract(129,6,6,x,439.91899,53.702/6,'123456',holes[k])
        d['60a'+k]=extract(428,6,6,xx,298.73899,53.702/6,'123456',holes[k])
    d['61']=extract(429,5,5,77.78999,231.88999,38.081/5,'12345')
    for i,x in enumerate([82.619,123.298999,163.919,204.599,245.27899,285.959,326.639,367.319],1):
        d[f'62n4-{i}']=extract(428,4,4,x,473.87898,21.481/4)
    for i,x in enumerate([54.359,111.179,167.999],1):
        d[f'62n7-{i}']=extract(429,7,7,x,87.39899,37.581/7)
    for i,x in enumerate([224.82,286.979,349.199],1):
        d[f'62n8-{i}']=extract(429,8,8,x,84.698978,42.981/8)
    for label,x in [('62n9-b',136.89),('62n9-c',225.45001),('63',315.03)]:
        d[label]=extract(429,9,9,x,216.63,68.58/9,'123456789' if label=='63' else '')
    for label,s in d.items():
        size=6 if label.startswith('60') else s['nrows']
        assert all(len(r)==size for r in s['regions']),(label,list(map(len,s['regions'])))
        print(label,'/'.join(s['rows']),len(s['glyphs']),list(map(len,s['regions'])))
    for letter in 'abc':
        assert d['34'+letter]['regions']==d['59'+letter]['regions']
        assert d['60q'+letter]['regions']==d['60a'+letter]['regions']
    assert d['35a']['regions']==d['61']['regions']
    assert d['35c']['cells']==d['63']['cells']
    result=dict(book_sha256=sha(BOOK),source_sha256=sha(__file__),
                trace_sha256={str(p):sha(OUT/f'page{p}-trace.xml') for p in (78,129,428,429)},
                sources=d)
    (OUT/'pdf-diagrams.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
