"""First bounded execution of the new complete RESUME audit repair.

Inputs are independent binary images in exercise20's format. No old C0015
witness or SAVE inverse is executed. Each new case runs exactly once.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import shutil
import struct
import subprocess
import tarfile
import tempfile
import time

B = Path(__file__).resolve().parent
R = B / "results"
S = B / "sources"
MASK = (1 << 64) - 1
D = 1 << 61
STACK = 3 << 61


def instruction(op, x=0, y=0, z=0):
    return (op << 24) | (x << 16) | (y << 8) | z


def cases():
    # Expected results are direct integer/bit/rounding derivations in the proof.
    normal = [
        ("binary-addu", 0x22, 123, 456, 579, 0, 77, 33),
        ("neg-large-y", 0x34, 1000, 3, 997, 0, 77, 33),
        ("neg-overflow", 0x35, (1 << 63)-1, MASK, 1 << 63, 0x40, 77, 33),
        ("negu", 0x37, 0, 1, MASK, 0, 77, 33),
        ("sfloti-round-off", 0x0D, 1, (1 << 24)+3, 0x4170000020000000, 1, 77, 33),
        ("sflotui-round-near", 0x0F, 4, (1 << 24)+1, 0x4170000000000000, 1, 77, 33),
        ("sqrt-round-current", 0x15, 0, 0x4010000000000000, 0x4000000000000000, 0, 77, 33),
        ("incml", 0xE6, 5, 9, 14, 0, 77, 33),
        ("orh", 0xE8, 0x55, 0xAA, 0xFF, 0, 77, 33),
        ("andnl", 0xEF, 0xFF, 0x0F, 0xF0, 0, 77, 33),
        ("seth", 0xE0, 88, 0x12345678, 0x12345678, 0, 77, 33),
        ("csz-false-zero-third", 0x62, 1, 9, 0, 0, 77, 33),
        ("csz-true", 0x63, 0, 9, 9, 0, 77, 33),
        ("mux-zero-third", 0xD8, 5, 9, 9, 0, 77, 33),
        ("divu-zero-third", 0x1E, 10, 3, 3, 0, 1, 33),
        ("epsilon-zero-third", 0x13, 0x3FF0000000000000, 0x3FF0000000000001, 0, 0, 77, 33),
        ("mulu-high", 0x1A, 1 << 63, 2, 0, 0, 77, 1),
    ]
    out = []
    for name, op, ry, rz, x, a, rem, high in normal:
        out.append(dict(name=name, rx=(1 << 56) | instruction(op, 0xF0, 0xF7, 0xF8), ry=ry, rz=rz, expected=[x, a, rem, high]))
    out.extend([
        dict(name="rop0-ordinary-operands", rx=instruction(0x22, 0xF0, 0xF7, 0xF8), ry=100, rz=200, expected=[42, 0, 77, 33]),
        dict(name="negative-rx", rx=(1 << 63) | instruction(0xF9), ry=100, rz=200, expected=[99, 0, 77, 33]),
        dict(name="rop2-events", rx=(2 << 56) | (0x40 << 40) | instruction(0x22, 0xF0, 0xF7, 0xF8), ry=100, rz=333, expected=[333, 0x40, 77, 33]),
        dict(name="rop2-resume-marker", rx=(2 << 56) | instruction(0xF9, 0xF0, 0xF7, 0xF8), ry=100, rz=444, expected=[444, 0, 77, 33]),
        dict(name="reject-rop3", rx=(3 << 56) | instruction(0x22, 0xF0), ry=1, rz=2, expected=None),
        dict(name="reject-rop1-load", rx=(1 << 56) | instruction(0x80, 0xF0), ry=1, rz=2, expected=None),
        dict(name="reject-rop1-marginal", rx=(1 << 56) | instruction(0x22, 2), ry=1, rz=2, expected=None),
        dict(name="reject-rop2-marginal", rx=(2 << 56) | instruction(0x22, 2), ry=1, rz=2, expected=None),
        dict(name="reject-rop0-resume", rx=instruction(0xF9), ry=1, rz=2, expected=None),
        dict(name="reject-saved-rounding", rx=(1 << 56) | instruction(0x15, 0xF0), ry=5, rz=0x4010000000000000, expected=None),
    ])
    return out


def image(case):
    code = [instruction(0xF6, reg, 0, src) for reg, src in [(21, 0xF9), (26, 0xF1), (27, 0xF2), (25, 0xF3), (24, 0xF4)]]
    code.append(instruction(0xF9))
    after = 0x100 + 4 * len(code)
    code.append(instruction(0xAF, 0xF0, 0xF5, 0))
    for special, offset in [(21, 8), (6, 16), (3, 24)]:
        code += [instruction(0xFE, 0xF8, 0, special), instruction(0xAF, 0xF8, 0xF5, offset)]
    code += [instruction(0xC1, 255, 0xF6, 0), instruction(0, 0, 6, 1), 0]
    if len(code) & 1:
        code.append(0)
    words = {0x100 + 4*i: (code[i] << 32) | code[i+1] for i in range(0, len(code), 2)}
    words[D + 0x100], words[D + 0x108] = D, 32
    globals_ = {0xF0: 99, 0xF1: case["ry"], 0xF2: case["rz"], 0xF3: case["rx"], 0xF4: after, 0xF5: D, 0xF6: D+0x100, 0xF7: 40, 0xF8: 2, 0xF9: 0, 255: 0x100}
    specials = {1: 7, 2: 0x3FE0000000000000, 3: 33, 5: MASK, 6: 77}
    context = [99, 1]  # L=1 local0 and its marker.
    context += [globals_.get(k, 0) for k in range(240, 256)]
    context += [specials.get(k, 0) for k in list(range(7)) + list(range(23, 28))]
    context += [240 << 56]
    words.update({STACK+8*i: value for i, value in enumerate(context)})
    # All unspecified bytes are zero. Only nonzero octabytes need file groups.
    raw = bytearray()
    previous = None
    for loc, value in sorted(words.items()):
        if not value:
            continue
        if previous is None or loc != previous+8:
            if previous is not None:
                raw += struct.pack(">Q", 0)
            raw += struct.pack(">Q", loc)
        raw += struct.pack(">Q", value & MASK)
        previous = loc
    raw += struct.pack(">Q", 0)
    assert previous == STACK+8*(len(context)-1)
    return bytes(raw)


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Run with nice -n15"
    result = dict(checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), scope="First bounded executions of the new full RESUME audit repair. Independent valid images; no old C0015 witness, arithmetic census or SAVE inverse rerun.", cases=[])
    logs = []
    start = time.monotonic()
    def save():
        (R / "resume-recovery-build-and-run.json").write_text(json.dumps(logs, indent=2)+"\n")
        (R / "resume-recovery-native.json").write_text(json.dumps(result, indent=2)+"\n")
    def run(cmd, cwd, timeout=20):
        tick = time.monotonic()
        p = subprocess.run(cmd, cwd=cwd, capture_output=True, timeout=timeout)
        logs.append(dict(command=cmd, returncode=p.returncode, stdout_hex=p.stdout.hex(), stderr=p.stderr.decode(errors="replace"), elapsed_seconds=time.monotonic()-tick))
        save()
        return p
    with tempfile.TemporaryDirectory(prefix="resume-recovery-first-", dir=R) as tmp:
        build = Path(tmp)
        with tarfile.open(S / "mmix-20250620.tar.gz") as archive:
            for name in ["Makefile", "mmixal.w", "mmix-arith.w", "mmix-io.w", "mmix-sim.w", "abstime.w", "boilerplate.w"]:
                (build/name).write_bytes(archive.extractfile(name).read())
        p = run(["make", "basic", "CFLAGS=-O0"], build)
        assert p.returncode == 0, logs[-1]
        source = S / "sim-resume-audit-fixed.mms"
        shutil.copyfile(source, build/source.name)
        p = run([str(build/"mmixal"), "-l", "sim.lst", "-o", "sim.mmo", source.name], build)
        (R / "resume-recovery-sim-listing.txt").write_bytes((build/"sim.lst").read_bytes())
        assert p.returncode == 0, logs[-1]
        result["source_sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
        result["object_sha256"] = hashlib.sha256((build/"sim.mmo").read_bytes()).hexdigest()
        for case in cases():
            data = image(case)
            name = "resume-"+case["name"]+".mmb"
            (S/name).write_bytes(data)
            shutil.copyfile(S/name, build/name)
            expected = b"" if case["expected"] is None else b"".join(struct.pack(">Q", x & MASK) for x in case["expected"])
            # Unchanged sim.mms SimHalt produces255 on normal exit; Error is234.
            # Exit status is transport evidence, not the virtual result oracle.
            expected_status = 234 if case["expected"] is None else 255
            p = run([str(build/"mmix"), "-q", "sim.mmo", name], build)
            record = dict(case, source="sources/"+name, image_sha256=hashlib.sha256(data).hexdigest(), expected_bytes_hex=expected.hex(), actual_bytes_hex=p.stdout.hex(), expected_host_status=expected_status, host_status=p.returncode, stderr=p.stderr.decode(errors="replace"), agrees=(p.stdout==expected and p.returncode==expected_status and not p.stderr))
            result["cases"].append(record)
            save()
            assert record["agrees"], record
    result["elapsed_seconds"] = time.monotonic()-start
    result["all_agree"] = True
    result["old_run_repeated"] = False
    save()
    print(json.dumps({"cases": len(result["cases"]), "all_agree": True, "elapsed_seconds": result["elapsed_seconds"]}))


if __name__ == "__main__":
    main()
