"""Ordered search-tree sums and partition orders, exercises203--214."""
from pathlib import Path
from itertools import product,combinations
from functools import lru_cache
import random,json
from check_search_trees import trees,markings
ROOT=Path(__file__).parent;OUT=ROOT/'results/focus_theory';OUT.mkdir(exist_ok=True)
INF=10**9

def degree(a):return INF if a[0] else len(a[1])

@lru_cache(None)
def plus(a,b):
    if a[0]:return b
    if b[0]:return a
    if degree(a)<=degree(b):return False,tuple(plus(c,b) for c in a[1])
    return False,tuple(plus(a,c) for c in b[1])

def dominant(a):
    result={}
    def visit(a,path,maximum):
        d=degree(a);result[path]=d>maximum
        for j,b in enumerate(a[1]):visit(b,path+(j,),max(maximum,d))
    visit(a,(),-1);return result

def states(a,b):
    out=[]
    def visit(a,b,pa,pb,maximum):
        d=min(degree(a),degree(b));out.append((pa,pb,d>maximum))
        if a[0] and b[0]:return
        if degree(a)<=degree(b):
            for j,c in enumerate(a[1]):visit(c,b,pa+(j,),pb,max(maximum,d))
        else:
            for j,c in enumerate(b[1]):visit(a,c,pa,pb+(j,),max(maximum,d))
    visit(a,b,(),(),-1);return out

def graft(a,b):return b if a[0] else (False,tuple(graft(c,b) for c in a[1]))

def partitions(n):
    def rec(s):
        if len(s)==n:yield tuple(s);return
        for k in range(1+max(s,default=-1)+1):yield from rec(s+[k])
    yield from rec([])

def main():
    small=[m for n in range(1,6) for t in trees(n) for m in markings(t)]
    dom=[dominant(t) for t in small];pairs=0;node_pairs=0;converse_counter=0;grafts=0
    for i,a in enumerate(small):
        minimal=all(not v or path==() or degree_at(a,path)==INF for path,v in dom[i].items())
        for j,b in enumerate(small):
            pairs+=1
            for pa,pb,d in states(a,b):
                node_pairs+=1
                assert dom[i][pa] or dom[j][pb]
                assert not d or (dom[i][pa] and dom[j][pb])
                converse_counter+=dom[i][pa] and dom[j][pb] and not d
            if minimal and degree(a)<=degree(b):assert plus(a,b)==graft(a,b);grafts+=1
    rng=random.Random(203)
    for _ in range(10000):
        a,b,c=rng.choices(small,k=3)
        assert plus(plus(a,b),c)==plus(a,plus(b,c))
    a=(False,((True,()),));b=(False,((False,()),))
    assert plus(a,b)!=plus(b,a)
    # All partitions up to7, every bipartition replacement of two parts.
    pchecks=0;prefix_exceptions=0
    for n in range(2,8):
        for p in partitions(n):
            blocks=[{i for i,x in enumerate(p) if x==k} for k in range(max(p)+1)]
            for j,k in combinations(range(len(blocks)),2):
                union=sorted(blocks[j]|blocks[k]);smallest=union[0]
                old=tuple(sorted(blocks[j] if smallest in blocks[j] else blocks[k]))
                rest=union[1:]
                for bits in range(1<<len(rest)):
                    first={smallest}|{v for i,v in enumerate(rest) if bits>>i&1};second=set(union)-first
                    if not second:continue
                    new=tuple(sorted(first))
                    if new==old:continue
                    # Padding with infinity makes a proper prefix greater.
                    key=lambda t:t+(INF,)*(n-len(t))
                    if not key(old)<key(new):continue
                    bs=[b for x,b in enumerate(blocks) if x not in (j,k)]+[first,second]
                    bs.sort(key=min);q=tuple(next(x for x,b in enumerate(bs) if i in b) for i in range(n))
                    assert p<q,(p,q,old,new);pchecks+=1
                    prefix_exceptions+=(new<old)
    report=dict(marked_trees=len(small),tree_pairs=pairs,node_pairs=node_pairs,
                failed_converses=converse_counter,graft_cases=grafts,associativity_samples=10000,
                partition_order_checks=pchecks,ordinary_dictionary_prefix_reversals=prefix_exceptions)
    (OUT/'verified.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))

def degree_at(t,path):
    for j in path:t=t[1][j]
    return degree(t)

if __name__=='__main__':main()
