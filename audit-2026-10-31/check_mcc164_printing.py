"""Check retrospective solution printing against observed branch ordinals.

Ten tiny, new diagnostic instances; at most five options. The accepted graph
and F071 enumerations are not repeated. All solution sets also have a direct
subset oracle, independent of dancing links.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import os
import re
import subprocess
import tempfile
import time
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/mcc163_170/printing'


def expected(primary, options):
    solutions = set()
    for mask in range(1 << len(options)):
        multiplicities = Counter()
        secondary = {}
        valid = True
        for j, option in enumerate(options):
            if not mask >> j & 1:
                continue
            for token in option:
                item, _, color = token.partition(':')
                if item in primary:
                    multiplicities[item] += 1
                elif item in secondary:
                    if not color or color != secondary[item]:
                        valid = False
                else:
                    secondary[item] = color
        if valid and all(lo <= multiplicities[item] <= hi for item, (lo, hi) in primary.items()):
            solutions.add(mask)
    return solutions


def inspect(log, options):
    lines = log.splitlines()
    stack, totals, seen, solutions = [], {}, Counter(), []
    move_count = printed_steps = null_moves = 0
    option_ids = {frozenset(row): j for j, row in enumerate(options)}
    assert len(option_ids) == len(options)
    i = 0
    while i < len(lines):
        line = lines[i]
        match = re.fullmatch(r'L(\d+):(.*) \((\d+) of (\d+)\)', line)
        if match:
            level, payload, ordinal, degree = match.groups()
            level, ordinal, degree = int(level), int(ordinal), int(degree)
            stack = stack[:level]
            assert len(stack) == level
            prefix = tuple(stack)
            seen[prefix] += 1
            # This ordinal is counted from actual sibling visits, not read
            # from the saved DLINK chain used by the native printer.
            assert ordinal == seen[prefix], (prefix, line)
            assert degree == totals.setdefault(prefix, degree)
            stack.append(payload+f' ({ordinal} of {degree})')
            move_count += 1
            null_moves += payload.strip().startswith('null ')
        elif re.fullmatch(r'\d+:', line):
            assert int(line[:-1]) == len(solutions)+1
            retrospective = lines[i+1:i+1+len(stack)]
            assert retrospective == stack, (stack, retrospective)
            mask = 0
            for step in retrospective:
                payload = re.sub(r' \(\d+ of \d+\)$', '', step).strip()
                if payload.startswith('null '):
                    continue
                bit = 1 << option_ids[frozenset(payload.split())]
                assert not mask & bit
                mask |= bit
            solutions.append(mask)
            printed_steps += len(stack)
            i += len(stack)
        i += 1
    assert len(set(solutions)) == len(solutions)
    assert dict(seen) == totals, (seen, totals)
    match = re.search(r'Altogether (\d+) solution', log)
    assert match and int(match[1]) == len(solutions)
    assert 'TIMEOUT' not in log and 'Illegal option' not in log and '(?)' not in log
    return dict(solutions=sorted(solutions), branches=move_count, printed_solution_steps=printed_steps,
                null_branches=null_moves, parent_nodes=len(seen))


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
    OUT.mkdir(exist_ok=True)
    assert not (OUT / 'accepted.json').exists(), 'Accepted already: do not repeat.'
    build = Path(tempfile.mkdtemp(prefix='knuth-vol4b-mcc164-build-'))
    files = ['sources/knuth-programs/dlx3.w', 'sources/knuth-programs/gb_flip.w',
             'sources/knuth-programs/gb_flip.ch', 'sources/knuth-programs/boilerplate.w', 'puzzle_xcc.py']
    (build / 'boilerplate.w').write_bytes((ROOT / files[3]).read_bytes())
    commands = [
        ['ctangle', str(ROOT / files[1]), str(ROOT / files[2]), str(build / 'gb_flip.c')],
        ['ctangle', str(ROOT / files[0]), '-', str(build / 'dlx3.c')],
        ['gcc', '-O2', '-std=gnu99', '-I', str(build), str(build / 'dlx3.c'), str(build / 'gb_flip.c'), '-o', str(build / 'dlx3')]]
    record = dict(at_utc=datetime.now(timezone.utc).isoformat(), checker_sha256=sha(__file__),
        source_hashes={p: sha(ROOT / p) for p in files}, build_directory=str(build), compile_commands=commands,
        nice=os.getpriority(os.PRIO_PROCESS, 0), per_case_timeout_seconds=10)
    save(OUT / 'started.json', record)
    for i, command in enumerate(commands):
        result = subprocess.run(command, cwd=build, capture_output=True, text=True, timeout=30)
        (OUT / f'compile-{i}.log').write_text(result.stdout+result.stderr)
        assert result.returncode == 0, result.stderr
    cases = [
        ('empty01', {'A': (0, 1)}, []),
        ('empty02', {'A': (0, 2)}, []),
        ('one11', {'A': (1, 1)}, [['A', 'x']]),
        ('one12', {'A': (1, 2)}, [['A', 'x']]),
        ('optional01', {'A': (0, 1)}, [['A', x] for x in 'xyz']),
        ('optional03', {'A': (0, 3)}, [['A', x] for x in 'xyz']),
        ('exact24', {'A': (2, 2)}, [['A', x] for x in 'xyzw']),
        ('colored', {'A': (0, 2), 'B': (1, 2)}, [
            ['A', 'B', 'x', 'c:0'], ['A', 'y', 'c:1'], ['B', 'z', 'c:0'],
            ['A', 'w', 'c:0'], ['B', 't', 'c:1']]),
        ('coupled', {'A': (1, 3), 'B': (1, 2)}, [
            ['A', 'x'], ['A', 'y'], ['A', 'B', 'z'], ['B', 'w'], ['B', 't']]),
        ('conflict', {'A': (2, 2), 'B': (1, 1)}, [
            ['A', 'x'], ['A', 'y'], ['A', 'z'], ['B', 'x'], ['B', 'w']])]
    results = []
    for name, primary, options in cases:
        secondary = sorted({token.partition(':')[0] for row in options for token in row}-set(primary))
        header = [f'{lo}:{hi}|{item}' for item, (lo, hi) in primary.items()]
        if secondary:
            header += ['|']+secondary
        problem = ' '.join(header)+'\n'+''.join(' '.join(row)+'\n' for row in options)
        (OUT / (name+'.mcc')).write_text(problem)
        command = [str(build / 'dlx3'), 'v7', 'm1', 'd0']
        start = time.monotonic()
        result = subprocess.run(command, input=problem, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT, timeout=10)
        elapsed = time.monotonic()-start
        (OUT / (name+'.log')).write_text(result.stdout)
        assert result.returncode == 0
        checked = inspect(result.stdout, options)
        oracle = sorted(expected(primary, options))
        assert checked['solutions'] == oracle, (name, checked['solutions'], oracle)
        results.append(dict(name=name, command=command, seconds=elapsed, options=len(options),
            exhaustive_subsets=1 << len(options), expected_solutions=oracle, **checked))
        save(OUT / 'cases.json', results)
    record.update(completed_at_utc=datetime.now(timezone.utc).isoformat(), binary_sha256=sha(build / 'dlx3'),
        cases=results, all_retrospective_paths_match=True, all_independent_ordinals_match=True,
        all_solution_sets_match_subset_oracle=True, no_previous_enumerations_repeated=True)
    save(OUT / 'accepted.json', record)
    print('PASS164:', len(results), 'tiny instances;', sum(x['printed_solution_steps'] for x in results),
          'printed solution steps;', sum(x['null_branches'] for x in results), 'null branches.')


if __name__ == '__main__':
    main()
