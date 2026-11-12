#!/usr/bin/env python3
"""A few fixed boundary traces for Algorithm T; the proof is in the notes.

No census or random search. Vertex identifiers 1..n, SENT=n+1;
settled codes SENT+leader are distinct and greater than every preorder rank.
"""
import json
from pathlib import Path


def printed_t(adj):
    n = len(adj)
    sent = n + 1
    parent = [0] * (n + 2)
    rep = [0] * (n + 2)
    link = [0] * (n + 2)
    arc = [0] * (n + 2)
    edges = [None] + [[v + 1 for v in row] for row in adj]
    p, sink, w, step = 0, sent, sent, 2
    counts = dict.fromkeys(range(2, 10), 0)
    shortcuts = scanned = 0
    while True:
        counts[step] += 1
        assert sum(counts.values()) < 10000
        if step == 2:
            if w == 1:
                break
            w -= 1
            if parent[w] != 0:
                continue
            v, parent[w], root = w, sent, w
            step = 3
        elif step == 3:
            a, p = 0, p + 1
            rep[v], link[v] = p, sent
            step = 4
        elif step == 4:
            step = 7 if a == len(edges[v]) else 5
        elif step == 5:
            u, a = edges[v][a], a + 1
            scanned += 1
            step = 6
        elif step == 6:
            if parent[u] == 0:
                parent[u], arc[v], v, step = v, a, u, 3
            elif u == root and p == n:
                shortcuts += 1
                while v != root:
                    link[v], sink, v = sink, v, parent[v]
                u, step = sent, 8
            else:
                if rep[u] < rep[v]:
                    rep[v], link[v] = rep[u], 0
                step = 4
        elif step == 7:
            u = parent[v]
            if link[v] == sent:
                step = 8
            else:
                if rep[v] < rep[u]:
                    rep[u], link[u] = rep[v], 0
                link[v], sink, step = sink, v, 9
        elif step == 8:
            while rep[sink] >= rep[v]:
                rep[sink], sink = sent + v, link[sink]
            rep[v], step = sent + v, 9
        else:
            if u == sent:
                step = 2
            else:
                v, a, step = u, arc[u], 4
    return rep[1:n + 1], counts, shortcuts, scanned


def reachability_partition(adj):
    n = len(adj)
    reachable = [[i == j or j in adj[i] for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reachable[i][j] |= reachable[i][k] and reachable[k][j]
    return [[reachable[i][j] and reachable[j][i] for j in range(n)] for i in range(n)]


cases = {
    "empty": [],
    "three_isolates": [[], [], []],
    "one_loop": [[0]],
    "parallel_arcs_two_components": [[1, 1], [0], [0, 0]],
    "chain_and_previously_settled_sink": [[], [0], [1], [0, 2]],
    "sibling_cross_arc_merges_suffix": [[2], [0], [1, 0]],
    "shortcut_with_inactive_stack_and_unread_arcs": [[5, 0], [0], [1], [5], [3], [4, 2, 5]],
    "multiple_roots_and_nonroot_cycle": [[1], [0], [], [4], [3], [5]],
}
out = []
for name, adj in cases.items():
    reps, counts, shortcuts, scanned = printed_t(adj)
    expected = reachability_partition(adj)
    actual = [[a == b for b in reps] for a in reps]
    assert actual == expected, name
    out.append({"name": name, "adjacency_zero_based": adj,
                "representative_codes": reps, "T_step_visits": counts,
                "shortcuts": shortcuts, "arcs_scanned": scanned,
                "total_arcs": sum(map(len, adj)), "partition_matches_reachability": True})
assert any(x["arcs_scanned"] < x["total_arcs"] for x in out)
path = Path(__file__).with_name("results") / "tarjan-targeted.json"
path.write_text(json.dumps({"scope": "Eight fixed traces only; general proof is separate.",
                            "cases": out}, indent=2) + "\n")
print(f"{len(out)} fixed traces agree with independent mutual reachability; {path}")
