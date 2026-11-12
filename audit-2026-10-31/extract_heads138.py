"""Decode all 488 signed edges from original clipped triangle vectors."""
from collections import defaultdict
from datetime import datetime, timezone
import math
import xml.etree.ElementTree as ET
import heads138 as h
from extract_jigsaw import paths

COLORS = {'0 1 0':'A', '0 0 1':'B', '1 1 1':'C', '1 0 0':'D'}


def extract(page):
    trace = h.ROOT / 'results/nuts137' / f'page{page}-trace.xml'
    tree = ET.parse(trace)
    stack, records = [], defaultdict(dict)
    raw = []
    for e in tree.getroot().find('page'):
        if e.tag.startswith('clip_'):
            polygons = paths(e) if e.tag == 'clip_path' else []
            box = None
            if len(polygons) == 1 and len(polygons[0]) == 5:
                p = polygons[0]
                xs, ys = [x for x,y in p], [y for x,y in p]
                x0,x1,y0,y1 = min(xs),max(xs),min(ys),max(ys)
                if abs(x1-x0-(y1-y0)) < .001 and 18 < x1-x0 < 25:
                    box = (round((x0+x1)/2,3), round((y0+y1)/2,3), round(x1-x0,3))
            stack.append(box)
        elif e.tag == 'pop_clip':
            stack.pop()
        elif e.tag == 'fill_path' and e.get('color') in COLORS and e.get('colorspace') == 'DeviceRGB':
            polys = paths(e)
            if not (len(polys) == 1 and len(polys[0]) == 3):
                continue
            boxes = [b for b in stack if b is not None]
            assert boxes
            cx,cy,step = boxes[-1]
            p = polys[0]
            # Locate the short base independently of PDF point ordering.
            lengths = [math.dist(p[i],p[(i+1)%3]) for i in range(3)]
            i = min(range(3), key=lambda j:lengths[j])
            tip = p[(i+2)%3]
            base = [(p[i][j]+p[(i+1)%3][j])/2 for j in range(2)]
            dx,dy = base[0]-cx,base[1]-cy
            assert min(abs(dx),abs(dy)) < .002
            d = (0 if dy < 0 else 2) if abs(dy)>abs(dx) else (1 if dx<0 else 3)
            distance = math.dist(tip,(cx,cy))/step
            assert min(abs(distance),abs(distance-1)) < .001
            head = distance < .001
            ch = COLORS[e.get('color')]
            if not head: ch = ch.lower()
            assert d not in records[cx,cy,step]
            records[cx,cy,step][d] = ch
            raw.append(dict(center=[cx,cy],step=step,side=d,label=ch,triangle=p))
    cells = []
    for (cx,cy,step),edges in sorted(records.items(),key=lambda x:(x[0][1],x[0][0])):
        assert len(edges) == 4
        cells.append(dict(center=[cx,cy],step=step,word=''.join(edges[i] for i in range(4))))
    return cells, raw


def grid(cells,nr,nc):
    assert len(cells) == nr*nc
    xs,ys = sorted(set(x['center'][0] for x in cells)),sorted(set(x['center'][1] for x in cells))
    assert len(xs)==nc and len(ys)==nr
    for seq in [xs,ys]:
        assert all(abs((b-a)-cells[0]['step'])<.002 for a,b in zip(seq,seq[1:]))
    cells.sort(key=lambda x:(x['center'][1],x['center'][0]))
    return dict(nr=nr,nc=nc,words=[x['word'] for x in cells],cells=cells)


def main():
    q, qr = extract(140); a, ar = extract(452)
    assert len(q)==73 and len(a)==49
    inventory = [c for c in q if c['step']<20]
    assert len(inventory)==24 and sorted(h.tile(c['word']) for c in inventory)==sorted(h.TILES)
    figures = {
        'question-a':grid([c for c in q if c['step']>20 and c['center'][0]<250],4,6),
        'question-b':grid([c for c in q if c['step']>20 and c['center'][0]>250],5,5),
        'answer-a':grid([c for c in a if c['center'][0]<250],4,6),
        'answer-c':grid([c for c in a if c['center'][0]>250],5,5)}
    for label,fig in figures.items():
        joker = fig['words'][12] if fig['nr']==5 else None
        h.validate(fig['words'],fig['nr'],fig['nc'],torus=fig['nr']==4,joker=joker)
        fig['joker']=joker
    h.save(h.OUT/'figures-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=h.sha(__file__),geometry_sha256=h.sha(h.__file__),
        book_sha256=h.sha(h.ROOT.parent/'books/taocp-vol4b-ed1-print2-2022.pdf'),
        traces={str(p):h.sha(h.ROOT/'results/nuts137'/f'page{p}-trace.xml') for p in [140,452]},
        signed_edges=488,inventory=inventory,figures=figures,triangles=qr+ar))
    print('PASS138: 24 inventory tiles and all four arrangements; 488 signed edges.')
    for name,fig in figures.items():
        print(name,fig['joker'])
        for r in range(fig['nr']):print(' '.join(fig['words'][r*fig['nc']:(r+1)*fig['nc']]))


if __name__=='__main__':main()
