"""Decode figure (65) directly; retain the earlier complete queen censuses."""
from collections import defaultdict
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
import json
import xml.etree.ElementTree as ET
from extract_chain150 import paths
from extract_jigsaw import transform
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/queens159_161'


def decode(path):
    _, segments = paths(path)
    horizontal = defaultdict(list)
    vertical = []
    for segment in segments:
        if len(segment['points']) != 2:
            continue
        (x, y), (u, v) = segment['points']
        if abs(y-v) < .001 and 63 < abs(x-u) < 65:
            horizontal[round(min(x, u), 2), round(max(x, u), 2)].append(y)
        if abs(x-u) < .001 and 63 < abs(y-v) < 65:
            vertical.append((x, min(y, v), max(y, v)))
    assert len(horizontal) == 4 and len(vertical) == 36
    glyphs = []
    for text in ET.parse(path).getroot().iter('fill_text'):
        for span in text:
            if abs(float(span.get('trm').split()[0])-51.1512) > .001:
                continue
            for g in span:
                assert g.get('unicode') in ['Q', '\ufffd']
                glyphs.append(transform(text, float(g.get('x')), float(g.get('y'))))
    assert len(glyphs) == 20
    result = []
    for (x0, x1), yy in sorted(horizontal.items()):
        yy.sort()
        assert len(yy) == 9
        y0, y1 = yy[0], yy[-1]
        unit = (x1-x0)/8
        assert all(abs((y-y0)/unit-i) < .003 for i, y in enumerate(yy))
        xx = sorted(x for x, a, b in vertical if abs(a-y0) < .01 and abs(b-y1) < .01 and x0-.01 <= x <= x1+.01)
        assert len(xx) == 9
        assert all(abs((x-x0)/unit-i) < .003 for i, x in enumerate(xx))
        queens, origins = [], []
        for x, y in glyphs:
            if not x0-.1 < x < x1+.1:
                continue
            # The chess font origin is at the lower left of its occupied cell.
            c, bottom = (x-x0)/unit, (y-y0)/unit
            assert abs(c-round(c)) < .04 and abs(bottom-round(bottom)) < .04
            r, c = round(bottom)-1, round(c)
            assert 0 <= r < 8 and 0 <= c < 8
            queens.append((r, c))
            origins.append((x, y))
        assert len(queens) == len(set(queens)) == 5
        result.append(dict(bounds=[x0, x1, y0, y1], queens=sorted(queens), glyph_origins=origins))
    return result


def attacks(a, b):
    r, c = a
    s, t = b
    return r == s or c == t or abs(r-s) == abs(c-t)


def main():
    assert not (OUT / 'source-checked.json').exists()
    traces = {'original': 'results/queens159_161/original-114.xml', 'draft': 'results/queens159_161/draft-36.xml'}
    figures = {key: decode(ROOT / p) for key, p in traces.items()}
    original, draft = [[r['queens'] for r in figures[key]] for key in ['original', 'draft']]
    assert original == draft
    prior = json.loads((ROOT / 'results/queen_domination/main-text.json').read_text())
    assert [[list(q) for q in f] for f in original] == prior['fig65']
    for f in original:
        assert all(any(attacks(q, (r, c)) for q in f) for r in range(8) for c in range(8))
    assert all(any(p != q and attacks(p, q) for p in original[2]) for q in original[2])
    assert all(not attacks(p, q) for p, q in combinations(original[3], 2))
    direct = json.loads((ROOT / 'results/queen_domination/components-direct.json').read_text())['last_printed_diagram']
    assert [list(q) for q in original[3]] == direct['seed']
    assert sum(attacks((0, 0), (r, c)) for r in range(8) for c in range(8)) == 22
    assert sum(attacks((1, 7), (r, c)) for r in range(8) for c in range(8) if (r, c) != (0, 0)) == 22
    old = ['QUEEN_DOMINATION_NOTES.md', 'queen_domination.cpp', 'check_queen_domination.py',
           'check_queen_component.py', 'check_queen_text.py']
    old += [str(p.relative_to(ROOT)) for p in sorted((ROOT / 'results/queen_domination').glob('*')) if p.is_file()]
    counts = json.loads((ROOT / 'results/queen_domination/counts.json').read_text())
    classes = ['2012', '2111', '2120', '3002', '3011', '3020', '3110', '4010', '4001', '5000']
    weights = [4, 4, 8, 4, 8, 8, 4, 8, 4, 4]
    values = [counts['quadrants'].get(str(int(c)), 0) for c in classes]
    assert values == [134, 884, 33, 23, 34, 1, 16, 0, 22, 0]
    assert sum(a*b for a, b in zip(weights, values)) == 4860
    costs = [95, 348, 60, 23, 75, 8, 19, 2, 10, 0]
    assert sum(costs) == 640
    hist = json.loads((ROOT / 'results/queen_domination/verified.json').read_text())['graphs'][0]['component_histogram']
    assert sum(hist.values()) == 589 and sum(int(k)*v for k, v in hist.items()) == 4860
    save(OUT / 'source-checked.json', dict(at_utc=datetime.now(timezone.utc).isoformat(), checker_sha256=sha(__file__),
        dependencies={p: sha(ROOT / p) for p in ['extract_chain150.py', 'extract_jigsaw.py']},
        traces={p: sha(ROOT / p) for p in traces.values()}, figures=figures,
        original_draft_equal=True, all20_queens_per_version_checked=True,
        all_four_equal_prior_transcription=True, third_total_dominating=True, fourth_independent=True,
        F067_seed_equals_printed_figure=True, accepted_prior_hashes={p: sha(ROOT / p) for p in old},
        first_two_option_counts=[22, 22], quadrant_counts_accepted=values, quadrant_weights=weights,
        weighted_sum=4860, given_cost_arithmetic_only=dict(total_megamems=640, ratio=13000/640, measured=False),
        component_histogram_accepted=hist, new_censuses=0))
    print('PASS159–161: all20 source queens per version match; third(ii), fourth(i), F067 seed correct. No census.')


if __name__ == '__main__':
    main()
