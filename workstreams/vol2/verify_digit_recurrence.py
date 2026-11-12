#!/usr/bin/env python3
"""Exact pattern recurrence and separate radix-one sumset certificates, 4.1-33."""
from collections import defaultdict
from itertools import combinations, product
from heapq import heappop, heappush
from math import gcd
from functools import reduce
from pathlib import Path
import json
import sympy as sp

ROOT=Path(__file__).resolve().parent
TARGET=ROOT/'results/digit-recurrence.json'


def normalize(s):
    m=min(s)
    return tuple(sorted(x-m for x in s))


def row(pattern,digits,base):
    coefficients=defaultdict(int)
    for j in range(base):
        choices=[[d for d in digits if (s+j-d)%base==0] for s in pattern]
        raw_patterns={frozenset((s+j-d)//base for s,d in zip(pattern,ds))
                      for ds in product(*choices)}
        # Incrementally expand the union's indicator. Keep absolute positions
        # until all intersections (= unions of patterns) have been formed.
        partial={}
        for t in sorted(raw_patterns,key=lambda t:tuple(sorted(t))):
            next_coeff=defaultdict(int,partial)
            next_coeff[t]+=1
            for u,c in partial.items():
                next_coeff[u|t]-=c
            partial={u:c for u,c in next_coeff.items() if c}
        for t,c in partial.items():
            coefficients[normalize(t)]+=c
    return {t:c for t,c in coefficients.items() if c}


def matrix(digits,base):
    assert digits and base>=2
    h=(max(digits)-min(digits)+base-2)//(base-1)
    patterns=[(0,)+tuple(i+1 for i in range(h) if mask>>i&1)
              for mask in range(1<<h)]
    index={s:i for i,s in enumerate(patterns)}
    rows=[row(s,digits,base) for s in patterns]
    assert all(max(t)<=h for r in rows for t in r)
    m=[[r.get(t,0) for t in patterns] for r in rows]
    return patterns,m


def pattern_count(values,pattern):
    return sum(all(x+s in values for s in pattern) for x in values)


def multiply(m,v):
    return [sum(a*b for a,b in zip(r,v)) for r in m]


def verify_matrix(digits,base,depth):
    patterns,m=matrix(digits,base)
    vector=[int(len(s)==1) for s in patterns]
    values={0};history=[]
    for n in range(depth+1):
        direct=[pattern_count(values,s) for s in patterns]
        assert vector==direct,(digits,base,n,vector,direct)
        history.append(vector)
        if n<depth:
            values={base*x+d for x in values for d in digits}
            vector=multiply(m,vector)
    return patterns,m,history


def semigroup_minima(ds,h):
    # Shortest value in each residue class modulo h, with shortest length to
    # break ties. Dijkstra uses the positive generators as edge weights.
    best=[None]*h;best[0]=(0,0);heap=[(0,0,0)]
    while heap:
        w,ell,r=heappop(heap)
        if best[r]!=(w,ell):continue
        for d in ds:
            if d==0:continue
            rr=(r+d)%h;new=(w+d,ell+1)
            if best[rr] is None or new<best[rr]:
                best[rr]=new;heappush(heap,(*new,rr))
    assert all(v is not None for v in best)
    return best


def base_one(digits):
    if not digits:return {'kind':'empty','gf':'1'}
    if len(digits)==1:return {'kind':'singleton','gf':'1/(1-z)'}
    ds=[d-min(digits) for d in digits];g=reduce(gcd,ds);ds=[d//g for d in ds]
    h=max(ds);left=semigroup_minima(ds,h);right=semigroup_minima([h-d for d in ds],h)
    n0=max(left[r][1]+right[(-r)%h][1] for r in range(h))
    gaps_left=sum((w-r)//h for r,(w,ell) in enumerate(left))
    gaps_right=sum((w-r)//h for r,(w,ell) in enumerate(right))
    counts=[];values={0}
    for n in range(n0+11):
        counts.append(len(values))
        if n>=n0:assert len(values)==n*h+1-gaps_left-gaps_right,(digits,n,n0)
        values={x+d for x in values for d in ds}
    # Independent check of the claimed gap counts within a sufficient range.
    for minima, generators, gaps in [(left,ds,gaps_left),(right,[h-d for d in ds],gaps_right)]:
        bound=max(w for w,ell in minima)+h
        reachable={0}
        for x in range(bound+1):
            if x in reachable:
                reachable.update(x+d for d in generators if x+d<=bound)
        assert sum(x not in reachable for x in range(bound+1))==gaps
    return {'digits':list(digits),'normalized_digits':ds,'step_gcd':g,'slope':h,
            'threshold':n0,'gaps':[gaps_left,gaps_right],'left_minima':left,
            'right_minima':right,'counts':counts}


def main():
    out=json.loads(TARGET.read_text()) if TARGET.exists() else {}
    if out.get('status')=='passed':raise SystemExit('Refusing to repeat successful checks.')
    def save():TARGET.write_text(json.dumps(out,indent=2)+'\n')
    if 'printed_example' not in out:
        patterns,m,history=verify_matrix([-1,0,3],3,10)
        assert patterns==[(0,),(0,1),(0,2),(0,1,2)]
        assert m==[[3,-1,0,0],[1,0,0,0],[0,1,1,-1],[0,0,0,0]]
        assert history[:4]==[[1,0,0,0],[3,1,0,0],[8,3,1,0],[21,8,4,0]]
        z=sp.symbols('z');f=(sp.eye(4)-z*sp.Matrix(m)).inv()*sp.Matrix([1,0,0,0])
        assert sp.cancel(f[0]-1/(1-3*z+z*z))==0
        for n,v in enumerate(history):
            assert v[0]==sp.fibonacci(2*n+2)
            assert v[2]==sp.fibonacci(2*n-1)-1
        out['printed_example']={'patterns':patterns,'matrix':m,'history':history,
                                'generating_functions':[str(sp.factor(x)) for x in f]}
        save();print('PASS printed matrix, generating functions, Fibonacci values',flush=True)
    if 'general_matrices' not in out:
        cases=0;coordinates=0;max_dimension=0
        for size in range(1,5):
            for ds in combinations(range(-2,4),size):
                for b in range(2,6):
                    patterns,m,history=verify_matrix(ds,b,5)
                    cases+=1;coordinates+=len(patterns)*len(history)
                    max_dimension=max(max_dimension,len(patterns))
        out['general_matrices']={'cases':cases,'pattern_values':coordinates,'max_dimension':max_dimension,'depth':5}
        save();print('PASS general matrices',out['general_matrices'],flush=True)
    if 'radix_one' not in out:
        cases=[base_one([])]
        for size in range(1,6):
            for ds in combinations(range(-3,5),size):
                cases.append(base_one(ds))
        for ds in [[0,6,9,20],[-8,-2,1,12],[0,4,7,25],[0,17,31],[2,8,14,20]]:
            cases.append(base_one(ds))
        out['radix_one']={'cases':len(cases),'eventual_linear':sum('slope' in c for c in cases),
                          'max_threshold':max(c.get('threshold',0) for c in cases),
                          'examples':cases[-5:]}
        save();print('PASS radix-one semigroups and direct sumsets',out['radix_one']['cases'],flush=True)
    out['status']='passed';save()


if __name__=='__main__':main()
