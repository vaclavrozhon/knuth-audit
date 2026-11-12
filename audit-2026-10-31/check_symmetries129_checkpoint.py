"""Accept the129 block and one completed127 boundary, without new searches."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import gzip
import hashlib
import json
import re
import sqlite3
import subprocess
import sys
from urllib.request import urlopen

import symmetries129 as s


def read(path):
    return json.loads(Path(path).read_text())


def native(path):
    m = read(path)
    assert m['status'] == 'completed' and m['returncode'] == 0
    assert read(path.with_name(path.stem+'-run.json')) == m
    for suffix, key in [('.dlx', 'input_sha256'), ('.log', 'stderr_sha256'), ('.out.gz', 'stdout_sha256')]:
        assert s.sha(path.with_name(path.stem+suffix)) == m[key]
    assert s.sha(m['command'][2]) == m['binary_sha256']
    assert s.sha(m['source']) == m['source_sha256']
    assert s.sha(s.ROOT/'graph_native.py') == m['runner_sha256']
    with gzip.open(path.with_name(path.stem+'.out.gz'), 'rb') as f:
        assert hashlib.file_digest(f, 'sha256').hexdigest() == m['raw_stdout_sha256']
    terminal = re.search(r'Altogether (\d+) solutions?, (\d+)\+(\d+)(?:-(\d+))? mems, .*?, (\d+) nodes', path.with_suffix('.log').read_text())
    assert terminal and tuple(int(v or 0) for v in terminal.groups()) == tuple(m[k] for k in ['solutions', 'initial_mems', 'search_mems', 'unmems', 'nodes'])
    assert m['net_search_mems'] == m['search_mems']-m['unmems']
    return dict(path=str(path.relative_to(s.ROOT)), solutions=m['solutions'], sha256=s.sha(path))


def main():
    baseline = Path(sys.argv[1])
    repo = s.ROOT.parent
    accepted = [native(s.OUT/'native/literal-strong-rotation.json')]
    literal = read(s.OUT/'literal-strong-rotation-checked.json')
    assert literal['source_sha256'] == s.sha(s.ROOT/'run_symmetry129_literal.py')
    assert literal['native_metadata_sha256'] == s.sha(s.OUT/'native/literal-strong-rotation.json')
    assert literal['old_independent_metadata_sha256'] == s.sha(s.ROOT/'results/macmahon/additional-bitset-counts.json')
    assert literal['solutions'] == 68024064 and literal['validated_samples'] == 680
    assert literal['net_search_mems'] == 453526853015 and literal['rounded_teramems'] == literal['book_teramems'] == .5
    assert s.sha(s.OUT/literal['models_file']) == literal['models_sha256']

    fixed = read(s.OUT/'fixed-queue.json')
    assert fixed['status'] == 'completed_accepted' and len(fixed['done']) == 32
    assert fixed['runner_sha256'] == s.sha(s.ROOT/'run_symmetry129_fixed.py')
    assert fixed['geometry_sha256'] == s.sha(s.__file__)
    assert fixed['old_count_sha256'] == s.sha(s.ROOT/'results/macmahon/reflection-bitset-counts.json')
    assert fixed['total_solutions'] == 430444 and fixed['essentially_distinct'] == 107611 and fixed['total_samples'] == 4288
    for case in fixed['done']:
        path = s.OUT/'fixed-native'/f'{case["label"]}.json'
        accepted.append(native(path))
        assert s.sha(path) == case['metadata_sha256']
        assert read(path)['solutions'] == case['solutions']
        assert s.sha(s.ROOT/'results/macmahon/lr'/f'{case["index"]:03d}.xcc') == case['old_input_sha256']
        assert s.sha(path.with_name(path.stem+'-sample-colors.txt')) == case['samples_sha256']

    reflections = read(s.OUT/'reflections-queue.json')
    assert reflections['status'] == 'completed_accepted' and len(reflections['done']) == 27
    assert reflections['source_sha256'] == s.sha(s.ROOT/'run_symmetry129_reflections.py')
    assert reflections['geometry_sha256'] == s.sha(s.__file__)
    assert reflections['old_counts_sha256'] == s.sha(s.ROOT/'results/macmahon/reflection-bitset-counts.json')
    assert reflections['both_models'] == 1298 and reflections['both_orbits_by_size'] == {'2': 261, '4': 194}
    for case in reflections['done']:
        path = s.OUT/'reflections-native'/f'{case["label"]}.json'
        accepted.append(native(path))
        assert s.sha(path) == case['metadata_sha256']
        assert read(path)['solutions'] == case['solutions']
        assert s.sha(s.ROOT/'results/macmahon'/case['old']) == case['old_input_sha256']
        assert s.sha(path.with_name(path.stem+'-colors.txt')) == case['colors_sha256']

    border_out = s.ROOT/'results/borders127_128'
    side = read(border_out/'side11-count-checked.json')
    accepted.append(native(border_out/'counts-native/side11.json'))
    assert side['native_sha256'] == s.sha(border_out/'counts-native/side11.json')
    assert side['model_sha256'] == s.sha(s.ROOT/'borders127_128.py')
    assert side['runner_sha256'] == s.sha(s.ROOT/'run_border_counts127.py')
    assert side['color_orbits'] == 24310208 and side['labeled_solutions'] == 48620416 and side['validated_samples'] == 243
    assert len(accepted) == 61

    proof = read(s.OUT/'geometric-proofs.json')
    assert proof['source_sha256'] == s.sha(s.__file__)
    assert proof['geometry_source_sha256'] == s.sha(s.g.__file__)
    assert [p['configurations'] for p in proof['selectors']] == [408, 168]
    assert all(c['accepted_transforms'] == 2 for p in proof['selectors'] for c in p['cases'])
    figures = read(s.OUT/'original-figures-checked.json')
    assert figures['source_sha256'] == s.sha(s.ROOT/'extract_symmetry129_figures.py')
    assert figures['geometry_source_sha256'] == s.sha(s.__file__)
    assert figures['book_sha256'] == s.sha(repo/'books/taocp-vol4b-ed1-print2-2022.pdf')
    assert figures['total_wedges'] == 360 and len(figures['figures']) == 5
    for p, h in figures['trace_sha256'].items():
        assert s.sha(s.OUT/f'page{p}-trace.xml') == h
    counts = read(s.OUT/'counts-reconciled.json')
    assert counts['source_sha256'] == s.sha(s.ROOT/'check_symmetry129_counts.py')
    for name, h in (counts['dependencies_sha256'] | counts['reused_evidence_sha256']).items():
        assert s.sha(s.ROOT/name) == h
    assert counts['totals']['any_symmetry_essentially_distinct'] == 2362048
    assert counts['total_lr_weak_not_strong'] == 294457 and counts['corrected_lr_difference'] == 12839

    errata = read(s.OUT/'errata-check.json')
    assert len(errata['local_files']) == 6
    for name, h in errata['local_files'].items():
        assert s.sha(repo/name) == h
    assert s.sha(s.ROOT/errata['remote_check_source']) == errata['remote_check_source_sha256']
    assert all(x['unchanged'] for x in errata['remote_files'])
    assert s.sha(s.OUT/errata['contexts_file']) == errata['contexts_sha256']
    for source in read(s.ROOT/'sources/symmetries129/retrieval.json'):
        assert source['status'] == 200 and s.sha(s.ROOT/source['file']) == source['sha256']
    history = read(s.ROOT/'sources/symmetries129/history-search.json')
    assert history['not_established'] and history['archive_search']['num_found'] == 0
    assert s.sha(s.ROOT/history['archive_search']['file']) == history['archive_search']['sha256']

    ledger = read(s.ROOT/'ledger.json')
    items = {x['id']: x for x in ledger['items']}
    old = read(baseline/'audit-2026-10-31/ledger.json')
    changed = {'F065', 'X127', 'X129'}
    assert len(items) == len(ledger['items']) == len(old['items'])+1 == 491
    for item in old['items']:
        if item['id'] in changed:
            assert set(item['evidence']) <= set(items[item['id']]['evidence'])
        else:
            assert item == items[item['id']], item['id']
    assert items['F065']['status'] == 'confirmed' and items['E065']['status'] == 'known_erratum'
    assert items['X127']['status'] == items['X129']['status'] == 'partial'
    for id in changed | {'E065'}:
        for path in items[id]['evidence']:
            assert (s.ROOT/path).is_file(), (id, path)
    full = read(s.ROOT/'full-review.json')
    previous = read(baseline/'audit-2026-10-31/full-review.json')
    assert len(full['exercises']) == 1202 and len(full['pages']) == 734
    for before, after in zip(previous['exercises'], full['exercises']):
        if before['id'] in ('DLX:127', 'DLX:129'):
            assert after['status'] == 'partial' and set(before['evidence']) <= set(after['evidence'])
        else:
            assert before == after, before['id']
    for before, after in zip(previous['pages'], full['pages']):
        if before['printed_page'] not in (138, 139, 448, 449):
            assert before == after, before['pdf_page']
    assert Counter(x['status'] for x in full['exercises']) == {'reviewed': 137, 'partial': 71, 'pending': 994}
    assert Counter(x['status'] for x in full['pages']) == {'reviewed': 28, 'partial': 96, 'pending': 610}
    assert next(p for p in full['pages'] if p['printed_page'] == 448)['status'] == 'reviewed'

    sys.path.insert(0, str(repo/'review-ui'))
    import server
    curated = read(repo/'review-ui/curation.json')
    old_curated = read(baseline/'review-ui/curation.json')
    for id, before in old_curated.items():
        if id != 'F065':
            assert curated[id] == before
    for id in ('F065', 'E065'):
        assert curated[id]['source_digest'] == server.source_digest(items[id])
        assert all(curated[id].get(k) for k in ('title', 'impact', 'summary', 'target'))
    with urlopen('http://127.0.0.1:4318/api/findings', timeout=10) as response:
        api = json.load(response)
    cards = api['findings']
    assert len(cards) == 229
    assert not any('awaiting an update' in f['summary'] for f in cards)
    con = sqlite3.connect('file:'+str(repo/'review-ui/data/annotations.sqlite3')+'?mode=ro', uri=True)
    annotations = {t: con.execute('SELECT * FROM '+t).fetchall() for t in ('annotations', 'annotation_history')}
    assert annotations == read(baseline/'annotations-before.json')
    con.close()
    state = read(s.ROOT/'RUN_STATE.json')
    assert not {985933, 992996, 999528} & {x['pid'] for x in state['active_audit_jobs']}
    observations = []
    for job in state['active_audit_jobs']:
        process = subprocess.check_output(['ps', '-p', str(job['pid']), '-o', 'pid=,stat=,etime=,args='], text=True).strip()
        assert job['script'] in process, (job, process)
        observations.append(dict(pid=job['pid'], process=process))
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=s.sha(__file__),
                  baseline_head=read(baseline/'baseline.json')['head'], accepted_native_cases=accepted,
                  original_wedges=360, fixed_lr_models=430444, fixed_lr_samples=4288,
                  literal_strong_models=68024064, literal_samples=680, literal_net_mems=453526853015,
                  both_axis_all_models=1298, corrected_symmetric_total=2362048,
                  border127_side11_labeled=48620416, border127_samples=243,
                  unrelated_previous_ledger_items_unchanged=len(old['items'])-len(changed),
                  prior_evidence_preserved=True, annotations_unchanged=True, english_cards=229,
                  ledger_counts=dict(Counter(x['status'] for x in ledger['items'])),
                  review_counts=dict(Counter(x['status'] for x in full['exercises'])),
                  page_counts=dict(Counter(x['status'] for x in full['pages'])), live_observations=observations,
                  gaps=['129: original1991 MultimatchIII manual and discovery attribution',
                        '127:corner/separated counts and abstract-symmetry reduction; global estimates',
                        'Other pending/partial volume content, including130 onward.'])
    (s.OUT/'checkpoint-checked.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS129 checkpoint:61 new native terminals;360 wedges;unchanged prior evidence and notes;129 remains partial for historical source.')


if __name__ == '__main__':
    main()
