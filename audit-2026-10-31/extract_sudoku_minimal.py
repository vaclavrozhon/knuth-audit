#!/usr/bin/env python3
"""Positional extraction of the diagrams for DLX51--54, with full glyph evidence."""
from pathlib import Path
import json
import subprocess
import xml.etree.ElementTree as ET
from dlx1_audit_tools import ROOT, sha

OUT = ROOT/'results/sudoku_minimal'
BOOK = ROOT.parent/'books/taocp-vol4b-ed1-print2-2022.pdf'


def words(page):
    OUT.mkdir(exist_ok=True)
    path = OUT/f'page{page}-bbox.html'
    if not path.exists():
        subprocess.run(['pdftotext', '-f', str(page+20), '-l', str(page+20),
                        '-bbox', str(BOOK), str(path)], check=True)
    return [dict(text=w.text, bbox=[float(w.get(k)) for k in
                 ('xMin', 'yMin', 'xMax', 'yMax')])
            for w in ET.parse(path).getroot().iter()
            if w.tag.endswith('word') and w.text]


def grid(page, n, x0, y0, step, alphabet):
    cells = ['.']*(n*n)
    glyphs = []
    for w in words(page):
        x, y = (w['bbox'][0]+w['bbox'][2])/2, w['bbox'][1]
        r, c = round((y-y0)/step), round((x-x0)/step)
        if not (0 <= r < n and 0 <= c < n):
            continue
        if abs(x-x0-c*step) > .04 or abs(y-y0-r*step) > .04:
            continue
        assert len(w['text']) == 1 and w['text'] in alphabet, w
        assert cells[n*r+c] == '.', w
        cells[n*r+c] = w['text']
        glyphs.append(dict(row=r, column=c, **w))
    return dict(page=page, size=n, rows=[''.join(cells[n*r:n*r+n]) for r in range(n)],
                cells=cells, glyphs=glyphs)


def main():
    sources = {
        '51': grid(426, 9, 429.2605, 123.110, 6.721, '12345679'),
        '52': grid(426, 9, 422.5685, 194.271, 7.6185, '123456789'),
        '53A': grid(426, 4, 233.709, 323.429, 6.700, '1234'),
        '53B': grid(426, 4, 305.229, 323.429, 6.700, '1234'),
        '53C': grid(426, 4, 376.629, 323.429, 6.700, 'ABCD'),
        '54': grid(427, 9, 164.4625, 171.171, 8.067, '123456789'),
    }
    top = [181.929, 218.949, 265.209, 302.229, 339.249, 376.209, 413.229]
    bottom = [181.929, 228.189, 265.209, 302.229, 339.249, 376.209, 413.229]
    for row, anchors, y in [('top', top, 387.629), ('bottom', bottom, 422.669)]:
        for c, x in enumerate(anchors):
            sources[f'53-{row}-{c+1}'] = grid(426, 4, x, y, 6.700, 'WXYZ')
    for name, s in sources.items():
        print(name, '/'.join(s['rows']), len(s['glyphs']))
    assert len(sources['54']['glyphs']) == 23
    assert len(sources['53-bottom-1']['glyphs']) == 6
    assert all(len(s['glyphs']) == 4 for name,s in sources.items()
               if name.startswith('53-') and name != '53-bottom-1')
    result = dict(book_sha256=sha(BOOK), source_sha256=sha(__file__), sources=sources)
    (OUT/'pdf-grids.json').write_text(json.dumps(result, indent=2)+'\n')


if __name__ == '__main__':
    main()
