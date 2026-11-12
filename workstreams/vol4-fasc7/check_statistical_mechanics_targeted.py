#!/usr/bin/env python3
"""Fixed 48-row table and five tiny Ising checks; not a general proof/census."""
from collections import Counter
from hashlib import sha256
from itertools import product
import json
from math import isclose, sqrt
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
source = (ROOT / "sources/file-020.txt").read_text()
table = source.split("Here are the 48 possibilities", 1)[1].split("To analyze", 1)[0]
printed = [(word, int(e.replace("−", "-")))
           for word, e in re.findall(r"([A-Z]{5})\s+([−-]?[0-3])", table)]
assert len(printed) == 48 and len({w for w, e in printed}) == 48
assert {w for w, e in printed} == {"".join(v) for v in product("BS", "CL", "AIU", "EO", "DN")}
relations = ({"BAN", "BUD", "SIN"}, {"BE", "SE", "SO"}, {"COD", "CON", "LED"})
rows = []
for word, e in printed:
    projections = (word[0] + word[2] + word[4], word[0] + word[3], word[1] + word[3] + word[4])
    bits = tuple(int(t in r) for t, r in zip(projections, relations))
    derived = -sum(bits)
    assert e == derived, (word, e, bits)
    rows.append({"word": word, "projections": projections, "membership_bits": bits,
                 "printed_energy": e, "derived_energy": derived})


def close(x, y):
    assert isclose(x, y, rel_tol=2e-11, abs_tol=2e-11), (x, y)


def check_ising(n, z, field):
    w = z ** field
    u = (w + 1 / w) / (2 * z)
    d = (w - 1 / w) / (2 * z)
    delta = sqrt(d * d + z * z)
    lam, mu = u + delta, u - delta
    a = lam * z + (z - z ** 3) / delta
    b = mu * z - (z - z ** 3) / delta
    ahat, bhat = -d * a / delta, d * b / delta  # Public 22 Oct 2026 sign correction.
    c = (w - 1 / w) * (1 - z * z) / (2 * delta * delta)
    g = a * lam ** (n - 1) + b * mu ** (n - 1)
    site = [ahat * lam ** (n - 1) + bhat * mu ** (n - 1)
            + c * (lam ** (n - k) * mu ** (k - 1) + lam ** (k - 1) * mu ** (n - k))
            for k in range(1, n + 1)]
    average = ((ahat + c * lam / (n * delta)) * lam ** (n - 1)
               + (bhat - c * mu / (n * delta)) * mu ** (n - 1)) / g
    up = (field * (w - 1 / w) - (w + 1 / w)) / (2 * z * z)
    dp = (field * (w + 1 / w) - (w - 1 / w)) / (2 * z * z)
    deltap = (d * dp + z) / delta
    lamp, mup = up + deltap, up - deltap
    corrp = (1 - 3 * z * z) / delta - (z - z ** 3) * deltap / delta ** 2
    ap, bp = lamp * z + lam + corrp, mup * z + mu - corrp
    gp = ap * lam ** (n - 1) + bp * mu ** (n - 1)
    if n >= 2:
        gp += (n - 1) * (a * lam ** (n - 2) * lamp + b * mu ** (n - 2) * mup)
    direct_g = direct_energy = 0.0
    direct_site = [0.0] * n
    for spins in product((-1, 1), repeat=n):
        energy = -sum(spins[j] * spins[j + 1] for j in range(n - 1)) - field * sum(spins)
        weight = z ** energy
        direct_g += weight
        direct_energy += energy * weight
        for k in range(n):
            direct_site[k] += spins[k] * weight
    close(g, direct_g)
    close(z * gp, direct_energy)
    for x, y in zip(site, direct_site):
        close(x, y)
    close(average, sum(direct_site) / (n * direct_g))
    return {"N": n, "z": z, "B": field, "configurations": 2 ** n,
            "partition": direct_g, "energy_per_particle": direct_energy / (n * direct_g),
            "mean_magnetization": average, "all_formulas_agree": True}


checks = [check_ising(*case) for case in
          [(1, .5, 2), (2, .5, -1), (5, .5, 0), (4, 1., 2), (5, 2., 1)]]
result = {
    "scope": "Every printed row of the fixed 48-state example, plus five fixed Ising instances of at most 32 configurations each. Not a general proof or parameter sweep.",
    "source": "sources/file-020.txt",
    "source_sha256": sha256(source.encode()).hexdigest(),
    "table_rows": rows,
    "energy_histogram": dict(sorted(Counter(e for w, e in printed).items())),
    "ising_checks": checks,
    "general_proof": "notes/statistical-mechanics-and-exercise-012.md",
}
(ROOT / "results/statistical-mechanics-targeted.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"table_rows_verified": len(rows), "energy_histogram": result["energy_histogram"],
                  "ising_cases": len(checks), "ising_total_configurations": sum(x["configurations"] for x in checks),
                  "all_passed": True}))
