"""Exact geometric checks supporting the general proofs of DLX124--125."""
from collections import Counter
from datetime import datetime,timezone
from fractions import Fraction as F
from itertools import permutations,product
import check_macmahon as g
from macmahon126 import OUT,save,sha


def endpoints(e):
    kind,x,y=e
    if kind=='-':return frozenset([(x,y),(x+1,y)])
    if kind=='/':return frozenset([(x,y),(x,y+1)])
    assert kind=='\\';return frozenset([(x+1,y),(x,y+1)])


def bary(t):
    x,y,z=t;return (x,y,2-z-x-y)


def face(q):
    z=2-sum(q);assert z in (0,1)
    return q[0],q[1],z


def odd(t):
    x,y,z=t;return (2*x-1,2*y-1,3-2*x-2*y-2*z)


def vertex(q):
    assert sum(q)==0 and all(x%2==0 for x in q)
    return 1+q[0]//2,1+q[1]//2


def dist2(a,b):
    x,y=a[0]-b[0],a[1]-b[1]
    return x*x+x*y+y*y


def directed(q):
    s=sum(q);assert s in (-1,1)
    j,= [i for i,x in enumerate(q) if x%2]
    v=list(q);v[j]-=s;w=v.copy()
    w[(j+1)%3]+=2*s;w[(j+2)%3]-=2*s
    return tuple(v),tuple(w)


def main():
    edge_checks=0;group_checks=0;parity_checks=0
    for x,y,z in product(range(-4,5),range(-4,5),range(2)):
        t=(x,y,z);v=g.vertices(t);assert face(bary(t))==t
        assert all(dist2(a,b)==1 for a,b in [(v[0],v[1]),(v[1],v[2]),(v[2],v[0])])
        geometric={frozenset([a,b]) for a,b in [(v[0],v[1]),(v[1],v[2]),(v[2],v[0])]}
        assert {endpoints(e) for e in g.edges(t)}==geometric
        adjacent=[(x,y+1,0),(x+1,y,0),(x,y,0)] if z else [(x,y-1,1),(x-1,y,1),(x,y,1)]
        for e,u in zip(g.edges(t),adjacent):
            assert set(g.vertices(u))&set(v)==set(endpoints(e))
            q=tuple(F(a+b,2) for a,b in zip(odd(t),odd(u)))
            assert all(a.denominator==1 for a in q) and sum(q)==0
            assert sum(int(a)%2==0 for a in q)==1
            # The edge point is the average of the two vertex positions too.
            midpoint=tuple(sum(F(p[i],2) for p in endpoints(e)) for i in (0,1))
            assert midpoint==(1+q[0]/2,1+q[1]/2)
            edge_checks+=1
        for perm,flip in product(permutations(range(3)),range(2)):
            q=tuple(bary(t)[i] for i in perm)
            if flip:q=tuple(1-a for a in q)
            transformed=face(q)
            vv=[]
            for a,b in v:
                raw=(a-1,b-1,2-a-b);raw=tuple(raw[i] for i in perm)
                if flip:raw=tuple(-s for s in raw)
                vv.append((1+raw[0],1+raw[1]))
            assert set(vv)==set(g.vertices(transformed));group_checks+=1
        assert all(a%2 for a in odd(t)) and abs(sum(odd(t)))==1
    for a,b in product(range(-4,5),repeat=2):
        v=(2*a,2*b,-2*a-2*b);neighbors=set()
        for j,s in product(range(3),(-1,1)):
            q=list(v);q[j]+=s;vv,w=directed(q)
            assert vv==v and dist2(vertex(v),vertex(w))==1
            reverse=list(w);reverse[j]-=s
            assert directed(reverse)==(w,v)
            neighbors.add(w);parity_checks+=1
        assert len(neighbors)==6
    scaling=[]
    for k in range(1,10):
        for x,y,z in product(range(-3,4),range(-3,4),range(2)):
            cells=[]
            for p,q,u in product(range(k),range(k),range(2)):
                candidate=(k*x+p,k*y+q,u)
                points=g.vertices(candidate)
                low=all(a+b<=k*(x+y+1) for a,b in points)
                high=all(a+b>=k*(x+y+1) for a,b in points)
                predicted=(p+q<k-u) if z==0 else (p+q>=k-u)
                assert predicted==(low if z==0 else high)
                if predicted:cells.append(candidate)
            counts=Counter(t[2] for t in cells)
            assert len(cells)==k*k
            assert counts[z]==k*(k+1)//2 and counts[1-z]==k*(k-1)//2
            scaling.append(dict(k=k,triangle=[x,y,z],counts=dict(counts)))
    q=tuple(odd((0,0,0)));assert q==(-1,-1,3)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),script_sha256=sha(__file__),
                faces=162,edge_adjacency_and_midpoint_checks=edge_checks,
                spatial_symmetry_checks=group_checks,directed_edge_checks=parity_checks,
                scaling_cases=scaling,known_error='F063: second coordinate kx must be ky in both orientations; k=1,(x,y)=(0,1) is a counterexample.',
                scope='Exact finite verification of the formulas, including negative coordinates and all12 symmetries. General affine, parity and subdivision proofs are separately written in TRIANGLES124_126_NOTES.md.')
    save(OUT/'coordinates-checked.json',result)
    print('PASS:',edge_checks,'edges,',group_checks,'isometries,',parity_checks,'directed edges,',len(scaling),'scalings')


if __name__=='__main__':main()
