#!/usr/bin/env python3
"""Tiny complete standard-labeling certificate for the saved Szilassi picture."""
from fractions import Fraction as F
import json
from check_line_csp22 import ROOT, ORDER, propagate


def main():
    saved = json.loads((ROOT / 'results/hc-picture-networks.json').read_text())
    picture = next(p for p in saved['pictures'] if p['name'] == 'szilassi')
    rs = {j: (r['variables'], r['tuples']) for j, r in picture['relations'].items()}
    edges = sorted(picture['physical_labeling'])
    domains = {e: set(ORDER) for e in edges}
    for b in picture['boundary_lines']:
        domains[b['variable']] = {b['label']}
    tree, solutions = [], []

    def visit(ds, parent=None, branch=None):
        assert len(tree) < 30
        new, trace = propagate(rs, ds)
        node = {'parent': parent, 'branch': branch, 'propagation': trace}
        k = len(tree)
        tree.append(node)
        if new is None:
            node['result'] = 'contradiction'
            return
        node['fixed_point'] = {e: ''.join(v for v in ORDER if v in new[e]) for e in edges}
        uncertain = [e for e in edges if len(new[e]) > 1]
        if not uncertain:
            x = {e: next(iter(new[e])) for e in edges}
            assert all(''.join(x[e] for e in es) in ts for es, ts in rs.values())
            solutions.append(x)
            node['result'] = 'solution'
            return
        e = min(uncertain, key=lambda e: (len(new[e]), e))
        node['split_variable'] = e
        for value in ORDER:
            if value in new[e]:
                smaller = dict(new)
                smaller[e] = {value}
                visit(smaller, k, {e: value})

    visit(domains)
    assert len(solutions) == 2 and picture['physical_labeling'] in solutions
    changes = []
    for j, r in picture['relations'].items():
        if picture['network'][j]['type'] != 'Y':
            continue
        y = dict(picture['printed_labeling_completion'])
        for e in r['variables']:
            y[e] = '-'
        bad = [k for k, (es, ts) in rs.items() if ''.join(y[e] for e in es) not in ts]
        changed_boundary = [b['variable'] for b in picture['boundary_lines'] if y[b['variable']] != b['label']]
        changes.append({'junction': j, 'point': picture['points'][j],
                        'local_before': ''.join(picture['printed_labeling_completion'][e] for e in r['variables']),
                        'local_after': '---', 'invalid_junctions': bad,
                        'changed_boundary_lines': changed_boundary,
                        'is_other_standard_solution': y in solutions and y != picture['physical_labeling']})
    assert sum(c['is_other_standard_solution'] for c in changes) == 1
    good = next(c for c in changes if c['is_other_standard_solution'])
    low = max(changes, key=lambda c: F(c['point'][1]))
    out = {'scope': 'Complete standard count and each possible interpretation of changing one Y to---; original coordinates retained for the word lower.',
           'solutions': solutions, 'tree': tree, 'Y_changes': changes,
           'valid_changed_Y': good['junction'], 'lower_on_page_Y': low['junction']}
    (ROOT / 'results/szilassi-standard-labelings.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'tree_nodes': len(tree), 'Y_changes': changes,
                      'valid_changed_Y': good['junction'], 'lower_on_page_Y': low['junction']}, indent=2))


if __name__ == '__main__':
    main()
