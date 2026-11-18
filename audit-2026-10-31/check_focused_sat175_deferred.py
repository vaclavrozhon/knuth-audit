"""Fixed local witness for the placement of the temporary-stack drain in SAT175.

This models two lookaheads and their clause counts, not a complete SAT solver.
F208's retained prefix and F209's unconditional decrement are applied in both
versions. Signed integers 1,...,7 denote a,b,c,d,e,u,v and their negations.
"""
from itertools import product
import json
from pathlib import Path
import time

started = time.perf_counter()
BINARY = [(1, -2)]
BIG = [(-1, -2, 3)]
BIG += [(-3, sd * 4, se * 5) for sd, se in product((-1, 1), repeat=2)]
BIG += [(1, su * 6, sv * 7) for su, sv in product((-1, 1), repeat=2)]
CLAUSES = BINARY + BIG


def run(drain_inside):
    values = {}
    stack = []
    sizes = [len(c) for c in BIG]
    cursor = 0
    trace = []
    implications = {}
    for x, y in BINARY:
        implications.setdefault(-x, []).append(y)
        implications.setdefault(-y, []).append(x)

    # b implies a, so a is a valid parent of b. Postorder offsets are 4,2.
    for literal, degree in [(1, 4), (2, 2)]:
        assert all(values[abs(x)][0] >= degree for x in stack[:cursor])
        stack[cursor:] = []  # E <- G, retaining the already processed prefix.
        weight = 0
        pending = []
        windfalls = []
        processed = []

        def status(x):
            old_degree, truth = values.get(abs(x), (0, False))
            return None if old_degree < degree else truth == (x > 0)

        def propagate_binary(x):
            state = status(x)
            assert state is not False, "Unexpected binary conflict in this witness"
            if state is None:
                values[abs(x)] = (degree, x > 0)
                stack.append(x)
                for y in implications.get(x, []):
                    propagate_binary(y)

        def drain():
            while pending:
                x = pending.pop()
                state = status(x)
                assert state is not False, "Unexpected temporary-stack conflict"
                if state is None:
                    windfalls.append(x)
                    propagate_binary(x)

        propagate_binary(literal)
        while cursor < len(stack):
            x = stack[cursor]
            cursor += 1
            processed.append(x)
            for index, clause in enumerate(BIG):
                if -x not in clause:
                    continue
                sizes[index] -= 1  # F209 is repaired in both runs.
                if sizes[index] >= 2:
                    assert sizes[index] == 2
                    weight += 1  # K_2=1; no other weight occurs here.
                elif not any(status(y) is True for y in clause):
                    free = [y for y in clause if status(y) is None]
                    assert len(free) == 1
                    pending.append(free[0])
            if drain_inside:
                drain()
        if not drain_inside:
            drain()  # Printed placement: immediately before the final line (72).
        trace.append({
            "literal": literal, "degree": degree, "processed": processed,
            "R": stack.copy(), "G": cursor, "E": len(stack),
            "new_weight": weight, "windfalls": windfalls,
            "sizes": sizes.copy(),
        })
    return trace


printed = run(False)
corrected = run(True)
assert printed[0]["new_weight"] == corrected[0]["new_weight"] == 1
assert printed[1]["new_weight"] == 0
assert (printed[1]["G"], printed[1]["E"]) == (2, 3)
assert corrected[1]["new_weight"] == 4
assert corrected[1]["G"] == corrected[1]["E"] == 3


def satisfied(clause, assignment):
    return any(assignment[abs(x) - 1] == (x > 0) for x in clause)


models = [bits for bits in product((False, True), repeat=7)
          if all(satisfied(clause, bits) for clause in CLAUSES)]
unsafe_clause = (2, -1)  # X9: b OR not-parent(b), where parent(b)=a.
remaining = [bits for bits in models if satisfied(unsafe_clause, bits)]
assert len(models) == 16 and not remaining
assert all(bits[:3] == (True, False, False) for bits in models)

result = {
    "variables": ["a", "b", "c", "d", "e", "u", "v"],
    "clauses": CLAUSES,
    "printed": printed, "corrected": corrected,
    "unsafe_X9_clause": unsafe_clause,
    "original_model_count": len(models),
    "model_count_after_X9_clause": len(remaining),
    "example_original_model": models[0],
    "assignments_checked": 128,
    "elapsed_seconds": time.perf_counter() - started,
    "scope": "Two fixed local lookaheads plus a 128-assignment truth table. "
             "Not a full L/X/Y implementation or a claim about SAT11K output.",
}
destination = Path(__file__).parent / "results/focused-sat175-deferred.json"
destination.write_text(json.dumps(result, indent=2) + "\n")
print("Printed: w(b)=0, G=2<E=3; corrected: w(b)=4, G=E=3.")
print("The X9 clause removes all 16 satisfying assignments of the fixed input.")
