#!/usr/bin/env python3
"""Twelve selected conversion/overflow cases; no simulator or enumeration.

Expected results are exact hand-derived bit patterns documented in the
recovery proofs. This is a reproduction check, not a general proof by testing.
Run with nice -n 15. No host floating-point operation is used.
"""
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

# name, operation, first input, second input, rounding, expected bits, flags
CASES = [
    ("short-positive-toward-zero", "STSF", "47f0000000000000", "0", 1, "000000007f7fffff", 0x900),
    ("short-negative-up", "STSF", "c7f0000000000000", "0", 2, "00000000ff7fffff", 0x900),
    ("short-positive-down", "STSF", "47f0000000000000", "0", 3, "000000007f7fffff", 0x900),
    ("short-positive-up-control", "STSF", "47f0000000000000", "0", 2, "000000007f800000", 0x900),
    ("short-negative-down-control", "STSF", "c7f0000000000000", "0", 3, "00000000ff800000", 0x900),
    ("largest-finite-short-control", "STSF", "47efffffe0000000", "0", 1, "000000007f7fffff", 0),
    ("double-positive-toward-zero", "FMUL", "7fe0000000000000", "4000000000000000", 1, "7fefffffffffffff", 0x900),
    ("double-negative-up", "FMUL", "ffe0000000000000", "4000000000000000", 2, "ffefffffffffffff", 0x900),
    ("double-nearest-control", "FMUL", "7fe0000000000000", "4000000000000000", 4, "7ff0000000000000", 0x900),
    ("unsigned-integer-top-control", "FLOTU", "ffffffffffffffff", "0", 4, "43f0000000000000", 0x100),
    ("short-integer-tie-control", "SFLOT", "0000000001000001", "0", 4, "4170000000000000", 0x100),
    ("load-smallest-short-control", "LDSF", "0000000000000001", "0", 4, "36a0000000000000", 0),
]


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Use nice -n 15."
    env = dict(os.environ)
    env["CWEBINPUTS"] = str(SOURCES) + ":"
    rows, logs = [], []
    with tempfile.TemporaryDirectory(prefix="fp-conversion-build-", dir=RESULTS) as temporary:
        build = Path(temporary)
        shutil.copyfile(SOURCES / "fp-conversion-boundary-driver.c", build / "driver.c")
        for version, tag, change in (
            ("20131017", "20131017", "-"),
            ("20250620", "20250620", "-"),
            ("audit-directed-overflow-20250620", "20250620", str(SOURCES / "audit-directed-overflow.ch")),
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
            for name, operation, first, second, rounding, expected, flags in CASES:
                result = subprocess.run([str(build / "driver"), operation, first, second, str(rounding)],
                                        text=True, capture_output=True, check=True)
                actual, actual_flags = result.stdout.split()
                actual_flags = int(actual_flags, 16)
                rows.append({"case": name, "version": version,
                             "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                             "operation": operation, "first_input": first, "second_input": second,
                             "rounding_mode": rounding, "expected_bits": expected,
                             "actual_bits": actual, "expected_internal_flags": flags,
                             "actual_internal_flags": actual_flags,
                             "agrees": actual == expected and actual_flags == flags})
    (RESULTS / "fp-conversion-boundary-build.json").write_text(json.dumps(logs, indent=2) + "\n")
    summary = {"scope": "Twelve selected witnesses and controls in two unmodified arithmetic modules and one audit-only change file; all arithmetic trips disabled in architectural interpretation.",
               "expected_results": "Hand-derived exact values, IEEE-directed finite overflow bounds inherited by MMIX STSF, and exact conversion controls; no host floating-point oracle.",
               "cases": rows, "mismatches": sum(not row["agrees"] for row in rows)}
    (RESULTS / "fp-conversion-boundary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"runs": len(rows), "mismatches": summary["mismatches"],
                      "result": "results/fp-conversion-boundary.json"}))


if __name__ == "__main__":
    main()
