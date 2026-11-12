"""Literal pointer algorithms from TAOCP 2.3.5, with separate test instrumentation.

Zero is null. Node addresses are positive integers. Algorithms mutate fields;
Python collections representing the simulated heap are not auxiliary stacks.
"""
from dataclasses import dataclass, replace


@dataclass
class Node:
    mark: int = 0
    atom: int = 0
    a: int = 0
    b: int = 0


def mark_a(mem, roots, variant=False):
    """Algorithm A with the published K -> K1 correction; optional A3'."""
    m = len(mem)
    for p in roots:
        if p:
            mem[p].mark = 1
    k, next_k, scans = 1, m + 1, 0
    while k <= m:
        scans += 1
        if not variant:
            next_k = k + 1
        node = mem[k]
        if node.mark and not node.atom:
            for q in (node.a, node.b):
                if q and not mem[q].mark:
                    mem[q].mark = 1
                    if not mem[q].atom:
                        next_k = min(next_k, q)
        if variant:
            k += 1
            if k > m:
                k, next_k = next_k, m + 1
        else:
            k = next_k
    return scans


def mark_b(mem, roots):
    stack = [p for p in roots if p]
    for p in stack:
        mem[p].mark = 1
    while stack:
        p = stack.pop()
        if not mem[p].atom:
            for q in (mem[p].a, mem[p].b):
                if q and not mem[q].mark:
                    mem[q].mark = 1
                    stack.append(q)


def mark_c(mem, roots, h):
    assert h >= 1
    m = len(mem)
    stack = [0] * h
    t = bottom = h - 1
    next_k = m + 1
    pushes = dropped = scans = 0

    def push(x):
        nonlocal t, bottom, next_k, pushes, dropped
        t = (t + 1) % h
        stack[t] = x
        pushes += 1
        if t == bottom:
            bottom = (bottom + 1) % h
            next_k = min(next_k, stack[bottom])
            dropped += 1

    for p in roots:
        if p:
            mem[p].mark = 1
            push(p)
    while True:
        if t != bottom:
            k = stack[t]
            t = (t - 1) % h
        else:
            while next_k <= m and (mem[next_k].atom or not mem[next_k].mark):
                next_k += 1
                scans += 1
            if next_k > m:
                return dict(pushes=pushes, dropped=dropped, scans=scans)
            k = next_k
            next_k += 1
            scans += 1
        if not mem[k].atom:
            for q in (mem[k].a, mem[k].b):
                if q and not mem[q].mark:
                    mem[q].mark = 1
                    push(q)


def mark_e(mem, root, trace=None):
    """E1--E6; entry root is nonnull, normally initially unmarked."""
    t, p, state = 0, root, 2
    while True:
        if trace is not None:
            trace.append((state, t, p, {k: replace(v) for k, v in mem.items()}))
        if state == 2:
            mem[p].mark = 1
            state = 6 if mem[p].atom else 4
        elif state == 4:
            q = mem[p].a
            if q and not mem[q].mark:
                mem[p].atom, mem[p].a = 1, t
                t, p, state = p, q, 2
            else:
                state = 5
        elif state == 5:
            q = mem[p].b
            if q and not mem[q].mark:
                mem[p].b = t
                t, p, state = p, q, 2
            else:
                state = 6
        else:
            if not t:
                return p
            q = t
            if mem[q].atom:
                mem[q].atom = 0
                t, mem[q].a, p, state = mem[q].a, p, q, 5
            else:
                t, mem[q].b, p = mem[q].b, p, q


def mark_s(mem, root, capacity):
    """Literal Schorr--Waite hybrid S1--S7, including zero capacity."""
    assert capacity >= 0
    mem[root].mark = 1
    if mem[root].atom:
        return
    stack, r, t, state = [], root, 0, 2
    while True:
        if state == 2:
            p = mem[r].b
            state = 3
            if p and not mem[p].mark:
                mem[p].mark = 1
                if not mem[p].atom:
                    if len(stack) < capacity:
                        stack.append(p)
                    else:
                        state = 5
        elif state == 3:
            p = mem[r].a
            state = 4
            if p and not mem[p].mark:
                mem[p].mark = 1
                if not mem[p].atom:
                    r, state = p, 2
        elif state == 4:
            if not stack:
                return
            r, state = stack.pop(), 2
        elif state == 5:
            q = mem[p].a
            state = 6
            if q and not mem[q].mark:
                mem[q].mark = 1
                if not mem[q].atom:
                    mem[p].atom, mem[p].a = 1, t
                    t, p, state = p, q, 5
        elif state == 6:
            q = mem[p].b
            state = 7
            if q and not mem[q].mark:
                mem[q].mark = 1
                if not mem[q].atom:
                    mem[p].b = t
                    t, p, state = p, q, 5
        else:
            if not t:
                state = 3
            else:
                q = t
                if mem[q].atom:
                    mem[q].atom = 0
                    t, mem[q].a, p, state = mem[q].a, p, q, 6
                else:
                    t, mem[q].b, p = mem[q].b, p, q


def mark_floyd(mem, root):
    """Exercise 7: no ATOM bit is read or written; acyclic input."""
    t, p, state = 0, root, 4
    while True:
        if state == 4:
            q = mem[p].a
            if q and not mem[q].mark:
                mem[p].a = t
                t, p = p, q
            else:
                state = 5
        elif state == 5:
            mem[p].mark = 1
            q = mem[p].b
            if q and not mem[q].mark:
                mem[p].b = t
                t, p, state = p, q, 4
            else:
                state = 6
        else:
            if not t:
                return p
            q = t
            if not mem[q].mark:
                t, mem[q].a, p, state = mem[q].a, p, q, 5
            else:
                t, mem[q].b, p = mem[q].b, p, q


@dataclass
class Cell:
    mark: int
    value: int


def mark_f(mem, root):
    """Variable-size nodes; header value=SIZE, other value=LINK."""
    t, p = 0, root
    while True:
        mem[p].mark = 1
        p += mem[p].value
        while True:
            if not mem[p].mark:
                q = mem[p].value
                if q and not mem[q].mark:
                    mem[p].value, t, p = t, p, q
                    break
                p -= 1
            else:
                if not t:
                    return p
                q = t
                t, mem[q].value, p = mem[q].value, p, q - 1


def mark_g(mem, root):
    """Exercise 8 solution 2; SIZE must be wide enough for an address."""
    t = 0
    mem[root].mark = 1
    p = root + mem[root].value
    while True:
        if not mem[p].mark:
            q = mem[p].value
            p -= 1
            if q and not mem[q].mark:
                mem[q].mark = 1
                size = mem[q].value
                mem[q].value = t
                t = q + size
        else:
            if not t:
                return
            p = q = t
            while not mem[q].mark:
                q -= 1
            t, mem[q].value = mem[q].value, p - q


def compact_h(mem, m):
    """Literal H1--H5. Sentinels 0 and M+1 must be available."""
    left, k = 0, m + 1
    mem[0], mem[m + 1] = Node(mark=1), Node()
    while True:
        left += 1
        while mem[left].mark:
            left += 1
        k -= 1
        while not mem[k].mark:
            k -= 1
        if left > k:
            break
        mem[left] = replace(mem[k])
        mem[k].a, mem[k].mark = left, 0
    for left in range(1, k + 1):
        mem[left].mark = 0
        if not mem[left].atom:
            if mem[left].a > k:
                mem[left].a = mem[mem[left].a].a
            if mem[left].b > k:
                mem[left].b = mem[mem[left].b].a
    return k


@dataclass
class ListCell:
    s: int = 0
    t: int = 0
    ref: int = 0
    right: int = 0


def mark_d(mem, roots):
    top = 0
    for p in roots:
        if p and not mem[p].s:
            mem[p].s, mem[p].ref, top = 1, top, p
    while top:
        p = top
        top = mem[p].ref
        p = mem[p].right
        while p and mem[p].t != 0:
            mem[p].s = 1
            if mem[p].t > 1:
                if mem[p].ref:
                    mem[mem[p].ref].s = 1
            else:
                q = mem[p].ref
                if q and not mem[q].s:
                    mem[q].s, mem[q].ref, top = 1, top, q
            p = mem[p].right


def copy_z(mem, root, allocate):
    """Z1--Z7, straight lists ending in null, every sublist has a head."""
    f = root
    r = allocate()
    mem[r] = replace(mem[f])
    mem[f].ref = r
    result = r
    while True:
        p, q = f, mem[f].ref
        while True:
            p = mem[p].right
            if not p:
                break
            q1 = allocate()
            mem[q].right = q1
            q = q1
            mem[q] = replace(mem[p])
            if mem[p].t == 1:
                p1 = mem[p].ref
                assert p1, "Z uses an explicit header even for an empty sublist"
                if not mem[p1].ref:
                    mem[r].ref = p1
                    r = allocate()
                    mem[p1].ref = r
                    mem[r] = replace(mem[p1])
                    mem[q].ref = r
                if mem[p1].ref:
                    mem[q].ref = mem[p1].ref
        mem[q].right = 0
        if mem[f].ref != r:
            f = mem[mem[f].ref].ref
        else:
            mem[r].ref = 0
            break
    p = root
    while mem[p].ref:
        q = mem[p].ref
        mem[p].ref = 0
        p = q
    return result


def equivalent(graph, x, y):
    """List expressions: each element is ('atom',value) or ('list',label,id)."""
    pending, seen = [(x, y)], set()
    while pending:
        p, q = pending.pop()
        if (p, q) in seen:
            continue
        seen.add((p, q))
        a, b = graph[p], graph[q]
        if len(a) != len(b):
            return False
        for u, v in zip(a, b):
            if u[:2] != v[:2]:
                return False
            if u[0] == 'list':
                pending.append((u[2], v[2]))
    return True
