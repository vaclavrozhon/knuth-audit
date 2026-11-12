"""Decode chess sudoku figures directly from PDF vector traces (no search)."""
from collections import defaultdict
from pathlib import Path
import json
import math
import xml.etree.ElementTree as ET
from extract_chain150 import paths
from extract_jigsaw import transform
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/chess173_174'


def decode(path):
    _, segments = paths(path)
    horizontal = defaultdict(set)
    vertical = []
    for s in segments:
        if len(s['points']) != 2:
            continue
        (x, y), (a, b) = s['points']
        if abs(y-b) < .001 and 35 < abs(x-a) < 100:
            horizontal[round(min(x, a), 3), round(max(x, a), 3)].add(round(y, 3))
        if abs(x-a) < .001 and 35 < abs(y-b) < 100:
            vertical.append((x, min(y, b), max(y, b)))
    glyphs = []
    for text in ET.parse(path).getroot().find('page'):
        if text.tag != 'fill_text':
            continue
        for span in text:
            for g in span:
                ch = g.get('unicode', '')
                if ch == '\ufffd' and float(span.get('trm').split()[0]) > 20:
                    ch = {'0': 'n', '2': 'b'}.get(g.get('glyph'), '')
                if ch in ('n', 'b') or ch.isdigit():
                    glyphs.append((*transform(text, float(g.get('x')), float(g.get('y'))), ch))
    boards = []
    used = set()
    for (x0, x1), yy in horizontal.items():
        yy = sorted(yy)
        unit = (x1-x0)/9
        for lo in range(len(yy)-9):
            lines = yy[lo:lo+10]
            y0, y1 = lines[0], lines[-1]
            if not all(abs((y-y0)/unit-i) < .005 for i, y in enumerate(lines)):
                continue
            xx = sorted({round(x, 3) for x, a, b in vertical
                         if abs(a-y0) < .02 and abs(b-y1) < .02 and x0-.02 <= x <= x1+.02})
            if len(xx) != 10 or not all(abs((x-x0)/unit-i) < .005 for i, x in enumerate(xx)):
                continue
            pieces, labels, ids = {}, defaultdict(list), []
            for k, (x, y, ch) in enumerate(glyphs):
                if not x0-.06*unit <= x < x1-.06*unit or not y0+.06*unit < y <= y1+.06*unit:
                    continue
                if ch in ('n', 'b'):
                    c, bottom = (x-x0)/unit, (y-y0)/unit
                    if max(abs(c-round(c)), abs(bottom-round(bottom))) >= .05:
                        continue  # Ordinary prose outside the board is not a piece.
                    cell = (round(bottom)-1, round(c))
                    assert cell not in pieces
                    pieces[cell] = {'n': 'knight', 'b': 'bishop'}[ch]
                    ids.append(k)
                else:
                    cell = (math.floor((y-y0)/unit), math.floor((x-x0)/unit))
                    labels[cell].append((x, ch))
            if not pieces:
                continue  # Non-chess grids in Appendix E.
            assert len(set(pieces.values())) == 1
            assert not used.intersection(ids)
            used.update(ids)
            assert all(0 <= r < 9 and 0 <= c < 9 for r, c in pieces)
            assert not labels or set(labels) == set(pieces), (path, x0, y0, pieces, labels)
            clues = [[r, c, int(''.join(ch for _, ch in sorted(labels[r, c])))]
                     for r, c in sorted(labels)]
            boards.append(dict(piece=next(iter(pieces.values())), cells=sorted(pieces), clues=clues,
                               source_bounds=[x0, x1, y0, y1]))
    return sorted(boards, key=lambda b: (round(b['source_bounds'][2]), b['source_bounds'][0]))


def main():
    names = ['original-166', 'draft-88', 'original-486', 'draft-176',
             'original-691', 'draft-259', 'errata-14', 'errata-23', 'fascicle-errata-7']
    result = {n: decode(OUT / (n+'.xml')) for n in names}
    for name, boards in result.items():
        print(name, len(boards), sum(len(b['cells']) for b in boards),
              [(b['piece'], len(b['cells']), sorted({c[2] for c in b['clues']})) for b in boards])
    assert [len(result[n]) for n in names] == [8, 8, 20, 20, 24, 24, 16, 20, 1]
    assert all(len(b['cells']) == 27 for n in ['original-691', 'draft-259', 'errata-23'] for b in result[n])
    save(OUT / 'figures.json', dict(extractor_sha256=sha(__file__),
        dependency_hashes={n: sha(ROOT/n) for n in ['extract_chain150.py', 'extract_jigsaw.py']},
        trace_hashes={n+'.xml': sha(OUT/(n+'.xml')) for n in names}, figures=result))


if __name__ == '__main__':
    main()
