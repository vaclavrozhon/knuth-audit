"""Original DLX2 versus independent forced-rotation enumeration, all four book cases."""
from datetime import datetime, timezone
import gzip
import json
import re
import nuts137 as n
import graph_native as native


def main():
    figures = json.loads((n.OUT / 'figures-checked.json').read_text())
    assert figures['geometry_sha256'] == n.sha(n.__file__)
    build = json.loads((n.ROOT / 'results/symmetry121_123/native/build.json').read_text())
    binary = build['binaries']['original']['binary']
    assert n.sha(binary) == build['binaries']['original']['sha256']
    native.OUT = n.OUT / 'native'; native.OUT.mkdir(exist_ok=True)
    records = []
    for label, index, rule, expected in [('a', 0, 'equal', 1), ('b', 0, 'sum7', 0),
                                        ('d-equal', 1, 'equal', 1), ('d-sum7', 1, 'sum7', 1)]:
        nuts = figures['figures'][index]['types']
        enc = n.problem(nuts, rule)
        result = native.run(label, n.native_text(enc), binary=binary, limit=3600)
        assert result['status'] == 'completed' and result['returncode'] == 0
        lookup = {tuple(sorted(row)): i for i, row in enumerate(enc['rows'])}
        selected, models = [], []

        def accept():
            assert len(selected) == 7
            words = [''] * 7
            for i in selected:
                pos, word = enc['placements'][i]
                assert not words[pos]
                words[pos] = word
            n.validate(words, nuts, rule)
            assert words[0][0] == '1'
            return '/'.join(words)

        with gzip.open(native.OUT / (label + '.out.gz'), 'rt') as f:
            for line in f:
                if re.fullmatch(r'\d+:\s*', line):
                    if selected:
                        models.append(accept()); selected = []
                elif line.strip():
                    tokens = re.sub(r'\s*\(\d+ of \d+\)\s*$', '', line).split()
                    selected.append(lookup[tuple(sorted(tokens))])
        if selected:
            models.append(accept())
        independent, profiles = n.ring_search(nuts, rule)
        assert sorted(models) == independent and len(models) == result['solutions'] == expected
        fig_index = 2 if label == 'd-sum7' else index
        if expected:
            assert '/'.join(figures['figures'][fig_index]['normalized']) in models
        records.append(dict(case=label, rule=rule, nuts=nuts, models=sorted(models),
                            solutions=len(models), full_set_equality=True, independent_centers=profiles,
                            native_metadata_sha256=n.sha(native.OUT / (label + '.json'))))
    n.save(n.OUT / 'book-cases-checked.json', dict(
        at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=n.sha(__file__),
        geometry_sha256=n.sha(n.__file__), figure_sha256=n.sha(n.OUT / 'figures-checked.json'),
        cases=records, primary_items=14, secondary_items=12, options=259,
        rotations_only=True, global_rotation_removed_by_fixed_center_orientation=True))
    print('PASS137 exact counts1,0,1,1; complete model equality and all original figures valid.')


if __name__ == '__main__':
    main()
