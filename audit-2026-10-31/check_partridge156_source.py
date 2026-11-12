"""Check new local symmetry claims and printed glyphs; never enumerate tilings."""
from collections import Counter
from datetime import datetime, timezone
from itertools import permutations
from pathlib import Path
import json
import xml.etree.ElementTree as ET
from extract_jigsaw import transform
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/partridge156'
LEFT = (0, 1, 2, 3)
RIGHT = (1, 2, 3, 0)


def read(path):
    return json.loads((ROOT / path).read_text())


def glyphs(path, bounds):
    lines = []
    x0, x1, y0, y1 = bounds
    for element in ET.parse(ROOT / path).getroot().find('page'):
        if element.tag != 'stroke_path':
            continue
        points = [transform(element, float(t.get('x')), float(t.get('y')))
                  for t in element if t.get('x') is not None]
        if points and all(x0 < x < x1 and y0 < y < y1 for x, y in points):
            assert len(points) == 2
            lines.append(points)
    assert len(lines) == 8
    lines.sort(key=lambda line: min(p[0] for p in line))
    result = []
    for group in [lines[:4], lines[4:]]:
        xx = min(p[0] for line in group for p in line)
        yy = min(p[1] for line in group for p in line)
        unit = (max(p[0] for line in group for p in line)-xx)/3
        normalized = []
        for line in group:
            pair = []
            for x, y in line:
                coords = ((x-xx)/unit, (y-yy)/unit)
                assert all(abs(v-round(v)) < .002 for v in coords)
                pair.append(tuple(round(v) for v in coords))
            normalized.append(tuple(sorted(pair)))
        result.append(tuple(sorted(normalized)))
    expected_left = tuple(sorted([((0, 1), (2, 1)), ((2, 0), (2, 2)), ((1, 2), (3, 2)), ((1, 1), (1, 3))]))
    expected_right = tuple(sorted(tuple(sorted((3-x, y) for x, y in line)) for line in expected_left))
    assert result == [expected_left, expected_right]
    return result


def context(tiles):
    r, c, _ = next(t for t in tiles if t[2] == 1)
    assert 0 < r < 35 and 0 < c < 35
    def owner(a, b):
        found = [i for i, (s, t, k) in enumerate(tiles) if s <= a < s+k and t <= b < t+k]
        assert len(found) == 1
        return found[0]
    sides = [owner(r-1, c), owner(r, c+1), owner(r+1, c), owner(r, c-1)]
    corners = [owner(r-1, c-1), owner(r-1, c+1), owner(r+1, c+1), owner(r+1, c-1)]
    assert len(set(sides)) == len(set(corners)) == 4 and set(sides) == set(corners)
    signature = tuple(corners.index(side) for side in sides)
    assert signature in [LEFT, RIGHT]
    return r, c, signature


def main():
    old_paths = ['partridge.cpp', 'check_partridge.py', 'results/partridge/ordinary8-wedge.json',
                 'results/partridge/ordinary8-wedge.verified.json', 'results/partridge/ordinary8-wedge.models.jsonl',
                 'results/partridge/ordinary8-mcc-dimensions.json', 'sources/knuth-programs/dlx3.w']
    old_hashes = {p: sha(ROOT / p) for p in old_paths}
    old, verified = read(old_paths[2]), read(old_paths[3])
    assert old['solutions'] == verified['models'] == 2566
    assert old['symmetry_classes'] == verified['symmetry_classes'] == 2332
    assert verified['unit_on_antidiagonal'] == 468 and verified['orbit_sizes'] == {'8': 2566}
    assert verified['all_unrestricted_solutions'] == 18656
    # A local four-cycle has exactly two perfect corner assignments.
    allowed = [(3, 0), (0, 1), (1, 2), (2, 3)]
    assignments = [p for p in permutations(range(4)) if all(p[i] in allowed[i] for i in range(4))]
    # Enumerated above are side assignments shifted once around the cycle.
    assert set(assignments) == {(3, 0, 1, 2), LEFT}
    orientation_counts = Counter()
    diagonal = {}
    total = 0
    for line in (ROOT / old_paths[4]).read_text().splitlines():
        tiles = tuple(sorted(map(tuple, json.loads(line)['tiles'])))
        r, c, orientation = context(tiles)
        assert r < 18 and c >= 35-r
        total += 1
        if r+c == 35:
            diagonal[tiles] = orientation
            orientation_counts['left' if orientation == LEFT else 'right'] += 1
    assert total == 2566 and len(diagonal) == 468
    assert orientation_counts == dict(left=234, right=234)
    for tiles, orientation in diagonal.items():
        reflected = tuple(sorted((36-c-k, 36-r-k, k) for r, c, k in tiles))
        assert reflected != tiles and diagonal[reflected] != orientation
    assert total-len(diagonal)//2 == 2332
    paths = {'original': 'results/path153/original-480.xml', 'draft': 'results/path153/draft-170.xml'}
    decoded = {'original': glyphs(paths['original'], (290, 326, 419, 435)),
               'draft': glyphs(paths['draft'], (300, 335, 525, 547))}
    assert decoded['original'] == decoded['draft']
    # Direct closed formulas for the MCC matrix, not a new input/solver run.
    sizes = {k: (37-k)**2 if k > 1 else sum(range(1, 19)) for k in range(1, 9)}
    items = 36*36+8
    options = sum(sizes.values())
    occurrences = sum(n*(k*k+1) for k, n in sizes.items())
    assert (items, options, occurrences, occurrences+options) == (1304, 7367, 198386, 205753)
    assert sizes[8] == 841 and 8*8+1 == 65
    costs_ratio = 490600/235
    assert costs_ratio > 2000
    save(OUT / 'source-claims-checked.json', dict(at_utc=datetime.now(timezone.utc).isoformat(),
        checker_sha256=sha(__file__), dependencies={'extract_jigsaw.py': sha(ROOT / 'extract_jigsaw.py')},
        accepted_prior_hashes=old_hashes, source_trace_hashes={p: sha(ROOT / p) for p in paths.values()},
        glyph_segments=decoded, all2566_unit_contexts_match=True, diagonal_context_counts=dict(orientation_counts),
        antidiagonal_reflection_pairs=234, selected_one_per_orbit=2332, accepted_raw_count=18656,
        mcc=dict(items=items, options=options, item_occurrences=occurrences, entries_including_spacers=occurrences+options,
                 options_by_size=sizes, max_square_option_items=65),
        board_bytes=36*8, published_cost_ratio_arithmetic=costs_ratio,
        ratio_caveat='Arithmetic only; original historical costs and runtime not independently reproduced.',
        new_searches=0, completed_census_not_restarted=True))
    print('PASS156: two original context glyphs agree with draft;468 diagonal models form234 reflected pairs. MCC dimensions correct; no search.')


if __name__ == '__main__':
    main()
