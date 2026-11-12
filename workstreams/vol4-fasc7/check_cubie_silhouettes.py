#!/usr/bin/env python3
"""Identify every filled cubie in all32 answer41 drawings from native vectors."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations, product
import json
import xml.etree.ElementTree as ET
from check_cubie_junctions import ROOT, LABELS, occupied, path_points, sub, dot, cross


def hull(points):
    points = sorted(set(points))
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(sub(lower[-1], lower[-2]), sub(p, lower[-1])) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(sub(upper[-1], upper[-2]), sub(p, upper[-1])) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def main():
    ps = [p.attrib for p in ET.parse(ROOT / 'sources/file-182.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    centers = []
    for p in ps:
        if p.get('fill') == 'rgb(0%, 0%, 0%)':
            q = path_points(p)
            centers.append(tuple((min(x[j] for x in q) + max(x[j] for x in q)) / 2 for j in (0, 1)))
    assert len(centers) == 32
    centers.sort(key=lambda z: z[1])
    centers = sum([sorted(centers[i:i + 8]) for i in range(0, 32, 8)], [])
    vectors = [(F('8.3'), F('-3.873')), (0, F('12.449')), (F('-11.619'), F('-2.766'))]
    grid = {p: tuple(sum(p[i] * vectors[i][j] for i in range(3)) for j in range(2))
            for p in product((-1, 0, 1), repeat=3)}
    reverse = {q: p for p, q in grid.items()}
    assert len(reverse) == 27
    separation = min(dot(sub(a, b), sub(a, b)) for a, b in combinations(grid.values(), 2))
    silhouettes = {}
    for octant in range(8):
        coordinates = [(-1, 0) if octant & bit else (0, 1) for bit in (4, 2, 1)]
        shape = hull([grid[p] for p in product(*coordinates)])
        assert len(shape) == 6
        silhouettes[octant] = frozenset(reverse[p] for p in shape)
    cells = [[] for _ in centers]
    max_error = F(0)
    count = 0
    for index, p in enumerate(ps):
        if p.get('fill') != 'rgb(94.999695%, 94.999695%, 94.999695%)':
            continue
        points = path_points(p)
        assert len(points) == 6
        center = tuple(sum(x[j] for x in points) / len(points) for j in (0, 1))
        cell = min(range(32), key=lambda k: dot(sub(centers[k], center), sub(centers[k], center)))
        snapped = []
        for point in points:
            relative = sub(point, centers[cell])
            near = min(grid, key=lambda v: dot(sub(grid[v], relative), sub(grid[v], relative)))
            error = dot(sub(grid[near], relative), sub(grid[near], relative))
            assert error < F(1, 10000)
            max_error = max(max_error, error)
            snapped.append(near)
        matches = [octant for octant, shape in silhouettes.items() if frozenset(snapped) == shape]
        assert len(matches) == 1
        # The actual path is cyclic around the convex hexagon, not a crossing
        # permutation of the same vertex set.
        ideal = [grid[p] for p in snapped]
        signs = [cross(sub(ideal[(i + 1) % 6], ideal[i]), sub(ideal[(i + 2) % 6], ideal[(i + 1) % 6])) for i in range(6)]
        assert all(x > 0 for x in signs) or all(x < 0 for x in signs)
        cells[cell].append({'octant': matches[0], 'path': index})
        count += 1
    assert count == 103
    for label, cell in zip(LABELS, cells):
        expected = set(occupied(label))
        if label == '~7':
            expected.remove(0)  # Fully hidden: a ray to octant7 exits0 into4,2 or1.
        assert Counter(x['octant'] for x in cell) == Counter(expected), (label, cell, expected)
    out = {'scope': 'All103 gray hexagons identify the occupied cubies of all32 diagrams. Octant0 of ~7 is fully hidden and omitted. Central78 rays checked separately.',
           'filled_cubies': count, 'max_snap_error_squared_points': str(max_error),
           'minimum_projected_grid_separation_squared_points': str(separation),
           'cells': [{'label': label, 'fills_in_paint_order': cell} for label, cell in zip(LABELS, cells)]}
    (ROOT / 'results/cubie-silhouettes.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'cells'}, indent=2))


if __name__ == '__main__':
    main()
