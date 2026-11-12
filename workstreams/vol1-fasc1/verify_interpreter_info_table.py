"""One finite reconciliation of all Info entries and the printed excerpt.

The independent family specification is explained in recovery-pages-087-097.md.
This reads existing sources/certificates; it does not assemble or run MMIX.
"""
from pathlib import Path
import hashlib
import json
import re

B = Path(__file__).resolve().parent


def compact(s):
    return re.sub(r"\s+", " ", s.strip())


def info_spec(op, name):
    """Host instruction, special input and flags, from architectural roles."""
    if op == 0:
        return "JMP Trap+@-O", "0", 0x0A
    if op in (5, 7, 0x15, 0x17):
        return f"{name} x,0,z", "0", 0x26
    if 8 <= op <= 15:
        base = name[:-1] if op & 1 else name
        return f"{base} x,0,z", "0", 0x25 if op & 1 else 0x26
    if op < 0x18:
        special = "rE" if op in (0x11, 0x12, 0x13) else "0"
        return f"{name} x,y,z", special, 0x2A
    if op < 0x40:
        flag = 0x29 if op & 1 else 0x2A
        base = name[:-1] if op & 1 else name
        if 0x1A <= op <= 0x1F:
            helper = "MulU" if op < 0x1C else "Div" if op < 0x1E else "DivU"
            return f"JMP {helper}+@-O", "rD" if op >= 0x1E else "0", flag
        if 0x34 <= op <= 0x37:
            return f"{base} x,0,z", "0", 0x25 if op & 1 else 0x26
        return f"{base} x,y,z", "0", flag
    if op < 0x60:
        base = name[:-1] if op & 1 else name
        helper = "BTaken" if op < 0x50 else "PBTaken"
        return f"{base} x,{helper}+@-O", "0", 0x50
    if op < 0x80:
        base = name[:-1] if op & 1 else name
        flag = (0x3A if op < 0x70 else 0x2A) - (op & 1)
        return f"{base} x,y,z", "0", flag
    if op < 0xC0:
        base = name[:-1] if op & 1 else name
        if op in (0x94, 0x95):
            return "JMP Cswap+@-O", "0", 0xBA - (op & 1)
        if op in (0x98, 0x99):
            return "JMP Error+@-O", "0", 0x2A - (op & 1)
        if op in (0x9A, 0x9B, 0x9C, 0x9D, 0xB8, 0xB9, 0xBA, 0xBB, 0xBC, 0xBD):
            return "SWYM 0", "0", 0x0A - (op & 1)
        if op in (0x9E, 0x9F, 0xBE, 0xBF):
            helper = "Go" if op < 0xA0 else "PushGo"
            return f"JMP {helper}+@-O", "0", 0x2A - (op & 1)
        if op in (0xB4, 0xB5):
            return "STO xx,res,0", "0", 0x8A - (op & 1)
        return f"{base} x,res,0", "0", (0xAA if op < 0xA0 else 0x9A) - (op & 1)
    if op < 0xE0:
        base = name[:-1] if op & 1 else name
        return f"{base} x,y,z", "rM" if op in (0xD8, 0xD9) else "0", 0x2A - (op & 1)
    if op < 0xF0:
        if op < 0xE4:
            return "SET x,z", "0", 0x20
        base = "ADDU" if op < 0xE8 else "OR" if op < 0xEC else "ANDN"
        return f"{base} x,x,z", "0", 0x30
    if op < 0xF2:
        return "SET inst_ptr,yz", "0", 0x41
    if op < 0xF4:
        return "JMP PushJ+@-O", "0", 0x60
    if op < 0xF6:
        return "SET x,yz", "0", 0x60
    tail = {
        0xF6: ("JMP Put+@-O", "0", 2),
        0xF7: ("JMP Put+@-O", "0", 1),
        0xF8: ("JMP Pop+@-O", "rJ", 0),
        0xF9: ("JMP Resume+@-O", "0", 0),
        0xFA: ("JMP Save+@-O", "0", 0x20),
        0xFB: ("JMP Unsave+@-O", "0", 2),
        0xFC: ("JMP Sync+@-O", "0", 1),
        0xFD: ("SWYM x,y,z", "0", 0),
        0xFE: ("JMP Get+@-O", "0", 0x20),
        0xFF: ("JMP Trip+@-O", "0", 0x0A),
    }
    return tail[op]


def main():
    source = B / "sources/sim-20250620.mms"
    pattern = re.compile(r"^\s*(.+?);\s*BYTE\s+(\d+),(\d+),([^,]+),#([0-9a-fA-F]+)\s+(\S+)\s*$", re.M)
    raw = pattern.findall(source.read_text())
    assert len(raw) == 256
    costs = json.loads((B / "results/opcode-table-reconciliation.json").read_text())["tables"][0]["entries"]
    assert len(costs) == 256
    rows = []
    for op, (host, mem, ops, special, flags, name) in enumerate(raw):
        c = costs[op]
        assert int(c["opcode"], 16) == op and c["name"] == name
        expected = info_spec(op, name)
        actual = (compact(host), special.strip(), int(flags, 16))
        assert actual == expected, (op, actual, expected)
        # Info starts a probable branch at3 and subtracts2 when taken;
        # the earlier architectural certificate starts at1 plus a miss penalty.
        info_oops = c["source_base_oops"] + (2 if 0x50 <= op <= 0x5F else 0)
        assert (int(mem), int(ops)) == (c["source_mems"], info_oops), (op, "cost")
        rows.append({"opcode": f"{op:02x}", "name": name, "host_instruction": actual[0], "mems": int(mem), "oops": int(ops), "special_source": actual[1], "flags": f"{actual[2]:02x}", "family_roles_agree": True, "accepted_cost_agrees": True})
    by_name = {r["name"]: r for r in rows}
    printed = B / "sources/file-096-targeted.txt"
    pp = re.compile(r"([A-Z][A-Z0-9]*[ \t]+[^;\n]+?);\s*BYTE\s+(\d+),(\d+),([^,\s]+),#([0-9a-fA-F]+)\s*\(([A-Z0-9]+)\)")
    found = pp.findall(printed.read_text())
    assert len(found) > 80
    printed_rows = []
    for host, mem, ops, special, flags, name in found:
        r = by_name[name]
        # The first two rows also contain the independent left-column heading.
        host = host.removeprefix("O IS Done-4").removeprefix("LOC Info").strip()
        actual = (compact(host), int(mem), int(ops), special, flags.lower())
        expected = (r["host_instruction"], r["mems"], r["oops"], r["special_source"], r["flags"])
        assert actual == expected, (name, actual, expected)
        printed_rows.append({"name": name, "all_fields_agree": True})
    result = {
        "scope": "Every one of256 symbolic Info entries compared with independent semantic-family roles and already accepted architectural costs; every explicitly printed entry compared with source. This is not a full simulator execution or a proof of its handlers.",
        "proof": "notes/recovery-pages-087-097.md",
        "source": "sources/sim-20250620.mms",
        "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "printed_source": "sources/file-096-targeted.txt",
        "printed_source_sha256": hashlib.sha256(printed.read_bytes()).hexdigest(),
        "entries": rows,
        "printed_entries": printed_rows,
        "printed_entry_count": len(printed_rows),
        "new_program_execution": False,
        "old_run_repeated": False,
        "cost_convention": "Probable branches use Info3 minus2 when taken, versus the accepted architectural base1 plus2 when not taken; ordinary branches use1 plus2 when taken.",
        "differences": [],
    }
    (B / "results/interpreter-info-table-reconciliation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"entries": len(rows), "printed_entries": len(printed_rows), "differences": 0}))


if __name__ == "__main__":
    main()
