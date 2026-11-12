#!/usr/bin/env python3
"""Independent monotone certificate covering all 2^32 subsets, without solving."""
from collections import Counter
from datetime import datetime, timezone
import json
from dlx1_audit_tools import ROOT, sha, statistics, input_text
from check_sudoku_native import instance
from check_sudoku_basics import UNITS

OUT = ROOT/'results/sudoku_minimal'


def main():
    result = json.loads((OUT/'minimal.json').read_text())
    queries = json.loads((OUT/'subset-queries.json').read_text())
    initial = json.loads((ROOT/'results/sudoku_basics/pdf-grids.json').read_text())['sources']['29a']['board']
    reference = result['reference']
    positions = result['clue_positions']
    assert positions == [v for v,k in enumerate(initial) if k]
    assert all({reference[v] for v in u} == set(range(1,10)) for u in UNITS)
    assert all(not k or k == reference[v] for v,k in enumerate(initial))
    query_map = {q['mask']:q for q in queries}
    full = (1<<32)-1
    negative = []
    for q in queries:
        if q['unique']:
            assert q['alternative'] is None
            continue
        b = q['alternative']
        assert len(b) == 81 and b != reference
        assert all({b[v] for v in u} == set(range(1,10)) for u in UNITS)
        assert all(not(q['mask']>>i&1) or b[v] == initial[v] for i,v in enumerate(positions))
        negative.append(q['mask'])
    mandatory = sum(1<<i for i in range(32) if not query_map[full^(1<<i)]['unique'])
    optional = [i for i in range(32) if not mandatory>>i&1]
    assert mandatory.bit_count() == 10 and len(optional) == 22
    def project(mask):
        assert mask & mandatory == mandatory
        return sum(1<<j for j,i in enumerate(optional) if mask>>i&1)
    good = 0
    minimal = [s['mask'] for s in result['native_minimals']]
    assert len(set(minimal)) == 777
    for stats in result['native_minimals']:
        mask = stats['mask']
        board = [0]*81
        for i,v in enumerate(positions):
            if mask>>i&1:
                board[v] = initial[v]
        names, rows, _, primary = instance(board)
        path = OUT/'minimal-native'/f'{mask:08x}.dlx'
        assert path.read_text() == input_text(names,rows,primary)
        assert sha(path) == stats['input_sha256']
        independent = statistics(path.with_suffix('.log').read_text())
        assert independent['solutions'] == 1
        assert all(stats[k] == v for k,v in independent.items())
        good |= 1 << project(mask)
    bad = 0
    for mask in negative:
        if mask & mandatory == mandatory:
            bad |= 1 << project(mask)
    n = 1<<22
    universe = (1<<n)-1
    # A bit indexed by clue mask X represents the proposition about X.
    # Upward closure of minimal positives; downward closure of negative witnesses.
    for i in range(22):
        stride = 1<<i
        low_blocks = universe // ((1<<stride)+1)
        good |= (good & low_blocks) << stride
        bad |= (bad >> stride) & low_blocks
    assert good & bad == 0 and good | bad == universe
    good_bytes = good.to_bytes(n//8,'little')
    bad_bytes = bad.to_bytes(n//8,'little')
    histogram = Counter()
    for byte_index,bits in enumerate(good_bytes):
        while bits:
            bit = bits & -bits
            index = 8*byte_index+bit.bit_length()-1
            histogram[index.bit_count()+10] += 1
            bits -= bit
    assert dict(histogram) == {23:22,24:373,25:1950,26:4244,27:4609,28:2780,29:978,30:200,31:22,32:1}
    assert good.bit_count() == sum(histogram.values()) == 15179
    for mask in minimal:
        for i in optional:
            if mask>>i&1:
                child = project(mask^(1<<i))
                assert bad_bytes[child//8] >> (child%8) & 1
    (OUT/'unique-subsets.bits').write_bytes(good_bytes)
    (OUT/'nonunique-subsets.bits').write_bytes(bad_bytes)
    record = dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__),minimal_result_sha256=sha(OUT/'minimal.json'),
                  queries_sha256=sha(OUT/'subset-queries.json'),mandatory_clue_mask=mandatory,
                  optional_clue_indices=optional,negative_witnesses=len(negative),
                  total_subsets_covered=1<<32,mandatory_containing_subsets=n,
                  unique_subsets=good.bit_count(),unique_by_clues=dict(sorted(histogram.items())),
                  unique_bitset_sha256=sha(OUT/'unique-subsets.bits'),
                  nonunique_bitset_sha256=sha(OUT/'nonunique-subsets.bits'),
                  bitset_format='Little endian, index is mask of optional clue indices in the given order; all10 mandatory clues included.',
                  proof='Every missing-mandatory subset inherits a validated alternative from full minus that clue. '
                        'The remaining2^22 masks are partitioned exactly into supersets of777 independently DLX-certified '
                        'unique puzzles and subsets of validated nonunique witnesses. The closures are disjoint and exhaustive. '
                        'No trust in the subset-oracle search or its traversal is needed for completeness.')
    (OUT/'minimal-certificate.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ('total_subsets_covered','negative_witnesses','unique_subsets','unique_by_clues')},indent=2))


if __name__ == '__main__':
    main()
