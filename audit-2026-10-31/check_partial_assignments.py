"""Exact lattices, symbolic weights and Horn construction, SAT 363--365."""
from itertools import product,combinations
from collections import Counter
from functools import lru_cache
from pathlib import Path
import random,json
from check_surveys import R,stable_and_constrained

F=[(1,-2),(2,3),(-1,-3),(-1,-2,3)]


def clauses_on(n):
    return [tuple((i+1)*v for i,v in enumerate(row) if v) for row in product([-1,0,1],repeat=n) if any(row)]


def literal_set(a):
    return frozenset((i+1)*(1 if v else -1) for i,v in enumerate(a) if v is not None)


def weight_polynomial(a,constrained):
    wild=sum(1<<i for i,v in enumerate(a) if v is None)
    free=[i for i,v in enumerate(a) if v is not None and i+1 not in constrained]
    out={wild:1}
    for i in free:
        for mask,c in list(out.items()):out[mask|1<<i]=-c
    return out


def audit(n,clauses):
    allstates=list(product([False,True,None],repeat=n));stable={};polys={}
    for a in allstates:
        valid,constrained=stable_and_constrained(a,clauses)
        if valid:
            L=literal_set(a);stable[L]=(a,constrained);polys[L]=weight_polynomial(a,constrained)
    @lru_cache(None)
    def down(L):
        out={L}
        for l in L:
            child=L-{l}
            if child in stable:out|=down(child)
        return frozenset(out)
    weights=meets=locals=clusters=0;cores={}
    for L,(a,constrained) in stable.items():
        children=[L-{l} for l in L if L-{l} in stable]
        assert set(children)=={L-{l} for l in L if abs(l) not in constrained}
        for A,B in combinations(children,2):assert A&B in stable;locals+=1
        lower=down(L);core=set.intersection(*(set(K) for K in lower))
        core=frozenset(core);assert core in lower
        assert stable[core][1]=={abs(l) for l in core};cores[L]=core
        for A,B in combinations(lower,2):assert A&B in lower;meets+=1
        total=Counter()
        for K in lower:total.update(polys[K])
        target=sum(1<<i for i,v in enumerate(a) if v is None)
        assert {k:v for k,v in total.items() if v}=={target:1};weights+=1
    solutions=[L for L in stable if len(L)==n]
    for A,B in combinations(solutions,2):
        if len(A^B)==2:assert cores[A]==cores[B];clusters+=1
    return dict(stable=stable,down=down,cores=cores,solutions=solutions,
                counts=[len(allstates),weights,meets,locals,clusters])


def family_construction(n):
    full=(1<<n)-1;families=0
    for mask in range(1<<(1<<n)):
        if not mask>>full&1:continue
        family={S for S in range(1<<n) if mask>>S&1}
        if any(S!=full and not any(S|1<<i in family for i in range(n) if not S>>i&1) for S in family):continue
        if any(A&B not in family for A,B in combinations(family,2)):continue
        clauses=[]
        for parent in family:
            for i in range(n):
                if not parent>>i&1:continue
                child=parent^(1<<i)
                if child not in family:
                    # Corrected index in answer 363(g): child, not parent.
                    clauses.append(tuple([i+1]+[-(k+1) for k in range(n) if child>>k&1]))
        got=audit(n,clauses)
        top=frozenset(range(1,n+1))
        actual={sum(1<<(l-1) for l in L) for L in got['down'](top)}
        assert actual==family;families+=1
    return families


@lru_cache(None)
def waerden(n):
    return tuple(tuple(sign*v for v in (a,a+d,a+2*d)) for a in range(1,n+1)
                 for d in range(1,(n-a)//2+1) for sign in (1,-1))


def main():
    formulas=0;totals=[0]*5
    def run(n,clauses):
        nonlocal formulas
        result=audit(n,clauses);formulas+=1
        for i,value in enumerate(result['counts']):totals[i]+=value
        return result
    C=clauses_on(2)
    for mask in range(1<<len(C)):run(2,[c for k,c in enumerate(C) if mask>>k&1])
    C=clauses_on(3)
    for k in range(4):
        for clauses in combinations(C,k):run(3,clauses)
    rng=random.Random(363);C=clauses_on(4)
    for _ in range(1000):run(4,rng.sample(C,rng.randrange(1,13)))
    # Book examples 363(b,d,e,f), 364(b,c,f).
    f=run(3,F)
    assert set(f['stable'])=={frozenset(),frozenset([-1,-2,3])}
    r=run(4,R)
    covers=[L for L,(a,c) in r['stable'].items() if c=={abs(l) for l in L}]
    assert covers==[frozenset()]
    assert set(r['solutions'])=={frozenset([-1,2,-3,4]),frozenset([-1,2,3,4])}
    for L in r['solutions']:assert r['stable'][L][1]=={1,2,4}
    single=run(3,[(1,2,3)]);top=frozenset([1,-2,-3])
    assert len(single['down'](top))==7 and frozenset([-2,-3]) not in single['down'](top)
    example=[(-1,-2,3,-4,-5),(-1,4),(-2,5),(-3,4,-5),(-3,-4,5)]
    five=run(5,example);top=frozenset(range(1,6))
    expected=[[],[4],[5],[1,4],[2,5],[4,5],[1,4,5],[2,4,5],[3,4,5],[1,3,4,5],[2,3,4,5],[1,2,3,4,5]]
    assert five['down'](top)==frozenset(map(frozenset,expected))
    assert frozenset([3]) in five['stable'] and frozenset([3]) not in five['down'](top)
    anti_middle=[(-1,-2,3,4),(-1,2,-3,4),(-1,2,3,-4),(1,-2,-3,4),(1,-2,3,-4),(1,2,-3,-4)]
    split=run(4,anti_middle)
    assert sorted(Counter(sum(l>0 for l in L) for L in split['solutions']).items())==[(0,1),(1,4),(3,4),(4,1)]
    assert set(split['cores'][L] for L in split['solutions'])=={frozenset()}
    # Printed construction includes x_l and -x_l, hence gives tautologies.
    # Normalize those away before applying the strict-literal definitions.
    # Otherwise "unique true literal" is not equivalent to a constrained
    # variable, since flipping it can satisfy its own complementary copy.
    printed_clause=(1,-1,-2)
    assert any(-l in printed_clause for l in printed_clause)
    printed=run(2,[])
    assert frozenset([2]) in printed['down'](frozenset([1,2]))
    corrected=run(2,[(1,-2)])
    assert corrected['down'](frozenset([1,2]))==frozenset(map(frozenset,[[],[1],[1,2]]))
    family_counts={}
    for n in range(1,5):
        family_counts[n]=family_construction(n)
        print('intersection families',n,family_counts[n],flush=True)
    base=[]
    for a in product([False,True],repeat=8):
        good,c=stable_and_constrained(a,waerden(8))
        if good:assert c==set(range(1,9));base.append(a)
    assert len(base)==6
    lifts=0
    for q in range(1,12,2):
        for d in range(q):
            for n in range(8*q-d,9*q-d):
                for a in base:
                    b=[None]*n
                    for i,v in enumerate(a,1):b[q*i-d-1]=v
                    good,c=stable_and_constrained(b,waerden(n))
                    assert good and c=={q*i-d for i in range(1,9)};lifts+=1
    result=dict(formulas=formulas,partial_assignments=totals[0],symbolic_weight_identities=totals[1],
                meet_checks=totals[2],local_diamonds=totals[3],adjacent_solution_cores=totals[4],
                intersection_families=family_counts,waerden8_solutions=[''.join(str(int(v)) for v in a) for a in base],
                scaled_covering_assignments=lifts,
                F047='Answer363(g): negative literals must be indexed by L, not L-prime; otherwise every clause is tautological.',
                F048='Answer364(c): empty assignment has four stars, not three.')
    Path('results/partial_assignments.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
