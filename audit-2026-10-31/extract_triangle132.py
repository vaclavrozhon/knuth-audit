"""Decode Esser's original24-color GIF into a finite, independently checkable witness."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import gzip
import hashlib
import json

from PIL import Image

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/triangles132'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n')


def main():
    OUT.mkdir(exist_ok=True)
    path = ROOT/'sources/triangles132/trios24.gif'
    im = Image.open(path)
    assert im.size == (1665, 1386) and im.mode == 'P'
    palette = im.getpalette()
    # The three gray/black values belong to the background and drawn grid.
    colors = sorted(i for count, i in im.getcolors() if count > 20000 and i not in (0, 22, 25))
    assert len(colors) == 24
    index = {c: i for i, c in enumerate(colors)}

    def vertex(r, c):
        return (13+12*r+24*c, 18+20*r)

    tiles, samples, majority_counts = [], [], Counter()
    for r in range(68):
        for c in range(68-r):
            triangles = [(0, [vertex(r, c), vertex(r, c+1), vertex(r+1, c)])]
            if c < 67-r:
                triangles.append((1, [vertex(r, c+1), vertex(r+1, c+1), vertex(r+1, c)]))
            for orient, vertices in triangles:
                center = [sum(p[k] for p in vertices)/3 for k in (0, 1)]
                labels = []
                for i in range(3):
                    a, b = vertices[i], vertices[(i+1) % 3]
                    # Centroid of the wedge [edge endpoint, endpoint, tile center].
                    x, y = [round((center[k]+a[k]+b[k])/3) for k in (0, 1)]
                    pixels = Counter(im.getpixel((x+dx, y+dy)) for dx in (-1, 0, 1) for dy in (-1, 0, 1))
                    eligible = {k: v for k, v in pixels.items() if k in index}
                    color = max(eligible, key=eligible.get)
                    assert eligible[color] >= 5  # strict majority of all nine pixels
                    labels.append(index[color]); majority_counts[eligible[color]] += 1
                    samples.append([r, c, orient, i, x, y, sorted(pixels.items()), color])
                tiles.append([r, c, orient, labels])
    save(OUT/'witness.json', dict(side=68, colors=24, source_image=str(path.relative_to(ROOT)),
                                 source_sha256=sha(path), palette_indices=colors,
                                 palette_rgb=[palette[3*c:3*c+3] for c in colors], tiles=tiles))
    data = json.dumps(samples, separators=(',', ':')).encode()
    (OUT/'pixel-samples.json.gz').write_bytes(gzip.compress(data, mtime=0))
    save(OUT/'image-extraction.json', dict(
        checked_at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=sha(__file__),
        image_sha256=sha(path), original_image_visually_inspected=True,
        vertices_formula=['13+12*r+24*c', '18+20*r'],
        tile_count=len(tiles), wedge_count=len(samples), colors=24,
        majority_histogram=dict(majority_counts), minimum_majority=min(majority_counts),
        witness_sha256=sha(OUT/'witness.json'), samples_sha256=sha(OUT/'pixel-samples.json.gz'),
        scope='Original raster decoding only; a separate symbolic checker validates all cells, edges, boundary and cyclic types. No search for a new solution.'))
    print('Decoded132:', len(tiles), 'tiles;', len(samples), 'wedges; minimum', min(majority_counts), 'of9 pixels agree.')


if __name__ == '__main__':
    main()
