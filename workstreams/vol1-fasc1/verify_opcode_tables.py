#!/usr/bin/env python3
"""Finite table reconciliation, not an instruction-execution test.

All 256 cells in each printed table are expanded, and both branch outcomes
are compared with the primary simulator's declared cost model. Run at nice 15.
"""
from pathlib import Path
import hashlib
import json
import os
import re

BASE = Path(__file__).resolve().parent


def expand_table(path, marker):
    text = path.read_text().split(marker, 1)[1].split("π =", 1)[0]
    pattern = r"(\[UN\]SAVE|[A-Z0-9]+(?:\[[IB]\])?)\s+(\d*[μυπ](?:\s*[+−]\s*\d*[μυπ])*)"
    entries = []
    for name, cost in re.findall(pattern, text):
        if name == "[UN]SAVE":
            names = ["SAVE", "UNSAVE"]
        elif name.endswith("[I]") or name.endswith("[B]"):
            names = [name[:-3], name[:-3] + name[-2]]
        else:
            names = [name]
        coefficients = dict.fromkeys("μυπ", 0)
        expression = re.sub(r"\s", "", cost)
        for sign, coefficient, symbol in re.findall(r"([+−]?)(\d*)([μυπ])", expression):
            coefficients[symbol] += (-1 if sign == "−" else 1) * int(coefficient or 1)
        for expanded in names:
            entries.append({"opcode": f"{len(entries):02x}", "name": expanded,
                            "printed_cost": expression, "coefficients": coefficients})
    assert len(entries) == 256, (path.name, len(entries))
    assert len({q["name"] for q in entries}) == 256
    return entries


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Use nice -n 15."
    source_path = BASE / "sources/mmix-sim-20131017.w"
    source = source_path.read_text()
    matches = re.findall(r'\{"([0-9A-Z]+)",0x[0-9a-f]+,[^,]+,(\d+),(\d+),', source)
    assert len(matches) == 256, len(matches)
    tables, differences = [], []
    for file_page, marker in [(28, "THE OPCODES OF MMIX"), (144, "MMIX OPERATION CODES"), (145, "MMIX OPERATION CODES")]:
        path = BASE / f"sources/file-{file_page:03}.txt"
        entries = expand_table(path, marker)
        for opcode, (entry, actual) in enumerate(zip(entries, matches)):
            name, mems, base_time = actual
            comparisons = []
            for taken in ([False, True] if 0x40 <= opcode <= 0x5f else [False]):
                coefficients = entry["coefficients"]
                book_time = coefficients["υ"] + 2 * taken * coefficients["π"]
                # Primary dispatch lines 2109–2116: base cost 1, plus 2
                # exactly when actual direction differs from B/PB prediction.
                penalty = 2 * (taken != (opcode >= 0x50)) if 0x40 <= opcode <= 0x5f else 0
                agrees = entry["name"] == name and coefficients["μ"] == int(mems) and book_time == int(base_time) + penalty
                comparisons.append({"taken": taken, "agrees": agrees})
                if not agrees:
                    differences.append({"file_page": file_page, "entry": entry,
                                        "source": actual, "taken": taken})
            entry["source_mems"] = int(mems)
            entry["source_base_oops"] = int(base_time)
            entry["comparisons"] = comparisons
        tables.append({"file_page": file_page, "native_source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "entries": entries})
    result = {"scope": "Every one of the 256 opcode/name/cost cells in each of three printed tables; every B/PB cell checked for taken and untaken. Original images also inspected. No claim about the correctness of the instruction implementations.",
              "source_path": str(source_path.relative_to(BASE)),
              "source_sha256": hashlib.sha256(source_path.read_bytes()).hexdigest(),
              "tables": tables, "differences": differences}
    (BASE / "results/opcode-table-reconciliation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"tables": len(tables), "cells_per_table": 256,
                      "branch_outcomes_per_table": 64, "differences": len(differences)}))
    assert not differences


if __name__ == "__main__":
    main()
