#!/usr/bin/env python3
"""Fig104(b): use the already proved book coordinates and all seven faces."""
from fractions import Fraction as F
from collections import Counter, defaultdict
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT, geometric_visibility, printed_visibility, graph, solve
from check_polyhedra_fixed import sub, add, scale, dot, cross, normal, triangulate, encode
from check_cubie_junctions import path_points


def main():
    source = json.loads((ROOT / 'results/szilassi-exact.json').read_text())
    signature = json.loads((ROOT / 'results/szilassi-signature.json').read_text())
    names = list(source['vertices'])
    index = {n: k for k, n in enumerate(names)}
    vertices = [tuple(map(F, source['vertices'][n])) for n in names]
    ed = [[index[a], index[b]] for a, b in [x['edge'] for x in signature['edge_signs']]]
    tiles, faces = [], []
    for f in source['faces']:
        cycle = [index[n] for n in f['cycle']]
        # Stored consistent cycles have negative volume; reverse to outward.
        if source['consistent_cycle_orientation_signs'][str(f['face'])] > 0:
            cycle.reverse()
        new = triangulate(cycle, vertices)
        faces.append({'tiles': list(range(len(tiles), len(tiles) + len(new))), 'boundary_cycles': [cycle]})
        tiles.extend(new)
    model = {'vertices': vertices, 'vertex_names': names, 'edges': ed,
             'convex_tiles': tiles, 'merged_faces': faces,
             'edge_signs': {str(tuple(sorted((index[x['edge'][0]], index[x['edge'][1]])))): x['sign'] for x in signature['edge_signs']}}

    wire = json.loads((ROOT / 'results/figure102-vectors.json').read_text())['b']
    mapping = dict(zip(['023', '206', '460', '054', '501', '310'], [7, 6, 13, 12, 4, 3]))
    neighbors, wn = defaultdict(set), defaultdict(set)
    for a, b in ed:
        neighbors[names[a]].add(names[b]); neighbors[names[b]].add(names[a])
    for a, b in wire['edges']:
        wn[a].add(b); wn[b].add(a)
    while len(mapping) < 14:
        before = len(mapping)
        for a, b in list(mapping.items()):
            left, right = neighbors[a] - mapping.keys(), wn[b] - set(mapping.values())
            if len(left) == len(right) == 1:
                mapping[next(iter(left))] = next(iter(right))
        assert len(mapping) > before
    assert len(set(mapping.values())) == 14
    assert {tuple(sorted((mapping[names[a]], mapping[names[b]]))) for a, b in ed} == {tuple(e) for e in wire['edges']}
    cyclic = lambda c: min(tuple(c[i:] + c[:i]) for i in range(len(c)))
    unoriented = lambda c: min(cyclic(c), cyclic(list(reversed(c))))
    assert {unoriented([mapping[n] for n in f['cycle']]) for f in source['faces']} == {unoriented(f['cycle']) for f in wire['boundaries']}
    old = [tuple(map(F, v)) for v in wire['vertices']]
    predicted = [add(old[mapping[n]], (F('32.52'), F('.66'))) for n in names]

    paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-026.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    relevant, occurrences = {}, defaultdict(list)
    for i in range(192, 228):
        p = paths[i]
        if p.get('fill') != 'rgb(100%, 100%, 100%)' and p.get('stroke') != 'rgb(0%, 0%, 0%)':
            continue
        mapped = []
        for point in path_points(p):
            distances = [dot(sub(v, point), sub(v, point)) for v in predicted]
            k = min(range(14), key=distances.__getitem__)
            assert distances[k] < F(1, 100)
            assert sorted(distances)[1] > 1
            mapped.append(k); occurrences[k].append(point)
        relevant[i] = {'path': p, 'vertices': mapped}
    refs = [index[n] for n in ('023', '206', '054', '532')]
    points = [tuple(sum(p[j] for p in occurrences[k]) / len(occurrences[k]) for j in (0, 1)) for k in refs]
    rows = [solve([list(vertices[k]) + [F(1)] for k in refs], [p[j] for p in points]) for j in (0, 1)]
    projected = [tuple(dot(row, (*v, F(1))) for row in rows) for v in vertices]
    residual = max(dot(sub(projected[k], p), sub(projected[k], p)) for k in occurrences for p in occurrences[k])
    assert residual < F(1, 10000)
    q = cross(rows[0][:3], rows[1][:3])
    n0 = normal([vertices[k] for k in tiles[faces[0]['tiles'][0]]])
    if dot(n0, q) < 0:
        q = scale(q, -1)
    geometric, atoms = geometric_visibility(model, vertices, projected, q)
    printed, trace, rejected = printed_visibility(model, projected, relevant)
    assert geometric == printed, [(ed[k], geometric[k], printed[k]) for k in geometric if geometric[k] != printed[k]]
    junctions, lines = graph(model, projected, atoms)
    counts = dict(Counter(j['type'] for j in junctions))
    out = {'scope': 'Fig104(b): every final black interval agrees with exact visibility of the already certified book-coordinate Szilassi model.',
           'model': model, 'book_vertex_to_wireframe_vertex': mapping,
           'projection_rows': rows, 'view_direction_towards_camera': q,
           'maximum_original_point_residual_squared': residual,
           'junction_types': counts, 'junctions_total': len(junctions), 'lines': lines,
           'visible_physical_vertices': sorted(names[k] for j in junctions for k in j['physical_vertex']),
           'front_faces': [i for i, f in enumerate(faces) if dot(normal([vertices[k] for k in tiles[f['tiles'][0]]]), q) > 0],
           'fully_erased_auxiliary_segments': rejected,
           'visibility': [{'edge': ed[k], 'intervals': v} for k, v in geometric.items()],
           'printed_interval_trace': trace, 'junctions': junctions}
    (ROOT / 'results/szilassi-projection.json').write_text(json.dumps(out, indent=2, default=encode) + '\n')
    print(json.dumps({k: out[k] for k in ('scope', 'maximum_original_point_residual_squared', 'junction_types', 'junctions_total', 'lines', 'visible_physical_vertices', 'front_faces')}, indent=2, default=encode))


if __name__ == '__main__':
    main()
