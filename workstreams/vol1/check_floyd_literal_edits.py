#!/usr/bin/env python3
"""C0096: three tiny inputs distinguish literal printed edits from the repair."""
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

from garbage_collection import mark_floyd


@dataclass(slots=True)
class Node:
    mark: int = 0
    a: int = 0
    b: int = 0


def literal_floyd(mem, root, trace):
    # E1, followed by E4 because the answer deletes E2 and E3.
    t, p, state = 0, root, 4
    for _ in range(100):
        trace.append({"step": f"E{state}", "T": t, "P": p,
                      "memory": {k: asdict(v) for k, v in mem.items()}})
        if state == 4:
            q = mem[p].a
            if q and not mem[q].mark:
                # The answer explicitly deletes ATOM(P) <- 1 here.
                mem[p].a = t
                t, p = p, q
            else:
                state = 5
        elif state == 5:
            mem[p].mark = 1  # Explicit addition in the printed answer.
            q = mem[p].b
            if q and not mem[q].mark:
                mem[p].b = t
                t, p, state = p, q, 4
            else:
                state = 6
        else:
            if not t:
                return p
            q = t
            if not mem[q].mark:  # Printed replacement of ATOM(Q) = 1.
                trace[-1]["next_assignment"] = f"ATOM({q}) <- 0"
                # This assignment is in original E6; answer 7 does not delete it.
                mem[q].atom = 0
                t, mem[q].a, p, state = mem[q].a, p, q, 5
            else:  # Printed replacement of ATOM(Q) = 0 by MARK(Q) = 1.
                t, mem[q].b, p = mem[q].b, p, q
    raise AssertionError("Unexpected loop in a tiny input")


def run():
    results = []
    cases = [
        ("singleton", {1: (0, 0)}, False),
        ("left_child", {1: (2, 0), 2: (0, 0)}, True),
        ("right_child", {1: (0, 2), 2: (0, 0)}, False),
    ]
    for name, links, should_fail in cases:
        mem = {k: Node(a=a, b=b) for k, (a, b) in links.items()}
        trace = []
        error = None
        try:
            root = literal_floyd(mem, 1, trace)
        except AttributeError as exc:
            error = str(exc)
        assert bool(error) == should_fail
        if error:
            assert trace[-1]["step"] == "E6"
            assert trace[-1]["next_assignment"] == "ATOM(1) <- 0"
        else:
            assert root == 1
            assert all(v.mark == 1 and (v.a, v.b) == links[k]
                       for k, v in mem.items())
        # Existing intended implementation already omits the leftover assignment.
        repaired = {k: Node(a=a, b=b) for k, (a, b) in links.items()}
        assert mark_floyd(repaired, 1) == 1
        assert all(v.mark == 1 and (v.a, v.b) == links[k]
                   for k, v in repaired.items())
        results.append({"name": name, "input_links": links,
                        "literal_error": error, "literal_trace": trace,
                        "repaired_marks_and_links": {k: asdict(v) for k, v in repaired.items()}})
    result = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Only three tiny cases; the omitted E6 deletion is established by source comparison and the two-node trace.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "existing_implementation_sha256": hashlib.sha256(Path(__file__).with_name("garbage_collection.py").read_bytes()).hexdigest(),
        "cases": results,
    }
    out = Path(__file__).with_name("results") / "sequential-floyd-literal-edits.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"cases": len(cases), "literal_left_return_invalid": True,
                      "repair_passed_all": True, "output": str(out)}))


if __name__ == "__main__":
    run()
