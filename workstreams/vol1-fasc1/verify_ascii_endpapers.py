#!/usr/bin/env python3
"""Reconcile every ASCII endpaper cell with the primary Latin-1 mapping.

The original images were inspected separately. The typeset apostrophe and
grave glyphs extract as curly quotes; their identity is recorded explicitly.
"""
from pathlib import Path
import hashlib
import json
import os
import re

BASE = Path(__file__).resolve().parent


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Use nice -n 15."
    source = BASE / "sources/unicode-8859-1.txt"
    mapping = {}
    for line in source.read_text().splitlines():
        match = re.match(r"0x([0-9A-F]+)\s+0x([0-9A-F]+)\s+#\s+(.*)", line)
        if match:
            byte, codepoint, name = match.groups()
            mapping[int(byte, 16)] = (int(codepoint, 16), name)
    tables = []
    for page in [144, 145]:
        path = BASE / f"sources/file-{page:03}.txt"
        text = path.read_text().split("MMIX OPERATION CODES", 1)[0]
        rows = re.findall(r"^#\s+([2-7])x\s+(.*?)\s+#\s+\1x\s*$", text, re.M)
        assert [int(row[0]) for row in rows] == list(range(2, 8))
        entries = []
        for high, glyphs in rows:
            high = int(high)
            chars = glyphs.split()
            if high == 2:
                chars.insert(0, " ")
            if high == 7:
                chars.append(None)  # gray square: nonprinting DEL in image
            assert len(chars) == 16, (page, high, chars)
            for low, glyph in enumerate(chars):
                byte = 16 * high + low
                codepoint, name = mapping[byte]
                if byte == 0x7f:
                    assert glyph is None and name == "DELETE"
                    normalized = None
                else:
                    normalized = {0x27: "'", 0x60: "`"}.get(byte, glyph)
                    if byte == 0x27:
                        assert glyph == "’"
                    if byte == 0x60:
                        assert glyph == "‘"
                    assert normalized == chr(codepoint), (page, byte, glyph)
                entries.append(dict(byte=f"{byte:02x}", extracted_glyph=glyph,
                                    character=normalized, primary_name=name,
                                    agrees=True))
        tables.append(dict(file_page=page, entries=entries,
                           native_source_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    result = {
        "scope": "All 95 printing ASCII positions and the nonprinting DEL position, in both endpapers. Original images inspected; curly extraction at 27/60 is a typeface-glyph issue, not an assertion of Unicode U+2018/U+2019 byte encodings.",
        "primary_source": str(source.relative_to(BASE)),
        "primary_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "tables": tables,
    }
    (BASE / "results/ascii-endpaper-reconciliation.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"tables": len(tables), "printing_cells_per_table": 95,
                      "nonprinting_cells_per_table": 1, "differences": 0}))


if __name__ == "__main__":
    main()
