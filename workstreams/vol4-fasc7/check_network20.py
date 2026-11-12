#!/usr/bin/env python3
"""Every native network20 edge, branch order, and relation to the3D picture."""
from fractions import Fraction as F
from collections import Counter, defaultdict
import json
import xml.etree.ElementTree as ET
from check_cubie_junctions import path_points
from check_clasp_projection import ROOT, path_segments, cross2, solve, parameter, cuts
from check_polyhedra_fixed import sub, dot, encode

NETWORK = {
    'a': ('V', 'bc'), 'b': ('W', 'eda'), 'c': ('W', 'adm'),
    'd': ('Y', 'bgc'), 'e': ('Y', 'bfg'), 'f': ('W', 'qhe'),
    'g': ('W', 'deh'), 'h': ('Y', 'fjg'), 'i': ('V', 'jk'),
    'j': ('W', 'lih'), 'k': ('W', 'iln'), 'l': ('Y', 'jsk'),
    'm': ('Y', 'cno'), 'n': ('T', 'kmp'), 'o': ('W', 'mpr'),
    'p': ('V', 'on'), 'q': ('V', 'sf'), 'r': ('V', 'os'),
    's': ('W', 'rlq'),
}
# The letters were read in the original page, not inferred by graph matching.
CIRCLE_LETTERS = dict(zip(range(176, 213, 2), 'naebqfmcigdjhr opksl'.replace(' ', '')))


def verify_planarity(centers, edges):
    from itertools import combinations
    count = 0
    for first, second in combinations(edges, 2):
        a, b = first
        c, d = second
        hits = set(cuts(centers[a], centers[b], centers[c], centers[d]))
        common = set(first) & set(second)
        expected = {F(0) if v == a else F(1) for v in common}
        assert hits == expected, (first, second, hits, expected)
        count += 1
    return count


def main():
    assert len(CIRCLE_LETTERS) == len(set(CIRCLE_LETTERS.values())) == 19
    paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-027.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    centers = {}
    for index, letter in CIRCLE_LETTERS.items():
        p = paths[index]
        assert p.get('stroke') == 'rgb(0%, 0%, 0%)' and 'C' in p['d']
        points = path_points(p)
        centers[letter] = tuple((min(p[j] for p in points) + max(p[j] for p in points)) / 2 for j in (0, 1))
    segments_read = []
    for index in range(167, 175):
        p = paths[index]
        points = path_points(p)
        mapped = []
        for point in points:
            ds = {k: dot(sub(c, point), sub(c, point)) for k, c in centers.items()}
            k = min(ds, key=ds.__getitem__)
            assert ds[k] < F(1, 10000)
            mapped.append(k)
        segments_read.extend((index, a, b) for a, b in path_segments(p, mapped))
    printed = set()
    inserted = []
    for index, a, b in segments_read:
        u = sub(centers[b], centers[a])
        along = []
        for k, c in centers.items():
            t = dot(sub(c, centers[a]), u) / dot(u, u)
            if not 0 <= t <= 1:
                continue
            distance = cross2(sub(c, centers[a]), u) ** 2 / dot(u, u)
            if distance < F(1, 10000):
                along.append((t, k))
                if k not in (a, b):
                    inserted.append({'path': index, 'segment': [a, b], 'junction': k, 'distance_squared': distance})
        along.sort()
        assert along[0][1] == a and along[-1][1] == b
        for (_, c), (_, d) in zip(along, along[1:]):
            printed.add(''.join(sorted((c, d))))
    expected = {''.join(sorted((a, b))) for a, (_, ns) in NETWORK.items() for b in ns}
    assert printed == expected and len(printed) == 26
    assert [x['junction'] for x in inserted] == ['n']
    assert all(a in NETWORK[b][1] for a, (_, ns) in NETWORK.items() for b in ns)
    records = []
    for a, (kind, ns) in NETWORK.items():
        rays = [sub(centers[b], centers[a]) for b in ns]
        determinants = [cross2(rays[i], rays[(i + 1) % len(rays)]) for i in range(len(rays))]
        if kind == 'V':
            assert determinants[0] > 0
        elif kind == 'W':
            assert determinants[0] > 0 and determinants[1] > 0 and cross2(rays[0], rays[2]) > 0
        elif kind == 'Y':
            assert all(d > 0 for d in determinants)
        else:
            assert kind == 'T'
            assert dot(rays[0], rays[2]) < 0
            assert cross2(rays[0], rays[2]) ** 2 / (dot(rays[0], rays[0]) * dot(rays[2], rays[2])) < F(1, 10000000)
            assert determinants[0] < 0 and determinants[1] < 0
        records.append({'junction': a, 'type': kind, 'printed_order': ns, 'cyclic_determinants': determinants})

    # Independently match every named center to the completed3D-derived graph.
    saved = json.loads((ROOT / 'results/histoscape-projection.json').read_text())
    js = saved['junctions']
    model_points = [tuple(map(F, row['point'])) for row in js]
    anchors = [('a', 1), ('b', 3), ('c', 7)]
    ref = [next(i for i, row in enumerate(js) if row['physical_vertex'] == [v]) for _, v in anchors]
    affine = [solve([list(model_points[i]) + [F(1)] for i in ref], [centers[a][j] for a, _ in anchors]) for j in (0, 1)]
    assert cross2(affine[0][:2], affine[1][:2]) > 0
    transformed = [tuple(dot(row, (*p, F(1))) for row in affine) for p in model_points]
    matching, residual = {}, F(0)
    for a, c in centers.items():
        ds = [dot(sub(v, c), sub(v, c)) for v in transformed]
        k = min(range(19), key=ds.__getitem__)
        assert ds[k] < F(1, 1000)
        assert sorted(ds)[1] > 1
        residual = max(residual, ds[k])
        matching[a] = k
        assert js[k]['type'] == NETWORK[a][0]
    assert len(set(matching.values())) == 19
    # Two vertices are adjacent precisely when their points lie consecutively
    # on one saved visible physical-edge interval, with intervening T cuts.
    picture_edges = set()
    proj_rows = [list(map(F, row)) for row in saved['projection_rows']]
    vs = [tuple(map(F, v)) for v in saved['model']['vertices']]
    proj = [tuple(dot(row, (*v, F(1))) for row in proj_rows) for v in vs]
    inverse = {k: a for a, k in matching.items()}
    for row in saved['visibility']:
        x, y = row['edge']
        for s, t in row['intervals']:
            s, t = F(s), F(t)
            along = []
            for i, p in enumerate(model_points):
                if cross2(sub(p, proj[x]), sub(proj[y], proj[x])) == 0:
                    u = parameter(p, proj[x], proj[y])
                    if s <= u <= t:
                        along.append((u, i))
            along.sort()
            for (_, u), (_, v) in zip(along, along[1:]):
                picture_edges.add(''.join(sorted((inverse[u], inverse[v]))))
    assert picture_edges == printed
    out = {'scope': 'All19 named junctions,26 edges, every type and ordered branch list in(20), and the complete correspondence to the independently checked histoscape image.',
           'circle_path_to_letter': CIRCLE_LETTERS, 'centers': centers,
           'edges': sorted(printed), 'junction_types': dict(Counter(k for k, _ in NETWORK.values())),
           'inserted_junctions_on_continuous_paths': inserted,
           'ordered_junction_checks': records, 'model_to_network_affine': affine,
           'maximum_model_center_residual_squared': residual,
           'letter_to_physical_vertex': {a: js[k]['physical_vertex'] for a, k in matching.items()}}
    out['planar_edge_pair_checks'] = verify_planarity(centers, sorted(printed))
    (ROOT / 'results/network20.json').write_text(json.dumps(out, indent=2, default=encode) + '\n')
    print(json.dumps({k: out[k] for k in ('scope', 'edges', 'junction_types', 'inserted_junctions_on_continuous_paths', 'maximum_model_center_residual_squared')}, indent=2, default=encode))


if __name__ == '__main__':
    main()
