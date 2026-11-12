"""Small checks of the printed 26-vertex tree and a derived source identity.

No exchange-history or partition census is repeated. The general identity
is proved by generating functions and telescoping in the sequential note.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
N = 28
C = [comb(2 * j, j) // (j + 1) for j in range(N + 1)]

# Literal arrow transcription from all2-prepre file page 33.
parents = [26, 26, 24, 22, 18, 18, 18, 18, 18, 18, 17, 17, 16,
           15, 15, 14, 13, 11, 5, 5, 5, 5, 4, 4, 3, 3]
merge = [1, 2, 26, 25, 3, 24, 23, 4, 22, 21, 20, 19, 5, 6, 7,
         8, 9, 10, 18, 11, 12, 17, 13, 16, 14, 15]
deck = list(range(1, 27))
for j, parent in enumerate(parents):
    deck[j], deck[parent - 1] = deck[parent - 1], deck[j]
assert deck == [26] + list(range(1, 26))
assert [v for v in merge if v < 15] == list(range(1, 15))
assert [v for v in merge if v > 15] == list(range(26, 15, -1))
for i, v in enumerate(merge[:-1]):
    target = next((w for w in merge[i + 1:]
                   if (v < 15 < w) or (w < 15 < v)), 15)
    assert parents[v - 1] == target
assert parents[14] == 15

def convolution(a, b):
    return [sum(a[i] * b[j - i] for i in range(j + 1))
            for j in range(N + 1)]

# Lemma 13's two decompositions, evaluated by polynomial convolution.
minus_one = [0] + C[1:]
power = [1] + [0] * N
H = {}
for k in range(1, N + 1):
    power = convolution(power, minus_one)
    prime = [k * x for x in power]
    h = [0] * (N + 1)
    for m in range(1, N + 1):
        h[m] = prime[m] + sum(h[u] * C[m - u - 1]
                              for u in range(1, m))
        if m >= k:
            delta = comb(2 * m, m - k)
            if m > k:
                delta -= comb(2 * m, m - k - 1)
            assert h[m] == k * delta
        else:
            assert h[m] == 0
        H[m, k] = h[m]

checks = 0
for m in range(1, N + 1):
    for p in range(1, N + 1):
        s, t = m + p, m * p
        by_decomposition = sum(F(H[m, k] * H[p, k], k)
                               for k in range(1, min(m, p) + 1))
        closed = F(comb(2 * m, m) * comb(2 * p, p) * (s + 4 * t)
                   - s * comb(2 * s, s), 2 * s * (s + 1))
        assert by_decomposition == closed
        assert closed.denominator == 1
        for k in range(1, min(m, p) + 1):
            denominator = (m + k + 1) * (p + k + 1)
            r = F(2 * (s + 1) * k * k - s * k + s + 2 * t, s * (s + 1))
            next_r = F(2 * (s + 1) * (k + 1)**2 - s * (k + 1)
                       + s + 2 * t, s * (s + 1))
            assert r - next_r * F((m - k) * (p - k), denominator) == (
                F(k * (2 * k + 1)**2, denominator) + F(1, s + 1))
            checks += 1

result = dict(
    printed_graph=dict(source="errata all2-prepre file page 33, answer 18(a)",
                       n=26, root=15, parents=parents,
                       merge_sequence=merge, output=deck),
    formula_models=N * N,
    telescoping_instances=checks,
    scope="Finite checks of the new general derivation, not a repeated "
          "history census or a new proof of the source structural theorem.",
)
(ROOT / "results/exchange-appendix.json").write_text(json.dumps(result, indent=2) + "\n")
print("PASS printed 26-vertex graph;", N * N, "formula models;", checks,
      "exact telescoping instances")
