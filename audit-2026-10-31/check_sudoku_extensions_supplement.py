#!/usr/bin/env python3
"""Check original Brouwer examples, printed cross-references, and census input."""
from datetime import datetime, timezone
from itertools import permutations, product
import json
from dlx1_audit_tools import ROOT, sha, run, input_text, decode_rows
from check_jigsaw_small import coordinate_solutions, violations
from check_jigsaw_symmetry import maps
from check_sudoku_extensions import hyper_instance

OUT = ROOT / 'results/sudoku_extensions'


def key(regions, n):
    labels = [0] * (n*n)
    for k, region in enumerate(regions):
        for v in region:
            labels[v] = k
    keys = []
    for m in maps(n):
        moved = [0] * (n*n)
        for v, k in enumerate(labels):
            moved[m[v]] = k
        renaming = {}
        keys.append(''.join(str(renaming.setdefault(k, len(renaming))) for k in moved))
    return min(keys)


def line_permutations():
    p = {frozenset(range(3*i, 3*i+3)) for i in range(3)}
    q = {frozenset(s) for s in [(1, 2, 3), (0, 4, 8), (5, 6, 7)]}
    tau = [3, 2, 1, 0, 4, 8, 7, 6, 5]
    preserving = []
    for bands in permutations(range(3)):
        for inner in product(list(permutations(range(3))), repeat=3):
            m = tuple(3*bands[r//3] + inner[r//3][r%3] for r in range(9))
            if {frozenset(m[v] for v in group) for group in q} == q:
                preserving.append(m)
    assert len(preserving) == 8
    exchanging = [tuple(tau[v] for v in m) for m in preserving]
    for m in preserving + exchanging:
        a = {frozenset(m[v] for v in group) for group in p}
        b = {frozenset(m[v] for v in group) for group in q}
        assert (a, b) in [(p, q), (q, p)]
    return [preserving, exchanging]


def variant_maps(source, target):
    found = []
    for group in line_permutations():
        for rows, columns in product(group, repeat=2):
            for transpose in [False, True]:
                cells = [9*columns[c]+rows[r] if transpose else 9*rows[r]+columns[c]
                         for r in range(9) for c in range(9)]
                old = ''.join(source[v] for v in cells)
                if any((a == '.') != (b == '.') for a, b in zip(old, target)):
                    continue
                digits = {}
                for a, b in zip(old, target):
                    if a != '.':
                        if a in digits and digits[a] != b:
                            break
                        digits[a] = b
                else:
                    if len(set(digits.values())) != len(digits):
                        continue
                    left = sorted(set('123456789') - digits.keys())
                    right = sorted(set('123456789') - set(digits.values()))
                    digits.update(zip(left, right))
                    assert ''.join(digits.get(a, '.') for a in old) == target
                    found.append(dict(rows=rows, columns=columns, transpose=transpose,
                                      new_to_old_cells=cells, digit_map=digits))
    return found


def main():
    ds = json.loads((OUT/'pdf-diagrams.json').read_text())['sources']
    small = json.loads((OUT/'small-check.json').read_text())
    for row, expected in [(0, 40), (1, 215)]:
        assert small['64-row'+str(row)]['native']['nodes'] == expected
    for label, counts in [('i', [231, 77]), ('ii', [708, 151])]:
        for mode, count in zip(['four', 'nine'], counts):
            assert small['hyper67'][label][mode]['native']['nodes'] == count

    census = {}
    for n in range(1, 7):
        tokens = (OUT/f'clueless64/n{n}.masks').read_text().split()
        masks = {int(t, 16) for t in tokens[2:]}
        assert int(tokens[0]) == n and len(masks) == int(tokens[1])
        straight = {sum(1 << (r*n+c) for c in range(n)) for r in range(n)}
        straight |= {sum(1 << (r*n+c) for r in range(n)) for c in range(n)}
        nonstraight = set()
        if n >= 3:
            original = (ROOT/f'results/jigsaw/tilings/n{n}.masks').read_text().split()
            nonstraight = {int(t, 16) for t in original[2:]}
        assert masks == nonstraight | straight
        census[n] = [json.loads(line) for line in (OUT/f'clueless64/n{n}.jsonl').read_text().splitlines()]
    old = json.loads((ROOT/'results/jigsaw/pdf-diagrams.json').read_text())['sources']
    bykey = {row['regions']: row for row in census[4]}
    n4 = [bykey[key(old[f'62n4-{i}']['regions'], 4)] for i in range(1, 9)]
    assert [len(row['solutions']) for row in n4] == [2, 0, 2, 2, 1, 2, 2, 2]
    n3 = next(row for row in census[3] if row['regions'] == '000112122')
    assert n3['solutions'] == ['123312231'] and n3['straight']

    # Transcriptions inspected against the four archived images on Brouwer's own site.
    originals = {
        '': ['.........', '.1......3', '.....8...', '.....9.4.', '.6.......', '..5......', '8.43.....', '.......2.', '.........'],
        'a': ['.4.......', '.1......3', '.....8...', '.....9.4.', '.6.......', '..5......', '8..3.....', '.......2.', '.........'],
        'b': ['.........', '.2......5', '.........', '.....3...', '.......9.', '.....7.5.', '...26....', '......8..', '1.7......'],
        'c': ['1..7.....', '......2..', '.4....9..', '.8.......', '.......5.', '.6.......', '....4....', '.........', '.....34..'],
    }
    partitions = small['hyper67']['partitions']
    regions = partitions['standard'] + partitions['derived']
    target = ''.join(ds['67q-ii']['cells'])
    target_solution = small['hyper67']['ii']['nine']['solution']
    brouwer = {}
    for suffix, rows in originals.items():
        board = ''.join(rows)
        assert len(board) == 81 and sum(v != '.' for v in board) == 11
        diagram = dict(nrows=9, ncols=9, omitted=[], cells=list(board), regions=regions)
        solutions, nodes = coordinate_solutions(diagram, '123456789')
        assert len(solutions) == 1
        names, options, moves = hyper_instance(board, list(range(9)))
        label = '67-brouwer11' + suffix
        stats, text = run(OUT/'native', label, input_text(names, options), models=True)
        (OUT/'native'/(label+'.models')).write_text(text)
        native = []
        for chosen in decode_rows(text, names, options):
            b = list(board)
            for i in chosen:
                v, k = moves[i]
                assert b[v] == '.'
                b[v] = k
            assert not violations(diagram, b)
            native.append(''.join(b))
        assert native == solutions
        mappings = variant_maps(board, target)
        for m in mappings:
            assert ''.join(m['digit_map'][solutions[0][v]] for v in m['new_to_old_cells']) == target_solution
        brouwer[suffix or 'original'] = dict(rows=rows, solution=solutions[0], coordinate_nodes=nodes,
                                             native=stats, maps_to_book=mappings,
                                             image_sha256=sha(ROOT/f'sources/sudoku_extensions/brouwer-nrc11{suffix}.png'))
    assert brouwer['original']['solution'] == brouwer['a']['solution']
    assert any(v['maps_to_book'] for v in brouwer.values())

    # Check the three explicit card-2 options in the answer, separately from model counts.
    card = {v: k for v, k in enumerate(ds['66-i-2']['cells']) if k != '.'}
    card_options = []
    for slot in [0, 1, 8]:
        r, c = divmod(slot, 3)
        card_options.append(sorted(f'{3*r+v//3}{3*c+v%3}:{k}' for v, k in card.items()))
    assert card_options == [['00:2', '11:3', '20:1', '22:4'], ['03:2', '14:3', '23:1', '25:4'], ['66:2', '77:3', '86:1', '88:4']]
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), small_check_sha256=sha(OUT/'small-check.json'),
                  n4_printed_diagrams=n4, n3_straight_witness=n3, census_input_matches=True,
                  book_node_counts_match=True, card2_printed_options=card_options, brouwer=brouwer)
    (OUT/'supplement.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS census inputs, all eight n4 diagrams, six printed node counts, card2 options, four original Brouwer puzzles')
    print('Brouwer maps to book:', {k: len(v['maps_to_book']) for k, v in brouwer.items()})


if __name__ == '__main__':
    main()
