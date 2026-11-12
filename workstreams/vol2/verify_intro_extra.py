"""Independent validation of K inverse certificates; Foata--Fuchs bijection."""
from collections import Counter
from itertools import product
from pathlib import Path
import json
import mpmath as mp
from verify_intro import algorithm_k, k_pass, decompose

ROOT = Path(__file__).resolve().parent


def encode(f):
    cycles, _, _ = decompose(f)
    # Canonical cycle notation of the INVERSE permutation on cyclic vertices.
    blocks = []
    for cycle in cycles:
        assert cycle[0] == min(cycle)
        blocks.append(cycle[:1] + cycle[:0:-1])
    blocks.sort(key=lambda x: x[0], reverse=True)
    out = [x for block in blocks for x in block]
    visited = set(out)
    leaves = sorted(set(range(len(f))) - set(f))
    for leaf in leaves:
        path = [leaf]
        x = leaf
        while x not in visited:
            visited.add(x)
            x = f[x]
            path.append(x)
        out.extend(reversed(path[1:]))
    assert len(out) == len(f) and len(visited) == len(f)
    return tuple(out)


def decode(seq):
    n = len(seq)
    distinct = set()
    k = 0
    while k < n and seq[k] not in distinct:
        distinct.add(seq[k])
        k += 1
    f = [-1] * n
    # Split the distinct prefix at its left-to-right minima.
    blocks = []
    minimum = n
    for x in seq[:k]:
        if x < minimum:
            minimum = x
            blocks.append([])
        blocks[-1].append(x)
    for block in blocks:
        for i, x in enumerate(block):
            f[x] = block[i - 1]
    nameless = []
    seen = set(seq[:k])
    for i in range(k, n):
        parent = seq[i]
        seen.add(parent)
        if i + 1 < n and seq[i + 1] not in seen:
            child = seq[i + 1]
            assert f[child] == -1
            f[child] = parent
        else:
            nameless.append(parent)
    unused = sorted(set(range(n)) - set(seq))
    assert len(unused) == len(nameless)
    for child, parent in zip(unused, nameless):
        assert f[child] == -1
        f[child] = parent
    assert all(x >= 0 for x in f)
    return tuple(f)


def verify_basin(target, expected_count, expected_min, expected_max):
    data = json.loads((ROOT / f'results/k-basin-{target}.json').read_text())
    edges = data['inverse_edges']
    successor = dict(edges)
    assert len(successor) == len(edges) == expected_count == data['count']
    nodes = set(successor)
    assert min(nodes) == expected_min == data['minimum']
    assert max(nodes) == expected_max == data['maximum']
    for x, y in edges:
        assert k_pass(x) == y and y in nodes
    full = {x: algorithm_k(x) for x in nodes}
    assert full[target] == target
    depths = []
    for x in nodes:
        seen = set()
        while x != target:
            assert x in nodes and x not in seen
            seen.add(x)
            x = full[x]
        depths.append(len(seen))
    return dict(target=target, count=len(nodes), minimum=min(nodes), maximum=max(nodes),
                max_iterations_to_fixed_point=max(depths), independently_validated_edges=len(edges),
                completeness='Exact inverse enumeration, justified in notes; this validator checks every returned node and edge.')


def main():
    example_f = (3, 1, 4, 1, 5, 9, 2, 6, 5, 4)
    example_s = (4, 9, 5, 1, 1, 3, 4, 2, 6, 5)
    assert encode(example_f) == example_s and decode(example_s) == example_f
    assert decode(example_f) == (6, 4, 9, 3, 1, 1, 2, 5, 4, 5)
    counts = []
    for m in range(1, 7):
        images = set()
        for f in product(range(m), repeat=m):
            seq = encode(f)
            assert decode(seq) == f and seq not in images
            images.add(seq)
            assert Counter(seq) == Counter(f)
            cycles, _, _ = decompose(f)
            cyclic = set(x for cycle in cycles for x in cycle)
            k = len(cyclic)
            assert set(seq[:k]) == cyclic and len(set(seq[:k])) == k
            if k < m:
                assert seq[k] in cyclic
            minima = {min(c) for c in cycles}
            for j in range(1, m):
                if seq[j] not in seq[:j] and seq[j] not in minima:
                    assert f[seq[j]] == seq[j - 1]
            if m > 1:
                assert (seq[0] == seq[1]) == (len(cycles) == 1 and len(cycles[0]) == 1)
        assert len(images) == m ** m
        counts.append(dict(m=m, functions=m ** m, distinct_codes=len(images)))
    basins = [verify_basin(6065038420, 597, 9612809, 9995371004),
              verify_basin(5008502835, 128, 8502835, 9944390948)]
    mp.mp.dps = 60
    probability = mp.exp(mp.loggamma(1000001) - 10 * mp.loggamma(100001) - 1000000 * mp.log(10))
    approximation = 1 / (16 * mp.pi ** 4 * mp.mpf(10) ** 22 * mp.sqrt(2 * mp.pi))
    assert mp.mpf('2.555e-26') < probability < mp.mpf('2.565e-26')
    assert abs(probability / approximation - 1) < mp.mpf('0.00001')
    result = dict(status='all assertions passed', foata_fuchs=counts, algorithm_k_basins=basins,
                  probability_3_1_2=mp.nstr(probability, 40),
                  stated_stirling_approximation=mp.nstr(approximation, 40),
                  relative_difference=mp.nstr(probability / approximation - 1, 15))
    (ROOT / 'results/intro-extra.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
