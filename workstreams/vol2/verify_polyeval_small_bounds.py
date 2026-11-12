#!/usr/bin/env python3
"""Exact checks supplementing structural proofs of TAOCP 4.6.4–32..36."""
import datetime
import itertools
import json
import os
from pathlib import Path
import time

import sympy as S

BASE = Path(__file__).resolve().parent
RESULT = BASE / "results/polyeval-small-bounds.json"


def skeletons(m):
    """All unordered operand choices, after folding parameter additions."""
    states = [([1], [])]
    for _ in range(m):
        states = [
            (degrees + [degrees[j] + degrees[k]], pairs + [(j, k)])
            for degrees, pairs in states
            for j, k in itertools.combinations_with_replacement(range(len(degrees)), 2)
        ]
    return states


def check():
    x = S.Symbol("x")
    a1, a2, a3, a4, a5 = S.symbols("a1:6")
    sparse = a3 + (a2 + a1*x*x)*x*x
    assert S.expand(sparse - (a1*x**4 + a2*x**2 + a3)) == 0

    # Exercise34 includes parameter subtraction and a negative chain product.
    old1 = a1+x
    old2 = a2*old1
    old3 = a3-old2
    old4 = -old1*old3
    old5 = a4*old4
    old6 = a5+old5
    new1 = x+a1
    new3 = new1-a3/a2
    new4 = new1*new3
    new6 = new4+a5/(a2*a4)
    contents = [1, a2, -a2, a2, a2*a4, a2*a4]
    new = [new1, new1, new3, new4, new4, new6]
    old = [old1, old2, old3, old4, old5, old6]
    for o, c, n in zip(old, contents, new):
        assert S.cancel(o-c*n) == 0

    quartic = [s for s in skeletons(2) if s[0][-1] == 4]
    sextic = [s for s in skeletons(3) if s[0][-1] == 6]
    assert quartic == [([1, 2, 4], [(0, 0), (1, 1)])]
    assert sextic == [
        ([1, 2, 3, 6], [(0, 0), (0, 1), (2, 2)]),
        ([1, 2, 4, 6], [(0, 0), (1, 1), (1, 2)]),
    ]

    # The printed quartic chain and its coefficient parametrization.
    q = (x+a1)*(x+a2)
    raw4 = (q+a3)*(q+a4)+a5
    A, B, C, D, E, F, G, H = S.symbols("A B C D E F G H")
    family4 = x**4+2*A*x**3+(E+A*A)*x*x+E*A*x+F
    mapping4 = {A:a1+a2, E:2*a1*a2+a3+a4,
                F:(a1*a2+a3)*(a1*a2+a4)+a5}
    assert S.expand(raw4-family4.subs(mapping4)) == 0
    coefficients4 = S.Poly(family4, x)
    c3, c2, c1 = [coefficients4.nth(i) for i in (3, 2, 1)]
    assert S.expand(8*c1-4*c3*c2+c3**3) == 0
    assert S.expand(raw4.subs({a1:0,a2:0,a3:0,a4:0,a5:1})) == x**4+1

    # First sextic family: two shifted copies of one cubic.
    family61 = (x**3+A*x*x+B*x+C)*(x**3+A*x*x+B*x+D)+E
    p61 = S.Poly(family61,x)
    c5, c4, c3, c2, c1 = [p61.nth(i) for i in (5,4,3,2,1)]
    assert S.expand(16*c1-(4*c4-c5**2)*(2*c3-c5*c4+c5**3/4)) == 0
    assert S.expand(family61.subs({A:0,B:0})).coeff(x,1) == 0

    # Second sextic family: a quadratic times a quartic built from it.
    family62 = family4*(x*x+A*x+G)+H
    p62 = S.Poly(family62,x)
    c5, c4, c3 = [p62.nth(i) for i in (5,4,3)]
    assert S.expand(27*c3-18*c5*c4+5*c5**3) == 0
    assert S.expand(family62.subs(A,0)).coeff(x,1) == 0

    # Check both complete displayed seven-parameter programs against the families.
    a6,a7 = S.symbols("a6 a7")
    cubic = (x+a3)*(q+a4)
    raw61 = (cubic+a5)*(cubic+a6)+a7
    cp = S.Poly(cubic,x)
    mapping61 = {A:cp.nth(2),B:cp.nth(1),C:cp.nth(0)+a5,
                 D:cp.nth(0)+a6,E:a7}
    assert S.expand(raw61-family61.subs(mapping61)) == 0
    raw62 = ((q+a3)*(q+a4)+a6)*(q+a5)+a7
    mapping62 = {A:a1+a2,E:2*a1*a2+a3+a4,
                 F:(a1*a2+a3)*(a1*a2+a4)+a6,G:a1*a2+a5,H:a7}
    assert S.expand(raw62-family62.subs(mapping62)) == 0
    return {
        "sparse_quartic": {"multiplications":3,"additions":2},
        "normalization34_intermediate_identities":6,
        "all_product_skeletons": {"two_products":len(skeletons(2)),
                                  "three_products":len(skeletons(3))},
        "degree4_skeletons":quartic,
        "degree6_skeletons":sextic,
        "generic_family_mappings":3,
        "coefficient_relations":3,
        "C0239":"The quartic final constant is a5; printed D=a6 is undefined.",
        "quartic_missing_example":"x^4+x",
        "sextic_missing_example":"x^6+x",
        "scope":"Structural completeness is proved separately in the note; skeleton enumeration assumes the proved parameter-addition normal form.",
    }


if __name__ == "__main__":
    if RESULT.exists():
        raise SystemExit("Result exists; do not repeat a completed block without a new concern.")
    start = time.monotonic()
    result = check()
    result.update(status="passed",pid=os.getpid(),seconds=time.monotonic()-start,
                  completed_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
    RESULT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(result,ensure_ascii=False))
