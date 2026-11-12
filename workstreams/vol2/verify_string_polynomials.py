#!/usr/bin/env python3
"""Exact noncommutative division, eight Cohn invariants, and matrix certificates."""
from fractions import Fraction as F
from pathlib import Path
from math import gcd
import argparse
import json
import random
import time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/string-polynomials.json'
ONE={'':F(1)}


def clean(a):return {w:F(c) for w,c in a.items() if c}
def degree(a):return max(map(len,a),default=float('-inf'))
def scale(a,c):return clean({w:v*c for w,v in a.items()})
def add(a,b):
    r=dict(a)
    for w,c in b.items():r[w]=r.get(w,0)+c
    return clean(r)
def sub(a,b):return add(a,scale(b,-1))
def mul(a,b):
    r={}
    for u,c in a.items():
        for v,d in b.items():r[u+v]=r.get(u+v,0)+c*d
    return clean(r)
def power(a,n):
    r=ONE
    for _ in range(n):r=mul(r,a)
    return r
def parse(s):
    r={}
    for t in s.replace('-','+-').split('+'):
        if not t:continue
        c=-1 if t.startswith('-') else 1;t=t.lstrip('-')
        i=0
        while i<len(t) and t[i].isdigit():i+=1
        if i:c*=int(t[:i])
        w=t[i:];r[w]=r.get(w,0)+c
    return clean(r)
def serial(a):return {w:str(c) for w,c in sorted(a.items(),key=lambda t:(-len(t[0]),t[0]))}
def randpoly(rng,deg,homogeneous=False,terms=3):
    a={}
    for i in range(terms):
        n=deg if homogeneous or i==0 else rng.randrange(deg+1)
        w=''.join(rng.choice('ab') for _ in range(n));a[w]=rng.choice([-2,-1,1,2])
    return clean(a)


def weak_reduce(U,V,L1,L2):
    assert degree(U)>=degree(V) and degree(sub(mul(L1,U),mul(L2,V)))<degree(mul(L1,U))
    steps=0
    while degree(L1)>0:
        w=max(L1,key=len);a=w[0]
        L1={w[1:]:c for w,c in L1.items() if w.startswith(a)}
        L2={w[1:]:c for w,c in L2.items() if w.startswith(a)}
        assert degree(sub(mul(L1,U),mul(L2,V)))<degree(mul(L1,U))
        steps+=1
    Q=scale(L2,1/L1[''])
    assert degree(sub(U,mul(Q,V)))<degree(U)
    return Q,steps


def cohn_divide(U,V,L1,L2):
    assert V and L1 and degree(sub(mul(L1,U),mul(L2,V)))<degree(V)
    Q={};R=U;steps=0
    while degree(R)>=degree(V):
        q,s=weak_reduce(R,V,L1,sub(L2,mul(L1,Q)));steps+=s
        Q=add(Q,q);R=sub(R,mul(q,V))
    assert U==add(mul(Q,V),R)
    return Q,R,steps


def suffix_divide(U,V):
    """Independent top-homogeneous coefficient oracle; can reject inadmissible pairs."""
    n=int(degree(V));word=next(w for w in V if len(w)==n);c=V[word]
    R=U;Q={}
    while degree(R)>=n:
        m=int(degree(R));t=m-n
        q={w[:t]:v/c for w,v in R.items() if len(w)==m and w[t:]==word}
        r=sub(R,mul(q,V))
        if degree(r)>=m:raise ValueError('No quotient with sufficiently small remainder')
        Q=add(Q,q);R=r
    return Q,R


def division_block():
    rng=random.Random(2026110411);steps=0;homogeneous=0
    for i in range(160):
        n=rng.randrange(2,6);V=randpoly(rng,n);Q=randpoly(rng,rng.randrange(0,4))
        L1=randpoly(rng,rng.randrange(1,n));R=randpoly(rng,n-int(degree(L1))-1)
        if i%3==0:R={}
        U=add(mul(Q,V),R);L2=mul(L1,Q)
        q,r,s=cohn_divide(U,V,L1,L2);steps+=s
        assert (q,r)==(Q,R)==suffix_divide(U,V)
    for i in range(80):
        A=randpoly(rng,rng.randrange(0,4),True)
        H=randpoly(rng,rng.randrange(0,4),True)
        B=randpoly(rng,rng.randrange(0,4),True)
        U1,U2,V1,V2=A,mul(A,H),mul(H,B),B
        q,r,s=cohn_divide(V1,V2,U1,U2)
        assert q==H and not r;homogeneous+=1;steps+=s
    a=parse('a');b=parse('b')
    try:suffix_divide(a,b)
    except ValueError:pass
    else:raise AssertionError('a cannot be right-divided by b with constant remainder')
    assert sub(mul({},a),mul({},b))=={}
    return {'division_cases':160,'homogeneous_factor_cases':homogeneous,
            'prefix_descent_steps':steps,'zero_witness_counterexample':True}


def homogeneous_root(U,V):
    assert U and V and mul(U,V)==mul(V,U)
    while True:
        if degree(U)<degree(V):U,V=V,U
        if degree(V)==0:return U
        Q,R=suffix_divide(U,V)
        assert not R and mul(Q,V)==mul(V,Q)
        U,V=V,Q


def homogeneous_block():
    rng=random.Random(2026110412)
    for i in range(80):
        W=randpoly(rng,rng.randrange(1,3),True,2)
        m,n=rng.randrange(1,5),rng.randrange(0,5)
        U=scale(power(W,m),rng.choice([-2,1,3]));V=scale(power(W,n),rng.choice([-3,1,2]))
        root=homogeneous_root(U,V);g=gcd(m,n)
        assert degree(root)==degree(W)*g
        target=power(W,g);word=next(iter(target));assert root==scale(target,root[word]/target[word])
    for k in range(1,11):
        W={'a'*k:F(1)}
        assert power(W,0)==ONE and degree(W)==k
    return {'commuting_pairs':80,'constant_input_unbounded_degree_witnesses':10}


def pmul(A,B):
    return [[add(mul(A[i][0],B[0][j]),mul(A[i][1],B[1][j])) for j in range(2)] for i in range(2)]


def extended(V1,V2,U1,U2):
    w1,w2,wp1,wp2=ONE,{},{},ONE
    z1,z2,zp1,zp2=ONE,{},{},ONE
    u1,u2,v1,v2=U1,U2,V1,V2;n=0;prefix=0
    while True:
        sg=(-1)**n
        assert add(mul(U1,w1),mul(U2,w2))==u1
        assert add(mul(U1,wp1),mul(U2,wp2))==u2
        assert add(mul(z1,V1),mul(z2,V2))==v1
        assert add(mul(zp1,V1),mul(zp2,V2))==v2
        assert sub(mul(u1,z1),mul(u2,zp1))==scale(U1,sg)
        assert sub(mul(u2,zp2),mul(u1,z2))==scale(U2,sg)
        assert sub(mul(w1,v1),mul(wp1,v2))==scale(V1,sg)
        assert sub(mul(wp2,v2),mul(w2,v1))==scale(V2,sg)
        assert mul(u1,v1)==mul(u2,v2)
        assert bool(u1)==bool(v2)
        if not v2:break
        Q,R,s=cohn_divide(v1,v2,u1,u2);prefix+=s
        assert (Q,R)==suffix_divide(v1,v2)
        w1,w2,wp1,wp2=sub(wp1,mul(w1,Q)),sub(wp2,mul(w2,Q)),w1,w2
        z1,z2,zp1,zp2=zp1,zp2,sub(z1,mul(Q,zp1)),sub(z2,mul(Q,zp2))
        u1,u2,v1,v2=sub(u2,mul(u1,Q)),u1,v2,R;n+=1
    L=mul(zp1,V1)
    assert L==scale(mul(zp2,V2),-1)
    return v1,L,n,prefix,(zp1,zp2)


def extended_block():
    U1=parse('abbbab+abbab-bbab+ab-1');V1=parse('babab+abab+ab-b')
    U2=parse('abb+ab-b');V2=parse('babbabab+bababab+babab+abab-babb-1')
    printed=parse('abbbabbabab+abbabbabab+abbbababab+abbababab-bbabbabab+abbbabab-bbababab+2abbabab-abbbabb+ababab-abbabb-bbabab-babab+bbabb-abb-ab+b')
    assert mul(U1,V1)==mul(U2,V2)==printed
    G,L,n,s,syzygy=extended(V1,V2,U1,U2)
    assert G==parse('ab+1')
    assert L==printed or L==scale(printed,-1)
    sample={'gcrd':serial(G),'lclm':serial(L),'iterations':n,'printed_product_terms':len(printed)}
    rng=random.Random(2026110413);iterations=n;prefix=s
    for i in range(90):
        G=randpoly(rng,rng.randrange(0,3),terms=2);H=[[ONE,{}],[{},ONE]];J=[[ONE,{}],[{},ONE]]
        for _ in range(rng.randrange(1,5)):
            Q=randpoly(rng,rng.randrange(1,3),terms=2)
            H=pmul(H,[[Q,ONE],[ONE,{}]])
            J=pmul([[{},ONE],[ONE,scale(Q,-1)]],J)
        assert pmul(H,J)==[[ONE,{}],[{},ONE]]
        V1,V2=mul(H[0][0],G),mul(H[1][0],G)
        T=randpoly(rng,rng.randrange(0,3),terms=2)
        U1,U2=mul(T,J[1][0]),scale(mul(T,J[1][1]),-1)
        g,l,n,s,_=extended(V1,V2,U1,U2);assert g==G
        iterations+=n;prefix+=s
    for V1,V2,U1,U2 in [(parse('a+b'),{}, {},ONE),({},parse('a+b'),ONE,{})]:
        g,l,n,s,_=extended(V1,V2,U1,U2);assert g==parse('a+b') and not l
        iterations+=n;prefix+=s
    a,b,c=parse('a'),parse('b'),parse('c')
    lhs=mul(add(add(mul(mul(a,b),c),a),c),add(ONE,mul(b,a)))
    rhs=mul(add(mul(a,b),ONE),add(add(mul(mul(c,b),a),a),c))
    assert lhs==rhs
    M=[[ONE,{}],[{},ONE]]
    for x in [a,b,c]:M=pmul(M,[[x,ONE],[ONE,{}]])
    for x in [c,b,a]:M=pmul(M,[[{},ONE],[ONE,scale(x,-1)]])
    assert M==[[ONE,{}],[{},ONE]]
    return {'book_example':sample,'constructed_pairs':90,'zero_input_pairs':2,
            'iterations':iterations,'invariant_states':iterations+93,
            'prefix_descent_steps':prefix,'noncommutative_matrix_identity':True}


def mmul(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]


def triangular(C):
    m,n=len(C),len(C[0]);T=[r[:] for r in C];U=ident(m);V=ident(m);steps=0
    for j in range(min(m,n)):
        while any(T[i][j] for i in range(j+1,m)):
            k=min((i for i in range(j,m) if T[i][j]),key=lambda i:abs(T[i][j]))
            T[j],T[k]=T[k],T[j];V[j],V[k]=V[k],V[j]
            for row in U:row[j],row[k]=row[k],row[j]
            for i in range(j+1,m):
                q=T[i][j]//T[j][j]
                T[i]=[a-q*b for a,b in zip(T[i],T[j])]
                V[i]=[a-q*b for a,b in zip(V[i],V[j])]
                for row in U:row[j]+=q*row[i]
            assert mmul(U,V)==ident(m) and mmul(V,C)==T
            steps+=1
    assert all(T[i][j]==0 for i in range(m) for j in range(n) if i>j)
    return U,V,T,steps


def matrix_block():
    rng=random.Random(2026110414);steps=0;singular=0
    for case in range(240):
        n=case%5+1;C=[[rng.randrange(-10,11) for _ in range(n)] for _ in range(2*n)]
        if case%5==0:C=[[0]*n for _ in range(2*n)]
        elif case%5==1:
            for r in C:r[0]=0
        U,V,T,s=triangular(C);steps+=s
        R=[r[:n] for r in U];D=T[:n];Z=V[:n]
        assert mmul(R,D)==C and mmul(Z,C)==D
        singular+=any(not any(r) for r in D)
    A=[[1,2],[3,4]];B=[[4,3],[2,1]];D=[[1,2],[0,-1]]
    P=[[1,0],[3,2]];Q=[[4,5],[2,3]];X=[[1,0],[2,-2]];Y=[[0,0],[1,0]]
    assert mmul(P,D)==A and mmul(Q,D)==B
    XA,YB=mmul(X,A),mmul(Y,B)
    assert [[a+b for a,b in zip(x,y)] for x,y in zip(XA,YB)]==D
    return {'matrix_pairs':240,'singular_or_zero_cases':singular,'row_passes':steps,'book_certificates':True}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'blocks':{}}
    for name,fn in [('division',division_block),('homogeneous',homogeneous_block),('extended',extended_block),('matrices',matrix_block)]:
        if name in data['blocks']:print('REUSE',name,flush=True);continue
        start=time.perf_counter();r=fn();r['seconds']=time.perf_counter()-start;data['blocks'][name]=r
        OUT.write_text(json.dumps(data,indent=2)+'\n');print('PASS',name,r,flush=True)
    data['status']='passed';OUT.write_text(json.dumps(data,indent=2)+'\n')


if __name__=='__main__':main()
