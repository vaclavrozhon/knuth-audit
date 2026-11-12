"""All222 original triangle wedges in58--59 and all labels in answer124."""
from collections import Counter
from datetime import datetime,timezone
from math import sqrt
import extract_jigsaw as ex
from extract_layout_figures import glyph_spans
import macmahon126 as mc

PALETTE={'1 1 1':'a','1 .75 .75':'b','.5 .5 1':'c','.2 .2 .2':'d'}


def main():
    ex.OUT=mc.OUT
    tree=ex.trace(91);fills=[p for p in tree.iter('fill_path') if p.get('colorspace')=='DeviceRGB']
    assert len(fills)==222
    tiles=[]
    for i in range(0,len(fills),3):
        points=[];cs={};center=None
        for p in fills[i:i+3]:
            paths=ex.paths(p);assert len(paths)==1 and len(paths[0])==3
            c,a,b=paths[0];assert center is None or max(abs(v-w) for v,w in zip(c,center))<.002
            center=c;points += [a,b]
            dx,dy=b[0]-a[0],b[1]-a[1]
            side='-' if abs(dy)<.002 else '/' if dx*dy<0 else '\\'
            assert side not in cs;cs[side]=PALETTE[p.get('color')]
        vertices=sorted({tuple(round(x,3) for x in p) for p in points});assert len(vertices)==3
        colors=''.join(cs[k] for k in ['-','/','\\'])
        tiles.append(dict(center=center,vertices=vertices,colors=colors,piece=mc.geom.piece(colors)))
    assert sorted(x['piece'] for x in tiles[:24])==mc.geom.PIECES
    lookup={frozenset(mc.geom.vertices(t)):t for t in mc.geom.TRIANGLES}
    actual_vertices={p for v in lookup for p in v}
    unit_x=[x+y/2 for x,y in actual_vertices];unit_y=[y*sqrt(3)/2 for x,y in actual_vertices]
    figures=[]
    for n,part in enumerate([tiles[24:48],tiles[48:72]]):
        xx=[x for tile in part for x,y in tile['vertices']];yy=[y for tile in part for x,y in tile['vertices']]
        scale=(max(xx)-min(xx))/(max(unit_x)-min(unit_x));x0=min(xx)-scale*min(unit_x);y0=max(yy)+scale*min(unit_y)
        cells={};edges={};records=[]
        for tile in part:
            vv=[]
            for x,y in tile['vertices']:
                v=(y0-y)/(scale*sqrt(3)/2);u=(x-x0)/scale-v/2
                assert abs(u-round(u))<.001 and abs(v-round(v))<.001
                vv.append((round(u),round(v)))
            t=lookup[frozenset(vv)];assert t not in cells;cells[t]=tile['colors']
            for e,c in zip(mc.geom.edges(t),tile['colors']):
                assert e not in edges or edges[e]==c
                edges[e]=c
            records.append(dict(cell=t,colors=tile['colors'],piece=tile['piece']))
        assert len(cells)==24 and sorted(tile['piece'] for tile in part)==mc.geom.PIECES
        boundary={e:c for e,c in edges.items() if len(mc.geom.EDGE_TRIANGLES[e])==1}
        if n==1:assert set(boundary.values())=={'a'}
        monos={cs[0]:t for t,cs in cells.items() if len(set(cs))==1}
        if n==1:assert monos['a']==(2,0,0) and {monos[c] for c in 'bcd'}=={(1,2,0),(2,1,0),(2,2,0)}
        figures.append(dict(label='59'+str(n),tiles=records,edge_colors=[dict(edge=e,color=c) for e,c in sorted(edges.items())],
                            boundary_color_histogram=dict(Counter(boundary.values())),monochrome_positions=monos))
    assert tiles[-2]['piece']!=tiles[-1]['piece']
    assert sorted(tiles[-2]['colors'])==sorted(tiles[-1]['colors'])
    spans=[gs for size,gs in glyph_spans(ex.trace(446)) if 4.49<size<4.51]
    assert len(spans)==1 and len(spans[0])==30
    glyphs=spans[0];labels=[];i=0
    while i<len(glyphs):
        part=glyphs[i:i+2];i+=2
        if i<len(glyphs) and glyphs[i]['letter']=="'":part.append(glyphs[i]);i+=1
        s=''.join(g['letter'] for g in part);labels.append(dict(label=s,x=part[0]['x'],y=part[0]['y']))
    expected={mc.geom.name((x,y,z)) for x in range(3) for y in range(2) for z in range(2)}
    assert {g['label'] for g in labels}==expected
    by={g['label']:g for g in labels};origin=by['00'];dx=by['10']['x']-origin['x'];dy=origin['y']-by['01']['y']
    for g in labels:
        x,y=int(g['label'][0]),int(g['label'][1]);z=int(len(g['label'])==3)
        xp=origin['x']+dx*(x+y/2)+z*(by["00'"]['x']-origin['x'])
        yp=origin['y']-dy*y+z*(by["00'"]['y']-origin['y'])
        assert abs(g['x']-xp)<.006 and abs(g['y']-yp)<.006
    assert abs(dy/dx-sqrt(3)/2)<.0002
    mc.save(mc.OUT/'original-figures-checked.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=mc.sha(__file__),
      traces={str(p):mc.sha(mc.OUT/f'page{p}-trace.xml') for p in [91,446]},wedge_count=222,
      definition_tiles=tiles[:24],figures=figures,chiral_examples=tiles[-2:],coordinate_figure_labels=labels,
      claim='Every original wedge, both24-piece tilings and all12 coordinate labels checked. Figure59b has white boundary and the stated central monochrome positions.'))
    print('PASS:222 wedges, both24-piece figures,12 coordinate labels; monochromes',figures[1]['monochrome_positions'])


if __name__=='__main__':main()
