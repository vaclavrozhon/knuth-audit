#!/usr/bin/env python3
"""Complete, independent finite census for DLX53, including every printed diagram."""
from collections import Counter
from datetime import datetime, timezone
from itertools import permutations, product
import json
from dlx1_audit_tools import ROOT, sha, run, input_text, decode_rows

OUT = ROOT/'results/sudoku_minimal'
PERMS = list(permutations(range(1, 5)))
UNITS = ([tuple(4*r+c for c in range(4)) for r in range(4)]
         + [tuple(4*r+c for r in range(4)) for c in range(4)]
         + [tuple(4*r+c for r in range(br, br+2) for c in range(bc, bc+2))
            for br in (0, 2) for bc in (0, 2)])


def valid(board):
    return all({board[v] for v in unit} == {1, 2, 3, 4} for unit in UNITS)


def all_boards():
    """Enumerate row permutations, independently of exact cover or symmetry."""
    result = set()
    for a, b in product(PERMS, repeat=2):
        if any(a[c] == b[c] for c in range(4)):
            continue
        if any(set(a[c:c+2]+b[c:c+2]) != {1, 2, 3, 4} for c in (0, 2)):
            continue
        for c in PERMS:
            if any(c[j] in (a[j], b[j]) for j in range(4)):
                continue
            d = tuple(({1, 2, 3, 4}-{a[j], b[j], c[j]}).pop() for j in range(4))
            board = a+b+c+d
            if valid(board):
                result.add(board)
    return result


def geometries():
    bands = [p for p in permutations(range(4))
             if p[0]//2 == p[1]//2 and p[2]//2 == p[3]//2]
    gs = [tuple(4*(cs[c] if transpose else rs[r])
                +(rs[r] if transpose else cs[c]) for r in range(4) for c in range(4))
          for rs, cs, transpose in product(bands, bands, (False, True))]
    assert len(set(gs)) == 128
    return gs


def relabel_to(board, target):
    mapping = {}
    for a, b in zip(board, target):
        if a in mapping and mapping[a] != b:
            return None
        mapping[a] = b
    return mapping if len(set(mapping.values())) == 4 else None


def transform_mask(mask, g):
    return sum(1 << v for v in range(16) if mask >> g[v] & 1)


def native_census(expected):
    names = [f'{kind}{i}{k}' for kind in 'prcb' for i in range(4) for k in range(4)]
    indices = {name: i+1 for i, name in enumerate(names)}
    rows, moves = [], []
    for i, j, k in product(range(4), repeat=3):
        rows.append([indices[s] for s in (f'p{i}{j}', f'r{i}{k}', f'c{j}{k}', f'b{2*(i//2)+j//2}{k}')])
        moves.append((4*i+j, k+1))
    stats, text = run(OUT/'shidoku', 'all', input_text(names, rows), models=True)
    (OUT/'shidoku/all.models').write_text(text)
    actual = set()
    for selection in decode_rows(text, names, rows):
        board = [0]*16
        for row in selection:
            v, k = moves[row]
            assert not board[v]
            board[v] = k
        assert valid(board)
        actual.add(tuple(board))
    assert actual == expected
    stats['model_sha256'] = sha(OUT/'shidoku/all.models')
    return stats


def main():
    source = json.loads((OUT/'pdf-grids.json').read_text())['sources']
    boards, gs = all_boards(), geometries()
    assert len(boards) == 288
    references = {label: tuple(map(int, source['53'+label]['cells'])) for label in 'AB'}
    assert all(b in boards for b in references.values())
    orbits, automorphisms, canonical, results = {}, {}, {}, {}
    all_minimals = set()
    for label, ref in references.items():
        orbit = {tuple(rename[ref[g[v]]-1] for v in range(16)) for g in gs for rename in PERMS}
        assert orbit <= boards
        orbits[label] = orbit
        autos = [g for g in gs if relabel_to(tuple(ref[v] for v in g), ref)]
        automorphisms[label] = autos
        assert len(autos) == (32 if label == 'A' else 16)
        assert len(orbit) == 3072//len(autos)
        # Histogram of all exact agreement sets; superset zeta transform gives
        # the complete solution count for EVERY one of the 65536 clue masks.
        counts = [0]*65536
        for board in boards:
            mask = sum(1 << v for v in range(16) if board[v] == ref[v])
            counts[mask] += 1
        for v in range(16):
            for mask in range(65536):
                if not mask >> v & 1:
                    counts[mask] += counts[mask | (1 << v)]
        assert counts[0] == 288 and counts[-1] == 1
        assert all(counts[m] > 1 for m in range(65536) if m.bit_count() < 4)
        minimal = [m for m in range(65536) if counts[m] == 1
                   and all(counts[m ^ (1 << v)] > 1 for v in range(16) if m >> v & 1)]
        reps = {min(transform_mask(m, g) for g in autos) for m in minimal}
        canonical[label] = reps
        for m in reps:
            all_minimals.add((label, m))
        # Every region of the displayed C is a four-cell Latin trade for A and B.
        trades = []
        for region in 'ABCD':
            cells = [v for v,c in enumerate(source['53C']['cells']) if c == region]
            digits = sorted({ref[v] for v in cells})
            assert len(cells) == 4 and len(digits) == 2
            other = list(ref)
            for v in cells:
                other[v] = digits[1] if ref[v] == digits[0] else digits[0]
            assert tuple(other) in boards and all(other[v] == ref[v] for v in range(16) if v not in cells)
            trades.append(dict(region=region, cells=cells, alternative=other))
        results[label] = dict(orbit_size=len(orbit), automorphisms=len(autos),
                             minimal_masks=minimal, minimal_orbit_representatives=sorted(reps),
                             by_size=dict(sorted(Counter(m.bit_count() for m in minimal).items())),
                             orbits_by_size=dict(sorted(Counter(m.bit_count() for m in reps).items())),
                             trades=trades)
        (OUT/f'shidoku-{label}-all-subset-counts.json').write_text(json.dumps(counts)+'\n')
    assert not orbits['A'] & orbits['B'] and orbits['A'] | orbits['B'] == boards
    assert results['A']['orbits_by_size'][4] == 2 and results['B']['orbits_by_size'][4] == 11
    assert Counter(m.bit_count() for _,m in all_minimals) == {4:13, 5:22, 6:1}

    diagrams, printed_orbits = [], set()
    for name, source_grid in source.items():
        if not name.startswith('53-'):
            continue
        # Letter names designate arbitrary pairwise distinct digits.
        puzzle = tuple('WXYZ'.index(c)+1 if c != '.' else 0 for c in source_grid['cells'])
        completions = [b for b in boards if all(not x or x == b[v] for v,x in enumerate(puzzle))]
        assert len(completions) == 1, name
        solution = completions[0]
        label = next(label for label in 'AB' if solution in orbits[label])
        g = next(g for g in gs if relabel_to(tuple(solution[v] for v in g), references[label]))
        mask = sum(1 << v for v,x in enumerate(puzzle) if x)
        transformed = transform_mask(mask, g)
        rep = min(transform_mask(transformed, a) for a in automorphisms[label])
        assert rep in canonical[label]
        key = (label, rep)
        assert key not in printed_orbits
        printed_orbits.add(key)
        diagrams.append(dict(name=name, clues=mask.bit_count(), reference=label,
                             orbit_representative=rep, solution=solution))
    assert printed_orbits == {(label,m) for label,m in all_minimals if m.bit_count() in (4, 6)}
    six = source['53-bottom-1']['cells']
    cmaps = [source['53C']['cells'], [source['53C']['cells'][4*c+r] for r in range(4) for c in range(4)]]
    assert all(any(any(all(six[v] == '.' or v == removed for v in range(16) if cmap[v] == region)
                       for region in 'ABCD') for cmap in cmaps)
               for removed,x in enumerate(six) if x != '.')
    native = native_census(boards)
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), grids_sha256=sha(OUT/'pdf-grids.json'),
                  native=native, complete_boards=sorted(boards), references=results,
                  diagrams=diagrams, total_minimal_orbits={4:13, 5:22, 6:1},
                  scope='All boards and all clue subsets of both solution classes. '
                        'Original DLX1 independently agrees on the complete 288-board set. '
                        'Every printed diagram is unique, irredundant, and represents a distinct required orbit. '
                        'Historical Russell2006 attribution checked separately.')
    (OUT/'shidoku.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({label:{k:v for k,v in r.items() if k in ('orbit_size','automorphisms','by_size','orbits_by_size')}
                      for label,r in results.items()}, indent=2))
    print('All 14 diagrams, 288 boards, 131072 subsets, and 36 minimal puzzle orbits verified.')


if __name__ == '__main__':
    main()
