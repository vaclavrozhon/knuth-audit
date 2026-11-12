#!/usr/bin/env python3
"""Certify the19 printed relations and the tiny propagation tree for(22)."""
from collections import Counter
from fractions import Fraction as F
import json
from check_network20 import NETWORK
from check_clasp_projection import ROOT, cross2, parameter
from check_polyhedra_fixed import sub, dot, encode


# O/I are outgoing/incoming relative to the current junction. The order of
# alternatives is the actual left-to-right order of Table1, including T.
TABLE = {
    'T': ['O+I', 'O-I', 'OOI', 'OII'],
    'V': ['I+', 'IO', '+O', 'O-', 'OI', '-I'],
    'W': ['O+I', '-+-', '+-+'],
    'Y': ['IO-', 'O-I', '-IO', '---', '+++'],
}
PRINTED = {
    'a': ('ab ac', '<+ <> +> >- >< -<'),
    'b': ('be bd ab', '>+> -+- +-+'),
    'c': ('ac cd cm', '<+< -+- +-+'),
    'd': ('bd dg cd', '<-> -<< >>- --- +++'),
    'e': ('be ef eg', '<-< -<> >>- --- +++'),
    'f': ('fq fh ef', '>+> -+- +-+'),
    'g': ('dg eg gh', '<+< -+- +-+'),
    'h': ('fh hj gh', '<-> -<< >>- --- +++'),
    'i': ('ij ik', '<+ <> +> >- >< -<'),
    'j': ('jl ij hj', '>+> -+- +-+'),
    'k': ('ik kl kn', '<+< -+- +-+'),
    'l': ('jl ls kl', '<-> -<< >>- --- +++'),
    'm': ('cm mn mo', '<-< -<> >>- --- +++'),
    'n': ('kn np', '<<'),
    'o': ('mo op or', '<+< -+- +-+'),
    'p': ('op np', '>+ >< +< <- <> ->'),
    'q': ('qs fq', '<+ << +< >- >> ->'),
    'r': ('or rs', '>+ >> +> <- << -<'),
    's': ('rs ls qs', '<+> -+- +-+'),
}
ORDER = '+-<>'


def global_symbol(symbol, junction, neighbor):
    if symbol in '+-':
        return symbol
    return '>' if (symbol == 'O') == (junction < neighbor) else '<'


def full_relations():
    relations = {}
    for j, (kind, neighbors) in NETWORK.items():
        variables = [''.join(sorted((j, k))) for k in neighbors]
        rows = [''.join(global_symbol(s, j, k) for s, k in zip(t, neighbors)) for t in TABLE[kind]]
        relations[j] = (variables, rows)
    return relations


def certify_printed(full):
    for j, (vs, ts) in full.items():
        pvs, pts = (s.split() for s in PRINTED[j])
        if j == 'n':
            assert vs == ['kn', 'mn', 'np']
            assert set(ts) == {'<+<', '<-<', '<<<', '<><'}
            assert pvs == ['kn', 'np'] and pts == ['<<']
        else:
            assert vs == pvs and set(ts) == set(pts), (j, vs, ts, pvs, pts)
    return {j: {'variables': v.split(), 'tuples': t.split()} for j, (v, t) in PRINTED.items()}


def propagate(relations, domains):
    domains = {v: set(d) for v, d in domains.items()}
    trace = []
    while True:
        changed = False
        for j, (vs, ts) in relations.items():
            surviving = [t for t in ts if all(s in domains[v] for s, v in zip(t, vs))]
            if not surviving:
                return None, trace + [{'constraint': j, 'contradiction': True}]
            for k, v in enumerate(vs):
                allowed = {t[k] for t in surviving}
                if allowed != domains[v]:
                    assert allowed < domains[v]
                    trace.append({'constraint': j, 'variable': v,
                                  'before': ''.join(s for s in ORDER if s in domains[v]),
                                  'after': ''.join(s for s in ORDER if s in allowed),
                                  'supporting_rows': surviving})
                    domains[v] = allowed
                    changed = True
        if not changed:
            return domains, trace


def search(relations, edges):
    nodes, solutions = [], []

    def visit(domains, parent=None, branch=None):
        assert len(nodes) < 100, 'This is a tiny certificate, not a large search.'
        d, changes = propagate(relations, domains)
        node = {'parent': parent, 'branch': branch, 'propagation': changes}
        index = len(nodes)
        nodes.append(node)
        if d is None:
            node['result'] = 'contradiction'
            return
        node['fixed_point'] = {v: ''.join(s for s in ORDER if s in d[v]) for v in edges}
        unsolved = [v for v in edges if len(d[v]) > 1]
        if not unsolved:
            solution = {v: next(iter(d[v])) for v in edges}
            assert all(''.join(solution[v] for v in vs) in ts for vs, ts in relations.values())
            node['result'] = 'solution'
            solutions.append(solution)
            return
        v = min(unsolved, key=lambda e: (len(d[e]), e))
        node['split_variable'] = v
        for s in ORDER:
            if s in d[v]:
                smaller = dict(d)
                smaller[v] = {s}
                visit(smaller, index, {v: s})

    visit({v: set(ORDER) for v in edges})
    return solutions, nodes


def dual_constraint(full, edge):
    a, b = edge
    av, at = full[a]
    bv, bt = full[b]
    return [str(i + 1) + str(j + 1)
            for i, x in enumerate(at) for j, y in enumerate(bt)
            if x[av.index(edge)] == y[bv.index(edge)]]


def existing_physical_labeling(edges):
    # Reuse already certified visible intervals/marks; no3D visibility rerun.
    net = json.loads((ROOT / 'results/network20.json').read_text())
    pic = json.loads((ROOT / 'results/histoscape-projection.json').read_text())
    lab = json.loads((ROOT / 'results/histoscape-labels.json').read_text())
    centers = {k: tuple(map(F, p)) for k, p in net['centers'].items()}
    affine = [tuple(map(F, row)) for row in net['model_to_network_affine']]
    js = [tuple(map(F, row['point'])) for row in pic['junctions']]
    images = [tuple(dot(row, (*p, F(1))) for row in affine) for p in js]
    named = {}
    for k, center in centers.items():
        i = min(range(len(js)), key=lambda i: dot(sub(center, images[i]), sub(center, images[i])))
        assert dot(sub(center, images[i]), sub(center, images[i])) < F(1, 1000)
        named[k] = js[i]
    assert len(set(named.values())) == 19
    projection = [tuple(map(F, row)) for row in pic['projection_rows']]
    vertices = [tuple(map(F, v)) for v in pic['model']['vertices']]
    points = [tuple(dot(row, (*v, F(1))) for row in projection) for v in vertices]
    visible = {tuple(r['edge']): [(F(s), F(t)) for s, t in r['intervals']] for r in pic['visibility']}
    labels = {tuple(r['edge']): r['label'] for r in lab['visible_edge_labels']}
    answer, correspondence = {}, []
    for edge in edges:
        u, v = [named[k] for k in edge]
        hits = []
        for (a, b), intervals in visible.items():
            pa, pb = points[a], points[b]
            if cross2(sub(u, pa), sub(pb, pa)) or cross2(sub(v, pa), sub(pb, pa)):
                continue
            x, y = parameter(u, pa, pb), parameter(v, pa, pb)
            if not any(s <= min(x, y) < max(x, y) <= t for s, t in intervals):
                continue
            label = labels[a, b]
            if label not in '+-':
                label = '>' if (y > x) == (label == 'a>b') else '<'
            hits.append(((a, b), label))
        assert len(hits) == 1, (edge, hits)
        answer[edge] = hits[0][1]
        correspondence.append({'line': edge, 'physical_edge': hits[0][0], 'label': hits[0][1]})
    return answer, correspondence


def main():
    full = full_relations()
    printed = certify_printed(full)
    relations = {j: (r['variables'], r['tuples']) for j, r in printed.items()}
    edges = sorted({v for vs, _ in relations.values() for v in vs})
    assert edges == json.loads((ROOT / 'results/network20.json').read_text())['edges']
    assert len(edges) == 26 and len(relations) == 19
    solutions, tree = search(relations, edges)
    assert len(solutions) == len({tuple(s[e] for e in edges) for s in solutions}) == 4
    dual = {e: dual_constraint(full, e) for e in ['ab', 'np', 'op']}
    assert set(dual['ab']) == {'41', '51', '33', '62'}
    assert set(dual['np']) == {'12', '13', '22', '23', '32', '33', '42', '43'}
    assert set(dual['op']) == {'13', '23', '36'}
    physical, correspondence = existing_physical_labeling(edges)
    assert physical in solutions
    ratio = F(1, 2) * F(3, 2) ** 5 * F(3, 8) ** 8 * F(5, 8) ** 5
    out = {'scope': 'All19 relations in(22), exact4-solution propagation certificate, physical104(d) identification, dual constraints43(a,b), and complete state-space ratio43(d).',
           'edges': edges, 'relations': printed, 'full_T_rows': full['n'],
           'solutions': solutions, 'propagation_tree': tree, 'dual_constraints': dual,
           'physical104d_solution': physical, 'physical_line_correspondence': correspondence,
           'state_space_ratio': ratio, 'state_space_ratio_decimal': float(ratio),
           'full_XCC_options': sum(len(ts) for _, ts in full.values()),
           'reduced_XCC_options': sum(len(ts) for _, ts in relations.values())}
    assert out['full_XCC_options'] == 83 and out['reduced_XCC_options'] == 80
    (ROOT / 'results/line-csp22.json').write_text(json.dumps(out, indent=2, default=encode) + '\n')
    print(json.dumps({'solutions': solutions, 'tree_nodes': len(tree),
                      'branch_nodes': [{k: n[k] for k in ('parent', 'branch', 'split_variable') if k in n} for n in tree if 'split_variable' in n],
                      'dual_constraints': dual, 'ratio': str(ratio),
                      'full_XCC_options': 83, 'reduced_XCC_options': 80}, indent=2))


if __name__ == '__main__':
    main()
