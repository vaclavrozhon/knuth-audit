#!/usr/bin/env python3
"""All original paths and marks in the three alternatives(23)."""
from fractions import Fraction as F
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT, solve, printed_visibility, segments, cuts, at, winding, cross2
from check_cubie_junctions import path_points
from check_polyhedra_fixed import sub, add, scale, dot, encode


def main():
    pic = json.loads((ROOT / 'results/histoscape-projection.json').read_text())
    base_labels = json.loads((ROOT / 'results/histoscape-labels.json').read_text())
    csp = json.loads((ROOT / 'results/line-csp22.json').read_text())
    source = [p.attrib for p in ET.parse(ROOT / 'sources/file-026.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-028.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    model = pic['model']
    vs = [tuple(map(F, p)) for p in model['vertices']]
    rows = [tuple(map(F, r)) for r in pic['projection_rows']]
    projected = [tuple(dot(row, (*v, F(1))) for row in rows) for v in vs]
    base_visible = {tuple(r['edge']): [(F(s), F(t)) for s, t in r['intervals']] for r in pic['visibility']}
    old_labels = {tuple(r['edge']): r['label'] for r in base_labels['visible_edge_labels']}
    out = []
    for begin in (18, 79, 140):
        # All61 paths have exactly the same structural order as104(d).
        # Labels may differ; geometry is checked without using label equality.
        # Spread the three references over the whole drawing; using the thin
        # top parallelogram would amplify subpixel rounding at the bottom.
        refs = [319, 307, 291]
        ref_old = [path_points(source[i])[0] for i in refs]
        ref_new = [path_points(paths[begin + i - 282])[0] for i in refs]
        affine = [solve([list(p) + [F(1)] for p in ref_old], [p[j] for p in ref_new]) for j in (0, 1)]
        assert cross2(affine[0][:2], affine[1][:2]) > 0
        points = [tuple(dot(row, (*v, F(1))) for row in affine) for v in projected]
        relevant, fills = {}, []
        max_residual = F(0)
        for offset in range(61):
            p, old = paths[begin + offset], source[282 + offset]
            if old.get('stroke') == 'rgb(0%, 0%, 0%)' or old.get('fill') == 'rgb(100%, 100%, 100%)':
                assert p.get('stroke') == old.get('stroke') and p.get('fill') == old.get('fill')
                a, b = path_points(old), path_points(p)
                assert len(a) == len(b)
                ds = []
                for u, v in zip(a, b):
                    predicted = tuple(dot(row, (*u, F(1))) for row in affine)
                    ds.append(dot(sub(predicted, v), sub(predicted, v)))
                assert max(ds) < F(1, 2500), (begin, offset, max(ds))
                max_residual = max(max_residual, max(ds))
                # Both the geometry clipping and glyph visibility use every
                # actual white polygon, with each vertex uniquely identified.
                mapped = []
                for v in b:
                    ds = [dot(sub(v, q), sub(v, q)) for q in points]
                    k = min(range(len(vs)), key=ds.__getitem__)
                    assert ds[k] < F(1, 2500) and sorted(ds)[1] > F(1, 4)
                    mapped.append(k)
                if p.get('fill') == 'rgb(100%, 100%, 100%)':
                    fills.append((begin + offset, [points[k] for k in mapped]))
                relevant[begin + offset] = {'path': p, 'vertices': mapped}
        actual_visible, trace, rejected = printed_visibility(model, points, relevant)
        assert all(actual_visible[k] == [list(pair) for pair in base_visible[tuple(e)]]
                   for k, e in enumerate(model['edges']))

        checked, hidden, labels = [], [], {}
        for index in range(begin, begin + 61):
            p = paths[index]
            if p.get('stroke') not in ('rgb(100%, 0%, 0%)', 'rgb(100%, 100%, 100%)'):
                continue
            z = path_points(p)
            assert len(z) in (2, 3)
            arrow = len(z) == 3
            minus = p.get('stroke') == 'rgb(100%, 100%, 100%)'
            center = z[1] if arrow else scale(add(z[0], z[1]), F(1, 2))
            direction = sub(z[1], scale(add(z[0], z[2]), F(1, 2))) if arrow else sub(z[1], z[0])
            candidates = []
            for a, b in model['edges']:
                u = sub(points[b], points[a])
                t = dot(sub(center, points[a]), u) / dot(u, u)
                if not 0 < t < 1:
                    continue
                dist = cross2(sub(center, points[a]), u) ** 2 / dot(u, u)
                angle = (cross2(direction, u) if arrow or minus else dot(direction, u)) ** 2 / (dot(direction, direction) * dot(u, u))
                if dist < F(1, 2500) and angle < F(1, 100000):
                    candidates.append(((a, b), t, dist))
            assert len(candidates) == 1, (index, candidates)
            edge, t, dist = candidates[0]
            u = sub(points[edge[1]], points[edge[0]])
            label = ('a>b' if dot(direction, u) > 0 else 'b>a') if arrow else ('-' if minus else '+')
            remaining = F(0)
            for a, b in zip(z, z[1:]):
                partition = {F(0), F(1)}
                later = [poly for j, poly in fills if j > index]
                for poly in later:
                    for c, d in segments(poly):
                        partition.update(cuts(a, b, c, d))
                partition = sorted(partition)
                for s, t1 in zip(partition, partition[1:]):
                    if not any(winding(at(a, b, (s + t1) / 2), poly) for poly in later):
                        remaining += (t1 - s) ** 2 * dot(sub(b, a), sub(b, a))
            if remaining <= F(1, 10000):
                hidden.append(index)
                continue
            assert edge not in labels or labels[edge] == label, (index, edge, labels.get(edge), label)
            labels[edge] = label
            checked.append({'path': index, 'edge': edge, 'label': label,
                            'distance_squared': dist, 'remaining_segment_length_squares_sum': remaining})
        assert set(labels) == {e for e in base_visible if base_visible[e]}
        assignment = {}
        for row in csp['physical_line_correspondence']:
            e = tuple(row['physical_edge'])
            new = labels[e]
            if new in '+-':
                assignment[row['line']] = new
            else:
                assert old_labels[e] in ('a>b', 'b>a') and row['label'] in '<>'
                assignment[row['line']] = row['label'] if new == old_labels[e] else ('<' if row['label'] == '>' else '>')
        assert assignment in csp['solutions']
        out.append({'paths': [begin, begin + 60], 'geometry_matches_full_visible_intervals': True,
                    'maximum_geometry_residual_squared': max_residual,
                    'marks': checked, 'fully_hidden_marks': hidden,
                    'solution_index': csp['solutions'].index(assignment), 'line_labels': assignment,
                    'changed_lines_from104d': {v: [csp['physical104d_solution'][v], value] for v, value in assignment.items() if value != csp['physical104d_solution'][v]}})
    assert [x['solution_index'] for x in out] == [2, 1, 0]
    (ROOT / 'results/line-fig23.json').write_text(json.dumps({'scope': 'Every original geometric path and every surviving mark in all three diagrams(23), with complete26-line assignments.', 'figures': out}, indent=2, default=encode) + '\n')
    print(json.dumps([{'paths': x['paths'], 'marks': len(x['marks']), 'hidden': x['fully_hidden_marks'], 'solution_index': x['solution_index'], 'changed_lines': x['changed_lines_from104d']} for x in out], indent=2))


if __name__ == '__main__':
    main()
