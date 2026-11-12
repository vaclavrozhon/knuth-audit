"""New bounded word231 census with an independent Cartesian oracle and validator."""
from pathlib import Path
from datetime import datetime, timezone
from itertools import product
import json
import os
import random
import subprocess
import time
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/words_primes231_238'
VALUE = dict(zip('abcdefghijklmnopqrstuvwxyz', [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]))


def score(flat):
    assert len(flat) == 20
    answer = 0
    lines = [[(i, j) for j in range(5)] for i in range(4)] + [[(i, j) for i in range(4)] for j in range(5)]
    for line in lines:
        total, multiplier = 0, 1
        for cell in line:
            i, j = cell
            total += VALUE[flat[5*i+j]] * {(1,1):3, (2,3):2}.get(cell, 1)
            multiplier *= {(0,0):2, (3,4):3}.get(cell, 1)
        answer += total * multiplier
    return answer


def columns(flat):
    return [''.join(flat[5*i+j] for i in range(4)) for j in range(5)]


def validate_output(path, row_words, col_words):
    models = {}
    with path.open() as f:
        for line in f:
            flat, cost = line.split()
            assert flat not in models
            assert all(flat[i:i+5] in row_words for i in range(0,20,5))
            assert all(w in col_words for w in columns(flat))
            assert score(flat) == int(cost)
            models[flat] = int(cost)
    return models


def main():
    assert not (OUT / 'word-runs.json').exists()
    assert os.nice(0) >= 15
    base = Path(json.loads((OUT / 'started.json').read_text())['baseline'])
    binary = base / 'word231-census'
    command = ['g++','-O3','-std=c++20','-Wall','-Wextra','-Werror',str(ROOT/'word231_census.cpp'),'-o',str(binary)]
    subprocess.run(command, check=True)
    metadata = dict(at_utc=datetime.now(timezone.utc).isoformat(), status='running', nice=os.nice(0),
        runner_sha256=sha(__file__), source_sha256=sha(ROOT/'word231_census.cpp'), binary_sha256=sha(binary),
        compile_command=command, timeout_seconds_per_new_case=20, small_cases=[], cases=[])
    save(OUT/'word-runs.json', metadata)
    rng = random.Random(231)
    small = [(['aaaaa'], ['aaaa']), (['aaaaa','bbbbb'], ['aaaa','bbbb']), (['ababa','babab'], ['abab','baba'])]
    allrows = [''.join(q) for q in product('ab', repeat=5)]
    allcols = [''.join(q) for q in product('ab', repeat=4)]
    small += [(rng.sample(allrows, rng.randint(1,6)), rng.sample(allcols, rng.randint(1,8))) for _ in range(24)]
    for i, (rr, cc) in enumerate(small):
        rowfile, colfile = base/'small-rows.txt', base/'small-cols.txt'
        rowfile.write_text('\n'.join(rr)+'\n'); colfile.write_text('\n'.join(cc)+'\n')
        output, log = base/'small.out', base/'small.json'
        with output.open('w') as a, log.open('w') as b:
            subprocess.run([str(binary),str(rowfile),str(colfile),'100'],stdout=a,stderr=b,check=True,timeout=3)
        oracle = {''.join(q):score(''.join(q)) for q in product(rr,repeat=4) if all(w in cc for w in columns(''.join(q)))}
        got = validate_output(output, set(rr), set(cc)); terminal=json.loads(log.read_text())
        assert got == oracle and terminal['count'] == terminal['validated'] == len(got)
        assert terminal['best'] == max(got.values(), default=-1)
        metadata['small_cases'].append(dict(rows=rr, columns=cc, complete_cartesian_trials=len(rr)**4, solutions=len(got)))
    print('PASS27 small complete Cartesian comparisons.', flush=True)
    rowsource = ROOT/'sources/wordlists/words5-from-sgb'
    colsource = ROOT/'sources/wordlists/words4-from-OSPD4'
    rr, cc = rowsource.read_text().splitlines(), colsource.read_text().splitlines()
    metadata['dictionary_hashes'] = {str(p.relative_to(ROOT)):sha(p) for p in [rowsource,colsource]}
    save(OUT/'word-runs.json', metadata)
    for n in [1000,2000,3000]:
        output, log = OUT/f'word-{n}.out', OUT/f'word-{n}.json'
        command=[str(binary),str(rowsource),str(colsource),str(n)]
        case=dict(n=n, command=command, started_at_utc=datetime.now(timezone.utc).isoformat(), status='running')
        metadata['cases'].append(case); save(OUT/'word-runs.json',metadata)
        start=time.monotonic()
        with output.open('w') as a, log.open('w') as b:
            try:
                run=subprocess.run(command,stdout=a,stderr=b,timeout=20)
                code=run.returncode
            except subprocess.TimeoutExpired:
                code=124
        case.update(returncode=code, wall_seconds=time.monotonic()-start, output_sha256=sha(output), terminal_sha256=sha(log))
        if code==0:
            got=validate_output(output,set(rr[:n]),set(cc[:n])); terminal=json.loads(log.read_text())
            assert terminal['count']==terminal['validated']==len(got)
            assert terminal['best']==max(got.values(),default=-1)
            assert set(terminal['best_models'])=={q for q,cost in got.items() if cost==terminal['best']}
            case.update(status='complete_and_independently_validated', **terminal)
            print(n,'count',terminal['count'],'best',terminal['best'],'seconds',round(case['wall_seconds'],3),flush=True)
        else:
            case.update(status='timeout_not_complete' if code==124 else 'failed', global_count_verified=False)
            print(n,case['status'],round(case['wall_seconds'],3),flush=True)
        save(OUT/'word-runs.json',metadata)
    metadata.update(status='finished', finished_at_utc=datetime.now(timezone.utc).isoformat(), old_searches_repeated=0)
    save(OUT/'word-runs.json',metadata)


if __name__ == '__main__':
    main()
