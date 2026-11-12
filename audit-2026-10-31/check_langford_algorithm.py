#!/usr/bin/env python3
"""Literal Algorithm L / answers 20--22 against label-first exact enumeration.

No external packages.  Printed positions are one-based throughout Algorithm L;
the independent oracle places labels from n down to 1, rather than filling the
first blank.  All returned arrangements are checked directly from definition.
"""
import argparse
import hashlib
import json
from pathlib import Path


class PrintedSymmetryLoop(Exception):
    def __init__(self, state):
        self.state = state


def distance(k, loose):
    return (3*k)//2 if loose else k+1


def valid(x, loose=False):
    n = len(x)//2
    return (len(x) == 2*n and set(x) == set(range(1, n+1)) | set(range(-n, 0))
            and all(x.index(-k)-x.index(k) == distance(k, loose)
                    for k in range(1, n+1)))


def dual(x):
    return tuple(-k for k in x[::-1])


def oracle(n, loose=False):
    x = [0]*(2*n)
    out = []

    def place(k):
        if k == 0:
            out.append(tuple(x))
            return
        d = distance(k, loose)
        for i in range(2*n-d):
            if x[i] == x[i+d] == 0:
                x[i], x[i+d] = k, -k
                place(k-1)
                x[i] = x[i+d] = 0

    place(n)
    return sorted(out)


def algorithm_l(n, loose=False, force=False, symmetry=False, repaired_symmetry=False):
    assert n >= 1 and (not symmetry or force)
    # n=1,2 in the loose version are self-dual, explicitly separated in answer22.
    assert not (loose and symmetry and n < 4)
    x = [0]*(2*n+1)
    p = list(range(1, n+1)) + [0]
    y = [None]*(2*n+1)
    a = [0]*(n+1)
    l, step, depth = 1, 2, 0
    out, snapshots, tree, conflicts = [], [], [], []
    profile = [0]*(n+1)
    if loose:
        special = n - (0, 1, 2, 0)[n % 4]
        half = n//4 + (0, 1, 2, 1)[n % 4]
        force_start = (n+1)//2
    else:
        special = n - (n % 2 == 0)
        half = n//2
        force_start = n-1

    def required():
        q = (4*n+2-2*l)//3 if loose else 2*n-l-1
        if l < force_start:
            return 0
        assert 1 <= q <= n, (n, loose, force, symmetry, l, x, q)
        return q if a[q] == 0 else 0

    def invariants():
        chain, k = [], p[0]
        while k:
            assert k not in chain and 1 <= k <= n
            chain.append(k)
            k = p[k]
        assert chain == sorted(set(range(1, n+1)) - set(x))
        assert sum(a) == depth
        for k in range(1, n+1):
            if a[k]:
                assert k in x and -k in x
                assert x.index(-k)-x.index(k) == distance(k, loose)
            else:
                assert k not in x and -k not in x

    while True:
        if step == 2:
            invariants()
            profile[depth] += 1
            if n == 4 and not loose and not force:
                tree.append([v for v in x if v > 0])
            if n == 4 and not loose and l == 4 and x[1:4] == [2, 4, 1]:
                snapshots.append({'x4_to_8': x[4:], 'p': p.copy(),
                                  'y1_to_8': y[1:]})
            k = p[0]
            if k == 0:
                assert valid(tuple(x[1:]), loose)
                out.append(tuple(x[1:]))
                step = 5
                continue
            j = 0
            while x[l] < 0:
                if force and ((symmetry and l == half and not a[special])
                              or required()):
                    break
                l += 1
            else:
                step = 3
                continue
            step = 5
        elif step == 3:
            assert k == p[j] and k != 0 and x[l] == 0
            if l+distance(k, loose) > 2*n:
                step = 5
                continue
            if symmetry and l == half and a[special] == 0:
                q = required()
                if q and q != special:
                    conflicts.append({'l': l, 'x': x[1:].copy(),
                                      'symmetry_label': special, 'deadline_label': q})
                    if repaired_symmetry:
                        step = 5
                        continue
                while k != special:
                    j, k = k, p[k]
                    if k == 0:
                        # The printed loop next takes p[0], revisits the same
                        # forced label, fails, and repeats the identical L4.
                        raise PrintedSymmetryLoop({'n':n, 'loose':loose, 'l':l,
                                                   'x':x[1:].copy(), 'p':p.copy(),
                                                   'special':special,
                                                   'solutions_before_loop':len(out)})
            if force and required():
                while l+distance(k, loose) != 2*n:
                    j, k = k, p[k]
                    assert k, ('forcing walked past end', n, loose, l, x, p)
            target = l+distance(k, loose)
            assert target <= 2*n
            if x[target] == 0:
                x[l], x[target], y[l], p[j] = k, -k, j, p[k]
                a[k] = 1
                depth += 1
                l += 1
                step = 2
            else:
                step = 4
        elif step == 4:
            if repaired_symmetry and symmetry and l == half and k == special:
                step = 5
                continue
            j = k
            k = p[j]
            step = 3 if k else 5
        else:
            assert step == 5
            l -= 1
            if l <= 0:
                invariants()
                break
            while x[l] < 0:
                l -= 1
            assert l > 0 and x[l] > 0
            k = x[l]
            x[l] = x[l+distance(k, loose)] = 0
            j = y[l]
            p[j] = k
            a[k] = 0
            depth -= 1
            step = 5 if symmetry and l == half and k == special else 4
    assert out == sorted(set(out))
    return out, {'profile': profile, 'nodes': sum(profile),
                 'exercise18_snapshots': snapshots, 'positive_tree': tree,
                 'forcing_conflicts': conflicts}


def run(max_n):
    results = []
    for loose in (False, True):
        for n in range(1, max_n+1):
            expected = oracle(n, loose)
            assert all(valid(x, loose) for x in expected)
            assert set(map(dual, expected)) == set(expected)
            variants = {}
            for name, force, symmetry in [('L', False, False), ('L20', True, False),
                                           ('L21', True, True)]:
                if loose and symmetry and n < 4:
                    continue
                try:
                    got, stats = algorithm_l(n, loose, force, symmetry)
                except PrintedSymmetryLoop as failure:
                    assert loose and symmetry and n >= 10 and n%4 == 2
                    variants[name] = {'printed_nontermination': failure.state}
                    continue
                if symmetry:
                    assert all(x != dual(x) for x in expected)
                    assert set(got) | set(map(dual, got)) == set(expected)
                    if loose and n == 6:
                        assert len(got) == 13 and len(expected) == 20
                        duplicates = [x for x in got if dual(x) in got]
                        assert len(duplicates) == 6
                        stats['duplicated_dual_pairs'] = [list(x) for x in duplicates if x < dual(x)]
                    else:
                        assert not set(got) & set(map(dual, got))
                else:
                    assert got == expected, (loose, n, name)
                variants[name] = dict(solutions=len(got), **stats)
            if loose and n >= 4:
                got, stats = algorithm_l(n, loose, True, True, repaired_symmetry=True)
                assert len(got)*2 == len(expected)
                assert set(got) | set(map(dual, got)) == set(expected)
                assert not set(got) & set(map(dual, got))
                variants['L21_corrected'] = dict(solutions=len(got), **stats)
            if n == 4 and not loose:
                s = variants['L']['exercise18_snapshots']
                assert len(s) == 1 and s[0] == {
                    'x4_to_8': [-2,-1,0,-4,0], 'p':[3,3,3,0,0],
                    'y1_to_8':[1,3,0,2,0,None,None,None]}
                # Exact positive decisions in printed tree (9), viewed at p35.
                printed = [[], [1],[1,2],[1,2,3],[1,3],[1,3,2],[1,4],[1,4,3],
                           [2],[2,3],[2,3,1],[2,3,4],[2,3,4,1],[2,4],[2,4,1],
                           [3],[3,1],[3,1,2],[3,1,4],[3,4],[3,4,2],
                           [4],[4,1],[4,1,3],[4,1,3,2],[4,2],[4,2,3]]
                assert variants['L']['positive_tree'] == printed
            for stats in variants.values():
                if not (n == 4 and not loose):
                    stats.pop('exercise18_snapshots', None)
                    stats.pop('positive_tree', None)
            results.append({'loose': loose, 'n': n, 'solutions': len(expected),
                            'model_sha256': hashlib.sha256(repr(expected).encode()).hexdigest(),
                            'variants': variants})
            if loose and n == 6:
                remark = 'printed L21 has 13 instead of 10; corrected L21 agrees'
            elif loose and n >= 10 and n%4 == 2:
                remark = 'printed L21 loops; corrected L21 agrees'
            else:
                remark = 'all variants agree'
            print(f'loose={loose} n={n}: {len(expected)} solutions; {remark}', flush=True)
    loose_counts = [1,1,0,2,4,20,0,156,516,2008,0,52536,297800,1767792,0,75678864]
    for item in results:
        if item['loose']:
            assert item['solutions'] == loose_counts[item['n']-1]
    return {'verified': True, 'max_n': max_n, 'results': results}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=10)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run(args.max_n)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
