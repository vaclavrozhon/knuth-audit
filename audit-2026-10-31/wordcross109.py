"""Literal edge/occupancy XCC construction, with direct geometric validation."""
from itertools import product
import argparse
import json
from layout_native import ROOT, OUT, encode, save, sha, run, read_models

WORDS = 'ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN'.split()


def instance(words, m, n, symmetry=True, fixed=None):
    edges = [(r*n+c, r*n+c+1, f'H{r+1}{c+1}') for r in range(m) for c in range(n-1)]
    edges += [(r*n+c, (r+1)*n+c, f'V{r+1}{c+1}') for r in range(m-1) for c in range(n)]
    edge_for = {frozenset([u, v]): name for u, v, name in edges}
    primary = [f'#{k}' for k in range(len(words))] + [e for u, v, e in edges]
    secondary = [f'X{c}' for c in range(m*n)] + [f'Q{c}' for c in range(m*n)]
    rows = []
    info = []
    for wi, word in enumerate(words):
        assert len(word) >= 2
        for direction in [0, 1]:
            if symmetry and m == n and wi == 0 and direction == 1:
                continue
            dr, dc = [(0, 1), (1, 0)][direction]
            for r, c in product(range(m), range(n)):
                if r+dr*(len(word)-1) >= m or c+dc*(len(word)-1) >= n:
                    continue
                cells = tuple((r+dr*k)*n+c+dc*k for k in range(len(word)))
                if fixed is not None and fixed.get(wi, cells) != cells:
                    continue
                row = [(f'#{wi}', 0)]
                if r-dr >= 0 and c-dc >= 0:
                    cell = (r-dr)*n+c-dc
                    row += [(f'X{cell}', 27), (f'Q{cell}', 1)]
                for k, (cell, letter) in enumerate(zip(cells, word)):
                    row += [(f'X{cell}', ord(letter)-64), (f'Q{cell}', 2)]
                    if k+1 < len(cells):
                        row += [(edge_for[frozenset([cell, cells[k+1]])], 0)]
                rr, cc = r+dr*len(word), c+dc*len(word)
                if rr < m and cc < n:
                    cell = rr*n+cc
                    row += [(f'X{cell}', 27), (f'Q{cell}', 1)]
                rows.append(row)
                info.append(dict(word=wi, direction=direction, cells=cells))
    for u, v, edge in edges:
        for a, b in [(0, 1), (1, 0), (0, 0)]:
            row = [(edge, 0), (f'Q{u}', a+1), (f'Q{v}', b+1)]
            if not a:
                row += [(f'X{u}', 27)]
            if not b:
                row += [(f'X{v}', 27)]
            rows.append(row)
            info.append(dict(edge=edge, endpoints=[u, v], occupancy=[a, b]))
    return encode(primary, secondary, rows), info


def geometry(words, m, n, chosen):
    """Validate only actual word placements; ignore all auxiliary color choices."""
    assert len(chosen) == len(words)
    board = ['.']*(m*n)
    occupied = {}
    traversed = set()
    for wi, placement in enumerate(chosen):
        cells = placement['cells']
        assert len(cells) == len(words[wi])
        direction = placement['direction']
        for j, cell in enumerate(cells):
            assert 0 <= cell < m*n
            if j:
                assert cell-cells[j-1] == (1 if direction == 0 else n)
                if direction == 0:
                    assert cell//n == cells[0]//n
                traversed.add(frozenset([cells[j-1], cell]))
            assert board[cell] in ['.', words[wi][j]]
            for other in occupied.get(cell, []):
                assert chosen[other]['direction'] != direction
            board[cell] = words[wi][j]
            occupied.setdefault(cell, []).append(wi)
    for cell in occupied:
        r, c = divmod(cell, n)
        for rr, cc in [(r+1, c), (r, c+1)]:
            if rr < m and cc < n and rr*n+cc in occupied:
                assert frozenset([cell, rr*n+cc]) in traversed
    groups = [{i} for i in range(len(words))]
    for ws in occupied.values():
        for u in ws:
            for v in ws:
                union = groups[u] | groups[v]
                for w in union:
                    groups[w] = union
    components = len({tuple(sorted(g)) for g in groups})
    overlaps = sum(len(ws)-1 for ws in occupied.values())
    return dict(board=''.join(board), components=components, intersections=overlaps)


def decode(label, enc, info, words, m, n):
    native_models = 0
    connected_models = 0
    placements = {}
    for model in read_models(label, enc):
        native_models += 1
        chosen = sorted((info[i] for i in model if 'word' in info[i]), key=lambda x:x['word'])
        assert [p['word'] for p in chosen] == list(range(len(words)))
        result = geometry(words, m, n, chosen)
        connected_models += result['components'] == 1
        key = tuple(tuple(p['cells']) for p in chosen)
        placements[key] = dict(chosen=chosen, **result)
    result = dict(script_sha256=sha(__file__), m=m, n=n, words=words,
        native_models=native_models, connected_native_models=connected_models,
        distinct_placements=len(placements), connected_distinct_placements=sum(p['components']==1 for p in placements.values()),
        placements=[placements[k] for k in sorted(placements)])
    save(OUT / (label+'-decoded.json'), result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--m', type=int, default=8)
    parser.add_argument('--n', type=int, default=8)
    parser.add_argument('--line-witness', action='store_true')
    args = parser.parse_args()
    if args.line_witness:
        assert sum(map(len, WORDS)) == 43
        fixed = {}
        start = 0
        for wi, word in enumerate(WORDS):
            fixed[wi] = tuple(range(start, start+len(word)))
            start += len(word)+1
        assert start-1 == 53
        enc, info = instance(WORDS, 1, 53, fixed=fixed)
        label = 'wordcross109-line53-witness'
        m, n = 1, 53
    else:
        m, n = args.m, args.n
        enc, info = instance(WORDS, m, n)
        label = f'wordcross109-{m}x{n}'
        if m == n == 8:
            assert len(enc['rows']) == 1192 and enc['primary'] == 123 and len(enc['names'])-enc['primary'] == 128
    build = json.loads((ROOT / 'results/puzzles101_107/word-variants-build.json').read_text())
    binary = build['binaries']['dlx2-sharp']
    assert sha(binary['path']) == binary['sha256']
    result = run(label, enc, binary=binary['path'])
    assert result['status'] == 'completed', result
    decoded = decode(label, enc, info, WORDS, m, n)
    print(label, {k:decoded[k] for k in ['native_models','connected_native_models','distinct_placements','connected_distinct_placements']}, flush=True)


if __name__ == '__main__':
    main()
