"""Compare completed full model sets; never launch or repeat a search."""
from datetime import datetime, timezone
import gzip, json
import macmahon126 as mc


def read(path):
    with gzip.open(path, 'rt') as f:
        rows = [line.strip() for line in f]
    assert len(rows) == len(set(rows)), path
    return set(rows)


def main():
    accepted = []
    for mode, expected in [('center-up', 2138), ('center-down', 2670), ('anchored', 987816)]:
        p = mc.OUT/'bitset'/(mode+'-bitset.json')
        bit = json.loads(p.read_text())
        assert bit['status'] == 'completed' and bit['returncode'] == 0
        assert bit['solutions'] == bit['validated_models'] == expected
        for name, digest in bit['files'].items():
            assert mc.sha(p.parent/name) == digest
        label = mode + ('-tile-colors' if mode == 'anchored' else '-original')
        checked = mc.OUT/(label+'-checked.json')
        native = json.loads(checked.read_text())
        assert native['status'] == 'completed' and native['model_period'] == 1
        term = mc.OUT/'native'/(label+'.json')
        assert mc.sha(term) == native['native_sha256']
        raw = json.loads(term.read_text())
        assert raw['status'] == 'completed' and raw['returncode'] == 0
        for suffix, field in [('.dlx','input_sha256'),('.log','stderr_sha256'),('.out.gz','stdout_sha256')]:
            assert mc.sha(term.parent/(label+suffix)) == raw[field]
        colors = mc.OUT/native['models_file']
        assert mc.sha(colors) == native['models_sha256']
        left = read(colors)
        if mode == 'anchored':
            assert bit['orbit_count'] == 164636 and bit['orbit_sizes'] == {'6':164636}
            canonical = {mc.orbit_key(s) for s in left}
            right = read(p.parent/(mode+'-bitset.orbits.txt.gz'))
            assert len(left) == len(canonical) == len(right) == 164636
            assert canonical == right
            comparison = 'Complete color-orbit sets equal; every independent orbit has six labeled models.'
        else:
            right = read(p.parent/(mode+'-bitset.models.txt.gz'))
            assert len(left) == len(right) == expected and left == right
            comparison = 'Complete labeled edge-color sets equal.'
        accepted.append(dict(mode=mode, independent_solutions=expected, native_models=len(left),
                             comparison=comparison, native_metadata_sha256=mc.sha(checked),
                             independent_metadata_sha256=mc.sha(p)))
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  script_sha256=mc.sha(__file__), comparisons=accepted,
                  scope='Compares existing complete validated output sets of two distinct solvers. No new search. The unconstrained full count follows separately from the proved twelve spatial positions.')
    mc.save(mc.OUT/'cross-solver-checked.json', result)
    print('PASS: both complete center sets and all164636 full-puzzle color orbits agree.')


if __name__ == '__main__':
    main()
