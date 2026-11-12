#!/usr/bin/env python3
"""First targeted scan_const boundary run; no old verifier or simulator.

Use nice -n15. An integer/Fraction oracle is independent of MMIXware and
does not use the host's floating parser. The original sources are unchanged.
Successful saved output is guarded against an accidental repeat.
"""
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import time

BASE = Path(__file__).resolve().parent
SOURCES = BASE / "sources"
RESULTS = BASE / "results"


def nearest_integer(x):
    q, r = divmod(x.numerator, x.denominator)
    return q + (2*r > x.denominator or (2*r == x.denominator and q % 2))


def binary64(x):
    """Exact nearest-even rounding, including zero/subnormal/overflow."""
    x = Fraction(x)
    sign = int(x < 0) << 63
    x = abs(x)
    if not x:
        return f"{sign:016x}"
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < Fraction(2) ** e:
        e -= 1
    if e < -1022:
        m = nearest_integer(x * Fraction(2) ** 1074)
        return f"{sign | m:016x}"
    m = nearest_integer(x * Fraction(2) ** (52-e))
    if m == 1 << 53:
        m >>= 1
        e += 1
    if e > 1023:
        return f"{sign | (2047 << 52):016x}"
    return f"{sign | ((e+1023) << 52) | (m-(1 << 52)):016x}"


def cases():
    out = []
    def add(name, text, exact, expression, kind=1):
        out.append(dict(name=name, text=text, exact=str(exact),
                        input_expression=expression, expected_kind=kind,
                        expected_hex=binary64(exact) if kind else f"{int(exact) % (1<<64):016x}"))
    add("last-fitting-integer", "1" + "0"*768 + "e-768", 1,
        "'1' + '0'*768 + 'e-768'")
    add("first-omitted-integer-digit", "1" + "0"*769 + "e-769", 1,
        "'1' + '0'*769 + 'e-769'")
    add("negative-first-boundary", "-1" + "0"*769 + "e-769", -1,
        "'-1' + '0'*769 + 'e-769'")
    add("explicit-point", "1" + "0"*769 + ".e-769", 1,
        "'1' + '0'*769 + '.e-769'")
    add("two-omitted-digits", "1" + "0"*770 + "e-770", 1,
        "'1' + '0'*770 + 'e-770'")
    add("231-omitted-digits", "1" + "0"*999 + "e-999", 1,
        "'1' + '0'*999 + 'e-999'")
    add("multi-digit-prefix", "12345" + "0"*769 + "e-769", 12345,
        "'12345' + '0'*769 + 'e-769'")
    add("fraction-sticky-after-full-integer", "1" + "0"*769 + ".5e-769",
        Fraction(1) + Fraction(5, 10**770), "'1' + '0'*769 + '.5e-769'")
    add("long-integer-modulo-unchanged", "1" + "0"*769 + "7", 7,
        "'1' + '0'*769 + '7'", kind=0)
    add("leading-zero-control", "0"*800 + "1.0", 1,
        "'0'*800 + '1.0'")
    add("fraction-only-control", "." + "0"*769 + "1e770", 1,
        "'.' + '0'*769 + '1e770'")
    add("ordinary-inexact-control", "0.1", Fraction(1,10), "'0.1'")
    return out


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Run with nice -n15."
    destination = RESULTS / "scan-constant-integer-length.json"
    assert not destination.exists(), "Saved successful results exist; do not rerun."
    started = time.monotonic()
    logs, outputs = [], []
    env = dict(os.environ, CWEBINPUTS=str(SOURCES)+":")
    inventory = cases()
    with tempfile.TemporaryDirectory(prefix="mmix-scan-length-", dir=RESULTS) as temporary:
        build = Path(temporary)
        shutil.copyfile(SOURCES / "scan-constant-integer-length-driver.c", build / "driver.c")
        for version, tag, change in (
            ("20131017", "20131017", "-"),
            ("20250620", "20250620", "-"),
            ("audit-corrected-20250620", "20250620", str(SOURCES / "audit-scan-constant-integer-length.ch")),
        ):
            source = SOURCES / f"mmix-arith-{tag}.w"
            for command in (["ctangle", str(source), change, "mmix-arith.c"],
                            ["gcc", "-O0", "-std=c11", "driver.c", "-o", "driver"]):
                result = subprocess.run(command, cwd=build, env=env, text=True,
                                        capture_output=True, timeout=20)
                logs.append(dict(version=version, command=command,
                                 returncode=result.returncode, stdout=result.stdout, stderr=result.stderr))
                result.check_returncode()
            for case in inventory:
                run = subprocess.run([str(build / "driver"), case["text"]],
                                     text=True, capture_output=True, check=True, timeout=5)
                kind, raw, consumed = run.stdout.split()
                outputs.append(dict(version=version, case=case["name"],
                                    actual_kind=int(kind), actual_hex=raw, consumed=int(consumed),
                                    expected_hex=case["expected_hex"], expected_kind=case["expected_kind"],
                                    input_length=len(case["text"]),
                                    agrees=(raw == case["expected_hex"] and int(kind) == case["expected_kind"]
                                            and int(consumed) == len(case["text"]))))
    fixed = [r for r in outputs if r["version"].startswith("audit-")]
    assert all(r["agrees"] for r in fixed), fixed
    assert all(r["consumed"] == r["input_length"] for r in outputs)
    expected_failures = {"first-omitted-integer-digit", "negative-first-boundary", "explicit-point",
                         "two-omitted-digits", "231-omitted-digits", "multi-digit-prefix",
                         "fraction-sticky-after-full-integer"}
    for tag in ("20131017", "20250620"):
        assert {r["case"] for r in outputs if r["version"] == tag and not r["agrees"]} == expected_failures
    saved_cases = [{**{k:v for k,v in c.items() if k != "text"},
                    "input_length":len(c["text"]),
                    "input_sha256":hashlib.sha256(c["text"].encode()).hexdigest()} for c in inventory]
    record = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  scope="Twelve new exact boundary/control inputs against two original versions and one local audit correction; no simulator or previous test run.",
                  oracle="Exact integers and Fraction nearest-even binary64 packing; no host floating parsing.",
                  elapsed_seconds=time.monotonic()-started, priority=os.getpriority(os.PRIO_PROCESS,0),
                  sources={tag:hashlib.sha256((SOURCES/f'mmix-arith-{tag}.w').read_bytes()).hexdigest()
                           for tag in ('20131017','20250620')},
                  cases=saved_cases, runs=outputs, total_runs=len(outputs),
                  original_mismatches=sum(not r['agrees'] for r in outputs if not r['version'].startswith('audit-')),
                  audit_corrected_all_agree=True)
    (RESULTS/'scan-constant-integer-length-build.json').write_text(json.dumps(logs,indent=2)+'\n')
    destination.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('total_runs','original_mismatches','audit_corrected_all_agree','elapsed_seconds')}))


if __name__ == "__main__":
    main()
