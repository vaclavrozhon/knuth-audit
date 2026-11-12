#!/usr/bin/env python3
"""Compare every native unlabelled101(a) polygon with certified104(a)."""
from collections import defaultdict
from fractions import Fraction as F
import json
import xml.etree.ElementTree as ET
from check_sphinx_native_network import decode
from check_clasp_projection import ROOT, solve, cross2
from check_cubie_junctions import path_points
from check_polyhedra_fixed import dot, sub, encode


def main():
    saved = decode(json.loads((ROOT / 'results/sphinx-native-geometry.json').read_text()))
    old = saved['relevant']
    paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-024.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    assert len(old) == 56
    occurrences, matched = defaultdict(list), []
    for target, source in zip(range(28, 84), sorted(old)):
        p, prior = paths[target], old[source]
        assert p.get('stroke') == prior['path'].get('stroke')
        assert p.get('fill') == prior['path'].get('fill')
        qs = path_points(p)
        assert len(qs) == len(prior['vertices'])
        for k, q in zip(prior['vertices'], qs):
            occurrences[k].append(q)
        matched.append({'path101a': target, 'path104a': source, 'vertices': prior['vertices']})
    refs = [26, 61, 34]
    means = [tuple(sum(p[j] for p in occurrences[k]) / len(occurrences[k]) for j in (0, 1)) for k in refs]
    matrix = [list(saved['points'][k]) + [F(1)] for k in refs]
    affine = [solve(matrix, [p[j] for p in means]) for j in (0, 1)]
    assert cross2(affine[0][:2], affine[1][:2]) > 0
    errors = [dot(sub(tuple(dot(row, (*saved['points'][k], F(1))) for row in affine), q),
                  sub(tuple(dot(row, (*saved['points'][k], F(1))) for row in affine), q))
              for k, qs in occurrences.items() for q in qs]
    assert max(errors) < F(1, 2500), float(max(errors))
    # Exactly the same paths, colors and painter order under an orientation-
    # preserving plane affine map give the same visible network. No3D
    # identity, hidden-surface geometry or old interval calculation is rerun.
    out = {'scope': 'All56 native101(a) polygons/strokes match104(a), with identical colors, vertex sequences and painter order.',
           'affine104a_to101a': affine, 'maximum_residual_squared': max(errors),
           'matched_paths': matched, 'network_reused': 'results/sphinx-native-network.json'}
    (ROOT / 'results/sphinx-repeated-view.json').write_text(json.dumps(out, indent=2, default=encode) + '\n')
    print(json.dumps({'matched_paths': len(matched), 'maximum_residual_squared': str(max(errors))}))


if __name__ == '__main__':
    main()
