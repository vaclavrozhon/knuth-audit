#!/usr/bin/env python3
"""Eight targeted boundary checks, with a separate exact rational oracle.

Run with nice -n 15. Builds only the arithmetic module in a temporary owned
directory, never the simulator; original CWEB sources are not modified.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import tempfile

BASE = Path(__file__).resolve().parent
SOURCES = BASE / "sources"
RESULTS = BASE / "results"


def two(k):
    return Fraction(2) ** k


def value_and_scale(raw):
    u = int(raw, 16)
    sign, exp, frac = u >> 63, (u >> 52) & 2047, u & ((1 << 52) - 1)
    assert exp != 2047, "These targeted witnesses use finite values only."
    if exp == 0:
        value = frac * two(-1074)
        scale = two(-1021) if frac else Fraction(0)
    else:
        value = ((1 << 52) + frac) * two(exp - 1075)
        scale = two(exp - 1022)
    return (-value if sign else value), scale


CASES = [
    ("opposite-d54-sim", "3ff0000000000000", "bc90000000000000", "3fe0000000000000", 1),
    ("opposite-d55-sim", "3ff0000000000000", "bc80000000000000", "3fe0000000000000", 1),
    ("opposite-d100-sim", "3ff0000000000000", "b9b0000000000000", "3fe0000000000000", 1),
    ("same-d55-sim", "3ff0000000000000", "3c80000000000000", "3fe0000000000000", 1),
    ("opposite-d55-next-epsilon", "3ff0000000000000", "bc80000000000000", "3fe0000000000001", 1),
    ("opposite-d55-equivalent", "3ff0000000000000", "bc80000000000000", "4350000000000000", 0),
    ("opposite-d54-equivalent", "3ff0000000000000", "bc90000000000000", "4340000000000000", 0),
    ("opposite-smallest-subnormal-sim", "3ff0000000000000", "8000000000000001", "3fe0000000000000", 1),
]


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Use nice -n 15."
    outputs = []
    logs = []
    env = dict(os.environ)
    env["CWEBINPUTS"] = str(SOURCES) + ":"
    with tempfile.TemporaryDirectory(prefix="fepscomp-build-", dir=RESULTS) as temporary:
        build = Path(temporary)
        shutil.copyfile(SOURCES / "fepscomp-boundary-driver.c", build / "driver.c")
        for version, tag, change in (
            ("20131017", "20131017", "-"),
            ("20250620", "20250620", "-"),
            ("audit-corrected-20250620", "20250620", str(SOURCES / "audit-fepscomp-ceiling.ch")),
        ):
            source = SOURCES / f"mmix-arith-{tag}.w"
            for command in (
                ["ctangle", str(source), change, "mmix-arith.c"],
                ["gcc", "-O0", "-std=c11", "driver.c", "-o", "driver"],
            ):
                result = subprocess.run(command, cwd=build, env=env, text=True,
                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                logs.append({"version": version, "command": command,
                             "returncode": result.returncode, "output": result.stdout})
                result.check_returncode()
            for name, yraw, zraw, eraw, similarity in CASES:
                y, yscale = value_and_scale(yraw)
                z, zscale = value_and_scale(zraw)
                epsilon, _ = value_and_scale(eraw)
                distance = abs(y-z)
                bound = epsilon * ((max if similarity else min)(yscale,zscale))
                expected_relation = int(distance <= bound)
                expected_order = (y > z) - (y < z)
                expected_instruction = (0 if expected_relation else expected_order) if similarity else expected_relation
                result = subprocess.run([str(build / "driver"), yraw, zraw, eraw, str(similarity)],
                                        text=True, capture_output=True, check=True)
                relation, order, instruction = map(int, result.stdout.split())
                assert order == expected_order
                outputs.append({"case": name, "version": version,
                                "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                                "y": yraw, "z": zraw, "epsilon": eraw,
                                "operation": "FCMPE" if similarity else "FEQLE",
                                "exact_distance": str(distance), "exact_bound": str(bound),
                                "expected_relation": expected_relation, "actual_relation": relation,
                                "expected_instruction": expected_instruction, "actual_instruction": instruction,
                                "agrees": instruction == expected_instruction})
    (RESULTS / "fepscomp-boundary-build.json").write_text(json.dumps(logs, indent=2) + "\n")
    summary = {"scope": "Eight explicit witnesses/controls against two unchanged arithmetic modules and one audit-only change file.",
               "oracle": "Exact Fraction values and neighborhood radii; no host floating-point arithmetic.",
               "cases": outputs, "mismatches": sum(not row["agrees"] for row in outputs)}
    (RESULTS / "fepscomp-boundary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"runs": len(outputs), "mismatches": summary["mismatches"],
                      "result": "results/fepscomp-boundary.json"}))


if __name__ == "__main__":
    main()
