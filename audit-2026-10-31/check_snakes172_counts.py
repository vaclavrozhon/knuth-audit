"""Count the unsearched queen MCC input and check its length convention."""
from collections import Counter
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/snakes172'


def adjacent(v, w):
    r, c = divmod(v, 8); s, t = divmod(w, 8)
    return v != w and (r == s or c == t or abs(r-s) == abs(c-t))


def count(remove_triangles):
    total = entries = 0
    kinds = Counter()
    by_vertex = []
    for v in range(64):
        neighbors = [w for w in range(64) if adjacent(v, w)]
        d = len(neighbors)
        # The start is forced, as made explicit by the2023 correction.
        blank = int(v != 0)
        interiors = (d if v == 0 else sum(not remove_triangles or not adjacent(a, b)
                                          for a, b in combinations(neighbors, 2)))
        endpoints = d if v != 0 and not adjacent(0, v) else 0
        options = blank + interiors + endpoints
        items = 2*blank + (d+3)*interiors + (d+4)*endpoints
        total += options; entries += items
        kinds.update(blank=blank, start=interiors if v == 0 else 0,
                     interior=interiors if v != 0 else 0, end=endpoints)
        by_vertex.append(dict(vertex=v, degree=d, options=options, item_entries=items))
    return dict(options=total, item_entries=entries, row_spacers=total,
                total_nodes=entries+total, kinds=dict(kinds), by_vertex=by_vertex)


def main():
    assert not (OUT / 'input-counts-checked.json').exists()
    original, corrected = count(False), count(True)
    assert (original['options'], original['total_nodes']) == (16788, 454380)
    assert (corrected['options'], corrected['total_nodes']) == (10422, 281934)
    assert original['kinds']['blank'] == corrected['kinds']['blank'] == 63
    save(OUT / 'input-counts-checked.json', dict(at_utc=datetime.now(timezone.utc).isoformat(),
        checker_sha256=sha(__file__), original=original, corrected=corrected,
        excluded_triangular_options=original['options']-corrected['options'],
        convention='Total length counts item nodes plus one spacer for every option. The start is selected in both inputs.',
        new_solution_searches=0))
    print('PASS172 input only:16788/454380 and10422/281934;6366 triangular options removed. No search.')


if __name__ == '__main__':
    main()
