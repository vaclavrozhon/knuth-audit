"""Literal B/B*/W implementations and independent finite checks for 7.2.2--1..14."""
from pathlib import Path
from itertools import product, permutations, combinations
from collections import Counter
import json
import random
from math import comb, factorial

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/backtrack_basics'
OUT.mkdir(exist_ok=True)


def basic(domains, predicate, walker=False):
    n = len(domains)
    x = [None] * n
    slot = [0] * n
    choices = [None] * n
    committed = []
    visited = []
    answers = []
    level = 0
    state = 'enter'
    while True:
        if state == 'enter':
            assert committed == x[:level]
            visited.append(tuple(committed))
            if level == n:
                answers.append(tuple(x))
                state = 'back'
            else:
                choices[level] = [v for v in domains[level]
                                  if not walker or predicate(tuple(x[:level]+[v]))]
                slot[level] = 0
                state = 'try'
        elif state == 'try':
            if slot[level] == len(choices[level]):
                state = 'back'
            else:
                x[level] = choices[level][slot[level]]
                if walker or predicate(tuple(x[:level+1])):
                    committed.append(x[level])
                    level += 1
                    state = 'enter'
                else:
                    slot[level] += 1
        else:
            level -= 1
            if level < 0:
                return answers, visited
            assert committed.pop() == x[level]
            slot[level] += 1
            state = 'try'


def valid_queens(x):
    n = len(x)
    return (set(x) == set(range(n)) and len({i+v for i,v in enumerate(x)}) == n
            and len({i-v for i,v in enumerate(x)}) == n)


def queens_star(n):
    # Literal B* arrays; no bit masks and no recursive search.
    a = [0] * (n+1)
    b = [0] * (2*n+1)
    c = [0] * (2*n+1)
    x = [0] * (n+1)
    level, state = 1, 2
    answers, profile = [], [0] * (n+1)
    while True:
        if state == 2:
            profile[level-1] += 1
            if level > n:
                answers.append(tuple(v-1 for v in x[1:]))
                state = 5
            else:
                t, state = 1, 3
        elif state == 3:
            if a[t] or b[t+level-1] or c[t-level+n]:
                state = 4
            else:
                a[t] = b[t+level-1] = c[t-level+n] = 1
                x[level] = t
                level += 1
                state = 2
        elif state == 4:
            if t < n:
                t += 1
                state = 3
            else:
                state = 5
        else:
            level -= 1
            if level == 0:
                assert not any(a+b+c)
                return answers, profile
            t = x[level]
            c[t-level+n] = b[t+level-1] = a[t] = 0
            state = 4


def queens_bits(n):
    full = (1 << n) - 1
    models, profile = [], [0] * (n+1)
    def search(prefix, cols, left, right):
        profile[len(prefix)] += 1
        if len(prefix) == n:
            models.append(prefix)
            return
        available = full & ~(cols | left | right)
        while available:
            bit = available & -available
            available -= bit
            search(prefix+(bit.bit_length()-1,), cols|bit, (left|bit)>>1, ((right|bit)<<1)&full)
    search((), 0, 0, 0)
    return models, profile


def partition_oracle(n, maximum=None):
    if n == 0:
        return [()]
    return [(first,)+rest for first in range(1, min(n,maximum or n)+1)
            for rest in partition_oracle(n-first,first)]


def main():
    rng = random.Random(722)
    for trial in range(500):
        n = rng.randrange(6)
        domains = [sorted(rng.sample(range(-3,8),rng.randrange(1,5))) for _ in range(n)]
        allowed = {()}
        for depth in range(1,n+1):
            for prefix in product(*domains[:depth]):
                if prefix[:-1] in allowed and rng.randrange(4):
                    allowed.add(prefix)
        oracle = sorted(p for p in allowed if len(p)==n)
        b, nodes = basic(domains,lambda p:p in allowed)
        w, other = basic(domains,lambda p:p in allowed,True)
        assert b == w == oracle and nodes == other
        assert set(nodes) == allowed

    counterexample = dict(domains=[[1,3]],predicate='always true',
                          algorithm_B=[[1],[3]],printed_recursive=[[1],[2],[3]],
                          correction='iterate over elements of D_l in increasing order')
    assert basic([[1,3]],lambda p:True)[0] == [(1,),(3,)]
    assert list(range(1,4)) == [1,2,3]
    (OUT/'recursive-domain-counterexample.json').write_text(json.dumps(counterexample,indent=2)+'\n')

    generators = []
    for n in range(1,9):
        d = [list(range(1,n+1))]*n
        perm,_ = basic(d,lambda p:len(set(p))==len(p))
        assert perm == list(permutations(range(1,n+1)))
        d = [list(range(n//k+1)) for k in range(1,n+1)]
        parts,_ = basic(d,lambda p:all(a>=b for a,b in zip(p,p[1:])) and n-(n-len(p))*p[-1]<=sum(p)<=n)
        assert {tuple(v for v in p if v) for p in parts} == set(partition_oracle(n))
        d = [list(range(k)) for k in range(1,n+1)]
        rgs,_ = basic(d,lambda p:all(p[j]<=1+max(p[:j]) for j in range(1,len(p))))
        # Independent Bell-number recurrence by choosing the block containing 1.
        bell = [1]
        for j in range(1,n+1):bell.append(sum(comb(j-1,k)*bell[k] for k in range(j)))
        assert len(rgs) == bell[n]
        d = [list(range(1,2*k)) for k in range(1,n+1)]
        parens,_ = basic(d,lambda p:all(a<b for a,b in zip(p,p[1:])))
        oracle = [p for p in combinations(range(1,2*n+1),n)
                  if all(2*sum(v<=j for v in p)>=j for j in range(1,2*n+1))]
        assert parens == oracle and len(parens)==comb(2*n,n)//(n+1)
        generators.append(dict(n=n,permutations=len(perm),partitions=len(parts),set_partitions=len(rgs),parentheses=len(parens)))
    for N in range(1,10):
        for n in range(1,min(N,6)+1):
            d = [list(range(1,N+2-k)) for k in range(1,n+1)]
            actual,_ = basic(d,lambda p:all(a>b for a,b in zip(p,p[1:])))
            assert set(actual)=={tuple(reversed(c)) for c in combinations(range(1,N+1),n)}

    queen_report=[]
    for n in range(1,13):
        models,profile=queens_bits(n)
        assert all(valid_queens(x) for x in models)
        if n<=10:
            literal,p2=queens_star(n)
            assert literal==models and p2==profile
        if n<=9:
            assert models==[p for p in permutations(range(n)) if valid_queens(p)]
        quarter=[x for x in models if {(x[i],n-1-i) for i in range(n)}==set(enumerate(x))]
        canonical=[x for x in quarter if all(x[i]>i for i in range(n//2))]
        assert len(quarter)==2**(n//4)*len(canonical)
        torus=[x for x in models if len({(v-i)%n for i,v in enumerate(x)})==n and len({(v+i)%n for i,v in enumerate(x)})==n]
        assert bool(torus)==(n%2!=0 and n%3!=0)
        queen_report.append(dict(n=n,solutions=len(models),profile=profile,quarterturn=len(quarter),canonical_quarterturn=len(canonical),toroidal=len(torus)))
        if n==8:
            assert profile==[1,8,42,140,344,568,550,312,92]
            assert sum(x[0]<4 for x in models)==46
    omitted=[]
    for missing in range(8):
        rows=[r for r in range(8) if r!=missing]
        models=[p for p in permutations(range(8),7)
                if len({r+c for r,c in zip(rows,p)})==7 and len({r-c for r,c in zip(rows,p)})==7]
        omitted.append([len(models),sum(missing not in p for p in models)])
    assert [x[0] for x in omitted]==[312,396,430,458,458,430,396,312]
    assert [x[1] for x in omitted]==[40,46,42,80,80,42,46,40]

    framed=[2,17,12,10,7,14,3,5,9,13,15,4,11,8,6,1,16]
    assert valid_queens([v-1 for v in framed])
    for s in ['42736815','42736851','57263148','57263184']:
        assert valid_queens([int(v)-1 for v in s])
    white_witnesses=[[5,8,13,16,3,7,15,11,6,2,10,14,1,4,9,12],
                     [7,10,13,20,17,24,3,6,23,11,16,21,4,9,14,2,19,22,1,8,5,12,15,18]]
    for x in white_witnesses:
        assert valid_queens([v-1 for v in x])
        assert sum((i+1+v)%2==0 for i,v in enumerate(x))==3*len(x)//4

    for n in range(1,501):
        if n%2 and n%3:
            for slope in [2,3]:
                x=[(slope*k)%n for k in range(1,n+1)]
                assert valid_queens(x) and len({(x[k]-k)%n for k in range(n)})==n and len({(x[k]+k)%n for k in range(n)})==n
        if n>2 and n%6 in [2,4]:
            x=[(n//2+2*k-3*(2*k<=n))%n for k in range(1,n+1)]
            assert valid_queens(x) and all(v!=i for i,v in enumerate(x))
            assert valid_queens(x+[n])
    base=queens_bits(4)[0]
    torus=[x for x in queens_bits(5)[0] if len({(v-i)%5 for i,v in enumerate(x)})==5 and len({(v+i)%5 for i,v in enumerate(x)})==5]
    composed=set()
    for xs in product(base,repeat=5):
        for y in torus:
            X=tuple(xs[j][i]*5+y[j] for i in range(4) for j in range(5))
            assert valid_queens(X)
            composed.add(X)
    assert len(composed)==len(base)**5*len(torus)
    report=dict(status='pass',random_trees=500,generators=generators,queens=queen_report,
                omitted_row_counts=omitted,composition_4_times_5=len(composed),
                framed17=framed,white_witnesses=white_witnesses,
                limits='No recomputation of Q(27), framed Q(27), historical timings, or Simkin asymptotics.')
    (OUT/'verified.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('generators','queens')}))


if __name__=='__main__':main()
