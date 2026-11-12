"""All original PDF glyphs and solution ovals in answers105--107."""
from collections import Counter,defaultdict
import json
import xml.etree.ElementTree as ET
import extract_jigsaw
from extract_jigsaw import transform,inside
from check_wordsearch_vectors import polygon
from puzzle_xcc import OUT,save,sha
from word_puzzles import placements


def curved_subpaths(tree):
    for path in tree.iter('stroke_path'):
        current=None
        for command in path:
            if command.tag=='moveto':
                if current is not None and any(c.tag=='curveto' for c in current):yield current
                current=ET.Element('stroke_path',path.attrib)
            assert current is not None
            current.append(command)
        if current is not None and any(c.tag=='curveto' for c in current):yield current


def main():
    extract_jigsaw.OUT=OUT;tree=extract_jigsaw.trace(440);grids=[]
    for text in tree.iter('fill_text'):
        for span in text:
            size=abs(float(span.get('trm').split()[0]))
            if not ((len(span)==36 and 6.9<size<7.1) or (len(span)==25 and 3.9<size<4.1) or (len(span)==81 and 3.5<size<3.7)):continue
            glyphs=[]
            for g in span:
                x,y=transform(text,float(g.get('x')),float(g.get('y')))
                glyphs.append(dict(letter=g.get('unicode'),x=x,y=y,width=size*float(g.get('adv')),size=size))
            n=round(len(glyphs)**.5);by_y=defaultdict(list)
            baselines=sorted({round(g['y'],3) for g in glyphs if g['letter']!='.'})
            assert len(baselines)==n
            for g in glyphs:
                # The unused-cell dot is vertically raised by the typesetter.
                baseline=min(baselines,key=lambda y:abs(g['y']-y))
                assert abs(g['y']-baseline)<.3*size
                g['source_y']=g['y'];g['y']=baseline
                by_y[baseline].append(g)
            assert len(by_y)==n and all(len(row)==n for row in by_y.values())
            flat=[g for y,row in sorted(by_y.items()) for g in sorted(row,key=lambda g:g['x'])]
            grids.append(dict(n=n,board=''.join(g['letter'] for g in flat),glyphs=flat,ovals=[]))
    assert [g['n'] for g in grids]==[6]*5+[5]*2+[9]
    for path in curved_subpaths(tree):
        poly=polygon(path);found=[]
        for gi,grid in enumerate(grids):
            hits=[]
            for offset in [.28,.30,.32]:
                cells=frozenset(i for i,g in enumerate(grid['glyphs'])
                     if inside(g['x']+g['width']/2,g['y']-offset*g['size'],poly))
                hits.append(cells)
            assert len(set(hits))==1,(gi,hits)
            if hits[0]:found.append((gi,hits[0]))
        assert len(found)==1,found
        gi,cells=found[0];grids[gi]['ovals'].append(sorted(cells))
    for gi,grid in enumerate(grids):
        label='words105' if gi<5 else 'words106' if gi<7 else 'words107-eleven'
        decoded=json.loads((OUT/(label+'-decoded.json')).read_text())
        places=placements(decoded['words'],grid['n'],False)
        matches=[]
        for cells in grid['ovals']:
            options=[k for k,p in enumerate(places) if set(c for c,l in p['letters'])==set(cells)
                     and all(grid['board'][c]==l for c,l in p['letters'])]
            assert len(options)==1,(gi,cells,options)
            matches.extend(options)
        assert len(matches)==len(decoded['words'])*decoded['copies']
        assert Counter(places[k]['word'] for k in matches)==Counter({i:decoded['copies'] for i in range(len(decoded['words']))})
        assert any(m['chosen']==sorted(matches) and m['board']==grid['board'] for m in decoded['models']),(gi,grid['board'])
        grid['placement_indices']=sorted(matches);grid['words']=[decoded['words'][places[k]['word']] for k in matches]
        del grid['glyphs']
    save(OUT/'figures-checked.json',dict(script_sha256=sha(__file__),trace_sha256=sha(OUT/'page440-trace.xml'),
         glyphs=sum(g['n']**2 for g in grids),ovals=sum(len(g['ovals']) for g in grids),grids=grids,
         method='Original PDF vector glyphs and Bezier outlines, independently read; cell membership stable at three glyph-center heights. Every printed placement matches an exhaustively enumerated model.'))
    print('Original PDF:',sum(g['n']**2 for g in grids),'glyphs;',sum(len(g['ovals']) for g in grids),'ovals; all8 grids exact.')


if __name__=='__main__':main()
