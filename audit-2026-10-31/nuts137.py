"""Exact seven-hexagon geometry and XCC model for DLX137; rotations only."""
from collections import Counter
from itertools import permutations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/nuts137'
# Cartesian coordinates are (sqrt(3)*x,y). Directions start north, then CCW.
DIRECTIONS = ((0, 2), (-1, 1), (-1, -1), (0, -2), (1, -1), (1, 1))
POSITIONS = ((0, 0),) + DIRECTIONS
EDGES = tuple((u, v, DIRECTIONS.index((b[0] - a[0], b[1] - a[1])))
              for u, a in enumerate(POSITIONS) for v, b in enumerate(POSITIONS)
              if u < v and (b[0] - a[0], b[1] - a[1]) in DIRECTIONS)
TYPES = tuple('1' + ''.join(p) for p in permutations('23456'))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


def canonical(word):
    assert len(word) == 6 and set(word) == set('123456')
    k = word.index('1')
    return word[k:] + word[:k]


def rotations(word):
    return tuple(word[k:] + word[:k] for k in range(6))


def compatible(a, b, rule):
    assert rule in ('equal', 'sum7')
    return a == b if rule == 'equal' else int(a) + int(b) == 7


def normalize(words):
    # A global rotation by t sends old edge k to new edge k+t.
    t = -words[0].index('1') % 6
    result = [''] * 7
    for i, word in enumerate(words):
        j = 0 if i == 0 else 1 + ((i - 1 + t) % 6)
        result[j] = ''.join(word[(k - t) % 6] for k in range(6))
    assert result[0][0] == '1'
    return result


def validate(words, nuts, rule):
    assert len(words) == 7 and Counter(map(canonical, words)) == Counter(nuts)
    assert len(set(nuts)) == 7
    assert all(compatible(words[u][k], words[v][(k + 3) % 6], rule)
               for u, v, k in EDGES)


def problem(nuts, rule):
    assert len(nuts) == len(set(nuts)) == 7 and all(x in TYPES for x in nuts)
    rows, placements = [], []
    for pos in range(7):
        for nut in nuts:
            for word in ([nut] if pos == 0 else rotations(nut)):
                row = ['p' + str(pos), 'n' + nut]
                for u, v, k in EDGES:
                    if pos == u:
                        color = word[k]
                    elif pos == v:
                        color = word[(k + 3) % 6]
                        if rule == 'sum7':
                            color = str(7 - int(color))
                    else:
                        continue
                    row.append(f'e{u}{v}:{color}')
                rows.append(row)
                placements.append((pos, word))
    header = ['p' + str(i) for i in range(7)] + ['n' + n for n in nuts]
    header += ['|'] + [f'e{u}{v}' for u, v, _ in EDGES]
    assert len(rows) == 259 and len(header) == 27
    return dict(header=header, rows=rows, placements=placements)


def native_text(problem):
    return ' '.join(problem['header']) + '\n' + '\n'.join(' '.join(r) for r in problem['rows']) + '\n'


def ring_search(nuts, rule):
    """Independent exhaustive permutation search after forced radial rotations.

    Uses the ring incidence formulas directly, not EDGES or an XCC encoding.
    """
    found, by_center = [], []
    for center, word in enumerate(nuts):
        available = [i for i in range(7) if i != center]
        oriented = {}
        for k in range(6):
            wanted = word[k] if rule == 'equal' else str(7 - int(word[k]))
            for i in available:
                choices = [w for w in rotations(nuts[i]) if w[(k + 3) % 6] == wanted]
                assert len(choices) == 1
                oriented[k, i] = choices[0]
        selected = []
        nodes, before = 0, len(found)

        def dfs(k, unused):
            nonlocal nodes
            nodes += 1
            if k == 6:
                left, right = oriented[5, selected[5]], oriented[0, selected[0]]
                if compatible(left[1], right[4], rule):
                    words = [word] + [oriented[j, i] for j, i in enumerate(selected)]
                    validate(words, nuts, rule)
                    found.append('/'.join(words))
                return
            for i in unused:
                if k:
                    left, right = oriented[k - 1, selected[-1]], oriented[k, i]
                    if not compatible(left[(k + 1) % 6], right[(k + 4) % 6], rule):
                        continue
                selected.append(i)
                dfs(k + 1, [j for j in unused if j != i])
                selected.pop()
        dfs(0, available)
        by_center.append(dict(center=word, nodes=nodes, solutions=len(found) - before))
    assert len(set(found)) == len(found)
    return sorted(found), by_center


assert len(EDGES) == 12 and len(TYPES) == 120
