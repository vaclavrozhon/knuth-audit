"""Validate the independent census implementation and, if present, its cycles."""
import argparse
import json
from pathlib import Path
import random
import subprocess
from verify_intro import algorithm_k, k_pass, decompose

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--binary')
    parser.add_argument('--census', type=Path)
    args = parser.parse_args()
    report = {}
    if args.binary:
        rng = random.Random(31012026)
        inputs = set(range(10000))
        inputs.update(rng.randrange(10 ** 10) for _ in range(20000))
        for k in range(1, 100):
            inputs.update([k * 10 ** 8 - 1, k * 10 ** 8, k * 10 ** 8 + 1])
        for target in [6065038420, 5008502835]:
            inputs.update(x for x, _ in json.loads((ROOT / f'results/k-basin-{target}.json').read_text())['inverse_edges'])
        inputs = sorted(inputs)
        run = subprocess.run([args.binary, '--map'], input=''.join(f'{x}\n' for x in inputs), text=True, capture_output=True, check=True)
        values = list(map(int, run.stdout.splitlines()))
        assert len(values) == len(inputs)
        for x, y in zip(inputs, values):
            assert y == k_pass(x), (x, y, k_pass(x))
        report['implementation_cross_checks'] = len(inputs)
    if args.census:
        data = json.loads(args.census.read_text())
        assert data['status'] == 'exhaustive census completed'
        assert data['domain_size'] == data['visited'] == 10 ** 10
        for key, function in [('g_cycles', k_pass), ('algorithm_k_cycles', algorithm_k)]:
            all_nodes = set()
            for cycle in data[key]:
                assert cycle and len(cycle) == len(set(cycle))
                assert not all_nodes.intersection(cycle)
                all_nodes.update(cycle)
                assert [function(x) for x in cycle] == cycle[1:] + cycle[:1]
            report[key + '_lengths'] = sorted(map(len, data[key]))
        # Independently recover ALL f-cycles on the complete set of g-cyclic
        # vertices. decompose peels indegree-zero vertices, unlike the C++ walk.
        nodes = sorted(x for cycle in data['g_cycles'] for x in cycle)
        index = {x: i for i, x in enumerate(nodes)}
        successors = [index[algorithm_k(x)] for x in nodes]
        recovered, _, _ = decompose(successors)
        def canonical(cycle):
            i = cycle.index(min(cycle))
            return tuple(cycle[i:] + cycle[:i])
        expected = {canonical([nodes[i] for i in c]) for c in recovered}
        actual = {canonical(c) for c in data['algorithm_k_cycles']}
        assert actual == expected
        report['independent_f_graph_vertices'] = len(nodes)
        report['independent_f_cycle_decomposition'] = 'indegree peeling; all cycles agree'
        report['completeness'] = 'Exhaustive census plus the graph proof in notes; validator checks every cycle edge independently.'
    assert report, 'Supply --binary and/or --census.'
    report['status'] = 'all assertions passed'
    suffix = 'complete' if args.census else 'implementation'
    (ROOT / f'results/k-census-{suffix}-validation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
