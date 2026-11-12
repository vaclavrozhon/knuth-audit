#!/usr/bin/env python3
"""Literal book Algorithm C and independent direct commafree predicates.

All word values inside MEM use hexadecimal digits, while state and inverse
addresses use radix m, exactly as in the text. No author source is imported.
"""
from collections import Counter, defaultdict
from itertools import product, combinations, permutations
from pathlib import Path
import json
import random

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/commafree'


def word(x, n=4):
    return f'{x:0{n}x}'


def rotations(w):
    return [w[i:]+w[:i] for i in range(len(w))]


def commafree(code):
    code = set(code)
    if not code:
        return True
    n = len(next(iter(code)))
    return all((a+b)[i:i+n] not in code for a in code for b in code
               for i in range(1, n))


def orbit(code, m):
    return {tuple(sorted(''.join(str(p[int(a)]) for a in w[::direction])
                         for w in code))
            for p in permutations(range(m)) for direction in [1, -1]}


class BadCandidate(Exception):
    def __init__(self, state):
        self.state = state


class AlgorithmC:
    def __init__(self, m, goal, repair44=True):
        self.m, self.N = m, m**4
        self.L = (self.N-m*m)//4
        assert 2 <= m <= 7 and self.L-m*(m-1) <= goal <= self.L
        self.goal, self.repair44 = goal, repair44
        self.mem = [0]*((47*self.N+1)//2)
        self.stamp = [0]*len(self.mem)
        self.sigma = 0
        self.undo = []
        self.off = [i*self.N for i in [2, 5, 8, 11, 14, 17, 20]]
        self.poison = 22*self.N
        self.pp = self.poison-1
        self.mem[self.pp] = self.poison
        self.alf = {int(''.join(map(str, w)), 16): sum(a*m**(3-i)
                    for i, a in enumerate(w)) for w in product(range(m), repeat=4)}
        self.rep = sorted(w for w in map(word, self.alf)
                          if len(set(rotations(w))) == 4 and w == min(rotations(w)))
        assert len(self.rep) == self.L
        self.cl = {int(w, 16): c for c, v in enumerate(self.rep) for w in rotations(v)}
        for x in self.alf:
            for d, off in zip(self.deltas(x)[:6], self.off[:6]):
                self.mem[off+d+self.N] = off+d
        for c, v in enumerate(self.rep):
            for i, w in enumerate(rotations(v)):
                x = int(w, 16)
                if x in [0x0100, 0x1000]:
                    continue
                alpha = self.alf[x]
                self.mem[alpha] = 1
                for d, off in zip(self.deltas(x)[:6], self.off[:6]):
                    head = off+d
                    tail = self.mem[head+self.N]
                    self.mem[tail] = x
                    self.mem[off-self.N+alpha] = tail
                    self.mem[head+self.N] = tail+1
                pos = self.off[6]+4*c+i
                self.mem[pos] = x
                self.mem[self.off[6]-self.N+alpha] = pos
            self.mem[self.off[6]+4*c+self.N] = self.off[6]+4*c+(4 if c else 2)
        self.free = list(range(self.L))
        self.ifree = self.free.copy()
        self.f = self.L
        self.frames = [None]*(self.L+1)
        self.profile = [0]*(self.L+1)
        self.snapshots = {}

    def deltas(self, x):
        a, b, c, d = map(int, word(x))
        m = self.m
        return [a*m**3, (a*m+b)*m*m, ((a*m+b)*m+c)*m,
                d*m**3, (c*m+d)*m*m, ((b*m+c)*m+d)*m,
                4*self.cl[x] if hasattr(self, 'cl') and x in self.cl else None]

    def store(self, a, v):
        assert 0 <= a < len(self.mem)
        if self.stamp[a] != self.sigma:
            self.stamp[a] = self.sigma
            self.undo.append((a, self.mem[a]))
        self.mem[a] = v

    def unstore(self, u):
        while len(self.undo) > u:
            a, v = self.undo.pop()
            self.mem[a] = v

    def redden(self, x):
        alpha = self.alf[x]
        assert self.mem[alpha] == 1, ('redden nonblue', word(x))
        self.store(alpha, 0)
        for d, off in zip(self.deltas(x), self.off):
            p = d+off
            q = self.mem[p+self.N]-1
            if q >= p:
                self.store(p+self.N, q)
                t = self.mem[alpha+off-self.N]
                if t != q:
                    y = self.mem[q]
                    self.store(t, y)
                    self.store(self.alf[y]+off-self.N, t)

    def green(self, x):
        alpha = self.alf[x]
        assert self.mem[alpha] == 1
        self.store(alpha, 2)
        for d, off in zip(self.deltas(x), self.off):
            p = d+off
            q = self.mem[p+self.N]
            if q != p-1:
                self.store(p+self.N, p-1)
        for r in range(p, q):
            if self.mem[r] != x:
                self.redden(self.mem[r])
        p = self.mem[self.pp]
        d = self.deltas(x)
        pairs = [(d[0]+self.off[3], d[5]+self.off[2]),
                 (d[1]+self.off[4], d[4]+self.off[1]),
                 (d[2]+self.off[5], d[3]+self.off[0])]
        for y, z in pairs:
            self.store(p, y)
            self.store(p+1, z)
            p += 2
        tail, p = p, self.poison
        while p < tail:
            y, z = self.mem[p:p+2]
            yy, zz = self.mem[y+self.N], self.mem[z+self.N]
            if yy == y or zz == z:
                pass
            elif yy < y and zz < z:
                return False
            elif yy > y and zz > z:
                p += 2
                continue
            elif yy < y:
                self.store(z+self.N, z)
                for r in range(z, zz):
                    self.redden(self.mem[r])
            else:
                self.store(y+self.N, y)
                for r in range(y, yy):
                    self.redden(self.mem[r])
            tail -= 2
            if p != tail:
                self.store(p, self.mem[tail])
                self.store(p+1, self.mem[tail+1])
        self.store(self.pp, tail)
        return True

    def choose(self, previous, level):
        r, c = 5, None
        for t in self.free[:self.f]:
            head = self.off[6]+4*t
            j = self.mem[head+self.N]-head
            if j < r:
                r, c = j, t
                if r == 0:
                    break
        x = -1 if r == 0 else self.mem[self.off[6]+4*(c if self.repair44 else self.cl[previous])]
        if r > 1:
            q, tail, p = 0, self.mem[self.pp], self.poison
            while p < tail:
                y, z = self.mem[p:p+2]
                yy, zz = self.mem[y+self.N], self.mem[z+self.N]
                if y == yy or z == zz:
                    tail -= 2
                    if p != tail:
                        self.store(p, self.mem[tail])
                        self.store(p+1, self.mem[tail+1])
                else:
                    p += 2
                    if yy-y >= zz-z and yy-y > q:
                        q, x = yy-y, self.mem[z]
                    if yy-y < zz-z and zz-z > q:
                        q, x = zz-z, self.mem[y]
            self.store(self.pp, tail)
            c = self.cl[x]
        if x >= 0 and (self.mem[self.alf[x]] != 1 or c not in self.free[:self.f]):
            raise BadCandidate(dict(level=level, previous=word(previous), r=r,
                chosen_class=self.rep[c], returned=word(x), state=self.mem[self.alf[x]],
                expected_first=word(self.mem[self.off[6]+4*c]),
                path=[word(v[0]) if v[0] >= 0 else None for v in self.frames[1:level]]))
        return x, c

    def invariants(self):
        assert sorted(self.free) == list(range(self.L))
        assert all(self.free[self.ifree[c]] == c for c in range(self.L))
        for x, alpha in self.alf.items():
            if x not in self.cl:
                assert self.mem[alpha] == 0
                continue
            for d, off in zip(self.deltas(x), self.off):
                head = d+off
                tail = self.mem[head+self.N]
                if tail < head:
                    assert any(self.mem[a] == 2 and dd == d for y, a in self.alf.items()
                               if y in self.cl for dd in [self.deltas(y)[self.off.index(off)]])
                elif self.mem[alpha] == 1:
                    loc = self.mem[alpha+off-self.N]
                    assert head <= loc < tail and self.mem[loc] == x
                elif self.mem[alpha] == 2:
                    raise AssertionError('green list not closed')

    def run(self, check=False):
        level, x, c, slack, step = 1, 1, 0, self.L-self.goal, 3
        self.profile[0] = 1
        solutions = []
        while True:
            if step == 2:
                if check:
                    self.invariants()
                if level > self.L:
                    code = tuple(sorted(word(v[0]) for v in self.frames[1:] if v[0] >= 0))
                    assert commafree(code) and len(code) >= self.goal
                    solutions.append(code)
                    step = 6
                else:
                    x, c = self.choose(x, level)
                    step = 3
            elif step == 3:
                u = len(self.undo)
                self.sigma += 1
                if x < 0:
                    if slack == 0 or level == 1:
                        step = 6
                        continue
                    slack -= 1
                elif not self.green(x):
                    step = 5
                    continue
                if level == 1:
                    self.snapshots[word(x)] = self.mem.copy()
                self.frames[level] = (x, c, slack, u)
                p = self.ifree[c]
                self.f -= 1
                if p != self.f:
                    y = self.free[self.f]
                    self.free[p], self.ifree[y] = y, p
                    self.free[self.f], self.ifree[c] = c, self.f
                level += 1
                self.profile[level-1] += 1
                step = 2
            elif step == 5:
                self.unstore(u)
                self.sigma += 1
                self.redden(x)
                step = 2
            else:
                level -= 1
                if level == 0:
                    break
                x, c, old_slack, u = self.frames[level]
                self.f += 1
                if x >= 0:
                    slack = old_slack
                    step = 5
        assert len(set(solutions)) == len(solutions)
        return sorted(solutions)


def parse_original(path):
    return sorted(tuple(sorted(w for w in line.split(':', 1)[1].split()
                               if not w.startswith('('))) for line in path.read_text().splitlines())


def main():
    OUT.mkdir(exist_ok=True)
    results = {}
    try:
        AlgorithmC(2, 3, repair44=False).run()
        raise AssertionError('printed selection unexpectedly passed')
    except BadCandidate as e:
        results['answer44_counterexample'] = e.state
    for goal in [3, 2, 1]:
        c = AlgorithmC(2, goal)
        actual = c.run(check=True)
        universe = [word(x) for x in range(0x1112) if x in c.alf]
        expected = sorted(code for k in range(goal, 4) for code in combinations(universe, k)
                          if ('0001' in code or '0010' in code) and commafree(code))
        assert actual == expected
        assert actual == parse_original(OUT/f'original-m2-g{goal}.out')
        results[f'm2_g{goal}'] = {'by_size':dict(Counter(map(len, actual))),
                                  'profile':c.profile, 'codes':actual}
        if goal == 3:
            initial = AlgorithmC(2, 3).mem
            after0010 = c.snapshots['0010']
            results['table1'] = initial
            results['table2'] = after0010
    (OUT/'literal-verified.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps({k:v for k,v in results.items() if not k.startswith('table') and not k.startswith('m2')}))
    print('Literal repaired Algorithm C agrees with complete subset enumeration and original C for all binary goals.')


if __name__ == '__main__':
    main()
