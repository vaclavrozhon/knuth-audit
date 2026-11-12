#!/usr/bin/env python3
"""Check the compressed-trie adaptation and measure the missing mem bounds.

Small dictionaries use complete Cartesian products as an independent oracle.
Large counts are compared with the earlier row-based enumerator; the new C++
program additionally validates every model against the original word strings.
"""
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import hashlib
import json
import os
import random
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/word_rectangles'
DATA = ROOT / 'sources/wordlists'


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, data):
    temporary = path.with_suffix(path.suffix + '.partial')
    temporary.write_text(json.dumps(data, indent=2) + '\n')
    temporary.replace(path)


def check_accounting(result):
    n = result['n']
    levels = [(i, j) for i in range(n) for j in range(i, n)]
    profile = result['profile']
    assert len(profile) == len(levels) + 1
    assert profile[0] == 1 and profile[-1] == result['count']
    accesses = result['accesses']
    assert accesses['stack_reads'] == accesses['stack_writes'] == sum(profile[1:])
    assert accesses['prefix_reads'] == sum(
        profile[k] * (1 if i == j else 2) for k, (i, j) in enumerate(levels))
    assert accesses['prefix_writes'] == n + sum(
        profile[k+1] * (1 if i == j else 2) for k, (i, j) in enumerate(levels))
    assert sum(accesses.values()) == result['search_mems']
    assert result['count'] == result['validated_models']
    assert result['total_upper_bound'] == (
        result['search_mems'] + result['initialization_upper_bound'])


def main():
    temporary = Path(tempfile.mkdtemp(prefix='knuth-vol4b-symcost-'))
    source = ROOT / 'symmetric_word_costs.cpp'
    binary = temporary / 'symmetric-word-costs'
    compile_command = ['g++', '-O3', '-std=c++17', '-Wall', '-Wextra', '-Werror',
                       str(source), '-o', str(binary)]
    metadata = dict(pid=os.getpid(), status='running', started_at_utc=now(),
                    command=[sys.executable] + sys.argv,
                    compile_command=compile_command, source_sha256=sha(source),
                    temporary_directory=str(temporary), timeout_seconds_per_case=1800,
                    small_checks=[], cases=[])
    destination = OUT / 'symmetric-costs-run.json'
    save(destination, metadata)
    try:
        subprocess.run(compile_command, check=True)
        metadata['binary_sha256'] = sha(binary)
        rng = random.Random(7223032)
        samples = [['a', 'b'], ['aa', 'ab', 'ba', 'bb'],
                   [''.join(w) for w in product('ab', repeat=4)]]
        for _ in range(120):
            n = rng.randint(1, 4)
            all_words = [''.join(w) for w in product('abc', repeat=n)]
            samples.append(rng.sample(all_words, rng.randint(1, min(8, len(all_words)))))
        for case, words in enumerate(samples):
            n = len(words[0])
            path = temporary / f'small-{case}.txt'
            path.write_text('\n'.join(words) + '\n')
            expected = {rows for rows in product(words, repeat=n)
                        if all(rows[i][j] == rows[j][i]
                               for i in range(n) for j in range(i))}
            result = json.loads(subprocess.check_output([str(binary), str(path), '--emit']))
            actual = [tuple(rows) for rows in result['solutions']]
            assert set(actual) == expected and len(actual) == len(expected), case
            check_accounting(result)
            metadata['small_checks'].append(dict(n=n, vocabulary=len(words),
                                                count=result['count'], words=words))
        metadata['small_checks_passed'] = len(samples)
        save(destination, metadata)
        print(f'{len(samples)} Cartesian-product comparisons and accounting checks passed.', flush=True)
        prior = {Path(x['file']).name: x for x in
                 map(json.loads, (OUT / 'squares.jsonl').read_text().splitlines())}
        files = [DATA / 'words5-from-sgb'] + [DATA / f'words{n}-from-OSPD4' for n in range(2, 13)]
        verified = []
        for path in files:
            command = [str(binary), str(path)]
            case = dict(dictionary=str(path.relative_to(ROOT)), dictionary_sha256=sha(path),
                        started_at_utc=now(), command=command, status='running')
            metadata['cases'].append(case)
            save(destination, metadata)
            start = time.monotonic()
            with (OUT / f'symmetric-cost-{path.name}.json').open('w') as output:
                with (OUT / f'symmetric-cost-{path.name}.log').open('w') as log:
                    process = subprocess.Popen(command, stdout=output, stderr=log)
                    case['pid'] = process.pid
                    save(destination, metadata)
                    try:
                        case['returncode'] = process.wait(timeout=1800)
                    except subprocess.TimeoutExpired:
                        process.terminate()
                        try:
                            process.wait(timeout=10)
                        except subprocess.TimeoutExpired:
                            process.kill(); process.wait()
                        case['returncode'] = 124
            case.update(finished_at_utc=now(), elapsed_seconds=time.monotonic()-start)
            assert case['returncode'] == 0, case
            result = json.loads((OUT / f'symmetric-cost-{path.name}.json').read_text())
            check_accounting(result)
            assert result['count'] == prior[path.name]['count'], path.name
            result['dictionary'] = case['dictionary']
            result['dictionary_sha256'] = case['dictionary_sha256']
            result['matches_previous_row_enumeration'] = True
            result['book_mem_claim'] = 'about 120 million' if path.name.endswith('sgb') else 'under 6 billion'
            if not path.name.endswith('sgb'):
                result['under_six_billion'] = result['total_upper_bound'] < 6000000000
            case['status'] = 'verified'
            verified.append(result)
            save(destination, metadata)
            save(OUT / 'symmetric-costs-verified.json', dict(complete=False, cases=verified))
            print(path.name, result['count'], 'models;', result['search_mems'],
                  'search mems;', result['total_upper_bound'], 'including initialization bound', flush=True)
        save(OUT / 'symmetric-costs-verified.json', dict(
            complete=True, source_sha256=sha(source), small_oracle_checks=len(samples),
            model='one 64-bit word per compressed-trie pair or packed continuation pair',
            scope='independent adaptation of the book algorithm; not recovered author timing code',
            cases=verified))
        metadata.update(status='verified', finished_at_utc=now())
        save(destination, metadata)
    except Exception as error:
        metadata.update(status='incomplete', error=repr(error), finished_at_utc=now())
        save(destination, metadata)
        raise


if __name__ == '__main__':
    main()
