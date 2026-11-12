#!/usr/bin/env python3
"""Fig104(d), fixed2x2 histoscape. Reuse its saved complete boundary proof."""
from fractions import Fraction as F
from collections import Counter
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT, geometric_visibility, printed_visibility, graph, solve
from check_polyhedra_fixed import sub, scale, dot, cross, normal, triangulate, encode
from check_cubie_junctions import path_points


def main():
    source = json.loads((ROOT / 'results/histoscape-local.json').read_text())['fig101d']
    vertices = [tuple(map(F, p)) for p in source['vertices']]
    index = {v: k for k, v in enumerate(vertices)}
    ed = [[index[tuple(a)], index[tuple(b)]] for a, b in source['edges']]
    tiles, faces, normals = [], [], []
    for f in source['faces']:
        axis, _, sign = f['plane_axis_coordinate_normal']
        n = tuple(F(sign if j == axis else 0) for j in range(3))
        assert len(f['boundary_loops']) == 1
        cycle = [index[tuple(v)] for v in f['boundary_loops'][0]]
        if dot(normal([vertices[k] for k in cycle]), n) < 0:
            cycle.reverse()
        new = triangulate(cycle, vertices)
        faces.append({'tiles': list(range(len(tiles), len(tiles) + len(new))), 'boundary_cycles': [cycle]})
        tiles.extend(new)
        normals.append(n)
    signs = {}
    for a, b in ed:
        incident = []
        for fi, f in enumerate(faces):
            cycle = f['boundary_cycles'][0]
            ee = list(zip(cycle, cycle[1:] + cycle[:1]))
            if (a, b) in ee:
                incident.append((fi, 1))
            elif (b, a) in ee:
                incident.append((fi, -1))
        assert len(incident) == 2 and incident[0][1] == -incident[1][1]
        (i, sign), (j, _) = incident
        value = dot(normals[j], cross(normals[i], scale(sub(vertices[b], vertices[a]), sign)))
        assert value
        signs[str(tuple(sorted((a, b))))] = 'concave' if value > 0 else 'convex'
    model = {'vertices': vertices, 'edges': ed, 'convex_tiles': tiles,
             'merged_faces': faces, 'edge_signs': signs}

    paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-026.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    top = path_points(paths[319])
    lower = path_points(paths[282])[0]
    references = [(0, 0, 4), (0, 1, 4), (1, 0, 4), (1, 0, 1)]
    points = [top[0], top[1], top[3], lower]
    rows = [solve([list(map(F, v)) + [F(1)] for v in references], [p[j] for p in points]) for j in (0, 1)]
    projected = [tuple(dot(row, (*v, F(1))) for row in rows) for v in vertices]
    relevant = {}
    residual = F(0)
    seen = set()
    for i in range(282, 343):
        p = paths[i]
        if p.get('fill') != 'rgb(100%, 100%, 100%)' and p.get('stroke') != 'rgb(0%, 0%, 0%)':
            continue
        mapped = []
        for point in path_points(p):
            distances = [dot(sub(v, point), sub(v, point)) for v in projected]
            k = min(range(20), key=distances.__getitem__)
            assert distances[k] < F(1, 10000)
            assert sorted(distances)[1] > 1
            residual = max(residual, distances[k])
            mapped.append(k)
            seen.add(k)
        relevant[i] = {'path': p, 'vertices': mapped}
    q = cross(rows[0][:3], rows[1][:3])
    if q[2] < 0:
        q = scale(q, -1)
    assert all(x > 0 for x in q)
    geometric, atoms = geometric_visibility(model, vertices, projected, q)
    printed, trace, rejected = printed_visibility(model, projected, relevant)
    assert geometric == printed, [(ed[k], geometric[k], printed[k]) for k in geometric if geometric[k] != printed[k]]
    junctions, lines = graph(model, projected, atoms)
    counts = dict(Counter(j['type'] for j in junctions))
    assert counts == {'V': 5, 'W': 8, 'Y': 5, 'T': 1}
    assert len(junctions) == 19 and lines == 26
    out = {'scope': 'Fig104(d): complete visible intervals and every final black path;19 junctions=5V+8W+5Y+1T,26 lines. Reuses the closed2x2 histoscape geometry.',
           'model': model, 'projection_rows': rows, 'view_direction_towards_camera': q,
           'maximum_original_point_residual_squared': residual,
           'original_path_vertices': sorted(seen), 'junction_types': counts,
           'junctions_total': len(junctions), 'lines': lines,
           'visible_physical_vertices': sorted(k for j in junctions for k in j['physical_vertex']),
           'fully_erased_auxiliary_segments': rejected,
           'visibility': [{'edge': ed[k], 'intervals': v} for k, v in geometric.items()],
           'printed_interval_trace': trace, 'junctions': junctions}
    (ROOT / 'results/histoscape-projection.json').write_text(json.dumps(out, indent=2, default=encode) + '\n')
    print(json.dumps({k: out[k] for k in ('scope', 'maximum_original_point_residual_squared', 'junction_types', 'visible_physical_vertices')}, indent=2, default=encode))


if __name__ == '__main__':
    main()
