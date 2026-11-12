"""Decode all16 printed snake boards; validate witnesses, without a census."""
from collections import defaultdict, Counter
from datetime import datetime, timezone
from pathlib import Path
import json
import xml.etree.ElementTree as ET
from extract_chain150 import paths
from extract_jigsaw import transform
from verify_chess_snakes import adjacency, orbit, classify
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/snakes172'
MAP = {'0': 'king', '2': 'knight', '3': 'bishop', '4': 'rook', '5': 'queen',
       'k': 'king', 'n': 'knight', 'b': 'bishop', 'r': 'rook', 'q': 'queen'}


def decode(path, question):
    _, segments = paths(path)
    horizontal, vertical = defaultdict(list), []
    for s in segments:
        if len(s['points']) != 2:
            continue
        (x, y), (a, b) = s['points']
        if abs(y-b) < .001 and 25 < abs(x-a) < 70:
            horizontal[round(min(x, a), 3), round(max(x, a), 3)].append(y)
        if abs(x-a) < .001 and 25 < abs(y-b) < 70:
            vertical.append((x, min(y, b), max(y, b)))
    glyphs = []
    for t in ET.parse(path).getroot().find('page'):
        if t.tag == 'fill_text':
            for s in t:
                if not 45 < float(s.get('trm').split()[0]) < 50:
                    continue
                for g in s:
                    key = g.get('glyph') if g.get('unicode') == '\ufffd' else g.get('unicode')
                    glyphs.append((*transform(t, float(g.get('x')), float(g.get('y'))), MAP[key]))
    boards = []
    n = 4 if question else 8
    used = set()
    for (x0, x1), ys in horizontal.items():
        yy = sorted(ys)
        assert len(yy) % (n+1) == 0
        for lo in range(0, len(yy), n+1):
            lines = yy[lo:lo+n+1]
            y0, y1 = lines[0], lines[-1]
            unit = (x1-x0)/n
            assert all(abs((y-y0)/unit-i) < .005 for i, y in enumerate(lines))
            xx = sorted(x for x, a, b in vertical if abs(a-y0) < .02 and abs(b-y1) < .02 and x0-.02 <= x <= x1+.02)
            assert len(xx) == n+1 and all(abs((x-x0)/unit-i) < .005 for i, x in enumerate(xx))
            cells, pieces = [], set()
            for k, (x, y, piece) in enumerate(glyphs):
                if x0-.1 <= x <= x1+.1 and y0-.1 <= y <= y1+.1:
                    c, bottom = (x-x0)/unit, (y-y0)/unit
                    assert abs(c-round(c)) < .1 and abs(bottom-round(bottom)) < .1
                    r, c = round(bottom)-1, round(c)
                    assert 0 <= r < n and 0 <= c < n and k not in used
                    used.add(k); cells.append((r, c)); pieces.add(piece)
            assert len(pieces) == 1 and len(cells) == len(set(cells))
            boards.append(dict(n=n, piece=pieces.pop(), cells=sorted(cells), source_bounds=[x0, x1, y0, y1]))
    assert used == set(range(len(glyphs)))
    return sorted(boards, key=lambda q: (round(q['source_bounds'][2]), q['source_bounds'][0]))


def main():
    assert not (OUT / 'source-checked.json').exists()
    traces = {version: [f'results/snakes172/{version}-{page}.xml' for page in pages]
              for version, pages in [('original', [165, 484, 485]), ('draft', [87, 174, 175])]}
    versions = {v: [q for i, p in enumerate(pp) for q in decode(ROOT / p, i == 0)] for v, pp in traces.items()}
    assert len(versions['original']) == len(versions['draft']) == 16
    for a, b in zip(versions['original'], versions['draft']):
        assert {k: v for k, v in a.items() if k != 'source_bounds'} == {k: v for k, v in b.items() if k != 'source_bounds'}
    figures = versions['original']
    assert sum(len(q['cells']) for q in figures) == 305
    expected = [('king', 7, None), ('king', 32, 'path'), ('knight', 32, 'path'),
                ('bishop', 13, 'path'), ('rook', 15, 'path'), ('queen', 12, 'path'),
                ('knight', 34, 'path'), ('rook', 15, 'path'), ('rook', 15, 'path'),
                ('queen', 13, 'path'), ('queen', 13, 'path'), ('king', 31, 'cycle'),
                ('knight', 32, 'cycle'), ('bishop', 12, 'cycle'), ('rook', 16, 'cycle'), ('queen', 13, 'cycle')]
    archives = set()
    for i, (q, (piece, count, kind)) in enumerate(zip(figures, expected)):
        assert q['piece'] == piece and len(q['cells']) == count
        n = q['n']; mask = sum(1 << (r*n+c) for r, c in q['cells']); adj = adjacency(n, piece)
        assert classify(mask, adj) == kind
        q.update(kind=kind, mask=mask, orbit_size=len(orbit(mask, n)),
                 degrees=dict(Counter((adj[v]&mask).bit_count() for v in range(n*n) if mask >> v & 1)))
        if i == 0:
            removable = [v for v in [0, 3, 12, 15] if mask >> v & 1 and classify(mask ^ (1 << v), adj) == 'path']
            assert len(removable) == 1
            q['corner_to_remove'] = divmod(removable[0], n)
        elif piece != 'rook':
            start = 0 if i <= 5 else -1
            archive = f'results/chess_snakes/{piece}-{kind}-{count}-start{start}.jsonl'
            rows = [json.loads(line) for line in (ROOT / archive).read_text().splitlines()]
            matches = [j+1 for j, (_, _, m) in enumerate(rows) if min(orbit(m, n)) == min(orbit(mask, n))]
            assert matches, (i, archive)
            q['accepted_archive'] = archive; q['matching_archive_lines'] = matches
            archives.add(archive)
        if i == 1:
            endpoints = [v for v in range(64) if mask >> v & 1 and (adj[v]&mask).bit_count() == 1]
            assert len(endpoints) == 2 and set(endpoints) <= {0, 7, 56, 63}
        if i == 5:
            # The text says "occupies opposite corners", not that both are ends.
            assert mask & 1 and mask >> 63 & 1 and (adj[0]&mask).bit_count() == 1
        if i == 12:
            assert {(7-r, 7-c) for r, c in q['cells']} == set(q['cells'])
        if i == 14:
            cells = set(q['cells'])
            assert cells == {(c, r) for r, c in cells} == {(7-c, 7-r) for r, c in cells}
            assert cells != {(7-r, c) for r, c in cells} and cells != {(r, 7-c) for r, c in cells}
    assert min(orbit(figures[9]['mask'], 8)) != min(orbit(figures[10]['mask'], 8))
    old = ['CHESS_SNAKES_NOTES.md', 'chess_snakes.cpp', 'verify_chess_snakes.py',
           'rook_snakes.cpp', 'verify_rook_symmetry.py']
    old += [str(p.relative_to(ROOT)) for p in sorted((ROOT / 'results/chess_snakes').glob('*')) if p.is_file()]
    save(OUT / 'source-checked.json', dict(at_utc=datetime.now(timezone.utc).isoformat(), checker_sha256=sha(__file__),
        dependency_hashes={p: sha(ROOT / p) for p in ['extract_chain150.py', 'extract_jigsaw.py', 'verify_chess_snakes.py']},
        trace_hashes={p: sha(ROOT / p) for pp in traces.values() for p in pp},
        original_draft_equal=True, figures_per_version=16, pieces_per_version=305,
        figures=figures, draft_bounds=[q['source_bounds'] for q in versions['draft']],
        accepted_prior_hashes={p: sha(ROOT / p) for p in old}, new_placement_searches=0))
    print('PASS172:16 boards and305 pieces per version;15 valid snakes, one corrected by removing its corner. All original/draft boards agree. No new search.')


if __name__ == '__main__':
    main()
