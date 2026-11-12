#!/usr/bin/env python3
"""Exact checks of TAOCP L, extended L, inverses and integer linear equations."""
from collections import Counter
from itertools import product
from math import gcd
from pathlib import Path
import json, random, sys, time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/gcd-extensions.json'


def extended_l(u, v, base, p, counts=None, trace=None):
    assert u >= v >= 0 and base >= 2 and p >= 1
    origin = (u, v); W = base**p
    x, y = (1, 0, u), (0, 1, v)
    if counts is None: counts = Counter()
    scale = 1
    while y[2] >= W:
        u, v = x[2], y[2]
        # Reuse the previous scale: u only decreases. This is exactly the
        # same minimal radix power, without rebuilding it at every block.
        while scale > 1 and u // (scale//base) < W: scale //= base
        while u // scale >= W: scale *= base
        assert u//scale < W and (scale==1 or u//(scale//base) >= W)
        h, j = u // scale, v // scale
        A, B, C, D = 1, 0, 0, 1
        exact_u, exact_v = u, v
        qs = []
        while True:
            upp, vpp, up, vp = h+A, j+C, h+B, j+D
            assert 0 <= upp <= W and 0 <= vpp < W
            assert 0 <= up < W and 0 <= vp <= W
            assert vpp or vp
            assert abs(A*D-B*C) == 1
            assert all(abs(t) < W for t in [A,B,C,D,h,j])
            assert A*B <= 0 and C*D <= 0
            # Cross multiplication checks both endpoint brackets without floats.
            c1 = up*exact_v-vp*exact_u
            c2 = upp*exact_v-vpp*exact_u
            assert c1*c2 < 0
            counts['inner_tests'] += 1
            if upp == W or vp == W:
                assert not qs
                counts['endpoint_word_overflow'] += 1
            if not vpp or not vp:
                counts['zero_endpoint_stops'] += 1; break
            q = upp // vpp
            if q != up // vp:
                counts['unequal_quotient_stops'] += 1; break
            assert 1 <= q < W and q == exact_u // exact_v
            assert q == h // j
            assert abs(q*C) < W and abs(q*D) < W and q*j < W
            A, B, C, D = C, D, A-q*C, B-q*D
            h, j = j, h-q*j
            exact_u, exact_v = exact_v, exact_u-q*exact_v
            assert exact_v > 0
            qs.append(q); counts['simulated_steps'] += 1
            assert (A*u+B*v,C*u+D*v) == (exact_u,exact_v)
        assert (B == 0) == (len(qs) == 0)
        if B == 0:
            q = u//v
            x, y = y, tuple(x[i]-q*y[i] for i in range(3))
            counts['full_divisions'] += 1
            if q == 1: counts['full_divisions_with_quotient_one'] += 1
        else:
            x, y = (tuple(A*x[i]+B*y[i] for i in range(3)),
                    tuple(C*x[i]+D*y[i] for i in range(3)))
            counts['matrix_batches'] += 1
        if trace is not None:
            trace.append(dict(input=[u,v],heads=[u//scale,v//scale],scale=scale,
                              matrix=[A,B,C,D],quotients=qs,output=[x[2],y[2]]))
        assert x[2] >= y[2] >= 0 and y[2] < v
        for row in [x,y]: assert row[0]*origin[0]+row[1]*origin[1] == row[2]
    while y[2]:
        q = x[2]//y[2]
        x, y = y, tuple(x[i]-q*y[i] for i in range(3))
        counts['final_euclidean_steps'] += 1
    assert x[2] == gcd(*origin)
    assert x[0]*origin[0]+x[1]*origin[1] == x[2]
    return x


def lehmer():
    counts = Counter(); pairs = 0
    configs = [(2,1),(2,4),(3,2),(10,1),(10,2),(10,4),(64,1),(100,1)]
    rng = random.Random(45218)
    for b,p in configs:
        for u in range(181):
            for v in range(u+1):
                extended_l(u,v,b,p,counts); pairs += 1
        for _ in range(100):
            u = rng.getrandbits(rng.choice([32,64,127,256,1024,2048]))
            v = rng.randrange(u+1)
            extended_l(u,v,b,p,counts); pairs += 1
        W=b**p
        for u,v in [(W+1,W),(W,W),(W*W-1,W),(W*W,W),(W**3-1,W**3-2)]:
            extended_l(u,v,b,p,counts); pairs += 1
    trace=[];answer=extended_l(27182818,10000000,10,4,counts,trace)
    assert trace[0]['quotients'] == [2,1,2,1,1]
    assert trace[0]['matrix'] == [-4,11,7,-19]
    assert trace[0]['output'] == [1268728,279726]
    counterexample=[];extended_l(10001,10000,10,4,trace=counterexample)
    assert not counterexample[0]['quotients']
    assert counterexample[0]['output'] == [10000,1]
    return dict(input_pairs=pairs+2,configs=configs,counts=counts,
                book_example=trace,bezout=answer,fallback_quotient_one=counterexample)


def inverses():
    count=0;newton=0;rng=random.Random(45217)
    for m in range(1,100):
        for v in range(1,100):
            if gcd(v,m)!=1: continue
            if v>=m: x=extended_l(v,m,10,2)[0]
            else: x=extended_l(m,v,10,2)[1]
            assert (v*x-1)%m==0
            for u in [1,2,m,m+1,177]:
                w=u*x%m
                assert 0<=w<m and (v*w-u)%m==0
                assert w==u*pow(v,-1,m)%m
                count+=1
    for e in range(1,10):
        M=1<<e
        for v in range(1,M,2):
            u=pow(v,-1,M)
            for shift in [0,-3,2]:
                us=u+shift*M;w=(us*v-1)//M
                a=(2*us-v*us*us)%(M*M)
                c=us+M*((-us*w)%M)
                assert a==c%(M*M)==pow(v,-1,M*M)
                newton+=1
    for _ in range(100):
        e=rng.randrange(10,1025);M=1<<e;v=rng.randrange(-M,M)|1
        u=pow(v,-1,M);w=(u*v-1)//M
        assert (2*u-v*u*u)%(M*M)==(u+M*((-u*w)%M))%(M*M)==pow(v,-1,M*M)
        newton+=1
    assert (1+4*((-3*2)%4))*3%16==11
    assert (3+4*((-3*2)%4))*3%16==1
    return dict(modular_divisions=count,newton_cases=newton,
                known_2001_erratum=dict(e=2,u=3,v=3,old_value=9,old_product_mod16=11,correct_value=11))


def solve_integer(A, rhs):
    """The printed changes of variables, plus explicit handling of zero rows."""
    n=len(A[0]);A=[list(r) for r in A];rhs=list(rhs)
    offset=[0]*n;T=[[int(i==j) for j in range(n)] for i in range(n)]
    chart=[];steps=0
    while A:
        clean=[i for i,row in enumerate(A) if any(row)]
        if any(rhs[i] for i,row in enumerate(A) if not any(row)):
            return None,chart,steps
        rhs=[rhs[i] for i in clean];A=[A[i] for i in clean]
        if not A: break
        c,i,j=min((abs(v),i,j) for i,row in enumerate(A) for j,v in enumerate(row) if v)
        if A[i][j]<0: A[i]=[-v for v in A[i]];rhs[i]=-rhs[i]
        if all(v%c==0 for v in A[i]):
            if rhs[i]%c: return None,chart,steps
            row=[v//c for v in A[i]];d=rhs[i]//c
            assert row[j]==1
            remaining=[k for k in range(len(row)) if k!=j]
            newA=[];newrhs=[]
            for l,a in enumerate(A):
                if l==i: continue
                newA.append([a[k]-a[j]*row[k] for k in remaining])
                newrhs.append(rhs[l]-a[j]*d)
            offset=[o+t[j]*d for o,t in zip(offset,T)]
            T=[[t[k]-t[j]*row[k] for k in remaining] for t in T]
            chart.append(('delete',j))
            A,rhs=newA,newrhs
        else:
            q=[v//c for v in A[i]];q[j]=0
            A=[[v-a[j]*q[k] for k,v in enumerate(a)] for a in A]
            T=[[v-t[j]*q[k] for k,v in enumerate(t)] for t in T]
            chart.append(('shear',j,q))
            assert min(abs(v) for a in A for v in a if v)<c
        steps+=1
    return (offset,T),chart,steps


def equations():
    rng=random.Random(45219);cases=[];totals=Counter()
    for entries in product(range(-1,2),repeat=4):
        for rhs in product(range(-2,3),repeat=2):
            cases.append(([entries[:2],entries[2:]],rhs))
    for _ in range(400):
        n=rng.randrange(1,5);m=rng.randrange(1,5)
        A=[[rng.randrange(-8,9) for _ in range(n)] for _ in range(m)]
        if rng.randrange(2):
            x=[rng.randrange(-3,4) for _ in range(n)]
            rhs=[sum(a*z for a,z in zip(row,x)) for row in A]
        else: rhs=[rng.randrange(-10,11) for _ in range(m)]
        cases.append((A,rhs))
    cases.extend([([[3,7,11],[5,7,-5]],[1,3]),([[3,7,11],[5,7,-5]],[1,-3]),
                  ([[10,3,3,8],[6,-7,0,-5]],[1,2])])
    for A,rhs in cases:
        solution,chart,steps=solve_integer(A,rhs)
        totals['systems']+=1;totals['transformations']+=steps
        if solution is None: totals['inconsistent']+=1
        else:
            offset,T=solution
            for row,d in zip(A,rhs):
                assert sum(a*z for a,z in zip(row,offset))==d
                for k in range(len(T[0])):
                    assert sum(a*t[k] for a,t in zip(row,T))==0
        for x in product(range(-2,3),repeat=len(A[0])):
            totals['bounded_vectors']+=1
            if any(sum(a*z for a,z in zip(row,x))!=d for row,d in zip(A,rhs)):continue
            totals['bounded_solutions']+=1
            assert solution is not None
            z=list(x)
            for op in chart:
                if op[0]=='delete': del z[op[1]]
                else:
                    _,j,q=op;z[j]+=sum(a*t for a,t in zip(q,z))
            recovered=[o+sum(a*t for a,t in zip(row,z)) for o,row in zip(offset,T)]
            assert recovered==list(x)
    assert solve_integer([[3,7,11],[5,7,-5]],[1,3])[0] is None
    # Independent substitution into the displayed affine families.
    for z in [-10**30,-3,-1,0,1,17,10**30]:
        x,y=8*z-2,1-5*z
        assert 3*x+7*y+11*z==1 and 5*x+7*y-5*z==-3
    for t1,t3 in product([-10**30,-2,-1,0,1,2,10**30],repeat=2):
        w,x,y,z=17-5*t1-14*t3,20-5*t1-17*t3,-55+19*t1+45*t3,-8+t1+7*t3
        assert 10*w+3*x+3*y+8*z==1 and 6*w-7*x-5*z==2
        assert 3*w+x+y+2*z==t1 and 15*w+7*x+5*y+15*z==t3
    totals['displayed_family_points']=56
    return dict(totals)


if __name__=='__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('lehmer',lehmer),('inverses',inverses),('equations',equations)]:
        if name in data: continue
        start=time.monotonic();result=fn()
        data[name]=dict(status='passed',seconds=time.monotonic()-start,result=result)
        OUT.write_text(json.dumps(data,indent=2)+'\n')
        print(name,'passed',round(data[name]['seconds'],3),flush=True)
