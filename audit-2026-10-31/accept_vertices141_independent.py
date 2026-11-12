"""Accept the completed geometric census, then audit every orbit and subcount.

This never launches a solver and does not claim agreement with a pending DLX run.
"""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import gzip
import hashlib
import json
import vertices141 as h


def read(path):
    return json.loads(path.read_text())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sides(word, vv, width, height):
    colors = dict(zip(vv, word))
    return {name: ''.join(colors[v] for v in sequence) for name, sequence in [
        ('left', [(0, y) for y in range(height+1)]),
        ('right', [(width, y) for y in range(height+1)]),
        ('bottom', [(x, 0) for x in range(width+1)]),
        ('top', [(x, height) for x in range(width+1)])]}


def main():
    base = h.OUT/'independent'
    terminal = read(base/'terminal.json')
    assert terminal['status'] == 'completed' and terminal['returncode'] == 0
    for name, expected in terminal['source_sha256'].items():
        assert h.sha(h.ROOT/name) == expected, name
    for key, path in [('input_sha256', base/'cases.txt'),
                      ('binary_sha256', Path(terminal['command'][-1])),
                      ('stderr_sha256', base/'stderr.log'),
                      ('compressed_sha256', base/'stdout.txt.gz')]:
        assert terminal[key] == h.sha(path), key
    assert (base/'cases.txt').read_text() == ''.join(
        h.independent_case(label, h.cells(w, ht, holes)) for label, w, ht, holes in h.CASES)
    raw = gzip.open(base/'stdout.txt.gz', 'rb').read()
    assert digest(raw) == terminal['stdout_sha256']
    models, counts, nodes = defaultdict(set), {}, {}
    for line in raw.decode().splitlines():
        parts = line.split()
        if parts[0] == 'M':
            _, label, word = parts
            assert label not in counts and word not in models[label]
            assert h.color_key(word) == word
            models[label].add(word)
        else:
            assert parts[0] == 'C' and len(parts) == 4
            label = parts[1]
            assert label not in counts
            counts[label], nodes[label] = map(int, parts[2:])
            assert counts[label] == len(models[label])
    assert list(counts) == [c[0] for c in h.CASES]
    expected_log = [f'COMPLETED {label} {counts[label]} {nodes[label]}' for label in counts]
    assert (base/'stderr.log').read_text().splitlines() == expected_log+['ALL_COMPLETED 3']
    figures = read(h.OUT/'figures-checked.json')['figures']
    summaries, representatives, special_models = {}, {}, {}
    for label, width, height, holes in h.CASES:
        board = h.cells(width, height, holes)
        vv = h.vertices(board)
        # Direct coordinate/rotation validator, independent of solver internals.
        indices = {v: i for i, v in enumerate(vv)}
        corners = [[indices[v] for v in [(x,y), (x+1,y), (x+1,y+1), (x,y+1)]]
                   for x, y in board]
        inventory = set(h.inventory()[1])
        for word in models[label]:
            assert len(word) == len(vv) and set(word) == set('abc')
            tiles = []
            for cell in corners:
                local = ''.join(word[j] for j in cell)
                tiles.append(min(local[k:]+local[:k] for k in range(4)))
            assert len(set(tiles)) == 24 and set(tiles) == inventory
        group = h.geometry_maps(board)
        seen, reps, orbit_sizes = set(), [], Counter()
        for word in sorted(models[label]):
            if word in seen:
                continue
            images = {h.color_key(''.join(word[j] for j in mapping)) for mapping in group}
            assert images <= models[label] and not (images & seen)
            assert min(images) == word
            seen.update(images); reps.append(word); orbit_sizes[len(images)] += 1
        assert seen == models[label]
        assert orbit_sizes == Counter({len(group): len(reps)})
        printed = figures[label]['vertex_colors']
        assert h.color_key(printed) in models[label]
        representatives[label] = reps
        summary = dict(color_classes=len(models[label]), geometric_classes=len(reps),
                       symmetry_order=len(group), orbit_sizes=dict(orbit_sizes),
                       independent_nodes=nodes[label], printed_figure_is_solution=True)
        if label == 'hole5':
            hole_indices = [indices[v] for v in [(2,2), (3,2), (3,3), (2,3)]]
            uniform = [word for word in reps if len({word[j] for j in hole_indices}) == 1]
            matching = []
            for word in uniform:
                side = sides(word, vv, width, height)
                if side['left'] == side['right'] or side['bottom'] == side['top']:
                    matching.append(word)
            summary.update(uniform_hole=len(uniform), uniform_hole_with_opposite_match=len(matching))
            special_models[label] = dict(uniform_hole=uniform, matching=matching)
        else:
            cylindrical, uniform, same_partitions = [], [], []
            for word in reps:
                side = sides(word, vv, width, height)
                if side['left'] == side['right']:
                    cylindrical.append(word)
                    if len(set(side['left'])) == 1:
                        uniform.append(word)
                if (h.color_key(side['left']) == h.color_key(side['right']) and
                    h.color_key(side['bottom']) == h.color_key(side['top'])):
                    same_partitions.append(word)
            families = defaultdict(set)
            cylindrical_set = set(cylindrical)
            for word in cylindrical:
                colors = dict(zip(vv, word))
                cuts = set()
                for shift in range(width):
                    shifted = h.color_key(''.join(colors[((x+shift) % width, y)] for x, y in vv))
                    assert shifted in models[label]
                    cuts.add(h.geometric_key(shifted, group))
                assert cuts <= cylindrical_set and len(cuts) == width
                families[min(cuts)].add(word)
            assert Counter(map(len, families.values())) == Counter({width: len(families)})
            summary.update(cylindrical=len(cylindrical), cylinder_families=len(families),
                           cylinder_family_sizes=dict(Counter(map(len, families.values()))),
                           same_solid_left_right=len(uniform),
                           same_opposite_partitions=len(same_partitions))
            special_models[label] = dict(cylindrical=cylindrical, uniform=uniform,
                                         same_partitions=same_partitions,
                                         cylinder_families={k: sorted(v) for k, v in families.items()})
            if label == 'rect4x6':
                assert same_partitions == [h.geometric_key(printed, group)]
        summaries[label] = summary
        print(label, json.dumps(summary), flush=True)
    assert [summaries[l]['color_classes'] for l in counts] == [138248, 49336, 147708]
    assert [summaries[l]['geometric_classes'] for l in counts] == [17281, 12334, 36927]
    assert summaries['hole5']['uniform_hole'] == 209
    assert summaries['hole5']['uniform_hole_with_opposite_match'] == 6
    assert summaries['rect4x6']['cylindrical'] == 180
    assert summaries['rect4x6']['cylinder_families'] == 30
    assert summaries['rect4x6']['same_opposite_partitions'] == 1
    assert summaries['rect3x8']['cylindrical'] == 1536
    assert summaries['rect3x8']['cylinder_families'] == 192
    assert summaries['rect3x8']['same_solid_left_right'] == 42
    h.save(h.OUT/'geometric-representatives.json', representatives)
    h.save(h.OUT/'special-models.json', special_models)
    h.save(h.OUT/'independent-accepted.json', dict(at_utc=datetime.now(timezone.utc).isoformat(),
        checker_sha256=h.sha(__file__), geometry_sha256=h.sha(h.__file__),
        terminal_sha256=h.sha(base/'terminal.json'), figures_sha256=h.sha(h.OUT/'figures-checked.json'),
        representatives_sha256=h.sha(h.OUT/'geometric-representatives.json'),
        special_models_sha256=h.sha(h.OUT/'special-models.json'), cases=summaries,
        all_models_directly_validated=sum(counts.values()), all_printed_counts_match=True,
        scope='Completed geometric census and all printed subcounts; native full-set comparison remains separate.'))
    print('PASS: every geometric model, all board orbits, all printed cylinder/hole/partition counts.')


if __name__ == '__main__':
    main()
