"""Literal implementation of Algorithm R, with independent truth-table oracle.

Clause and literal order are retained. No memoization, SCC preprocessing,
subsumption, or extra propagation is inserted into the measured algorithm.
"""
from itertools import combinations, product
from pathlib import Path
import json
import random


def restrict(formula, literals):
    true=set(literals);false={-l for l in true}
    assert not true&false
    return tuple(tuple(l for l in clause if l not in false)
                 for clause in formula if not true.intersection(clause))


def autarky(formula, literals):
    true=set(literals);touched=true|{-l for l in true}
    return all(not touched.intersection(clause) or true.intersection(clause)
               for clause in formula)


def add(*counts):
    return tuple(sum(c[j] for c in counts) for j in range(3))


def upper_bounds(k, limit):
    assert k>=3
    t=[0];u=[0];v=[[0]*k]
    for n in range(1,limit+1):
        oldt=t[n-2] if n>=2 else 0
        newv=[0,1+u[-1]]
        for h in range(2,k):
            newv.append(1+max(u[-1],oldt,u[-1]+v[-1][h-1]))
        newu=1+max(t[-1],oldt,*(u[-1]+v[-1][h] for h in range(1,k-1)))
        newt=1+max(t[-1],oldt,u[-1]+v[-1][k-1])
        t.append(newt);u.append(newu);v.append(newv)
    return t,u,v


def solve(formula, bounds=None, k=None, audit=None):
    """Return SAT status and the actual visit counts (R1,R2,R3)."""
    def nvars(f):
        return len({abs(l) for c in f for l in c})
    def r1(f):
        if not f:
            return True,(1,0,0)
        if () in f:
            return False,(1,0,0)
        clause=min(f,key=len)
        sat,cost=r2(f,clause,False)
        result=add((1,0,0),cost)
        if bounds:
            t,u,v=bounds;n=nvars(f)
            assert result[1]<=t[n],('T',k,n,f,result,t[n])
            if any(len(c)<k for c in f):
                assert result[1]<=u[n],('U',k,n,f,result,u[n])
            audit['R1_states']+=1
        return sat,result
    def r2(f,clause,from_r3):
        h=len(clause);l=clause[-1]
        if h==1 or autarky(f,(l,)):
            reduced=restrict(f,(l,))
            if from_r3 and k:
                assert not reduced or any(len(c)<k for c in reduced)
            sat,cost=r1(reduced)
            result=add((0,1,0),cost)
        elif autarky(f,(-l,clause[-2])):
            sat,cost=r1(restrict(f,(-l,clause[-2])))
            result=add((0,1,0),cost)
        else:
            reduced=restrict(f,(l,))
            if k:
                assert any(len(c)<k for c in reduced)
            sat,cost=r1(reduced)
            result=add((0,1,1),cost)
            if not sat:
                sat,cost=r2(restrict(f,(-l,)),clause[:-1],True)
                result=add(result,cost)
        if from_r3 and bounds:
            n=nvars(f)
            assert result[1]<=bounds[2][n][h],('V',k,n,h,result,bounds[2][n][h])
            audit['fallback_states']+=1
        return sat,result
    return r1(formula)


def brute_sat(formula,n):
    for mask in range(1<<n):
        if all(any(bool(mask&(1<<(abs(l)-1)))==(l>0) for l in c) for c in formula):
            return True
    return False


def clauses(n,k):
    result=[]
    for h in range(min(n,k)+1):
        for variables in combinations(range(1,n+1),h):
            for signs in product((-1,1),repeat=h):
                result.append(tuple(v*s for v,s in zip(variables,signs)))
    return result


def cycle_family(copies):
    f=[]
    for j in range(copies):
        a,b,c=3*j+1,3*j+2,3*j+3
        f.extend([(-a,b),(-b,c),(-c,a)])
    a,b=3*copies+1,3*copies+2
    f.extend([(a,b),(a,-b),(-a,b),(-a,-b)])
    return tuple(f)


def main():
    bounds={k:upper_bounds(k,60) for k in range(3,9)}
    fib=[0,1]
    for _ in range(64):fib.append(sum(fib[-2:]))
    t,u,v=bounds[3]
    assert all(t[n]==2*fib[n+2]-3+(n==0) and u[n]==fib[n+3]-2 and v[n][1]==fib[n+2]-1 for n in range(61))
    recurrence_checks=0
    for k,(t,u,v) in bounds.items():
        for n in range(k,61):
            assert u[n]==v[n][k-1]
            assert t[n]==u[n]+u[n-k]+1==2*u[n-1]+1
            for h in range(1,k):
                assert v[n][h]==h+sum(u[n-j] for j in range(1,h+1))
                recurrence_checks+=1
    state_audit={'R1_states':0,'fallback_states':0}
    exhaustive={}
    for n in range(1,4):
        choices=clauses(n,3);count=0
        sizes=range(len(choices)+1) if n<3 else range(5)
        for size in sizes:
            for selected in combinations(choices,size):
                sat,cost=solve(selected,bounds[3],3,state_audit)
                assert sat==brute_sat(selected,n)
                count+=1
        exhaustive[n]=count
    rng=random.Random(163164);random_cases=0
    for k in range(3,7):
        for _ in range(500):
            n=rng.randrange(3,10);pool=clauses(n,k)[1:]
            # Favor maximum-width clauses to avoid only testing easy units.
            maximum=[c for c in pool if len(c)==min(n,k)]
            selected=[]
            for _ in range(rng.randrange(1,6*n)):
                c=list(rng.choice(maximum if rng.random()<.8 else pool))
                rng.shuffle(c);selected.append(tuple(c))
            formula=tuple(selected)
            sat,cost=solve(formula,bounds[k],k,state_audit)
            assert sat==brute_sat(formula,n)
            random_cases+=1
    witness=[]
    for copies in range(11):
        formula=cycle_family(copies)
        sat,cost=solve(formula)
        assert not sat
        assert cost==(8*2**copies-4,8*2**copies-5,2**(copies+1)-1)
        if copies<3:
            assert not brute_sat(formula,3*copies+2)
        witness.append({'cycles':copies,'variables':3*copies+2,'clauses':len(formula),
                        'R1':cost[0],'R2':cost[1],'R3':cost[2]})
    report={'exhaustive_formulas_by_variables':exhaustive,
            'n3_scope':'all formulas with at most four distinct clauses, including the empty clause',
            'random_3_to_6SAT_cases':random_cases,'checked_states':state_audit,
            'general_recurrence_formula_checks':recurrence_checks,
            'F024_witnesses':witness,
            'F024_formula':'For m disjoint implication 3-cycles followed by an unsatisfiable 2-variable core, R2 visits = 8*2^m-5 with n=3m+2. Thus Algorithm R itself does not have a linear 2SAT step bound.',
            'F024_small_formula':cycle_family(1),
            'scope':'Truth-table oracle validates SAT result; actual step counts validate recurrence states for k>=3. Exponential 2SAT family uses a specific permitted minimum-clause and literal ordering; no preprocessing is added.'}
    (Path(__file__).parent/'results/recursive_sat.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
