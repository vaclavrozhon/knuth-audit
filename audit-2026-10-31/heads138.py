"""DLX138: signed square edges, CCW from north (N,W,S,E).

An uppercase edge is a head, its lowercase mate is a tail. Reflections
are transformations of a complete arrangement, not allowed placements
of an individual tile. No searches or writes happen at import time.
"""
from collections import Counter
from itertools import permutations
from pathlib import Path
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/heads138'
TILES = tuple(''.join(p[:2]) + ''.join(p[2:]).lower() for p in permutations('ABCD'))
DIRS = ((-1, 0), (0, -1), (1, 0), (0, 1))


def rotations(word):
    return tuple(word[i:] + word[:i] for i in range(4))


def tile(word):
    return next(w for w in rotations(word) if w[:2].isupper() and w[2:].islower())


def validate(words, nr, nc, torus=False, joker=None):
    assert len(words) == nr * nc
    inventory = []
    for u, word in enumerate(words):
        assert len(word) == 4 and sorted(word.upper()) == list('ABCD')
        if joker is not None and u == (nr * nc // 2):
            assert word == joker
        else:
            inventory.append(tile(word))
        r, c = divmod(u, nc)
        for d, (dr, dc) in enumerate(DIRS):
            rr, cc = r + dr, c + dc
            if torus:
                rr %= nr; cc %= nc
            if 0 <= rr < nr and 0 <= cc < nc:
                assert word[d] == words[rr * nc + cc][(d + 2) % 4].swapcase(), (u, d)
            elif joker is not None:
                # Each outside side has the color of the corresponding
                # central-joker edge; its heads/tails need not be uniform.
                assert word[d].upper() == joker[d].upper(), (u, d, word, joker)
    assert Counter(inventory) == Counter(TILES)
    return True


def problem(kind, anchor_orientations=(0, 1, 2, 3), joker='ABCD'):
    nr, nc = (4, 6) if kind == 'torus' else (5, 5)
    torus = kind == 'torus'
    cells = tuple((r, c) for r in range(nr) for c in range(nc))
    def edges(r, c):
        return (f'h{r}{c}', f'v{r}{c}',
                f'h{(r + 1) % nr if torus else r + 1}{c}',
                f'v{r}{(c + 1) % nc if torus else c + 1}')
    secondary = sorted({e for r, c in cells for e in edges(r, c)})
    primary = [f'p{r}{c}' for r, c in cells] + list(TILES)
    rows, placements = [], []
    for r, c in cells:
        if not torus and (r, c) == (2, 2):
            candidates = [(None, joker)]
        else:
            candidates = [(t, w) for t in TILES for w in rotations(t)]
        for t, w in candidates:
            if torus:
                if (r, c) == (0, 0):
                    if t != 'ABcd' or w not in [rotations(t)[i] for i in anchor_orientations]:
                        continue
                elif t == 'ABcd':
                    continue
            else:
                if any(not (0 <= r + dr < nr and 0 <= c + dc < nc) and w[d].upper() != joker[d].upper()
                       for d, (dr, dc) in enumerate(DIRS)):
                    continue
            row = [f'p{r}{c}'] + ([t] if t else [])
            # Reversing polarity on S/E changes complement matching into
            # ordinary equality of XCC colors, also across torus seams.
            row += [e + ':' + (ch if d < 2 else ch.swapcase())
                    for d, (e, ch) in enumerate(zip(edges(r, c), w))]
            rows.append(row); placements.append([r * nc + c, w])
    return dict(kind=kind, nr=nr, nc=nc, primary=len(primary), secondary=len(secondary),
                header=primary + ['|'] + secondary, rows=rows, placements=placements,
                anchor_orientations=list(anchor_orientations) if torus else None,
                joker=None if torus else joker)


def native_text(enc):
    return ' '.join(enc['header']) + '\n' + '\n'.join(' '.join(row) for row in enc['rows']) + '\n'


def spatial(words, nr, nc, shift=(0, 0), flipr=False, flipc=False, transpose=False):
    new = [None] * len(words)
    out_r, out_c = (nc, nr) if transpose else (nr, nc)
    for u, word in enumerate(words):
        r, c = divmod(u, nc)
        r = (-r if flipr else r) + shift[0]
        c = (-c if flipc else c) + shift[1]
        r %= nr; c %= nc
        if transpose:
            r, c = c, r
        sides = [''] * 4
        for d, (dr, dc) in enumerate(DIRS):
            if flipr: dr = -dr
            if flipc: dc = -dc
            if transpose: dr, dc = dc, dr
            sides[DIRS.index((dr, dc))] = word[d]
        new[r * out_c + c] = ''.join(sides)
    return new


def rename(words, mapping):
    table = {**mapping, **{k.lower():v.lower() for k,v in mapping.items()}}
    return [''.join(table[ch] for ch in w) for w in words]


def normalize_colors(words):
    canonical = tile(words[0])
    return rename(words, dict(zip(canonical.upper(), 'ABCD')))
