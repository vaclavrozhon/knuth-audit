"""Check every sample record, and two independent full solvers on stratified cases."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
import gzip
import hashlib
import json
import math
import re
import subprocess
import nuts137 as n
import graph_native as native


def wilson(hits, total):
    z = 1.959963984540054
    p = hits / total
    center = (p + z*z/(2*total)) / (1 + z*z/total)
    radius = z * math.sqrt(p*(1-p)/total + z*z/(4*total*total)) / (1+z*z/total)
    return [center-radius, center+radius]


def main():
    out = n.OUT / 'sampling'
    assert not (out / 'calibration-checked.json').exists(), 'Reuse accepted calibration; do not rerun.'
    meta = json.loads((out / 'run.json').read_text())
    assert meta['status'] == 'completed' and meta['returncode'] == 0
    assert meta['source_sha256'] == n.sha(n.ROOT / 'sample_nuts137.cpp')
    assert meta['runner_sha256'] == n.sha(n.ROOT / 'run_nuts137_sampling.py')
    assert meta['stdout_sha256'] == n.sha(out / 'stdout.json')
    assert meta['records_gzip_sha256'] == n.sha(out / 'records.bin.gz')
    data = gzip.decompress((out / 'records.bin.gz').read_bytes())
    assert hashlib.sha256(data).hexdigest() == meta['records_raw_sha256']
    trials = meta['trials']
    assert len(data) == 9 * trials
    histogram, occurrences, by_class = Counter(), Counter(), defaultdict(list)
    selected = set(range(128))
    for i in range(trials):
        row = data[9*i:9*i+9]
        assert len(set(row[:7])) == 7 and list(row[:7]) == sorted(row[:7]) and row[6] < 120
        assert row[7] <= 3 and row[8] <= 3
        bucket = tuple(row[7:])
        histogram[bucket] += 1
        occurrences.update(row[:7])
        if len(by_class[bucket]) < 8:
            by_class[bucket].append(i)
            selected.add(i)
    summary = json.loads((out / 'stdout.json').read_text())
    assert summary['histogram'] == [[histogram[i,j] for j in range(4)] for i in range(4)]
    assert summary['type_occurrences'] == [occurrences[i] for i in range(120)]
    cases = [list(data[9*i:9*i+7]) for i in sorted(selected)]
    binary = json.loads((out / 'build.json').read_text())['binary']
    assert n.sha(binary) == meta['binary_sha256']
    rows = '\n'.join(' '.join(map(str, x)) for x in cases) + '\n'
    cpp = subprocess.check_output([binary, '--cases'], input=rows, text=True).splitlines()
    assert len(cpp) == len(cases)
    dlx_build = json.loads((n.ROOT / 'results/symmetry121_123/native/build.json').read_text())
    dlx = dlx_build['binaries']['original']['binary']
    assert n.sha(dlx) == dlx_build['binaries']['original']['sha256']
    native.OUT = out / 'native-calibration'; native.OUT.mkdir(exist_ok=True)
    checked = []
    for i, ids, counts in zip(sorted(selected), cases, cpp):
        nuts = [n.TYPES[t] for t in ids]
        counts = list(map(int, counts.split()))
        for r, rule in enumerate(['equal', 'sum7']):
            label = f'sample-{i:06d}-{rule}'
            enc = n.problem(nuts, rule)
            result = native.run(label, n.native_text(enc), binary=dlx, limit=120)
            assert result['status'] == 'completed' and result['returncode'] == 0
            lookup = {tuple(sorted(row)): k for k, row in enumerate(enc['rows'])}
            models, chosen = [], []

            def accept():
                assert len(chosen) == 7
                words = [''] * 7
                for k in chosen:
                    pos, word = enc['placements'][k]
                    assert not words[pos]
                    words[pos] = word
                n.validate(words, nuts, rule)
                assert words[0][0] == '1'
                return '/'.join(words)

            with gzip.open(native.OUT / (label + '.out.gz'), 'rt') as stream:
                for line in stream:
                    if re.fullmatch(r'\d+:\s*', line):
                        if chosen:
                            models.append(accept()); chosen = []
                    elif line.strip():
                        row = re.sub(r'\s*\(\d+ of \d+\)\s*$', '', line).split()
                        chosen.append(lookup[tuple(sorted(row))])
            if chosen:
                models.append(accept())
            independent, _ = n.ring_search(nuts, rule)
            assert sorted(models) == independent
            assert counts[r] == len(models) == result['solutions']
            assert min(3, counts[r]) == data[9*i+7+r]
            checked.append(dict(sample=i, nuts=nuts, rule=rule, exact_count=counts[r],
                                full_model_set_equal=True, models=independent,
                                native_metadata_sha256=n.sha(native.OUT / (label + '.json'))))
        if len(checked) % 64 == 0:
            print('Validated', len(checked), 'complete native/Python searches', flush=True)
    n.save(out / 'calibration-checked.json', dict(
        at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=n.sha(__file__),
        cpp_sha256=n.sha(n.ROOT / 'sample_nuts137.cpp'), geometry_sha256=n.sha(n.__file__),
        experiment_sha256=n.sha(out / 'run.json'), cases=checked,
        selection='First128 records plus first8 in each of16 joint strata (all5 in rare3+/3+ stratum).',
        full_set_equality=True, capped_counts_agree=True,
        independent_method='Original DLX2 whole model sets versus forced-rotation Python enumeration; optimized C++ full counts also agree.'))
    equal = [sum(histogram[i,j] for j in range(4)) for i in range(4)]
    sum7 = [sum(histogram[i,j] for i in range(4)) for j in range(4)]
    estimate = lambda hits: dict(hits=hits, probability=hits/trials,
                                 iid_95pct_wilson_interval=wilson(hits, trials))
    n.save(out / 'statistics-checked.json', dict(
        at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=n.sha(__file__),
        experiment_sha256=n.sha(out / 'run.json'),
        calibration_sha256=n.sha(out / 'calibration-checked.json'),
        records=trials, all_records_well_formed=True,
        finite_population=math.comb(120, 7),
        equal=[estimate(x) for x in equal], sum7=[estimate(x) for x in sum7],
        unique_both=estimate(histogram[1,1]),
        histogram=summary['histogram'], strata_cross_checked=len(by_class),
        exact_native_cases=len(checked),
        statistical_scope='Pseudorandom Monte Carlo, not exhaustive finite-population counting. '
          'Wilson intervals assume independent uniform samples, not a proof of MT19937 independence '
          'or a certified bound. Selection is uniform over120 choose7 under that assumption.',
        book_percentages=[93,5,1,1],
        conclusion='The first three coarse book percentages and0.4% joint uniqueness are supported. '
          'The final remaining1% is materially higher than the observed0.3432%; retain a candidate '
          'about coarse rounding, not a confirmed exact mathematical error.'))
    print('PASS137: all1M records;16 strata; native whole model sets and both counters agree.', flush=True)


if __name__ == '__main__':
    main()
