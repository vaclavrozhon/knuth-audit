"""Read all126 original glyphs, including rotated sixes, and verify figure incidences."""
from datetime import datetime, timezone
import math
import xml.etree.ElementTree as ET
import nuts137 as n
from extract_jigsaw import transform


def extract(page):
    trace = n.OUT / f'page{page}-trace.xml'
    tree = ET.parse(trace)
    records = []
    for text in tree.iter('fill_text'):
        if text.get('color') != '1 1 1':
            continue
        glyphs = []
        for span in text:
            a, b, c, d = map(float, span.get('trm').split())
            for g in span:
                ch = g.get('unicode')
                assert ch in '123456'
                x, y, adv = float(g.get('x')), float(g.get('y')), float(g.get('adv'))
                point = transform(text, x + a * adv / 2 - c * .33, y + b * adv / 2 - d * .33)
                glyphs.append(dict(digit=ch, point=point, matrix=span.get('trm'),
                                   baseline=transform(text, x, y), font=span.get('font')))
        assert len(glyphs) == 6
        center = [sum(g['point'][j] for g in glyphs) / 6 for j in range(2)]
        labels = {}
        for g in glyphs:
            x, y = g['point']; angle = math.atan2(-(y - center[1]), x - center[0])
            phase = (angle - math.pi / 2) / (math.pi / 3)
            assert abs(phase - round(phase)) < .015
            k = round(phase) % 6
            assert k not in labels
            labels[k] = g['digit']; g['side_ccw_from_north'] = k
        word = ''.join(labels[i] for i in range(6))
        records.append(dict(center=center, word=word, canonical=n.canonical(word), glyphs=glyphs))
    # Match each independent black rounded-hexagon outline to a glyph group.
    outlines = []
    for path in tree.iter('fill_path'):
        if path.get('color') != '0 0 0':
            continue
        vertices = []
        for element in path:
            if element.tag in ('moveto', 'lineto'):
                vertices.append(transform(path, float(element.get('x')), float(element.get('y'))))
            elif element.tag == 'curveto':
                vertices.append(transform(path, float(element.get('x3')), float(element.get('y3'))))
        assert len(vertices) == 13 and math.dist(vertices[0], vertices[-1]) < .001
        # Opposite line/corner endpoints are centrally symmetric.
        center = [sum(v[j] for v in vertices[:-1]) / 12 for j in range(2)]
        matches = [i for i, rec in enumerate(records) if math.dist(rec['center'], center) < .01]
        assert len(matches) == 1
        outlines.append(dict(glyph_group=matches[0], center=center, points=vertices))
    assert len(outlines) == len(records) and len({x['glyph_group'] for x in outlines}) == len(records)
    return records, outlines


def assemble(records):
    assert len(records) == 7
    cx, cy = [sum(p['center'][j] for p in records) / 7 for j in range(2)]
    central = min(records, key=lambda p: math.dist(p['center'], (cx, cy)))
    assert math.dist(central['center'], (cx, cy)) < .001
    radius = max(math.dist(p['center'], (cx, cy)) for p in records)
    placed = {0: central}
    for rec in records:
        if rec is central:
            continue
        assert abs(math.dist(rec['center'], (cx, cy)) - radius) < .001
        angle = math.atan2(-(rec['center'][1] - cy), rec['center'][0] - cx)
        phase = (angle - math.pi / 2) / (math.pi / 3)
        assert abs(phase - round(phase)) < .001
        k = 1 + round(phase) % 6
        assert k not in placed
        placed[k] = rec
    words = [placed[i]['word'] for i in range(7)]
    actual_edges = {(u, v) for u in range(7) for v in range(u + 1, 7)
                    if abs(math.dist(placed[u]['center'], placed[v]['center']) - radius) < .001}
    assert actual_edges == {(u, v) for u, v, _ in n.EDGES}
    return dict(words=words, normalized=n.normalize(words), types=sorted(map(n.canonical, words)),
                centers=[placed[i]['center'] for i in range(7)], adjacency=sorted(actual_edges))


def main():
    question, qo = extract(140)
    answers, ao = extract(452)
    assert len(question) == 7 and len(answers) == 14
    answers.sort(key=lambda p: p['center'][0])
    figures = [assemble(question), assemble(answers[:7]), assemble(answers[7:])]
    assert figures[1]['types'] == figures[2]['types']
    for f, rule in zip(figures, ['equal', 'equal', 'sum7']):
        n.validate(f['words'], f['types'], rule)
        f['matching_rule'] = rule
    n.save(n.OUT / 'figures-checked.json', dict(
        at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=n.sha(__file__),
        geometry_sha256=n.sha(n.__file__), book_sha256=n.sha(n.ROOT.parent / 'books/taocp-vol4b-ed1-print2-2022.pdf'),
        traces={str(p): n.sha(n.OUT / f'page{p}-trace.xml') for p in [140, 452]},
        glyph_count=126, figures=figures, glyph_groups=dict(question=question, answers=answers),
        outlines=dict(question=qo, answers=ao),
        scope='All42 question digits and84 answer digits decoded with original text matrices. '
              'Each group matches a black rounded-hexagon outline. Figure geometry gives '
              'exactly12 touching pairs. No reflections introduced.'))
    print('PASS137 all126 digits and3 arrangements; types:', figures[0]['types'], figures[1]['types'])


if __name__ == '__main__':
    main()
