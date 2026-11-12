"""Draw the explicit F137 witness, including all vertex labels and tile types."""
import hashlib
import json
from pathlib import Path
from math import sqrt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import verify_f137 as proof

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results/polygons143"
COLORS = dict(a="#ffffff", b="#ee80ac", c="#8e64b0", d="#24222b")


def draw():
    types = proof.verify()
    fig, ax = plt.subplots(figsize=(15, 4.5), facecolor="#f6f7fb")
    ax.set_facecolor("#f6f7fb")
    for x in range(12):
        cells = [(((x, 0), (x + 1, 0), (x, 1)),
                  (proof.BOTTOM[x], proof.BOTTOM[x + 1], proof.TOP[x])),
                 (((x + 1, 1), (x, 1), (x + 1, 0)),
                  (proof.TOP[x + 1], proof.TOP[x], proof.BOTTOM[x + 1]))]
        for points, letters in cells:
            p = [(u + v / 2, v * sqrt(3) / 2) for u, v in points]
            center = tuple(sum(q[i] for q in p) / 3 for i in range(2))
            for j, (q, letter) in enumerate(zip(p, letters)):
                before, after = p[(j - 1) % 3], p[(j + 1) % 3]
                sector = [q, tuple((q[k] + after[k]) / 2 for k in range(2)),
                          center, tuple((q[k] + before[k]) / 2 for k in range(2))]
                ax.add_patch(Polygon(sector, facecolor=COLORS[letter], edgecolor="none"))
            ax.add_patch(Polygon(p, fill=False, edgecolor="#343441", linewidth=1.2))
    for y, row in enumerate([proof.BOTTOM, proof.TOP]):
        for x, letter in enumerate(row):
            ax.text(x + y / 2, y * sqrt(3) / 2 + (0.14 if y else -0.17), letter,
                    ha="center", va="center", fontsize=12, fontfamily="monospace")
    ax.text(0, 1.78, "F137 · A strip the book says cannot be tiled", fontsize=19,
            weight="bold", color="#24222b")
    ax.text(0, 1.39, "Answer 7.2.2.1–143, p.455  ·  12 × 1 parallelogram  ·  24 triangles",
            fontsize=12, color="#515164")
    ax.text(0, -0.57, "Every shared vertex has one color. Every rotational tile type appears once.",
            fontsize=12, color="#24222b")
    ax.text(0, -0.93, "Tile types (rotations identified, reflections distinct):", fontsize=11,
            color="#515164")
    ax.text(0, -1.23, "   ".join(sorted(types)[:12]), fontfamily="monospace", fontsize=11)
    ax.text(0, -1.50, "   ".join(sorted(types)[12:]), fontfamily="monospace", fontsize=11)
    ax.set_aspect("equal")
    ax.set_xlim(-0.25, 12.9)
    ax.set_ylim(-1.75, 2.02)
    ax.axis("off")
    fig.subplots_adjust(left=0.025, right=0.98, top=0.98, bottom=0.03)
    paths = []
    for ext in ["svg", "png"]:
        path = ROOT / "images" / ("f137-strip-witness." + ext)
        fig.savefig(path, dpi=150, facecolor=fig.get_facecolor())
        paths.append(path)
    record = dict(verifier_sha256=hashlib.sha256(Path(proof.__file__).read_bytes()).hexdigest(),
                  renderer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  bottom=proof.BOTTOM, top=proof.TOP, tile_types=types,
                  images={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in paths})
    (OUT / "witness-figure.json").write_text(json.dumps(record, indent=2) + "\n")
    print("PASS: F137 diagram generated from the checked literal witness.")


if __name__ == "__main__":
    draw()
