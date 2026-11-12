"""Vertex-matched MacMahon squares, DLX141. No import-time searches."""
from collections import Counter
from itertools import permutations, product
from pathlib import Path
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/vertices141'
CASES = [('hole5', 5, 5, {(2, 2)}), ('rect4x6', 6, 4, set()), ('rect3x8', 8, 3, set())]


def tile(word):
    return min(word[i:] + word[:i] for i in range(4))


def inventory(palette='abc'):
    words = [''.join(w) for w in product(palette, repeat=4)]
    return words, sorted({tile(w) for w in words})


def cells(width, height, holes=()):
    return [(x, y) for x in range(width) for y in range(height) if (x, y) not in holes]


def corners(cell):
    x, y = cell
    return [(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)]


def vertices(board):
    return sorted({v for cell in board for v in corners(cell)})


def color_key(word):
    labels = {}
    return ''.join(labels.setdefault(c, chr(97 + len(labels))) for c in word)


def validate(board, word, palette='abc', complete=True):
    vv = vertices(board)
    assert len(word) == len(vv) and set(word) <= set(palette)
    colors = dict(zip(vv, word))
    tiles = [tile(''.join(colors[v] for v in corners(cell))) for cell in board]
    assert len(set(tiles)) == len(tiles)
    if complete:
        assert sorted(tiles) == inventory(palette)[1]
    return colors


def problem(board, palette='abc', complete=True):
    words, tiles = inventory(palette)
    vv = vertices(board)
    position = lambda c: 'p' + str(c[0]) + '_' + str(c[1])
    vertex = lambda v: 'v' + str(v[0]) + '_' + str(v[1])
    primary = [position(c) for c in board] + (tiles if complete else [])
    secondary = ([] if complete else tiles) + [vertex(v) for v in vv]
    rows = [[position(c), tile(w)] + [vertex(v) + ':' + k for v, k in zip(corners(c), w)]
            for c in board for w in words]
    return dict(header=primary + ['|'] + secondary, rows=rows, cells=board,
                vertices=vv, palette=palette, complete=complete)


def native_text(enc):
    return ' '.join(enc['header']) + '\n' + ''.join(' '.join(row) + '\n' for row in enc['rows'])


def decode_native(raw, board, palette='abc', complete=True):
    import re
    models, colors, chosen, begun = [], {}, [], False
    def finish():
        assert len(chosen) == len(board) and set(chosen) == set(board)
        word = ''.join(colors[v] for v in vertices(board))
        validate(board, word, palette, complete)
        models.append(word)
    for line in raw.decode().splitlines():
        if re.fullmatch(r'\d+:\s*', line):
            if begun:
                finish()
            colors, chosen, begun = {}, [], True
        elif line.strip():
            tokens = re.sub(r'\s*\(\d+ of \d+\)\s*$', '', line).split()
            positions = [t for t in tokens if re.fullmatch(r'p\d+_\d+', t)]
            assert begun and len(positions) == 1
            cell = tuple(map(int, positions[0][1:].split('_')))
            chosen.append(cell)
            local = {}
            for token in tokens:
                if token.startswith('v'):
                    name, c = token.split(':')
                    v = tuple(map(int, name[1:].split('_')))
                    assert v not in colors or colors[v] == c
                    colors[v] = local[v] = c
            assert set(local) == set(corners(cell))
            assert tile(''.join(local[v] for v in corners(cell))) in tokens
    if begun:
        finish()
    assert len(set(models)) == len(models)
    return models


def independent_case(label, board, palette='abc', complete=True):
    vv = vertices(board)
    index = {v: i for i, v in enumerate(vv)}
    width = max(x for x, y in vv)
    height = max(y for x, y in vv)
    ordered = sorted(board, key=(lambda c: (c[1], c[0])) if width <= height else (lambda c: c))
    return f'{label} {len(palette)} {len(vv)} {len(board)} {int(complete)}\n' + ''.join(
        ' '.join(str(index[v]) for v in corners(c)) + '\n' for c in ordered)


def geometry_maps(board):
    vv = vertices(board)
    width = max(v[0] for v in vv)
    height = max(v[1] for v in vv)
    original = {tuple(sorted(corners(c))) for c in board}
    result = []
    for swap in [False, True]:
        if swap and width != height:
            continue
        for flipx, flipy in product([False, True], repeat=2):
            def transform(v):
                x, y = v[::-1] if swap else v
                return (width - x if flipx else x, height - y if flipy else y)
            assert {tuple(sorted(transform(v) for v in corners(c))) for c in board} == original
            result.append(tuple(vv.index(transform(v)) for v in vv))
    assert len(set(result)) == len(result)
    return result


def geometric_key(word, mappings):
    return min(color_key(''.join(word[j] for j in mapping)) for mapping in mappings)
