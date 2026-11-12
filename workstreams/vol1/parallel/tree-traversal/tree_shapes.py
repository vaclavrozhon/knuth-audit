"""Independent recursive tree oracle; nodes receive preorder identities 1..n."""
from functools import lru_cache

@lru_cache(None)
def shapes(n):
    if n == 0:
        return (None,)
    return tuple((l, r) for k in range(n) for l in shapes(k) for r in shapes(n-1-k))

def build(shape, offset=0):
    nodes = {}
    def rec(s):
        if s is None:
            return None
        p = offset + len(nodes) + 1
        nodes[p] = {'L': None, 'R': None, 'info': p}
        nodes[p]['L'], nodes[p]['R'] = rec(s[0]), rec(s[1])
        return p
    return rec(shape), nodes

def orders(root, nodes):
    if root is None:
        return [], [], [], [], []
    lp, li, lo, ld, lt = orders(nodes[root]['L'], nodes)
    rp, ri, ro, rd, rt = orders(nodes[root]['R'], nodes)
    return ([root]+lp+rp, li+[root]+ri, lo+ro+[root],
            [(root, 1)]+ld+[(root, 2)]+rd,
            [root]+lt+[root]+rt+[root])

def stack_height(shape):
    return 0 if shape is None else max(1+stack_height(shape[0]), stack_height(shape[1]))

def size(shape):
    return 0 if shape is None else 1+size(shape[0])+size(shape[1])

def recursive_key(root, nodes):
    return () if root is None else (nodes[root]['info'], recursive_key(nodes[root]['L'],nodes), recursive_key(nodes[root]['R'],nodes))
