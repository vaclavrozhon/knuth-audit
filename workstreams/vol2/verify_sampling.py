"""Exact finite distributions for TAOCP 2, section 3.4.2, S and R.

Uses rational probabilities, not Monte Carlo. Reservoir states retain the
physical reservoir and its index table to check R6, not just the final set.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import comb
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def selection(N, n):
    output = defaultdict(F)

    def visit(t, chosen, probability):
        if len(chosen) == n:
            output[chosen] += probability
            return
        assert t < N
        take = F(n - len(chosen), N - t)
        visit(t + 1, chosen + (t + 1,), probability * take)
        if take < 1:
            visit(t + 1, chosen, probability * (1 - take))

    visit(0, (), F(1))
    assert len(output) == comb(N, n)
    assert set(output.values()) == {F(1, comb(N, n))}
    mean = sum(p * max(s) for s, p in output.items())
    variance = sum(p * (max(s) - mean) ** 2 for s, p in output.items())
    assert mean == F(n * (N + 1), n + 1)
    assert variance == F(n * (N + 1) * (N - n), (n + 1) ** 2 * (n + 2))
    return len(output)


def reservoir(N, n):
    states = {(tuple(range(1, n + 1)), tuple(range(n))): F(1)}
    for t in range(n + 1, N + 1):
        new = defaultdict(F)
        for (res, indices), probability in states.items():
            # All rejected M values have the same effect.
            if t > n:
                new[res, indices] += probability * F(t - n, t)
            for M in range(n):
                new_indices = list(indices)
                new_indices[M] = len(res)
                new[res + (t,), tuple(new_indices)] += probability / t
        states = new
    output, size_distribution = defaultdict(F), defaultdict(F)
    for (res, indices), p in states.items():
        assert len(indices) == len(set(indices)) == n
        sample = tuple(res[i] for i in sorted(indices))
        assert len(sample) == n and list(sample) == sorted(sample)
        output[sample] += p
        size_distribution[len(res)] += p
    assert len(output) == comb(N, n)
    assert set(output.values()) == {F(1, comb(N, n))}
    mean = sum(m * p for m, p in size_distribution.items())
    variance = sum(p * (m - mean) ** 2 for m, p in size_distribution.items())
    dh = sum((F(1, t) for t in range(n + 1, N + 1)), F(0))
    dh2 = sum((F(1, t * t) for t in range(n + 1, N + 1)), F(0))
    assert mean == n * (1 + dh)
    assert variance == n * dh - n * n * dh2
    # Independent product formula for the generating function, answer 11.
    poly = {n: F(1)}
    for t in range(n + 1, N + 1):
        new = defaultdict(F)
        for degree, coeff in poly.items():
            new[degree] += coeff * F(t - n, t)
            new[degree + 1] += coeff * F(n, t)
        poly = new
    assert dict(size_distribution) == dict(poly)
    return len(states), len(output)


def example9():
    choices = [4, 1, 6, 7, 5, 3, 5, 11, 11, 3, 7, 9, 3, 11, 4, 5, 4]
    res = [1, 2, 3]
    indices = [0, 1, 2]
    for t, M in enumerate(choices, 4):
        assert 1 <= M <= t
        if M <= 3:
            res.append(t)
            indices[M - 1] = len(res) - 1
    sample = [res[i] for i in sorted(indices)]
    assert res == [1, 2, 3, 5, 9, 13, 16] and sample == [2, 5, 16]
    return dict(reservoir=res, sample=sample)


def main():
    s_count = sum(selection(N, n) for N in range(1, 13) for n in range(1, N + 1))
    r_counts = [reservoir(N, n) for N in range(1, 9) for n in range(1, N + 1)]
    result = dict(selection_N_max=12, selection_parameter_pairs=78,
                  selection_final_subsets=s_count,
                  reservoir_N_max=8, reservoir_parameter_pairs=36,
                  reservoir_terminal_states=sum(x for x, _ in r_counts),
                  reservoir_final_subsets=sum(y for _, y in r_counts),
                  example_3_4_2_9=example9(), status="all assertions passed",
                  scope="S/R with independent ideal uniform draws; no finite-grid RNG claim")
    (ROOT / "results/sampling.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
