"""One targeted test: can McGregor(8) use a color at most six times?"""
import itertools
import json
import time
from pathlib import Path
from pysat.card import CardEnc, EncType
from pysat.formula import CNF
from pysat.solvers import Solver

n = 8
vertices = [(j, k) for j in range(n+1) for k in range(n)]
edges = set()


def edge(u, v):
    assert u in vertices and v in vertices and u != v
    edges.add(tuple(sorted((u, v))))


# Literal transcription of answer 15, including the two inequalities
# j != k and j != k+1 that PDF text extraction often loses.
for j, k in vertices:
    u = j, k
    if u == (1, 0):
        for i in range(n//2, n):
            edge(u, (n, i))
        continue
    if j < n and k < n-1:
        edge(u, (j+1, k+1))
    if j < n and j != k:
        edge(u, (j+1, k))
    if k < n-1 and j != k+1:
        edge(u, (j, k+1))
    if j == 0:
        edge(u, (n, n-1))
    if k < n-1 and j == k:
        edge(u, (n-j, 0))
    if j > 0 and j == k:
        edge(u, (n+1-j, 0))
    if k == n-1 and 0 < j < k:
        edge(u, (n-j, n-j-1))
    if k == n-1 and 0 < j < n:
        edge(u, (n+1-j, n-j))
edge((0, 0), (1, 0))
for i in range(1, n//2+1):
    edge((0, 0), (n, i))
assert len(edges) == 3*len(vertices)-6

# The explicit case n mod 6 == 2 from answer 18.
color = {}
for j, k in vertices:
    color[j, k] = 1 + ((j+k) if j <= k else
                      (j+k+1-n) if 2*k < j else (j+k+2-n)) % 3
color[1, 0] = 3
color[n, n-1] = 4
for k in range(n-1):
    if color[n, k] == color[(0, 0) if 2*k <= n else (1, 0)]:
        color[n, k] = 4
for j in range(1, (n+1)//2):
    color[2*j, j] = 4
    color[2*j+1, j] = 1
color[n, n-2] = 1
color[n-1, n-3] = 4
assert all(color[u] != color[v] for u, v in edges)
distribution = [sum(c == k for c in color.values()) for k in range(1, 5)]
assert distribution == [20, 23, 22, 7]

def var(v, c):
    return 4*(n*v[0]+v[1])+c

clauses = []
for v in vertices:
    clauses.append([var(v, c) for c in range(1, 5)])
    clauses.extend([[-var(v, c), -var(v, d)]
                    for c, d in itertools.combinations(range(1, 5), 2)])
for u, v in sorted(edges):
    clauses.extend([[-var(u, c), -var(v, c)] for c in range(1, 5)])
clauses += CardEnc.atmost([var(v, 1) for v in vertices], bound=6,
                         top_id=4*len(vertices), encoding=EncType.seqcounter).clauses

out = Path(__file__).parent / 'results/bookwise-mcgregor18'
out.mkdir(exist_ok=True)
cnf = CNF(from_clauses=clauses)
cnf.to_file(str(out / 'n8-atmost6.cnf'))
start = time.monotonic()
with Solver(name='glucose4', bootstrap_with=clauses, with_proof=True) as solver:
    satisfiable = solver.solve()
    assert satisfiable is False
    proof = solver.get_proof()
    (out / 'n8-atmost6.drat').write_text('\n'.join(proof)+'\n')
    stats = solver.accum_stats()
result = {'n': n, 'vertices': len(vertices), 'edges': len(edges),
          'printed_coloring_distribution': distribution,
          'at_most_six_satisfiable': satisfiable,
          'clauses': len(cnf.clauses), 'variables': cnf.nv,
          'elapsed_seconds': time.monotonic()-start, 'solver_stats': stats,
          'proof_lines': len(proof),
          'scope': 'Only n=8 and the bound six; no general census or new optimality conjecture.'}
(out / 'result.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
