"""Exact checks for TAOCP 2 section 3.1. Results supplement written proofs."""
from array import array
from collections import Counter, deque
from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
MOD = 10 ** 10


def k_pass(x, trace=None):
    start = 3 + (x // 10 ** 8) % 10
    for step in range(start, 13):
        if step == 3:
            if x < 5 * 10 ** 9:
                x += 5 * 10 ** 9
        elif step == 4:
            x = (x * x // 10 ** 5) % MOD
        elif step in (5, 8):
            x = (1001001001 * x) % MOD
        elif step == 6:
            x = x + 9814055677 if x < 10 ** 8 else MOD - x
        elif step == 7:
            x = (x % 10 ** 5) * 10 ** 5 + x // 10 ** 5
        elif step == 9:
            x = int(''.join(str(max(0, int(d) - 1)) for d in f'{x:010d}'))
        elif step == 10:
            x = x * x + 99999 if x < 10 ** 5 else x - 99999
        elif step == 11:
            assert x > 0
            while x < 10 ** 9:
                x *= 10
        elif step == 12:
            x = (x * (x - 1) // 10 ** 5) % MOD
        assert 0 <= x < MOD
        if trace is not None:
            trace.append((step, x))
    return x


def algorithm_k(x, trace=None):
    rounds = 1 + x // 10 ** 9
    if trace is not None:
        trace.append((1, x))
    for _ in range(rounds):
        x = k_pass(x, trace)
    return x


def orbit(f, start):
    seen, seq = {}, []
    x = start
    while x not in seen:
        seen[x] = len(seq)
        seq.append(x)
        x = f[x]
    return seen[x], len(seq) - seen[x]


def decompose(f):
    """Prune indegree-zero vertices, identify cycles, propagate certificates."""
    n = len(f)
    indegree = array('i', [0]) * n
    for x in f:
        indegree[x] += 1
    queue = deque(x for x in range(n) if indegree[x] == 0)
    peeled = array('i')
    while queue:
        x = queue.popleft()
        peeled.append(x)
        y = f[x]
        indegree[y] -= 1
        if indegree[y] == 0:
            queue.append(y)
    component = array('i', [-1]) * n
    depth = array('i', [0]) * n
    cycles = []
    for x in range(n):
        if indegree[x] and component[x] == -1:
            cycle, y = [], x
            while component[y] == -1:
                component[y] = len(cycles)
                cycle.append(y)
                y = f[y]
            assert y == x
            cycles.append(cycle)
    for x in reversed(peeled):
        component[x] = component[f[x]]
        depth[x] = depth[f[x]] + 1
    # Validate the complete decomposition, separately from the peeling loop.
    assert sum(map(len, cycles)) + len(peeled) == n
    for x in range(n):
        assert component[x] >= 0 and component[x] == component[f[x]]
        if depth[x]:
            assert depth[x] == depth[f[x]] + 1
        else:
            assert indegree[x] == 1 and depth[f[x]] == 0
    for cycle in cycles:
        assert len(cycle) == len(set(cycle))
        assert [f[x] for x in cycle] == cycle[1:] + cycle[:1]
    return cycles, component, depth


def detection(mu, lam):
    def value(n):
        return n if n < mu else mu + (n - mu) % lam
    n = 1
    while value(n) != value(2 * n):
        n += 1
    expected = lam * ((mu + lam - 1) // lam + (mu == 0))
    assert n == expected and mu <= n <= mu + lam
    i = 0
    while value(i) != value(n + i):
        i += 1
    assert i == mu
    period = next((j for j in range(1, mu) if value(n + j) == value(n)), n)
    assert period == lam
    # Brent's actual recurrence, answer 7(b), independently of the formula.
    X = Y = value(0)
    remaining = block = 1
    t = 0
    while True:
        t += 1
        X = value(t)
        remaining -= 1
        if X == Y:
            break
        if remaining == 0:
            Y = X
            block *= 2
            remaining = block
    power = 1 << (max(mu + 1, lam) - 1).bit_length()
    assert t == power - 1 + lam and block - remaining == lam
    # Gosper's online algorithm. Store indices too, to check its period output.
    table = {0: (value(0), 0)}
    def valuation(n):
        return ((n + 1) & -(n + 1)).bit_length() - 1
    n = 0
    while True:
        n += 1
        matches = [j for v, j in table.values() if v == value(n)]
        if matches:
            assert all(n - j == lam for j in matches)
            break
        table[valuation(n)] = (value(n), n)
    threshold = (lam - 1).bit_length() - 1
    j = next(j for j in range(lam) if valuation(mu + j) >= threshold)
    assert n == mu + lam + j
    multiplicities = Counter(value(i) for i in range(n + 1))
    assert max(multiplicities.values()) <= 2
    assert sum(v == 2 for v in multiplicities.values()) <= max(1, 2 ** threshold)


def random_maps(m):
    joint, cycles_hist, longest_hist, roots_hist = Counter(), Counter(), Counter(), Counter()
    no_fixed = 0
    for f in product(range(m), repeat=m):
        cycles, component, depths = decompose(f)
        cycles_hist[len(cycles)] += 1
        longest_hist[max(map(len, cycles))] += 1
        if all(len(c) == 1 for c in cycles):
            roots_hist[len(cycles)] += 1
        no_fixed += all(f[x] != x for x in range(m))
        for start in range(m):
            mu, lam = orbit(f, start)
            assert mu == depths[start] and lam == len(cycles[component[start]])
            joint[mu, lam] += 1
    total = m ** (m + 1)
    Q = F(0)
    survival = F(1)
    for j in range(m):
        if j:
            survival *= F(m - j, m)
        Q += survival
        for mu in range(j + 1):
            lam = j + 1 - mu
            assert F(joint[mu, lam], total) == survival / m
    assert sum(joint.values()) == total
    assert F(sum(lam * count for (mu, lam), count in joint.items()), total) == (Q + 1) / 2
    assert F(sum(mu * count for (mu, lam), count in joint.items()), total) == (Q - 1) / 2
    assert F(sum(count for (mu, lam), count in joint.items() if lam == 1), total) == Q / m
    assert no_fixed == (m - 1) ** m
    expected_cycles = sum((F(factorial(m), factorial(m - j) * j * m ** j) for j in range(1, m + 1)), F(0))
    assert F(sum(c * count for c, count in cycles_hist.items()), m ** m) == expected_cycles
    assert cycles_hist[1] == m ** (m - 1) * Q
    # Independent forest/permutation decomposition, answers 13 and 14.
    derived_longest, derived_cycles = Counter(), Counter()
    for n in range(1, m + 1):
        forests = comb(m - 1, n - 1) * m ** (m - n)
        assert roots_hist[n] == forests
        for perm in permutations(range(n)):
            lengths = []
            seen = set()
            for x in range(n):
                if x not in seen:
                    length, y = 0, x
                    while y not in seen:
                        seen.add(y)
                        length += 1
                        y = perm[y]
                    lengths.append(length)
            derived_longest[max(lengths)] += forests
            derived_cycles[len(lengths)] += forests
    assert derived_longest == longest_hist and derived_cycles == cycles_hist
    return dict(m=m, functions=m ** m, rooted_orbits=total, Q=str(Q), expected_cycle_count=str(expected_cycles))


def main():
    table = '''1 6065038420
3 6065038420
4 6910360760
5 8031120760
6 1968879240
7 7924019688
8 9631707688
9 8520606577
10 8520506578
11 8520506578
12 0323372207
6 9676627793
7 2779396766
8 4942162766
9 3831051655
10 3830951656
11 3830951656
12 1905867781
12 3319967479
6 6680032521
7 3252166800
8 2218966800
9 1107855700
10 1107755701
11 1107755701
12 1226919902
5 0048821902
6 9862877579
7 7757998628
8 2384626628
9 1273515517
10 1273415518
11 1273415518
12 5870802097
11 5870802097
12 3172562687
4 1540029446
5 7015475446
6 2984524554
7 2455429845
8 2730274845
9 1620163734
10 1620063735
11 1620063735
12 6065038420'''
    expected = [tuple(map(int, row.split())) for row in table.splitlines()]
    trace = []
    assert algorithm_k(6065038420, trace) == 6065038420 and trace == expected
    chain = [3830951656, 5870802097, 1226919902, 3172562687, 3319967479, 6065038420]
    assert [algorithm_k(x) for x in chain] == chain[1:] + chain[-1:]
    assert algorithm_k(5008502835) == 5008502835
    cycle3 = [225923640, 2811514413, 590051662]
    assert [algorithm_k(x) for x in cycle3] == cycle3[1:] + cycle3[:1]
    assert 5772156649 ** 2 == 33317792380594909201
    assert (5772156649 ** 2 // 10 ** 5) % MOD == 7923805949
    assert (1010101010 ** 2 // 10 ** 5) % MOD == 3040504030
    assert 3792 ** 2 == 14379264 and 3 * 79 * 2 ** 4 == 3792
    graph = [(x * x // 10) % 100 for x in range(100)]
    cycles, components, depth = decompose(graph)
    basins = {tuple(c): components.count(i) for i, c in enumerate(cycles)}
    assert basins == {(0,): 62, (10,): 19, (24, 57): 3, (50,): 1, (60,): 15}
    lengths = [depth[x] + len(cycles[components[x]]) for x in range(100)]
    assert max(lengths) == 15 and [x for x, n in enumerate(lengths) if n == 15] == [42, 69]
    binary = array('i', (((x * x) >> 10) & ((1 << 20) - 1) for x in range(1 << 20)))
    binary_cycles, _, _ = decompose(binary)
    assert len(binary_cycles) == 13 and max(map(len, binary_cycles)) == 142
    for mu in range(128):
        for lam in range(1, 129):
            detection(mu, lam)
    maps = [random_maps(m) for m in range(1, 7)]
    result = dict(status='all assertions passed', table_1_rows=len(expected),
                  known_erratum_1998=dict(fixed_point=5008502835, three_cycle=cycle3),
                  middle_square_100_basins={','.join(map(str, k)): v for k, v in basins.items()},
                  middle_square_20bit_states=1 << 20,
                  middle_square_20bit_cycle_lengths=sorted(map(len, binary_cycles)),
                  detectors_mu_range=[0, 127], detectors_lambda_range=[1, 128], detector_cases=128 ** 2,
                  random_maps=maps,
                  limits=['Algorithm K global cycle census and full preimage counts not checked here.',
                          'Sedgewick/Szymanski/Yao algorithm and optimal Brent base not checked here.',
                          'Asymptotic estimates are justified in notes, not by these finite tests.'])
    (ROOT / 'results/intro.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
