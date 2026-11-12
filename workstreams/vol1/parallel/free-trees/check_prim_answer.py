"""Reproduce the p580 answer-12 defect; independently check the correction.

All costs are finite and symmetric. Undefined diagonal costs are generously
treated as infinity. This removes a separate notational issue without repairing
the updates of already chosen vertices.
"""
from itertools import combinations, product
from pathlib import Path
import json
import math


def cost(c, i, j):
    return math.inf if i == j else c[tuple(sorted((i, j)))]


def answer12(n, c, corrected=False):
    a = {i: cost(c, i, n) for i in range(1, n)}
    b = {i: n for i in range(1, n)}
    edges, trace = [], []
    for step in range(1, n):
        i = min(a, key=lambda j: (a[j], j))
        picked = (i, b[i])
        edges.append(picked)
        before = dict(a)
        for j in range(1, n):
            if corrected and (j == i or a[j] == math.inf):
                continue
            if cost(c, i, j) < a[j]:
                a[j] = cost(c, i, j)
                b[j] = i
        a[i] = math.inf
        trace.append({"step": step, "edge": picked, "before": before,
                      "after": dict(a), "parents_after": dict(b)})
    return edges, trace


def component_count(n, edges):
    parent = list(range(n + 1))
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i, j in edges:
        parent[find(i)] = find(j)
    return len({find(i) for i in range(1, n + 1)})


def kruskal_cost(n, c):
    edges = []
    for ij, value in sorted(c.items(), key=lambda kv: (kv[1], kv[0])):
        if component_count(n, edges + [ij]) < component_count(n, edges):
            edges.append(ij)
    assert component_count(n, edges) == 1
    return sum(c[ij] for ij in edges)


def printable(obj):
    if isinstance(obj, dict):
        return {str(k): printable(v) for k, v in obj.items()}
    if isinstance(obj, (tuple, list)):
        return [printable(v) for v in obj]
    return "infinity" if obj == math.inf else obj


def main():
    c = {(1, 2): 2, (1, 3): 30, (1, 4): 1,
         (2, 3): 20, (2, 4): 3, (3, 4): 10}
    original, trace = answer12(4, c)
    fixed, fixed_trace = answer12(4, c, corrected=True)
    assert original == [(1, 4), (2, 1), (1, 2)]
    assert component_count(4, original) == 2
    assert fixed == [(1, 4), (2, 1), (3, 4)]
    assert sum(cost(c, *e) for e in fixed) == kruskal_cost(4, c) == 13
    counts = {}
    for n in range(1, 5):
        pairs = list(combinations(range(1, n + 1), 2))
        total = failed_original = 0
        for weights in product((1, 2, 3), repeat=len(pairs)):
            costs = dict(zip(pairs, weights))
            old, _ = answer12(n, costs)
            new, _ = answer12(n, costs, corrected=True)
            best = kruskal_cost(n, costs)
            assert len(new) == n - 1 and component_count(n, new) == 1
            assert sum(cost(costs, *e) for e in new) == best
            failed_original += component_count(n, old) != 1
            total += 1
        counts[n] = {"instances": total,
                     "original_disconnected_outputs": failed_original,
                     "corrected_outputs_match_independent_kruskal": total}
    result = {"counterexample_costs": {f"{i},{j}": v for (i, j), v in c.items()},
              "literal_original_trace": trace, "corrected_trace": fixed_trace,
              "original_components": component_count(4, original),
              "correct_minimum_cost": 13, "exhaustive_complete_graph_checks": counts,
              "proof_not_replaced_by_tests": "notes/prim-answer12.md"}
    out = Path(__file__).parent / "results" / "prim-answer12.json"
    out.write_text(json.dumps(printable(result), indent=2) + "\n")
    print(json.dumps(counts, sort_keys=True))


if __name__ == "__main__":
    main()
