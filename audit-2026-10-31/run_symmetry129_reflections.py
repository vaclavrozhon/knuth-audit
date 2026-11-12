"""Independent native counterparts for archived TB/intersection bitset counts.

These27 cases previously had no native terminal records. Strong cases and
the two-axis intersection export every model; larger TB cases export every
hundredth. Old successful bitset searches are only read, never repeated.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import gzip
import json
import os
import re

import graph_native
import macmahon126 as mc
import symmetries129 as s

OUT = s.OUT/'reflections-native'
OLD = s.ROOT/'results/macmahon'


def validate_output(label, header, rows, mode, kind=None, mono=None):
    lookup = {tuple(sorted(r)): r for r in rows}
    sec = header[header.index('|')+1:]
    names = [n for n in sec if n.startswith('E')]
    strong = mode in ('badc', 'cdab', 'dcba')
    mapping = s.g.edge_system(False) if strong else None
    bases = sorted({v[0] for v in mapping.values()}) if strong else s.ES
    assert len(names) == len(bases)
    by_name = dict(zip(names, bases))
    models, selected = [], []

    def accept():
        values = {}
        for row in selected:
            for item in row:
                if ':' not in item:
                    continue
                n, c = item.split(':')
                if n not in by_name:
                    continue
                e = by_name[n]
                assert e not in values or values[e] == c
                values[e] = c
        if strong:
            colors = ''.join(mode[ord(values[mapping[e][0]])-97] if mapping[e][1] else values[mapping[e][0]] for e in s.ES)
        else:
            colors = ''.join(values[e] for e in s.ES)
        cc = s.validate(colors)
        axes = ('tb', 'lr') if mode == 'both' else ('tb',)
        for axis in axes:
            moved = s.cells(s.transform(colors, s.BY[axis]))
            assert all(s.g.patchmask(cc[t]) == s.g.patchmask(moved[t]) for t in s.TS)
        if strong:
            assert s.transform(colors, s.BY['r3'], mode) == colors
        if kind is not None:
            assert s.canonical_types(colors, 'tb') == [kind]
        if mono is not None:
            assert all(cc[tuple(t)] == c*3 for c, t in zip('abcd', mono))
        return colors

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


def cases():
    for kind, (a, bs, edge) in s.g.TB_TYPES.items():
        allowed = {'aaa': [a], 'ddd': [s.g.reflect(a, 'tb')],
                   'bbb': bs, 'ccc': [s.g.reflect(b, 'tb') for b in bs]}
        for mode in ('badc', 'cdab', 'dcba', 'weak'):
            strong = mode != 'weak'
            h, rows = s.g.reflection_options('tb', allowed, edge, strong, mode if strong else 'dcba')
            old = f'tb-{kind}'+(f'-strong-{mode}' if strong else '')+'.xcc'
            yield dict(label=Path(old).stem, old=old, header=h, rows=rows, mode=mode, kind=kind, period=1 if strong else 100)
    metadata = json.loads((OLD/'lr/metadata.json').read_text())
    for d in metadata:
        if not d.get('both'):
            continue
        old = f'lr/{d["index"]:03d}-both.xcc'
        lines = (OLD/old).read_text().splitlines()
        yield dict(label=f'lr-{d["index"]:03d}-both', old=old, header=lines[0].split(),
                   rows=[line.split() for line in lines[1:]], mode='both', mono=d['mono'], period=1)


def main():
    OUT.mkdir(exist_ok=True)
    graph_native.OUT = OUT
    reference = {d['label']: d['solutions'] for d in json.loads((OLD/'reflection-bitset-counts.json').read_text())}
    planned = list(cases())
    assert len(planned) == 27
    built = mc.build()
    state = dict(status='running', wrapper_pid=os.getpid(), started_at_utc=datetime.now(timezone.utc).isoformat(),
                 source_sha256=s.sha(__file__), geometry_sha256=s.sha(s.__file__),
                 old_counts_sha256=s.sha(OLD/'reflection-bitset-counts.json'),
                 expected_cases=27, timeout_seconds_per_case=172800, done=[])
    both_models = []
    for case in planned:
        label = case['label']
        state['current'] = label
        mc.save(s.OUT/'reflections-queue.json', state)
        text = ' '.join(case['header'])+'\n'+'\n'.join(' '.join(r) for r in case['rows'])+'\n'
        assert text == (OLD/case['old']).read_text()
        result = graph_native.run(label, text, binary=built['binaries']['original']['path'], every=case['period'])
        if result['status'] != 'completed':
            state.update(status='incomplete', terminal_case=label)
            mc.save(s.OUT/'reflections-queue.json', state)
            return
        assert result['solutions'] == reference[case['old']]
        models = validate_output(label, case['header'], case['rows'], case['mode'], case.get('kind'), case.get('mono'))
        assert len(models) == result['solutions']//case['period']
        path = OUT/f'{label}-colors.txt'
        path.write_text('\n'.join(models)+('\n' if models else ''))
        if case['mode'] == 'both':
            both_models.extend(models)
        state['done'].append(dict(label=label, old=case['old'], solutions=result['solutions'],
                                  validated_models=len(models), period=case['period'],
                                  old_input_sha256=s.sha(OLD/case['old']), metadata_sha256=s.sha(OUT/f'{label}.json'),
                                  colors_sha256=s.sha(path)))
        mc.save(s.OUT/'reflections-queue.json', state)
        print('ACCEPT', label, result['solutions'], 'solutions;', len(models), 'validated models', flush=True)
    assert len(both_models) == len(set(both_models)) == 1298
    orbits = Counter(s.axis_canonical(cs) for cs in both_models)
    hist = Counter(orbits.values())
    assert hist == {2: 261, 4: 194}
    for representative, size in orbits.items():
        flags = s.symmetry_flags(representative)
        assert ('r3' in flags['strong']) == (size == 2)
    state.update(status='completed_accepted', current=None, finished_at_utc=datetime.now(timezone.utc).isoformat(),
                 both_models=1298, both_orbits_by_size=dict(hist), both_weak_not_strong=194,
                 total_validated_models=sum(d['validated_models'] for d in state['done']))
    mc.save(s.OUT/'reflections-queue.json', state)
    print('PASS129 reflections and full two-axis quotient:', dict(hist), flush=True)


if __name__ == '__main__':
    main()
