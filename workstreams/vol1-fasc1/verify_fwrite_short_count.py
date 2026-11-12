#!/usr/bin/env python3
"""Eleven focused Fwrite short-block/control cases, no broad I/O test suite.

The two original MMIX-IO releases are byte-identical, so compile their
common source only once. Compile the audit-only patch separately.
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

BASE = Path(__file__).resolve().parent
SOURCES, RESULTS = BASE / "sources", BASE / "results"
CASES = [
    ("one-byte-write-fails", 1, 2, "mock", [0]),
    ("short-first-small-block", 13, 2, "mock", [5]),
    ("short-full-block", 256, 2, "mock", [255]),
    ("failure-final-one-byte-block", 257, 2, "mock", [256, 0]),
    ("short-intermediate-block", 600, 2, "mock", [256, 23]),
    ("short-first-large-request", 600, 2, "mock", [128]),
    ("one-byte-success", 1, 2, "mock", []),
    ("three-block-success", 600, 2, "mock", []),
    ("zero-size-success", 0, 2, "mock", []),
    ("wrong-mode-rejects", 7, 1, "mock", []),
    ("real-stderr-dev-full", 1, 2, "real", []),
]


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Use nice -n 15."
    original = SOURCES / "mmix-io-20250620.w"
    assert original.read_bytes() == (SOURCES / "mmix-io-20131017.w").read_bytes()
    env = dict(os.environ)
    env["CWEBINPUTS"] = str(SOURCES) + ":"
    rows, logs = [], []
    result = dict(scope="Six mock short writes, four controls and one actual stderr/dev-full error for the common original module and audit-only correction. No flush-failure or broad I/O conformance claim.",
                  common_original_sha256=hashlib.sha256(original.read_bytes()).hexdigest(),
                  original_versions=["20131017", "20250620"], cases=rows)

    def checkpoint():
        (RESULTS / "fwrite-short-count-build.json").write_text(json.dumps(logs, indent=2) + "\n")
        (RESULTS / "fwrite-short-count.json").write_text(json.dumps(result, indent=2) + "\n")

    with tempfile.TemporaryDirectory(prefix="fwrite-audit-build-", dir=RESULTS) as temporary:
        build = Path(temporary)
        shutil.copyfile(SOURCES / "fwrite-short-count-driver.c", build / "driver.c")
        for version, change in [
            ("original-2013-and-2025-identical", "-"),
            ("audit-short-count", str(SOURCES / "audit-fwrite-short-count.ch")),
        ]:
            for command in [
                ["ctangle", str(original), change, "mmix-io.c"],
                ["gcc", "-O0", "-std=c11", "driver.c", "-o", "driver"],
            ]:
                process = subprocess.run(command, cwd=build, env=env, text=True,
                                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                logs.append(dict(version=version, command=command,
                                 returncode=process.returncode, output=process.stdout))
                checkpoint()
                process.check_returncode()
            for name, size, mode, host, responses in CASES:
                command = [str(build / "driver"), str(size), str(mode), host,
                           *map(str, responses)]
                if host == "real":
                    with open("/dev/full", "wb", buffering=0) as failure_stream:
                        process = subprocess.run(command, text=True, stdout=subprocess.PIPE,
                                                 stderr=failure_stream, check=True)
                else:
                    process = subprocess.run(command, text=True, capture_output=True, check=True)
                actual, expected, successful, calls, host_error, *trace = process.stdout.split()
                row = dict(case=name, version=version, requested_bytes=size, mode_code=mode,
                           host=host, host_short_results=responses, actual_bits=actual,
                           expected_bits=expected, host_successful_bytes=int(successful),
                           host_calls=int(calls),
                           host_error_flag=bool(int(host_error)) if host == "real" else None,
                           block_trace=[dict(requested=int(t.split(":")[0]),
                                             written=int(t.split(":")[1])) for t in trace],
                           agrees=actual == expected)
                if host == "real":
                    assert row["host_error_flag"] and row["host_successful_bytes"] == 0
                rows.append(row)
                checkpoint()
    assert sum(not r["agrees"] for r in rows if r["version"].startswith("original")) == 7
    assert all(r["agrees"] for r in rows if r["version"].startswith("audit"))
    print(json.dumps(dict(calls=len(rows), original_mismatches=7, audit_all_agree=True)))


if __name__ == "__main__":
    main()
