"""Convex polygons in the triangular lattice: exact boundary and simplex models."""
from fractions import Fraction
from itertools import combinations
from math import isqrt
from pathlib import Path
from puzzle_xcc import save, sha
import vertices140 as triangles

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/polygons143'
DIRECTIONS=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
SIX24=((7,5,0,0),(5,1,0,0),(12,12,1,0),(6,6,2,0),(2,2,2,2),(4,4,3,0))
BOOK_SIMPLEX=((8,6,8,2),(7,4,7,3),(5,5,5,4))


def boundary(parameters):
    a,b,c,d=parameters
    assert a>=b>=c>=d>=0
    return a,d,a-b+c,b,a-b+d,c


def area(parameters):
    a,b,c,d=parameters
    return (a+c+d)**2-b*b-c*c-d*d


def path_vertices(lengths):
    x=y=0;points=[(x,y)]
    for length,(dx,dy) in zip(lengths,DIRECTIONS):
        x+=length*dx;y+=length*dy;points.append((x,y))
    assert points[-1]==points[0]
    return points


def shoelace(lengths):
    points=path_vertices(lengths)
    return sum(x*v-y*u for (x,y),(u,v) in zip(points,points[1:]))


def orbit(lengths):
    lengths=tuple(lengths);reflection=lengths[:1]+lengths[:0:-1]
    return {w[i:]+w[:i] for w in [lengths,reflection] for i in range(6)}


def canonical_parameters(lengths):
    choices={tuple(w[i] for i in [0,3,5,1]) for w in orbit(lengths) if w[0]>=w[3]>=w[5]>=w[1]}
    assert len(choices)==1
    params=next(iter(choices));assert boundary(params) in orbit(lengths)
    return params


def divisors_table(limit):
    result=[[] for _ in range(limit+1)]
    for q in range(1,isqrt(limit)+1):
        for x in range(q*q,limit+1,q):
            result[x].append(q)
    return result


def book_algorithm(n,corrected=True,divisors=None):
    assert n>=1
    answers=[]
    for c in range(isqrt(n//2)+1):
        for d in range(c+1):
            if 2*c*(c+2*d)>n:break
            x=n+c*c+d*d
            if x%4==2:continue
            candidates=divisors[x] if divisors is not None else [q for q in range(1,isqrt(x)+1) if x%q==0]
            for q in candidates:
                other=x//q
                if q%2 != (other if corrected else x)%2:continue
                a=Fraction(other+q,2)-c-d;b=Fraction(other-q,2)
                if a>=b>=c:
                    if corrected:
                        assert a.denominator==b.denominator==1
                        answers.append((int(a),int(b),c,d))
                    else:
                        answers.append((a,b,c,d))
    assert len(answers)==len(set(answers))
    return answers


def simplex_parameters(parameters):
    a,b,c,d=parameters
    return a+c+d,a+c,a+d,a-b+c+d


def simplex_graph(parameters):
    n,a,b,c=parameters
    vertices={(x,y,n-x-y) for x in range(a+1) for y in range(b+1) if 0<=n-x-y<=c}
    edges={tuple(sorted((u,v))) for u,v in combinations(vertices,2) if max(abs(i-j) for i,j in zip(u,v))==1}
    cells=[]
    projected={(x,y) for x,y,z in vertices}
    for x in range(a+1):
        for y in range(b+1):
            for turn in [0,1]:
                if set(triangles.vertices((x,y,turn)))<=projected:cells.append((x,y,turn))
    return dict(vertices=sorted(vertices),edges=sorted(edges),cells=tuple(sorted(cells)))


def cells_boundary(cells):
    edges={}
    for t in cells:
        vv=triangles.vertices(t)
        for a,b in zip(vv,vv[1:]+vv[:1]):
            if (b,a) in edges:del edges[b,a]
            else:
                assert (a,b) not in edges;edges[a,b]=True
    counts=[0]*6
    for a,b in edges:
        d=b[0]-a[0],b[1]-a[1]
        counts[DIRECTIONS.index(d)]+=1
    return tuple(counts)
