"""Two fixed matrices for the suspected column polarity error in answer 418.

No enumeration or SAT search: fixed inputs are propagated, then unused
branching-program states are set to zero and every clause is evaluated.
"""
import json
from pathlib import Path


def check(matrix, corrected):
    m, n = len(matrix), len(matrix[0])
    names = {}
    clauses = []

    def var(name):
        if name not in names:
            names[name] = len(names) + 1
        return names[name]

    def x(i, j):
        return var(f"x_{i}_{j}")

    def line(kind, index, length, inputs, complement):
        def a(k, j):
            return var(f"{kind}_{index}_{k}_{j}")
        clauses.append([a(1, 1)])  # Repair c_i to c_j in both comparisons.
        for k in range(1, length + 1):
            for j in range(1, k + 1):
                clauses.append([-a(k, j), inputs[k - 1], a(k + 1, j)])
                clauses.append([-a(k, j), -inputs[k - 1], a(k + 1, j + 1)])
        sign = -1 if complement else 1
        clauses.append([-sign * a(length + 1, 1)])
        clauses.append([sign * a(length + 1, length + 1)])
        for j in range(1, length):
            clauses.append([-a(length + 1, j + 1), sign * inputs[j - 1]])

    for i in range(1, m + 1):
        line("r", i, n, [x(i, j) for j in range(1, n + 1)], False)
    for j in range(1, n + 1):
        line("c", j, m, [x(i, j) for i in range(1, m + 1)], corrected)
    values = {x(i + 1, j + 1): bool(matrix[i][j])
              for i in range(m) for j in range(n)}
    inverse = {v: k for k, v in names.items()}
    while True:
        changed = False
        for clause in clauses:
            if any(abs(l) in values and values[abs(l)] == (l > 0) for l in clause):
                continue
            unknown = [l for l in clause if abs(l) not in values]
            if not unknown:
                return {"satisfiable": False, "proof": "unit propagation conflict",
                        "conflict_clause": [("" if l > 0 else "not ") + inverse[abs(l)]
                                            for l in clause]}
            if len(unknown) == 1:
                l = unknown[0]
                values[abs(l)] = l > 0
                changed = True
        if not changed:
            break
    for v in names.values():
        values.setdefault(v, False)
    assert all(any(values[abs(l)] == (l > 0) for l in c) for c in clauses)
    return {"satisfiable": True, "clauses_checked": len(clauses),
            "true_variables": [inverse[v] for v in sorted(values) if values[v]]}


def intended(matrix):
    def hidden(row):
        weight = sum(row)
        return bool(weight and row[weight - 1])
    return all(hidden(row) for row in matrix) and not any(hidden(col) for col in zip(*matrix))


if __name__ == "__main__":
    cases = [([list(map(int, row)) for row in ["111", "111", "111"]], False),
             ([list(map(int, row)) for row in ["1000", "0110", "1000"]], True)]
    result = []
    for matrix, expected in cases:
        assert intended(matrix) == expected
        printed = check(matrix, False)
        repaired = check(matrix, True)
        assert printed["satisfiable"] != expected
        assert repaired["satisfiable"] == expected
        result.append({"matrix": matrix, "intended": expected,
                       "printed_after_initial_index_repair": printed,
                       "corrected_column_polarities": repaired})
    output = Path(__file__).parent / "results/bookwise-sat418-fixed-matrices.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print("Two fixed matrices checked; printed and corrected outcomes verified.")
