"""Check answer 162 against resolution and the definition of an autarky."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
from check_recursive_sat import clauses, brute_sat


def graph(formula,n):
    literals=tuple(range(1,n+1))+tuple(range(-1,-n-1,-1))
    return {l:{a for a in literals if abs(a)!=abs(l)
               and all(-a not in c or l in c for c in formula)} for l in literals}


def components(g):
    reach={l:{l}|set(a) for l,a in g.items()}
    for middle in g:
        for start in g:
            if middle in reach[start]:
                reach[start]|=reach[middle]
    unseen=set(g);answer=[]
    while unseen:
        l=min(unseen);component={a for a in g if a in reach[l] and l in reach[a]}
        unseen-=component;answer.append(component)
    return answer


def is_autarky(formula,literals):
    a=set(literals)
    if any(-l in a for l in a):return False
    return all(not a.intersection(-l for l in c) or a.intersection(c) for c in formula)


def blocked_by_resolution(formula,candidate):
    for pivot in candidate:
        valid=True
        for clause in formula:
            if -pivot not in clause:continue
            resolvent=(set(candidate)-{pivot})|(set(clause)-{-pivot})
            if not any(-l in resolvent for l in resolvent):
                valid=False;break
        if valid:return True
    return False


def main():
    # The book defines a -> l when every clause containing -l contains a.
    # F025 was withdrawn on 2026-11-12: the old audit transposed this graph.
    degree_witness=((-1,2),(1,2),(-2,3),(-3,2))
    binary_witness=((1,2,3),(-1,3),(-1,-3),(-2,3),(-2,-3))
    inconsistent_witness=((1,-2,3),(-1,2,-3))
    checks=0
    for formula in [degree_witness,binary_witness,inconsistent_witness]:
        g=graph(formula,3)
        k=max(map(len,formula))
        for l in g:
            if any(-l in c for c in formula):
                assert sum(l in g[a] for a in g)<k
        for pair in clauses(3,2):
            if len(pair)!=2:continue
            p,q=pair
            printed=(q in g[-p]) or (p in g[-q])
            assert printed==blocked_by_resolution(formula,(p,q))
            checks+=1
    g=graph(binary_witness,3)
    assert 2 not in g[-1] and 1 not in g[-2]
    assert brute_sat(binary_witness,3)
    assert not brute_sat(binary_witness+((1,2),),3)
    g=graph(inconsistent_witness,3)
    assert components(g)==[set(g)]
    assert not is_autarky(inconsistent_witness,set(g))
    report={
        'source_review':'2026-11-12: original p.579 has lprime -> l; previous graph was transposed.',
        'F025_status':'dismissed',
        'binary_resolution_comparisons':checks,
        'F025_binary_witness':{'printed_rule_allows_xy':False},
        'F026':{'status':'confirmed','formula':inconsistent_witness,'component':sorted(g)},
        'scope':'Three targeted witness formulas; original orientation checked against direct resolution. No repeated exhaustive census.'}
    (Path(__file__).parent/'results/blocking_graph.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
