"""Validate all source figures; solve only 28 previously unchecked clue sets.

SAT uses the accepted direct 81-variable encoding. DLX3 uses the residual
quotas of answer 173(a). Each new solver call has a 15-second wall limit.
This checks particular puzzles, never a census of all smaller clue sets.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import re
import subprocess
import sys
import time
from check_chess_sudoku import adjacent, verify, sat
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/chess173_174'
NEW = OUT / 'new-cases'


def key(q):
    return q['piece'], tuple(map(tuple, q['clues']))


def cells(q):
    return sorted(9*r+c for r, c in q['cells'])


def valid(model, q):
    try:
        verify(set(model), q['clues'], q['piece'])
        return True
    except AssertionError:
        return False


def prepare():
    f = json.loads((OUT / 'figures.json').read_text())['figures']
    old = json.loads((ROOT / 'results/chess_sudoku/verified.json').read_text())
    catalog = {key(q): dict(q, old_evidence='results/chess_sudoku/verified.json', sources=[])
               for q in old['cases']}
    for a, b in [('original-486', 'draft-176'), ('original-691', 'draft-259')]:
        assert [{k: v for k, v in q.items() if k != 'source_bounds'} for q in f[a]] == [
            {k: v for k, v in q.items() if k != 'source_bounds'} for q in f[b]]
    assert f['original-166'][1]['clues'] == f['fascicle-errata-7'][0]['clues']
    for i in range(8):
        if i != 1:
            assert key(f['original-166'][i]) == key(f['draft-88'][i])
    for i, q in enumerate([f['original-166'][0], f['original-166'][2]]):
        assert q['clues'] == old['complete_diagrams'][i]
        assert valid(cells(q), q)
    for name in ['original-166', 'original-486', 'errata-14', 'draft-88']:
        for i, q in enumerate(f[name]):
            if name == 'original-166' and i in (0, 2):
                continue
            if name == 'draft-88' and i != 1:
                continue
            k = key(q)
            if k not in catalog:
                catalog[k] = dict(name=f'new-{len(catalog)-10:02}', piece=q['piece'],
                                  clues=q['clues'], sources=[])
            catalog[k]['sources'].append(dict(trace=name, board=i))
    assert len(catalog) == 39 and sum('old_evidence' not in q for q in catalog.values()) == 28
    mappings = {}
    for version, gallery, appendix in [('original', 'original-486', 'original-691'),
                                      ('corrected', 'errata-14', 'errata-23')]:
        puzzles = f['original-166'][4:] + f[gallery][:16]
        solutions = f[appendix][:20]
        for q in solutions:
            assert valid(cells(q), q)
        used = []
        mappings[version] = []
        for i, q in enumerate(puzzles):
            matches = [j for j, a in enumerate(solutions) if q['piece'] == a['piece'] and valid(cells(a), q)]
            assert len(matches) == 1, (version, i, matches)
            j = matches[0]; used.append(j)
            cat = catalog[key(q)]
            model = cells(solutions[j])
            if 'old_evidence' in cat:
                assert cat['models'] == [model]
            if 'appendix_model' in cat:
                assert cat['appendix_model'] == model
            cat['appendix_model'] = model
            mappings[version].append(dict(case=cat['name'], appendix_board=j))
        assert sorted(used) == list(range(20))
    for i, q in enumerate(f['original-486'][16:]):
        a = f['original-691'][20+i]
        assert a['piece'] == q['piece'] and valid(cells(a), q)
        assert catalog[key(q)]['models'] == [cells(a)]
    save(OUT / 'prepared.json', dict(at_utc=datetime.now(timezone.utc).isoformat(),
         checker_sha256=sha(__file__), figures_sha256=sha(OUT/'figures.json'),
         old_verified_sha256=sha(ROOT/'results/chess_sudoku/verified.json'),
         old_checker_sha256=sha(ROOT/'check_chess_sudoku.py'), appendix_mapping=mappings,
         all_44_original_and_corrected_appendix_boards_valid=True,
         all_24_draft_appendix_boards_equal_original=True,
         cases=list(catalog.values())))


def mcc_input(q):
    fixed = {9*r+c for r, c, _ in q['clues']}
    scopes = {}
    for r in range(9):
        scopes[f'r{r}'] = ({9*r+c for c in range(9)}, 3)
    for c in range(9):
        scopes[f'c{c}'] = ({9*r+c for r in range(9)}, 3)
    for b in range(9):
        scopes[f'b{b}'] = ({9*r+c for r in range(9) for c in range(9)
                           if 3*(r//3)+c//3 == b}, 3)
    for i, (r, c, label) in enumerate(q['clues']):
        scopes[f'p{i}'] = ({v for v in range(81) if adjacent(9*r+c, v, q['piece'])}, label)
    quota = {k: n-len(s & fixed) for k, (s, n) in scopes.items()}
    assert min(quota.values()) >= 0
    forbidden = fixed | set().union(*(s for k, (s, _) in scopes.items() if quota[k] == 0))
    options = [[k for k, (s, _) in scopes.items() if v in s] for v in range(81) if v not in forbidden]
    assert all(quota[k] > 0 for option in options for k in option)
    return ' '.join(f'{n}|{k}' for k, n in quota.items() if n) + '\n' + '\n'.join(
        ' '.join(option) for option in options) + '\n'


def one(q, method):
    base = NEW / q['name']
    record = base.with_suffix('.'+method+'.json')
    assert not record.exists(), record
    start = time.monotonic()
    cmd = [sys.executable, str(Path(__file__).resolve()), '--sat-worker', q['name']]
    stdin = None
    if method == 'mcc':
        stdin = mcc_input(q)
        base.with_suffix('.mcc').write_text(stdin)
        cmd = ['/tmp/knuth-dlx3', 'v1', 'd0', 'm1', 't2']
    try:
        p = subprocess.run(cmd, input=stdin, text=True, capture_output=True, timeout=15)
    except subprocess.TimeoutExpired as error:
        save(record, dict(status='timeout', wall_seconds=time.monotonic()-start,
             limit_seconds=15, command=cmd, stdout=str(error.stdout), stderr=str(error.stderr)))
        return
    base.with_suffix('.'+method+'.out').write_text(p.stdout)
    base.with_suffix('.'+method+'.log').write_text(p.stderr)
    assert p.returncode == 0, (q['name'], method, p.stderr)
    if method == 'sat':
        models = json.loads(p.stdout)
    else:
        count = int(re.search(r'Altogether (\d+) solution', p.stderr)[1])
        models, model = [], None
        for line in p.stdout.splitlines()+['END']:
            if re.fullmatch(r'\d+:', line) or line == 'END':
                if model is not None:
                    models.append(sorted(model))
                model = {9*r+c for r, c, _ in q['clues']}
            elif line.strip():
                parts = line.split(' (')[0].split()
                r = int(next(t[1:] for t in parts if t.startswith('r')))
                c = int(next(t[1:] for t in parts if t.startswith('c')))
                assert 9*r+c not in model
                model.add(9*r+c)
        assert len(models) == count
    assert all(valid(m, q) for m in models)
    save(record, dict(status='complete', models=models, unique=len(models) == 1,
         search_stopped_after_second_model=len(models) == 2, wall_seconds=time.monotonic()-start,
         limit_seconds=15, command=cmd))


def run():
    prepared = json.loads((OUT / 'prepared.json').read_text())
    assert prepared['checker_sha256'] == sha(__file__)
    NEW.mkdir(exist_ok=True)
    for q in prepared['cases']:
        if 'old_evidence' in q:
            continue
        for method in ['sat', 'mcc']:
            path = NEW / (q['name']+'.'+method+'.json')
            if not path.exists():
                one(q, method)
            r = json.loads(path.read_text())
            print(q['name'], method, r['status'], len(r.get('models', [])), round(r['wall_seconds'], 4), flush=True)
    records = []
    for q in prepared['cases']:
        if 'old_evidence' in q:
            continue
        methods = {m: json.loads((NEW/(q['name']+'.'+m+'.json')).read_text()) for m in ['sat', 'mcc']}
        if all(r['status'] == 'complete' for r in methods.values()):
            a, b = [r['models'] for r in methods.values()]
            assert len(a) == len(b)
            if len(a) <= 1:
                assert a == b
            if 'appendix_model' in q:
                assert a == [q['appendix_model']]
        records.append(dict(case=q['name'], methods=methods))
    save(OUT / 'checked.json', dict(at_utc=datetime.now(timezone.utc).isoformat(),
         checker_sha256=sha(__file__), prepared_sha256=sha(OUT/'prepared.json'),
         native_binary_sha256=sha('/tmp/knuth-dlx3'), reused_cases=11, new_cases=28,
         lower_bound_searches=0, records=records))


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--sat-worker':
        q = next(q for q in json.loads((OUT/'prepared.json').read_text())['cases'] if q['name'] == sys.argv[2])
        print(json.dumps(sat(q['clues'], q['piece'])))
    elif sys.argv[1:] == ['prepare']:
        prepare()
    elif sys.argv[1:] == ['run']:
        run()
    else:
        raise SystemExit('use prepare or run')
