"""Exact checks for TAOCP 3.3.2-26/27, independent moment and geometric models."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from math import comb, factorial, sqrt
from pathlib import Path
import json
import sys
import sympy as S

ROOT=Path(__file__).resolve().parent
DEST=ROOT/'results/spacings.json'


def survival(n,k,s):
    return sum(Q(comb(n,l)*comb(n-l-1,k-l-1)*(-1)**(k-l-1))*
               max(0,1-(n-l)*s)**(n-1) for l in range(k))


def moments():
    rows=[];cdf_checks=0
    for n in range(2,31):
        for k in range(1,n+1):
            h=sum(Q(1,j) for j in range(n-k+1,n+1))
            h2=sum(Q(1,j*j) for j in range(n-k+1,n+1))
            integrated=[]
            for r in (1,2):
                total=sum(Q(comb(n,l)*comb(n-l-1,k-l-1)*(-1)**(k-l-1),(n-l)**r)
                          for l in range(k))
                integrated.append(total*Q(factorial(r)*factorial(n-1),factorial(n+r-1)))
            assert integrated==[h/n,(h*h+h2)/(n*(n+1))]
            assert integrated[1]-integrated[0]**2==(h2-h*h/n)/(n*(n+1))
            # Separate inclusion-exclusion count for exactly j small spacings.
            for s in (Q(0),Q(1,2*n),Q(1,n),Q(1,2),Q(1)):
                g=[sum(Q(comb(n,j)*comb(j,l)*(-1)**(j-l))*
                       max(0,1-(n-l)*s)**(n-1) for l in range(j+1))
                   for j in range(n+1)]
                assert all(x>=0 for x in g) and sum(g)==1
                assert sum(g[:k])==survival(n,k,s)
                cdf_checks+=1
            rows.append(dict(n=n,k=k,mean=str(integrated[0]),second=str(integrated[1])))
    # Printed G1+...+G(k-1) omits G0. Smallest nonempty example k=2.
    assert survival(2,2,Q(1,4))==1
    assert survival(2,1,Q(1,4))==Q(1,2)
    return dict(moment_pairs=len(rows),cdf_checks=cdf_checks,
                missing_G0=dict(n=2,k=2,s='1/4',lhs='1',printed_rhs='1/2'),rows=rows)


def transform(v):
    w=sorted(v);n=len(v)
    return tuple((n-j)*(w[j]-(w[j-1] if j else 0)) for j in range(n))


def inverse(v,p):
    n=len(v);x=[Q(0)]*n;partial=Q(0)
    for j in range(n):
        partial+=v[j]/(n-j);x[p[j]]=partial
    return tuple(x)


def inverse_geometry():
    rows=[]
    for n in range(2,17):
        vertices=[tuple(Q(i==j) for i in range(n)) for j in range(n)]
        columns=[inverse(v,tuple(range(n))) for v in vertices]
        matrix=S.Matrix(n,n,lambda i,j:S.Rational(columns[j][i]))
        # Column sums one: full determinant equals the tangent-volume factor.
        assert abs(matrix.det())==S.Rational(1,factorial(n))
        assert all(transform(c)==v for c,v in zip(columns,vertices))
        overlaps=[sum(min(x,y) for x,y in zip(a,b)) for a,b in combinations(columns,2)]
        assert min(overlaps)==Q(1,n)
        for i,j in combinations(range(n),2):
            d2=sum((a-b)**2 for a,b in zip(columns[i],columns[j]))
            assert d2==abs(Q(1,n-i)-Q(1,n-j))
        rows.append(dict(n=n,determinant=str(matrix.det()),l1_contraction=str(1-Q(1,n))))
    return dict(dimensions=rows)


def triangle_geometry():
    n=3;perms=list(permutations(range(n)))
    vertices=[tuple(Q(i==j) for i in range(n)) for j in range(n)]
    rows=[];drawing=[]
    for depth in (1,2,3):
        edges=defaultdict(list);areas=[]
        for digits in product(range(6),repeat=depth):
            triangle=vertices
            for d in reversed(digits):triangle=[inverse(v,perms[d]) for v in triangle]
            center=tuple(sum(v[i] for v in triangle)/3 for i in range(3))
            z=center
            for d in digits:
                assert tuple(sorted(range(3),key=lambda i:z[i]))==perms[d]
                z=transform(z)
            assert z==tuple(Q(1,3) for i in range(3))
            x,y,z=triangle
            area=abs((y[0]-x[0])*(z[1]-x[1])-(z[0]-x[0])*(y[1]-x[1]))
            assert area==Q(1,6**depth);areas.append(area)
            for e in combinations(triangle,2):edges[tuple(sorted(e))].append(digits)
            if depth==2:drawing.append((digits,triangle,center))
        assert sum(areas)==1
        adj=0
        for codes in edges.values():
            assert len(codes)<=2
            if len(codes)==2:
                assert sum(x!=y for x,y in zip(*codes))==1
                adj+=1
        rows.append(dict(depth=depth,cells=6**depth,shared_edges=adj,all_areas=str(areas[0])))
    # Scientific reconstruction of the book's 36 labeled triangles.
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(8,7))
    def xy(v):return float(v[1]+v[2]/2),float(v[2])*sqrt(3)/2
    for digits,triangle,center in drawing:
        points=[xy(v) for v in triangle+[triangle[0]]]
        ax.plot(*zip(*points),color='black',linewidth=.6)
        ax.text(*xy(center),''.join(map(str,digits)),ha='center',va='center',fontsize=10)
    ax.set_aspect('equal');ax.set_axis_off();fig.tight_layout()
    fig.savefig(ROOT/'results/spacings-triangles.svg')
    fig.savefig(ROOT/'results/spacings-triangles.png',dpi=140);plt.close(fig)
    return dict(levels=rows,figure='spacings-triangles.svg')


def finite_precision():
    cases=0;maximum=[]
    for e in range(1,15):
        M=2**e;longest=0
        for k in range(M+1):
            v=(k,M-k);steps=0
            while v!=(0,M):
                v=transform(v);steps+=1
                assert steps<=e+1
            longest=max(longest,steps);cases+=1
        maximum.append(dict(bits=e,maximum_steps=longest))
    codes=[]
    for k in range(16):
        v=(Q(2*k+1,32),1-Q(2*k+1,32));code=''
        for _ in range(4):
            assert v[0]!=v[1];code+=str(int(v[0]>v[1]));v=transform(v)
        codes.append(code)
    assert codes==['0000','0001','0011','0010','0110','0111','0101','0100',
                   '1100','1101','1111','1110','1010','1011','1001','1000']
    fixed=(Q(3,8),Q(1,2),Q(1,8));assert transform(fixed)==fixed
    return dict(binary_models=cases,maximum_steps=maximum,printed_codes=codes,
                nonvertex_fixed_point_n3=list(map(str,fixed)),
                limitation='Only n=2 is asserted to converge to the vertex; n=3 need not.')


def irrational_boundary():
    a=S.sqrt(2)/4
    x=(a/3,5*a/6,1-7*a/6)
    assert all(z.is_irrational for z in x)
    assert all(S.simplify(x[j+1]-x[j])>0 for j in (0,1))
    transformed=tuple(S.simplify((3-j)*(x[j]-(x[j-1] if j else 0))) for j in range(3))
    assert transformed==(a,a,1-2*a)
    assert 0<transformed[2]<a
    return dict(original=list(map(str,x)),first_digit=0,
                transformed=list(map(str,transformed)),second_digit='undefined under strict inequalities; closures allow 4 or 5')


def main():
    out=json.loads(DEST.read_text()) if '--resume' in sys.argv and DEST.exists() else {}
    for name,fn in [('moments',moments),('inverse_geometry',inverse_geometry),
                    ('triangles',triangle_geometry),('finite_precision',finite_precision),
                    ('irrational_boundary',irrational_boundary)]:
        if name in out:continue
        print('START',name,flush=True);out[name]=fn()
        DEST.write_text(json.dumps(out,indent=2)+'\n');print('PASS',name,flush=True)
    print('ALL BLOCKS COMPLETE',flush=True)


if __name__=='__main__':main()
