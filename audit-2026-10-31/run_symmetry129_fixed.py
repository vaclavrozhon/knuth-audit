"""Previously missing independent DLX2 counts for the32 fixed-mono cases.

The existing bitset counts are reused. All newly emitted native samples are
validated geometrically; full-count agreement is checked separately for
each of the32 cases. No old successful search is restarted.
"""
from datetime import datetime, timezone
from pathlib import Path
import gzip
import json
import os
import re

import graph_native
import macmahon126 as mc
import symmetries129 as s

OUT = s.OUT / 'fixed-native'
PERIOD = 100


def check_samples(label, mono, header, rows):
    lookup = {tuple(sorted(row)): row for row in rows}
    sec = header[header.index('|')+1:]
    edge_indices = {sec[i]: i for i in range(42)}
    models, selected = [], []

    def accept():
        colors, cells, pieces = {}, set(), []
        for row in selected:
            tile, cell, *rest = row
            assert cell not in cells
            cells.add(cell)
            pieces.append(tile)
            for item in rest:
                name, c = item.split(':')
                if name not in edge_indices:
                    continue
                i = edge_indices[name]
                assert i not in colors or colors[i] == c
                colors[i] = c
        assert cells == {s.g.name(t) for t in s.TS} and sorted(pieces) == s.g.PIECES
        assert set(colors) == set(range(42))
        vector = ''.join(colors[i] for i in range(42))
        cc = s.validate(vector)
        assert all(cc[tuple(t)] == c*3 for c, t in zip('abcd', mono))
        # Physical endpoint reflection, independently of encoded patch columns.
        reflected = s.cells(s.transform(vector, s.BY['lr']))
        assert all(s.g.patchmask(cc[t]) == s.g.patchmask(reflected[t]) for t in s.TS)
        return vector

    with gzip.open(OUT/f'{label}.out.gz', 'rt') as f:
        for line in f:
            if re.fullmatch(r'\d+:\s*', line):
                if selected:
                    models.append(accept())
                selected = []
            elif line.strip():
                tokens = re.sub(r'\s*\(\d+ of \d+\)\s*$', '', line).split()
                selected.append(lookup[tuple(sorted(tokens))])
    if selected:
        models.append(accept())
    assert len(models) == len(set(models))
    return models


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    graph_native.OUT = OUT
    old = s.ROOT / 'results/macmahon'
    meta = json.loads((old/'lr/metadata.json').read_text())
    reference = {x['label']: x for x in json.loads((old/'reflection-bitset-counts.json').read_text())}
    fixed = [x for x in meta if x['fixed'] == 2]
    assert len(fixed) == 32
    built = mc.build()
    state = dict(status='running', wrapper_pid=os.getpid(), started_at_utc=datetime.now(timezone.utc).isoformat(),
                 runner_sha256=s.sha(__file__), geometry_sha256=s.sha(s.__file__),
                 old_count_sha256=s.sha(old/'reflection-bitset-counts.json'),
                 expected_cases=32, model_output_period=PERIOD, timeout_seconds_per_case=172800, done=[])
    for case in fixed:
        label = f'lr-fixed-{case["index"]:03d}'
        state['current'] = label
        mc.save(s.OUT/'fixed-queue.json', state)
        mono = [tuple(t) for t in case['mono']]
        # Thus no strong rotation can occur in this entire branch; strong
        # reflections have already been excluded generally.
        assert {s.g.opposite(t) for t in mono} != set(mono)
        h, rows = s.g.reflection_options('lr', {c*3: [t] for c, t in zip('abcd', mono)})
        text = ' '.join(h)+'\n'+'\n'.join(' '.join(r) for r in rows)+'\n'
        source = old/'lr'/f'{case["index"]:03d}.xcc'
        assert text == source.read_text() and len(rows) == case['options']
        result = graph_native.run(label, text, binary=built['binaries']['original']['path'], every=PERIOD)
        if result['status'] != 'completed':
            state.update(status='incomplete', terminal_case=label)
            mc.save(s.OUT/'fixed-queue.json', state)
            return
        expected = reference[f'lr/{case["index"]:03d}.xcc']['solutions']
        assert result['solutions'] == expected
        samples = check_samples(label, mono, h, rows)
        assert len(samples) == expected // PERIOD
        sample_file = OUT/f'{label}-sample-colors.txt'
        sample_file.write_text('\n'.join(samples)+'\n')
        record = dict(index=case['index'], label=label, solutions=expected, validated_samples=len(samples),
                      old_input_sha256=s.sha(source), metadata_sha256=s.sha(OUT/f'{label}.json'),
                      samples_sha256=s.sha(sample_file))
        state['done'].append(record)
        mc.save(s.OUT/'fixed-queue.json', state)
        print('ACCEPT', label, expected, 'solutions;', len(samples), 'validated samples', flush=True)
    total = sum(d['solutions'] for d in state['done'])
    assert total == 430444
    state.update(status='completed_accepted', finished_at_utc=datetime.now(timezone.utc).isoformat(),
                 current=None, total_solutions=total, orbit_size=4, essentially_distinct=total//4,
                 total_samples=sum(d['validated_samples'] for d in state['done']))
    mc.save(s.OUT/'fixed-queue.json', state)
    print('PASS129 fixed branch:', total, 'labeled;', total//4, 'orbits', flush=True)


if __name__ == '__main__':
    main()
