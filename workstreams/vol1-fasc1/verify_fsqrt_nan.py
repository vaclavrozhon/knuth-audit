#!/usr/bin/env python3
"""Ten selected NaN/sign witnesses and controls; no simulator or enumeration.

Expected bits/events follow directly from MMIX's own documented contract.
No host floating-point operation is used. Run once with nice -n 15.
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

CASES = [
    ("negative-quiet-payload", "fff8000000000001", "fff8000000000001", 0),
    ("negative-quiet-canonical", "fff8000000000000", "fff8000000000000", 0),
    ("negative-signaling-payload", "fff0000000000001", "fff8000000000001", 0x1000),
    ("positive-quiet-control", "7ff8000000000001", "7ff8000000000001", 0),
    ("positive-signaling-control", "7ff0000000000001", "7ff8000000000001", 0x1000),
    ("negative-zero-control", "8000000000000000", "8000000000000000", 0),
    ("negative-infinity-control", "fff0000000000000", "fff8000000000000", 0x1000),
    ("negative-one-control", "bff0000000000000", "fff8000000000000", 0x1000),
    ("positive-four-control", "4010000000000000", "4000000000000000", 0),
    ("positive-infinity-control", "7ff0000000000000", "7ff0000000000000", 0),
]


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Use nice -n 15."
    env = dict(os.environ)
    env["CWEBINPUTS"] = str(SOURCES) + ":"
    rows, logs = [], []
    with tempfile.TemporaryDirectory(prefix="fsqrt-nan-build-", dir=RESULTS) as temporary:
        build = Path(temporary)
        shutil.copyfile(SOURCES / "fsqrt-nan-driver.c", build / "driver.c")
        for version, tag, change in (
            ("20131017", "20131017", "-"),
            ("20250620", "20250620", "-"),
            ("audit-fsqrt-nan-20250620", "20250620", str(SOURCES / "audit-fsqrt-nan.ch")),
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
            for name, raw, expected, flags in CASES:
                result = subprocess.run([str(build / "driver"), raw], text=True,
                                        capture_output=True, check=True)
                actual, actual_flags = result.stdout.split()
                actual_flags = int(actual_flags, 16)
                rows.append({"case": name, "version": version,
                             "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                             "input_bits": raw, "expected_bits": expected,
                             "actual_bits": actual, "expected_internal_flags": flags,
                             "actual_internal_flags": actual_flags,
                             "agrees": actual == expected and actual_flags == flags})
    (RESULTS / "fsqrt-nan-build.json").write_text(json.dumps(logs, indent=2) + "\n")
    summary = {"scope": "Ten selected FSQRT NaN/sign witnesses and controls in both original modules and one audit-only guard correction; Y=0, nearest rA mode, all arithmetic trips disabled.",
               "oracle": "Exact documented MMIX NaN propagation, invalid-operation and signed-zero rules; sqrt(4)=2. No host floating-point oracle.",
               "cases": rows, "mismatches": sum(not row["agrees"] for row in rows)}
    (RESULTS / "fsqrt-nan.json").write_text(json.dumps(summary, indent=2) + "\n")
    assert sum(not row["agrees"] for row in rows if row["version"] == "20131017") == 3
    assert sum(not row["agrees"] for row in rows if row["version"] == "20250620") == 3
    assert all(row["agrees"] for row in rows if row["version"].startswith("audit-"))
    print(json.dumps({"runs": len(rows), "mismatches": summary["mismatches"],
                      "audit_correction_agrees": True}))


if __name__ == "__main__":
    main()
