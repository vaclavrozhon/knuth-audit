#!/usr/bin/env python3
"""Recover exact HC networks from saved projections; certify boundary/45."""
from collections import defaultdict
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import permutations
import json
from check_clasp_projection import ROOT, cross2, parameter
from check_polyhedra_fixed import sub, dot, encode
from check_line_csp22 import TABLE, global_symbol


def angular_compare(a, b):
    # PDF coordinates: positive determinant means clockwise rotation<pi.
    ha = 0 if a[1] > 0 or (a[1] == 0 and a[0] >= 0) else 1
    hb = 0 if b[1] > 0 or (b[1] == 0 and b[0] >= 0) else 1
    if ha != hb:
        return -1 if ha < hb else 1
    c = cross2(a, b)
    assert c != 0, ('duplicate outgoing ray', a, b)
    return -1 if c > 0 else 1


def face_walks(points, adjacency):
    clockwise = {}
    for v, ns in adjacency.items():
        clockwise[v] = sorted(ns, key=cmp_to_key(lambda a, b: angular_compare(sub(points[a], points[v]), sub(points[b], points[v]))))
    successor = {}
    for v, ns in clockwise.items():
        for i, u in enumerate(ns):
            successor[u, v] = (v, ns[(i + 1) % len(ns)])
    remaining = set(successor)
    faces = []
    while remaining:
        start = min(remaining)
        walk, current = [], start
        while current in remaining:
            remaining.remove(current)
            walk.append(current[0])
            current = successor[current]
        assert current == start
        area2 = sum(cross2(points[a], points[b]) for a, b in zip(walk, walk[1:] + walk[:1]))
        faces.append({'walk': walk, 'area_twice': area2})
    outer = [f for f in faces if f['area_twice'] > 0]
    assert len(outer) == 1
    return faces, outer[0]['walk']


def ordered_neighbors(j, kind, ns, points):
    if kind == 'Y':
        a = min(ns)
        rest = sorted(set(ns) - {a})
        possibilities = [(a, *p) for p in permutations(rest)]
    else:
        possibilities = list(permutations(ns))
    legal = []
    for p in possibilities:
        rays = [sub(points[k], points[j]) for k in p]
        if kind == 'V':
            ok = cross2(*rays) > 0
        elif kind == 'W':
            ok = all(cross2(rays[a], rays[b]) > 0 for a, b in [(0, 1), (1, 2), (0, 2)])
        elif kind == 'Y':
            ok = all(cross2(rays[i], rays[(i + 1) % 3]) > 0 for i in range(3))
        else:
            assert kind == 'T'
            ok = cross2(rays[0], rays[2]) == 0 and dot(rays[0], rays[2]) < 0 and cross2(rays[0], rays[1]) < 0 and cross2(rays[1], rays[2]) < 0
        if ok:
            legal.append(p)
    assert len(legal) == 1, (j, kind, legal)
    return legal[0]


def build(which):
    pic = json.loads((ROOT / ('results/' + which + '-projection.json')).read_text())
    lab = json.loads((ROOT / ('results/' + which + '-labels.json')).read_text())
    model = (json.loads((ROOT / 'results/polyhedra-fixed.json').read_text())['Clasp']
             if which == 'clasp' else pic['model'])
    vertices = [tuple(map(F, p)) for p in model['vertices']]
    rows = [tuple(map(F, r)) for r in pic['projection_rows']]
    projected = [tuple(dot(row, (*v, F(1))) for row in rows) for v in vertices]
    points = {'j%02d' % i: tuple(map(F, r['point'])) for i, r in enumerate(pic['junctions'])}
    junctions = {'j%02d' % i: r for i, r in enumerate(pic['junctions'])}
    adjacency = defaultdict(dict)
    segments = []
    for row in pic['visibility']:
        a, b = row['edge']
        for s, t in row['intervals']:
            s, t = F(s), F(t)
            along = []
            for j, p in points.items():
                if cross2(sub(p, projected[a]), sub(projected[b], projected[a])) == 0:
                    k = parameter(p, projected[a], projected[b])
                    if s <= k <= t:
                        along.append((k, j))
            along.sort()
            assert along[0][0] == s and along[-1][0] == t
            for (_, u), (_, v) in zip(along, along[1:]):
                assert v not in adjacency[u]
                adjacency[u][v] = adjacency[v][u] = (a, b)
                segments.append({'ends': sorted((u, v)), 'physical_edge': [a, b]})
    assert len(segments) == pic['lines'] and len(adjacency) == pic['junctions_total']
    network, relations = {}, {}
    for j in points:
        kind = junctions[j]['type']
        neighbors = ordered_neighbors(j, kind, adjacency[j], points)
        vs = ['_'.join(sorted((j, k))) for k in neighbors]
        ts = [''.join(global_symbol(s, j, k) for s, k in zip(t, neighbors)) for t in TABLE[kind]]
        network[j] = {'type': kind, 'neighbors': neighbors}
        relations[j] = {'variables': vs, 'tuples': ts}
    expected = {tuple(x['edge']): x['label'] for x in lab['visible_edge_labels']}
    actual = {}
    for mark in lab['marks']:
        edge = tuple(mark['edge'])
        assert edge not in actual or actual[edge] == mark['label']
        actual[edge] = mark['label']
    unmarked = set(expected) - set(actual)

    def assignment(labels):
        output = {}
        for s in segments:
            u, v = s['ends']
            a, b = s['physical_edge']
            value = labels[a, b]
            if value not in '+-':
                delta = parameter(points[v], projected[a], projected[b]) - parameter(points[u], projected[a], projected[b])
                value = '>' if (delta > 0) == (value == 'a>b') else '<'
            output[u + '_' + v] = value
        return output

    physical = assignment(expected)
    printed = assignment({**expected, **actual})
    for labeling in [physical, printed]:
        assert all(''.join(labeling[v] for v in r['variables']) in r['tuples'] for r in relations.values())
    faces, boundary = face_walks(points, adjacency)
    boundary_lines = []
    for u, v in zip(boundary, boundary[1:] + boundary[:1]):
        variable = '_'.join(sorted((u, v)))
        wanted = '>' if u < v else '<'
        assert printed[variable] == physical[variable] == wanted
        assert adjacency[u][v] not in unmarked
        boundary_lines.append({'from': u, 'to': v, 'variable': variable, 'label': wanted})
    out = {'scope': 'All local relations and the unique clockwise outer face of the saved original picture. Printed unmarked internal fragments use the explicit physical completion.',
           'name': which, 'points': points, 'network': network, 'relations': relations,
           'lines': sorted(segments, key=lambda s: s['ends']), 'faces': faces,
           'boundary': boundary, 'boundary_lines': boundary_lines,
           'physical_labeling': physical, 'printed_labeling_completion': printed,
           'unmarked_physical_edges': sorted(unmarked),
           'printed_local_relations_all_valid': True, 'boundary_marks_all_present_and_clockwise': True}
    if which == 'szilassi':
        lower = max((j for j in points if network[j]['type'] == 'Y'), key=lambda j: points[j][1])
        changed = dict(printed)
        changed_lines = relations[lower]['variables']
        for e in changed_lines:
            changed[e] = '-'
        out['exercise45'] = {'junction': lower, 'physical_vertex': junctions[lower]['physical_vertex'],
                             'changed_lines': changed_lines,
                             'changed_local_rows': {j: [''.join(printed[v] for v in r['variables']), ''.join(changed[v] for v in r['variables'])] for j, r in relations.items() if any(e in changed_lines for e in r['variables'])},
                             'literal_candidate_invalid_at': [j for j, r in relations.items() if ''.join(changed[v] for v in r['variables']) not in r['tuples']],
                             'literal_candidate_preserves_boundary': all(changed[r['variable']] == r['label'] for r in boundary_lines),
                             'literal_candidate': changed}
    return out


def main():
    out = [build(name) for name in ['histoscape', 'clasp', 'szilassi']]
    (ROOT / 'results/hc-picture-networks.json').write_text(json.dumps({'pictures': out}, indent=2, default=encode) + '\n')
    print(json.dumps([{'name': x['name'], 'vertices': len(x['points']), 'edges': len(x['lines']),
                       'boundary': x['boundary'], 'unmarked_edges': x['unmarked_physical_edges'],
                       'exercise45': x.get('exercise45')} for x in out], indent=2))


if __name__ == '__main__':
    main()
