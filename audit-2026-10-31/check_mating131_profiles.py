"""Check that the original curved sides use four consistent oriented profiles."""
from collections import defaultdict
from datetime import datetime, timezone
import xml.etree.ElementTree as ET

import extract_mating131 as ex
import mating131 as m
import symmetries129 as s


def distance(p, q):
    assert len(p) == len(q)
    return max(abs(a-b) for x, y in zip(p, q) for a, b in zip(x, y))


def reverse(p):
    return [(1-t, v) for t, v in reversed(p)]


def anti(p):
    return [(t, -v) for t, v in p]


def main():
    trace = s.OUT/'page139-trace.xml'
    curves = []
    for element in ET.parse(trace).iter('stroke_path'):
        if element.get('color') != '0 0 0':
            continue
        points = ex.path_points(element)
        if points and all(75 < x < 215 and 220 < y < 328 for x, y in points):
            curves.append((points, sum(p.tag == 'curveto' for p in element)))
    assert len(curves) == 72
    profiles = defaultdict(list)
    for i in range(0, 72, 3):
        group = curves[i:i+3]
        center = [sum(ps[j][k] for ps, n in group for j in (0, -1))/6 for k in (0, 1)]
        for ps, n in group:
            a, b = ps[0], ps[-1]; dx, dy = b[0]-a[0], b[1]-a[1]
            side = dx*(center[1]-a[1])-dy*(center[0]-a[0]); length2 = dx*dx+dy*dy
            profile = [((dx*(p[0]-a[0])+dy*(p[1]-a[1]))/length2,
                        (dx*(p[1]-a[1])-dy*(p[0]-a[0]))/length2*(1 if side > 0 else -1)) for p in ps]
            if side < 0:
                profile = reverse(profile)
            typ = 'a' if n == 0 else ('b' if n == 2 else ('c' if sum(v for t, v in profile) < 0 else 'd'))
            profiles[typ].append(profile)
    assert {t: len(p) for t, p in profiles.items()} == dict(a=18, b=18, c=18, d=18)
    references = {t: ps[0] for t, ps in profiles.items()}
    deviations = {t: max(distance(p, references[t]) for p in ps) for t, ps in profiles.items()}
    identities = dict(wave_reversal_is_anti=distance(reverse(references['b']), anti(references['b'])),
                      hump_reversal_unchanged=distance(reverse(references['c']), references['c']),
                      dip_reversal_unchanged=distance(reverse(references['d']), references['d']),
                      hump_and_dip_complementary=distance(anti(references['c']), references['d']))
    tolerance = .0001
    assert max([*deviations.values(), *identities.values()]) < tolerance
    m.save(m.OUT/'curve-profiles-checked.json', dict(
        checked_at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=m.sha(__file__),
        extractor_sha256=m.sha(ex.__file__), trace_sha256=m.sha(trace),
        side_occurrences=72, counts=dict(a=18, b=18, c=18, d=18),
        normalization='Unit chord; positive normal points inside the tile; all sides oriented with tile interior on the same side.',
        reference_control_points=references, maximum_within_type_deviation=deviations,
        profile_identity_errors=identities, tolerance=tolerance,
        interpretation='Within rounding of the PDF control coordinates, all four profiles are consistent. Reversal turns the wave into its anti-profile while preserving hump/dip; taking the complementary profile restores the wave and swaps hump/dip.'))
    print('PASS131 oriented profiles:18 copies of each type; all profile/anti-profile errors below', tolerance)


if __name__ == '__main__':
    main()
