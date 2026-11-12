"""Pointer-level audit of TAOCP 1, Algorithm 2.3.3A and exercise 15.

Node numbers are addresses; zero is the null pointer. Variables have positive
integer names, in their alphabetical order. Arithmetic on coefficients is exact.
This is the printed algorithm, not a MIX program or a floating-point model.
"""

from collections import Counter
from dataclasses import dataclass, asdict


@dataclass
class Node:
    up: int = 0
    exp: int = 0
    right: int = 0
    left: int = 0
    cv: object = 0
    down: int = 0


class Pool:
    def __init__(self):
        self.nodes = {}
        self.free = []
        self.freed = set()
        self.next_address = 1

    def __getitem__(self, address):
        assert address and address not in self.freed, ("invalid address", address)
        return self.nodes[address]

    def allocate(self):
        if self.free:
            p = self.free.pop()
            self.freed.remove(p)
        else:
            p = self.next_address
            self.next_address += 1
        self.nodes[p] = Node(left=p, right=p)
        return p

    def release(self, p):
        self[p]
        self.freed.add(p)
        self.free.append(p)

    def row(self, p):
        """Children of p in increasing exponent order, starting with exponent 0."""
        first = self[p].down
        if not first:
            return []
        out = []
        q = first
        while True:
            assert q not in out, ("row misses first node", p)
            out.append(q)
            q = self[q].right
            if q == first:
                return out

    def attach(self, p, entries):
        """Install a sorted list of (exponent, freshly owned child) pairs."""
        assert entries and entries[0][0] == 0
        ids = [q for _, q in entries]
        self[p].down = ids[0]
        for i, (e, q) in enumerate(entries):
            self[q].up = p
            self[q].exp = e
            self[q].left = ids[(i - 1) % len(ids)]
            self[q].right = ids[(i + 1) % len(ids)]

    def build(self, terms):
        """Independent construction from monomial tuples -> exact coefficients."""
        terms = {m: c for m, c in terms.items() if c}
        p = self.allocate()
        used = [i for m in terms for i, e in enumerate(m) if e]
        if not used:
            self[p].cv = sum(terms.values())
            return p
        v = max(used)
        self[p].cv = v + 1
        groups = {0: {}}
        for m, c in terms.items():
            e = m[v]
            child = m[:v] + (0,) + m[v + 1:]
            group = groups.setdefault(e, {})
            group[child] = group.get(child, 0) + c
        self.attach(p, [(e, self.build(g)) for e, g in sorted(groups.items())])
        return p

    def validate(self, p, nvars, canonical=True):
        """Check all links and obtain the independent flat polynomial and node set."""
        root = self[p]
        assert root.up == 0 and root.exp == 0 and root.left == root.right == p
        seen = set()

        def visit(q, bound):
            assert q not in seen, ("alias or cycle", q)
            seen.add(q)
            node = self[q]
            if node.down == 0:
                return {(0,) * nvars: node.cv} if node.cv else {}
            v = node.cv
            assert isinstance(v, int) and 1 <= v < bound
            row = self.row(q)
            assert not canonical or len(row) >= 2
            exps = [self[c].exp for c in row]
            assert exps[0] == 0 and all(a < b for a, b in zip(exps, exps[1:]))
            result = {}
            for i, c in enumerate(row):
                child = self[c]
                assert child.up == q
                assert child.left == row[i - 1] and child.right == row[(i + 1) % len(row)]
                poly = visit(c, v)
                assert not canonical or child.exp == 0 or poly
                for m, coefficient in poly.items():
                    assert m[v - 1] == 0
                    shifted = m[:v - 1] + (child.exp,) + m[v:]
                    assert shifted not in result
                    result[shifted] = coefficient
            return result

        return visit(p, nvars + 1), seen

    def snapshot(self, ids):
        return {i: asdict(self[i]) for i in ids}

    def partition(self, *node_sets):
        union = set()
        for s in node_sets:
            assert not union.intersection(s), "shared polynomial nodes"
            union.update(s)
        assert not union.intersection(self.freed)
        assert union | self.freed == set(self.nodes), "unreachable allocated node"
        assert len(self.free) == len(self.freed)

    def erase(self, p):
        for q in self.row(p):
            self.erase(q)
        self.release(p)


def context(pool, p):
    """Nonzero variable powers on the ancestor chain of a coefficient node."""
    out = {}
    while pool[p].up:
        parent = pool[p].up
        if pool[p].exp:
            assert pool[parent].cv not in out
            out[pool[parent].cv] = pool[p].exp
        p = parent
    return out


def add_printed(pool, p, q, check_structure=None):
    """Literal A1-A11; preserve both root addresses and all of the first input.

    check_structure, when supplied, is the number of variables and requests
    structural checks between steps, permitting temporary unnormalized rows.
    The generous finite limit is only a test-harness failure detector.
    """
    p0, q0 = p, q
    assert p != q
    step = 1
    counts = Counter()
    while True:
        counts[step] += 1
        assert sum(counts.values()) < 1000000, "audit step limit"
        if check_structure is not None:
            pool.validate(q0, check_structure, canonical=False)
        if step == 1:
            if pool[p].down == 0:
                while pool[q].down:
                    q = pool[q].down
                step = 3
            elif pool[q].down == 0 or pool[q].cv < pool[p].cv:
                step = 2
            elif pool[q].cv == pool[p].cv:
                p, q = pool[p].down, pool[q].down
            else:
                q = pool[q].down
        elif step == 2:
            r = pool.allocate()
            s = pool[q].down
            if s:
                while True:
                    pool[s].up = r
                    s = pool[s].right
                    if pool[s].exp == 0:
                        break
            pool[r].up = q
            pool[r].down = pool[q].down
            pool[r].left = pool[r].right = r
            pool[r].cv = pool[q].cv
            pool[r].exp = 0
            pool[q].cv = pool[p].cv
            pool[q].down = r
            step = 1
        elif step == 3:
            assert pool[p].down == pool[q].down == 0
            assert context(pool, p) == context(pool, q)
            pool[q].cv += pool[p].cv
            if pool[q].cv == 0 and pool[q].exp != 0:
                step = 8
            elif pool[q].exp == 0:
                step = 7
            else:
                step = 4
        elif step == 4:
            p = pool[p].left
            if pool[p].exp == 0:
                step = 6
            else:
                while True:
                    q = pool[q].left
                    if pool[q].exp <= pool[p].exp:
                        break
                step = 1 if pool[q].exp == pool[p].exp else 5
        elif step == 5:
            r = pool.allocate()
            pool[r].up = pool[q].up
            pool[r].down = 0
            pool[r].cv = 0
            pool[r].left = q
            pool[r].right = pool[q].right
            pool[pool[r].right].left = r
            pool[q].right = r
            pool[r].exp = pool[p].exp
            q = r
            step = 1
        elif step == 6:
            p = pool[p].up
            step = 7
        elif step == 7:
            if pool[p].up == 0:
                step = 11
            else:
                while pool[pool[q].up].cv != pool[pool[p].up].cv:
                    q = pool[q].up
                step = 4
        elif step == 8:
            assert pool[p].exp == pool[q].exp != 0
            assert pool[pool[p].up].cv == pool[pool[q].up].cv
            assert context(pool, p) == context(pool, q)
            assert pool[q].down == 0 and pool[q].cv == 0
            r = q
            q, s = pool[r].right, pool[r].left
            pool[q].left = s
            pool[s].right = q
            pool.release(r)
            step = 9 if pool[pool[p].left].exp == 0 and q == s else 4
        elif step == 9:
            r = q
            q = pool[q].up
            pool[q].down = pool[r].down
            pool[q].cv = pool[r].cv
            pool.release(r)
            s = pool[q].down
            if s:
                while True:
                    pool[s].up = q
                    s = pool[s].right
                    if pool[s].exp == 0:
                        break
            step = 10
        elif step == 10:
            if pool[q].down == 0 and pool[q].cv == 0 and pool[q].exp != 0:
                p = pool[p].up
                step = 8
            else:
                step = 6
        else:
            assert step == 11
            while pool[q].up:
                q = pool[q].up
            assert (p, q) == (p0, q0)
            return counts


def multiply(pool, p, q):
    """Exercise 15: exact recursive convolution on the linked representation.

    Inputs are read-only coefficient subtrees. Output is a fresh root. The
    dictionary is temporary indexing of result coefficients by exponent;
    polynomial data remain in six-field nodes throughout the computation.
    """
    if pool[p].down == pool[q].down == 0:
        r = pool.allocate()
        pool[r].cv = pool[p].cv * pool[q].cv
        return r
    pv = pool[p].cv if pool[p].down else 0
    qv = pool[q].cv if pool[q].down else 0
    v = max(pv, qv)
    a = [(pool[c].exp, c) for c in pool.row(p)] if pv == v else [(0, p)]
    b = [(pool[c].exp, c) for c in pool.row(q)] if qv == v else [(0, q)]
    coefficients = {0: pool.allocate()}
    for e, x in a:
        for f, y in b:
            t = multiply(pool, x, y)
            k = e + f
            if k in coefficients:
                add_printed(pool, t, coefficients[k])
                pool.erase(t)
            else:
                coefficients[k] = t
    for e, c in list(coefficients.items()):
        if e and pool[c].down == 0 and pool[c].cv == 0:
            pool.erase(c)
            del coefficients[e]
    if len(coefficients) == 1:
        return coefficients[0]
    r = pool.allocate()
    pool[r].cv = v
    pool.attach(r, sorted(coefficients.items()))
    return r
