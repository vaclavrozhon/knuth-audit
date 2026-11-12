"""Finite checks accompanying the general cell-center/parity proof of DLX145."""
from collections import Counter
from datetime import datetime,timezone
from itertools import product
from pathlib import Path
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent


def vertex_set(point):
    return frozenset(product(*[([x//2] if x%2==0 else [x//2,x//2+1]) for x in point]))


def center(vertices):
    return tuple(sum(p[j] for p in vertices)*2//len(vertices) for j in range(3))


def main():
    cases=[];objects=midpoint_checks=0
    for l,m,n in product(range(5),repeat=3):
        points=list(product(range(2*l+1),range(2*m+1),range(2*n+1)))
        geometries={};counts=Counter()
        for point in points:
            geometry=vertex_set(point);dim=sum(x%2 for x in point)
            assert len(geometry)==2**dim and center(geometry)==point
            assert geometry not in geometries;geometries[geometry]=point;counts[dim]+=1
            # Opposite boundary elements average to the higher-dimensional object.
            for axis in range(3):
                if point[axis]%2:
                    a=list(point);b=list(point);a[axis]-=1;b[axis]+=1
                    assert vertex_set(a)|vertex_set(b)==geometry
                    assert tuple((x+y)//2 for x,y in zip(a,b))==point
                    midpoint_checks+=1
                elif 0<point[axis]<2*[l,m,n][axis]:
                    # Parallel adjacent elements meet in the lower-dimensional object.
                    a=list(point);b=list(point);a[axis]-=1;b[axis]+=1
                    assert vertex_set(a)&vertex_set(b)==geometry
                    midpoint_checks+=1
        expected=[(l+1)*(m+1)*(n+1),l*(m+1)*(n+1)+(l+1)*m*(n+1)+(l+1)*(m+1)*n,
                  l*m*(n+1)+l*(m+1)*n+(l+1)*m*n,l*m*n]
        assert [counts[i] for i in range(4)]==expected
        assert sum(expected)==(2*l+1)*(2*m+1)*(2*n+1)
        cases.append(dict(dimensions=[l,m,n],counts=expected));objects+=len(points)
    out=ROOT/'results/coordinates145';out.mkdir(exist_ok=True)
    save(out/'checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
        grids=125,objects=objects,midpoint_checks=midpoint_checks,all_counts_and_bijections_valid=True,
        general_proof='Each axis independently chooses a vertex2i or interval2i+1. The product is a cell of dimension equal to the number of odd coordinates; reverse by endpoints.',
        examples=dict(edge=[0,1,0],face=[1,0,1],cell=[1,1,1]),cases=cases))
    print('PASS145: general parity/product proof;',len(cases),'grids,',objects,'objects,',midpoint_checks,'midpoint identities including degenerate grids.')


if __name__=='__main__':main()
