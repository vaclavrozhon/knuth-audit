"""Literal131 complementary-edge models; separate from all existing live jobs."""
from collections import Counter, defaultdict
from pathlib import Path
import check_macmahon as g
import macmahon126 as mc
import symmetries129 as sy
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/mating131'
MATES = {'a': 'abdc', 'b': 'badc'}


def mate(c, mode):
    return MATES[mode][ord(c)-97]


def problem(mode, symmetry=None):
    assert mode in MATES and (symmetry is None or mode == 'b')
    primary = [g.name(t) for t in g.TRIANGLES]+g.PIECES+['*']
    edges = sorted(g.EDGE_TRIANGLES)
    pairs = []
    if symmetry:
        action = sy.BY[symmetry]
        pairs = sorted({tuple(sorted((e, sy.ES[action['edges'][sy.EI[e]]]))) for e in edges
                        if len(g.EDGE_TRIANGLES[e]) == 2 and e != sy.ES[action['edges'][sy.EI[e]]]})
        primary += ['#'+mc.edge_name(a) for a, b in pairs]
    header = primary+['|']+[mc.edge_name(e) for e in edges]
    rows, placements = [], []
    for t in g.TRIANGLES:
        for p in g.PIECES:
            if mode == 'a' and p == 'aaa' and t != (0, 2, 0):
                continue
            for cs in sorted({p[i:]+p[:i] for i in range(3)}):
                values = ''.join(mate(c, mode) for c in cs) if t[2] else cs
                rows.append([g.name(t), p]+[mc.edge_name(e)+':'+c for e, c in zip(g.edges(t), values)])
                placements.append(dict(cell=t, tile=p, colors=cs))
    boundary = [e for e in edges if len(g.EDGE_TRIANGLES[e]) == 1]
    forced = {e: 'a' if mode == 'a' or e[0] != '-' else 'b' for e in boundary}
    rows.append(['*']+[mc.edge_name(e)+':'+forced[e] for e in boundary])
    placements.append(None)
    for a, b in pairs:
        for c in g.COLORS:
            rows.append(['#'+mc.edge_name(a), mc.edge_name(a)+':'+c, mc.edge_name(b)+':'+c])
            placements.append(None)
    enc = dict(mode=mode, symmetry=symmetry, header=header, rows=rows, placements=placements,
               edges=edges, primary_names=primary, pairs=pairs, boundary=forced)
    literal = "01' abc -02:a /11:b \\01:d" if mode == 'a' else "01' abc -02:b /11:a \\01:d"
    assert tuple(sorted(literal.split())) in {tuple(sorted(row)) for row in rows}
    if symmetry == 'r3':
        assert len(pairs) == 15
        # A primary selector's arbitrary name is immaterial. Our sorted
        # representative is /20; the printed example chooses /23 instead.
        assert tuple(sorted('#/20 /23:a /20:a'.split())) in {tuple(sorted(row)) for row in rows}
    return enc


def validate(model, enc):
    """Validate physical triangle sides by endpoints and mating, not XCC row names."""
    edge_incidence, cells, tiles = defaultdict(list), {}, []
    for index in model:
        placement = enc['placements'][index]
        if placement is None:
            continue
        t = tuple(placement['cell']); cs = placement['colors']
        assert t not in cells; cells[t] = cs; tiles.append(g.piece(cs))
        u, v, w = g.vertices(t)
        a, b = (v, u) if t[2] else (u, v)
        for pair, color in zip([(w, a), (w, b), (u, v)], cs):
            edge_incidence[frozenset(pair)].append((t, color))
    assert set(cells) == set(g.TRIANGLES) and sorted(tiles) == g.PIECES
    encoded = {}
    for e in enc['edges']:
        adjacent = g.EDGE_TRIANGLES[e]
        # Independent physical endpoint incidence; sy.ends returns actual endpoints.
        seen = edge_incidence[frozenset(sy.ends(e))]
        assert {t for t, c in seen} == set(adjacent)
        normalized = {mate(c, enc['mode']) if t[2] else c for t, c in seen}
        assert len(normalized) == 1
        encoded[e] = normalized.pop()
        if len(seen) == 2:
            assert mate(seen[0][1], enc['mode']) == seen[1][1]
        else:
            assert encoded[e] == enc['boundary'][e]
    if enc['mode'] == 'a':
        assert cells[0, 2, 0] == 'aaa'
    assert all(encoded[a] == encoded[b] for a, b in enc['pairs'])
    return ''.join(encoded[e] for e in enc['edges'])
