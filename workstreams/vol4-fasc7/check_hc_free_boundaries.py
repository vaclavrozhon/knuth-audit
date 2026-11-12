#!/usr/bin/env python3
"""Four finite cycle certificates and two tiny interior labeling proofs.

Reuse the previously proved Szilassi and histoscape counts. No all-labeling
enumeration: boundary choices are counted by four-state matrix products.
"""
import json
from math import prod
from check_line_csp22 import ROOT, ORDER, propagate


def identity():
    return [[int(a == b) for b in range(4)] for a in range(4)]


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def edge(a, b):
    return '_'.join(sorted((a, b)))


def boundary_certificate(pic):
    boundary = pic['boundary']
    assert len(boundary) == len(set(boundary))
    boundary_edges = {edge(a, b) for a, b in zip(boundary, boundary[1:] + boundary[:1])}
    matrices, local = [], []
    for i, j in enumerate(boundary):
        before, after = edge(boundary[i - 1], j), edge(j, boundary[(i + 1) % len(boundary)])
        r = pic['relations'][j]
        a, b = r['variables'].index(before), r['variables'].index(after)
        other = [v for v in r['variables'] if v not in (before, after)]
        assert len(other) <= 1 and not (set(other) & boundary_edges)
        matrix = [[0] * 4 for _ in range(4)]
        for t in r['tuples']:
            matrix[ORDER.index(t[a])][ORDER.index(t[b])] = 1
        matrices.append(matrix)
        local.append({'junction': j, 'incoming_variable': before,
                      'outgoing_variable': after, 'interior_variables': other,
                      'incoming_index': a, 'outgoing_index': b})
    prefixes = [identity()]
    for m in matrices:
        prefixes.append(multiply(prefixes[-1], m))
    count = sum(prefixes[-1][i][i] for i in range(4))
    ports = {}
    for i, data in enumerate(local):
        # Product of the other junction matrices, starting after this one.
        rest = identity()
        for k in list(range(i + 1, len(local))) + list(range(i)):
            rest = multiply(rest, matrices[k])
        pairs = [(a, b) for a in range(4) for b in range(4)
                 if matrices[i][a][b] and rest[b][a]]
        r = pic['relations'][data['junction']]
        surviving = [t for t in r['tuples']
                     if (ORDER.index(t[data['incoming_index']]),
                         ORDER.index(t[data['outgoing_index']])) in pairs]
        assert surviving
        data['globally_supported_boundary_pairs'] = [ORDER[a] + ORDER[b] for a, b in pairs]
        data['globally_supported_full_rows'] = surviving
        for v in data['interior_variables']:
            values = {t[r['variables'].index(v)] for t in surviving}
            assert len(values) == 1, (pic['name'], data['junction'], v, values)
            value = next(iter(values))
            assert v not in ports or ports[v] == value
            ports[v] = value
    # Thus every cycle labeling extends uniquely at every boundary junction,
    # to exactly the same interior-port vector. All remaining constraints are
    # wholly on the interior variable set, giving a Cartesian product.
    standard = {b['variable']: b['label'] for b in pic['boundary_lines']}
    for j in boundary:
        r = pic['relations'][j]
        row = ''.join((standard if v in boundary_edges else ports)[v] for v in r['variables'])
        assert row in r['tuples']
    return {'boundary': boundary, 'boundary_variables': sorted(boundary_edges),
            'matrices': matrices, 'prefix_products': prefixes,
            'local_certificates': local, 'fixed_interior_ports': ports,
            'boundary_labeling_count': count, 'standard_boundary_is_allowed': True}


def tiny_interior_count(pic, bc):
    outer = set(bc['boundary'])
    rs = {j: (r['variables'], r['tuples']) for j, r in pic['relations'].items() if j not in outer}
    variables = sorted({v for r in pic['relations'].values() for v in r['variables']} - set(bc['boundary_variables']))
    domains = {v: {bc['fixed_interior_ports'][v]} if v in bc['fixed_interior_ports'] else set(ORDER) for v in variables}
    nodes, leaves = [], []

    def visit(ds, parent=None, branch=None, inherited_free=None):
        assert len(nodes) < 100, 'The certified interior is tiny; stop rather than launch a census.'
        d, trace = propagate(rs, ds)
        node = {'parent': parent, 'branch': branch, 'propagation': trace}
        index = len(nodes)
        nodes.append(node)
        if d is None:
            node['count'] = 0
            return 0
        node['fixed_point'] = {v: ''.join(s for s in ORDER if s in d[v]) for v in variables}
        active = set()
        for vs, ts in rs.values():
            rows = [t for t in ts if all(t[k] in d[v] for k, v in enumerate(vs))]
            assert len(rows) == len(set(rows))
            if len(rows) != prod(len(d[v]) for v in vs):
                active.update(vs)
        free = {v: ''.join(s for s in ORDER if s in d[v]) for v in variables if len(d[v]) > 1 and v not in active}
        factor = prod(len(values) for values in free.values())
        node['independent_free_variables'] = free
        node['free_factor'] = factor
        all_free = {**(inherited_free or {}), **free}
        for v, values in free.items():
            d[v] = {values[0]}
        uncertain = [v for v in variables if len(d[v]) > 1]
        if not uncertain:
            witness = {v: next(iter(d[v])) for v in variables}
            assert all(''.join(witness[v] for v in vs) in ts for vs, ts in rs.values())
            leaves.append({'representative': witness, 'free_domains': all_free})
            node['count'] = factor
            return factor
        v = min(uncertain, key=lambda v: (len(d[v]), v))
        node['split_variable'] = v
        subtotal = 0
        for s in ORDER:
            if s in d[v]:
                child = dict(d)
                child[v] = {s}
                subtotal += visit(child, index, {v: s}, all_free)
        node['count'] = factor * subtotal
        return node['count']

    count = visit(domains)
    return {'interior_variables': variables, 'constraints': rs,
            'tree': nodes, 'compressed_solutions': leaves, 'count': count}


def main():
    other = json.loads((ROOT / 'results/hc-picture-networks.json').read_text())['pictures']
    sphinx = json.loads((ROOT / 'results/sphinx-native-network.json').read_text())
    sphinx['name'] = 'sphinx'
    pictures = [sphinx] + [next(p for p in other if p['name'] == name) for name in ('szilassi', 'clasp', 'histoscape')]
    expected = {'sphinx': (720, 2), 'szilassi': (3, 2), 'clasp': (6, 256), 'histoscape': (4, 1)}
    out = []
    for pic in pictures:
        bc = boundary_certificate(pic)
        wanted_boundary, wanted_interior = expected[pic['name']]
        assert bc['boundary_labeling_count'] == wanted_boundary
        item = {'name': pic['name'], 'boundary_certificate': bc}
        if pic['name'] in ('sphinx', 'clasp'):
            interior = tiny_interior_count(pic, bc)
            assert interior['count'] == wanted_interior, (pic['name'], interior['count'])
            item['interior_certificate'] = interior
            if pic['name'] == 'sphinx':
                printed = pic['printed_labeling_completion']
                changes = [[v for v, value in x['representative'].items() if value != printed[v]] for x in interior['compressed_solutions']]
                assert sorted(map(len, changes)) == [0, 2]
                item['changes_from_printed_labeling'] = changes
        else:
            item['closed_count_reused'] = {
                'count': wanted_interior,
                'evidence': ('results/szilassi-standard-labelings.json' if pic['name'] == 'szilassi'
                             else 'notes/line-csp-and-exercises-042-044.md'),
                'reason': 'The standard boundary is allowed and the just-proved product decomposition makes its interior solution set identical to the unrestricted one.'}
        item['standard_count'] = wanted_interior
        item['total_count'] = wanted_boundary * wanted_interior
        out.append(item)
    (ROOT / 'results/hc-free-boundaries.json').write_text(json.dumps({'pictures': out}, indent=2) + '\n')
    print(json.dumps([{'picture': x['name'], 'boundary': x['boundary_certificate']['boundary_labeling_count'],
                      'standard': x['standard_count'], 'total': x['total_count'],
                      'interior_tree_nodes': len(x.get('interior_certificate', {}).get('tree', []))} for x in out], indent=2))


if __name__ == '__main__':
    main()
