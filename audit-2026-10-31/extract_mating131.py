"""Original131 diagrams:72 stroked jigsaw sides,72 black wedges and108 dots."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from math import sqrt
import xml.etree.ElementTree as ET

import extract_jigsaw as ex
import mating131 as m
import symmetries129 as s


def path_points(el):
    points = []
    for q in el:
        if q.tag in ('moveto', 'lineto'):
            points.append(ex.transform(el, float(q.get('x')), float(q.get('y'))))
        elif q.tag == 'curveto':
            points.extend(ex.transform(el, float(q.get('x'+str(i))), float(q.get('y'+str(i)))) for i in (1, 2, 3))
        else:
            assert q.tag == 'closepath'
    return points


def grid_map(points):
    vertices = {v for t in s.TS for v in m.g.vertices(t)}
    ux = [x+y/2 for x, y in vertices]
    uy = [y*sqrt(3)/2 for x, y in vertices]
    xx, yy = zip(*points)
    scale = (max(xx)-min(xx))/(max(ux)-min(ux))
    x0 = min(xx)-scale*min(ux); y0 = max(yy)+scale*min(uy)

    def convert(p):
        b = (y0-p[1])/(scale*sqrt(3)/2)
        a = (p[0]-x0)/scale-b/2
        assert max(abs(a-round(a)), abs(b-round(b))) < .0002, (p, a, b)
        return round(a), round(b)

    return convert, dict(scale=scale, x0=x0, y0=y0)


def finalize(cells, mode):
    assert set(cells) == set(s.TS)
    types = [m.g.piece(''.join(cells[t][e] for e in m.g.edges(t))) for t in s.TS]
    assert sorted(types) == m.g.PIECES
    edges = {}
    for t, colors in cells.items():
        for e, c in colors.items():
            value = m.mate(c, mode) if t[2] else c
            assert e not in edges or edges[e] == value
            edges[e] = value
    for e, ts in m.g.EDGE_TRIANGLES.items():
        if len(ts) == 1:
            assert edges[e] == ('a' if mode == 'a' or e[0] != '-' else 'b')
        else:
            assert m.mate(cells[ts[0]][e], mode) == cells[ts[1]][e]
    vector = ''.join(edges[e] for e in s.ES)
    symmetries = [(a['label'], p) for a in (s.D6 if mode == 'a' else [s.BY[k] for k in ('r0', 'r3', 'lr', 'tb')])
                  for p in ('abcd', 'abdc') if s.transform(vector, a, p) == vector]
    return dict(encoded_colors=vector, symmetries=symmetries,
                tiles=[dict(cell=t, colors=''.join(cells[t][e] for e in m.g.edges(t)), piece=p) for t, p in zip(s.TS, types)])


def jigsaw(tree):
    curves = []
    for el in tree.iter('stroke_path'):
        if el.get('color') != '0 0 0':
            continue
        points = path_points(el)
        if points and all(75 < x < 215 and 220 < y < 328 for x, y in points):
            curves.append(dict(points=points, cubic_segments=sum(q.tag == 'curveto' for q in el)))
    assert len(curves) == 72
    to_grid, coordinates = grid_map([p for c in curves for p in (c['points'][0], c['points'][-1])])
    tile_lookup = {frozenset(m.g.vertices(t)): t for t in s.TS}
    edge_lookup = {frozenset(s.ends(e)): e for e in s.ES}
    cells, occurrences = {}, defaultdict(list)
    records = []
    for i in range(0, 72, 3):
        sides = curves[i:i+3]
        corners = {to_grid(p) for c in sides for p in (c['points'][0], c['points'][-1])}
        t = tile_lookup[frozenset(corners)]
        assert t not in cells
        cells[t] = {}
        center = tuple(sum(c['points'][j][k] for c in sides for j in (0, -1))/6 for k in range(2))
        for c in sides:
            ps = c['points']; a, b = ps[0], ps[-1]
            ea, eb = to_grid(a), to_grid(b)
            e = edge_lookup[frozenset((ea, eb))]
            assert e in m.g.edges(t)
            cross = lambda p: (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
            inside = cross(center)
            deviations = [cross(p)*(1 if inside > 0 else -1) for p in ps]
            n = c['cubic_segments']
            if n == 0:
                assert len(ps) == 2
                color = 'a'
            elif n == 2:
                assert len(ps) == 7 and deviations[1]*deviations[4] < 0
                assert abs(sum(deviations)) < .1
                color = 'b'
            else:
                assert n == 3 and len(ps) == 10
                assert deviations[1]*deviations[4] < 0 and deviations[1]*deviations[7] > 0
                assert abs(sum(deviations)) > 100
                color = 'c' if sum(deviations) < 0 else 'd'
            cells[t][e] = color
            ordered = ps if ea < eb else list(reversed(ps))
            occurrences[e].append(ordered)
            records.append(dict(cell=t, edge=e, type=color, cubic_segments=n,
                                normalized_inward_deviations=[v/abs(inside) for v in deviations]))
    assert set(occurrences) == set(s.ES)
    for e, paths in occurrences.items():
        assert len(paths) == len(m.g.EDGE_TRIANGLES[e])
        if len(paths) == 2:
            assert len(paths[0]) == len(paths[1])
            assert max(abs(x-y) for a, b in zip(paths[0], paths[1]) for x, y in zip(a, b)) < .004
    result = finalize(cells, 'a')
    result.update(stroked_sides=72, distinct_edges=42, internal_curve_pairs=30,
                  curve_kinds=dict(Counter(c['cubic_segments'] for c in curves)),
                  coordinates=coordinates, sides=records)
    return result


def triminoes(tree):
    wedges = []
    for el in tree.iter('fill_path'):
        if el.get('colorspace') != 'DeviceRGB':
            continue
        points = path_points(el)
        if not points or not all(240 < x < 382 and 220 < y < 328 for x, y in points):
            continue
        if el.get('color') == '0 0 0':
            assert len(points) == 3 and all(q.tag in ('moveto', 'lineto') for q in el)
            wedges.append(dict(vertices=points, dots=[]))
        else:
            assert el.get('color') == '1 1 1' and len(points) == 25
            assert sum(q.tag == 'curveto' for q in el) == 8
            ring = [points[0]]+[points[i] for i in (3, 6, 9, 12, 15, 18, 21)]
            center = tuple(sum(p[k] for p in ring)/8 for k in (0, 1))
            radii = [sum((p[k]-center[k])**2 for k in (0, 1)) for p in ring]
            assert max(radii)-min(radii) < .005
            assert ex.inside(*center, wedges[-1]['vertices'])
            wedges[-1]['dots'].append(center)
    assert len(wedges) == 72 and sum(len(w['dots']) for w in wedges) == 108
    # The first two vertices delimit the outer side; the third is the tile center.
    to_grid, coordinates = grid_map([p for w in wedges for p in w['vertices'][:2]])
    tile_lookup = {frozenset(m.g.vertices(t)): t for t in s.TS}
    edge_lookup = {frozenset(s.ends(e)): e for e in s.ES}
    cells, records = {}, []
    for i in range(0, 72, 3):
        group = wedges[i:i+3]
        center = group[0]['vertices'][2]
        assert max(abs(w['vertices'][2][k]-center[k]) for w in group for k in (0, 1)) < .003
        corners = {to_grid(p) for w in group for p in w['vertices'][:2]}
        t = tile_lookup[frozenset(corners)]; assert t not in cells; cells[t] = {}
        for w in group:
            edge = edge_lookup[frozenset(to_grid(p) for p in w['vertices'][:2])]
            dots = len(w['dots']); assert 0 <= dots <= 3
            cells[t][edge] = 'cabd'[dots]
            records.append(dict(cell=t, edge=edge, dots=dots, dot_centers=w['dots']))
    result = finalize(cells, 'b')
    assert ('r3', 'abcd') in result['symmetries']
    result.update(black_wedges=72, dots=108, coordinates=coordinates, sides=records)
    return result


def main():
    trace = s.OUT/'page139-trace.xml'; tree = ET.parse(trace)
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=m.sha(__file__),
                  model_sha256=m.sha(m.__file__), geometry_sha256=m.sha(s.__file__),
                  book_sha256=m.sha(ex.BOOK), trace=str(trace.relative_to(m.ROOT)), trace_sha256=m.sha(trace),
                  jigsaw=jigsaw(tree), triminoes=triminoes(tree))
    m.save(m.OUT/'original-figures-checked.json', result)
    print('PASS131 original figures:', result['jigsaw']['curve_kinds'], '108 dots;',
          result['triminoes']['symmetries'])


if __name__ == '__main__':
    main()
