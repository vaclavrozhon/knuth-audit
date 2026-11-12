#!/usr/bin/env python3
"""Read the sphinx HC picture directly, without assuming its public3D model."""
from collections import defaultdict, Counter
from fractions import Fraction as F
import json
import re
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT, solve, printed_visibility, graph, segments, cuts, at, winding, cross2, parameter
from check_cubie_junctions import path_points
from check_polyhedra_fixed import sub, add, scale, dot, encode
from check_hc_picture_networks import ordered_neighbors, face_walks
from check_line_csp22 import TABLE, global_symbol, propagate, ORDER


def geometry():
    wire = json.loads((ROOT / 'results/figure102-vectors.json').read_text())['a']
    base = [tuple(map(F, p)) for p in wire['vertices']]
    model = {'edges': wire['edges']}
    paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-026.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    relevant, occurrences = {}, defaultdict(list)
    predicted = [add(p, (F('33.25'), F('-.04'))) for p in base]
    for index in range(18, 192):
        p = paths[index]
        if p.get('stroke') != 'rgb(0%, 0%, 0%)' and p.get('fill') != 'rgb(100%, 100%, 100%)':
            continue
        mapped = []
        for q in path_points(p):
            ds = [dot(sub(q, v), sub(q, v)) for v in predicted]
            k = min(range(len(base)), key=ds.__getitem__)
            assert ds[k] < F(1, 100) and sorted(ds)[1] > 9 * ds[k], (index, q, k, float(ds[k]))
            mapped.append(k)
            occurrences[k].append(q)
        relevant[index] = {'path': p, 'vertices': mapped}
    refs = [26, 61, 34]
    means = [tuple(sum(p[j] for p in occurrences[k]) / len(occurrences[k]) for j in (0, 1)) for k in refs]
    affine = [solve([list(base[k]) + [F(1)] for k in refs], [p[j] for p in means]) for j in (0, 1)]
    assert cross2(affine[0][:2], affine[1][:2]) > 0
    points = [tuple(dot(row, (*p, F(1))) for row in affine) for p in base]
    residual = max(dot(sub(points[k], q), sub(points[k], q)) for k, ps in occurrences.items() for q in ps)
    assert residual < F(1, 2500), float(residual)
    visible, trace, auxiliary = printed_visibility(model, points, relevant)
    atoms = []
    for ei, (a, b) in enumerate(model['edges']):
        allcuts = {F(0), F(1)}
        for c, d in model['edges']:
            if (a, b) != (c, d):
                allcuts.update(cuts(points[a], points[b], points[c], points[d]))
        for s, t in visible[ei]:
            partition = sorted({s, t} | {u for u in allcuts if s < u < t})
            atoms.extend((ei, u, v) for u, v in zip(partition, partition[1:]))
    junctions, line_count = graph(model, points, atoms)
    jp = {'j%02d' % i: tuple(j['point']) for i, j in enumerate(junctions)}
    adjacency, lines = defaultdict(dict), {}
    for ei, (a, b) in enumerate(model['edges']):
        for s, t in visible[ei]:
            along = []
            for name, q in jp.items():
                if cross2(sub(q, points[a]), sub(points[b], points[a])) == 0:
                    z = parameter(q, points[a], points[b])
                    if s <= z <= t:
                        along.append((z, name))
            along.sort()
            assert along[0][0] == s and along[-1][0] == t
            for (u, j), (v, k) in zip(along, along[1:]):
                assert k not in adjacency[j]
                adjacency[j][k] = adjacency[k][j] = ei
                name = '_'.join(sorted((j, k)))
                lines[name] = {'physical_edge': [a, b], 'interval': [u, v],
                               'along_physical_edge': [j, k]}
    assert len(lines) == line_count
    network, relations = {}, {}
    for i, original in enumerate(junctions):
        j = 'j%02d' % i
        kind = original['type']
        ns = ordered_neighbors(j, kind, adjacency[j], jp)
        vs = ['_'.join(sorted((j, k))) for k in ns]
        ts = [''.join(global_symbol(s, j, k) for s, k in zip(row, ns)) for row in TABLE[kind]]
        network[j] = {'type': kind, 'neighbors': ns}
        relations[j] = {'variables': vs, 'tuples': ts}
    fills = [(i, [points[k] for k in item['vertices']]) for i, item in relevant.items() if item['path'].get('fill') == 'rgb(100%, 100%, 100%)']
    # Persist the newly completed geometric block before analyzing all glyphs.
    (ROOT / 'results/sphinx-native-geometry.json').write_text(json.dumps({
        'affine': affine, 'residual': residual, 'points': points, 'model': model,
        'relevant': relevant, 'visible': visible, 'trace': trace, 'auxiliary': auxiliary,
        'junctions': junctions, 'line_count': line_count, 'jp': jp,
        'adjacency': dict(adjacency), 'lines': lines, 'network': network,
        'relations': relations, 'fills': fills}, indent=2, default=encode) + '\n')


def decode(value):
    if isinstance(value, list):
        return [decode(v) for v in value]
    if isinstance(value, dict):
        return {(int(k) if k.isdigit() else k): decode(v) for k, v in value.items()}
    if isinstance(value, str) and re.fullmatch(r'-?\d+/\d+', value):
        return F(value)
    return value


def main():
    cache = ROOT / 'results/sphinx-native-geometry.json'
    if not cache.exists():
        geometry()
    data = decode(json.loads(cache.read_text()))
    affine, residual, points, model, relevant, visible, trace, auxiliary, junctions, line_count, jp, adjacency, lines, network, relations, fills = (
        data[k] for k in ['affine', 'residual', 'points', 'model', 'relevant', 'visible', 'trace', 'auxiliary', 'junctions', 'line_count', 'jp', 'adjacency', 'lines', 'network', 'relations', 'fills'])
    paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-026.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    marks, hidden, actual = [], [], {}
    for index in range(18, 192):
        p = paths[index]
        if p.get('stroke') not in ('rgb(100%, 0%, 0%)', 'rgb(100%, 100%, 100%)'):
            continue
        z = path_points(p)
        assert len(z) in (2, 3)
        arrow = len(z) == 3
        minus = p.get('stroke') == 'rgb(100%, 100%, 100%)'
        center = z[1] if arrow else scale(add(z[0], z[1]), F(1, 2))
        direction = sub(z[1], scale(add(z[0], z[2]), F(1, 2))) if arrow else sub(z[1], z[0])
        remainder = F(0)
        for a, b in zip(z, z[1:]):
            partition = {F(0), F(1)}
            later = [poly for j, poly in fills if j > index]
            for poly in later:
                for c, d in segments(poly):
                    partition.update(cuts(a, b, c, d))
            partition = sorted(partition)
            for s, t in zip(partition, partition[1:]):
                if not any(winding(at(a, b, (s + t) / 2), poly) for poly in later):
                    remainder += (t - s) ** 2 * dot(sub(b, a), sub(b, a))
        if remainder <= F(1, 10000):
            hidden.append(index)
            continue
        candidates = []
        for name, line in lines.items():
            j, k = name.split('_')
            u = sub(jp[k], jp[j])
            t = dot(sub(center, jp[j]), u) / dot(u, u)
            if not 0 < t < 1:
                # A glyph can have its center/tip hidden while a tail remains
                # on a positive visible part of its line (e.g.paths24,31).
                projected_glyph = [dot(sub(q, jp[j]), u) / dot(u, u) for q in z]
                if max(F(0), min(projected_glyph)) >= min(F(1), max(projected_glyph)):
                    continue
            distance = cross2(sub(center, jp[j]), u) ** 2 / dot(u, u)
            angle = (cross2(direction, u) if arrow or minus else dot(direction, u)) ** 2 / (dot(direction, direction) * dot(u, u))
            if distance < F(1, 2500) and angle < F(1, 100000):
                candidates.append((name, u, distance, t))
        # A single glyph can cross a T bar junction. Its visible tip/center
        # identifies its own line; the T relation subsequently transports
        # the bar label to the other collinear line. Only when the anchor
        # itself has been hidden do we use the surviving-tail overlap.
        anchored = [c for c in candidates if 0 < c[3] < 1]
        if anchored:
            candidates = anchored
        assert len(candidates) == 1, (index, candidates, float(remainder))
        name, u, distance, anchor_parameter = candidates[0]
        label = ('>' if dot(direction, u) > 0 else '<') if arrow else ('-' if minus else '+')
        assert name not in actual or actual[name] == label, (index, name, actual.get(name), label)
        actual[name] = label
        marks.append({'path': index, 'line': name, 'label': label, 'anchor_distance_squared': distance,
                      'anchor_parameter_on_visible_line': anchor_parameter,
                      'remaining_segment_length_squares_sum': remainder})
    faces, boundary = face_walks(jp, adjacency)
    boundary_lines = []
    for j, k in zip(boundary, boundary[1:] + boundary[:1]):
        name = '_'.join(sorted((j, k)))
        wanted = '>' if j < k else '<'
        assert name not in actual or actual[name] == wanted, (name, actual.get(name), wanted)
        boundary_lines.append({'from': j, 'to': k, 'variable': name, 'label': wanted})
    relation_pairs = {j: (r['variables'], r['tuples']) for j, r in relations.items()}
    completion, propagation = propagate(relation_pairs, {name: {actual[name]} if name in actual else set(ORDER) for name in lines})
    assert completion is not None
    (ROOT / 'results/sphinx-native-mark-analysis.json').write_text(json.dumps({
        'marks': marks, 'fully_hidden_marks': hidden, 'explicitly_marked_lines': actual,
        'boundary': boundary, 'boundary_lines': boundary_lines,
        'remaining_domains': {e: ''.join(v for v in ORDER if v in ds) for e, ds in completion.items()},
        'propagation': propagation}, indent=2, default=encode) + '\n')
    # Several very short boundary fragments have no surviving glyph. The
    # displayed labels leave two of those fragments undetermined. Record
    # that fact above; the claim checked here is the standard completion
    # of the displayed labeling, so impose its defining clockwise arrows.
    unmarked_boundary = [b['variable'] for b in boundary_lines if b['variable'] not in actual]
    for b in boundary_lines:
        completion[b['variable']] &= {b['label']}
    completion, boundary_propagation = propagate(relation_pairs, completion)
    assert completion is not None
    assert all(len(v) == 1 for v in completion.values()), {
        e: (''.join(v for v in ORDER if v in ds), lines[e])
        for e, ds in completion.items() if len(ds) > 1}
    solution = {k: next(iter(v)) for k, v in completion.items()}
    assert all(''.join(solution[e] for e in es) in ts for es, ts in relation_pairs.values())
    assert all(solution[b['variable']] == b['label'] for b in boundary_lines)
    out = {'scope': 'Only the native2D sphinx HC geometry and the unique standard completion of all displayed marks. Short unmarked boundary fragments are explicitly completed clockwise. No3D realization or public-model identity is inferred.',
           'wireframe_to_picture_affine': affine, 'maximum_point_residual_squared': residual,
           'original_path_vertices': {i: r['vertices'] for i, r in relevant.items()},
           'wireframe_vertex_points': points, 'visible_intervals': [{'edge': e, 'intervals': visible[i]} for i, e in enumerate(model['edges'])],
           'paint_trace': trace, 'erased_auxiliary_segments': auxiliary,
           'junctions': junctions, 'points': jp, 'network': network, 'relations': relations,
           'lines': lines, 'line_count': len(lines), 'junction_types': dict(Counter(r['type'] for r in network.values())),
           'faces': faces, 'boundary': boundary, 'boundary_lines': boundary_lines,
           'marks': marks, 'fully_hidden_marks': hidden, 'explicitly_marked_lines': actual,
           'unmarked_lines': sorted(set(lines) - set(actual)),
           'printed_labeling_completion': solution, 'completion_propagation': propagation,
           'unmarked_boundary_lines_completed_clockwise': unmarked_boundary,
           'boundary_completion_propagation': boundary_propagation}
    (ROOT / 'results/sphinx-native-network.json').write_text(json.dumps(out, indent=2, default=encode) + '\n')
    print(json.dumps({'junction_types': out['junction_types'], 'lines': len(lines), 'marks': len(marks),
                      'hidden_marks': hidden, 'boundary_length': len(boundary),
                      'unmarked_lines': out['unmarked_lines'], 'maximum_residual_squared': str(residual)}, indent=2))


if __name__ == '__main__':
    main()
