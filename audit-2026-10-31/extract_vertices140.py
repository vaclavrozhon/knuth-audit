"""Read every colored corner from the original 18 triangular tile figures."""
from datetime import datetime,timezone
from math import dist,sqrt
from itertools import combinations
from collections import defaultdict,Counter
import xml.etree.ElementTree as ET
import vertices140 as h
from extract_jigsaw import transform

PALETTE={'1 1 1':'a','1 .75 .75':'b','.5 .5 1':'c','.2 .2 .2':'d'}


def page_sectors(page):
    path=(h.ROOT/'results/heads139/page453-trace.xml') if page==453 else h.OUT/f'page{page}-trace.xml'
    result=[]
    for e in ET.parse(path).getroot().iter('fill_path'):
        if e.get('colorspace')!='DeviceRGB' or e.get('color') not in PALETTE:continue
        if [x.tag for x in e]!=['moveto','lineto','curveto']:continue
        p=e[0];point=transform(e,float(p.get('x')),float(p.get('y')))
        if page==141 and point[1]>160:continue
        result.append(dict(point=point,color=PALETTE[e.get('color')]))
    expected={141:216,453:576,454:504}[page]
    assert len(result)==expected,(page,len(result))
    return result


def decode(sectors):
    assert len(sectors)==72
    for i in range(0,72,3):
        ds=[dist(a['point'],b['point']) for a,b in combinations(sectors[i:i+3],2)]
        assert max(ds)-min(ds)<.004,ds
    step=dist(sectors[0]['point'],sectors[1]['point'])
    ymax=max(x['point'][1] for x in sectors)
    floats=[((x['point'][0]/step)-(ymax-x['point'][1])/(step*sqrt(3)),(ymax-x['point'][1])/(step*sqrt(3)/2)) for x in sectors]
    xmin=min(x for x,y in floats)
    points=[(x-xmin,y) for x,y in floats]
    assert max(abs(a-round(a)) for p in points for a in p)<.001
    points=[tuple(map(round,p)) for p in points]
    colors=defaultdict(list);cells=[];triangles=[]
    for i in range(0,72,3):
        triangle=points[i:i+3];t=h.cell(triangle);cells.append(t)
        for v,s in zip(triangle,sectors[i:i+3]):
            colors[v].append(dict(triangle=i//3,color=s['color']))
        triangles.append(dict(cell=t,vertices=triangle,colors=[s['color'] for s in sectors[i:i+3]]))
    cells=h.normalize_shape(cells);assert len(cells)==len(set(cells))==24
    tile_types=[]
    for tri in triangles:
        cs=dict(zip(tri['vertices'],tri['colors']))
        tile_types.append(h.piece(''.join(cs[v] for v in h.vertices(tri['cell']))))
    assert sorted(tile_types)==h.PIECES
    conflicts=[dict(vertex=v,occurrences=cs) for v,cs in sorted(colors.items()) if len({x['color'] for x in cs})>1]
    word=None if conflicts else ''.join(colors[v][0]['color'] for v in h.vertex_list(cells))
    if not conflicts:h.validate(cells,word)
    return dict(cells=cells,vertex_colors=word,vertices=h.vertex_list(cells),shape_key=h.shape_key(cells),
        pixel_bounds=[min(s['point'][0] for s in sectors),min(s['point'][1] for s in sectors),max(s['point'][0] for s in sectors),max(s['point'][1] for s in sectors)],
        triangles=triangles,sectors=sectors,vertex_conflicts=conflicts,all24_tile_types_verified=True)


def main():
    figures={}
    for page,labels in [(141,['a1','a2','a3']),
                        (453,['b1','b2','b3','b4','b5','b6','b7','b8']),
                        (454,['c1','c2','c3','c4','c5','c6','c7'])]:
        sectors=page_sectors(page)
        for i,label in enumerate(labels):
            fig=decode(sectors[72*i:72*i+72]);fig['page']=page;figures[label]=fig
    invalid={name:fig['vertex_conflicts'] for name,fig in figures.items() if fig['vertex_conflicts']}
    assert set(invalid)=={'c3'} and len(invalid['c3'])==2
    shapes,levels=h.polyiamonds(6);hexes,hexlevels=h.polyhexes(4)
    assert levels==[1,1,1,3,4,12] and hexlevels==[1,1,3,7]
    scaled={h.shape_key(h.scale(s,2)):s for s in shapes};assert len(scaled)==12
    shown_b={tuple(map(tuple,figures[k]['shape_key'])) for k in ['a1']+[f'b{i}' for i in range(1,9)]}
    assert len(shown_b)==9 and shown_b<=set(scaled)
    shown_c={tuple(map(tuple,figures[f'c{i}']['shape_key'])) for i in range(1,8)}
    assert len(shown_c)==7 and shown_c=={x['cells'] for x in hexes}
    cases=[]
    for label,fig in figures.items():
        cases.append(dict(label=label,cells=fig['cells'],figure=label,part=label[0]))
    for i,key in enumerate(sorted(set(scaled)-shown_b),1):
        cases.append(dict(label=f'b-impossible{i}',cells=key,base_hexiamond=scaled[key],part='b',figure=None))
    assert len(cases)==21 and len({h.shape_key(c['cells']) for c in cases})==21
    h.save(h.OUT/'figures-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=h.sha(__file__),
        geometry_sha256=h.sha(h.__file__),book_sha256=h.sha(h.ROOT.parent/'books/taocp-vol4b-ed1-print2-2022.pdf'),
        trace_sha256={str(p):h.sha(h.ROOT/'results/heads139/page453-trace.xml' if p==453 else h.OUT/f'page{p}-trace.xml') for p in [141,453,454]},
        figures=figures,all_corners=1296,all_triangles=432,invalid_figures=invalid,
        hexiamond_generation_counts=levels,tetrahex_generation_counts=hexlevels,
        hexiamonds=shapes,tetrahexes=hexes,cases=cases,
        impossible_shape_icons_status='The three remaining generated hexiamonds still need direct comparison with the three small original silhouette icons.'))
    print('EXTRACTED140:18 figures,432 triangles,1296 corners; c3 has two conflicting vertices; all12 hexiamonds and7 tetrahexes generated;21 distinct cases.')
    for c in cases:print(c['label'],len(h.vertex_list(c['cells'])),len(h.symmetries(c['cells'])))


if __name__=='__main__':main()
