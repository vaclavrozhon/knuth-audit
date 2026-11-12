"""Read every colored wedge and forced-neighborhood glyph from PDF vectors."""
from pathlib import Path
from collections import Counter
import subprocess,xml.etree.ElementTree as ET
import extract_jigsaw as ex
from extract_layout_figures import glyph_spans,grid
from graph_native import ROOT,sha,save

OUT=ROOT/'results/graphs117_120'
PALETTE={'1 1 1':'W','1 .75 .75':'R','.5 .5 1':'B','.2 .2 .2':'K'}

def tiles(tree):
    fills=[p for p in tree.iter('fill_path') if p.get('colorspace')=='DeviceRGB']
    assert len(fills)%4==0
    result=[]
    for offset in range(0,len(fills),4):
        four=fills[offset:offset+4];triangles=[ex.paths(p) for p in four]
        assert all(len(ps)==1 and len(ps[0])==3 for ps in triangles)
        triangles=[ps[0] for ps in triangles]
        xs=[x for t in triangles for x,y in t];ys=[y for t in triangles for x,y in t]
        x0,x1,y0,y1=min(xs),max(xs),min(ys),max(ys)
        assert abs((x1-x0)-(y1-y0))<.005
        cx,cy=(x0+x1)/2,(y0+y1)/2;cs={}
        for p,t in zip(four,triangles):
            dx=sum(x for x,y in t)/3-cx;dy=sum(y for x,y in t)/3-cy
            side=('E' if dx>0 else 'W') if abs(dx)>abs(dy) else ('S' if dy>0 else 'N')
            assert side not in cs and p.get('color') in PALETTE;cs[side]=PALETTE[p.get('color')]
        assert len(cs)==4
        result.append(dict(bounds=[x0,y0,x1,y1],colors=''.join(cs[d] for d in 'NESW')))
    return result

def main():
    ex.OUT=OUT
    types=tiles(ex.trace(138));assert len(types)==20
    families=[[t['colors'] for t in types[:10]],[t['colors'] for t in types[10:]]]
    assert all(len(set(f))==10 for f in families)
    figures=tiles(ex.trace(445));assert len(figures)==672
    arrays=[]
    for family,subset in zip(families,[figures[:336],figures[336:]]):
        # The drawing emits each row left to right, from top to bottom.
        rows=[subset[k:k+56] for k in range(0,336,56)]
        assert len(rows)==6
        for row in rows:
            assert max(t['bounds'][1] for t in row)-min(t['bounds'][1] for t in row)<.004
            assert all(a['bounds'][0]<b['bounds'][0] for a,b in zip(row,row[1:]))
        board=[[family.index(t['colors']) for t in row] for row in rows]
        for r in range(6):
            for c in range(56):
                t=family[board[r][c]]
                if r:assert family[board[r-1][c]][2]==t[0]
                if c:assert family[board[r][c-1]][1]==t[3]
        arrays.append(board)
    forced=[]
    for size,gg in glyph_spans(ex.trace(445)):
        if 6.9<size<7.1 and len(gg)==25 and all(g['letter'] in '0123456789?' for g in gg):forced.append(grid(gg,5,5))
    forced.sort(key=lambda g:min(x['x'] for x in g['glyphs']));assert len(forced)==10
    assert all(g['board'][12]==str(i) for i,g in enumerate(forced))
    save(OUT/'tetrads120-vectors.json',dict(book_sha256=sha(ex.BOOK),script_sha256=sha(__file__),palette=PALETTE,
        edge_order='NESW',types=types,families=families,printed_arrays=arrays,
        forced_neighborhoods=forced,wedge_count=2768,forced_glyph_count=250,
        traces={str(p):sha(OUT/f'page{p}-trace.xml') for p in [138,445]}))
    print('120 vectors:80 type wedges +2688 tiling wedges +250 forced-neighborhood glyphs; all displayed edges match.')

if __name__=='__main__':main()
