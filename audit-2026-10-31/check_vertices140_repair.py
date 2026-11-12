"""Check the printed corner mismatch and every possible single-tile rotation."""
from collections import defaultdict
from datetime import datetime, timezone
from math import sqrt
import json
import xml.etree.ElementTree as ET
import vertices140 as h
from extract_vertices140 import decode, PALETTE
from extract_jigsaw import transform


def inspect(triangles):
    at = defaultdict(list)
    tiles = []
    for i, tri in enumerate(triangles):
        colors = dict(zip(map(tuple, tri['vertices']), tri['colors']))
        tiles.append(h.piece(''.join(colors[v] for v in h.vertices(tri['cell']))))
        for v, color in colors.items():
            at[v].append(dict(triangle=i, color=color))
    assert sorted(tiles) == h.PIECES
    conflicts = [dict(vertex=v, occurrences=cs) for v, cs in sorted(at.items())
                 if len({c['color'] for c in cs}) != 1]
    word = None if conflicts else ''.join(at[v][0]['color'] for v in sorted(at))
    return conflicts, word


def draw(original, repaired):
    palette = dict(a='#ffffff', b='#ffbfbf', c='#8080ff', d='#333333')
    out = ['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="345" viewBox="0 0 1120 345">',
           '<rect width="1120" height="345" fill="white"/>',
           '<style>text{font-family:Arial,sans-serif;fill:#152035}</style>',
           '<text x="24" y="30" font-size="21">TAOCP 4B, p. 454, answer 140(c): third figure</text>']
    for panel, tris in enumerate([original, repaired]):
        offset = 25 + 560 * panel
        point = lambda v: (offset + 48 * (v[0] + v[1]/2), 290 - 48*sqrt(3)/2*v[1])
        label = 'Printed: white and pink meet at two vertices' if panel == 0 else 'Corrected: rotate the outlined tile 120° clockwise'
        out.append(f'<text x="{offset}" y="65" font-size="16">{label}</text>')
        for i, tri in enumerate(tris):
            ps = [point(v) for v in tri['vertices']]
            poly = ' '.join(f'{x:.3f},{y:.3f}' for x, y in ps)
            clip = f'c{panel}-{i}'
            out.append(f'<defs><clipPath id="{clip}"><polygon points="{poly}"/></clipPath></defs>')
            out.append(f'<polygon points="{poly}" fill="white"/>')
            for (x, y), col in zip(ps, tri['colors']):
                out.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="23.8" fill="{palette[col]}" clip-path="url(#{clip})"/>')
            out.append(f'<polygon points="{poly}" fill="none" stroke="#222" stroke-width="1.2"/>')
        tri = tris[7]
        poly = ' '.join(f'{x:.3f},{y:.3f}' for x, y in map(point, tri['vertices']))
        out.append(f'<polygon points="{poly}" fill="none" stroke="#dc6600" stroke-width="3"/>')
    out.append('<text x="24" y="330" font-size="14">a = white, b = pink, c = blue, d = dark gray. All 24 tile types occur exactly once in both panels.</text></svg>')
    target = h.ROOT/'images/vertices140-c3-repair.svg'
    target.write_text('\n'.join(out)+'\n')
    return str(target.relative_to(h.ROOT))


def main():
    figures = json.loads((h.OUT/'figures-checked.json').read_text())
    assert figures['source_sha256'] == h.sha(h.ROOT/'extract_vertices140.py')
    assert figures['geometry_sha256'] == h.sha(h.__file__)
    for page, digest in figures['trace_sha256'].items():
        path = h.ROOT/'results/heads139/page453-trace.xml' if page == '453' else h.OUT/f'page{page}-trace.xml'
        assert h.sha(path) == digest
    fig = figures['figures']['c3']
    original = fig['triangles']
    conflicts, word = inspect(original)
    assert word is None and len(conflicts) == 2
    repairs = []
    for i, tri in enumerate(original):
        for shift in (1, 2):
            trial = json.loads(json.dumps(original))
            trial[i]['colors'] = tri['colors'][shift:] + tri['colors'][:shift]
            bad, w = inspect(trial)
            if not bad:
                h.validate(fig['cells'], w)
                repairs.append(dict(triangle=i, shift=shift, word=w, triangles=trial))
    assert len(repairs) == 1 and repairs[0]['triangle'] == 7
    repaired = repairs[0]
    old = dict(zip(map(tuple, original[7]['vertices']), original[7]['colors']))
    new = dict(zip(map(tuple, repaired['triangles'][7]['vertices']), repaired['triangles'][7]['colors']))
    ccw = h.vertices(original[7]['cell'])
    assert ''.join(old[v] for v in ccw) == 'abb'
    assert ''.join(new[v] for v in ccw) == 'bba'
    # All seven draft figures, not merely an isolated color or cropped image.
    palette = dict(PALETTE, **{'.199951 .199951 .199951': 'd'})
    sectors = []
    for e in ET.parse(h.OUT/'draft158-trace.xml').getroot().iter('fill_path'):
        if e.get('colorspace') != 'DeviceRGB' or e.get('color') not in palette:
            continue
        if [x.tag for x in e] != ['moveto', 'lineto', 'curveto']:
            continue
        p = e[0]
        sectors.append(dict(point=transform(e, float(p.get('x')), float(p.get('y'))), color=palette[e.get('color')]))
    assert len(sectors) == 504
    draft = {}
    for i in range(7):
        label = f'c{i+1}'
        draft[label] = decode(sectors[72*i:72*(i+1)])
        book = figures['figures'][label]
        for key in ['cells', 'vertices', 'triangles', 'vertex_conflicts']:
            assert json.dumps(draft[label][key]) == json.dumps(book[key]), (label, key)
    diagram = draw(original, repaired['triangles'])
    h.save(h.OUT/'repair-checked.json', dict(
        at_utc=datetime.now(timezone.utc).isoformat(), checker_sha256=h.sha(__file__),
        figures_sha256=h.sha(h.OUT/'figures-checked.json'), geometry_sha256=h.sha(h.__file__),
        book_sha256=figures['book_sha256'], draft_trace_sha256=h.sha(h.OUT/'draft158-trace.xml'),
        original_ps_sha256=h.sha(h.ROOT/'sources/fasc5c.ps.gz'), draft_pdf_sha256=h.sha(h.ROOT/'sources/fasc5c.pdf'),
        original_conflicts=conflicts, attempted_single_tile_rotations=48, unique_repair=repaired,
        tile_cell=original[7]['cell'], before_ccw='abb', after_ccw='bba',
        rotation='120 degrees clockwise: white moves from the right vertex to the bottom vertex',
        all_draft_corners_identical=504, all_draft_figures_identical=7,
        diagram=diagram, diagram_sha256=h.sha(h.ROOT/diagram),
        physical_print_verified=False))
    print('PASS: two printed conflicts; unique single-tile repair among 48; all 504 draft corners identical.')


if __name__ == '__main__':
    main()
