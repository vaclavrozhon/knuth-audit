"""Validate the full4624-tile certificate on an abstract triangular complex."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/triangles132'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def cyclic(xs):
    return min(tuple(xs[i:]+xs[:i]) for i in range(3))


def main():
    witness = json.loads((OUT/'witness.json').read_text())
    n, d = witness['side'], witness['colors']
    assert (n, d) == (68, 24)
    expected_cells = {(r, c, 0) for r in range(n) for c in range(n-r)}
    expected_cells |= {(r, c, 1) for r in range(n-1) for c in range(n-1-r)}
    actual_cells = set(); edges = defaultdict(list); types = Counter(); color_occurrences = Counter()
    for r, c, orient, cs in witness['tiles']:
        cell = (r, c, orient)
        assert cell in expected_cells and cell not in actual_cells
        actual_cells.add(cell)
        assert len(cs) == 3 and all(isinstance(k, int) and 0 <= k < d for k in cs)
        # Lattice vertices are integer pairs. Image coordinates play no role.
        if orient == 0:
            vs = [(r, c), (r, c+1), (r+1, c)]
        else:
            vs = [(r, c+1), (r+1, c+1), (r+1, c)]
        for i, color in enumerate(cs):
            edge = tuple(sorted((vs[i], vs[(i+1) % 3])))
            edges[edge].append((cell, color))
        types[cyclic(cs)] += 1; color_occurrences.update(cs)
    assert actual_cells == expected_cells and len(actual_cells) == n*n == 4624
    expected_types = {cyclic(list(t)) for t in product(range(d), repeat=3)}
    assert set(types) == expected_types and set(types.values()) == {1}
    assert len(types) == (d**3+2*d)//3 == 4624
    border, interior = [], []
    for edge, occurrences in edges.items():
        if len(occurrences) == 1:
            assert any(all(p[k] == 0 for p in edge) for k in (0, 1)) or all(sum(p) == n for p in edge)
            border.append((edge, occurrences[0][1]))
        else:
            assert len(occurrences) == 2 and occurrences[0][1] == occurrences[1][1]
            interior.append(edge)
    assert len(border) == 3*n == 204 and len({c for e, c in border}) == 1
    assert len(interior) == (3*n*n-3*n)//2 == 6834
    assert set(color_occurrences.values()) == {578}
    result = dict(
        checked_at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=sha(__file__),
        witness_sha256=sha(OUT/'witness.json'), tiles=4624, different_cyclic_types=4624,
        colors=24, each_color_side_occurrences=578, matched_internal_edges=6834,
        constant_boundary_edges=204, boundary_color=border[0][1],
        existence_proved=True, new_search_performed=False,
        counting_formula='d + d(d-1) + d(d-1)(d-2)/3 = (d^3+2d)/3',
        counting_proof='One type per monochrome choice; d(d-1) types with exactly two equal edges; two cyclic orientations per three-element subset. Equivalently Burnside on C3 has fixed counts d^3,d,d.',
        elliptic_reduction=dict(equation='3*m^2 = d^3+2*d', X='3*d', Y='9*m', curve='Y^2=X^3+18*X',
                               inverse_conditions='X>0, X divisible by3, Y divisible by9; m can be chosen positive.',
                               completeness_of_integral_points_verified=False),
        limitations='This proves the requested arrangement exists. The infinite Diophantine classification and historical dates/citations require separate evidence.')
    (OUT/'witness-checked.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS132 complete witness:4624 distinct cyclic tiles;6834 matching internal edges;204 constant boundary edges.')


if __name__ == '__main__':
    main()
