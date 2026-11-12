#!/usr/bin/env python3
"""Native exercise49, its four level chains, all29 printed top strings."""
from fractions import Fraction as F
from collections import Counter
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT
from check_cubie_junctions import path_points
from check_polyhedra_fixed import encode
from check_hc_drawings26_27 import network
from check_hc_free_boundaries import boundary_certificate
from check_line_csp22 import ORDER, TABLE, global_symbol, propagate


PRINTED_TOP = [
    '->+<->>-', '->+<->>>', '->+<<+>-', '->+<<+>>', '->+<<<->',
    '->>-<+>-', '->>-<+>>', '->>-<<->', '->>>+<->', '->>>>>>-', '->>>>>>>',
    '>-<+>>>-', '>-<+>>>>', '>-<<->>-', '>-<<->>>', '>-<<<+>-', '>-<<<+>>',
    '>-<<<<->', '>>+<->>-', '>>+<->>>', '>>+<<+>-', '>>+<<+>>', '>>+<<<->',
    '>>>-<+>-', '>>>-<+>>', '>>>-<<->', '>>>>+<->', '>>>>>>>-', '>>>>>>>>',
]


def directed_value(solution, a, b):
    s = solution['_'.join(sorted((a, b)))]
    return s if a < b or s in '+-' else ('<' if s == '>' else '>')


def certify_side_chains(data):
    boundary = data['boundary']
    top, bottom = data['top_chain'], data['levels'][0]['junction_chain']

    def backward(start, end):
        result = [start]
        k = boundary.index(start)
        while result[-1] != end:
            k = (k - 1) % len(boundary)
            result.append(boundary[k])
            assert len(result) <= len(boundary)
        assert len(result) == 9
        return result

    left, right = backward(top[1], bottom[0]), backward(bottom[-1], top[-2])
    assert left[:2] == [top[1], top[0]] and right[-2:] == [top[-1], top[-2]]
    output = []
    for side, chain in [('left', left), ('right', right)]:
        assert data['junctions'][chain[0]]['type'] == data['junctions'][chain[-1]]['type'] == 'V'
        for i in range(1, 8):
            j = chain[i]
            n = data['junctions'][j]
            kind = 'W' if i % 2 else 'Y'
            assert n['type'] == kind
            before, after = chain[i - 1], chain[i + 1]
            inner = next(k for k in n['neighbors'] if k not in (before, after))
            expected = [before, inner, after]
            assert (list(n['neighbors']) == expected if kind == 'W'
                    else any(list(n['neighbors']) == expected[k:] + expected[:k] for k in range(3)))
        assert ''.join(directed_value(data['standard_labeling'], a, b) for a, b in zip(chain, chain[1:])) == '<' * 8
        valid = []
        for side_value in '+-<':
            for bottom_value in '+-<':
                values = {}

                def put(a, b, s):
                    values['_'.join(sorted((a, b)))] = s if a < b or s in '+-' else ('>' if s == '<' else '<')

                if side == 'left':
                    corner = bottom[0]
                    put(chain[-2], chain[-1], side_value)
                    put(bottom[0], bottom[1], bottom_value)
                else:
                    corner = bottom[-1]
                    put(chain[0], chain[1], side_value)
                    put(bottom[-2], bottom[-1], bottom_value)
                vs, ts = data['relations'][corner]
                assert set(vs) == set(values)
                if ''.join(values[v] for v in vs) in ts:
                    valid.append(side_value + bottom_value)
        assert set(valid) == {'-<', '<-', '<<'}
        output.append({'side': side, 'junction_chain_in_printed_direction': chain,
                       'uniform_values_before_corner_test': '+-<',
                       'allowed_side_bottom_pairs': valid})
    data['side_chain_certificates'] = output
    remaining = set(data['junctions']) - set(boundary)
    components = []
    while remaining:
        todo, part = [min(remaining)], []
        while todo:
            j = todo.pop()
            if j not in remaining:
                continue
            remaining.remove(j)
            part.append(j)
            todo.extend(data['junctions'][j]['neighbors'])
        components.append(sorted(part))
    assert sorted(map(len, components)) == [9, 18, 18, 18]
    data['components_after_covering_boundary_junctions'] = components
    return data


def main():
    paths = [p.attrib for p in ET.parse(ROOT / 'sources/file-133.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    original = {i: path_points(paths[i]) for i in range(18, 77)}
    allpoints = [p for qs in original.values() for p in qs]
    origin = tuple(min(p[k] for p in allpoints) for k in (0, 1))
    units = tuple((max(p[k] for p in allpoints) - origin[k]) / n for k, n in enumerate((96, 302)))
    mapped, errors = {}, []
    for i, qs in original.items():
        mapped[i] = []
        for p in qs:
            q = tuple(F(round((p[k] - origin[k]) / units[k])) for k in (0, 1))
            mapped[i].append(q)
            errors.append(sum((p[k] - origin[k] - units[k] * q[k]) ** 2 for k in (0, 1)))
    assert max(errors) < F(1, 10000)
    points, ns, rs, lines, faces, boundary = network(mapped, paths)
    names = {p: j for j, p in points.items()}
    boundary_lines = [{'from': a, 'to': b, 'variable': '_'.join(sorted((a, b))), 'label': '>' if a < b else '<'}
                      for a, b in zip(boundary, boundary[1:] + boundary[:1])]
    pic = {'name': 'exercise49', 'relations': {j: {'variables': vs, 'tuples': ts} for j, (vs, ts) in rs.items()},
           'boundary': boundary, 'boundary_lines': boundary_lines}
    bc = boundary_certificate(pic)
    assert bc['boundary_labeling_count'] == 40
    domains = {e: set(ORDER) for e in lines}
    for b in boundary_lines:
        domains[b['variable']] = {b['label']}
    fixed, trace = propagate(rs, domains)
    assert fixed is not None and all(len(d) == 1 for d in fixed.values())
    witness = {e: next(iter(d)) for e, d in fixed.items()}
    assert all(''.join(witness[e] for e in es) in ts for es, ts in rs.values())
    levels = []
    for index, start in enumerate((19, 32, 45, 58)):
        path_order = [start + k for k in (0, 1, 2, 4, 5, 7, 8, 10, 11, 3)]
        chain = []
        for i in path_order:
            u, v = [names[p] for p in mapped[i][:2]]
            if chain:
                assert chain[-1] == u
            else:
                chain.append(u)
            chain.append(v)
        for i in range(1, 10):
            j = chain[i]
            kind = 'W' if i % 2 else 'Y'
            assert ns[j]['type'] == kind
            previous, following = chain[i - 1], chain[i + 1]
            inner = next(k for k in ns[j]['neighbors'] if k not in (previous, following))
            expected = [previous, inner, following]
            assert (list(ns[j]['neighbors']) == expected if kind == 'W'
                    else any(list(ns[j]['neighbors']) == expected[k:] + expected[:k] for k in range(3)))
        word = ''.join(directed_value(witness, a, b) for a, b in zip(chain, chain[1:]))
        assert word == ('<' if index == 0 else '-') * 10
        levels.append({'level_from_bottom': index, 'native_lower_edge_paths': path_order,
                       'junction_chain': chain, 'standard_labels_left_to_right': word})
    top = [names[p] for p in mapped[18]]
    assert len(top) == 9
    local_pairs = []
    for i in range(1, 8):
        j = top[i]
        expected = [top[i + 1], top[i - 1]] if i % 2 else [top[i - 1], top[i + 1]]
        assert ns[j]['type'] == 'V' and list(ns[j]['neighbors']) == expected
        pairs = set()
        for row in TABLE['V']:
            d = {k: s for k, s in zip(expected, row)}
            incoming = '+' if d[top[i - 1]] == '+' else '-' if d[top[i - 1]] == '-' else '<' if d[top[i - 1]] == 'O' else '>'
            outgoing = '+' if d[top[i + 1]] == '+' else '-' if d[top[i + 1]] == '-' else '>' if d[top[i + 1]] == 'O' else '<'
            pairs.add((incoming, outgoing))
        local_pairs.append(sorted(pairs))
    prefixes = ['-', '>']
    prefix_counts = [len(prefixes)]
    for pairs in local_pairs:
        prefixes = [s + t for s in prefixes for t in ORDER if (s[-1], t) in pairs]
        prefix_counts.append(len(prefixes))
    words = sorted(s for s in prefixes if s[-1] in '->')
    assert len(PRINTED_TOP) == len(set(PRINTED_TOP)) == 29
    assert all(len(s) == 8 for s in PRINTED_TOP)
    assert set(PRINTED_TOP) == set(words)
    groups = Counter(s[0] + s[-1] for s in words)
    assert groups == {'--': 4, '->': 7, '>-': 7, '>>': 11}
    out = {'scope': 'Every native path of49, all local relations, all four ten-edge level chains, each of29 printed top strings, unique standard labeling and exact boundary Cartesian factor40.',
           'source_origin': origin, 'source_units': units, 'maximum_source_residual_squared': max(errors),
           'source_path_grid_vertices': mapped, 'points': points, 'junctions': ns, 'relations': rs,
           'lines': lines, 'faces': faces, 'boundary': boundary, 'boundary_lines': boundary_lines,
           'boundary_certificate': bc, 'standard_labeling': witness, 'standard_propagation': trace,
           'levels': levels, 'top_chain': top, 'top_local_pairs': local_pairs,
           'top_prefix_counts': prefix_counts, 'printed_top_strings': PRINTED_TOP,
           'derived_top_strings': words, 'top_endpoint_counts': dict(groups),
           'boundary_sum': [4, 7, 7, 11, 11], 'total_labelings': 40}
    certify_side_chains(out)
    (ROOT / 'results/hc-staircase49.json').write_text(json.dumps(out, indent=2, default=encode) + '\n')
    print(json.dumps({'junction_types': dict(Counter(j['type'] for j in ns.values())),
                      'lines': len(lines), 'boundary_length': len(boundary),
                      'standard_count': 1, 'boundary_and_total_count': 40,
                      'top_endpoint_counts': dict(groups), 'top_prefix_counts': prefix_counts}, indent=2))


if __name__ == '__main__':
    main()
