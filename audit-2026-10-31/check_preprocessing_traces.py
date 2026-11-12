"""Replay the concrete refutations in SAT 371 and 373."""
from pathlib import Path
from collections import Counter
import json
from check_preprocessing import eliminate, resolve, direct_cores, substitution


def c(*literals):
    return frozenset(literals)


def waerden():
    f = {c(sign*a, sign*(a+d), sign*(a+2*d))
         for d in range(1,5) for a in range(1,10-2*d) for sign in (-1,1)}
    assert len(f) == 32
    expected1 = {c(*x) for x in ((2,3,-4,-7),(-2,-3,4,7),(2,3,-5,-9),
        (-2,-3,5,9),(3,-4,5,-7),(-3,4,-5,7),(4,-5,7,-9),(-4,5,-7,9))}
    expected8 = {c(*x) for x in ((2,-4,5,-6),(-2,4,-5,6),(2,5,-6,-7),
        (-2,-5,6,7),(2,5,-7,-9),(-2,-5,7,9),(4,6,-7,-9),(-4,-6,7,9))}
    for variable, expected in ((1,expected1),(8,expected8)):
        new, positive, negative = eliminate(f,variable)
        assert len(positive)+len(negative) == 8
        unchanged = f-set(positive)-set(negative)
        assert new-unchanged == expected
        f = new
    changes = [((2,3,-4,-7),(2,3,-7)),((3,-4,5,-7),(3,5,-7)),
        ((3,5,7),(3,5)),((2,3,-5,-9),(2,3,-9)),((-2,-3,5,9),(-2,-3,9)),
        ((-2,-5,7,9),(-2,7,9)),((-2,4,-5,6),(-2,4,6)),((2,4,6),(4,6)),
        ((-2,-5,6,7),(-2,6,7)),((-4,5,-7,9),(-4,5,9)),
        ((-2,-3,4,7),(-2,-3,7)),((-3,4,-5,7),(-3,-5,7)),
        ((-3,-5,-7),(-3,-5)),((2,-4,5,-6),(2,-4,-6)),
        ((-2,-4,-6),(-4,-6)),((2,5,-6,-7),(2,-6,-7)),
        ((4,-5,7,-9),(4,-5,-9)),((2,5,-7,-9),(2,-7,-9))]
    pending = [(c(*a),c(*b)) for a,b in changes]
    trace = []
    passes = 0
    while pending:
        passes += 1
        progress = False
        for old,new in pending.copy():
            assert old in f, (old,new)
            literal, = old-new
            witness = next((d for d in f if -literal in d and d-{-literal} <= new),None)
            if witness is None:
                continue
            f.remove(old); f.add(new); pending.remove((old,new))
            trace.append({'old':sorted(old),'new':sorted(new),'witness':sorted(witness)})
            progress = True
        assert progress, ('No listed step can be applied',pending)
    # Carry out the explicitly stated subsumptions and any resulting duplicates.
    f = {a for a in f if not any(b<a for b in f)}
    stages = []
    expected4 = {c(*x) for x in ((2,3,-6),(-2,-3,6),(5,6,9),(-5,-6,-9))}
    expected3 = {c(*x) for x in ((2,-5,-6),(-2,5,6),(2,-5,-7),(-2,5,7),
                  (2,-5,-9),(-2,5,9),(5,-6,-9),(-5,6,9))}
    expected2 = {c(*x) for x in ((5,6,-7,-9),(5,-6,-7,9),(-5,6,7,-9),(-5,-6,7,9))}
    for variable, oldcount, expected in ((4,6,expected4),(3,10,expected3),(2,10,expected2)):
        full, positive, negative = eliminate(f,variable)
        unchanged = f-set(positive)-set(negative)
        assert len(positive)+len(negative) == oldcount
        if variable in (4,3):
            possibilities = [(l,core,substitution(f,l,core)) for l in (variable,-variable)
                             for core in direct_cores(f,l)]
            match = next(((l,core,new) for l,core,new in possibilities if new-unchanged == expected),None)
            assert match is not None, (variable,expected,possibilities)
            literal,core,f = match
            stages.append({'variable':variable,'literal':literal,'core':sorted(core),
                           'old_count':oldcount,'new_count':len(expected)})
        else:
            assert full-unchanged == expected
            f=full
    for variable in (7,9):
        f,_,_=eliminate(f,variable)
    assert f == {c(5,6),c(5,-6),c(-5,6),c(-5,-6)}
    for variable in (5,6):
        f,_,_=eliminate(f,variable)
    assert f == {frozenset()}
    return {'self_subsumptions':trace,'passes_needed_in_printed_listing_order':passes,
            'substitution_stages':stages,'final_clause':'empty'}


def maximal_element(m,counts):
    # Keep a fixed encoding while successively reducing the parameter.
    x=lambda i,j: (i-1)*m+j
    M=lambda i,k: frozenset(x(i,j) for j in range(1,k+1))
    def system(k):
        return ({c(-x(j,j)) for j in range(1,k+1)} |
                {M(j,k) for j in range(1,k+1)} |
                {c(-x(i,j),-x(j,h),x(i,h))
                 for j in range(1,k+1) for i in range(1,j) for h in range(1,j)})
    f=system(m)
    assert len(f)==2*m+sum(j*j for j in range(m))
    for k in range(m,1,-1):
        for i in range(1,k+1):
            f,positive,negative=eliminate(f,x(i,k))
            assert len(positive)==1
            counts['column_eliminations']+=1
        for i in range(1,k):
            for h in range(1,k):
                assert M(i,k-1)|{-x(k,h)} in f
        assert M(k,k-1) in f
        f,positive,negative=eliminate(f,x(k,k-1))
        assert len(positive)==1 and len(negative)==k-1
        for i in range(1,k):
            current=M(i,k-1)|M(k,k-2)
            assert current in f
            for h in range(1,k-1):
                witness=M(i,k-1)|{-x(k,h)}
                assert witness in f
                updated=resolve(current,witness,x(k,h))
                assert updated==current-{x(k,h)}
                f.remove(current);f.add(updated);current=updated
                counts['self_subsumptions']+=1
        f={a for a in f if not any(b<a for b in f)}
        assert f==system(k-1), (m,k)
        counts['parameter_reductions']+=1
    f,_,_=eliminate(f,x(1,1))
    assert f=={frozenset()}
    counts['refuted_instances']+=1


def main():
    first=waerden()
    counts=Counter()
    for m in range(2,16):
        maximal_element(m,counts)
    out={'status':'all assertions passed','371':first,'373':dict(counts)}
    (Path(__file__).parent/'results/preprocessing_traces.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':
    main()
