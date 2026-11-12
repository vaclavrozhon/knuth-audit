"""Validate the finished SGB5 DLX2 census without restarting either search."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import gzip
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/double_words'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def main():
    label = 'dlx-all-sgb5'
    meta_path = OUT / (label + '-run.json')
    meta = read(meta_path)
    result_path = OUT / (label + '.json')
    result = read(result_path)
    assert meta['status'] == 'finished' and meta['returncode'] == 0
    assert meta['config'] == result['config'] == dict(
        label=label, method='all', n=5, ospd=False, expected_total=323264)
    assert sha(result_path) == meta['result_sha256'] and result['verified']
    build = read(OUT / 'build.json')
    for name, digest in {**build['sources'], **meta['source_sha256']}.items():
        assert sha(ROOT / name) == digest, name
    assert sha(meta['command'][2]) == meta['binary_sha256'] == build['binaries']['all']['sha256']
    for suffix, key in [('.dlx', 'input_sha256'), ('.log', 'log_sha256'),
                        ('-double-models.txt.gz', 'models_sha256')]:
        assert sha(OUT / (label + suffix)) == meta[key]

    # Reconstruct the exact input independently of the encoding helper.
    dictionary = ROOT / 'sources/wordlists/words5-from-sgb'
    words = dictionary.read_text().upper().splitlines()
    assert len(words) == len(set(words)) == 5757
    assert all(len(w) == 5 and w.isascii() and w.isalpha() for w in words)
    rank = {w: i + 1 for i, w in enumerate(words)}
    primary = [f'a{i}' for i in range(5)] + [f'd{i}' for i in range(5)]
    with (OUT / (label + '.dlx')).open() as f:
        expected = primary + ['|'] + [f'{i}.{j}' for i in range(5) for j in range(5)]
        expected += words + [w + '@' for w in words]
        assert next(f).split() == expected
        for word in words:
            for slot in range(10):
                i = slot % 5
                tokens = [primary[slot]]
                tokens += [f'{i}.{j}:{c}' if slot < 5 else f'{j}.{i}:{c}'
                           for j, c in enumerate(word)]
                tokens += [word] + ([word + '@'] if slot in (0, 5) else [])
                assert next(f).split() == tokens
        assert not f.read()

    log = (OUT / (label + '.log')).read_text()
    match = re.search(r'Altogether (\d+) solutions, (\d+)\+(\d+)-(\d+) mems, '
                      r'(\d+) updates, (\d+) cleansings, (\d+) bytes, (\d+) nodes', log)
    assert match
    values = list(map(int, match.groups()))
    assert values[0] == result['count'] == meta['validated_solutions'] == 323264
    names = ['input_mems', 'search_mems', 'secondary_length_mems',
             'updates', 'cleansings', 'bytes', 'nodes']
    stats = dict(zip(names, values[1:]))
    stats['effective_mems'] = stats['search_mems'] - stats['secondary_length_mems']
    assert stats == result['statistics']
    assert stats['effective_mems'] == 14284514144977

    models, orbits, histogram = set(), set(), Counter()
    raw_xor = raw_sum = orbit_xor = orbit_sum = 0
    best = {1720: [], 1800: []}
    modulus = 1 << 256
    with gzip.open(OUT / (label + '-double-models.txt.gz'), 'rt') as f:
        for line in f:
            rows = tuple(line.split())
            assert len(rows) == 5 and all(w in rank for w in rows)
            cols = tuple(''.join(rows[i][j] for i in range(5)) for j in range(5))
            assert all(w in rank for w in cols) and len(set(rows + cols)) == 10
            assert rank[rows[0]] < rank[cols[0]]
            assert rows not in models
            models.add(rows)
            key = min(rows, cols)
            assert key not in orbits
            orbits.add(key)
            cost = max(rank[w] for w in rows + cols)
            histogram[cost] += 1
            if cost in best:
                best[cost].append(key)
            h = int(sha256_text(''.join(rows)), 16)
            raw_xor ^= h
            raw_sum = (raw_sum + h) % modulus
            h = int(sha256_text(''.join(key)), 16)
            orbit_xor ^= h
            orbit_sum = (orbit_sum + h) % modulus
    assert len(models) == len(orbits) == result['double_count'] == result['double_orbits'] == 323264
    assert meta['validated_double'] == 323264 and result['repeated'] == result['symmetric'] == 0
    assert result['book_total_matches']
    assert {str(k): v for k, v in sorted(histogram.items())} == result['rank_histogram']
    assert sorted(histogram)[:2] == result['best_two_distinct_ranks'] == [1720, 1800]
    assert [len(best[1720]), len(best[1800])] == [1, 3]
    for key, value in [('sha256_xor', raw_xor), ('sha256_sum', raw_sum),
                       ('double_canonical_sha256_xor', orbit_xor), ('double_canonical_sha256_sum', orbit_sum),
                       ('orbit_sha256_xor', orbit_xor), ('orbit_sha256_sum', orbit_sum)]:
        assert result[key] == f'{value:064x}', key
    for cost, witnesses in result['witnesses'].items():
        for rows in witnesses:
            assert tuple(rows) in models
            cols = tuple(''.join(rows[i][j] for i in range(5)) for j in range(5))
            assert max(rank[w] for w in tuple(rows) + cols) == int(cost)

    # Compare with the previously accepted independent cell count; its full
    # raw models were not saved, so do not claim a cross-solver set comparison.
    cell_path = ROOT / 'results/word_rectangles/cell-5x5.json'
    cell = read(cell_path)
    cell_run_path = ROOT / 'results/word_rectangles/cell-5x5-run.json'
    cell_run = read(cell_run_path)
    assert cell['verified'] and cell_run['returncode'] == 0
    assert cell['count'] == cell_run['validated_solutions'] == 1787056
    assert cell['repeated_words'] == 1140528
    assert (cell['count'] - cell['repeated_words']) == 2 * len(orbits)
    artifacts = [meta_path, result_path, OUT / (label + '.dlx'), OUT / (label + '.log'),
                 OUT / (label + '-double-models.txt.gz'), OUT / 'build.json',
                 dictionary, cell_path, cell_run_path]
    accepted = dict(
        checked_at_utc=datetime.now(timezone.utc).isoformat(), script_sha256=sha(__file__),
        finished_at_utc=meta['finished_at_utc'], wrapper_pid=meta['wrapper_pid'],
        status='verified', complete_double_squares=len(models), transpose_classes=len(orbits),
        all_stored_models_valid_unique_and_transpose_distinct=True,
        rank_histogram_matches=True, best_two_ranks=[1720, 1800], best_orbits=best,
        exact_input_reconstructed=True, statistics=stats,
        independent_cell_count_matches=True, complete_cross_solver_set_comparison=False,
        historical_15T_reproduced=False,
        scope='Complete native DLX2 count matches the earlier independent cell count. '
              'All 323264 saved native models were checked directly. Raw solver stdout '
              'has only its streaming hash; the complete row-word model list is archived. '
              '14.284514144977T net search mems do not reproduce the historical 15T. '
              'No search restarted; exercise87 remains partial only for the benchmark.',
        artifacts={str(p.relative_to(ROOT)): sha(p) for p in artifacts})
    (OUT / 'sgb5-terminal-checked.json').write_text(json.dumps(accepted, indent=2) + '\n')
    print('PASS SGB5: all 323264 saved models and transpose classes validated; '
          'independent count agrees; net 14.284514144977T mems; historical 15T remains open.')


def sha256_text(value):
    return hashlib.sha256(value.encode()).hexdigest()


if __name__ == '__main__':
    main()
