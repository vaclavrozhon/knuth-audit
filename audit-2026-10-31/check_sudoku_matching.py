#!/usr/bin/env python3
"""DLX49: every subset in every matching graph, checked against full permutations."""
from datetime import datetime, timezone
from itertools import combinations, permutations
import json
from check_sudoku_basics import OUT, DIGITS, UNITS
from dlx1_audit_tools import sha


def graph_check(label, edges, to_option):
    left = sorted(edges); right = sorted(set().union(*edges.values()))
    r = len(left); assert len(right) == r
    models = [list(zip(left, p)) for p in permutations(right)
              if all(v in edges[u] for u, v in zip(left, p))]
    assert models, label
    naked, hidden = [], []
    for q in range(1, r):
        for us in combinations(left, q):
            vs = set().union(*(edges[u] for u in us))
            assert len(vs) >= q
            if len(vs) == q:
                deleted = [(u, v) for u in left if u not in us for v in sorted(edges[u] & vs)]
                assert all(all(edge not in model for edge in deleted) for model in models)
                naked.append(dict(q=q, left=list(us), neighbors=sorted(vs),
                                  deleted=[to_option(u, v) for u, v in deleted]))
        for vs in combinations(right, q):
            us = {u for u in left if edges[u].intersection(vs)}
            assert len(us) >= q
            if len(us) == q:
                complement = set(left)-us
                neighbors = set().union(*(edges[u] for u in complement))
                assert neighbors == set(right)-set(vs)
                assert any(set(t['left']) == complement for t in naked) or r-q > q
                hidden.append(dict(q=q, right=list(vs), neighbors=sorted(us),
                                   complementary_naked=sorted(complement)))
    assert {tuple(t['complementary_naked']) for t in hidden} == {tuple(t['left']) for t in naked}
    return dict(label=label, vertices_per_part=r, edges={str(u): sorted(edges[u]) for u in left},
                perfect_matchings=len(models), naked=naked, hidden=hidden,
                deleted=sorted({s for t in naked for s in t['deleted']}))


def main():
    sources = json.loads((OUT/'pdf-grids.json').read_text())['sources']
    chart = [set(s) for s in sources['33']['cells']]
    basics = json.loads((OUT/'basics.json').read_text())
    completed = basics['solutions']['b'][0]
    fixed = [next(iter(s)) if len(s) == 1 else 0 for s in chart]
    results = []
    for kind, offset in [('row', 0), ('column', 9), ('box', 18)]:
        for index in range(9):
            unit = UNITS[offset+index]
            edges = {u: chart[v] for u, v in enumerate(unit) if not fixed[v]}
            results.append(graph_check(f'{kind}{index}', edges,
                           lambda u, k: f'{unit[u]//9}{unit[u]%9}{k}'))
    all_unit_naked = [(g['label'], t['left']) for g in results for t in g['naked']]
    assert all_unit_naked == [('row4', [3, 8]), ('row4', [1, 3, 8]), ('box4', [0, 3, 6])], all_unit_naked
    expected = {'row4': ['411','417','421','424','427','471'],
                'box4': ['341','346','347','351','356','357']}
    assert {g['label']: g['deleted'] for g in results if g['deleted']} == expected
    value_graphs = []
    for k in range(1, 10):
        edges = {i: {j for j in range(9) if k in chart[9*i+j] and not fixed[9*i+j]}
                 for i in range(9) if k not in fixed[9*i:9*i+9]}
        value_graphs.append(graph_check(f'value{k}', edges, lambda i,j:f'{i}{j}{k}'))
    pointing = []
    for k in (4, 8):
        cells = [v for v in UNITS[18+4] if k in chart[v]]
        assert {v//9 for v in cells} == {3}
        pointing += [f'{v//9}{v%9}{k}' for v in UNITS[3] if v not in UNITS[22] and k in chart[v]]
    assert sorted(pointing) == ['314','324','328','364','368','378']
    for g in results+value_graphs:
        for item in g['deleted']:
            i,j,k = map(int,item); assert completed[9*i+j] != k
    for item in pointing:
        i,j,k = map(int,item); assert completed[9*i+j] != k
    # Every corrected box formula maps its nine local cell indices bijectively.
    box_maps = [[9*(3*(x0//3)+j//3)+3*(x0%3)+j%3 for j in range(9)] for x0 in range(9)]
    assert box_maps == UNITS[18:]
    # Column j0=0, e.g. cell(2,0) with value2: left vertex must be u2, not u0.
    assert 2 in chart[9*2] and not fixed[9*2]
    result = dict(status='verified', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__), grids_sha256=sha(OUT/'pdf-grids.json'),
                  unit_graphs=results, value_graphs=value_graphs, pointing_eliminations=sorted(pointing),
                  corrected_box_indices=box_maps,
                  column_index_witness=dict(column=0, row=2, value=2, correct_edge='u2-v2', printed_edge='u0-v2'),
                  scope='Every proper naked/hidden tuple in27 unit graphs and9 value graphs; '
                        'all deletions independently excluded from every perfect matching and complete Sudoku solution.')
    (OUT/'matching.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(unit_tuples=all_unit_naked, value_tuples=[(g['label'], t) for g in value_graphs for t in g['naked']],
                          unit_matchings=sum(g['perfect_matchings'] for g in results),
                          value_matchings=sum(g['perfect_matchings'] for g in value_graphs)), indent=2))


if __name__ == '__main__':
    main()
