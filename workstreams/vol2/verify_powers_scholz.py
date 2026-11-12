#!/usr/bin/env python3
"""Check the marked-chain transformation in G and exercise 24.

The generator and the validators use different descriptions of valid
markings. No shortest-chain computations are performed.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import time

BASE = Path(__file__).resolve().parent
RESULT = BASE/'results/powers-scholz.json'


def marked_chains(max_depth):
    chain, marked = [1], {1}
    def visit():
        if chain[-1] in marked:
            yield tuple(chain), frozenset(marked)
        if len(chain)-1 == max_depth:
            return
        anchor = max(marked)
        for value in sorted({anchor+a for a in chain if anchor+a > chain[-1]}):
            chain.append(value)
            yield from visit()
            marked.add(value)
            yield from visit()
            marked.remove(value)
            chain.pop()
    yield from visit()


def validate(chain, marked):
    assert chain[0] == 1 and chain[-1] in marked and 1 in marked
    assert marked <= set(chain)
    seen = {1}
    for i, value in enumerate(chain[1:], 1):
        assert value > chain[i-1]
        anchor = max(x for x in marked if x < value)
        assert value-anchor in seen
        seen.add(value)


def transform(chain, marked, base_chain=(1, 2), base_marked=frozenset([1, 2])):
    B, h = base_chain[-1], len(base_chain)-1
    assert B > 1
    n = chain[-1]
    # Repunits are formed by recurrence, rather than the quotient formula.
    R = [0]
    for _ in range(n): R.append(B*R[-1]+1)
    values = [R[a] for a in chain]
    output_marks = {R[a] for a in marked}
    anchors = sorted(marked)
    for b, next_b in zip(anchors, anchors[1:]):
        Q = R[b]
        for _ in range(next_b-b):
            for c in base_chain[1:]:
                values.append(c*Q)
                if c in base_marked: output_marks.add(c*Q)
            Q *= B
    assert len(set(values)) == len(values), 'The two families must not overlap'
    result = sorted(values)
    assert len(result)-1 == len(chain)-1+(n-1)*h
    assert result[-1] == (B**n-1)//(B-1)
    validate(result, output_marks)
    return result, output_marks


def binary_block():
    counts, star_counts = Counter(), Counter()
    generated_numbers = 0
    for chain, marked in marked_chains(7):
        validate(chain, marked)
        out, marks = transform(chain, marked)
        counts[len(chain)-1] += 1
        generated_numbers += len(out)
        if len(marked) == len(chain):
            assert len(marks) == len(out)
            assert all(out[i]-out[i-1] in out[:i] for i in range(1,len(out)))
            star_counts[len(chain)-1] += 1
    original = (1, 2, 4, 5, 8, 10, 12, 18)
    original_marks = frozenset([1, 2, 4, 8, 18])
    actual, marks = transform(original, original_marks)
    expected = [1,2,3,6,12,15,30,31,60,120,240,255,510,1020,1023,2040,
                4080,4095,8160,16320,32640,65280,130560,261120,262143]
    assert actual == expected
    assert set(expected)-marks == {31,1023,4095}
    return {'marked_chains_by_length':dict(counts), 'chains':sum(counts.values()),
            'all_marked_star_chains_by_length':dict(star_counts),
            'total_output_numbers':generated_numbers,
            'printed_example':expected,'unmarked_example_values':sorted(set(expected)-marks)}


def radix_block():
    inputs = list(marked_chains(5))
    bases = [(c,m) for c,m in marked_chains(4) if c[-1] > 1]
    count = nonbinary = 0
    base_values, final_bits = set(), 0
    for chain, marks in inputs:
        validate(chain, marks)
        for base_chain, base_marks in bases:
            validate(base_chain, base_marks)
            output, _ = transform(chain,marks,base_chain,base_marks)
            count += 1
            nonbinary += base_chain[-1] > 2
            base_values.add(base_chain[-1])
            final_bits = max(final_bits, output[-1].bit_length())
    return {'input_marked_chains':len(inputs),'base_marked_chains':len(bases),
            'transformations':count,'nonbinary_transformations':nonbinary,
            'base_values':sorted(base_values),'maximum_target_bits':final_bits}


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('block',choices=['binary','radix'])
    args = p.parse_args()
    data = json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert args.block not in data['blocks'], 'Do not repeat a passed block'
    start = time.perf_counter()
    result = globals()[args.block+'_block']()
    data['blocks'][args.block] = {'status':'passed','seconds':time.perf_counter()-start,'result':result}
    data['updated_at_utc'] = datetime.now(timezone.utc).isoformat()
    RESULT.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'block':args.block,**data['blocks'][args.block]}),flush=True)
