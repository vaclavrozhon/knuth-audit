"""Continue after the book's false zero-count claim; never repeat completed cases."""
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import subprocess
import polygons143 as h
import graph_native as native


def read(path):
    return json.loads(path.read_text())


def main():
    out = h.OUT / "tilings"
    assert not (out / "followup-started.json").exists()
    old = read(out / "started.json")
    assert h.sha(h.ROOT / "check_polygons143_tilings.py") == old["checker_sha256"]
    assert h.sha(h.__file__) == old["geometry_sha256"]
    assert h.sha(h.triangles.__file__) == old["triangles_sha256"]
    previous = {}
    for label, count in [("shape1", 0), ("shape3", 206472)]:
        meta = read(out / (label + ".json"))
        assert meta["status"] == "completed" and meta["returncode"] == 0
        assert meta["solutions"] == count
        assert h.sha(out / (label + ".out.gz")) == meta["stdout_sha256"]
        previous[label] = h.sha(out / (label + ".json"))
    assert not (out / "shape5-run.json").exists()
    assert not (out / "independent-terminal.json").exists()
    h.save(out / "followup-started.json", dict(at_utc=datetime.now(timezone.utc).isoformat(),
        wrapper_pid=os.getpid(), checker_sha256=h.sha(__file__), previous_terminals=previous,
        reason="Original wrapper stopped on its false expected-zero assertion. Both native searches completed successfully; reuse them."))
    source = Path(meta["source"])
    binary = Path(meta["command"][2])
    assert h.sha(source) == meta["source_sha256"]
    assert h.sha(binary) == meta["binary_sha256"]
    native.OUT = out
    cells = h.triangles.normalize_shape(h.simplex_graph(h.simplex_parameters(h.SIX24[4]))["cells"])
    enc = h.triangles.problem(cells)
    h.save(out / "shape5-encoding.json", enc)
    result = native.run("shape5", h.triangles.native_text(enc), binary=binary, source=source,
                        every=1, limit=172800)
    assert result["status"] == "completed" and result["returncode"] == 0
    print("NATIVE shape5", result["solutions"], flush=True)
    build = read(h.ROOT / "results/vertices140/independent-fixed/build.json")
    independent = Path(build["binary"])
    assert h.sha(independent) == build["binary_sha256"]
    assert h.sha(h.ROOT / "count_vertices140.cpp") == build["source_sha256"]
    lines = []
    for index in [0, 2, 4]:
        cells = read(out / (f"shape{index + 1}-encoding.json"))["cells"]
        vv = h.triangles.vertex_list(cells)
        idx = {v: i for i, v in enumerate(vv)}
        lines.append(f"shape{index + 1} {len(vv)}")
        lines.extend(" ".join(str(idx[v]) for v in h.triangles.vertices(t)) for t in cells)
    inp = out / "independent-input.txt"
    inp.write_text("\n".join(lines) + "\n")
    command = ["timeout", "172800", str(independent)]
    started = dict(at_utc=datetime.now(timezone.utc).isoformat(), wrapper_pid=os.getpid(),
        command=command, binary_sha256=h.sha(independent), source_sha256=build["source_sha256"],
        input_sha256=h.sha(inp), runner_sha256=h.sha(__file__))
    with inp.open("rb") as fin, (out / "independent-stdout.txt").open("xb") as fout, (out / "independent-stderr.log").open("xb") as ferr:
        proc = subprocess.Popen(command, stdin=fin, stdout=fout, stderr=ferr)
        started["pid"] = proc.pid
        h.save(out / "independent-started.json", started)
        code = proc.wait()
    terminal = dict(started, finished_utc=datetime.now(timezone.utc).isoformat(), returncode=code,
        stdout_sha256=h.sha(out / "independent-stdout.txt"), stderr_sha256=h.sha(out / "independent-stderr.log"))
    h.save(out / "independent-terminal.json", terminal)
    assert code == 0
    assert (out / "independent-stderr.log").read_text().splitlines()[-1] == "ALL_COMPLETED 3"
    print("PASS: native shape5 and the first independent enumeration of all three shapes completed.")


if __name__ == "__main__":
    main()
