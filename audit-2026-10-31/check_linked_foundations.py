#!/usr/bin/env python3
"""DLX1–5: linked-list invariants, equivalence classes, and incidence duality."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def initial(n):
    return [(k-1) % (n+1) for k in range(n+1)], [(k+1) % (n+1) for k in range(n+1)]


def delete(left, right, k):
    right[left[k]] = right[k]
    left[right[k]] = left[k]


def undelete(left, right, k):
    right[left[k]] = k
    left[right[k]] = k


def bst_bounds(insertion):
    """Independent ordinary BST insertion; record bounds from actual ancestors."""
    n = len(insertion)
    bounds = [(0,0)]*(n+1)
    children = {}
    for key in insertion:
        if not children:
            root = key
        else:
            node = root
            ancestors = []
            while True:
                ancestors.append(node)
                direction = int(key > node)
                child = children[node][direction]
                if child is None:
                    children[node][direction] = key
                    break
                node = child
            bounds[key] = (max((v for v in ancestors if v<key), default=0),
                           min((v for v in ancestors if v>key), default=0))
        children[key] = [None,None]
    return tuple(x for x,y in bounds), tuple(y for x,y in bounds)


def linear_extensions(signature):
    left,right = signature
    n = len(left)-1
    predecessors = [0]*n
    for k in range(1,n+1):
        for after in (left[k],right[k]):
            if after:
                predecessors[after-1] |= 1 << (k-1)
    @lru_cache(None)
    def count(mask):
        if mask == (1<<n)-1:
            return 1
        return sum(count(mask | (1<<k)) for k in range(n)
                   if not mask>>k&1 and predecessors[k]&mask == predecessors[k])
    return count(0)


def list_checks():
    by_n=[]
    for n in range(1,9):
        classes=Counter()
        for order in permutations(range(1,n+1)):
            left,right=initial(n)
            for k in order:
                delete(left,right,k)
            signature=tuple(left),tuple(right)
            assert signature == bst_bounds(order[::-1])
            classes[signature]+=1
            for restoration in (order,order[::-1]):
                l,r=left.copy(),right.copy()
                for k in restoration:
                    if restoration == order:
                        assert l[k]==k-1 and r[k]==(k+1)%(n+1)
                    undelete(l,r,k)
                assert (l,r)==initial(n)
        assert len(classes)==comb(2*n,n)//(n+1)
        assert sum(count==1 for count in classes.values())==2**(n-1)
        for signature,count in classes.items():
            assert linear_extensions(signature)==count
        by_n.append(dict(n=n,permutations=factorial(n),classes=len(classes),
                         singleton_classes=sum(count==1 for count in classes.values())))
    partial=0
    for n in range(8):
        for k in range(n+1):
            for order in permutations(range(1,n+1),k):
                l,r=initial(n)
                for v in order:delete(l,r,v)
                for v in order:
                    assert l[v]==v-1 and r[v]==(v+1)%(n+1)
                    undelete(l,r,v)
                assert (l,r)==initial(n)
                partial+=1
    l,r=initial(3)
    for k in (1,2,3):delete(l,r,k)
    for k in (1,3,2):undelete(l,r,k)
    assert (l,r)!=initial(3)
    wrong_order=dict(left=l,right=r)
    l,r=initial(4)
    diagrams=[dict(deleted=[],left=l.copy(),right=r.copy())]
    for k in (3,2,4,1):
        delete(l,r,k)
        diagrams.append(dict(deleted=diagrams[-1]['deleted']+[k],left=l.copy(),right=r.copy()))
    names='CAPRICORN AQUARIUS PISCES ARIES TAURUS GEMINI CANCER LEO VIRGO LIBRA SCORPIO'.split()
    rank={name:i+1 for i,name in enumerate(sorted(names))}
    l,r=bst_bounds(tuple(rank[name] for name in names))
    assert r[rank['LEO']]==rank['PISCES'] and l[rank['AQUARIUS']]==0
    return dict(full_permutations=by_n,partial_deletion_sequences=partial,
                arbitrary_restoration_counterexample=wrong_order,diagrams=diagrams,
                zodiac_example='RLINK(LEO)=PISCES; LLINK(AQUARIUS)=0')


def rref(matrix, rhs):
    a=[[Fraction(v) for v in row]+[Fraction(b)] for row,b in zip(matrix,rhs)]
    rank=0
    for col in range(len(matrix[0])):
        pivot=next((i for i in range(rank,len(a)) if a[i][col]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        divisor=a[rank][col];a[rank]=[x/divisor for x in a[rank]]
        for i in range(len(a)):
            if i!=rank:
                scale=a[i][col];a[i]=[x-scale*y for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank,a


def incidence_checks():
    rows=[(3,5),(1,4,7),(2,3,6),(1,4,6),(2,7),(4,5,7)]
    equations=[[int(c in row) for row in rows] for c in range(1,8)]
    rank,a=rref(equations,[1]*7)
    assert rank==6 and [row[-1] for row in a[:6]]==[1,0,0,1,1,0]
    assert a[-1]==[0]*7
    rank,triangle=rref([[1,1,0],[0,1,1],[1,0,1]],[1]*3)
    assert rank==3 and [r[-1] for r in triangle]==[Fraction(1,2)]*3
    graph_cases=0
    for n in range(6):
        all_edges=list(combinations(range(n),2))
        for mask in range(1<<len(all_edges)):
            edges=[e for i,e in enumerate(all_edges) if mask>>i&1]
            valid=[choice for choice in range(1<<n)
                   if all(((choice>>u&1)+(choice>>v&1))==1 for u,v in edges)]
            adj=[[] for _ in range(n)]
            for u,v in edges:adj[u].append(v);adj[v].append(u)
            color={};components=0;bipartite=True
            for start in range(n):
                if start in color:continue
                components+=1;color[start]=0;todo=[start]
                while todo:
                    v=todo.pop()
                    for w in adj[v]:
                        if w in color:
                            if color[w]==color[v]:bipartite=False
                        else:color[w]=1-color[v];todo.append(w)
            assert len(valid)==(2**components if bipartite else 0)
            graph_cases+=1
    dual_cases=0
    for m in range(4):
        for n in range(4):
            for bits in product((0,1),repeat=m*n):
                a=[bits[i*n:(i+1)*n] for i in range(m)]
                transpose=[[a[i][j] for i in range(m)] for j in range(n)]
                covers={choice for choice in range(1<<n)
                        if all(sum(transpose[j][i] for j in range(n) if choice>>j&1)==1
                               for i in range(m))}
                hyperedges=[{j for j in range(n) if a[i][j]} for i in range(m)]
                hits={choice for choice in range(1<<n)
                      if all(len(edge & {j for j in range(n) if choice>>j&1})==1
                             for edge in hyperedges)}
                assert covers==hits;dual_cases+=1
    return dict(example_rref=dict(rank=6,unique_solution=[1,0,0,1,1,0]),
                fractional_counterexample=['1/2']*3,
                simple_graphs_through_five_vertices=graph_cases,
                transposed_zero_one_matrices=dual_cases)


def main():
    output=dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                linked_lists=list_checks(),incidence=incidence_checks(),
                scope='DLX1–5, formulas(1)–(8), and illustrated list states. General proofs are in DANCING_LINKS_FOUNDATIONS.md.')
    out=ROOT/'results/dancing_links';out.mkdir(exist_ok=True)
    (out/'foundations.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__=='__main__':main()
