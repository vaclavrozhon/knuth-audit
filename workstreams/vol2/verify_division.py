"""Exact checks for TAOCP 2, section 4.3.1; no floating-point arithmetic.

Run from the repository root. Python divmod is an independent arithmetic oracle
for the translated digit algorithm, not another run of that algorithm.
"""
from collections import Counter
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parent


def digits(x, b, size):
    ds = []
    for _ in range(size):
        x, r = divmod(x, b)
        ds.append(r)
    assert x == 0
    return ds


def value(ds, b):
    x = 0
    for d in reversed(ds):
        x = x * b + d
    return x


def trial(u, v, b, n, version="2026"):
    """D3 on a single window; v is normalized and u < b*v."""
    a = v // b ** (n - 1)
    c = (v // b ** (n - 2)) % b
    top = u // b ** (n - 1)
    next_digit = (u // b ** (n - 2)) % b
    h, r = divmod(top, a)
    raw = h
    decrements = 0
    special = version == "2026" and b % 2 and h == b + 2
    if special:
        h = b - 1
    else:
        while (h == b if version == "1997" else h >= b) or h * c > b * r + next_digit:
            h -= 1
            r += a
            decrements += 1
            if r >= b:
                break
    return h, {"raw": raw, "decrements": decrements, "special": bool(special)}


def algorithm_d(U, V, b, n, m, stats):
    """D1--D8 after the 1998, 2005 and 2026 corrections.

    D4 is carried out on digits, retaining the negative-result borrow; D6
    propagates the carry on digits and discards the final carry as prescribed.
    """
    assert b >= 2 and n >= 2 and m >= 0
    assert b ** (n - 1) <= V < b ** n and 0 <= U < b ** (m + n)
    d = b // (V // b ** (n - 1) + 1)
    u = digits(U * d, b, m + n + 1)
    v = digits(V * d, b, n)
    assert v[-1] >= b // 2
    stats["normalization_d_gt_1"] += int(d > 1)
    qs = [0] * (m + 1)
    for j in range(m, -1, -1):
        window = value(u[j:j + n + 1], b)
        assert 0 <= window < b * V * d
        h, meta = trial(window, V * d, b, n)
        stats["special_2026"] += meta["special"]
        stats["d3_decrements_" + str(meta["decrements"])] += 1
        borrow = 0
        for i in range(n):
            product = h * v[i] + borrow
            borrow, low = divmod(product, b)
            diff = u[j + i] - low
            if diff < 0:
                diff += b
                borrow += 1
            u[j + i] = diff
        top = u[j + n] - borrow
        u[j + n] = top % b
        if top < 0:
            stats["add_back"] += 1
            h -= 1
            carry = 0
            for i in range(n):
                carry, u[j + i] = divmod(u[j + i] + v[i] + carry, b)
            carry, u[j + n] = divmod(u[j + n] + carry, b)
            assert carry == 1
        assert 0 <= h < b
        assert value(u[j:j + n + 1], b) == window - h * V * d
        assert 0 <= value(u[j:j + n + 1], b) < V * d
        qs[j] = h
    residual = value(u[:n], b)
    assert residual % d == 0
    result = value(qs, b), residual // d
    assert result == divmod(U, V), (U, V, b, n, m, result)
    assert U == result[0] * V + result[1] and 0 <= result[1] < V
    return result


def main():
    theorem_cases = 0
    gaps = Counter()
    first_failures = {}
    theorem_ranges = [(b, 2) for b in range(2, 13)] + [(b, 3) for b in range(2, 8)]
    for b, n in theorem_ranges:
        for v in range((b // 2) * b ** (n - 1), b ** n):
            a = v // b ** (n - 1)
            for u in range(b * v):
                q = u // v
                h = (u // b ** (n - 1)) // a
                assert q <= h <= q + 3
                if h == q + 3:
                    assert b % 2 == 1 and q == b - 1 and a == (b - 1) // 2
                double = (u // b ** (n - 2)) // (v // b ** (n - 2))
                assert q <= double <= q + 1
                h3, meta = trial(u, v, b, n)
                assert h3 in (q, q + 1) and h3 < b, (b, n, u, v, q, h3)
                gaps[h - q] += 1
                theorem_cases += 1
                for version in ("1997", "2005"):
                    if version not in first_failures:
                        old, oldmeta = trial(u, v, b, n, version)
                        if old not in (q, q + 1) or old >= b:
                            first_failures[version] = dict(b=b, n=n, u=u, v=v, q=q, after_D3=old, **oldmeta)

    # A certificate for the incorrect v_1 condition in the 2026 errata.
    b, n, u, v = 3, 3, 45, 16
    ud, vd = digits(u, b, n + 1), digits(v, b, n)
    q, rem = divmod(u, v)
    h = (ud[n] * b + ud[n - 1]) // vd[n - 1]
    assert vd[n - 1] >= b // 2 and u < b * v
    assert q == 2 and rem == 13 and h == q + 3
    assert vd[1] == 2 != (b - 1) // 2
    assert vd[n - 1] == (b - 1) // 2
    certificate = dict(b=b, n=n, u=u, v=v, u_digits_msd=ud[::-1], v_digits_msd=vd[::-1], q=q, remainder=rem, qhat=h, v_1=vd[1], v_n_minus_1=vd[-1])

    normalization_cases = 0
    for b in range(2, 33):
        for n in (2, 3):
            for v in range(b ** (n - 1), b ** n):
                d = b // (v // b ** (n - 1) + 1)
                assert (b // 2) * b ** (n - 1) <= d * v < b ** n
                normalization_cases += 1
    assert ((3 - 1) // 1) * 5 >= 3 ** 2  # the 1997 D1 overflows

    stats = Counter()
    full_cases = 0
    full_ranges = [(b, 2) for b in range(2, 9)] + [(b, 3) for b in range(2, 6)]
    for b, n in full_ranges:
        for v in range(b ** (n - 1), b ** n):
            for u in range(b ** (n + 1)):
                algorithm_d(u, v, b, n, 1, stats)
                full_cases += 1
    rng = random.Random(20261101)
    for _ in range(5000):
        b = rng.choice([2, 3, 5, 7, 10, 16, 256])
        n = rng.randrange(2, 13)
        m = rng.randrange(0, 13)
        v = rng.randrange(b ** (n - 1), b ** n)
        u = rng.randrange(b ** (m + n))
        algorithm_d(u, v, b, n, m, stats)
    assert stats["add_back"] and stats["special_2026"]
    result = dict(theorem_ranges=theorem_ranges, theorem_cases=theorem_cases,
                  raw_error_histogram=dict(sorted(gaps.items())),
                  known_D3_failure_witnesses=first_failures,
                  new_errata_index_certificate=certificate,
                  normalization_cases=normalization_cases,
                  full_algorithm_ranges=full_ranges,
                  full_exhaustive_cases=full_cases, full_seeded_cases=5000,
                  seed=20261101, branch_counts=dict(stats), status="all assertions passed")
    (ROOT / "results/division.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
