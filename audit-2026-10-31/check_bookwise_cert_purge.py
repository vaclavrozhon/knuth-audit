"""Fixed witnesses for D245; no solver benchmark or instance census."""
import json
from pathlib import Path


def propagate(clauses, values, trail):
    """One straightforward unit-propagation model, with explicit initial state."""
    reason = {}
    while True:
        changed = False
        for ci, clause in enumerate(clauses):
            if any(abs(l) in values and values[abs(l)] == (l > 0) for l in clause):
                continue
            free = [l for l in clause if abs(l) not in values]
            if not free:
                return ci, reason, trail
            if len(free) == 1:
                l = free[0]
                values[abs(l)] = l > 0
                trail.append(l)
                reason[abs(l)] = ci
                changed = True
        if not changed:
            return None, reason, trail


def check():
    # Signed literals use 1 for the dummy x0 and 2 for the ordinary variable a.
    sat_input = [(-2, -1)]
    bad = propagate(sat_input, {1: True, 2: True}, [1])
    good = propagate(sat_input, {1: True}, [1])
    assert bad[0] == 0 and good[0] is None
    f224 = {"input": ["not a"], "candidate": [],
            "printed_initialization_finds_conflict": True,
            "correct_initialization_finds_conflict": False,
            "satisfying_assignment": {"a": False}}

    clauses = [(2, -1), (-2, -1)]
    conflict, reasons, trail = propagate(clauses, {1: True}, [1])
    assert conflict == 1 and trail == [1, 2]
    tloc = {abs(l): p for p, l in enumerate(trail)}

    def backward_mark(include_first):
        c = clauses[conflict]
        marked, stamped = {conflict}, {abs(l) for l in c}
        p = max(tloc[abs(l)] for l in (c if include_first else c[1:]))
        while p >= 1:  # E=1, only the dummy is an initial assumption.
            l = trail[p]
            p -= 1
            if abs(l) in stamped:
                ri = reasons[abs(l)]
                marked.add(ri)
                stamped.update(abs(x) for x in clauses[ri][1:])
        return sorted(marked)

    assert backward_mark(False) == [1]
    assert backward_mark(True) == [0, 1]
    f225 = {"input": ["a", "not a"], "trail": ["x0", "a"],
            "printed_marked_clause_indices": backward_mark(False),
            "correct_marked_clause_indices": backward_mark(True),
            "printed_core_has_model": {"a": False}}

    # Two protected clauses and six ordinary clauses tied at RANGE=16.
    protected, tied, target = 2, 6, 4
    corrected_keep_at_threshold = target - protected
    assert protected + corrected_keep_at_threshold == target
    # Isolate F226 by correcting the tie-selection rule first.
    keep_using_unrecorded_zero_bucket = target - 0
    f226 = {"protected": protected, "tied": tied, "target": target,
            "retained_with_omitted_zero_bucket_and_correct_tie_rule":
                protected + keep_using_unrecorded_zero_bucket,
            "correct_retained": target}
    assert f226["retained_with_omitted_zero_bucket_and_correct_tie_rule"] == 6
    # Isolate F227 by supplying the correct histogram first.
    printed_discard = target - protected
    f227 = {"protected": protected, "tied": tied, "target": target,
            "printed_discard": printed_discard,
            "printed_retained": protected + tied - printed_discard,
            "correct_discard": protected + tied - target,
            "book_example_printed_retained": 3081 + 59 - (3126 - 3081),
            "book_example_correct_retained": 3126}
    assert f227["printed_retained"] == 6
    assert f227["book_example_printed_retained"] == 3095

    # d=0 after learning the unit x1 from (x1 or x2), (x1 or not x2).
    # Stale i1=0 from the previous decision; i2 has never been established.
    trail, decisions, activities = [1], {1: 0}, {1: 1, 2: 1}
    d = 0
    depth = 0
    invalid_read = None
    while True:
        try:
            decision_var = trail[decisions[depth + 1]]
        except KeyError:
            invalid_read = depth + 1
            break
        if activities[decision_var] < activities[2]:
            break
        depth += 1
    assert invalid_read == 2
    corrected_depth = 0
    while corrected_depth < d and activities[trail[decisions[corrected_depth + 1]]] >= activities[2]:
        corrected_depth += 1
    assert corrected_depth == 0
    f228 = {"current_depth": d, "printed_accesses_nonexistent_decision_level": invalid_read,
            "corrected_depth": corrected_depth}

    f229 = {"existing": 6252, "protected": 12, "target": 3126,
            "printed_number_to_forget": 3114, "printed_retained": 6252 - 3114,
            "correct_number_to_forget": 6252 - 3126,
            "correct_number_of_unprotected_clauses_to_keep": 3126 - 12}
    assert f229["printed_retained"] == 3138 > f229["target"]
    return {"scope": "Fixed local witnesses only; no independent full CDCL implementation.",
            **{f"F{224+i}": x for i, x in enumerate([f224, f225, f226, f227, f228, f229])}}


if __name__ == "__main__":
    result = check()
    target = Path(__file__).parent / "results/bookwise-cert-purge-fixed-witnesses.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"checked": [f"F{i}" for i in range(224, 230)], "result": str(target)}))
