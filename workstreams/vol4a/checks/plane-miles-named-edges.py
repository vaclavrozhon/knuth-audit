"""Two named empty-circle witnesses and one hull witness, no Delaunay census."""
import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
cities = {}
for line in (root / 'sources/sgb-miles.dat').read_text().splitlines():
    match = re.fullmatch(r'(.+)\[(\d+),(\d+)\](\d+)', line)
    if match:
        name, lat, lon, population = match.groups()
        a = int(lat) - 2672
        cities[name] = (12312 - int(lon), a + (a >> 1))
assert len(cities) == 128 and len(set(cities.values())) == 128


def frac(x):
    return str(Fraction(x))


out = {'scope': 'Exactly two printed finite edges and Vancouver hull membership; no global degeneracy check or triangulation run.',
       'city_count': len(cities), 'distinct_coordinates': len(set(cities.values())),
       'coordinate_transform': 'x=12312-lon; a=lat-2672; y=a+floor(a/2)', 'pairs': []}
for un, vn in [('Seattle, WA', 'Vancouver, BC'), ('Toronto, ON', 'Rochester, NY')]:
    u, v = cities[un], cities[vn]
    dx, dy = v[0] - u[0], v[1] - u[1]
    normal = (-dy, dx)
    low, high, low_by, high_by = None, None, None, None
    constraints = []
    for name, w in cities.items():
        if name in (un, vn):
            continue
        a = (w[0] - u[0]) * (w[0] - v[0]) + (w[1] - u[1]) * (w[1] - v[1])
        b = 2 * (normal[0] * (w[0] - u[0]) + normal[1] * (w[1] - u[1]))
        constraints.append((name, a, b))
        if b > 0:
            q = Fraction(a, b)
            if high is None or q < high:
                high, high_by = q, name
        elif b < 0:
            q = Fraction(a, b)
            if low is None or q > low:
                low, low_by = q, name
        else:
            assert a > 0
    assert low is None or high is None or low < high
    if (low is None or low < 0) and (high is None or high > 0):
        t = Fraction(0)
    elif low is not None and high is not None:
        t = (low + high) / 2
    elif low is not None:
        t = low + 1
    else:
        t = high - 1
    gaps = [(name, a - b * t) for name, a, b in constraints]
    assert all(gap > 0 for _, gap in gaps)
    center = [Fraction(u[i] + v[i], 2) + t * normal[i] for i in range(2)]
    radius_sq = sum((center[i] - u[i]) ** 2 for i in range(2))
    out['pairs'].append({'ends': [un, vn], 'coordinates': [u, v],
                         't_interval': [frac(low) if low is not None else None,
                                        frac(high) if high is not None else None],
                         'limiting_cities': [low_by, high_by], 'chosen_t': frac(t),
                         'center': [frac(x) for x in center], 'radius_squared': frac(radius_sq),
                         'minimum_outside_gap': {'city': min(gaps, key=lambda p: p[1])[0],
                                                 'value': frac(min(gap for _, gap in gaps))},
                         'all_outside_gaps': [{'city': n, 'gap': frac(g)} for n, g in gaps]})
support = {name: xy[0] for name, xy in cities.items()}
assert support['Vancouver, BC'] == 0
assert all(x > 0 for name, x in support.items() if name != 'Vancouver, BC')
out['hull'] = {'vertex': 'Vancouver, BC', 'coordinates': cities['Vancouver, BC'],
               'supporting_line': 'x=0', 'others_in': 'x>0',
               'minimum_other_x': min(x for name, x in support.items() if name != 'Vancouver, BC')}
(root / 'results/plane-miles-named-edges.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({**out, 'pairs': [{k: v for k, v in p.items() if k != 'all_outside_gaps'} for p in out['pairs']]}, indent=2))
