"""Exact finite expectations for the two displayed saddle programs.

All costs include the one-unit HLT. Distinct-entry intervals bound the saved
work on the mutually exclusive saddle events; binary expectations are exact.
"""
from fractions import Fraction as F
from math import comb
from functools import lru_cache
from itertools import product


def harmonic(n):return sum((F(1,k) for k in range(1,n+1)),F(0))


def probability_distinct(m,n):return F(m+n,comb(m+n,n))
def probability_binary(m,n):return 2-(1-F(1,2**m))**n-(1-F(1,2**n))**m


@lru_cache(None)
def integral(m,k,N):
    # Expand (1-x)^k(1-x^m)^(N-1), then integrate each monomial exactly.
    assert m>=1 and k>=0 and N>=1
    return sum((F(m*(-1)**(r+s)*comb(k,r)*comb(N-1,s),m*(s+1)+r)
                for r in range(k+1) for s in range(N)),F(0))


def distinct_intervals(m,n):
    p=probability_distinct(m,n)
    a=[F(1,comb(n+k,k)) for k in range(m)]
    d=sum(((m-t)*a[t]+(t*a[t-1] if t else 0) for t in range(m)),F(0))
    star1=2+6*m*n+7*m*harmonic(n)+m+5*d
    # W_i lies between 6n+13 and 13n+5m+1 for a complete distinct row.
    missed=F(m-1,2)*p
    interval1=(star1-(13*n+5*m+1)*missed,star1-(6*n+13)*missed)
    q=[F(1)]+[(n-j)*integral(m,j,n-j)+F(j,m)*integral(m,j-1,n-j+1)
               for j in range(1,n)]
    r=[F(1)]+[(n-j)*integral(m,j,n-j)+j*integral(m,j-1,n-j+1)
               for j in range(1,n)]
    equality=sum((integral(m,j,n-j) for j in range(n)),F(0))
    phase1=5*m*n+7*n+2*n*harmonic(m)+2*harmonic(n)-2
    star2=phase1+3+7*m*sum(q)+4*equality+p
    interval2=(star2-(7*n+6)*missed,star2-7*missed)
    return {'phase1':phase1,'column_scans':d,'row_scans':sum(q),
            'selected_row_scans':sum(r),'equality_visits':equality,
            'solution1':interval1,'solution2':interval2}


def binary_phase2(m,n):
    p=F(1,2**m);q=1-p;r=F(1,2**n);p0=1-q**n
    zero=(3+7*n)*p0+3*n*(F(1,2)-(F(1,2)-p)*q**(n-1))+n*p
    reached=[(1-r)**i-p0 for i in range(m)]
    failures=[(1-r)**(i+1)-p0 for i in range(m)]
    ones=sum((F(1,2**k)*((1-r)**i+q**(n-k)-1)
              for i in range(m) for k in range(1,n+1)),F(0))
    one=q**n+2*sum(reached)+11*ones+5*sum(failures)+(1-r)**m-p0
    return zero+one


def binary_solution2(m,n):
    p=F(1,2**m);q=1-p
    phase1=5*m*n+10*n-2*n*p+2*q*(1-q**(n-1))
    return phase1+binary_phase2(m,n)+1


def row_cost(bits):
    v=bits[-1];cost=10
    for x in reversed(bits[:-1]):
        if x>v:cost+=6
        elif x<v:cost+=13;v=x
        else:cost+=11
    return cost


def binary_solution1(m,n):
    # Rows i and columns are numbered in their respective processing orders.
    r=F(1,2**n);h=F(1,2**(m-1));q=1-h
    failure=[]
    for i in range(m):
        failure.append(sum((F(5*t+3,2**(t-(t>i+1)))
                            for t in range(1,m+1) if t!=i+1),F(0)))
    prior=[-r*sum(((1-r)**(i-1-k)*(13-F(5,2**k)) for k in range(i)),F(0))
           for i in range(m)]
    total=F(2)  # initial ENT1 and final HLT
    for bits in product((0,1),repeat=n):
        z=n-sum(bits);cost=row_cost(bits)
        if z==0:
            total+=r*sum(((1-r)**i*(cost+5*m+4) for i in range(m)),F(0))
            continue
        first=cost+sum((q**k for k in range(z)),F(0))*(failure[0]+h*(5*m+4))+q**z
        total+=r*first
        for i in range(1,m):
            weight=r*((1-r)**i+q**z-1)
            total+=weight*(cost+1)+r*z*(q**(z-1)*failure[i]+prior[i])
    return total
