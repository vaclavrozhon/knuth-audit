"""Small, targeted traces for the new §2.3.3 prose concerns.

This does not repeat the accepted polynomial test suite.  A line tracer reads
the actual A2 result and counts A4's leftward links in the preserved literal
algorithm.  No implementation of A is changed.
"""

import inspect
import json
from pathlib import Path
import sys

from tree_polynomials import Pool, add_printed


def trace_add(first, second):
    pool = Pool()
    p, q = pool.build(first), pool.build(second)
    original_first, first_nodes = pool.validate(p, 1)
    before_first = pool.snapshot(first_nodes)
    source, start = inspect.getsourcelines(add_printed)
    left_line = start + next(
        i for i, line in enumerate(source) if line.strip() == "q = pool[q].left"
    )
    loop_line = start + next(
        i for i, line in enumerate(source) if line.strip() == "counts[step] += 1"
    )
    previous_step = None
    left_exponents = []
    insertions = []

    def tracer(frame, event, arg):
        nonlocal previous_step
        if frame.f_code is not add_printed.__code__:
            return tracer
        if event == "line" and frame.f_lineno == left_line:
            here = frame.f_locals["q"]
            left_exponents.append(pool[pool[here].left].exp)
        if event == "line" and frame.f_lineno == loop_line:
            step = frame.f_locals["step"]
            if previous_step == 2:
                parent = frame.f_locals["q"]
                child = pool[parent].down
                insertions.append({
                    "new_child": child,
                    "cv": pool[child].cv,
                    "down": pool[child].down,
                    "exp": pool[child].exp,
                    "up": pool[child].up,
                    "parent": parent,
                })
            previous_step = step
        return tracer

    sys.settrace(tracer)
    try:
        counts = add_printed(pool, p, q)
    finally:
        sys.settrace(None)
    result, result_nodes = pool.validate(q, 1)
    assert pool.validate(p, 1)[0] == original_first
    assert pool.snapshot(first_nodes) == before_first
    expected = dict(first)
    for m, c in second.items():
        expected[m] = expected.get(m, 0) + c
    expected = {m: c for m, c in expected.items() if c}
    assert result == expected
    pool.partition(first_nodes, result_nodes)
    return {
        "insertions": insertions,
        "a4_leftward_exponents": left_exponents,
        "a4_leftward_links": len(left_exponents),
        "step_counts": dict(counts),
        "result": {str(m): c for m, c in result.items()},
    }


def main():
    insertion = trace_add({(1,): 1}, {(0,): 1})
    assert len(insertion["insertions"]) == 1
    node = insertion["insertions"][0]
    assert (node["cv"], node["down"], node["exp"]) == (1, 0, 0)
    families = []
    for n in [1, 2, 3, 8, 32, 64]:
        result = trace_add({(1,): 1}, {(i,): 1 for i in range(1, n + 1)})
        assert result["a4_leftward_exponents"] == list(range(n, 0, -1))
        # An independent descending monomial list reaches exponent 1 only
        # after visiting every nonzero term of the second polynomial.
        flat_exponents = list(range(n, 0, -1))
        matched = next(i for i, exponent in enumerate(flat_exponents) if exponent == 1)
        assert matched + 1 == n
        families.append({"n": n, "tree_trace": result,
                         "flat_nonzero_terms_visited": matched + 1})
    output = {
        "status": "pass",
        "scope": "A2 explanatory wording and a family qualifying the informal speed claim, not a new correctness audit of Algorithm A.",
        "insertion_x_plus_one": insertion,
        "speed_family": families,
        "limits": "The general argument is in the accompanying note. No machine-time constant or universal performance ratio is inferred from these small traces.",
    }
    path = Path(__file__).parent / "results/sequential-tree-addition-boundary-notes.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"status": "pass", "cases": len(families) + 1,
                      "output": str(path)}))


if __name__ == "__main__":
    main()
