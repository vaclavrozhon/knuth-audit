"""Read all four printed nested-queen boards without any new placement search."""
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import json
import xml.etree.ElementTree as ET
from extract_chain150 import paths, points
from extract_jigsaw import transform
from check_nested_queens import valid, occurrences
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/nested162'


def decode(path, question):
    _, segments = paths(path)
    h, v = defaultdict(list), []
    for s in segments:
        if len(s['points']) != 2:
            continue
        (x, y), (a, b) = s['points']
        if abs(y-b) < .001 and abs(x-a) > 60:
            h[round(min(x, a), 2), round(max(x, a), 2)].append(y)
        if abs(x-a) < .001 and abs(y-b) > 60:
            v.append((x, min(y, b), max(y, b)))
    h = {key: sorted(val) for key, val in h.items() if len(val) >= 15}
    assert len(h) == (1 if question else 3)
    glyphs, shades = [], []
    for t in ET.parse(path).getroot().find('page'):
        if t.tag == 'fill_text':
            for span in t:
                if not 30 < float(span.get('trm').split()[0]) < 31:
                    continue
                for g in span:
                    assert g.get('unicode') in ['Q', '\ufffd']
                    glyphs.append(transform(t, float(g.get('x')), float(g.get('y'))))
        if t.tag == 'fill_path':
            color = [float(c) for c in t.get('color').split()]
            if len(color) == 3 and all(abs(a-b) < .002 for a, b in zip(color, [.85, .85, 1])):
                ps = [p for q in t for p in points(t, q)]
                xs, ys = sorted({round(x, 3) for x, y in ps}), sorted({round(y, 3) for x, y in ps})
                assert len(ps) == 4 and len(xs) == len(ys) == 2
                shades.append([xs[0], xs[-1], ys[0], ys[-1]])
    assert len(glyphs) == (17 if question else 66)
    result = []
    for (x0, x1), yy in sorted(h.items()):
        n, y0, y1 = len(yy)-1, yy[0], yy[-1]
        unit = (x1-x0)/n
        assert all(abs((y-y0)/unit-i) < .005 for i, y in enumerate(yy))
        xx = sorted(x for x, a, b in v if abs(a-y0) < .02 and abs(b-y1) < .02 and x0-.02 <= x <= x1+.02)
        assert len(xx) == n+1
        assert all(abs((x-x0)/unit-i) < .005 for i, x in enumerate(xx))
        q = []
        for x, y in glyphs:
            if x0-.15 < x < x1+.15:
                c, bottom = (x-x0)/unit, (y-y0)/unit
                # The original PDF baselines drift by up to0.081 cell; still far
                # from the half-cell boundary. Draft offsets stay below0.032.
                assert abs(c-round(c)) < .04 and abs(bottom-round(bottom)) < .1, (str(path), n, x, y, c, bottom)
                r, c = round(bottom)-1, round(c)
                assert 0 <= r < n and 0 <= c < n
                q.append((r, c))
        assert len(q) == n and valid(q)
        p = tuple(c for r, c in sorted(q))
        blue = []
        for a, b, c, d in shades:
            if x0-.02 <= a < b <= x1+.02 and y0-.02 <= c < d <= y1+.02:
                coords = [(c-y0)/unit, (a-x0)/unit, (b-a)/unit, (d-c)/unit]
                assert all(abs(z-round(z)) < .005 for z in coords)
                r, col, k, height = map(round, coords)
                assert k == height and (r, col) in occurrences(p, k)
                blue.append((r, col, k))
        result.append(dict(n=n, columns=list(p), shaded_blocks=sorted(blue),
            all_blocks={str(k): occurrences(p, k) for k in [4, 5, 6]}, source_bounds=[x0, x1, y0, y1]))
    return result


def main():
    assert not (OUT / 'source-checked.json').exists()
    traces = dict(original_question='results/nested162/original-165.xml', original_answer='results/nested162/original-482.xml',
        draft_question='results/nested162/draft-87.xml', draft_answer='results/nested162/draft-172.xml')
    figures = {key: decode(ROOT / path, key.endswith('question')) for key, path in traces.items()}
    for kind in ['question', 'answer']:
        for a, b in zip(figures['original_'+kind], figures['draft_'+kind]):
            assert {k: v for k, v in a.items() if k != 'source_bounds'} == {k: v for k, v in b.items() if k != 'source_bounds'}
    question = figures['original_question'][0]
    assert question['n'] == 17 and len(question['shaded_blocks']) == 2
    assert sorted(k for r, c, k in question['shaded_blocks']) == [4, 5]
    answers = figures['original_answer']
    assert [r['n'] for r in answers] == [22, 19, 25]
    for figure, (k, t) in zip(answers, [(4, 5), (5, 3), (6, 3)]):
        assert len(figure['shaded_blocks']) == t
        assert all(block[2] == k for block in figure['shaded_blocks'])
        archive = ROOT / f'results/nested_queens/independent-n{figure["n"]}-q{k}-t{t}.jsonl'
        members = [json.loads(line) for line in archive.read_text().splitlines()]
        assert figure['columns'] in members
        figure['accepted_archive'] = str(archive.relative_to(ROOT))
        figure['archive_line'] = members.index(figure['columns'])+1
    assert len(answers[-1]['all_blocks']['5']) == 1
    assert not any(k == 5 for r, c, k in answers[-1]['shaded_blocks'])
    # Additional claim162(a): obtain a witness from an accepted archive, not a search.
    members = [tuple(json.loads(line)) for line in (ROOT / 'results/nested_queens/independent-n15-q4-t2.jsonl').read_text().splitlines()]
    disjoint = []
    for p in members:
        for r, c in occurrences(p, 4):
            for s, t in occurrences(p, 5):
                if (r+4 <= s or s+5 <= r) and (c+4 <= t or t+5 <= c):
                    disjoint.append(dict(columns=p, Q4=[r, c], Q5=[s, t]))
    assert disjoint
    # Accept the already complete comparison, including its two native first-witness cases.
    native = json.loads((ROOT / 'results/nested_queens/suite.json').read_text())
    independent = json.loads((ROOT / 'results/nested_queens/independent-suite.json').read_text())
    assert len(native) == len(independent) == 51
    for a, b in zip(native, independent):
        assert all(a[k] == b[k] for k in ['n', 'k', 't'])
        assert b['matches_dlx3']
        if a['solutions'] == 0:
            assert a['complete'] and b['distinct_models'] == 0 and b['complete']
    minima = [(4, 2, 15), (4, 3, 17), (4, 4, 17), (4, 5, 22), (5, 2, 16), (5, 3, 19), (5, 4, 20), (6, 2, 22), (6, 3, 25)]
    assert {(d['n'], d['k'], d['t']) for d in native} == {(n, k, t) for k, t, m in minima for n in range(k*t, m+1)}
    old = ['NESTED_QUEENS_NOTES.md', 'check_nested_queens.py', 'verify_nested_queens.py', 'nested_queens.cpp']
    old += [str(p.relative_to(ROOT)) for p in sorted((ROOT / 'results/nested_queens').glob('*')) if p.is_file()]
    save(OUT / 'source-checked.json', dict(at_utc=datetime.now(timezone.utc).isoformat(), checker_sha256=sha(__file__),
        dependencies={p: sha(ROOT / p) for p in ['extract_chain150.py', 'extract_jigsaw.py', 'check_nested_queens.py']},
        traces={p: sha(ROOT / p) for p in traces.values()}, figures=figures,
        original_draft_equal=True, all83_queens_per_version_checked=True,
        all13_shaded_blocks_per_version_checked=True, missing_Q5_shading_confirmed=answers[-1]['all_blocks']['5'],
        printed_answer_witnesses_in_accepted_archives=True, disjoint_Q4_Q5_on_Q15_witness=disjoint[0],
        all51_prior_ranges_complete=True, accepted_prior_hashes={p: sha(ROOT / p) for p in old}, new_placement_searches=0))
    print('PASS162: four boards,83 queens,13 shaded blocks per version. All answer witnesses archived; known Q5 shading omission confirmed. No search.')


if __name__ == '__main__':
    main()
