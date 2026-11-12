#!/usr/bin/env python3
"""Untrusted certificate producer; verify_primality_basic.py uses only integers."""
from pathlib import Path
from math import prod
import json
from sympy import factorint

ROOT = Path(__file__).resolve().parent
N0 = 37866809061660057264219253397
N2 = 143675413657196977
N4 = 1653701519
known = {
    N0: {2: 2, 19: 1, 107: 1, 353: 1, 91813: 1, N2: 1},
    N2: {2: 4, 3: 2, 547: 1, 1103: 1, N4: 1},
    N4: {2: 1, 7: 1, 19: 1, 23: 1, 137: 1, 1973: 1},
}
nodes = {2: dict(n=2, factors=[], witness=1)}


def certificate(n):
    if n in nodes:
        return
    fs = known.get(n)
    if fs is None:
        fs = {int(p): int(e) for p, e in factorint(n-1).items()}
    assert prod(p**e for p, e in fs.items()) == n-1
    for p in fs:
        certificate(p)
    a = 2
    while pow(a, n-1, n) != 1 or any(pow(a, (n-1)//p, n) == 1 for p in fs):
        a += 1
        assert a < 10000
    nodes[n] = dict(n=n, factors=sorted(fs.items()), witness=a)


targets = [3, 5, 17, 257, 65537, 857, 843589, 8174912477117,
           23528569104401, N0, 1009, 2341, 16381]
for n in targets:
    certificate(n)
data = dict(targets=targets, nodes=[nodes[n] for n in sorted(nodes)],
            generator='SymPy factorint for auxiliary n-1 factorizations; no primality trust')
(ROOT/'results/primality-certificates.json').write_text(json.dumps(data, indent=2)+'\n')
print('Generated', len(nodes), 'nodes for', len(targets), 'targets')
