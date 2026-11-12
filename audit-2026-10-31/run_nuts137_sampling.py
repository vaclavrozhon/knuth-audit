"""Record a preselected one-million-trial experiment and its immutable build."""
from datetime import datetime, timezone
from pathlib import Path
import gzip
import json
import os
import random
import subprocess
import tempfile
import nuts137 as n


def now():
    return datetime.now(timezone.utc).isoformat()


def main():
    out = n.OUT / 'sampling'
    out.mkdir(exist_ok=True)
    assert not (out / 'run.json').exists(), 'Never silently overwrite an existing experiment.'
    build = Path(tempfile.mkdtemp(prefix='knuth-vol4b-nuts137-native-'))
    binary = build / 'sample-nuts137'
    source = n.ROOT / 'sample_nuts137.cpp'
    command = ['g++', '-std=c++17', '-O3', '-Wall', '-Wextra', str(source), '-o', str(binary)]
    compilation = subprocess.run(command, capture_output=True, text=True)
    (out / 'build.log').write_text(compilation.stdout + compilation.stderr)
    assert compilation.returncode == 0
    n.save(out / 'build.json', dict(command=command, source_sha256=n.sha(source),
                                  binary=str(binary), binary_sha256=n.sha(binary),
                                  compiler=subprocess.check_output(['g++', '--version'], text=True)))
    # Validate the new optimized counter before launching the large experiment.
    book = json.loads((n.OUT / 'book-cases-checked.json').read_text())
    cases = [book['cases'][i]['nuts'] for i in (0, 2)]
    rng = random.Random(13720261102)
    cases += [sorted(rng.sample(n.TYPES, 7)) for _ in range(128)]
    cases += [['123456', '123465', '123546', '123564', '142356', '142635', '152634']]
    rows = '\n'.join(' '.join(str(n.TYPES.index(x)) for x in case) for case in cases) + '\n'
    actual = subprocess.check_output([str(binary), '--cases'], input=rows, text=True).splitlines()
    assert len(actual) == len(cases)
    checks = []
    for i, (case, row) in enumerate(zip(cases, actual)):
        counts = list(map(int, row.split()))
        if i < 2:
            expected = [book['cases'][2*i+j]['solutions'] for j in (0, 1)]
        else:
            expected = [len(n.ring_search(case, rule)[0]) for rule in ('equal', 'sum7')]
        assert counts == expected, (case, counts, expected)
        checks.append(dict(nuts=case, exact_counts=counts))
    n.save(out / 'preflight-checked.json', dict(
        cases=checks, full_counts_equal=True, geometry_sha256=n.sha(n.__file__),
        source_sha256=n.sha(source), binary_sha256=n.sha(binary),
        book_cases_reused_without_search=True))
    # This sample size and seed are chosen before inspecting the probabilities.
    trials, seed = 1000000, 20261102137
    records = out / 'records.bin'
    command = [str(binary), str(trials), str(seed), str(records)]
    meta = dict(status='running', started_at_utc=now(), wrapper_pid=os.getpid(),
                trials=trials, seed=seed, command=command, runner_sha256=n.sha(__file__),
                source_sha256=n.sha(source), binary_sha256=n.sha(binary),
                sampling='Seven distinct types by rejection from unbiased bounded MT19937-64 draws; sorted, independently repeated.',
                classification='Counts capped at three; axes equal and sum7, classes 0,1,2,at least3.')
    n.save(out / 'run.json', meta)
    with (out / 'stdout.json').open('w') as stdout, (out / 'progress.log').open('w') as stderr:
        child = subprocess.Popen(command, stdout=stdout, stderr=stderr)
        meta['pid'] = child.pid
        n.save(out / 'run.json', meta)
        rc = child.wait()
    meta.update(returncode=rc, finished_at_utc=now(), status='completed' if rc == 0 else 'failed')
    assert rc == 0
    assert records.stat().st_size == 9 * trials
    meta['records_raw_sha256'] = n.sha(records)
    with records.open('rb') as src, gzip.open(out / 'records.bin.gz', 'wb') as dst:
        while block := src.read(1024 * 1024):
            dst.write(block)
    meta['records_gzip_sha256'] = n.sha(out / 'records.bin.gz')
    meta['stdout_sha256'] = n.sha(out / 'stdout.json')
    n.save(out / 'run.json', meta)
    print(json.dumps(meta, indent=2), flush=True)


if __name__ == '__main__':
    main()
