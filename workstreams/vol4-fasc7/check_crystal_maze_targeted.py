#!/usr/bin/env python3
"""Exact small structural sums, not enumeration of 8**8 assignments."""
from itertools import combinations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
vertices = set(range(1, 9))
drawn_edges = {tuple(map(int, s)) for s in
               '12 34 45 56 78 14 25 47 58 13 15 24 26 37 48 57 68'.split()}
all_edges = set(combinations(range(1, 9), 2))
complement = all_edges - drawn_edges
assert len(drawn_edges) == 17 and len(complement) == 11
printed15 = '16 17 18 23 27 28 32 35 36 38 46 53 61 63 64 67 71 72 76 81 82 83'.split()
oriented = {tuple(map(int, s)) for s in printed15}
assert len(oriented) == 22
assert oriented == {(u, v) for u, v in complement} | {(v, u) for u, v in complement}
printed12 = 'AC AD AE AF AG AH BD BE BF BG BH CA CE CF CG CH DA DB DF DG DH EA EB EC EG EH FA FB FC FD FH GA GB GC GD GE HA HB HC HD HE HF'.split()
assert len(printed12) == 42 and len(set(printed12)) == 42
assert set(printed12) == {a+b for a in 'ABCDEFGH' for b in 'ABCDEFGH' if abs(ord(a)-ord(b)) > 1}
allowed = {a: {b for b in vertices if abs(a-b) > 1} for a in vertices}
matrix = [[0]*8 for _ in range(8)]
summands = 0
for a in vertices:
    for b in allowed[a]:
        pool = allowed[a] & allowed[b]
        pairs = [(u, v) for u in pool for v in pool if v in allowed[u]]
        for u, v in pairs:
            for r, s in pairs:
                matrix[a-1][b-1] += len(allowed[u] & allowed[a] & allowed[r]) * len(allowed[v] & allowed[b] & allowed[s])
                summands += 1
assert sum(map(sum, matrix)) == 2624
lex = (1, 3, 3, 5, 7, 1, 1, 3)
assert all(abs(lex[u-1]-lex[v-1]) > 1 for u, v in drawn_edges)
neighbors = {v: {u for u in vertices if (u,v) in oriented} for v in vertices}
walk_vectors = [[1]*8]
for _ in range(7):
    old = walk_vectors[-1]
    walk_vectors.append([sum(old[u-1] for u in neighbors[v]) for v in range(1,9)])
assert sum(walk_vectors[-1]) == 20358
paths = [[4,6,1,7,2,8,3,5], [4,6,7,1,8,2,3,5]]
paths += [p[::-1] for p in paths]
labels = []
for path in paths:
    assert set(path) == vertices and all((u,v) in oriented for u,v in zip(path,path[1:]))
    x = ['']*8
    for letter,v in zip('ABCDEFGH',path):x[v-1]=letter
    labels.append(''.join(x))
alpha = [set() for _ in range(6)]
beta = [set() for _ in range(6)]
for k in range(1,6):
    t = k & -k
    for j in range(k,min(6,k+t)):alpha[j].add(k)
    for j in range(k-t,k):beta[j].add(k)
assert all(bool(alpha[i]&beta[j]) == (i>j) for i in range(6) for j in range(6))
assert alpha[3] == {2,3}
edge_pairs = [(a,b) for a in complement for b in complement if a!=b]
touch = sum(bool(set(a)&set(b)) for a,b in edge_pairs)
assert touch == 48 and len(edge_pairs)-touch == 62
result = {'scope':'Bounded central-pair decomposition (at most6048 summands), seven 8-entry walk-vector updates, printed tuple sets and fixed ordering gadget. No8**8 search, no benchmark reproduction.',
          'graph_edges':sorted(drawn_edges),'complement_edges':sorted(complement),
          'first_model_central_pair_matrix':matrix,'first_model_summands':summands,'first_model_total':2624,
          'first_model_lexicographic_witness':'ACCEGAAC',
          'second_model_walk_vectors':walk_vectors,'second_model_total':20358,
          'four_hamiltonian_paths':paths,'four_vertex_labelings':labels,
          'ordering_alpha_items':[sorted(s) for s in alpha],'ordering_beta_items':[sorted(s) for s in beta],
          'ordered_distinct_edge_pairs':{'intersecting':touch,'disjoint':len(edge_pairs)-touch},
          'proof':'notes/crystal-maze-and-exercises-013-016.md'}
(ROOT/'results/crystal-maze-targeted.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['first_model_central_pair_matrix','first_model_summands','first_model_total','second_model_walk_vectors','second_model_total','four_vertex_labelings','ordering_alpha_items','ordering_beta_items']},ensure_ascii=False,indent=2))
