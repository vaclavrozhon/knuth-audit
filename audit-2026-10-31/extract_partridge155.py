"""Decode four printed square packings and labels, without a packing search."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import json
import xml.etree.ElementTree as ET
from extract_chain150 import paths
from extract_jigsaw import transform
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/partridge155'


def glyphs(path):
    result = []
    for text in ET.parse(path).getroot().find('page'):
        if text.tag != 'fill_text':
            continue
        for span in text:
            for g in span:
                x, y = transform(text, float(g.get('x')), float(g.get('y')))
                result.append((g.get('unicode'), x, y))
    return result


def integral(x):
    n = round(x)
    assert abs(x-n) < .002, x
    return n


def check(side, tiles, counts):
    assert Counter(k for r, c, k in tiles) == Counter(counts)
    cells = {}
    for index, (r, c, k) in enumerate(tiles):
        assert 0 <= r <= side-k and 0 <= c <= side-k
        for i in range(r, r+k):
            for j in range(c, c+k):
                assert (i, j) not in cells
                cells[i, j] = index, k
    assert len(cells) == side*side
    by_cells = sum(cells[r, c][1] == cells[s, t][1] and cells[r, c][0] != cells[s, t][0]
                   for r, c in cells for s, t in [(r+1, c), (r, c+1)] if (s, t) in cells)
    by_rectangles = 0
    for index, (r, c, k) in enumerate(tiles):
        for s, t, m in tiles[:index]:
            if k != m:
                continue
            if r+k == s or s+m == r:
                by_rectangles += max(0, min(c+k, t+m)-max(c, t))
            if c+k == t or t+m == c:
                by_rectangles += max(0, min(r+k, s+m)-max(r, s))
    assert by_cells == by_rectangles
    return dict(side=side, tiles=tiles, inventory=dict(Counter(k for r, c, k in tiles)),
                area=len(cells), affinity_by_unit_edges=by_cells, affinity_by_shared_lengths=by_rectangles)


def decode(path, side, counts):
    rects, _ = paths(path)
    frames = sorted([r for r in rects if r[1]-r[0] > 40])
    assert len(frames) == 2
    letters = glyphs(path)
    result = []
    for frame in frames:
        x0, x1, y0, y1 = frame
        assert abs(x1-x0-(y1-y0)) < .005
        unit = (x1-x0)/side
        pieces = [r for r in rects if r != frame and r[0] >= x0-.005 and r[1] <= x1+.005
                  and r[2] >= y0-.005 and r[3] <= y1+.005]
        assert len(pieces) == sum(counts.values())
        tiles = []
        labels = []
        for a, b, c, d in pieces:
            r, col, k, m = [integral(t/unit) for t in [c-y0, a-x0, b-a, d-c]]
            assert k == m
            gs = [(g, x, y) for g, x, y in letters if a < x < b and c < y < d]
            assert len(gs) == 1 and gs[0][0] == str(k), (path, frame, (a, b, c, d), gs)
            tiles.append((r, col, k))
            labels.append(gs[0][0])
        assert len([g for g, x, y in letters if x0 < x < x1 and y0 < y < y1]) == len(labels)
        report = check(side, sorted(tiles), counts)
        report.update(source_bounds=frame, labels_checked=len(labels))
        result.append(report)
    return result


def main():
    traces = dict(original_main='results/partridge155/original-112.xml', draft_main='results/partridge155/draft-34.xml',
                  original_answer='results/path153/original-480.xml', draft_answer='results/path153/draft-170.xml')
    decoded = {}
    for key, path in traces.items():
        main = key.endswith('main')
        decoded[key] = decode(ROOT/path, 36 if main else 14, {k: k if main else 7-k for k in range(1, 9 if main else 7)})
        expected = [165, 67] if main else [35, 5]
        assert [r['affinity_by_unit_edges'] for r in decoded[key]] == expected
    for part in ['main', 'answer']:
        for a, b in zip(decoded['original_'+part], decoded['draft_'+part]):
            for key in a:
                if key != 'source_bounds':
                    assert a[key] == b[key], (part, key)
    # Match only the two new printed witnesses against already accepted saved models.
    targets = {tuple(map(tuple, r['tiles'])): str(r['affinity_by_unit_edges']) for r in decoded['original_answer']}
    matches = {}
    path = ROOT/'results/partridge/authentic6.models.jsonl'
    with path.open() as f:
        for index, line in enumerate(f, 1):
            model = json.loads(line)
            sig = tuple(sorted(map(tuple, model['tiles'])))
            if sig in targets:
                assert model['affinity'] == int(targets[sig])
                matches[targets[sig]] = index
            if len(matches) == 2:
                break
    assert len(matches) == 2
    prior = ['partridge.cpp', 'check_partridge.py', 'results/partridge/authentic6.json',
             'results/partridge/authentic6.verified.json', 'results/partridge/validation.json', str(path.relative_to(ROOT))]
    count = json.loads((ROOT/prior[2]).read_text())
    verified = json.loads((ROOT/prior[3]).read_text())
    assert count['solutions'] == verified['models'] == 60568 == 8*7571
    assert count['affinity_histogram'] == verified['affinity_histogram']
    assert min(map(int, count['affinity_histogram'])) == 5 and max(map(int, count['affinity_histogram'])) == 35
    assert count['symmetry_classes'] == verified['symmetry_classes'] == 7585
    save(OUT/'figures-checked.json', dict(at_utc=datetime.now(timezone.utc).isoformat(), checker_sha256=sha(__file__),
         dependencies={p: sha(ROOT/p) for p in ['extract_chain150.py', 'extract_jigsaw.py']},
         trace_sha256={p: sha(ROOT/p) for p in traces.values()}, figures=decoded,
         original_draft_equal=True, all114_labels_per_version_checked=True, saved_model_line_matches=matches,
         accepted_prior_hashes={p: sha(ROOT/p) for p in prior}, accepted_count=60568, accepted_symmetry_classes=7585,
         new_solver_calls=0, old_complete_census_not_restarted=True))
    print('PASS: four printed packings and114 labels in each version; scores165/67/35/5; both extremal figures in old60568 models.')


if __name__ == '__main__':
    main()
