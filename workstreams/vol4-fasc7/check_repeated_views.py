#!/usr/bin/env python3
"""Compare original unlabelled drawings with already certified visible intervals."""
from fractions import Fraction as F
from collections import defaultdict
from itertools import combinations
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT, printed_visibility, solve, cross2
from check_polyhedra_fixed import sub, add, dot, encode
from check_cubie_junctions import path_points


def main():
    results = []
    for tag, name, file, begin, end, shift in [
        ('101b', 'szilassi', '024', 84, 92, ('14.22', '419.94')),
        ('101c', 'clasp', '024', 92, 110, ('7.51', '419.94')),
        ('101d', 'histoscape', '024', 110, 126, ('.60', '423.91')),
        ('103b', 'szilassi', '025', 123, 131, ('-32.52', '125.04')),
    ]:
        saved = json.loads((ROOT / ('results/' + name + '-projection.json')).read_text())
        model = (json.loads((ROOT / 'results/polyhedra-fixed.json').read_text())['Clasp']
                 if name == 'clasp' else saved['model'])
        vertices = [tuple(map(F, v)) for v in model['vertices']]
        rows = [list(map(F, row)) for row in saved['projection_rows']]
        projected = [tuple(dot(row, (*v, F(1))) for row in rows) for v in vertices]
        predicted = [add(p, tuple(map(F, shift))) for p in projected]
        paths = [p.attrib for p in ET.parse(ROOT / ('sources/file-' + file + '.svg')).findall('.//{http://www.w3.org/2000/svg}path')]
        relevant, occurrences = {}, defaultdict(list)
        for i in range(begin, end):
            p = paths[i]
            if p.get('fill') != 'rgb(100%, 100%, 100%)' and p.get('stroke') != 'rgb(0%, 0%, 0%)':
                continue
            mapped = []
            for point in path_points(p):
                distances = [dot(sub(v, point), sub(v, point)) for v in predicted]
                k = min(range(len(vertices)), key=distances.__getitem__)
                assert distances[k] < F(1, 100)
                assert sorted(distances)[1] > F(1, 10)
                mapped.append(k); occurrences[k].append(point)
            relevant[i] = {'path': p, 'vertices': mapped}
        refs = max(combinations(occurrences, 3), key=lambda abc: abs(cross2(sub(projected[abc[1]], projected[abc[0]]), sub(projected[abc[2]], projected[abc[0]]))))
        means = [tuple(sum(p[j] for p in occurrences[k]) / len(occurrences[k]) for j in (0, 1)) for k in refs]
        matrix = [list(projected[k]) + [F(1)] for k in refs]
        affine = [solve(matrix, [p[j] for p in means]) for j in (0, 1)]
        assert cross2(affine[0][:2], affine[1][:2]) > 0
        residual = max(dot(sub(tuple(dot(row, (*projected[k], F(1))) for row in affine), p),
                           sub(tuple(dot(row, (*projected[k], F(1))) for row in affine), p))
                       for k in occurrences for p in occurrences[k])
        # The base projection already fits rounded source vertices with up to
        # .01pt residual; a second rounded copy adds its own quantization.
        assert residual < F(1, 2500), (tag, float(residual))
        printed, trace, rejected = printed_visibility(model, projected, relevant)
        prior = {k: [[F(a), F(b)] for a, b in row['intervals']] for k, row in enumerate(saved['visibility'])}
        assert printed == prior, (tag, [(model['edges'][k], printed[k], prior[k]) for k in prior if printed[k] != prior[k]])
        results.append({'figure': tag, 'reused_projection': name,
                        'source_file_page': int(file), 'source_path_range_half_open': [begin, end],
                        'plane_affine_rows': affine, 'maximum_point_residual_squared': residual,
                        'original_path_vertices': {i: item['vertices'] for i, item in relevant.items()},
                        'fully_erased_auxiliary_segments': rejected,
                        'visible_interval_trace': trace,
                        'junction_types': saved['junction_types'], 'lines': saved['lines']})
    out = {'scope': 'Every unlabelled original path of101(b,c,d) and103(b), with all occlusion intervals. Reuses completed3D visibility; no old geometry rerun.', 'figures': results}
    (ROOT / 'results/repeated-views.json').write_text(json.dumps(out, indent=2, default=encode) + '\n')
    print(json.dumps([{'figure': x['figure'], 'maximum_point_residual_squared': x['maximum_point_residual_squared'], 'junction_types': x['junction_types']} for x in results], indent=2, default=encode))


if __name__ == '__main__':
    main()
