"""Exact-cover 29-30: every small ordered tree, with every leaf marking."""
from collections import Counter
from functools import lru_cache
from itertools import product
from pathlib import Path
import json
from algorithm_x import DLX


@lru_cache(None)
def forests(size):
    if not size:
        return ((),)
    return tuple((first,)+rest for firstsize in range(1,size+1)
                 for first in trees(firstsize) for rest in forests(size-firstsize))


@lru_cache(None)
def trees(size):
    return forests(size-1)


def markings(tree):
    if not tree:
        yield False,()
        yield True,()
    else:
        for children in product(*(tuple(markings(child)) for child in tree)):
            yield False,children


def construct(node,path=()):
    solved,children=node
    if not children:
        # The 2023-03-22 erratum changes a marked solution leaf to 0x0.
        return ([],[]) if solved else ([path+('leaf',)],[])
    blocks=[construct(child,path+(j,)) for j,child in enumerate(children)]
    oldcols=[c for cols,_ in blocks for c in cols]
    newcols=[path+(tag,) for tag in ('zero','one','two')]
    rows=[row for _,blockrows in blocks for row in blockrows]
    for cols,_ in blocks:
        own=set(cols)
        rows.append(tuple(newcols+[c for c in oldcols if c not in own]))
    for j in (0,1):
        rows.append(tuple([newcols[j]]+oldcols))
    return newcols+oldcols,rows


def immutable_search(items,rows):
    """Record the entire ordered tree, using sets rather than dancing links."""
    if not items:
        return True,()
    lengths=[sum(item in row for row in rows) for item in items]
    best=min(lengths)
    assert lengths.count(best)==1, ('MRV is not unique',items,lengths)
    chosen=items[lengths.index(best)]
    children=[]
    for row in rows:
        if chosen in row:
            covered=set(row)
            children.append(immutable_search([x for x in items if x not in covered],
                              [other for other in rows if covered.isdisjoint(other)]))
    return False,tuple(children)


def profile(node):
    counts=Counter();solutions=0
    def walk(node,level):
        nonlocal solutions
        counts[level]+=1
        solved,children=node
        solutions+=solved
        for child in children:
            walk(child,level+1)
    walk(node,0)
    return counts,solutions


def main():
    counts={};total=0;duplicate_cases=0
    for size in range(1,9):
        marked_count=0
        for tree in trees(size):
            for node in markings(tree):
                items,rows=construct(node)
                assert immutable_search(items,rows)==node
                expected_profile,expected_solutions=profile(node)
                measured=DLX(items,rows).solve()
                assert measured.nodes_by_depth==expected_profile
                assert measured.solution_count==expected_solutions
                assert sum(expected_profile.values())==size
                marked_count+=1
                duplicate_cases+=len(set(rows))!=len(rows)
        counts[size]={'ordered_tree_shapes':len(trees(size)),'leaf_markings':marked_count}
        total+=marked_count
    report={'exercises':'7.2.2.1-29,30','trees_by_size':counts,
            'total_marked_trees':total,'cases_with_duplicate_options':duplicate_cases,
            'checks':'Full ordered tree and solution/dead-leaf labels match an independent immutable-set search. MRV minimum is unique at every visited non-solution node. DLX independently matches node profiles and solution counts.',
            'known_erratum':'2023-03-22: a tree consisting only of a solution root uses a matrix with no rows or columns. The corrected recursive construction is used.',
            'findings':'No additional discrepancy after the published correction.',
            'limitation':'Finite enumeration covers every ordered tree up to eight vertices and every leaf marking; the induction proof is in the notes.'}
    (Path(__file__).parent/'results/search_trees.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
