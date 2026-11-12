"""Accept complete DLX137 artifacts without rerunning any enumerations or sampling."""
from datetime import datetime, timezone
import gzip
import hashlib
import json
import tarfile
import nuts137 as n


def read(path):
    return json.loads(path.read_text())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def check_native(label, get):
    raw = get(label + '.json')
    meta = json.loads(raw)
    assert meta['status'] == 'completed' and meta['returncode'] == 0
    for suffix, key in [('.dlx', 'input_sha256'), ('.out.gz', 'stdout_sha256'), ('.log', 'stderr_sha256')]:
        assert digest(get(label + suffix)) == meta[key]
    assert digest(gzip.decompress(get(label + '.out.gz'))) == meta['raw_stdout_sha256']
    assert n.sha(meta['source']) == meta['source_sha256']
    assert n.sha(n.ROOT / 'graph_native.py') == meta['runner_sha256']
    return meta, digest(raw)


def main():
    sources = {
        'figures-checked.json': 'extract_nuts137.py',
        'book-cases-checked.json': 'run_nuts137.py',
        'hand-certificate-checked.json': 'check_nuts137_hand.py',
        'sampling/run.json': 'sample_nuts137.cpp',
        'sampling/statistics-checked.json': 'check_nuts137_sampling.py',
        'sampling/calibration-checked.json': 'check_nuts137_sampling.py',
        'errata-check.json': 'check_nuts137_sources.py',
        'source-status.json': 'check_nuts137_sources.py',
    }
    data = {}
    for path, source in sources.items():
        item = read(n.OUT / path); data[path] = item
        assert item['source_sha256'] == n.sha(n.ROOT / source), path
        if 'geometry_sha256' in item:
            assert item['geometry_sha256'] == n.sha(n.__file__), path
    figures = data['figures-checked.json']
    assert figures['glyph_count'] == 126
    assert figures['book_sha256'] == n.sha(n.ROOT.parent / 'books/taocp-vol4b-ed1-print2-2022.pdf')
    for page, sha in figures['traces'].items():
        assert n.sha(n.OUT / ('page' + page + '-trace.xml')) == sha
    book = data['book-cases-checked.json']
    assert (book['primary_items'], book['secondary_items'], book['options']) == (14,12,259)
    assert [c['solutions'] for c in book['cases']] == [1,0,1,1]
    assert book['figure_sha256'] == n.sha(n.OUT / 'figures-checked.json')
    for case in book['cases']:
        meta, sha = check_native(case['case'], lambda p:(n.OUT / 'native' / p).read_bytes())
        assert sha == case['native_metadata_sha256']
        assert meta['solutions'] == case['solutions'] and case['full_set_equality']
    hand = data['hand-certificate-checked.json']
    assert hand['all_deletions_independently_replayed'] and hand['branch_choices'] == 7
    assert hand['book_cases_sha256'] == n.sha(n.OUT / 'book-cases-checked.json')
    run = data['sampling/run.json']
    assert run['status'] == 'completed' and run['returncode'] == 0
    assert run['runner_sha256'] == n.sha(n.ROOT / 'run_nuts137_sampling.py')
    assert run['records_gzip_sha256'] == n.sha(n.OUT / 'sampling/records.bin.gz')
    assert run['records_raw_sha256'] == digest(gzip.decompress((n.OUT / 'sampling/records.bin.gz').read_bytes()))
    assert run['stdout_sha256'] == n.sha(n.OUT / 'sampling/stdout.json')
    calibration = data['sampling/calibration-checked.json']
    assert calibration['experiment_sha256'] == n.sha(n.OUT / 'sampling/run.json')
    assert len(calibration['cases']) == 454
    manifest = read(n.OUT / 'sampling/native-calibration-files.json')
    with tarfile.open(n.OUT / 'sampling/native-calibration.tar.gz', 'r:gz') as archive:
        members = {m.name: m for m in archive.getmembers()}
        assert set(members) == set(manifest) and len(members) == 2724
        raw = {p:archive.extractfile(members[p]).read() for p in members}
        assert all(digest(raw[p]) == sha for p,sha in manifest.items())
        for case in calibration['cases']:
            label = f"sample-{case['sample']:06d}-{case['rule']}"
            meta, sha = check_native(label, raw.__getitem__)
            assert sha == case['native_metadata_sha256']
            assert meta['solutions'] == case['exact_count'] == len(case['models'])
            assert case['full_model_set_equal']
    stats = data['sampling/statistics-checked.json']
    assert stats['calibration_sha256'] == n.sha(n.OUT / 'sampling/calibration-checked.json')
    assert stats['records'] == run['trials'] == 1000000
    assert stats['strata_cross_checked'] == 16 and stats['exact_native_cases'] == 454
    assert [x['hits'] for x in stats['equal']] == [932090,53421,11057,3432]
    assert stats['unique_both']['hits'] == 4242
    errata = data['errata-check.json']
    assert errata['contexts_sha256'] == n.sha(n.OUT / 'errata-contexts.json')
    assert errata['correction137_found'] is False
    for path, sha in errata['local_files'].items():
        assert n.sha(n.ROOT.parent / path) == sha
    history = data['source-status.json']
    for path, sha in history['files'].items():
        assert n.sha(n.ROOT / path) == sha
    assert history['manufacturer']['equals_unique_book_solution']
    assert history['draft2019']['same_probability_wording']
    exact = read(n.OUT / 'census/accepted.json')
    assert exact['source_sha256'] == n.sha(n.ROOT / 'accept_nuts137_census.py')
    assert exact['all_orbits_exact_solution_count_checked'] and exact['global_completeness_independently_checked']
    assert exact['grouped_0_1_2_3plus'] == [55439557440,3180020160,662739120,205252200]
    for path, sha in exact['artifacts'].items():
        assert n.sha(n.OUT / 'census' / path) == sha
    for path, sha in exact['dependencies'].items():
        assert n.sha(n.ROOT / path) == sha
    extra = ['sampling/build.json', 'sampling/build.log', 'sampling/preflight-checked.json',
             'sampling/stdout.json', 'sampling/progress.log', 'sampling/records.bin.gz',
             'sampling/native-calibration.tar.gz', 'sampling/native-calibration-files.json',
             'errata-remote-check.json', 'errata-contexts.json', 'page140-trace.xml', 'page452-trace.xml']
    extra += [str(p.relative_to(n.OUT)) for p in sorted((n.OUT/'native').iterdir()) if p.suffix!='.lock']
    extra += ['census/accepted.json'] + ['census/' + p for p in exact['artifacts']]
    paths = sorted(set(sources) | set(extra))
    dependencies = sorted(set(sources.values()) | set(exact['dependencies']) | {
        'nuts137.py', 'run_nuts137_sampling.py', 'graph_native.py', 'extract_jigsaw.py',
        'accept_nuts137_census.py', 'sources/knuth-programs/dlx2.w', 'results/symmetry121_123/native/build.json'})
    n.save(n.OUT / 'accepted.json', dict(
        at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=n.sha(__file__),
        geometry_sha256=n.sha(n.__file__), exact_book_counts=[1,0,1,1],
        original_book_digits=126, manufacturer_digits=42,
        hand_deletion_certificate=True, sample_size=1000000,
        independent_full_model_set_comparisons=454,
        exact_census_type_sets=exact['total_type_sets'], exact_census_orbits=exact['nonempty_orbits'],
        exact_histogram_0_1_2_3plus=exact['grouped_0_1_2_3plus'], probability_candidate='C032',
        confirmed_new_findings=[], whole_exercise_status='partial',
        remaining=history['historical_limits'] + [
            'Resolve whether remaining1% warrants an erratum or merely a precision improvement; exact equality probabilities are now proved by the full census.'],
        artifacts={p:n.sha(n.OUT/p) for p in paths},
        dependencies={p:n.sha(n.ROOT/p) for p in dependencies}))
    print('PASS137 acceptance: four book cases,126 digits,1M trials,454 comparisons and exact census of all59,487,568,920 sets; C032 remains a candidate.')


if __name__ == '__main__':
    main()
