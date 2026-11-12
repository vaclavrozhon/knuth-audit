#!/usr/bin/env python3
"""The independent reverse view103(d), using the closed histoscape solid."""
from fractions import Fraction as F
from collections import Counter, defaultdict
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT, geometric_visibility, printed_visibility, graph, solve
from check_polyhedra_fixed import sub, add, scale, dot, cross, encode
from check_cubie_junctions import path_points


def main():
    old = json.loads((ROOT / 'results/histoscape-projection.json').read_text())
    model = old['model']
    vertices = [tuple(map(F, v)) for v in model['vertices']]
    front_rows = [list(map(F, row)) for row in old['projection_rows']]
    rotated_rows = [[row[0] * -1, row[1] * -1, row[2]] for row in front_rows]
    predicted = [tuple(dot(row, v) for row in rotated_rows) for v in vertices]
    paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-025.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    all_points = [p for item in paths[136:146] for p in path_points(item)]
    shift = tuple(min(p[k] for p in all_points) - min(p[k] for p in predicted) for k in (0, 1))
    predicted = [add(p, shift) for p in predicted]
    relevant, occurrences = {}, defaultdict(list)
    rotation_residual = F(0)
    for i in range(136, 146):
        p = paths[i]
        mapped = []
        for point in path_points(p):
            distances = [dot(sub(v, point), sub(v, point)) for v in predicted]
            k = min(range(20), key=distances.__getitem__)
            assert distances[k] < F(1, 1000)
            assert sorted(distances)[1] > 1
            rotation_residual = max(rotation_residual, distances[k])
            mapped.append(k); occurrences[k].append(point)
        relevant[i] = {'path': p, 'vertices': mapped}
    refs = [0, 1, 4, 14]  # Three independent coordinate axes from the origin.
    points = [tuple(sum(p[j] for p in occurrences[k]) / len(occurrences[k]) for j in (0, 1)) for k in refs]
    rows = [solve([list(vertices[k]) + [F(1)] for k in refs], [p[j] for p in points]) for j in (0, 1)]
    projected = [tuple(dot(row, (*v, F(1))) for row in rows) for v in vertices]
    residual = max(dot(sub(projected[k], p), sub(projected[k], p)) for k in occurrences for p in occurrences[k])
    assert residual < F(1, 10000)
    q = cross(rows[0][:3], rows[1][:3])
    if q[2] < 0:
        q = scale(q, -1)
    assert q[0] < 0 and q[1] < 0 < q[2]
    geometric, atoms = geometric_visibility(model, vertices, projected, q)
    printed, trace, rejected = printed_visibility(model, projected, relevant)
    assert printed == geometric, [(model['edges'][k], printed[k], geometric[k]) for k in printed if printed[k] != geometric[k]]
    junctions, lines = graph(model, projected, atoms)
    counts = dict(Counter(j['type'] for j in junctions))
    out = {'scope': 'Fig103(d): all original black intervals and complete independent visibility of the2x2 histoscape. Coordinates agree with the180-degree z-axis reversal within printing precision.',
           'projection_rows': rows, 'view_direction_towards_camera': q,
           'maximum_halfturn_vertex_residual_squared_before_refit': rotation_residual,
           'maximum_original_point_residual_squared': residual,
           'junction_types': counts, 'junctions_total': len(junctions), 'lines': lines,
           'visible_physical_vertices': sorted(k for j in junctions for k in j['physical_vertex']),
           'fully_erased_auxiliary_segments': rejected,
           'visibility': [{'edge': model['edges'][k], 'intervals': v} for k, v in geometric.items()],
           'printed_interval_trace': trace, 'junctions': junctions}
    (ROOT / 'results/histoscape-reverse.json').write_text(json.dumps(out, indent=2, default=encode) + '\n')
    print(json.dumps({k: out[k] for k in ('scope', 'maximum_original_point_residual_squared', 'junction_types', 'junctions_total', 'lines', 'visible_physical_vertices')}, indent=2, default=encode))


if __name__ == '__main__':
    main()
