"""Check all360 original wedges in the five figures of DLX129."""
from collections import defaultdict
from datetime import datetime, timezone
from math import sqrt
import json

import extract_jigsaw as ex
import symmetries129 as s

PALETTE = {'1 1 1': 'a', '1 .75 .75': 'b', '.5 .5 1': 'c', '.2 .2 .2': 'd'}


def figure(fills, label):
    assert len(fills) == 72
    tiles = []
    for i in range(0, 72, 3):
        points, colors, center = [], {}, None
        for path in fills[i:i+3]:
            polygons = ex.paths(path)
            assert len(polygons) == 1 and len(polygons[0]) == 3
            c, a, b = polygons[0]
            assert center is None or max(abs(v-w) for v, w in zip(c, center)) < .002
            center = c
            points.extend((a, b))
            dx, dy = b[0]-a[0], b[1]-a[1]
            side = '-' if abs(dy) < .002 else '/' if dx*dy < 0 else '\\'
            assert side not in colors
            colors[side] = PALETTE[path.get('color')]
        vertices = sorted({tuple(round(v, 3) for v in p) for p in points})
        assert len(vertices) == 3
        tiles.append(dict(center=center, vertices=vertices, colors=''.join(colors[k] for k in ('-', '/', '\\'))))

    lookup = {frozenset(s.g.vertices(t)): t for t in s.TS}
    vertices = {v for vv in lookup for v in vv}
    ux = [x+y/2 for x, y in vertices]
    uy = [y*sqrt(3)/2 for x, y in vertices]
    xx = [x for tile in tiles for x, y in tile['vertices']]
    yy = [y for tile in tiles for x, y in tile['vertices']]
    scale = (max(xx)-min(xx))/(max(ux)-min(ux))
    x0 = min(xx)-scale*min(ux)
    y0 = max(yy)+scale*min(uy)
    edges, cells, records = {}, {}, []
    for tile in tiles:
        vv = []
        for x, y in tile['vertices']:
            b = (y0-y)/(scale*sqrt(3)/2)
            a = (x-x0)/scale-b/2
            assert max(abs(a-round(a)), abs(b-round(b))) < .001
            vv.append((round(a), round(b)))
        t = lookup[frozenset(vv)]
        assert t not in cells
        cells[t] = tile['colors']
        for e, c in zip(s.g.edges(t), tile['colors']):
            assert e not in edges or edges[e] == c
            edges[e] = c
        records.append(dict(cell=t, colors=tile['colors'], piece=s.g.piece(tile['colors'])))
    assert set(cells) == set(s.TS) and set(edges) == set(s.ES)
    vector = ''.join(edges[e] for e in s.ES)
    s.validate(vector)
    return dict(label=label, wedge_count=72, tiles=records, colors=vector,
                edges=[dict(edge=e, color=edges[e]) for e in s.ES],
                symmetry=s.symmetry_flags(vector), monos=s.mono_positions(vector))


def periodic_pairs():
    # Translation lattice <(4,-2),(2,2)> has index12; its quotient has
    # exactly24 distinct triangle cells and36 distinct edges.
    key = lambda x, y: ((x-y) % 6, (x+2*y) % 6)
    assert len({(key(x, y), z) for x, y, z in s.TS}) == 24
    cosets = defaultdict(list)
    for kind, x, y in s.ES:
        cosets[kind, key(x, y)].append((kind, x, y))
    assert len(cosets) == 36
    pairs = []
    for part in cosets.values():
        assert len(part) in (1, 2)
        if len(part) == 2:
            assert all(len(s.g.EDGE_TRIANGLES[e]) == 1 for e in part)
            pairs.append(part)
        else:
            assert len(s.g.EDGE_TRIANGLES[part[0]]) == 2
    assert len(pairs) == 6
    return pairs


def main():
    ex.OUT = s.OUT
    figures = []
    for page, count in [(139, 2), (449, 3)]:
        tree = ex.trace(page)
        fills = [p for p in tree.iter('fill_path') if p.get('colorspace') == 'DeviceRGB']
        assert len(fills) == {139: 420, 449: 288}[page]
        for i in range(count):
            figures.append(figure(fills[72*i:72*(i+1)], f'p{page}-{i+1}'))
    first, second, *special = figures
    assert set(first['symmetry']['strong']) == {'r0', 'r3'}
    assert set(second['symmetry']['strong']) == {'r0'}
    assert set(second['symmetry']['weak']) != {'r0'}
    pairs = periodic_pairs()
    assert all(first['colors'][s.EI[e]] == first['colors'][s.EI[f]] for e, f in pairs)
    first['unrotated_periodic'] = dict(lattice_basis=[[4, -2], [2, 2]], index=12, edge_pairs=pairs)
    for f, tb_kind, rot_kind in zip(special, (1, 4, 6), (5, 3, 1)):
        assert set(f['symmetry']['strong']) == {'r0', 'r3'}
        assert set(f['symmetry']['weak']) == {'r0', 'r3', 'lr', 'tb'}
        f['canonical_types'] = {mode: s.all_canonical_types(f['colors'], mode) for mode in ('rotation', 'tb')}
        assert {x['kind'] for x in f['canonical_types']['rotation']} == {rot_kind}
        assert {x['kind'] for x in f['canonical_types']['tb']} == {tb_kind}
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=s.sha(__file__),
                  geometry_source_sha256=s.sha(s.__file__), book_sha256=s.sha(ex.BOOK),
                  trace_sha256={str(p): s.sha(s.OUT/f'page{p}-trace.xml') for p in (139, 449)},
                  total_wedges=360, figures=figures,
                  scope='All five129 figures, all24 distinct pieces in each, every shared edge, the complete weak/strong symmetry group, the periodic example and the three canonical type pairs. Other illustrations on these pages are not included.')
    (s.OUT/'original-figures-checked.json').write_text(json.dumps(result, indent=2)+'\n')
    for f in figures:
        print('PASS', f['label'], f['symmetry'], flush=True)


if __name__ == '__main__':
    main()
