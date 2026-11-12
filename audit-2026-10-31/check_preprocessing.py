"""Exact SAT preprocessing checks, exercises 366--381.

Set-based truth tables are the semantic oracle. Sorted-list routines are
independent translations of 374. The exploitation-stack example isolates 376.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import json
import random


def clauses(n):
    return [frozenset((j+1)*v for j, v in enumerate(values) if v)
            for values in product((-1, 0, 1), repeat=n) if any(values)]


def sat_clause(c, x):
    return any(bool(x & (1 << (abs(l)-1))) == (l > 0) for l in c)


def models(f, n):
    return {x for x in range(1 << n) if all(sat_clause(c, x) for c in f)}


def resolve(c, d, literal):
    r = (c - {literal}) | (d - {-literal})
    return None if any(-l in r for l in r) else r


def eliminate(f, literal):
    a = [c for c in f if literal in c]
    b = [c for c in f if -literal in c]
    rest = {c for c in f if literal not in c and -literal not in c}
    resolvents = {r for c in a for d in b if (r := resolve(c, d, literal)) is not None}
    return rest | resolvents, a, b


def assign(x, literal, truth):
    mask = 1 << (abs(literal)-1)
    return (x | mask) if truth == (literal > 0) else (x & ~mask)


def substitution(f, literal, core):
    # 369 uses core C1=(l or l1 ... lr) and the r converse binaries.
    tails = core - {literal}
    a = [c for c in f if literal in c and c != core]
    b = [c for c in f if -literal in c]
    chosen = {frozenset((-literal, -u)) for u in tails}
    assert chosen <= set(b)
    result = {c for c in f if literal not in c and -literal not in c}
    pairs = [(core, d) for d in b if d not in chosen]
    pairs += [(c, d) for c in a for d in chosen]
    for c, d in pairs:
        if (r := resolve(c, d, literal)) is not None:
            result.add(r)
    p, q, r = len(a)+1, len(b), len(tails)
    assert len(pairs) == (p-2)*r + q
    return result


def direct_cores(f, literal):
    return {c for c in f if literal in c and len(c) > 1 and
            all(frozenset((-literal, -u)) in f for u in c - {literal})}


def stamped_cores(f, literal, signatures):
    stamped = set()
    signature = 0
    for c in f:
        if -literal in c and len(c) == 2:
            u = -next(iter(c - {-literal}))
            stamped.add(u)
            signature |= signatures[u]
    if not signature:
        return set()
    signature |= signatures[literal]
    result = set()
    for c in f:
        if literal not in c:
            continue
        sig = 0
        for u in c:
            sig |= signatures[u]
        if not sig & ~signature and c - {literal} <= stamped:
            result.add(c)
    return result


def audit_formulas(counts):
    rng = random.Random(376)
    pool = clauses(3)
    cases = [(3, frozenset(f)) for k in range(4) for f in combinations(pool, k)]
    pool5 = [c for c in clauses(5) if 1 < len(c) <= 4]
    cases += [(5, frozenset(rng.sample(pool5, rng.randrange(4, 15)))) for _ in range(1000)]
    # Add definitions deliberately, so larger r and nontrivial omitted pairs occur.
    for _ in range(1000):
        core = rng.choice([c for c in pool5 if 1 in c])
        f = set(rng.sample(pool5, 8)) | {core}
        f |= {frozenset((-1, -u)) for u in core - {1}}
        cases.append((5, frozenset(f)))
    signatures = {l: (1 << rng.randrange(8)) | (1 << rng.randrange(8))
                  for l in range(-5, 6) if l}
    for n, f in cases:
        actual = models(f, n)
        counts['formulas'] += 1
        for v in range(1, n+1):
            reduced, a, b = eliminate(f, v)
            reduced_models = models(reduced, n)
            projection = {assign(x, v, False) for x in actual}
            assert {assign(x, v, False) for x in reduced_models} == projection
            for x in reduced_models:
                # Either version of erp rule (161) must reconstruct a model.
                x1 = assign(x, v, not all(sat_clause(c - {v}, x) for c in a))
                x2 = assign(x, v, all(sat_clause(c - {-v}, x) for c in b))
                assert x1 in actual and x2 in actual
                counts['reconstructed_assignments'] += 2
            counts['variable_eliminations'] += 1
        for l in range(-n, n+1):
            if not l:
                continue
            cores = direct_cores(f, l)
            # Unit clauses are handled before 375, hence omitted here.
            detected = {c for c in stamped_cores(f, l, signatures) if len(c) > 1}
            assert detected == cores
            counts['stamp_detection_checks'] += 1
            for core in cores:
                reduced = substitution(f, l, core)
                full, _, _ = eliminate(f, l)
                new_models = models(reduced, n)
                assert new_models == models(full, n)
                for x in new_models:
                    restored = assign(x, -l, sat_clause(core - {l}, x))
                    assert restored in actual
                    counts['substitution_erp_assignments'] += 1
                counts['substitutions'] += 1
        for c in f:
            for l in c:
                if all(resolve(c, d, l) is None for d in f if -l in d):
                    for x in models(f - {c}, n):
                        new_truth = sat_clause({l}, x) or not sat_clause(c - {l}, x)
                        assert assign(x, l, new_truth) in actual
                        counts['blocked_erp_assignments'] += 1
                    counts['blocked_eliminations'] += 1
    print('formula checks complete', dict(counts), flush=True)


def encoded(l):
    return 2*abs(l) + (l < 0)


def merge_resolvent(c, d, literal):
    a, b = sorted(map(encoded, c), reverse=True), sorted(map(encoded, d), reverse=True)
    i = j = 0
    out = []
    while i < len(a) or j < len(b):
        u = a[i] if i < len(a) else 0
        v = b[j] if j < len(b) else 0
        if u == v:
            out.append(u); i += 1; j += 1
        elif u == (v ^ 1):
            if u != encoded(literal):
                return None
            i += 1; j += 1
        elif u > v:
            out.append(u); i += 1
        else:
            out.append(v); j += 1
    return frozenset(out)


def detailed_subsumption(c, d, change=None):
    a, b = sorted(map(encoded, c), reverse=True), sorted(map(encoded, d), reverse=True)
    if change is not None:
        old, new = map(encoded, change)
        a = [new if u == old else u for u in a]
    a.append(0); b.append(0)
    i = j = 0
    while b[j] >= a[i] > 0:
        while b[j] > a[i]:
            j += 1
        if b[j] == a[i]:
            i += 1; j += 1
    return a[i] <= b[j]


def audit_lists(counts):
    pool = clauses(5)
    for c in pool:
        for d in pool:
            assert detailed_subsumption(c, d) == (c <= d)
            counts['subsumption_pairs'] += 1
            for l in c:
                if -l in d:
                    r = resolve(c, d, l)
                    assert merge_resolvent(c, d, l) == (None if r is None else frozenset(map(encoded, r)))
                    counts['merged_resolvents'] += 1
                assert detailed_subsumption(c, d, (l, -l)) == ((c - {l}) | {-l} <= d)
                counts['self_subsumption_pairs'] += 1


def exploitation(clear_links):
    # All four variables initially occur in both polarities; no easy operation
    # preempts the initial C,E,N,D processing order.
    f = {'C': frozenset((1, 2, 3)), 'E': frozenset((1, 2, 4)),
         'N': frozenset((-1, -2, -4)), 'D': frozenset((1, -3))}
    order = ['C', 'E', 'N', 'D']
    sentinel = 'END'
    link = {name: (order[i+1] if i+1 < len(order) else sentinel)
            for i, name in enumerate(order)}
    top = order[0]
    trace = []

    def touched(name):
        nonlocal top
        if link[name] == 0:
            link[name] = top; top = name
            trace.append(['push', name])
        else:
            trace.append(['skip_push', name, link[name]])

    def easy():
        while f:
            literals = set().union(*f.values())
            choices = [next(iter(c)) for c in f.values() if len(c) == 1]
            choices += [l for l in sorted(literals) if -l not in literals]
            if not choices:
                return
            l = choices[0]
            trace.append(['condition', l])
            for name, c in list(f.items()):
                if l in c:
                    del f[name]
                elif -l in c:
                    f[name] = c - {-l}; touched(name)
                    assert f[name]

    easy()
    while top != sentinel:
        c = top; top = link[c]
        if clear_links:
            link[c] = 0
        trace.append(['pop', c])
        if c not in f:
            continue
        for d in list(f):
            if d != c and f[c] <= f[d]:
                del f[d]; trace.append(['subsume', c, d])
        easy()
        if c not in f:
            continue
        for d in list(f):
            if c not in f or d not in f or c == d:
                continue
            for l in tuple(f[c]):
                if -l in f[d] and f[c] - {l} <= f[d] - {-l}:
                    f[d] -= {-l}; touched(d)
                    trace.append(['strengthen', c, d, sorted(f[d])])
                    break
        easy()
    return {'clauses': {k: sorted(v) for k, v in f.items()}, 'trace': trace,
            'links': link}


def audit_examples(counts):
    original = [frozenset(c) for c in ((1, 2, -3), (-1, -2, 3), (2, 3, -4),
                (-2, -3, 4), (1, 3, 4), (-1, -3, -4), (-1, 2, 4))]
    f, positive, negative = eliminate(original, 1)
    # The answer lists the four NEW clauses; two untouched clauses remain.
    unchanged = set(original) - set(positive) - set(negative)
    assert f - unchanged == {frozenset(c) for c in ((2, -3, 4), (2, -3, -4), (2, 3, 4), (-2, 3, 4))}
    f, _, _ = eliminate(f, 2)
    assert f == {frozenset((3, 4)), frozenset((-3, 4))}
    for value in (0, 1):
        x = value << 2
        x = assign(x, 4, True)
        x = assign(x, 2, sat_clause((3, 4), x) and sat_clause((-3, 4), x))
        x = assign(x, -1, sat_clause((2, -3), x) and sat_clause((3, 4), x))
        assert x in models(original, 4)
        counts['366_reconstructions'] += 1
    lhs = [frozenset(c) for c in ((1, 2), (1, -2, -3), (-1, 2, 3))]
    rhs = [frozenset(c) for c in ((1, -3), (2, 3))]
    assert models(lhs, 3) == models(rhs, 3)
    counts['370_truth_tables'] += 1
    h = {frozenset(c) for c in ((-1,-5),(-1,-6),(-2,-5),(-2,-6),
             (-3,-7),(-3,-8),(-4,-7),(-4,-8),(1,2,3),(1,2,4),(1,3,4),
             (2,3,4),(5,6,7),(5,6,8),(5,7,8),(6,7,8))}
    assert len(models(h, 8)) == 2
    assert all(any(l in c for c in h) for l in range(-8, 9) if l)
    for c, d in product(h, repeat=2):
        if c == d:
            continue
        assert not c <= d
        assert not any(-l in d and c-{l} <= d-{-l} for l in c)
    for v in range(1, 9):
        reduced, a, b = eliminate(h, v)
        assert len(a)+len(b) == 5 and len(reduced) == len(h)+1
        assert not direct_cores(h, v) and not direct_cores(h, -v)
        counts['372_irreducible_variables'] += 1
    for n in range(2, 9):
        chain = [frozenset((-j, j+1)) for j in range(1, n)]
        cycle = chain + [frozenset((-n, 1))]
        for x in models(chain, n):
            for j in range(n-1, 0, -1):
                condition = bool(x & (1 << (n-1))) and not (x & ((1 << (j-1))-1))
                x = assign(x, j, bool(x & (1 << (j-1))) or condition)
            assert x in models(cycle, n)
            counts['381_reconstructions'] += 1
    # 379: every permitted additional clause survives the forward repair.
    for d in clauses(4):
        if -1 in d and -2 not in d and -3 not in d and 4 not in d:
            continue
        for x in models((frozenset((1,2,3,4)), d), 4):
            y = x if sat_clause((1,2,3), x) else assign(x, 1, True)
            assert sat_clause((1,2,3), y) and sat_clause(d, y)
            counts['379_forward_repairs'] += 1
    a = [frozenset(c) for c in ((1,2,-4),(1,4,5),(2,4,-5))]
    b = [frozenset(c) for c in ((1,2,-4),(1,-3,-4),(2,4,-5),(2,-3,-5))]
    c = frozenset((1,2,3))
    assert models(a, 5) == models(a+[c], 5)
    for x in models(b, 5):
        y = assign(x, 3, sat_clause((3,),x) or not sat_clause((1,2),x))
        assert y in models(b+[c], 5)
        counts['380_reconstructions'] += 1


def audit_triangles(counts):
    for n in range(1, 6):
        edges = list(combinations(range(n), 2))
        for mask in range(1 << len(edges)):
            graph = {edge for i, edge in enumerate(edges) if (mask >> i) & 1}
            triangle = any(all(tuple(sorted(edge)) in graph for edge in combinations(triple,2))
                           for triple in combinations(range(n),3))
            adjacency = {l:set() for v in range(1,3*n+1) for l in (v,-v)}
            for u,v in graph:
                u1,u2,u3 = (3*u+i for i in (1,2,3))
                v1,v2,v3 = (3*v+i for i in (1,2,3))
                for a,b in ((-u1,v2),(-u2,v3),(-u3,-v1),(u2,-v1),(u3,-v2),(-u1,-v3)):
                    adjacency[-a].add(b); adjacency[-b].add(a)
            failed = False
            for l in adjacency:
                seen = {l}; todo = [l]
                while todo:
                    for k in adjacency[todo.pop()]:
                        if k not in seen:
                            seen.add(k); todo.append(k)
                failed |= -l in seen
            assert failed == triangle
            counts['377_graphs'] += 1


def main():
    counts = Counter()
    audit_formulas(counts)
    audit_lists(counts)
    audit_examples(counts)
    audit_triangles(counts)
    printed, corrected = exploitation(False), exploitation(True)
    assert printed['clauses'] == {'C':[1,2], 'E':[1,2,4], 'N':[-4,-2,-1]}
    assert corrected['clauses'] == {}
    # Literal copy in 374(a): S(1) points to the first, p to the last cell.
    links = {}; p = 1
    for new in (100,101):
        previous = p; p = new; links[previous] = p
    assert links[1] == 100 and links[100] == 101 and p == 101
    result = {'status':'all assertions passed', 'counts':dict(counts),
              '376_printed':printed, '376_corrected':corrected,
              '374_copy_links':{'S(1)':100,'S(100)':101,'p':101,
                                'correct_traversal':[100,101]}}
    (Path(__file__).parent/'results/preprocessing.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__ == '__main__':
    main()
