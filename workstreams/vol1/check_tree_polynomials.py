"""Supplementary finite checks for the proofs of Algorithm 2.3.3A and ex. 15."""

from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import random
from tree_polynomials import Pool, add_printed, multiply


def clean(p):
    return {m: c for m, c in p.items() if c}


def sum_flat(p, q):
    out = dict(q)
    for m, c in p.items():
        out[m] = out.get(m, 0) + c
    return clean(out)


def product_flat(p, q):
    out = {}
    for a, c in p.items():
        for b, d in q.items():
            m = tuple(x + y for x, y in zip(a, b))
            out[m] = out.get(m, 0) + c * d
    return clean(out)


def check_add(p, q, nvars, steps):
    pool = Pool()
    a, b = pool.build(p), pool.build(q)
    pa, na = pool.validate(a, nvars)
    pb, nb = pool.validate(b, nvars)
    assert pa == clean(p) and pb == clean(q)
    old = pool.snapshot(na)
    counts = add_printed(pool, a, b, check_structure=nvars)
    actual, output = pool.validate(b, nvars)
    assert actual == sum_flat(p, q), (p, q, actual)
    assert pool.snapshot(na) == old
    pool.partition(na, output)
    steps.update(counts)
    return counts


def check_multiply(p, q, nvars):
    pool = Pool()
    a, b = pool.build(p), pool.build(q)
    _, na = pool.validate(a, nvars)
    _, nb = pool.validate(b, nvars)
    old = pool.snapshot(na | nb)
    r = multiply(pool, a, b)
    actual, nr = pool.validate(r, nvars)
    assert actual == product_flat(p, q), (p, q, actual)
    assert pool.snapshot(na | nb) == old
    pool.partition(na, nb, nr)


def random_poly(rng, nvars):
    out = {}
    for _ in range(rng.randrange(13)):
        m = tuple(rng.randrange(5) if rng.random() < 0.45 else 0 for _ in range(nvars))
        out[m] = rng.randrange(-4, 5)
    return clean(out)


def main():
    counts = Counter()
    additions = multiplications = 0
    p = {(1, 1, 0): 1, (2, 0, 0): -1, (1, 1, 1): -1,
         (0, 0, 3): -1, (1, 0, 3): 3}
    q = {(0, 0, 0): 3, (2, 0, 0): 1, (1, 1, 1): 1,
         (0, 0, 3): 1, (1, 0, 3): -3}
    book_counts = check_add(p, q, 3, counts)
    assert sum_flat(p, q) == {(0, 0, 0): 3, (1, 1, 0): 1}
    additions += 1
    monomials = [(0, 0), (1, 0), (0, 1), (1, 1)]
    small = [{m: c for m, c in zip(monomials, cs) if c}
             for cs in product((-1, 0, 1), repeat=4)]
    for a in small:
        for b in small:
            check_add(a, b, 2, counts)
            additions += 1
    rng = random.Random(2332026)
    for nvars in (1, 2, 3, 5, 8):
        for i in range(80):
            a, b = random_poly(rng, nvars), random_poly(rng, nvars)
            if i % 4 == 0:
                b = {m: -c for m, c in a.items()}
            elif i % 4 == 1:
                b = sum_flat(b, {m: -c for m, c in a.items()})
            if i % 10 == 0:
                a = {m: Fraction(c, 3) for m, c in a.items()}
                b = {m: Fraction(c, 7) for m, c in b.items()}
            check_add(a, b, nvars, counts)
            additions += 1
            if nvars <= 5 and i < 20:
                check_multiply(a, b, nvars)
                multiplications += 1
    for a in small:
        for b in small[:9]:
            check_multiply(a, b, 2)
            multiplications += 1
    assert set(counts) == set(range(1, 12))
    result = {
        "status": "pass",
        "addition_cases": additions,
        "multiplication_cases": multiplications,
        "book_example_steps": dict(sorted(book_counts.items())),
        "all_steps": dict(sorted(counts.items())),
        "exact_coefficients": "integers and rational numbers; no floating-point rounding",
        "invariants": ["all reciprocal row links", "all parent links", "strict exponent order",
                       "variable order", "canonical final form", "source unchanged",
                       "both addition root addresses unchanged", "no shared output nodes",
                       "complete allocated/free partition", "A8 context and parent agreement"],
        "limits": "Finite tests supplement the general proof; this is not a MIX program."
    }
    out = Path(__file__).resolve().parent / "results/tree-polynomials.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
