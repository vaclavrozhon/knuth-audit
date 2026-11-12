"""Compare the three original Eureka 22 ring solutions to the complete modern census.

The twelve words and three rings were transcribed from the original scanned
printed pages 16 and 22, not accepted from OCR. Source colours 1..5 map to 0..4.
This only scans the already accepted 7200 models; it does not repeat a search.
"""
from datetime import datetime, timezone
import json
import re
import dodeca136 as d

SOURCE_TYPES = dict(zip('ABCDEFGHJKLM', [
    '12345', '12354', '12435', '12453', '12534', '12543',
    '13245', '13254', '13425', '13524', '14235', '14325',
]))
SOURCE_REVERSES = dict(zip('ABCDEFGHJKLM', [
    '15432', '14532', '15342', '13542', '14352', '13452',
    '15423', '14523', '15243', '14253', '15324', '15234',
]))
RINGS = [
    'G5K3M2C4B1H4J3L2E5A1G',
    'B2M5K2F5A1H3L5E3D5G1B',
    'E2L3D1G3H1F3M2C1J3K1E',
]


def main():
    labels = {d.tile(''.join(str(int(c) - 1) for c in word)): label
              for label, word in SOURCE_TYPES.items()}
    assert len(labels) == 12 and set(labels) == set(d.TILES)
    assert all(d.tile(w) == d.tile(SOURCE_REVERSES[label])
               for label, w in SOURCE_TYPES.items())
    # Remove two opposite faces. The ten remaining faces form a zigzag belt;
    # each also touches the belt faces at distances two, as in the source.
    north = '000'
    aa = list(d.CYCLES[north])
    bb = []
    for i in range(5):
        candidates = set(d.ADJ[aa[i]]) & set(d.ADJ[aa[(i + 1) % 5]])
        assert len(candidates) == 2 and north in candidates
        bb.append(next(iter(candidates - {north})))
    belt = [f for pair in zip(aa, bb) for f in pair]
    assert len(set(belt)) == 10
    belt_edges = [tuple(sorted((belt[i], belt[(i + 1) % 10]))) for i in range(10)]
    assert all(e in d.EDGES for e in belt_edges)
    assert all(set(d.ADJ[f]) & set(belt) ==
               {belt[(i + k) % 10] for k in [-2, -1, 1, 2]}
               for i, f in enumerate(belt))
    geom = json.loads((d.OUT / 'geometry-checked.json').read_text())
    classes = {v: c['automorphisms'] for c in geom['classes'] for v in c['models']}
    models_path = d.OUT / 'all-color-models.txt'
    models = models_path.read_text().splitlines()
    assert d.sha(models_path) == geom['expanded_models_sha256'] and len(models) == 7200
    accepted = []
    for ring in RINGS:
        pairs = re.findall(r'([A-M])([1-5])', ring)
        assert len(pairs) == 10 and len(ring) == 21 and ring[-1] == ring[0]
        wanted_labels = ''.join(x for x, _ in pairs)
        wanted_colors = ''.join(str(int(c) - 1) for _, c in pairs)
        matching = []
        for vector in models:
            ec = dict(zip(d.EDGES, vector))
            if ''.join(ec[e] for e in belt_edges) != wanted_colors:
                continue
            words = d.validate(vector)
            if ''.join(labels[d.tile(words[f])] for f in belt) != wanted_labels:
                continue
            matching.append(dict(vector=vector, normalized_vector=d.normalize(vector),
                                 automorphisms=classes[d.normalize(vector)],
                                 cap_faces={f: labels[d.tile(words[f])]
                                            for f in d.FACES if f not in belt}))
        assert matching, ring
        assert len({x['automorphisms'] for x in matching}) == 1
        accepted.append(dict(source_ring=ring, completions=matching))
    assert sorted({x['completions'][0]['automorphisms'] for x in accepted}) == [4, 6, 12]
    d.save(d.OUT / 'history-checked.json', dict(
        at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=d.sha(__file__),
        geometry_sha256=d.sha(d.__file__),
        original_pdf_sha256=d.sha(d.ROOT / 'sources/dodeca136/Eureka-22.pdf'),
        model_set_sha256=d.sha(models_path), source_types=SOURCE_TYPES,
        source_reverse_words=SOURCE_REVERSES, belt=belt, solutions=accepted,
        original_citation='M. R. Boothroyd and J. H. Conway, Problems Drive, 1959, '
                          'Eureka 22 (October 1959), 15–17; solutions 22–23.',
        exercise_location=dict(printed=16, pdf=17, number=6),
        solution_location=dict(printed=22, pdf=23, number=6),
        verified='Original formulation, twelve pentagonal types and all three '
                 'printed rings agree with the modern complete census.',
        limits=['The scanned article does not independently establish discovery in 1958.',
                'The name quintominal dodecahedra is absent from this article.',
                'The original article gives three solutions but does not describe '
                'the method by which Conway obtained the exhaustive count.']))
    print('PASS136 historical rings:',
          [(len(x['completions']), x['completions'][0]['automorphisms']) for x in accepted])


if __name__ == '__main__':
    main()
