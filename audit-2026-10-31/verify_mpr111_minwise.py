#!/usr/bin/env python3
"""One bounded certificate for the 60 printed permutations and PDF table.

All 63 nonempty subsets are traversed once. No family search, optimization,
sampling, previous-run restart, or enumeration of the 720 possible permutations.
Run from repository root with nice -n 15.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations
import json
import os
from pathlib import Path
from time import perf_counter
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parent
START = perf_counter()
SEEDS = "123456 126345 152346 152634 164235 154263 165324 164523 156342 165432".split()
PRINTED = """134 163 123 126 142 142 153 145 163 154 245 234 534 563 623 526 632 652 534 643
356 645 246 234 435 463 524 423 642 532 461 351 361 641 251 231 341 531 321 421
512 412 415 315 316 615 216 216 415 316 623 526 652 452 564 354 465 364 256 265""".split()
assert len(SEEDS) == len(set(SEEDS)) == 10
assert all(sorted(s) == list("123456") and s[0] == "1" for s in SEEDS)
FAMILY = [s[r:] + s[:r] for r in range(6) for s in SEEDS]
assert len(FAMILY) == len(set(FAMILY)) == 60

source = BASE / "sources/mpr111-page407.xml"
texts = ET.parse(source).getroot().findall(".//text")
glyph_rows = []
for tops in [(287, 292), (303, 309), (320, 325)]:
    parts = sorted((e for e in texts if int(e.attrib["top"]) in tops),
                   key=lambda e: int(e.attrib["left"]))
    glyphs = []
    for e in parts:
        assert e.attrib["font"] in {"3", "9"}
        for char in "".join(e.itertext()):
            assert char in "123456 "
            if char != " ":
                glyphs.append((char, e.attrib["font"] == "9"))
    assert len(glyphs) == 60
    glyph_rows.append(glyphs)

table = []
for i, permutation in enumerate(FAMILY):
    triple = "".join(permutation[j - 1] for j in [1, 3, 4])
    glyphs = glyph_rows[i // 20][3 * (i % 20):3 * (i % 20) + 3]
    extracted = "".join(c for c, bold in glyphs)
    bold_positions = [j + 1 for j, (c, bold) in enumerate(glyphs) if bold]
    minimum_position = triple.index(min(triple)) + 1
    assert triple == PRINTED[i] == extracted
    assert bold_positions == [minimum_position]
    table.append({"row": i // 20 + 1, "column": i % 20 + 1,
                  "shift": i // 10, "seed": SEEDS[i % 10],
                  "permutation": permutation, "triple": triple,
                  "bold_minimum_position": minimum_position,
                  "winning_original_element": [1, 3, 4][minimum_position - 1]})

subsets = []
for size in range(1, 7):
    for subset in combinations(range(1, 7), size):
        winners = Counter(min(subset, key=lambda a: p[a - 1]) for p in FAMILY)
        assert set(winners) == set(subset)
        assert all(winners[a] == 60 // size for a in subset)
        subsets.append({"subset": list(subset), "size": size,
                        "winning_counts": dict(sorted(winners.items())),
                        "required_count_per_element": 60 // size})
assert len(subsets) == 63
assert sum(x["size"] for x in subsets) == 192
target = next(x for x in subsets if x["subset"] == [1, 3, 4])
assert target["winning_counts"] == {1: 20, 3: 20, 4: 20}

result = {
    "at_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Exact specified 60-element family; all nonempty subsets; all 60 table triples and bold minima",
    "nice": os.getpriority(os.PRIO_PROCESS, 0),
    "seconds": perf_counter() - START,
    "family_size": len(FAMILY), "nonempty_subsets": len(subsets),
    "subset_member_conditions": 192, "minimum_evaluations": 3780,
    "source_xml_sha256": sha256(source.read_bytes()).hexdigest(),
    "pdf_bold_font": "font9 T26; visually matched against the rendered original; ordinary digits font3 T6",
    "all_checks_passed": True, "table": table, "subsets": subsets,
}
assert result["nice"] >= 15
destination = BASE / "results/sequential/mpr-111-minwise-certificate.json"
assert not destination.exists(), "Preserve an existing successful certificate; do not rerun."
destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k not in {"table", "subsets"}}, ensure_ascii=False))
