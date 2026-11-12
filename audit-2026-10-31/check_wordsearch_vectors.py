#!/usr/bin/env python3
"""Read every original PDF grid glyph and all27 solution ovals in Figures71--72."""
import json
from pathlib import Path
from collections import defaultdict
import extract_jigsaw
from extract_jigsaw import transform,inside
from dlx1_audit_tools import sha
from check_colored_basics import OUT,GRID


def polygon(element):
    points=[];previous=None
    for command in element:
        if command.tag in ('moveto','lineto'):
            previous=(float(command.get('x')),float(command.get('y')))
            points.append(transform(element,*previous))
        elif command.tag=='curveto':
            p=[previous]+[(float(command.get('x'+str(i))),float(command.get('y'+str(i)))) for i in range(1,4)]
            for k in range(1,41):
                t=k/40;s=1-t
                point=tuple(s**3*p[0][j]+3*s*s*t*p[1][j]+3*s*t*t*p[2][j]+t**3*p[3][j] for j in (0,1))
                points.append(transform(element,*point))
            previous=p[-1]
        elif command.tag!='closepath':raise AssertionError(command.tag)
    return points


def main():
    extract_jigsaw.OUT=OUT
    expected=json.loads((OUT/'check.json').read_text())['word_search']['matches']
    lookup={frozenset(map(tuple,x['cells'])):name for name,x in expected.items()}
    result={}
    for page in (87,88):
        tree=extract_jigsaw.trace(page);glyphs=[]
        for text in tree.iter('fill_text'):
            for span in text:
                if len(span)!=225:continue
                size=abs(float(span.get('trm').split()[0]))
                for g in span:
                    x,y=transform(text,float(g.get('x')),float(g.get('y')))
                    glyphs.append(dict(letter=g.get('unicode'),x=x,y=y,width=size*float(g.get('adv')),size=size))
        assert len(glyphs)==225,(page,len(glyphs))
        by_y=defaultdict(list)
        for g in glyphs:by_y[round(g['y'],2)].append(g)
        assert len(by_y)==15 and all(len(row)==15 for row in by_y.values())
        grid=[sorted(row,key=lambda g:g['x']) for y,row in sorted(by_y.items())]
        assert [''.join(g['letter'] for g in row) for row in grid]==GRID
        ovals=[]
        if page==88:
            for path in tree.iter('stroke_path'):
                if not any(cmd.tag=='curveto' for cmd in path):continue
                poly=polygon(path);matches=[]
                for dy in (.28,.30,.32):
                    cells=frozenset((r,c) for r,row in enumerate(grid) for c,g in enumerate(row)
                      if inside(g['x']+g['width']/2,g['y']-dy*g['size'],poly))
                    assert cells in lookup,sorted(cells)
                    matches.append(lookup[cells])
                assert len(set(matches))==1
                ovals.append(matches[0])
            assert len(ovals)==27 and set(ovals)==set(expected)
        result[str(page)]=dict(glyphs=225,grid=GRID,ovals=ovals,trace_sha256=sha(OUT/f'page{page}-trace.xml'))
    result.update(status='pass',source_sha256=sha(__file__),method='Original PDF glyph origins and widths; all Bézier ovals sampled40times per segment; membership stable for three vertical glyph-center offsets.')
    (OUT/'vectors.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:450 original glyphs and all27 solution ovals')


if __name__=='__main__':main()
