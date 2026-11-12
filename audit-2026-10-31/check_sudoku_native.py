#!/usr/bin/env python3
"""Original DLX1 on all three Sudoku examples; complete independent model comparison."""
from datetime import datetime, timezone
import json
from check_sudoku_basics import OUT, DIGITS, UNITS
from dlx1_audit_tools import sha, run, input_text, decode_rows


def instance(board, naked_only=False):
    all_names = [f'{kind}{i}{k}' for kind in 'prcb' for i in range(9)
                 for k in (range(9) if kind == 'p' else range(1, 10))]
    def option(v, k):
        i, j = divmod(v, 9)
        return [f'p{i}{j}', f'r{i}{k}', f'c{j}{k}', f'b{3*(i//3)+j//3}{k}']
    used = {name for v, k in enumerate(board) if k for name in option(v, k)}
    names = [s for s in all_names if s not in used]
    indices = {name: i+1 for i, name in enumerate(names)}
    rows, moves = [], []
    for v in range(81):
        for k in range(1, 10):
            o = option(v, k)
            if not used.intersection(o):
                rows.append([indices[name] for name in o]); moves.append((v, k))
    primary = sum(name.startswith('p') for name in names) if naked_only else len(names)
    return names, rows, moves, primary


def check_case(label, board, expected, naked_only=False):
    names, rows, moves, primary = instance(board, naked_only)
    data = input_text(names, rows, primary)
    stats, text = run(OUT/'native', label, data, models=True)
    (OUT/'native'/f'{label}.models').write_text(text)
    solutions = set()
    for selected in decode_rows(text, names, rows):
        completed = list(board)
        for r in selected:
            v, k = moves[r]; assert not completed[v]; completed[v] = k
        assert all({completed[v] for v in unit} == DIGITS for unit in UNITS)
        solutions.add(tuple(completed))
    assert solutions == {tuple(s) for s in expected}, label
    stats.update(items=len(names), primary_items=primary, options=len(rows),
                 model_sha256=sha(OUT/'native'/f'{label}.models'),
                 coordinate_solutions_compared=len(solutions))
    return stats


def main():
    sources = json.loads((OUT/'pdf-grids.json').read_text())['sources']
    basics = json.loads((OUT/'basics.json').read_text())
    cases = [check_case(f'29{x}', sources[f'29{x}']['board'], basics['solutions'][x]) for x in 'abc']
    cases.append(check_case('29b-naked-only', sources['29b']['board'], basics['solutions']['b'], True))
    # The displayed option sequence and elementary active lists on pp75/77.
    names, rows, moves, primary = instance(sources['29a']['board'])
    assert len(names) == primary == 196 and len(rows) == 146
    assert [names[i-1] for i in rows[0]] == 'p00 r07 c07 b07'.split()
    assert [names[i-1] for i in rows[-1]] == 'p88 r86 c86 b86'.split()
    assert [v%9 for v,k in moves if v//9 == 0 and k == 2] == [5,6,7]
    assert [v//9 for v,k in moves if v%9 == 0 and k == 1] == [4,5,6,7]
    lines = (OUT/'native/29b.models').read_text().splitlines()[1:]
    printed_lines = {0:'c33 b13 p23 r23 (1 of 1)',1:'r13 c13 b03 p11 (1 of 1)',
                     15:'c42 b72 p84 r82 (1 of 1)',16:'p16 r18 c68 b28 (2 of 2)',
                     17:'b27 p18 r17 c87 (1 of 1)',-1:'p85 r81 c51 b71 (1 of 1)'}
    assert all(lines[i].strip() == s for i,s in printed_lines.items())
    # 50: Every one of the 36 possible distinguishing clues actually gives one solution.
    extensions = []
    for v, k in basics['exercise50']['distinguishing_clues']:
        board = list(sources['29c']['board']); assert not board[v]; board[v] = k
        expected = [s for s in basics['solutions']['c'] if s[v] == k]
        assert len(expected) == 1
        extensions.append(check_case(f'50-{v//9}{v%9}-{k}', board, expected))
    claimed_nodes = {'29b': 89, '29c': 129, '29b-naked-only': 41877}
    discrepancies = [dict(label=c['label'], claimed=claimed_nodes[c['label']], actual=c['nodes'])
                     for c in cases if c['label'] in claimed_nodes and c['nodes'] != claimed_nodes[c['label']]]
    assert not discrepancies
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), helper_sha256=sha(__file__.replace('check_sudoku_native.py','dlx1_audit_tools.py')),
                  grids_sha256=sha(OUT/'pdf-grids.json'), basics_sha256=sha(OUT/'basics.json'),
                  cases=cases, extensions50=extensions, node_discrepancies=discrepancies,
                  displayed_path_lines_compared=printed_lines,
                  scope='Complete DLX1 model sets equal independent coordinate models. '
                        'Every distinguishing single-clue extension uniquely solvable. '
                        'Historical implementation costs must be assessed separately.')
    (OUT/'native.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(cases=cases, extensions_checked=len(extensions), node_discrepancies=discrepancies),indent=2))


if __name__ == '__main__':
    main()
