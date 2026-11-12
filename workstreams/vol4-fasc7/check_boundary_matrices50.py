#!/usr/bin/env python3
"""All96 matrix entries in50(b), its full example, and fixed chord cases."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json
from check_clasp_projection import ROOT
from check_line_csp22 import TABLE, ORDER, propagate
from check_hc_drawings26_27 import network
from check_polyhedra_fixed import encode


STATES = '><-+'
CASE = {'L': ('T', ['next', 'prev', 'inner']),
        'R': ('T', ['inner', 'next', 'prev']),
        'V': ('V', ['next', 'prev']),
        'A': ('V', ['prev', 'next']),
        'W': ('W', ['next', 'inner', 'prev']),
        'Y': ('Y', ['next', 'inner', 'prev'])}
PRINTED = {
    'L': ['l000', 'l000', 'l000', 'l000'],
    'R': ['gggg', '0000', '0000', '0000'],
    'V': ['1010', '0101', '1000', '0100'],
    'A': ['1001', '0110', '0100', '1000'],
    'W': ['p000', '0000', '00p0', '000m'],
    'Y': ['m000', '00l0', '0gm0', '000p'],
}


def matrices():
    result = {}
    for case, (kind, order) in CASE.items():
        matrix = [['0'] * 4 for _ in range(4)]
        for row in TABLE[kind]:
            values = dict(zip(order, row))
            a = values['prev']
            b = values['next']
            a = '<' if a == 'O' else '>' if a == 'I' else a
            b = '>' if b == 'O' else '<' if b == 'I' else b
            symbol = {'O': 'g', 'I': 'l', '-': 'm', '+': 'p'}[values['inner']] if 'inner' in values else '1'
            i, j = STATES.index(a), STATES.index(b)
            assert matrix[i][j] == '0'
            matrix[i][j] = symbol
        assert [''.join(row) for row in matrix] == PRINTED[case], (case, matrix)
        result[case] = [[{} if s == '0' else {'' if s == '1' else s: 1} for s in row] for row in matrix]
    return result


def multiply(a, b):
    out = [[defaultdict(int) for _ in range(4)] for _ in range(4)]
    for i, j, k in product(range(4), repeat=3):
        for u, count_u in a[i][k].items():
            for v, count_v in b[k][j].items():
                out[i][j][u + v] += count_u * count_v
    return [[dict(x) for x in row] for row in out]


def word_product(word, ms):
    answer = [[{'': 1} if i == j else {} for j in range(4)] for i in range(4)]
    for c in word:
        answer = multiply(answer, ms[c])
    return answer


def trace(p):
    out = defaultdict(int)
    for i in range(4):
        for w, c in p[i][i].items():
            out[w] += c
    return dict(out)


def fixed_case(name, chords, ms):
    polygon = [(0, 0), (0, -1), (2, -1), (2, 0), (1, 0), (1, 1), (-1, 1), (-1, 0)]
    segments = [(polygon[i], polygon[(i + 1) % 8]) for i in range(8)] + [(polygon[i], polygon[j]) for i, j in chords]
    paths = {i: {'d': 'M %s %s L %s %s' % (*a, *b)} for i, (a, b) in enumerate(segments)}
    mapped = {i: [tuple(map(F, a)), tuple(map(F, b))] for i, (a, b) in enumerate(segments)}
    points, ns, rs, lines, faces, boundary = network(mapped, paths)
    names = {p: j for j, p in points.items()}
    start = boundary.index(names[polygon[0]])
    boundary = boundary[start:] + boundary[:start]
    assert [points[j] for j in boundary] == polygon
    cases, ports = [], []
    for i, j in enumerate(boundary):
        previous, following = boundary[i - 1], boundary[(i + 1) % len(boundary)]
        inner = [k for k in ns[j]['neighbors'] if k not in (previous, following)]
        which = {'prev': previous, 'next': following}
        if inner:
            assert len(inner) == 1
            which['inner'] = inner[0]
        hits = []
        for case, (kind, order) in CASE.items():
            if kind != ns[j]['type'] or set(order) != set(which):
                continue
            wanted = [which[k] for k in order]
            actual = list(ns[j]['neighbors'])
            if actual == wanted or (kind == 'Y' and any(actual == wanted[k:] + wanted[:k] for k in range(3))):
                hits.append(case)
        assert len(hits) == 1
        cases.append(hits[0])
        if inner:
            ports.append({'junction': j, 'neighbor': inner[0], 'variable': '_'.join(sorted((j, inner[0])))})
    polynomial = trace(word_product(cases, ms))
    consistent_words = {}
    actual_port_values = defaultdict(set)
    for word, coefficient in polynomial.items():
        assert len(word) == len(ports)
        values, consistent = {}, True
        for s, p in zip(word, ports):
            value = {'g': '>', 'l': '<', 'p': '+', 'm': '-'}[s]
            if p['junction'] > p['neighbor'] and value in '<>':
                value = '>' if value == '<' else '<'
            if p['variable'] in values and values[p['variable']] != value:
                consistent = False
            values[p['variable']] = value
        if consistent:
            consistent_words[word] = coefficient
            for v, value in values.items():
                actual_port_values[v].add(value)
    # All junctions of these fixed examples are on the boundary. Matching
    # the two occurrences of each chord is therefore the only omitted
    # condition; the filtered cycle language is an exact full count.
    assert set(boundary) == set(points)
    standard = {e: set(ORDER) for e in lines}
    for u, v in zip(boundary, boundary[1:] + boundary[:1]):
        standard['_'.join(sorted((u, v)))] = {'>' if u < v else '<'}
    fixed, proof = propagate(rs, standard)
    return {'name': name, 'polygon': polygon, 'chords_by_polygon_index': chords,
            'points': points, 'junctions': ns, 'relations': rs, 'lines': lines,
            'faces': faces, 'boundary': boundary, 'boundary_case_word': ''.join(cases),
            'ordered_inner_occurrences': ports, 'unfiltered_trace': polynomial,
            'consistent_trace': consistent_words, 'actual_inner_value_sets': {e: ''.join(s for s in ORDER if s in v) for e, v in actual_port_values.items()},
            'full_boundary_labeling_count': sum(consistent_words.values()),
            'standard_domains': None if fixed is None else {e: ''.join(s for s in ORDER if s in ds) for e, ds in fixed.items()},
            'standard_propagation': proof}


def main():
    ms = matrices()
    hist = word_product('VWYWVWVWYW', ms)
    expected = [[{} for _ in range(4)] for _ in range(4)]
    for i, j, count in [(0, 0, 3), (0, 2, 2), (2, 0, 2), (2, 2, 1)]:
        expected[i][j] = {'pmpppmp': count}
    assert hist == expected
    witnesses = [fixed_case(name, chords, ms) for name, chords in [
        ('two_T_chord', [(0, 4)]),
        ('two_T_and_ear_chords', [(0, 4), (1, 3)]),
        ('one_ear_chord', [(1, 3)])]]
    out = {'matrices_derived_and_all_printed_entries_checked': PRINTED,
           'histoscape_full_product': hist, 'histoscape_trace': trace(hist),
           'fixed_chord_examples': witnesses}
    (ROOT / 'results/boundary-matrices50.json').write_text(json.dumps(out, indent=2, default=encode) + '\n')
    print(json.dumps([{'name': w['name'], 'case_word': w['boundary_case_word'],
                      'trace': w['unfiltered_trace'], 'consistent_trace': w['consistent_trace'],
                      'inner_values': w['actual_inner_value_sets'], 'count': w['full_boundary_labeling_count']} for w in witnesses], indent=2))


if __name__ == '__main__':
    main()
