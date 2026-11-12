"""Geometric actions and finite proof certificates for DLX129.

No search is run on import.  Point/edge permutations are constructed from
endpoints, independently of the secondary-item names in the old XCC inputs.
"""
from collections import Counter
from datetime import datetime, timezone
from itertools import permutations, product
from pathlib import Path
import json

import check_macmahon as g
from graph_native import sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/symmetries129'
ES = sorted(g.EDGE_TRIANGLES)
EI = {e: i for i, e in enumerate(ES)}
TS = tuple(g.TRIANGLES)
TI = {t: i for i, t in enumerate(TS)}


def ends(e):
    kind, x, y = e
    return tuple(sorted(((x, y), (x + 1, y)) if kind == '-' else
                        ((x, y), (x, y + 1)) if kind == '/' else
                        ((x + 1, y), (x, y + 1))))


def point(p, rotation=0, reflected=False):
    x, y = p[0] - 2, p[1] - 2
    if reflected:
        x, y = y, x
    for _ in range(rotation):
        x, y = -y, x + y
    return x + 2, y + 2


def actions():
    ev = {ends(e): i for i, e in enumerate(ES)}
    tv = {frozenset(g.vertices(t)): i for i, t in enumerate(TS)}
    result = []
    for reflected, rotation in product((False, True), range(6)):
        ep = tuple(ev[tuple(sorted(point(p, rotation, reflected) for p in ends(e)))] for e in ES)
        tp = tuple(tv[frozenset(point(p, rotation, reflected) for p in g.vertices(t))] for t in TS)
        assert sorted(ep) == list(range(42)) and sorted(tp) == list(range(24))
        label = ('f' if reflected else 'r') + str(rotation)
        if tuple(TS[i] for i in tp) == tuple(g.reflect(t, 'lr') for t in TS):
            label = 'lr'
        if tuple(TS[i] for i in tp) == tuple(g.reflect(t, 'tb') for t in TS):
            label = 'tb'
        result.append(dict(label=label, rotation=rotation, reflected=reflected, edges=ep, cells=tp))
    assert len({a['edges'] for a in result}) == 12
    assert {'lr', 'tb'} <= {a['label'] for a in result}
    return result


D6 = actions()
BY = {a['label']: a for a in D6}
CP = tuple(''.join(p) for p in permutations('abcd'))
SIGMA = 'dcba'
CENTRALIZER = tuple(p for p in CP if all(p[3-i] == SIGMA[ord(p[i])-97] for i in range(4)))
assert len(CENTRALIZER) == 8


def transform(colors, action, colorperm='abcd'):
    out = [None] * 42
    for i, j in enumerate(action['edges']):
        out[j] = colorperm[ord(colors[i])-97]
    return ''.join(out)


def cells(colors):
    return {t: ''.join(colors[EI[e]] for e in g.edges(t)) for t in TS}


def validate(colors):
    assert len(colors) == 42 and set(colors) == set('abcd')
    cc = cells(colors)
    assert sorted(g.piece(cs) for cs in cc.values()) == g.PIECES
    return cc


def mono_positions(colors):
    cc = validate(colors)
    return {cs[0]: t for t, cs in cc.items() if len(set(cs)) == 1}


def symmetry_flags(colors):
    original = cells(colors)
    masks = [g.patchmask(original[t]) for t in TS]
    weak, strong = [], {}
    for action in D6:
        moved = transform(colors, action)
        if [g.patchmask(cs) for cs in cells(moved).values()] == masks:
            weak.append(action['label'])
        mapping = {a: {b for aa, b in zip(moved, colors) if aa == a} for a in 'abcd'}
        if all(len(v) == 1 for v in mapping.values()):
            p = ''.join(next(iter(mapping[c])) for c in 'abcd')
            if p in CP:
                strong[action['label']] = p
    return dict(weak=weak, strong=strong)


def normalize_colors(colors):
    mapping = {}
    return ''.join(mapping.setdefault(c, 'abcd'[len(mapping)]) if c not in mapping else mapping[c]
                   for c in colors)


def axis_canonical(colors, axis='lr'):
    """Normalize the unique axis, then all global color permutations."""
    return min(normalize_colors(transform(colors, BY[k])) for k in ('r0', 'r3', 'lr', 'tb'))


def canonical_types(colors, mode):
    monos = mono_positions(colors)
    types = g.TYPES if mode == 'rotation' else g.TB_TYPES
    action = BY['r3' if mode == 'rotation' else 'tb']
    if any(monos[SIGMA[ord(c)-97]] != TS[action['cells'][TI[t]]] for c, t in monos.items()):
        return []
    found = []
    for kind, (a, bs, selector) in types.items():
        if monos['a'] == a and monos['b'] in bs and (selector is None or colors[EI[selector]] in 'ac'):
            found.append(kind)
    return found


def all_canonical_types(colors, mode):
    result = []
    for action in D6:
        for cp in CP:
            moved = transform(colors, action, cp)
            for kind in canonical_types(moved, mode):
                result.append(dict(kind=kind, action=action['label'], colors=cp))
    return result


def cycles(perm):
    unseen = set(range(len(perm)))
    out = []
    while unseen:
        x = min(unseen)
        part = []
        while x not in part:
            part.append(x)
            unseen.remove(x)
            x = perm[x]
        assert x == part[0]
        out.append(part)
    return out


def general_proofs():
    # Only the half turn can preserve the set of four monochromatic cells.
    rotations = {}
    for k in range(1, 6):
        c = cycles(BY[f'r{k}']['cells'])
        lengths = set(map(len, c))
        assert len(lengths) == 1
        n = next(iter(lengths))
        assert (4 % n == 0) == (k == 3)
        rotations[str(60*k)] = dict(cell_orbits=len(c), orbit_size=n, can_preserve_four_cells=4 % n == 0)

    involutions = [p for p in CP if all(p[ord(p[i])-97] == chr(97+i) for i in range(4))]
    assert len(involutions) == 10
    reflection = {}
    for axis in ('tb', 'lr'):
        action = BY[axis]
        fixed_cells = [TS[i] for i, j in enumerate(action['cells']) if i == j]
        fixed_edges = [ES[i] for i, j in enumerate(action['edges']) if i == j]
        rejected = []
        for cp in involutions:
            fixed_colors = [c for c, d in zip('abcd', cp) if c == d]
            fixed_pieces = [tile for tile in g.PIECES
                            if g.piece(''.join(cp[ord(c)-97] for c in (tile[0], tile[2], tile[1]))) == tile]
            # Every fixed type occurs exactly once, hence must occupy a fixed cell.
            # A geometrically fixed edge requires a fixed color.
            reason = 'fixed edge has no fixed color' if not fixed_colors else 'more fixed tile types than fixed cells'
            assert not fixed_colors or len(fixed_pieces) > len(fixed_cells)
            rejected.append(dict(color_involution=cp, fixed_colors=fixed_colors, fixed_pieces=fixed_pieces, reason=reason))
        reflection[axis] = dict(fixed_cells=fixed_cells, fixed_edges=fixed_edges, excluded_involutions=rejected)
    assert len(reflection['tb']['fixed_cells']) == 0 and len(reflection['tb']['fixed_edges']) == 4
    assert len(reflection['lr']['fixed_cells']) == 4 and len(reflection['lr']['fixed_edges']) == 2
    special = next(x for x in reflection['lr']['excluded_involutions'] if x['color_involution'] == 'acbd')
    assert special['fixed_pieces'] == sorted(['aaa', 'aad', 'abc', 'acb', 'bcd', 'bdc', 'add', 'ddd'])

    # Two distinct axes of the same conjugacy class compose to a forbidden120-degree rotation.
    axis_products = []
    for a in D6:
        if not a['reflected']:
            continue
        for b in D6:
            if not b['reflected'] or a is b:
                continue
            c = tuple(a['cells'][b['cells'][i]] for i in range(24))
            product_label = next(v['label'] for v in D6 if v['cells'] == c)
            same_type = sum(i == j for i, j in enumerate(a['cells'])) == sum(i == j for i, j in enumerate(b['cells']))
            assert product_label in ('r2', 'r4') if same_type else product_label in ('r1', 'r3', 'r5')
            axis_products.append(dict(left=a['label'], right=b['label'], product=product_label, same_axis_type=same_type))

    # Independently generate all invariant nonadjacent monochrome sets from point actions.
    from itertools import combinations
    mono_sets = {}
    for axis in ('lr', 'tb', 'r3'):
        action = BY[axis]
        sets = []
        for sub in combinations(TS, 4):
            if {TS[action['cells'][TI[t]]] for t in sub} != set(sub):
                continue
            physical_edges = [ends(e) for t in sub for e in g.edges(t)]
            if len(physical_edges) != len(set(physical_edges)):
                continue
            sets.append(sub)
        if axis in ('lr', 'tb'):
            assert sets == g.mono_sets(axis)
        mono_sets[axis] = dict(total=len(sets), by_fixed_cells=dict(Counter(sum(action['cells'][TI[t]] == TI[t] for t in sub) for sub in sets)))
    assert mono_sets['lr'] == {'total': 67, 'by_fixed_cells': {0: 35, 2: 32}}
    return dict(rotation_obstruction=rotations, reflection_obstruction=reflection, axis_products=axis_products,
                monochrome_geometry_census=mono_sets, strong_halfturn_color_involutions=['badc', 'cdab', 'dcba'],
                centralizer=list(CENTRALIZER), residual_group_order=96, strong_stabilizer_order=2,
                strong_orbit_size=48,
                explanation='Four single-color cells exclude all nontrivial rotations except180. Fixed-edge and fixed-tile obstructions exclude every strong reflection. Thus a strong coloring has exactly identity and halfturn/color-swap in its stabilizer. At most one weak axis of each type is possible; coexistence forces their perpendicular pair and a weak halfturn.')


def selector_proof(mode):
    """Check canonical completeness on every admissible colored mono geometry.

    Count admissible group elements rather than solutions. The selector
    predicates involve at most a few source edges, so their truth table can
    be checked exhaustively without redoing the huge tiling enumeration.
    """
    partner = BY['r3' if mode == 'rotation' else 'tb']
    spatial = D6 if mode == 'rotation' else [BY[k] for k in ('r0', 'r3', 'lr', 'tb')]
    types = g.TYPES if mode == 'rotation' else g.TB_TYPES
    cases = []
    for a, b in product(TS, repeat=2):
        d, c = (TS[partner['cells'][TI[t]]] for t in (a, b))
        monos = dict(zip('abcd', (a, b, c, d)))
        if len(set(monos.values())) != 4:
            continue
        es = [e for t in monos.values() for e in g.edges(t)]
        if len(es) != len(set(es)):
            continue
        fixed = {e: color for color, t in monos.items() for e in g.edges(t)}
        tests = []
        for action, cp in product(spatial, CENTRALIZER):
            transformed = {cp[ord(color)-97]: TS[action['cells'][TI[t]]] for color, t in monos.items()}
            for kind, (aa, bs, selector) in types.items():
                if transformed['a'] != aa or transformed['b'] not in bs:
                    continue
                source = None if selector is None else ES[action['edges'].index(EI[selector])]
                allowed = ''.join(color for color in 'abcd' if cp[ord(color)-97] in 'ac')
                tests.append((kind, source, allowed))
        relevant = sorted({e for _, e, _ in tests if e is not None and e not in fixed})
        histogram = Counter()
        # Small predicate truth table: these are NOT assumed to be valid tilings.
        # A constant result on all assignments is stronger than needed.
        for cs in product('abcd', repeat=len(relevant)):
            values = fixed | dict(zip(relevant, cs))
            histogram[sum(e is None or values[e] in allowed for _, e, allowed in tests)] += 1
        assert set(histogram) == {2}, (mode, monos, tests, histogram)
        cases.append(dict(monos=monos, types=sorted({k for k, _, _ in tests}),
                          unfiltered_transforms=len(tests), selector_source_edges=relevant,
                          color_assignments=sum(histogram.values()), accepted_transforms=2))
    assert cases
    return dict(mode=mode, configurations=len(cases), cases=cases,
                claim='Every valid colored mono geometry has exactly two canonicalizing group elements, for every assignment of the selector colors. Strong halfturn stabilizer2 gives one representative; trivial strong stabilizer gives two. For the TB mode, the residual group has32 elements and only the261 special strong-rotation cases have stabilizer2.')


def main():
    OUT.mkdir(exist_ok=True)
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=sha(__file__),
                  geometry_source_sha256=sha(g.__file__), general=general_proofs(),
                  selectors=[selector_proof('rotation'), selector_proof('tb')])
    (OUT/'geometric-proofs.json').write_text(json.dumps(result, indent=2)+'\n')
    print('PASS129 general obstructions and selectors:', [(d['mode'], d['configurations']) for d in result['selectors']])


if __name__ == '__main__':
    main()
