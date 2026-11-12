#!/usr/bin/env python3
"""Native Reutersvaerd26 and both locally valid but nonplanar-face pictures27."""
from collections import defaultdict, Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import prod
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT, path_segments, cross2, dot, sub, cuts, at, winding
from check_cubie_junctions import path_points
from check_polyhedra_fixed import encode
from check_hc_picture_networks import ordered_neighbors, face_walks
from check_line_csp22 import TABLE, global_symbol, propagate, ORDER


def network(mapped, paths):
    segments = [ab for i, qs in mapped.items() for ab in path_segments(paths[i], qs)]
    split = []
    for a, b in segments:
        partition = {F(0), F(1)}
        for c, d in segments:
            partition.update(cuts(a, b, c, d))
        partition = sorted(partition)
        split.extend((at(a, b, s), at(a, b, t)) for s, t in zip(partition, partition[1:]))
    points = {'v%02d' % i: p for i, p in enumerate(sorted({p for ab in split for p in ab}))}
    names = {p: j for j, p in points.items()}
    adjacency = defaultdict(set)
    for a, b in split:
        u, v = names[a], names[b]
        adjacency[u].add(v); adjacency[v].add(u)
    ns, rs = {}, {}
    for j, neighbors in adjacency.items():
        assert len(neighbors) in (2, 3), (j, points[j], neighbors)
        rays = [sub(points[k], points[j]) for k in neighbors]
        if len(neighbors) == 2:
            assert cross2(*rays), (j, rays)
            kind = 'V'
        elif any(cross2(a, b) == 0 and dot(a, b) < 0 for a, b in combinations(rays, 2)):
            kind = 'T'
        elif any(cross2(p[0], p[1]) > 0 and cross2(p[1], p[2]) > 0 and cross2(p[0], p[2]) > 0 for p in permutations(rays)):
            kind = 'W'
        else:
            kind = 'Y'
        ordered = ordered_neighbors(j, kind, neighbors, points)
        vs = ['_'.join(sorted((j, k))) for k in ordered]
        ts = [''.join(global_symbol(s, j, k) for s, k in zip(t, ordered)) for t in TABLE[kind]]
        ns[j] = {'type': kind, 'neighbors': ordered}
        rs[j] = (vs, ts)
    lines = sorted({'_'.join(sorted((j, k))) for j, others in adjacency.items() for k in others})
    faces, boundary = face_walks(points, adjacency)
    return points, ns, rs, lines, faces, boundary


def main():
    paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-029.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    out = []
    for tag, start, stop, width_units in [('26', 47, 66, None), ('27-left', 66, 73, 41), ('27-right', 73, 78, 33)]:
        original = {i: path_points(paths[i]) for i in range(start, stop)}
        allpoints = [p for qs in original.values() for p in qs]
        maps, errors, transform = {}, [], None
        if tag == '26':
            left = [p for p in allpoints if p[0] < 200]
            right = [p for p in allpoints if p[0] > 200]
            lx, ly = min(p[0] for p in left), min(p[1] for p in left)
            rx, ry = min(p[0] for p in right), min(p[1] for p in right)
            ux = (max(p[0] for p in left) - lx) / 5
            uy = (F('439.828125') - ly) / 8
            ur = (max(p[1] for p in right) - ry) / 32
            transform = {'left_origin': [lx, ly], 'left_units': [ux, uy],
                         'right_origin': [rx, ry], 'right_unit': ur}
            for i, qs in original.items():
                maps[i] = []
                for p in qs:
                    x0, y0, sx, sy = (lx, ly, ux, uy) if p[0] < 200 else (rx, ry, ur, ur)
                    grid = (round((p[0] - x0) / sx), round((p[1] - y0) / sy))
                    q = (x0 + sx * grid[0], y0 + sy * grid[1])
                    errors.append(dot(sub(p, q), sub(p, q)))
                    maps[i].append(q)
        else:
            origin = tuple(min(p[k] for p in allpoints) for k in (0, 1))
            units = ((max(p[0] for p in allpoints) - origin[0]) / width_units,
                     (max(p[1] for p in allpoints) - origin[1]) / 5)
            transform = {'origin': origin, 'units': units}
            for i, qs in original.items():
                maps[i] = []
                for p in qs:
                    q = tuple(F(round((p[k] - origin[k]) / units[k])) for k in (0, 1))
                    errors.append(sum((p[k] - origin[k] - units[k] * q[k]) ** 2 for k in (0, 1)))
                    maps[i].append(q)
        assert max(errors) < F(1, 10000), (tag, float(max(errors)))
        points, ns, rs, lines, faces, boundary = network(maps, paths)
        row = {'picture': tag, 'source_path_range_half_open': [start, stop],
               'source_transform': transform, 'maximum_source_residual_squared': max(errors),
               'source_path_canonical_vertices': maps, 'points': points, 'junctions': ns,
               'relations': rs, 'lines': lines, 'faces': faces, 'boundary': boundary}
        ds = {e: set(ORDER) for e in lines}
        if tag == '26':
            solution, trace = propagate(rs, ds)
            assert solution is None
            row['unlabelability_propagation'] = trace
        else:
            for u, v in zip(boundary, boundary[1:] + boundary[:1]):
                ds['_'.join(sorted((u, v)))] = {'>' if u < v else '<'}
            solution, trace = propagate(rs, ds)
            assert solution is not None
            assert prod(len(d) for d in solution.values()) <= 16
            assignments = []
            for values in product(*[''.join(s for s in ORDER if s in solution[e]) for e in lines]):
                witness = dict(zip(lines, values))
                if all(''.join(witness[v] for v in vs) in ts for vs, ts in rs.values()):
                    assignments.append(witness)
            assert assignments
            row['standard_labelings'] = assignments
            row['propagated_standard_domains'] = {e: ''.join(s for s in ORDER if s in d) for e, d in solution.items()}
            row['standard_labeling_propagation'] = trace
            common = []
            for i, f in enumerate(faces):
                if f['area_twice'] > 0:
                    continue
                edges_f = {'_'.join(sorted((u, v))) for u, v in zip(f['walk'], f['walk'][1:] + f['walk'][:1])}
                for j in range(i + 1, len(faces)):
                    g = faces[j]
                    if g['area_twice'] > 0:
                        continue
                    edges_g = {'_'.join(sorted((u, v))) for u, v in zip(g['walk'], g['walk'][1:] + g['walk'][:1])}
                    shared = sorted(edges_f & edges_g)
                    directed_f = {'_'.join(sorted((u, v))): (u, v) for u, v in zip(f['walk'], f['walk'][1:] + f['walk'][:1])}
                    forced_creases = [e for e in shared if all(witness[e] in '+-' for witness in assignments)]
                    for first, second in combinations(forced_creases, 2):
                        a, b = [points[k] for k in first.split('_')]
                        if any(cross2(sub(points[k], a), sub(b, a)) != 0 for k in second.split('_')):
                            common.append({'faces': [i, j], 'type': 'two_distinct_shared_crease_lines',
                                           'crease_lines': [first, second],
                                           'crease_labels_for_each_standard_labeling': [[witness[e] for e in (first, second)] for witness in assignments]})
                    for crease in shared:
                        if not all(witness[crease] in '+-' for witness in assignments):
                            continue
                        ca, cb = [points[k] for k in directed_f[crease]]
                        for arrow in shared:
                            if not all(witness[arrow] in '<>' for witness in assignments):
                                continue
                            aa, ab = [points[k] for k in arrow.split('_')]
                            mid = tuple((x + y) / 2 for x, y in zip(aa, ab))
                            h = cross2(sub(cb, ca), sub(mid, ca))
                            if h == 0:
                                continue
                            cases = []
                            for witness in assignments:
                                # Bounded face f runs with its interior to its
                                # algebraic left (negative cross in PDF coords).
                                # A convex crease gives d=z_f-z_g=-positive*h;
                                # concavity gives d=positive*h.
                                predicted = (1 if h > 0 else -1) * (-1 if witness[crease] == '+' else 1)
                                direction = arrow.split('_')
                                if witness[arrow] == '<':
                                    direction.reverse()
                                f_front = tuple(direction) != directed_f[arrow]
                                required = -1 if f_front else 1
                                cases.append({'crease_label': witness[crease], 'arrow_label': witness[arrow],
                                              'predicted_sign_z_f_minus_z_g': predicted,
                                              'required_sign_z_f_minus_z_g': required})
                            if all(c['predicted_sign_z_f_minus_z_g'] != c['required_sign_z_f_minus_z_g'] for c in cases):
                                common.append({'faces': [i, j], 'type': 'crease_vs_occlusion_depth_order', 'shared_crease': crease,
                                               'shared_occlusion_edge': arrow, 'h_at_arrow_midpoint': h,
                                               'all_standard_labeling_obstructions': cases})
            (ROOT / ('results/hc-drawing-' + tag + '-analysis.json')).write_text(json.dumps(row, indent=2, default=encode) + '\n')
            assert common, (tag, common)
            row['plane_order_obstructions'] = common
        out.append(row)
    (ROOT / 'results/hc-drawings26-27.json').write_text(json.dumps({'pictures': out}, indent=2, default=encode) + '\n')
    print(json.dumps([{'picture': x['picture'], 'junction_types': dict(Counter(j['type'] for j in x['junctions'].values())),
                      'lines': len(x['lines']), 'contradiction': x.get('unlabelability_propagation', [None])[-1],
                      'plane_order_obstructions': x.get('plane_order_obstructions'),
                      'standard_labelings': len(x.get('standard_labelings', []))} for x in out], indent=2, default=encode))


if __name__ == '__main__':
    main()
