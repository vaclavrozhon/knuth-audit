"""Original and published improved XCC reductions for Sudoku automorphisms."""
from itertools import product
import argparse
from layout_native import OUT, encode, save, sha, run, read_models


def instance(base=3, improved=True, alpha=None):
    n = base*base
    cells = list(product(range(n), repeat=2))
    alpha = alpha or {(i, j): (j, i) for i, j in cells}
    assert set(alpha) == set(cells) and set(alpha.values()) == set(cells)
    primary = [f'{kind}{i}{k}' for kind in 'prcb' for i in range(n) for k in range(n)]
    if not improved:
        primary += [f'{kind}{i}{k}' for kind in 'RCB' for i in range(n) for k in range(n)]
    primary += [f'{kind}{k}' for kind in 'uv' for k in range(n)]
    secondary = [f'q{k}' for k in range(n)] + [f'x{i}{j}' for i, j in cells]
    rows = [[(f'u{k}', 0), (f'v{l}', 0), (f'q{k}', l+1)] for k in range(n) for l in range(n)]
    info = [dict(permutation=[k, l]) for k in range(n) for l in range(n)]
    for i, j in cells:
        ii, jj = alpha[i, j]
        b = base*(i//base)+j//base
        bb = base*(ii//base)+jj//base
        for k, l in product(range(n), repeat=2):
            if (i, j) == (ii, jj) and k != l:
                continue
            if i == 0 and k != j:
                continue
            if improved and ((ii == 0 and l != jj) or (i > 0 and k == j) or (ii > 0 and l == jj)):
                continue
            if improved:
                row = [(f'p{ii}{jj}', 0), (f'r{ii}{l}', 0), (f'c{jj}{l}', 0), (f'b{bb}{l}', 0)]
            else:
                row = [(f'p{i}{j}', 0), (f'r{i}{k}', 0), (f'c{j}{k}', 0), (f'b{b}{k}', 0),
                       (f'R{ii}{l}', 0), (f'C{jj}{l}', 0), (f'B{bb}{l}', 0)]
            row += [(f'x{i}{j}', k+1)]
            if (i, j) != (ii, jj):
                row += [(f'x{ii}{jj}', l+1)]
            row += [(f'q{k}', l+1)]
            rows.append(row)
            info.append(dict(cell=[i, j], value=k, image=[ii, jj], image_value=l))
    return encode(primary, secondary, rows), info


def validate_models(label, enc, info, base):
    n = base*base
    boards = set()
    for model in read_models(label, enc):
        board = [-1]*(n*n)
        perm = {}
        for ri in model:
            r = info[ri]
            if 'permutation' in r:
                k, l = r['permutation'];perm[k] = l
            else:
                i, j = r['cell'];ii, jj = r['image']
                for pos, val in [(n*i+j, r['value']), (n*ii+jj, r['image_value'])]:
                    assert board[pos] in [-1, val]
                    board[pos] = val
        target = set(range(n))
        assert set(perm) == set(perm.values()) == target
        assert board[:n] == list(range(n))
        for r in range(n):
            assert set(board[r*n:r*n+n]) == target
            assert set(board[r::n]) == target
        for r, c in product(range(base), repeat=2):
            assert {board[n*(base*r+i)+base*c+j] for i, j in product(range(base), repeat=2)} == target
        for i, j in product(range(n), repeat=2):
            assert board[n*j+i] == perm[board[n*i+j]]
        boards.add(tuple(board))
    return boards


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', type=int, default=3)
    parser.add_argument('--original', action='store_true')
    args = parser.parse_args()
    enc, info = instance(args.base, not args.original)
    label = f'sudoku114-n{args.base**2}-' + ('original' if args.original else 'improved')
    result = run(label, enc, every=1 if args.base == 2 else 1000000)
    assert result['status'] == 'completed', result
    if args.base == 3:
        assert result['solutions'] == 30258432
    boards = validate_models(label, enc, info, args.base)
    save(OUT / (label + '-checked.json'), dict(script_sha256=sha(__file__), native_solutions=result['solutions'],
        sampled_boards=len(boards), every=result['model_output_period'],
        all_outputs_are_normalized_sudoku_with_transposition=True,
        boards=[list(b) for b in sorted(boards)]))
    print(label, result['solutions'], 'sampled', len(boards), flush=True)


if __name__ == '__main__':
    main()
