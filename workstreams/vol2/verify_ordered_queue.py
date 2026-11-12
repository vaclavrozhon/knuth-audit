"""Check the new cyclic-queue proof against saved exact sampling costs.

This is a small, separate check, not a rerun of the old query census.
The general tail bound is proved in the accompanying sequential note.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
old = json.loads((ROOT / "results/ordered-sampling.json").read_text())
saved = {(r["N"], r["n"]): r for r in old["expected_probes"]["rows"]}
rows = []
states = intervals = 0

for N in range(2, 13):
    for n in range(1, min(N // 2, 4) + 1):
        M = 2 * n
        population = [sum(M * x // N == i for x in range(N))
                      for i in range(M)]
        for i in range(M):
            for length in range(1, M + 1):
                q = sum(population[(i + j) % M] for j in range(length))
                assert q <= (N * length + M - 1) // M
                intervals += 1

        expected_displacements = []
        for k in range(n + 1):
            total = 0
            for subset in combinations(range(N), k):
                arrivals = [0] * M
                for x in subset:
                    arrivals[M * x // N] += 1
                backlog = []
                for i in range(M):
                    cumulative = best = 0
                    for length in range(1, M + 1):
                        cumulative += arrivals[(i + length - 1) % M]
                        best = max(best, cumulative - length)
                    backlog.append(best)
                assert all(backlog[i] == max(
                    0, backlog[(i + 1) % M] + arrivals[i] - 1)
                    for i in range(M))

                # Independent ordinary insertion, largest key first.
                table = [None] * M
                displacement = 0
                for x in reversed(subset):
                    i = M * x // N
                    while table[i] is not None:
                        displacement += 1
                        i = (i - 1) % M
                    table[i] = x
                assert displacement == sum(backlog)
                total += sum(backlog)
                states += 1
            expected_displacements.append(F(total, comb(N, k)))

        d = expected_displacements
        stages = [F(N, N - k) + d[k + 1] - d[k] + d[k] / (N - k)
                  for k in range(n)]
        assert stages == [F(v) for v in saved[N, n]["stage_costs"]]
        assert sum(stages) == F(saved[N, n]["total"])
        rows.append(dict(N=N, n=n, expected_displacements=list(map(str, d)),
                         stage_costs=list(map(str, stages)),
                         total=str(sum(stages))))

result = dict(
    scope="N <= 12, n <= min(N/2, 4); validates queue and cost identities, "
          "not the general proof or the unresolved 5n/2 constant.",
    subset_states=states, population_intervals=intervals,
    models=len(rows), rows=rows,
)
(ROOT / "results/ordered-queue.json").write_text(json.dumps(result, indent=2) + "\n")
print("PASS", len(rows), "models;", states, "subset states;", intervals,
      "population intervals; every stage agrees with archived exact query costs")
