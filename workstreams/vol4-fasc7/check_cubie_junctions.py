#!/usr/bin/env python3
"""Exact 64 local octant cases; compare all 32 printed central junctions.

No search over solids: the complete local classification is proved in
notes/trihedral-exercises-038-039.md and used to generate exactly 64 cases.
SVG tolerances concern only rounded printed coordinates, not the geometry.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
BITS = (4, 2, 1)
# Cartesian screen coordinates, with y upwards; same oriented ray arrangement
# as the original. Positive kernel means the viewer is in octant 7.
PROJ = {4: (3, 1), 2: (0, -3), 1: (-4, 1)}
LABELS = [
    '0', '1', '2', '3', '4', '5', '6', '~7',
    '023', '102', '231', '310', '~467', '546', '~675', '~754',
    '046', '~157', '204', '315', '462', '~573', '620', '~731',
    '015', '154', '~237', '~376', '401', '540', '623', '~762',
]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def scale(s, a):
    return tuple(s * x for x in a)


def occupied(label):
    a = {int(x) for x in label.lstrip('~')}
    return frozenset(set(range(8)) - a if label.startswith('~') else a)


def local_cases():
    base = [{0}, {1, 2, 3}, {1, 4, 5}, {2, 4, 6}]
    base += [set(range(8)) - a for a in base]
    out = [frozenset(x ^ t for x in a) for t in range(8) for a in base]
    assert len(out) == len(set(out)) == 64
    assert Counter(map(len, out)) == {1: 8, 3: 24, 5: 24, 7: 8}
    return out


def edges(a):
    out = []
    for bit in BITS:
        for negative in (False, True):
            fixed = bit if negative else 0
            quadrant = {x for x in range(8) if x & bit == fixed}
            k = len(quadrant & a)
            if k not in (1, 3):
                continue
            ray = scale(-1 if negative else 1, PROJ[bit])
            visible = (7 if negative else 7 ^ bit) not in a
            row = {'axis_bit': bit, 'negative': negative,
                   'material_quadrants': k, 'visible': visible}
            if visible:
                fronts = []
                for normal_bit in BITS:
                    if normal_bit == bit:
                        continue
                    other_bit = 7 ^ bit ^ normal_bit
                    for other_negative in (False, True):
                        z = fixed | (other_bit if other_negative else 0)
                        if z in a and (z | normal_bit) not in a:
                            fronts.append((normal_bit, other_bit, other_negative))
                assert len(fronts) in (1, 2)
                if len(fronts) == 2:
                    label = '+' if k == 1 else '-'
                else:
                    _, other_bit, other_negative = fronts[0]
                    interior = scale(-1 if other_negative else 1, PROJ[other_bit])
                    side = cross(ray, interior)
                    assert side
                    label = 'O' if side < 0 else 'I'
                row.update(label=label, ray=list(ray), front_faces=fronts)
            out.append(row)
    assert len(out) == 3
    assert len({x['axis_bit'] for x in out}) == 3
    assert sum(x['material_quadrants'] == 3 for x in out) == (len(a) - 1) // 2
    return out


def junction(rows):
    v = [x for x in rows if x['visible']]
    assert len(v) in (2, 3)
    if len(v) == 2:
        if cross(v[0]['ray'], v[1]['ray']) > 0:
            v.reverse()
        assert cross(v[0]['ray'], v[1]['ray']) < 0
        return 'V', ''.join(x['label'] for x in v)
    for i in range(3):
        for j in range(3):
            if j == i:
                continue
            k = 3 - i - j
            l, m, r = [v[t] for t in (i, j, k)]
            if (cross(l['ray'], m['ray']) < 0
                    and cross(m['ray'], r['ray']) < 0
                    and cross(r['ray'], l['ray']) > 0):
                return 'W', l['label'] + m['label'] + r['label']
    # Y: start with the branch of smallest bit, then go clockwise.
    v.sort(key=lambda x: x['axis_bit'])
    if cross(v[0]['ray'], v[1]['ray']) > 0:
        v[1], v[2] = v[2], v[1]
    assert all(cross(v[i]['ray'], v[(i + 1) % 3]['ray']) < 0 for i in range(3))
    return 'Y', ''.join(x['label'] for x in v)


NUMBER = r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?'


def path_points(p):
    nums = list(map(F, re.findall(NUMBER, p['d'])))
    assert len(nums) % 2 == 0
    points = list(zip(nums[::2], nums[1::2]))
    if 'transform' in p:
        a, b, c, d, e, f = map(F, re.findall(NUMBER, p['transform']))
        points = [(a * x + c * y + e, b * x + d * y + f) for x, y in points]
    return points


def printed_junctions():
    source = ROOT / 'sources/file-182.svg'
    paths = [p.attrib for p in ET.parse(source).findall('.//{http://www.w3.org/2000/svg}path')]
    centers = []
    for i, p in enumerate(paths):
        if p.get('fill') == 'rgb(0%, 0%, 0%)':
            q = path_points(p)
            c = tuple((min(x[j] for x in q) + max(x[j] for x in q)) / 2 for j in (0, 1))
            centers.append((c, i))
    assert len(centers) == 32
    # A few centers are vertically offset by .84pt; row separation is >50pt.
    centers.sort(key=lambda z: z[0][1])
    centers = sum([sorted(centers[i:i + 8], key=lambda z: z[0][0]) for i in range(0, 32, 8)], [])
    printed = [[] for _ in centers]
    # Actual first diagram directions in screen-y-down coordinates, associated
    # with bits by the single-cubie diagrams 1, 2, 4 (each reverses one axis).
    templates = {4: (F('8.300781'), F('-3.875')),
                 2: (0, F('12.449219')),
                 1: (F('-11.617187'), F('-2.769531'))}
    counts = Counter()
    max_center_error_sq = F(0)
    max_ray_cross_sq_ratio = F(0)
    for i, p in enumerate(paths):
        if p.get('stroke-width') != '0.3' or p.get('stroke') != 'rgb(0%, 0%, 0%)':
            continue
        q = path_points(p)
        assert len(q) == 2 and re.findall('[A-Za-z]', p['d']) == ['M', 'L']
        dist = [dot(sub(q[0], c), sub(q[0], c)) for c, _ in centers]
        cell = min(range(32), key=dist.__getitem__)
        assert dist[cell] < F(1, 10000)
        max_center_error_sq = max(max_center_error_sq, dist[cell])
        ray = sub(q[1], q[0])
        ratios = {bit: cross(ray, d) ** 2 / (dot(ray, ray) * dot(d, d)) for bit, d in templates.items()}
        bit = min(BITS, key=ratios.__getitem__)
        assert ratios[bit] < F(1, 1000000)
        assert all(ratios[b] > F(1, 10) for b in BITS if b != bit)
        max_ray_cross_sq_ratio = max(max_ray_cross_sq_ratio, ratios[bit])
        negative = dot(ray, templates[bit]) < 0
        # Every ray's next path is exactly its printed mark: red tick/chevron,
        # or a white mask that splits the black stroke for a concave edge.
        mark = paths[i + 1]
        z = path_points(mark)
        if mark.get('stroke') == 'rgb(100%, 100%, 100%)':
            assert mark.get('stroke-width') == '0.36' and len(z) == 2
            delta_mark = sub(z[1], z[0])
            assert cross(delta_mark, ray) ** 2 / (dot(delta_mark, delta_mark) * dot(ray, ray)) < F(1, 100000)
            label = '-'
        else:
            assert mark.get('stroke') == 'rgb(100%, 0%, 0%)'
            assert mark.get('stroke-width') == '0.3'
            if len(z) == 2:
                delta_mark = sub(z[1], z[0])
                assert dot(delta_mark, ray) ** 2 / (dot(delta_mark, delta_mark) * dot(ray, ray)) < F(1, 100000)
                label = '+'
            else:
                assert len(z) == 3
                arrow = sub(z[1], scale(F(1, 2), tuple(a + b for a, b in zip(z[0], z[2]))))
                label = 'O' if dot(arrow, ray) > 0 else 'I'
        midpoint = scale(F(1, len(z)), tuple(sum(t[j] for t in z) for j in (0, 1)))
        delta = sub(midpoint, q[0])
        assert F(1, 10) < dot(delta, ray) / dot(ray, ray) < F(9, 10)
        assert cross(delta, ray) ** 2 / dot(ray, ray) < F(1, 10)
        printed[cell].append({'axis_bit': bit, 'negative': negative, 'label': label,
                              'ray_path': i, 'mark_path': i + 1})
        counts[label] += 1
    assert sum(counts.values()) == 78
    return printed, {'svg_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                     'central_discs': len(centers), 'visible_rays': sum(counts.values()),
                     'marks': dict(counts),
                     'max_center_error_squared_points': str(max_center_error_sq),
                     'max_ray_cross_squared_ratio': str(max_ray_cross_sq_ratio)}


def main():
    all_cases = local_cases()
    visible = [a for a in all_cases if 7 not in a]
    assert len(visible) == 32
    assert set(map(occupied, LABELS)) == set(visible)
    printed, vector_checks = printed_junctions()
    results = []
    by_type = {'V': Counter(), 'W': Counter(), 'Y': Counter()}
    for cell, label in enumerate(LABELS):
        a = occupied(label)
        rows = edges(a)
        expected = {(x['axis_bit'], x['negative'], x['label']) for x in rows if x['visible']}
        actual = {(x['axis_bit'], x['negative'], x['label']) for x in printed[cell]}
        assert expected == actual, (label, expected, actual)
        kind, pattern = junction(rows)
        by_type[kind][pattern] += 1
        results.append({'printed_label': label, 'occupied': sorted(a), 'edges': rows,
                        'type': kind, 'clockwise_pattern': pattern,
                        'printed_rays': printed[cell]})
    assert by_type['V'] == Counter({'I+': 3, 'IO': 3, '+O': 3, 'O-': 3, 'OI': 3, '-I': 3})
    assert by_type['W'] == Counter({'O+I': 3, '-+-': 3, '+-+': 3})
    assert by_type['Y'] == Counter({'IO-': 1, 'O-I': 1, '-IO': 1, '---': 1, '+++': 1})
    out = {'scope': 'All64 local cases by proved classification; all32 visible central diagrams and78 labels; Table1 V/W/Y.',
           'all_case_sizes': dict(Counter(map(len, all_cases))),
           'visible_case_sizes': dict(Counter(map(len, visible))),
           'patterns': {k: dict(v) for k, v in by_type.items()},
           'vector_checks': vector_checks, 'cases': results}
    (ROOT / 'results/cubie-junctions.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({k: v for k, v in out.items() if k != 'cases'}, indent=2))


if __name__ == '__main__':
    main()
