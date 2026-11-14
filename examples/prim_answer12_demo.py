"""Trace TAOCP 1, answer 2.3.4.1-12, on a four-vertex counterexample.

Based on the pseudocode transcribed in
workstreams/vol1/parallel/free-trees/notes/prim-answer12.md.
Vertex labels are 1..n. Skip the undefined diagonal c(i, i); otherwise
preserve the update range and order, including the final infinity marker.
Run with: python3 examples/prim_answer12_demo.py
"""

from itertools import combinations
from math import inf


def knuth_answer12(c):
    n = len(c) - 1  # Row and column zero are unused.
    a = {i: c[i][n] for i in range(1, n)}
    b = {i: n for i in range(1, n)}
    edges = []
    print(f"Start at vertex {n}: a={list(a.values())}, b={list(b.values())}")

    for step in range(1, n):
        i = min(range(1, n), key=lambda j: a[j])
        edge = (i, b[i])
        edges.append(edge)

        for j in range(1, n):
            if j != i and c[i][j] < a[j]:
                a[j] = c[i][j]
                b[j] = i
        a[i] = inf

        print(f"Step {step}: add {edge}, a={list(a.values())}, b={list(b.values())}")

    return edges


def reachable(n, edges, start):
    """Check connectivity independently of the algorithm's bookkeeping."""
    neighbors = {v: set() for v in range(1, n + 1)}
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    seen, pending = {start}, [start]
    while pending:
        for v in neighbors[pending.pop()]:
            if v not in seen:
                seen.add(v)
                pending.append(v)
    return seen


def main():
    # All six edge costs are positive, finite, symmetric, and distinct.
    # None below marks an absent vertex-zero entry or an undefined diagonal.
    c = [
        [None, None, None, None, None],
        [None, None,    2,   30,    1],
        [None,    2, None,   20,    3],
        [None,   30,   20, None,   10],
        [None,    1,    3,   10, None],
    ]
    n = len(c) - 1
    pairs = list(combinations(range(1, n + 1), 2))
    print("Input costs:", {f"{u}-{v}": c[u][v] for u, v in pairs})
    edges = knuth_answer12(c)
    seen = reachable(n, edges, start=n)
    unique_edges = {tuple(sorted(edge)) for edge in edges}
    is_tree = len(seen) == n and len(unique_edges) == n - 1
    print("\nReturned edges:", edges)
    print(f"Reachable from {n}:", sorted(seen))
    print("Spanning tree:", is_tree)

    # Independent reference: try all 20 subsets of three undirected edges.
    trees = [es for es in combinations(pairs, n - 1)
             if len(reachable(n, es, start=n)) == n]
    best = min(trees, key=lambda es: sum(c[u][v] for u, v in es))
    print("Brute-force minimum spanning tree:", list(best))
    print("Minimum cost:", sum(c[u][v] for u, v in best))
    assert not is_tree, "This input should reproduce the disconnected output."


if __name__ == "__main__":
    main()
