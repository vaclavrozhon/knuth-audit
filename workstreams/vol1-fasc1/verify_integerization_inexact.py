#!/usr/bin/env python3
"""Sixteen selected FINT/FIX/FIXU witnesses and branch controls.

Bit patterns and flags follow exact integer arithmetic and IEEE 754-1985
sections 4, 5.4, 5.5, 7.5, as inherited by the documented MMIX contract.
No host floating-point oracle, simulator, enumeration or prior run restart.
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

# name, operation, input, Y rounding selector, expected result, internal flags
CASES = [
    ("half-nearest-via-rA", "FINT", "3fe0000000000000", 0, "0000000000000000", 0x100),
    ("one-and-half-off", "FINT", "3ff8000000000000", 1, "3ff0000000000000", 0x100),
    ("negative-one-and-half-up", "FINT", "bff8000000000000", 2, "bff0000000000000", 0x100),
    ("negative-one-and-half-down", "FINT", "bff8000000000000", 3, "c000000000000000", 0x100),
    ("least-subnormal-nearest", "FINT", "0000000000000001", 4, "0000000000000000", 0x100),
    ("one-exact-middle-branch", "FINT", "3ff0000000000000", 4, "3ff0000000000000", 0),
    ("two-to-52-fast-branch", "FINT", "4330000000000000", 4, "4330000000000000", 0),
    ("quiet-nan-preserved", "FINT", "fff8000000000001", 4, "fff8000000000001", 0),
    ("signaling-nan-quieted", "FINT", "7ff0000000000001", 4, "7ff8000000000001", 0x1000),
    ("fix-zero-after-rounding", "FIX", "3fe0000000000000", 0, "0000000000000000", 0x100),
    ("fix-negative-rounded", "FIX", "bff8000000000000", 4, "fffffffffffffffe", 0x100),
    ("fixu-rounded", "FIXU", "3ff8000000000000", 4, "0000000000000002", 0x100),
    ("fix-negative-signed-boundary", "FIX", "c3e0000000000000", 4, "8000000000000000", 0),
    ("fix-positive-signed-boundary", "FIX", "43e0000000000000", 4, "8000000000000000", 0x2000),
    ("fixu-suppresses-only-W", "FIXU", "43e0000000000000", 4, "8000000000000000", 0),
    ("fix-signaling-raw-bits", "FIX", "7ff0000000000001", 4, "7ff0000000000001", 0x1000),
]


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Use nice -n 15."
    env = dict(os.environ)
    env["CWEBINPUTS"] = str(SOURCES) + ":"
    rows, logs = [], []
    with tempfile.TemporaryDirectory(prefix="integerization-build-", dir=RESULTS) as temporary:
        build = Path(temporary)
        shutil.copyfile(SOURCES / "integerization-inexact-driver.c", build / "driver.c")
        for version, tag, change in (
            ("20131017", "20131017", "-"),
            ("20250620", "20250620", "-"),
            ("audit-integerization-20250620", "20250620",
             str(SOURCES / "audit-integerization-inexact.ch")),
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
            for name, op, raw, mode, expected, flags in CASES:
                result = subprocess.run([str(build / "driver"), op, raw, str(mode)],
                                        text=True, capture_output=True, check=True)
                actual, actual_flags = result.stdout.split()
                actual_flags = int(actual_flags, 16)
                rows.append({"case": name, "version": version, "operation": op,
                             "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                             "input_bits": raw, "rounding_selector": mode,
                             "expected_bits": expected, "actual_bits": actual,
                             "expected_internal_flags": flags,
                             "actual_internal_flags": actual_flags,
                             "agrees": actual == expected and actual_flags == flags})
    (RESULTS / "integerization-inexact-build.json").write_text(json.dumps(logs, indent=2) + "\n")
    summary = {"scope": "Sixteen selected FINT/FIX/FIXU witnesses and controls, each called once in both original modules and one audit-only correction. All arithmetic trips disabled; Y=0 selects nearest rA mode.",
               "oracle": "Exact encoded rational inputs, integer rounding and IEEE 754-1985 4/5.4/5.5/7.5 via MMIX's explicit arithmetic and conversion contract. No host floating-point oracle.",
               "cases": rows, "mismatches": sum(not row["agrees"] for row in rows)}
    (RESULTS / "integerization-inexact.json").write_text(json.dumps(summary, indent=2) + "\n")
    for original in ("20131017", "20250620"):
        assert sum(not row["agrees"] for row in rows if row["version"] == original) == 8
    assert all(row["agrees"] for row in rows if row["version"].startswith("audit-"))
    print(json.dumps({"runs": len(rows), "mismatches": summary["mismatches"],
                      "audit_correction_agrees": True}))


if __name__ == "__main__":
    main()
