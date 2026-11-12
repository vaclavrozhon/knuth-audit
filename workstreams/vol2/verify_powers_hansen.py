#!/usr/bin/env python3
"""Exact checks of Hansen's multiset structure and constructive upper bound.

These are new properties of chains, not repeated minimum-length searches.
General proofs are in notes/powers-hansen.md.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
from itertools import combinations_with_replacement
import json
from pathlib import Path
import time

BASE = Path(__file__).resolve().parent
RESULT = BASE / 'results/powers-hansen.json'


def bits(n):
    return [i for i in range(n.bit_length()-1, -1, -1) if n >> i & 1]


def partition(exponents):
    """The book's increasing-order, lowest-final-bit-first partition."""
    remaining = iter(sorted(exponents))
    n = sum(1 << x for x in exponents)
    groups = []
    for e in reversed(bits(n)):
        left = 1 << e
        group = []
        while left:
            x = next(remaining)
            assert 1 << x <= left
            left -= 1 << x
            group.append(x)
        groups.append(group)
    assert next(remaining, None) is None
    return list(reversed(groups))


def partition_block():
    count = groups = 0
    for size in range(1, 11):
        for exponents in combinations_with_replacement(range(8), size):
            n = sum(1 << x for x in exponents)
            result = partition(exponents)
            assert sorted(x for group in result for x in group) == list(exponents)
            for e, group in zip(bits(n), result):
                assert sum(1 << x for x in group) == 1 << e
                assert all(e >= x > e-len(group) for x in group)
                assert len(group) <= size-len(result)+1
                groups += 1
            count += 1
    return {'multisets': count, 'binary_groups': groups,
            'exponents': [0, 7], 'multiplicity_total': [1, 10]}


def structure(chain):
    S, d, f = [[0]], [0], [0]
    choices = []
    for i in range(1, len(chain)):
        k = chain[:i].index(chain[i]-chain[i-1])
        choices.append(k)
        double = k == i-1
        S.append([x+1 for x in S[-1]] if double else sorted(S[-1]+S[k]))
        d.append(d[-1]+double)
        f.append(f[-1]+(not double))
        assert sum(1 << x for x in S[-1]) == chain[i]
        assert max(S[-1]) == d[-1] and len(S[-1]) <= 1 << f[-1]
    M = [None]*len(chain)
    M[-1] = partition(S[-1])
    for i in range(len(chain)-2, -1, -1):
        k = choices[i]
        if k == i:
            M[i] = [[x-1 for x in group] for group in M[i+1]]
        else:
            row = [group[:] for group in M[i+1]]
            for x in S[k]:
                for group in reversed(row):
                    if x in group:
                        group.remove(x)
                        break
                else:
                    raise AssertionError('No occurrence to remove')
            M[i] = row
    e = bits(chain[-1])
    sizes = list(map(len, M[-1]))
    locations = {}
    for i, row in enumerate(M):
        assert sorted(x for group in row for x in group) == sorted(S[i])
        assert d[i] in row[0]
        for j, group in enumerate(row):
            for x in group:
                assert x >= 0 and e[j]+d[i]-d[-1] >= x > e[j]+d[i]-d[-1]-sizes[j]
                locations.setdefault(x, set()).add((i, j))
            # Independent weight bound, stronger than the pointwise estimate.
            assert sum(1 << x for x in group) << (d[-1]-d[i]) <= 1 << e[j]
    pairs = 0
    for positions in locations.values():
        for i, j in positions:
            for u, v in positions:
                difference = e[j]-e[v]-(d[u]-d[i])
                assert -sizes[v] < difference < sizes[j]
                pairs += 1
    return M, pairs


def structure_block():
    counts = Counter()
    pairs = 0
    path = [1]
    def visit():
        nonlocal pairs
        depth = len(path)-1
        _, checked = structure(path)
        pairs += checked
        counts[depth] += 1
        if depth < 8:
            last = path[-1]
            for a in path[:]:
                path.append(last+a)
                visit()
                path.pop()
    visit()
    example = [1, 2, 3, 5, 10, 20, 23]
    actual, _ = structure(example)
    expected = [[[0], [], [], []], [[1], [], [], []],
                [[1], [0], [], []], [[1, 1], [0], [], []],
                [[2, 2], [1], [], []], [[3, 3], [2], [], []],
                [[3, 3], [2], [1], [0]]]
    assert actual == expected
    family_counts = Counter()
    # Explicit answer 20, independent closed forms for every row.
    for a in range(1, 9):
        pure = [1 << j for j in range(a+1)]
        for c in range(2, 9):
            chain = pure+[3*(1 << (a-1)), 5*(1 << (a-1))]
            chain += [1 << (a+j) for j in range(2, c+1)]
            actual, _ = structure(chain)
            target = [[[j]] for j in range(a+1)]
            target += [[[a-1, a]], [[a-1, a, a]]]
            target += [[[a+j-3, a+j-3, a+j-2, a+j-2, a+j-2]]
                       for j in range(2, c+1)]
            assert actual == target
            family_counts['type3'] += 1
        for c in range(1, 9):
            for tail in range(9):
                chain = pure+[3*(1 << (a-1))]
                for _ in range(c): chain.append(2*chain[-1])
                chain.append((1 << (a+c+1))+(1 << (a+c-2)))
                for _ in range(tail): chain.append(2*chain[-1])
                actual, _ = structure(chain)
                target = [[[j], []] for j in range(a+1)]
                target += [[[a-1+j, a+j], []] for j in range(c+1)]
                target += [[[a+c-1+j, a+c-1+j, a+c+j], [a+c-2+j]]
                           for j in range(tail+1)]
                assert actual == target
                family_counts['type5'] += 1
    return {'star_chains_by_length': dict(counts), 'chains': sum(counts.values()),
            'lemma_K_ordered_location_pairs': pairs,
            'printed_example': expected,
            'answer20_parameter_cases': dict(family_counts)}


def construct_F(x, y, A):
    xb, yb = bits(x), bits(y)
    assert xb[0]+yb[0] <= A
    top = A-yb[0]
    values = {1 << j for j in range(top+1)}
    underlined = set(values)
    witness = {1 << j: (1 << (j-1), 1 << (j-1)) for j in range(1, top+1)}
    partial = 1 << xb[-1]
    for j in reversed(xb[:-1]):
        next_partial = partial+(1 << j)
        witness[next_partial] = (partial, 1 << j)
        values.add(next_partial)
        partial = next_partial
    chain = sorted(values)
    current = 1 << top
    for i, exponent in enumerate(yb):
        value = current+x
        witness[value] = (current, x)
        chain.append(value)
        underlined.add(value)
        current = value
        next_exponent = yb[i+1] if i+1 < len(yb) else 0
        for _ in range(exponent-next_exponent):
            witness[2*current] = (current, current)
            current *= 2
            chain.append(current)
            underlined.add(current)
    return chain, underlined, witness


def validate_F(x, y, A):
    chain, marked, witness = construct_F(x, y, A)
    assert chain[0] == 1 and chain[-1] == (1 << A)+x*y
    assert len(chain)-1 == A+x.bit_count()+y.bit_count()-1
    seen = {1}
    previous_mark = 1
    for i, value in enumerate(chain[1:], 1):
        assert value > chain[i-1]
        a, b = witness[value]
        assert a in seen and b in seen and a+b == value
        # Check the l^0 property without using the construction's witnesses.
        assert value-previous_mark in seen
        seen.add(value)
        if value in marked: previous_mark = value
    return len(chain)-1


def construction_block():
    counts = Counter()
    for x in range(1, 129):
        for y in range(1, 129):
            bound = x.bit_length()+y.bit_length()-2
            for extra in range(3):
                validate_F(x, y, bound+extra)
                counts['equality' if extra == 0 else 'strict'] += 1
    x, y, A = (1 << 1016)+1, (1 << 2032)+1, 6103
    length = validate_F(x, y, A)
    e = bits((1 << A)+x*y)
    t = len(e)-1
    m = (1 << (3271*(t-1)//1000))-t
    assert e == [6103, 3048, 2032, 1016, 0] and m == 508
    assert 1000*(e[0]-2*e[1]) > 2271*(t-1)
    assert all(e[i-1]-e[i] >= 2*m for i in range(1, len(e)))
    assert length == 6106 and e[0]+t == 6107
    # Only the exponent algebra of answer 21: do not allocate gigantic n.
    family = []
    for q in range(1, 101):
        u = 1 << (8*q+5)
        t = 2*q+2
        m = (1 << (3271*(t-1)//1000))-t
        assert u >= 2*m and 2000*u > 2271*(t-1)
        # Exponents of xy are disjoint, precisely 0,u,...,(2q+1)u.
        exponents = [a+b for a in range(q+1) for b in (0, q+1)]
        assert sorted(exponents) == list(range(2*q+2))
        assert (4*(q+1)*u+2*q+2)-(4*(q+1)*u+q+2) == q
        family.append({'q':q, 'u_bit_length':u.bit_length(), 'gap_lower_bound':q})
    return {'finite_constructions': dict(counts),
            'book_example': {'exponents':e,'m':508,'general_length':6106,'star_minimum_by_H':6107},
            'answer21_symbolic_parameter_checks': family,
            'giant_integer_allocated_for_answer21': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('block', choices=['partition', 'structure', 'construction'])
    args = parser.parse_args()
    data = json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert args.block not in data['blocks'], 'Do not repeat a passed block'
    start = time.perf_counter()
    result = globals()[args.block+'_block']()
    data['blocks'][args.block] = {'status':'passed', 'seconds':time.perf_counter()-start,
                                 'result':result}
    data['updated_at_utc'] = datetime.now(timezone.utc).isoformat()
    RESULT.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'block':args.block,**data['blocks'][args.block]}),flush=True)
