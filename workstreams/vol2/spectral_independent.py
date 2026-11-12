"""Independent exact shortest-vector solver for the spectral audit.

LLL only changes an explicitly supplied integer basis. Its unimodular
transformation is checked exactly. A separate rational Gram--Schmidt sphere
enumeration then certifies the minimum; no floating-point pruning is used.
The book's spectral S implementation and its dual-coordinate box are not used.
"""
from fractions import Fraction as Q
from math import isqrt
import sympy as sp


def scalar(x,y):
    return sum(a*b for a,b in zip(x,y))


def lcg_basis(a,m,t):
    return [[m]+[0]*(t-1)]+[
        [-pow(a,j,m)]+[int(i==j) for i in range(1,t)] for j in range(1,t)]


def recurrence_basis(a,b,p,t):
    """Dual basis for x_(n+2)=a*x_(n+1)+b*x_n modulo p."""
    f,g=[1,0],[0,1]
    while len(f)<t:
        f.append((a*f[-1]+b*f[-2])%p)
        g.append((a*g[-1]+b*g[-2])%p)
    return [[p,0]+[0]*(t-2),[0,p]+[0]*(t-2)]+[
        [-f[j],-g[j]]+[int(i==j) for i in range(2,t)] for j in range(2,t)]


def gram_schmidt(B):
    t=len(B)
    star=[];norms=[];mu=[[Q(0) for _ in range(t)] for _ in range(t)]
    for i in range(t):
        v=list(map(Q,B[i]))
        for j in range(i):
            mu[i][j]=scalar(B[i],star[j])/norms[j]
            v=[x-mu[i][j]*y for x,y in zip(v,star[j])]
        star.append(v);norms.append(scalar(v,v))
        assert norms[-1]>0
    return star,norms,mu


def rational_lll(basis):
    """Small-dimensional exact LLL with full orthogonalization after changes.

    Avoids SymPy's math.floor conversion of large PythonMPQ values, which
    can round via floating point. Speed is secondary to transparent checks.
    """
    B=[row[:] for row in basis];n=len(B)
    transform=[[int(i==j) for j in range(n)] for i in range(n)]
    _,norms,mu=gram_schmidt(B)
    k=1;swaps=0;reductions=0
    while k<n:
        for j in range(k-1,-1,-1):
            z=mu[k][j]
            q=(2*z.numerator+z.denominator)//(2*z.denominator)
            if q:
                B[k]=[x-q*y for x,y in zip(B[k],B[j])]
                transform[k]=[x-q*y for x,y in zip(transform[k],transform[j])]
                _,norms,mu=gram_schmidt(B);reductions+=1
        if norms[k]>=(Q(3,4)-mu[k][k-1]**2)*norms[k-1]:
            k+=1
        else:
            B[k],B[k-1]=B[k-1],B[k]
            transform[k],transform[k-1]=transform[k-1],transform[k]
            _,norms,mu=gram_schmidt(B)
            swaps+=1;k=max(1,k-1)
    assert all(abs(mu[i][j])<=Q(1,2) for i in range(n) for j in range(i))
    assert all(norms[k]>=(Q(3,4)-mu[k][k-1]**2)*norms[k-1] for k in range(1,n))
    return sp.Matrix(B),sp.Matrix(transform),dict(swaps=swaps,reductions=reductions)


def shortest_basis(basis,node_limit=10_000_000):
    initial=sp.Matrix(basis)
    if max(abs(x).bit_length() for row in basis for x in row)>512:
        reduced,transform,reduction_stats=rational_lll(basis)
        implementation='own rational LLL; exact integer rounding'
    else:
        reduced,transform=initial.lll_transform(delta=sp.Rational(3,4))
        reduction_stats=None;implementation='SymPy LLL; transform checked exactly'
    assert abs(transform.det())==1 and transform*initial==reduced
    B=[[int(x) for x in reduced.row(i)] for i in range(reduced.rows)]
    t=len(B);star,norms,mu=gram_schmidt(B)
    for i in range(t):
        assert all(scalar(star[i],star[j])==0 for j in range(i))
        assert [star[i][k]+sum(mu[i][j]*star[j][k] for j in range(i))
                for k in range(t)]==B[i]
    best=min(scalar(row,row) for row in B)
    coords=[0]*t;vectors=[];nodes=[0]*t

    def visit(k,used):
        nonlocal best,vectors
        if used>best:return
        if k<0:
            if not any(coords):return
            v=[sum(coords[i]*B[i][j] for i in range(t)) for j in range(t)]
            n=scalar(v,v)
            assert n==used and n>0
            if n<best:best,vectors=n,[v]
            elif n==best:vectors.append(v)
            return
        center=-sum((mu[j][k]*coords[j] for j in range(k+1,t)),Q(0))
        radius_squared=(Q(best)-used)/norms[k]
        # (den*x-num)^2 <= radius_squared*den^2. The left side is integer.
        num,den=center.numerator,center.denominator
        r=isqrt(radius_squared.numerator*den*den//radius_squared.denominator)
        lo=-((-(num-r))//den);hi=(num+r)//den
        nearest=(2*num+den)//(2*den)
        # Visit nearby integers first, without allocating a huge interval.
        for delta in range(max(nearest-lo,hi-nearest)+1):
            for x in ((nearest,) if delta==0 else (nearest-delta,nearest+delta)):
                if not lo<=x<=hi:continue
                nodes[k]+=1
                if sum(nodes)>node_limit:raise RuntimeError('sphere node limit')
                coords[k]=x
                visit(k-1,used+norms[k]*(Q(x)-center)**2)
        coords[k]=0

    visit(t-1,Q(0))
    assert vectors
    vectors=sorted(vectors)
    return dict(squared=best,vectors=vectors,basis=B,
                reduction_implementation=implementation,reduction_stats=reduction_stats,
                transform=[[int(x) for x in transform.row(i)] for i in range(t)],
                gram_schmidt_squared=[str(x) for x in norms],
                visited_by_depth=nodes,method='exact LLL transform + rational sphere census')


def reduced_box_minimum(basis,scale,limit=10_000_000):
    """Book-style dual reduction + finite box, for non-LCG initial bases.

    This is deliberately separate from shortest_basis; it is used for the
    second-order example where the first-order S1--S4 do not apply.
    """
    from itertools import product
    from spectral import round_ratio,dot
    B=sp.Matrix(basis);dual=scale*B.inv().T
    assert all(x.q==1 for x in dual)
    U=[list(map(int,B.row(i))) for i in range(B.rows)]
    V=[list(map(int,dual.row(i))) for i in range(B.rows)]
    t=len(U);best=min(dot(x,x) for x in U);changes=0
    while True:
        changed=False
        for j in range(t):
            for i in range(t):
                if i==j:continue
                n=dot(V[j],V[j]);d=dot(V[i],V[j])
                if 2*abs(d)<=n:continue
                q=round_ratio(d,n);old=dot(V[i],V[i])
                V[i]=[x-q*y for x,y in zip(V[i],V[j])]
                U[j]=[x+q*y for x,y in zip(U[j],U[i])]
                assert dot(V[i],V[i])<old
                best=min(best,dot(U[j],U[j]));changed=True;changes+=1
        if not changed:break
    assert sp.Matrix(U)*sp.Matrix(V).T==scale*sp.eye(t)
    z=[isqrt(dot(v,v)*best//(scale*scale)) for v in V]
    visited=0;vectors=[]
    for x in product(*(range(-n,n+1) for n in z)):
        if not any(x):continue
        visited+=1
        if visited>limit:raise RuntimeError('dual box limit')
        v=[sum(x[i]*U[i][j] for i in range(t)) for j in range(t)]
        n=dot(v,v)
        if n<best:best,vectors=n,[v]
        elif n==best:vectors.append(v)
    assert vectors
    return dict(squared=best,vectors=sorted(vectors),U=U,V=V,z=z,
                searched=visited,reductions=changes)
