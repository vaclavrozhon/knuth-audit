#!/usr/bin/env python3
"""Check every displayed mark in104(c), reusing its saved visibility proof."""
from collections import Counter, defaultdict
from fractions import Fraction as F
import json
import sys
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT, segments, cuts, at, winding, cross2, parameter
from check_polyhedra_fixed import sub, add, scale, dot, cross, normal, encode
from check_cubie_junctions import path_points


def main(which='clasp'):
    assert which in ('clasp', 'histoscape', 'szilassi')
    saved = json.loads((ROOT / ('results/' + which + '-projection.json')).read_text())
    m = (json.loads((ROOT / 'results/polyhedra-fixed.json').read_text())['Clasp']
         if which == 'clasp' else saved['model'])
    begin, end = {'clasp': (228, 282), 'histoscape': (282, 343), 'szilassi': (192, 228)}[which]
    vertices = [tuple(map(F, v)) for v in m['vertices']]
    rows = [[F(v) for v in row] for row in saved['projection_rows']]
    q = tuple(map(F, saved['view_direction_towards_camera']))
    project_vector = lambda v: tuple(dot(row[:3], v) for row in rows)
    projected = [tuple(dot(row, (*v, F(1))) for row in rows) for v in vertices]
    ed = [tuple(e) for e in m['edges']]
    visible = {tuple(a['edge']): [[F(s), F(t)] for s, t in a['intervals']] for a in saved['visibility']}
    faces = []
    for f in m['merged_faces']:
        n = normal([vertices[k] for k in m['convex_tiles'][f['tiles'][0]]])
        faces.append((n, f['boundary_cycles']))
    expected = {}
    for a, b in ed:
        front = []
        incident = []
        for fi, (n, cycles) in enumerate(faces):
            for cycle in cycles:
                if (a, b) in segments(cycle):
                    incident.append(fi)
                    if dot(n, q) > 0:
                        front.append((fi, 1))
                elif (b, a) in segments(cycle):
                    incident.append(fi)
                    if dot(n, q) > 0:
                        front.append((fi, -1))
        assert len(incident) == 2
        if len(front) == 2:
            kind = '+' if m['edge_signs'][str(tuple(sorted((a, b))))] == 'convex' else '-'
        elif len(front) == 1:
            fi, sign = front[0]
            u = sub(vertices[b], vertices[a])
            interior = scale(cross(faces[fi][0], u), sign)
            # PDF screen y points down: positive determinant puts the face right.
            kind = 'a>b' if cross2(project_vector(u), project_vector(interior)) > 0 else 'b>a'
        else:
            kind = 'back'
        expected[(a, b)] = {'label': kind, 'front_faces': [x[0] for x in front]}
        if visible[(a, b)]:
            assert kind != 'back'

    paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-026.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    fills = []
    for index in range(begin, end):
        p = paths[index]
        if p.get('fill') != 'rgb(100%, 100%, 100%)':
            continue
        mapped = []
        for point in path_points(p):
            k = min(range(len(vertices)), key=lambda k: dot(sub(projected[k], point), sub(projected[k], point)))
            assert dot(sub(projected[k], point), sub(projected[k], point)) < F(1, 10000)
            mapped.append(projected[k])
        fills.append((index, mapped))

    checked = []
    hidden_marks = []
    covered_edges = set()
    disagreements = []
    for index in range(begin, end):
        p = paths[index]
        if p.get('stroke') not in ('rgb(100%, 0%, 0%)', 'rgb(100%, 100%, 100%)'):
            continue
        z = path_points(p)
        assert len(z) in (2, 3)
        arrow = len(z) == 3
        minus = p.get('stroke') == 'rgb(100%, 100%, 100%)'
        center = z[1] if arrow else scale(add(z[0], z[1]), F(1, 2))
        mark_direction = sub(z[1], scale(add(z[0], z[2]), F(1, 2))) if arrow else sub(z[1], z[0])
        candidates = []
        for a, b in ed:
            u = sub(projected[b], projected[a])
            t = dot(sub(center, projected[a]), u) / dot(u, u)
            if not 0 < t < 1:
                continue
            distance = cross2(sub(center, projected[a]), u) ** 2 / dot(u, u)
            angle = (cross2(mark_direction, u) if arrow or minus else dot(mark_direction, u)) ** 2 / (dot(mark_direction, mark_direction) * dot(u, u))
            if distance < F(1, 10000) and angle < F(1, 100000):
                candidates.append(((a, b), t, distance))
        assert len(candidates) == 1, (index, candidates)
        edge, t, distance = candidates[0]
        u = sub(projected[edge[1]], projected[edge[0]])
        label = ('a>b' if dot(mark_direction, u) > 0 else 'b>a') if arrow else ('-' if minus else '+')
        # Decide whether the whole glyph is erased by later white faces; its
        # two sides may be partly visible even when its tip lies behind a face.
        remaining_length_squared = F(0)
        for a, b in zip(z, z[1:]):
            partition = {F(0), F(1)}
            later = [poly for j, poly in fills if j > index]
            for poly in later:
                for c, d in segments(poly):
                    partition.update(cuts(a, b, c, d))
            partition = sorted(partition)
            for s, t1 in zip(partition, partition[1:]):
                if not any(winding(at(a, b, (s + t1) / 2), poly) for poly in later):
                    remaining_length_squared += (t1 - s) ** 2 * dot(sub(b, a), sub(b, a))
        if remaining_length_squared <= F(1, 10000):
            hidden_marks.append(index)
            continue
        if label != expected[edge]['label']:
            disagreements.append({'path': index, 'edge': edge, 'printed': label,
                                  'model': expected[edge]['label']})
        checked.append({'path': index, 'edge': edge, 'label': label,
                        'anchor_parameter': t, 'anchor_distance_squared': distance,
                        'remaining_segment_length_squares_sum': remaining_length_squared})
        covered_edges.add(edge)
    visible_edges = {edge for edge in ed if visible[edge]}
    # Tiny exposed portions can have no surviving tick: report them explicitly.
    unmarked = sorted(visible_edges - covered_edges)
    out = {'scope': 'Compare every surviving mark in Fig104(' + {'clasp': 'c', 'histoscape': 'd', 'szilassi': 'b'}[which] + ') with its fixed3D model. Saved visibility reused. Disagreements are not declared book errors without resolving the drawing interpretation.',
           'checked_marks': len(checked), 'fully_hidden_marks': hidden_marks,
           'visible_edge_labels': [{'edge': edge, **expected[edge]} for edge in ed if edge in visible_edges],
           'visible_physical_edges_with_no_surviving_mark': unmarked,
           'model_disagreements': disagreements,
           'marks': checked}
    (ROOT / ('results/' + which + '-labels.json')).write_text(json.dumps(out, indent=2, default=encode) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k not in ('visible_edge_labels', 'marks')}, indent=2))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'clasp')
