#!/usr/bin/env python3
"""Fixed30-edge clasp: exact hidden-surface proof and original104(c) paths.

Read the already certified3D model. Do not rerun its embedding certificate.
Recover the printed projection, then independently compare every final black
stroke interval with exact ray/facet visibility. No polyhedron search.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET
from check_polyhedra_fixed import ROOT, sub, add, scale, dot, cross, normal, encode
from check_figure102_vectors import solve
from check_cubie_junctions import path_points


def cross2(a, b):
    return a[0] * b[1] - a[1] * b[0]


def segments(p):
    return list(zip(p, p[1:] + p[:1]))


def on(p, a, b):
    return cross2(sub(p, a), sub(b, a)) == 0 and dot(sub(p, a), sub(p, b)) <= 0


def at(a, b, t):
    return add(a, scale(sub(b, a), t))


def parameter(p, a, b):
    k = next(i for i in (0, 1) if b[i] != a[i])
    return (p[k] - a[k]) / (b[k] - a[k])


def cuts(a, b, c, d):
    u, v, w = sub(b, a), sub(d, c), sub(c, a)
    det = cross2(u, v)
    if det:
        s, t = cross2(w, v) / det, cross2(w, u) / det
        return [s] if 0 <= s <= 1 and 0 <= t <= 1 else []
    if cross2(w, u):
        return []
    return [parameter(p, a, b) for p in (c, d) if on(p, a, b)]


def winding(p, poly):
    count = 0
    for a, b in segments(poly):
        if on(p, a, b):
            return True
        det = cross2(sub(b, a), sub(p, a))
        if a[1] <= p[1] < b[1] and det > 0:
            count += 1
        elif b[1] <= p[1] < a[1] and det < 0:
            count -= 1
    return count != 0


def merge(intervals):
    out = []
    for a, b in sorted(intervals):
        if a == b:
            continue
        assert a < b
        if out and a <= out[-1][1]:
            out[-1][1] = max(b, out[-1][1])
        else:
            out.append([a, b])
    return out


def path_segments(p, mapped):
    # All relevant paths use M,L,Z. A trailing M after Z contributes no line.
    tokens = re.findall(r'[A-Za-z]|[-+]?(?:\d+(?:\.\d*)?|\.\d+)', p['d'])
    point_index = 0
    current = first = None
    out = []
    i = 0
    while i < len(tokens):
        cmd = tokens[i]
        i += 1
        if cmd == 'Z':
            if current != first:
                out.append((current, first))
            current = first
        else:
            assert cmd in ('M', 'L')
            i += 2
            point = mapped[point_index]
            point_index += 1
            if cmd == 'M':
                first = point
            elif current != point:
                out.append((current, point))
            current = point
    assert point_index == len(mapped)
    return out


def load():
    model = json.loads((ROOT / 'results/polyhedra-fixed.json').read_text())['Clasp']
    vertices = [tuple(F(x) for x in p) for p in model['vertices']]
    drawing = json.loads((ROOT / 'results/figure102-vectors.json').read_text())['c']
    old = [tuple(F(x) for x in p) for p in drawing['vertices']]
    predicted = [add(old[k], (F('32.15'), F('.67'))) for k in drawing['source_to_drawing_vertex']]
    all_paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-026.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    relevant = {}
    occurrences = defaultdict(list)
    rough_max_error = F(0)
    for index in range(228, 278):
        p = all_paths[index]
        if not (p.get('fill') == 'rgb(100%, 100%, 100%)'
                or p.get('stroke') == 'rgb(0%, 0%, 0%)'):
            continue
        points = path_points(p)
        mapped = []
        for point in points:
            distances = [dot(sub(v, point), sub(v, point)) for v in predicted]
            k = min(range(20), key=distances.__getitem__)
            assert distances[k] < F(1, 100)
            assert sorted(distances)[1] > F(1, 10)
            rough_max_error = max(rough_max_error, distances[k])
            mapped.append(k)
            occurrences[k].append(point)
        relevant[index] = {'path': p, 'vertices': mapped}
    assert set(occurrences) == set(range(20)) - {16}
    # Four outer corners of the first tetrahedron give an affine projection.
    anchors = [tuple(sum(p[j] for p in occurrences[k]) / len(occurrences[k]) for j in (0, 1)) for k in range(4)]
    mat = [list(v) + [F(1)] for v in vertices[:4]]
    rows = [solve(mat, [p[j] for p in anchors]) for j in (0, 1)]
    projected = [tuple(sum(x * y for x, y in zip(row, (*v, F(1)))) for row in rows) for v in vertices]
    residual = max(dot(sub(projected[k], p), sub(projected[k], p)) for k in occurrences for p in occurrences[k])
    assert residual < F(1, 10000)
    # This exact fitted direction, not approximate orthonormality, determines
    # all incidences and visibility. The screen map may include a plane affine
    # distortion; it has the same viewing rays as an orthographic projection.
    q = cross(rows[0][:3], rows[1][:3])
    assert q != (0, 0, 0)
    return model, vertices, projected, q, rows, relevant, residual


def ray_hidden(p, q, polygons, normals):
    witnesses = []
    for k, (poly, n) in enumerate(zip(polygons, normals)):
        den = dot(n, q)
        assert den
        t = dot(n, sub(poly[0], p)) / den
        if t <= 0:
            continue
        hit = add(p, scale(q, t))
        if all(dot(cross(sub(b, a), sub(hit, a)), n) >= 0 for a, b in segments(poly)):
            witnesses.append(k)
    return witnesses


def geometric_visibility(model, vertices, projected, q):
    ed = [tuple(e) for e in model['edges']]
    polygons = [[vertices[k] for k in f] for f in model['convex_tiles']]
    normals = [normal(poly) for poly in polygons]
    intervals = {}
    atoms = []
    for edge_index, (a, b) in enumerate(ed):
        cut = {F(0), F(1)}
        for c, d in ed:
            cut.update(cuts(projected[a], projected[b], projected[c], projected[d]))
        cut = sorted(cut)
        live = []
        for s, t in zip(cut, cut[1:]):
            mid = (s + t) / 2
            hidden = ray_hidden(at(vertices[a], vertices[b], mid), q, polygons, normals)
            if not hidden:
                live.append([s, t])
                atoms.append((edge_index, s, t))
        intervals[edge_index] = merge(live)
    return intervals, atoms


def printed_visibility(model, projected, relevant):
    fills = [(index, [projected[k] for k in a['vertices']]) for index, a in relevant.items()
             if a['path'].get('fill') == 'rgb(100%, 100%, 100%)']
    intervals = defaultdict(list)
    rejected_auxiliary_segments = 0
    trace = []
    ed = model['edges']
    for index, item in relevant.items():
        p = item['path']
        if p.get('stroke') != 'rgb(0%, 0%, 0%)':
            continue
        for va, vb in path_segments(p, item['vertices']):
            a, b = projected[va], projected[vb]
            later = [(j, poly) for j, poly in fills if j > index]
            cut = {F(0), F(1)}
            for _, poly in later:
                for c, d in segments(poly):
                    cut.update(cuts(a, b, c, d))
            cut = sorted(cut)
            retained = False
            for s, t in zip(cut, cut[1:]):
                p0 = at(a, b, (s + t) / 2)
                covers = [j for j, poly in later if winding(p0, poly)]
                if covers:
                    continue
                matches = [k for k, (c, d) in enumerate(ed) if on(p0, projected[c], projected[d])]
                assert len(matches) == 1, ('visible nonedge or ambiguity', index, va, vb, matches)
                k = matches[0]
                c, d = ed[k]
                u, v = sorted(parameter(at(a, b, z), projected[c], projected[d]) for z in (s, t))
                assert 0 <= u < v <= 1
                intervals[k].append([u, v])
                trace.append({'path': index, 'source_segment': [va, vb], 'physical_edge': ed[k], 'interval': [u, v]})
                retained = True
            if not retained and tuple(sorted((va, vb))) not in {tuple(sorted(e)) for e in ed}:
                rejected_auxiliary_segments += 1
    return {k: merge(intervals[k]) for k in range(len(ed))}, trace, rejected_auxiliary_segments


def graph(model, projected, atoms):
    adj = defaultdict(dict)
    for ei, s, t in atoms:
        a, b = model['edges'][ei]
        p, q = at(projected[a], projected[b], s), at(projected[a], projected[b], t)
        assert p != q
        adj[p][q] = ei
        adj[q][p] = ei
    # Remove unused intersection cuts inside a single straight visible line.
    while True:
        remove = next((p for p, ns in adj.items() if len(ns) == 2
                       and cross2(sub(next(iter(ns)), p), sub(list(ns)[1], p)) == 0), None)
        if remove is None:
            break
        a, b = adj[remove]
        assert adj[remove][a] == adj[remove][b]
        ei = adj[remove][a]
        del adj[a][remove]
        del adj[b][remove]
        del adj[remove]
        adj[a][b] = adj[b][a] = ei
    junctions = []
    for p, ns in adj.items():
        assert len(ns) in (2, 3)
        rays = [sub(v, p) for v in ns]
        if len(rays) == 2:
            assert cross2(*rays)
            kind = 'V'
        elif any(cross2(a, b) == 0 and dot(a, b) < 0 for a, b in combinations(rays, 2)):
            kind = 'T'
        else:
            # A positive linear dependence means the rays surround the origin.
            coeff = [cross2(rays[1], rays[2]), cross2(rays[2], rays[0]), cross2(rays[0], rays[1])]
            kind = 'Y' if all(x > 0 for x in coeff) or all(x < 0 for x in coeff) else 'W'
        physical = [k for k, v in enumerate(projected) if p == v]
        assert len(physical) <= 1
        assert (kind == 'T') == (not physical)
        junctions.append({'point': p, 'type': kind, 'physical_vertex': physical,
                          'incident_edges': [model['edges'][ei] for ei in ns.values()]})
    return junctions, sum(map(len, adj.values())) // 2


def main():
    model, vertices, projected, q, rows, relevant, residual = load()
    printed, trace, rejected = printed_visibility(model, projected, relevant)
    # The original front face012 (with hole456) is visible; its outward normal
    # fixes the direction sign. The model's oriented volumes are positive.
    n = normal([vertices[k] for k in model['convex_tiles'][0]])
    if dot(n, q) < 0:
        q = scale(q, -1)
    geometric, atoms = geometric_visibility(model, vertices, projected, q)
    assert printed == geometric, ('visibility mismatch',
                                  [(model['edges'][k], printed[k], geometric[k]) for k in printed if printed[k] != geometric[k]])
    junctions, lines = graph(model, projected, atoms)
    counts = dict(Counter(j['type'] for j in junctions))
    assert counts.get('T') == 15
    out = {'scope': 'Fig104(c): all physical-edge visible intervals compared with every final black SVG stroke. Exact independent ray/facet visibility; all junctions and15T counted.',
           'projection_rows': rows, 'view_direction_towards_camera': q,
           'maximum_original_point_residual_squared': residual,
           'physical_edges': len(model['edges']), 'junction_types': counts,
           'junctions_total': len(junctions), 'lines': lines,
           'visible_physical_vertices': sorted(k for j in junctions for k in j['physical_vertex']),
           'fully_erased_auxiliary_segments': rejected,
           'visibility': [{'edge': model['edges'][k], 'intervals': v} for k, v in geometric.items()],
           'printed_interval_trace': trace, 'junctions': junctions}
    (ROOT / 'results/clasp-projection.json').write_text(json.dumps(out, indent=2, default=encode) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k not in ('visibility', 'printed_interval_trace', 'junctions', 'projection_rows', 'view_direction_towards_camera')}, indent=2, default=encode))


if __name__ == '__main__':
    main()
