"""Exact DNF fitting, with independent small-case validation and DRAT checking.

Requires python-sat; use the isolated environment recorded in the result JSON.
The CNF describes at most M noncontradictory terms, each covering a positive.
This is without loss when the positive set is nonempty: duplicate a useful term
in place of any contradictory, unused or missing term. Adjacent terms are
ordered by their positive-set truth vectors to remove permutation symmetry.
"""
from itertools import product
from pathlib import Path
import argparse, hashlib, json, random, subprocess, threading, time
import pysat
from pysat.solvers import Solver

ROOT = Path(__file__).parent


def encode(positives, negatives, count):
    assert positives and count > 0
    n = len(positives[0]); size = len(positives)
    clauses = []; top = 0
    def variables(length):
        nonlocal top
        out = list(range(top + 1, top + length + 1)); top += length
        return out
    p = [variables(n) for _ in range(count)]
    q = [variables(n) for _ in range(count)]
    z = [variables(size) for _ in range(count)]
    for i in range(count):
        clauses.extend([[-p[i][j], -q[i][j]] for j in range(n)])
        clauses.append(z[i][:])
        for k, point in enumerate(positives):
            wrong = [q[i][j] if bit else p[i][j] for j, bit in enumerate(point)]
            clauses.extend([[-z[i][k], -literal] for literal in wrong])
            clauses.append([z[i][k]] + wrong)
        for point in negatives:
            clauses.append([q[i][j] if bit else p[i][j] for j, bit in enumerate(point)])
    for k in range(size):
        clauses.append([z[i][k] for i in range(count)])
    for i in range(count - 1):
        prefix = variables(1)[0]; clauses.append([prefix])
        for k in range(size):
            a, b = z[i][k], z[i+1][k]
            clauses.append([-prefix, a, -b])
            if k + 1 < size:
                nxt = variables(1)[0]
                clauses.extend([[-nxt, prefix], [-nxt, -a, b], [-nxt, a, -b],
                                [-prefix, -a, -b, nxt], [-prefix, a, b, nxt]])
                prefix = nxt
    return top, clauses, p, q


def decode(model, p, q, positives, negatives):
    true = set(x for x in model if x > 0)
    terms = [[sign * (j+1) for sign, table in [(1, p), (-1, q)]
              for j, var in enumerate(table[i]) if var in true] for i in range(len(p))]
    def value(point):
        return any(all(point[abs(lit)-1] == int(lit > 0) for lit in term) for term in terms)
    assert all(value(x) for x in positives)
    assert not any(value(x) for x in negatives)
    assert all(not (set(term) & {-v for v in term}) for term in terms)
    return terms


def cube_minimum(positives, negatives):
    """Independent enumeration of all 3**n conjunctions followed by cover DP."""
    n = len(positives[0]); masks = set()
    def matches(cube, point):
        return all(c == -1 or c == x for c, x in zip(cube, point))
    for cube in product((-1, 0, 1), repeat=n):
        if any(matches(cube, x) for x in negatives):
            continue
        mask = sum(1 << i for i, x in enumerate(positives) if matches(cube, x))
        if mask:
            masks.add(mask)
    full = (1 << len(positives)) - 1
    distances = [len(positives)+1] * (full+1); distances[0] = 0
    for mask in range(full+1):
        for cube in masks:
            nxt = mask | cube
            distances[nxt] = min(distances[nxt], distances[mask]+1)
    return distances[full]


def validate():
    cases = []
    for truth in range(1, 16):
        points = list(product((0, 1), repeat=2))
        cases.append(([p for i,p in enumerate(points) if truth >> i & 1],
                      [p for i,p in enumerate(points) if not truth >> i & 1]))
    rng = random.Random(558)
    for _ in range(500):
        groups = [[], [], []]
        for point in product((0, 1), repeat=3):
            groups[rng.randrange(3)].append(point)
        if groups[0]:
            cases.append((groups[0], groups[1]))
    checked = 0
    for positives, negatives in cases:
        minimum = cube_minimum(positives, negatives)
        for count in range(1, len(positives)+1):
            _, clauses, p, q = encode(positives, negatives, count)
            with Solver(name='g4', bootstrap_with=clauses) as solver:
                result = solver.solve()
                assert result == (count >= minimum), (positives, negatives, count, minimum)
                if result:
                    decode(solver.get_model(), p, q, positives, negatives)
            checked += 1
    return {'training_sets': len(cases), 'solver_comparisons': checked,
            'oracle': 'all ternary cubes and exact set-cover dynamic programming'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_case(count, rows, limit, checker, directory, positives, negatives):
    positives = positives[:rows]; negatives = negatives[:rows]
    top, clauses, p, q = encode(positives, negatives, count)
    base = directory / f'm{count}-r{rows}'
    cnf = base.with_suffix('.cnf')
    cnf.write_text(f'p cnf {top} {len(clauses)}\n' +
                   ''.join(' '.join(map(str, clause)) + ' 0\n' for clause in clauses))
    start = time.monotonic()
    out = {'terms': count, 'rows': rows, 'variables': top, 'clauses': len(clauses),
           'cnf_sha256': sha(cnf), 'solver_limit_seconds': limit}
    print(f'Start m={count}, rows={rows}: {top} variables, {len(clauses)} clauses', flush=True)
    with Solver(name='g4', bootstrap_with=clauses, with_proof=True) as solver:
        timer = threading.Timer(limit, solver.interrupt); timer.start()
        try:
            result = solver.solve_limited(expect_interrupt=True)
        finally:
            timer.cancel()
        out['solver_seconds'] = time.monotonic() - start
        out['solver_statistics'] = solver.accum_stats()
        out['status'] = 'SAT' if result is True else 'UNSAT' if result is False else 'TIMEOUT'
        if result is True:
            out['witness'] = decode(solver.get_model(), p, q, positives, negatives)
            out['witness_independently_evaluated'] = True
        elif result is False:
            proof = base.with_suffix('.drat')
            proof.write_text('\n'.join(solver.get_proof()) + '\n')
            out['proof_sha256'] = sha(proof); out['proof_bytes'] = proof.stat().st_size
            checked = subprocess.run([checker, str(cnf), str(proof), '-t', '1200'],
                                     text=True, capture_output=True, timeout=1230)
            base.with_suffix('.verification.txt').write_text(checked.stdout + checked.stderr)
            out['proof_verified'] = checked.returncode == 0 and 's VERIFIED' in checked.stdout
            assert out['proof_verified'], checked.stdout + checked.stderr
    base.with_suffix('.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out), flush=True)
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--checker', default='/tmp/knuth-drat-trim/drat-trim')
    parser.add_argument('--limit', type=float, default=1800)
    parser.add_argument('--validate-only', action='store_true')
    parser.add_argument('--cases', default='3:16,3:17,4:20,4:21,5:28,5:29')
    args = parser.parse_args()
    validation = validate(); print(json.dumps(validation), flush=True)
    directory = ROOT / 'results/learning_dnf'; directory.mkdir(exist_ok=True)
    (directory / 'validation.json').write_text(json.dumps(validation, indent=2) + '\n')
    if args.validate_only:
        return
    data = json.loads((ROOT / 'results/learning_table_data.json').read_text())
    positives = [tuple(map(int, s)) for s in data['positive_words_pi']]
    negatives = [tuple(map(int, s)) for s in data['negative_words_e']]
    results = {'python_sat_version': pysat.__version__, 'solver': 'Glucose4',
               'checker': 'DRAT-trim',
               'checker_source': 'https://github.com/marijnheule/drat-trim',
               'checker_commit': '2e3b2dc0ecf938addbd779d42877b6ed69d9a985',
               'validation': validation, 'cases': []}
    for case in args.cases.split(','):
        count, rows = map(int, case.split(':'))
        results['cases'].append(run_case(count, rows, args.limit, args.checker,
                                        directory, positives, negatives))
        (directory / 'summary.json').write_text(json.dumps(results, indent=2) + '\n')


if __name__ == '__main__':
    main()
