"""Read the original vector glyphs, ovals and binary diagrams108--112."""
from collections import defaultdict
import xml.etree.ElementTree as ET
import extract_jigsaw
from extract_jigsaw import transform,inside
from check_wordsearch_vectors import polygon
from check_puzzle_figures import curved_subpaths
from layout_native import OUT,save,sha


def glyph_spans(tree):
    for text in tree.iter('fill_text'):
        for span in text:
            size=abs(float(span.get('trm').split()[0]))
            glyphs=[]
            for g in span:
                x,y=transform(text,float(g.get('x')),float(g.get('y')))
                glyphs.append(dict(letter=g.get('unicode'),x=x,y=y,width=size*float(g.get('adv')),size=size))
            yield size,glyphs


def grid(glyphs,m,n):
    x0=min(g['x'] for g in glyphs);x1=max(g['x'] for g in glyphs)
    yy=[g['y'] for g in glyphs if g['letter']!='.'];y0=min(yy);y1=max(yy)
    dx=(x1-x0)/(n-1);dy=(y1-y0)/(m-1)
    board=['.']*(m*n);seen=set()
    for g in glyphs:
        c=round((g['x']-x0)/dx);r=round((g['y']-y0)/dy)
        assert 0<=r<m and 0<=c<n
        assert abs(g['x']-(x0+c*dx))<.2*dx and abs(g['y']-(y0+r*dy))<.3*dy
        cell=r*n+c;assert cell not in seen;seen.add(cell)
        g['cell']=cell;g['source_y']=g['y'];g['y']=y0+r*dy
        board[cell]=g['letter']
    return dict(m=m,n=n,board=''.join(board),glyphs=glyphs)


def subpaths(path):
    current=[]
    for cmd in path:
        if cmd.tag=='moveto' and current:
            yield current;current=[]
        current.append(cmd)
    if current:yield current


def diagrams(tree):
    rects=[]
    for tag in ['fill_path','stroke_path']:
        for path in tree.iter(tag):
            for commands in subpaths(path):
                pts=[transform(path,float(c.get('x')),float(c.get('y')))
                     for c in commands if c.tag in ['moveto','lineto']]
                if not pts:continue
                xs=[x for x,y in pts];ys=[y for x,y in pts]
                w=max(xs)-min(xs);h=max(ys)-min(ys)
                if min(ys)>570 and max(ys)<610 and 3.9<w<4.1 and 3.9<h<4.1:
                    rects.append(dict(x=(min(xs)+max(xs))/2,y=(min(ys)+max(ys))/2,black=tag=='fill_path'))
    xs=sorted({round(p['x'],2) for p in rects});groups=[]
    for x in xs:
        if not groups or x-groups[-1][-1]>6:groups.append([])
        groups[-1].append(x)
    assert len(groups)==6 and all(len(g)==8 for g in groups),(len(groups),[len(g) for g in groups])
    ys=sorted({round(p['y'],2) for p in rects});assert len(ys)==8,ys
    result=[]
    for group in groups:
        seen=set();black=set()
        for p in rects:
            if not group[0]-.1<p['x']<group[-1]+.1:continue
            c=min(range(8),key=lambda k:abs(group[k]-p['x']));r=min(range(8),key=lambda k:abs(ys[k]-p['y']))
            assert abs(group[c]-p['x'])<.02 and abs(ys[r]-p['y'])<.02
            seen.add(8*r+c)
            if p['black']:black.add(8*r+c)
        assert len(seen)==64
        result.append(dict(board=''.join('.' if k in black else 'A' for k in range(64)),black_cells=sorted(black)))
    return result


def main():
    extract_jigsaw.OUT=OUT
    trees={page:extract_jigsaw.trace(page) for page in [136,441,442,443]}
    presidential=[];wordcross=[];torto=[]
    for size,glyphs in glyph_spans(trees[441]):
        if len(glyphs)==225 and 6.9<size<7.1:presidential.append(grid(glyphs,15,15))
        if len(glyphs)==215 and 5.9<size<6.1:presidential.append(grid(glyphs,5,43))
    assert len(presidential)==2
    for path in curved_subpaths(trees[441]):
        poly=polygon(path);matches=[]
        for i,g in enumerate(presidential):
            hits=[frozenset(p['cell'] for p in g['glyphs'] if inside(p['x']+p['width']/2,p['y']-k*p['size'],poly)) for k in [.28,.30,.32]]
            assert len(set(hits))==1
            if hits[0]:matches.append((i,hits[0]))
        assert len(matches)==1,matches
        i,cells=matches[0];presidential[i].setdefault('ovals',[]).append(sorted(cells))
    assert [len(g['ovals']) for g in presidential]==[38,38]
    for size,glyphs in glyph_spans(trees[136]):
        if len(glyphs)==35 and size==8:wordcross.append(grid(glyphs,8,8))
        if len(glyphs)==18 and size==8:torto.append(grid(glyphs,6,3))
    for size,glyphs in glyph_spans(trees[442]):
        if len(glyphs)==33 and size==8:
            wordcross.append(grid(glyphs,8,8) if len(wordcross)<4 else grid(glyphs,7,9))
        if len(glyphs)==34 and size==8:wordcross.append(grid(glyphs,5,11))
        if len(glyphs)==205 and 6.3<size<6.5:wordcross.append(grid(glyphs,20,20))
    for size,glyphs in glyph_spans(trees[443]):
        if len(glyphs)==18 and size==8 and max(g['y'] for g in glyphs)-min(g['y'] for g in glyphs)>1:
            torto.append(grid(glyphs,6,3))
    assert len(wordcross)==7 and len(torto)==5
    for g in presidential+wordcross+torto:
        g['printed_glyphs']=len(g.pop('glyphs'))
    result=dict(script_sha256=sha(__file__),trace_hashes={p:sha(OUT/f'page{p}-trace.xml') for p in trees},
                presidential=presidential,wordcross=wordcross,torto=torto,diagrams=diagrams(trees[442]))
    save(OUT/'original-figures.json',result)
    print('Read2 presidential grids/76 ovals,7 wordcross grids,5 Torto grids and6 binary diagrams.')


if __name__=='__main__':main()
