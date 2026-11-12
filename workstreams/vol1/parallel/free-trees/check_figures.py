"""Exact independent checks of scanned figures and their printed equations.

The generic fundamental-cycle routine uses only edge endpoints and the chosen
tree. Its output is compared with the separately transcribed printed cycles.
No successful Prim answer-12 test is repeated here.
"""
from collections import defaultdict, deque
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent


def vertices(edges):
    return set(x for pair in edges.values() for x in pair)


def cycle(edges, tree, chord):
    adj = defaultdict(list)
    for e in tree:
        u, v = edges[e]
        adj[u].append((v, e, 1))
        adj[v].append((u, e, -1))
    u, v = edges[chord]
    q = deque([(v, {})])
    seen = {v}
    while q:
        x, path = q.popleft()
        if x == u:
            return {chord: 1, **path}
        for y, e, sign in adj[x]:
            if y not in seen:
                seen.add(y)
                q.append((y, {**path, e: sign}))
    raise AssertionError("Tree does not span the chord endpoints")


def terms(positive, negative=()):
    return {**{str(e): 1 for e in positive}, **{str(e): -1 for e in negative}}


def check_basis(edges, expected):
    tree = set(edges) - set(expected)
    assert len(tree) == len(vertices(edges)) - 1
    actual = {}
    for e, c in expected.items():
        actual[e] = cycle(edges, tree, e)
        assert actual[e] == c, (e, actual[e], c)
        div = defaultdict(int)
        for f, x in c.items():
            u, v = edges[f]
            div[u] -= x
            div[v] += x
        assert all(x == 0 for x in div.values())
    # Every tree edge is reached by a search in the whole chosen tree.
    adj = defaultdict(set)
    for e in tree:
        u, v = edges[e]
        adj[u].add(v)
        adj[v].add(u)
    seen, todo = set(), [next(iter(vertices(edges)))]
    while todo:
        v = todo.pop()
        if v not in seen:
            seen.add(v)
            todo.extend(adj[v] - seen)
    assert seen == vertices(edges)
    return actual


raw = {
    '1': ('Start', 'A'), '2': ('A', 'C'), '3': ('A', 'B'),
    '4': ('B', 'C'), '5': ('C', 'Cp'), '6': ('C', 'D'),
    '7': ('D', 'Cp'), '8': ('Cp', 'A'), '9': ('Cp', 'ONE'),
    '10': ('ONE', 'E'), '11': ('E', 'F'), '12': ('F', 'G'),
    '13': ('G', 'F'), '14': ('G', 'Stop'), '15': ('F', 'H'),
    '16': ('H', 'J'), '17': ('J', 'L'), '18': ('K', 'L'),
    '19': ('L', 'K'), '20': ('Q', 'K'), '21': ('K', 'J'),
    '22': ('L', 'P'), '23': ('P', 'Q'), '24': ('P', 'R'),
    '25': ('R', 'S'), '26': ('S', 'E'), '27': ('R', 'E'),
}
edges = {**raw, '0': ('Stop', 'Start')}
for e in ('13', '19'):
    u, v = edges.pop(e)
    edges[e+'p'] = (u, 'X'+e)
    edges[e+'d'] = ('X'+e, v)
printed = {
    '0': terms([0, 1, 3, 4, 6, 7, 9, 10, 11, 12, 14]),
    '2': terms([2], [4, 3]), '5': terms([5], [7, 6]),
    '8': terms([8, 3, 4, 6, 7]),
    '13d': terms(['13d', 12, '13p']),
    '17': terms([17, 22, 24, 27, 11, 15, 16]),
    '19d': terms(['19d', 18, '19p']),
    '20': terms([20, 18, 22, 23]),
    '21': terms([21], [16, 15, 11, 27, 24, 22, 18]),
    '25': terms([25, 26], [27]),
}
basis = check_basis(edges, printed)
eq6 = {
    '1': terms([0]), '3': terms([0, 8], [2]),
    '4': terms([0, 8], [2]), '6': terms([0, 8], [5]),
    '7': terms([0, 8], [5]), '9': terms([0]), '10': terms([0]),
    '11': terms([0, 17], [21]), '12': terms([0, '13d']),
    '13p': terms(['13d']), '14': terms([0]),
    '15': terms([17], [21]), '16': terms([17], [21]),
    '18': terms(['19d', 20], [21]), '19p': terms(['19d']),
    '22': terms([17, 20], [21]), '23': terms([20]),
    '24': terms([17], [21]), '26': terms([25]),
    '27': terms([17], [21, 25]),
}
for e, rhs in eq6.items():
    assert {c: co[e] for c, co in basis.items() if e in co} == rhs
assert set(eq6) == set(edges) - set(basis)

node_expected = {
    'A': terms([0, 8]), 'B': terms([0, 8], [2]),
    'C': terms([0, 8]), 'D': terms([0, 8], [5]),
    'E': terms([0, 17], [21]), 'F': terms([0, '13d', 17], [21]),
    'G': terms([0, '13d']), 'H': terms([17], [21]),
    'J': terms([17]), 'K': terms(['19d', 20]),
    'L': terms([17, '19d', 20], [21]),
    'P': terms([17, 20], [21]), 'Q': terms([20]),
    'R': terms([17], [21]), 'S': terms([25]),
}
for v, rhs in node_expected.items():
    actual = {c: sum(co.get(e, 0) for e, (_, w) in edges.items() if w == v)
              for c, co in basis.items()}
    assert {c: x for c, x in actual.items() if x} == rhs, (v, actual, rhs)

ex7 = {
    '0': ('Stop', 'Start'), '1': ('Start', 'A'), '2': ('A', 'B'),
    '3': ('C', 'A'), '4': ('A', 'D'), '5': ('B', 'C'),
    '6': ('D', 'B'), '7': ('C', 'D'), '8': ('C', 'Stop'),
    '9': ('D', 'Stop'),
}
basis7 = check_basis(ex7, {
    '0': terms([0, 1, 4, 9]), '5': terms([5, 3, 2]),
    '6': terms([6, 4], [2]), '7': terms([7], [4, 3]),
    '8': terms([8], [9, 4, 3]),
})
for e, rhs in {
    '1': terms([0]), '2': terms([5], [6]), '3': terms([5], [7, 8]),
    '4': terms([0, 6], [7, 8]), '9': terms([0], [8]),
}.items():
    assert {c: co[e] for c, co in basis7.items() if e in co} == rhs

# Figure 29: enumerate simple B-based cycles, using endpoints only.
fig29 = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('B', 'E'), ('D', 'E')]
adj = defaultdict(set)
for u, v in fig29:
    adj[u].add(v)
    adj[v].add(u)
cycles = []
def visit(path):
    for v in sorted(adj[path[-1]]):
        if v == 'B' and len(path) >= 3:
            cycles.append(''.join(path + ['B']))
        elif v not in path:
            visit(path + [v])
visit(['B'])
assert cycles == ['BACDB', 'BACDEB', 'BDCAB', 'BDEB', 'BEDB', 'BEDCAB']

fig30 = dict(enumerate([tuple(s) for s in
    ('AC', 'BC', 'CD', 'CG', 'FG', 'EF', 'GH', 'HI', 'HM', 'FK', 'JK', 'KL', 'KN')]))
assert len(vertices(fig30)) == 14 and len(fig30) == 13
check_basis({**fig30, 'test': ('A', 'N')}, {'test': cycle(fig30 | {'test': ('A', 'N')}, set(fig30), 'test')})

# Figure 33: use squared integer distances to check each stated cheapest cut edge.
xy = {1:(1,5), 2:(3,5), 3:(0,4), 4:(5,4), 5:(2,3),
      6:(3,3), 7:(0,2), 8:(4,1), 9:(3,0)}
def distance2(a, b):
    return sum((x-y)**2 for x,y in zip(xy[a], xy[b]))
order = [(8,9), (6,8), (5,6), (2,6), (1,2), (3,1), (7,3), (4,2)]
chosen, lengths = {9}, []
for a,b in order:
    cut = [(distance2(x,y),x,y) for x in xy if x not in chosen for y in chosen]
    d = min(x[0] for x in cut)
    assert a not in chosen and b in chosen and distance2(a,b) == d
    chosen.add(a)
    lengths.append(d)
assert lengths == [2,5,1,4,4,2,4,5]
assert distance2(4,6) == distance2(4,2) == 5

result = {
    'status': 'passed',
    'figure29_cycles': cycles,
    'figure30': {'vertices': 14, 'edges': 13, 'tree': True},
    'figure31': {'vertices': len(vertices(raw)), 'edges': len(raw), 'free_parameters_with_unit_entry': 9},
    'figure32': {'vertices': len(vertices(edges)), 'edges': len(edges), 'fundamental_cycles': len(basis),
                 'all_printed_cycles_match_independent_tree_search': True, 'eq6_rows': len(eq6),
                 'answer5_vertex_formulas': len(node_expected)},
    'exercise7': {'fundamental_cycles': len(basis7), 'equations_checked': 5},
    'figure33': {'chosen_edges': order, 'squared_lengths': lengths, 'length': '7+2*sqrt(2)+2*sqrt(5)'},
}
(BASE/'results'/'figures.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
