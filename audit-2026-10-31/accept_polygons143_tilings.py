"""Validate every saved model and compare complete, independently generated sets."""
from collections import Counter
from datetime import datetime, timezone
import gzip
import hashlib
import json
import re
import polygons143 as h


def read(path):
    return json.loads(path.read_text())


def main():
    out = h.OUT / "tilings"
    assert not (out / "accepted.json").exists(), "Do not repeat completed validation."
    old = read(out / "started.json")
    assert h.sha(h.__file__) == old["geometry_sha256"]
    assert h.sha(h.triangles.__file__) == old["triangles_sha256"]
    independent = read(out / "independent-terminal.json")
    assert independent["returncode"] == 0
    for key, name in [("input_sha256", "independent-input.txt"),
                      ("stdout_sha256", "independent-stdout.txt"),
                      ("stderr_sha256", "independent-stderr.log")]:
        assert h.sha(out / name) == independent[key]
    assert h.sha(independent["command"][2]) == independent["binary_sha256"]
    assert h.sha(h.ROOT / "count_vertices140.cpp") == independent["source_sha256"]
    assert h.sha(h.ROOT / "run_polygons143_followup.py") == independent["runner_sha256"]
    reference = {label: set() for label in ["shape1", "shape3", "shape5"]}
    counts, nodes = {}, {}
    for line in (out / "independent-stdout.txt").read_text().splitlines():
        fields = line.split()
        if fields[0] == "M":
            _, label, word = fields
            assert word not in reference[label]
            assert h.triangles.canonical_colors(word) == word
            reference[label].add(word)
        else:
            assert len(fields) == 4 and fields[0] == "C"
            _, label, number, visits = fields
            assert label not in counts
            counts[label], nodes[label] = int(number), int(visits)
    assert set(counts) == set(reference)
    assert (out / "independent-stderr.log").read_text().splitlines()[-1] == "ALL_COMPLETED 3"
    cases = {}
    first_strip = None
    for index in [0, 2, 4]:
        label = f"shape{index + 1}"
        cells = h.triangles.normalize_shape(h.simplex_graph(h.simplex_parameters(h.SIX24[index]))["cells"])
        enc = h.triangles.problem(cells)
        assert json.loads(json.dumps(enc)) == read(out / (label + "-encoding.json"))
        assert (out / (label + ".dlx")).read_text() == h.triangles.native_text(enc)
        vv = h.triangles.vertex_list(cells)
        for word in reference[label]:
            h.triangles.validate(cells, word)
        assert len(reference[label]) == counts[label]
        meta = read(out / (label + ".json"))
        assert meta["status"] == "completed" and meta["returncode"] == 0
        assert meta["model_output_period"] == 1
        for key, path in [("input_sha256", out / (label + ".dlx")),
                          ("stdout_sha256", out / (label + ".out.gz")),
                          ("stderr_sha256", out / (label + ".log")),
                          ("source_sha256", meta["source"]),
                          ("binary_sha256", meta["command"][2]),
                          ("runner_sha256", h.ROOT / "graph_native.py")]:
            assert h.sha(path) == meta[key]
        lookup = {}
        for row in enc["rows"]:
            pos, tile, *colors = row
            values = {int(s.split(":")[0][1:]): s.split(":")[1] for s in colors}
            lookup[tuple(sorted(row))] = (pos, tile, values)
        assert len(lookup) == 1536
        models, frequency = set(), Counter()
        places, tiles, coloring = set(), set(), {}
        begun = False
        output_hash = hashlib.sha256()

        def finish():
            nonlocal first_strip
            assert len(places) == len(tiles) == 24 and len(coloring) == len(vv)
            word = "".join(coloring[i] for i in range(len(vv)))
            assert word not in models
            h.triangles.validate(cells, word)
            models.add(word)
            frequency[h.triangles.canonical_colors(word)] += 1
            if label == "shape3" and first_strip is None:
                first_strip = word

        with gzip.open(out / (label + ".out.gz"), "rb") as inp:
            for raw in inp:
                output_hash.update(raw)
                line = raw.decode().strip()
                if re.fullmatch(r"\d+:", line):
                    if begun:
                        finish()
                    assert int(line[:-1]) == len(models) + 1
                    begun = True
                    places, tiles, coloring = set(), set(), {}
                elif line:
                    assert begun
                    tokens = re.sub(r"\s*\(\d+ of \d+\)\s*$", "", line).split()
                    pos, tile, values = lookup[tuple(sorted(tokens))]
                    assert pos not in places and tile not in tiles
                    places.add(pos)
                    tiles.add(tile)
                    for v, c in values.items():
                        assert v not in coloring or coloring[v] == c
                        coloring[v] = c
        if begun:
            finish()
        assert output_hash.hexdigest() == meta["raw_stdout_sha256"]
        assert len(models) == meta["solutions"] == 24 * counts[label]
        assert set(frequency) == reference[label]
        assert all(n == 24 for n in frequency.values())
        assert int(re.search(r"Altogether (\d+) solutions?", (out / (label + ".log")).read_text()).group(1)) == len(models)
        canonical = out / (label + "-color-classes.txt.gz")
        with gzip.open(canonical, "wt") as fout:
            fout.write("".join(word + "\n" for word in sorted(reference[label])))
        cases[label] = dict(parameters=h.SIX24[index], native_models=len(models),
            color_classes=counts[label], native_nodes=meta["nodes"], independent_nodes=nodes[label],
            all_native_and_independent_models_valid=True, complete_sets_equal=True,
            each_color_class_has_24_labeled_models=True,
            native_terminal_sha256=h.sha(out / (label + ".json")),
            color_classes_sha256=h.sha(canonical), native_net_search_mems=meta["net_search_mems"])
        print("PASS", label, len(models), "labeled models;", counts[label], "equal color classes", flush=True)
    assert first_strip == read(h.OUT / "first-strip-witness.json")["unrotated_vertex_word"]
    h.save(out / "accepted.json", dict(at_utc=datetime.now(timezone.utc).isoformat(),
        checker_sha256=h.sha(__file__), geometry_sha256=h.sha(h.__file__),
        triangles_sha256=h.sha(h.triangles.__file__),
        independent_terminal_sha256=h.sha(out / "independent-terminal.json"), cases=cases,
        scope="Two complete independent enumerations. Shape3 is a counterexample to the claimed impossibility; shape1 and shape5 are untileable."))


if __name__ == "__main__":
    main()
