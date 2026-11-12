#!/usr/bin/env python3
"""All eight native small forbidden subpictures24–25; no search."""
from collections import defaultdict, Counter
from fractions import Fraction as F
from itertools import combinations, permutations
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT, path_segments, cross2, on, parameter, cuts, at
from check_cubie_junctions import path_points
from check_polyhedra_fixed import sub, dot, encode
from check_hc_picture_networks import ordered_neighbors
from check_line_csp22 import TABLE, global_symbol, propagate, ORDER


def main():
    paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-029.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    out = []
    for name, start, stop, wanted in [
        ('24-TT', 18, 21, 'TT'), ('24-VTT', 21, 24, 'VTT'),
        ('24-YTT', 24, 28, 'YTT'), ('24-WTVT', 28, 32, 'WTVT'),
        ('25-WT', 32, 35, 'WT'), ('25-WWT-left', 35, 39, 'WWT'),
        ('25-WWT-right', 39, 43, 'WWT'), ('25-WYT', 43, 47, 'WYT')]:
        originals = {i: path_points(paths[i]) for i in range(start, stop)}
        allpoints = [p for ps in originals.values() for p in ps]
        origin = tuple(min(p[k] for p in allpoints) for k in (0, 1))
        unit = (max(p[1] for p in allpoints) - origin[1]) / 4
        mapped, errors = {}, []
        for i, ps in originals.items():
            mapped[i] = []
            for p in ps:
                q = tuple(round((p[k] - origin[k]) / unit) for k in (0, 1))
                error = sum((p[k] - origin[k] - unit * q[k]) ** 2 for k in (0, 1))
                assert error < F(1, 10000), (name, i, p, q, float(error))
                errors.append(error)
                mapped[i].append(q)
        segments = []
        for i, qs in mapped.items():
            segments.extend(path_segments(paths[i], qs))
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
            adjacency[u].add(v)
            adjacency[v].add(u)
        network, relations = {}, {}
        for j, ns in adjacency.items():
            assert len(ns) in (1, 2, 3)
            if len(ns) == 1:
                continue  # A dangling end means the containing picture continues.
            rays = [sub(points[k], points[j]) for k in ns]
            if len(ns) == 2:
                assert cross2(*rays)
                kind = 'V'
            elif any(cross2(a, b) == 0 and dot(a, b) < 0 for a, b in combinations(rays, 2)):
                kind = 'T'
            elif any(cross2(p[0], p[1]) > 0 and cross2(p[1], p[2]) > 0 and cross2(p[0], p[2]) > 0 for p in permutations(rays)):
                kind = 'W'
            else:
                kind = 'Y'
            ordered = ordered_neighbors(j, kind, ns, points)
            vs = ['_'.join(sorted((j, k))) for k in ordered]
            ts = [''.join(global_symbol(s, j, k) for s, k in zip(t, ordered)) for t in TABLE[kind]]
            network[j] = {'type': kind, 'neighbors': ordered}
            relations[j] = (vs, ts)
        assert Counter(n['type'] for n in network.values()) == Counter(wanted), (name, network)
        edges = sorted({'_'.join(sorted((j, k))) for j, ns in adjacency.items() for k in ns})
        solution, trace = propagate(relations, {e: set(ORDER) for e in edges})
        assert solution is None, name
        out.append({'name': name, 'source_path_range_half_open': [start, stop],
                    'source_origin': origin, 'source_grid_unit': unit,
                    'maximum_source_residual_squared': max(errors),
                    'source_path_grid_vertices': mapped, 'points': points,
                    'lines': edges, 'junctions': network, 'relations': relations,
                    'dangling_ends': sorted(set(points) - set(network)),
                    'contradiction_propagation': trace})
    (ROOT / 'results/impossible-subpictures24-25.json').write_text(json.dumps({'subpictures': out}, indent=2, default=encode) + '\n')
    print(json.dumps([{'name': x['name'], 'junctions': x['junctions'],
                      'last_contradiction': x['contradiction_propagation'][-1],
                      'propagation_steps': len(x['contradiction_propagation'])} for x in out], indent=2))


if __name__ == '__main__':
    main()
