"""Independent word-variable CSP, with no exact-cover or dancing-links code.

Domains are sets of dictionary ranks represented by integers. Each physical
crossing imposes equality of two letters. All words must be different.
Arc consistency and singleton propagation are sound pruning only; exhaustive
branching supplies completeness. A deadline raises, never returns UNSAT.
"""
from functools import lru_cache
import time


class SearchIncomplete(Exception):
    pass


class WordCSP:
    def __init__(self, words, kind, period=None, symmetry=True):
        self.words = words
        self.n = len(words[0])
        self.p = self.n if kind == 'square' else period
        self.kind = kind
        self.full = (1 << len(words)) - 1
        self.neighbors = [[] for _ in range(2 * self.p)]
        self.ordered = ([self.p] if kind == 'square' else list(range(1, 2 * self.p))) if symmetry else []
        alphabet = sorted(set(''.join(words)))
        self.masks = []
        for j in range(self.n):
            masks = {c: 0 for c in alphabet}
            for rank, word in enumerate(words):
                masks[word[j]] |= 1 << rank
            self.masks.append(tuple(masks[c] for c in alphabet))
        for i in range(self.p):
            for j in range(self.n):
                if kind == 'square':
                    d, k = j, i
                elif kind == 'left':
                    d, k = (i - j) % self.p, j
                elif kind == 'right':
                    d, k = (i - self.n + 1 + j) % self.p, self.n - 1 - j
                else:
                    raise ValueError(kind)
                self.neighbors[i].append((self.p + d, j, k))
                self.neighbors[self.p + d].append((i, k, j))

    def solve(self, first=False, timeout=None):
        self.nodes = self.failures = 0
        self.solutions = []
        start = time.monotonic()
        deadline = start + timeout if timeout else float('inf')

        @lru_cache(maxsize=100000)
        def support(domain, position, other_position):
            result = 0
            for a, b in zip(self.masks[position], self.masks[other_position]):
                if domain & a:
                    result |= b
            return result

        def propagate(domains):
            queue = list(range(len(domains)))
            queued = set(queue)

            def narrow(v, new):
                if new == 0:
                    return False
                if new != domains[v]:
                    domains[v] = new
                    if v not in queued:
                        queue.append(v)
                        queued.add(v)
                return True

            while queue:
                if time.monotonic() >= deadline:
                    raise SearchIncomplete('deadline reached')
                v = queue.pop()
                queued.remove(v)
                domain = domains[v]
                if domain & (domain - 1) == 0:
                    for u in range(len(domains)):
                        if u != v and not narrow(u, domains[u] & ~domain):
                            return False
                for u, j, k in self.neighbors[v]:
                    if not narrow(u, domains[u] & support(domain, j, k)):
                        return False
                for u in self.ordered:
                    minimum = (domains[0] & -domains[0]).bit_length() - 1
                    if not narrow(u, domains[u] & ~((1 << (minimum + 1)) - 1)):
                        return False
                    maximum = domains[u].bit_length() - 1
                    if not narrow(0, domains[0] & ((1 << maximum) - 1)):
                        return False
            return True

        def visit(domains):
            self.nodes += 1
            if not propagate(domains):
                self.failures += 1
                return False
            choices = [(d.bit_count(), i) for i, d in enumerate(domains) if d & (d - 1)]
            if not choices:
                ranks = [d.bit_length() - 1 for d in domains]
                assert len(set(ranks)) == len(ranks)
                self.solutions.append(tuple(self.words[r] for r in ranks[:self.p]))
                return first
            _, v = min(choices)
            remaining = domains[v]
            while remaining:
                bit = remaining & -remaining
                remaining -= bit
                child = domains.copy()
                child[v] = bit
                if visit(child):
                    return True
            return False

        try:
            visit([self.full] * (2 * self.p))
        finally:
            self.seconds = time.monotonic() - start
            self.cache = support.cache_info()._asdict()
            support.cache_clear()
        return self.solutions
