"""Independent exact finite and continuous models for TAOCP2 3.3.3-18–28.

Each block checkpoints separately; --resume never repeats a finished block.
"""
import argparse
from fractions import Fraction as Q
import itertools
import json
from math import gcd, floor, ceil, comb, factorial
from pathlib import Path
import time

from verify_dedekind import psi, sigma, sigma_real, tableau

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/theoretical-tests.json'


def partial_sums():
    count=0
    for h in range(1,16):
        for k in range(1,16):
            d=gcd(h,k)
            for c in (Q(-5,3),Q(0),Q(1),Q(7,2),Q(17)):
                for z in sorted({0,1,k-1,k,k+1,2*k+3}):
                    direct=sum(psi((h*j+c)/k) for j in range(z))
                    val=Q(z*d,k)*psi(c/d)+(sigma_real(h,k,h*z+c)-sigma_real(h,k,c))/12+psi(c/k)/2-psi((h*z+c)/k)/2
                    assert direct==val,(h,k,c,z,direct,val)
                    weights=sum((j//k-(j-z)//k)*psi((h*j+c)/k) for j in range(k))
                    assert weights==direct
                    count+=1
    return dict(cases=count,scope='Noncoprime and real shifts, negative shifts, z beyond full periods; direct partial sum versus closed form18.')


def full_period(a,m,c):
    seen=set();x=0
    while x not in seen:
        seen.add(x);x=(a*x+c)%m
    return len(seen)==m and x==0


def rectangle_tests():
    import numpy as np
    models=rectangles=0;counter=None;max_epsilon=Q(0)
    for m in range(2,51):
        for a in range(1,m):
            if not full_period(a,m,1):continue
            # Vertical cyclic shifts preserve maximal rectangle discrepancy:
            # a wrapping interval can be complemented, changing only the sign.
            c=1
            mat=np.zeros((m+1,m+1),dtype=np.int64)
            for x in range(m):mat[x+1,(a*x+c)%m+1]=1
            mat=mat.cumsum(axis=0).cumsum(axis=1)
            best=0;best_rect=None
            for lo in range(m):
                for hi in range(lo+1,m+1):
                    v=m*(mat[hi]-mat[lo])-(hi-lo)*np.arange(m+1)
                    u,w=int(v.argmin()),int(v.argmax());delta=int(v[w]-v[u])
                    if delta>best:best=delta;best_rect=(lo,hi,min(u,w),max(u,w))
            bound=Q(sum(row['a'] for row in tableau(a,m,0)),4*m)
            if Q(best,m*m)>bound and counter is None:
                counter=dict(m=m,a=a,c=c,rectangle=best_rect,actual=str(Q(best,m*m)),bound=str(bound))
            # Exhaustive formula/error checks on small moduli, plus selected
            # boundary/interior intervals on larger ones. Integer endpoints.
            if m<=12:intervals=list(itertools.combinations(range(m+1),2))
            else:intervals=sorted({(0,m),(0,1),(0,m//2),(m//3,m),(1,m-1),best_rect[:2],best_rect[2:]})
            for lo,hi in intervals:
                for bot,top in intervals:
                    direct=Q(int(mat[hi,top]-mat[lo,top]-mat[hi,bot]+mat[lo,bot]),m)
                    main=Q((hi-lo)*(top-bot),m*m)+(sigma(a,m,c+a*lo-bot)-sigma(a,m,c+a*lo-top)+sigma(a,m,c+a*hi-top)-sigma(a,m,c+a*hi-bot))/(12*m)
                    epsilon=abs(direct-main);assert epsilon<=Q(5,2*m)
                    max_epsilon=max(max_epsilon,m*epsilon);rectangles+=1
            models+=1
    return dict(full_period_multipliers=models,rectangles=rectangles,max_m_epsilon=str(max_epsilon),printed_discrepancy_bound_counterexample=counter,scope='Exact maxima for all full-period multipliers m<=50; all c covered by vertical-translation/complement symmetry.')


def descending_triples():
    count=0;exceptions=[]
    for m in range(2,61):
        for a in range(1,m):
            if not full_period(a,m,1):continue
            ap=pow(a,-1,m);b=a-1;d=gcd(b,m)
            for c in range(1,m):
                if gcd(c,m)!=1:continue
                values=[(a*x+c)%m for x in range(m)]
                direct=Q(sum(x>values[x]>values[values[x]] for x in range(m)),m)
                xp=(-ap*c)%m;xpp=(ap*(xp-c))%m;c0=c%d
                s1=sigma(a,m,c);s2=sigma(a*a,m,a*c+c);s3=sigma(a*b,m,a*c)
                s4=sigma(1,m,0);s5=sigma(a,m,c);s6=sigma(b,m,c)
                s7=-sigma(ap-1,m,ap*c);s8=-sigma(ap*(ap-1),m,ap*ap*c)
                s9=12*sum(psi(Q(b*x+c,m))*psi(Q(a*(b*x+c),m)) for x in range(m))
                reduced=d*(sigma(a*d,m,a*c0)+12*Q(c0,m)*psi(Q(a*c0,d))-6*psi(Q(a*c0,m)))
                assert s9==reduced,(a,m,c,s9,reduced)
                result=Q(1,4)+(s1-s2+s3-s4+s5-s6+s7-s8+s9)/(12*m)+Q(d,m)*psi(Q(c,d))
                result+=(psi(Q(xp-xpp,m))-psi(Q(xp,m))+psi(Q(xpp,m))+psi(Q(a*c+c,m))-psi(Q(a*c,m))-psi(Q(c,m))-Q(1,2))/(2*m)
                if result!=direct: exceptions.append(dict(a=a,m=m,c=c,printed=str(result),actual=str(direct)))
                count+=1
    return dict(full_period_models=count,printed_formula_exceptions=exceptions,scope='Nine printed sums, special noncoprime S9 reduction, boundary corrections vs actual consecutive triples.')


def descending_intervals(a,theta,length):
    """Independent exact affine-branch clipping, with every previous descent.

    A branch stores current value A*x+B and its allowed initial-x interval.
    At a discontinuity endpoints have measure zero, so closed bounds suffice.
    """
    branches=[(Q(0),Q(1),Q(1),Q(0))]
    for step in range(length-1):
        new=[]
        for lo,hi,A,B in branches:
            base=a*B+theta;slope=a*A
            for j in range(floor(slope*lo+base),ceil(slope*hi+base)):
                left=max(lo,(j-base)/slope);right=min(hi,(j+1-base)/slope)
                ds=slope-A;db=base-j-B
                if ds>0:right=min(right,-db/ds)
                elif ds<0:left=max(left,-db/ds)
                elif db>=0:continue
                if left<right:new.append((left,right,slope,base-j))
        branches=new
    return branches


def triple_formula(a,theta):
    n=floor(a*theta)
    return Q(1,6)+Q(1,6*a)-theta/(2*a)+(Q(n)*(n+1-2*theta)/(2*(a-1))+max(Q(0),a*theta-n+theta-1))/(a*a)


def continuous_tests():
    integrals=triples=runs=rectangles=0;equalities=[]
    for a in range(2,13):
        shifts=sorted({Q(0),Q(1,2),Q(1,3),Q(1,4),Q(2,3),Q(9,10)}|{Q(j,a+1) for j in range(a+1)}|{Q(j,a) for j in range(a)})
        for theta in shifts:
            moment=Q(0)
            for j in range(a+1):
                lo=max(Q(0),(j-theta)/a);hi=min(Q(1),(j+1-theta)/a)
                if lo>=hi:continue
                moment+=Q(a,3)*(hi**3-lo**3)+(theta-j)*(hi**2-lo**2)/2
            assert 12*(moment-Q(1,4))==(1-6*theta+6*theta*theta)/a
            integrals+=1
            desc=sum(hi-lo for lo,hi,A,B in descending_intervals(a,theta,2))
            triple=sum(hi-lo for lo,hi,A,B in descending_intervals(a,theta,3))
            assert desc==Q(1,2)
            assert triple==triple_formula(a,theta),(a,theta,triple,triple_formula(a,theta))
            if triple==Q(1,6):equalities.append(dict(a=a,theta=str(theta),intervals=[[str(lo),str(hi)] for lo,hi,A,B in descending_intervals(a,theta,3)]))
            triples+=1
        for length in range(1,8):
            if a>6 and length>4:continue
            direct=sum(hi-lo for lo,hi,A,B in descending_intervals(a,Q(0),length))
            val=Q(comb(a+length-2,length),a**(length-1)*(a-1))
            assert direct==val,(a,length,direct,val);runs+=1
    # Exercise25, independent intersection of all affine preimages.
    grid=[Q(i,6) for i in range(7)]
    intervals=list(itertools.combinations(grid,2))
    for a in range(1,8):
        for theta in (Q(0),Q(1,3),Q(1,2),Q(5,7)):
            for lo,hi in intervals:
                for bot,top in intervals:
                    direct=sum(max(Q(0),min(hi,(j+top-theta)/a)-max(lo,(j+bot-theta)/a)) for j in range(-1,a+2))
                    k0=ceil(a*lo+theta-top);k1=ceil(a*hi+theta-top)
                    val=Q(k1-k0)*(top-bot)/a+max(Q(0),hi-(k1+bot-theta)/a)-max(Q(0),lo-(k0+bot-theta)/a)
                    assert direct==val,(a,theta,lo,hi,bot,top,direct,val)
                    assert abs(direct-(hi-lo)*(top-bot))<2*(top-bot)/a
                    rectangles+=1
    return dict(correlation_integrals=integrals,descending_triple_cases=triples,exact_one_sixth_cases=equalities,run_length_cases=runs,continuous_rectangles=rectangles,a1_counterexample=dict(theta='1/4',actual_descent='1/4',printed_descent='1/2'),scope='Exact rational interval clipping, not simulation; formula23 checked even at its breakpoints.')


def clip(poly,line):
    """Keep the halfplane A*x+B*y+C >= 0, with rational intersections."""
    if not poly:return []
    def value(p):return line[0]*p[0]+line[1]*p[1]+line[2]
    out=[]
    for u,v in zip(poly,poly[1:]+poly[:1]):
        fu,fv=value(u),value(v)
        if fu>=0:out.append(u)
        if (fu<0<fv) or (fv<0<fu):
            t=fu/(fu-fv);out.append(tuple(u[i]+t*(v[i]-u[i]) for i in range(2)))
    return out


def area(poly):
    return abs(sum((u[0]*v[1]-u[1]*v[0] for u,v in zip(poly,poly[1:]+poly[:1])),Q(0)))/2


def difference(v,u):return tuple(x-y for x,y in zip(v,u))


def permutation_regions(A,B,C):
    square=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
    output={''.join(str(i+1) for i in p):Q(0) for p in itertools.permutations(range(3))}
    for j in range(floor(min(C,C+A,C+B,C+A+B)),ceil(max(C,C+A,C+B,C+A+B))):
        z=(Q(A),Q(B),Q(C-j));base=clip(clip(square,z),difference((Q(0),Q(0),Q(1)),z))
        values=[(Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),z]
        for order in itertools.permutations(range(3)):
            poly=base
            for u,v in zip(order,order[1:]):poly=clip(poly,difference(values[v],values[u]))
            output[''.join(str(i+1) for i in order)]+=area(poly)
    return output


def planar_tests():
    fib=permutation_regions(1,1,0)
    assert fib=={'123':Q(1,4),'132':Q(0),'213':Q(1,4),'231':Q(0),'312':Q(1,4),'321':Q(1,4)}
    # Direct affine recurrence, stopped at its first decline. Conditional
    # density two on U0>U1; no Fibonacci expression is used to construct cells.
    tri=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1))]
    branches=[(tri,(Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)))]
    F=[0,1]
    for _ in range(21):F.append(F[-1]+F[-2])
    rows=[]
    for k in range(1,16):
        stop=Q(0);new=[]
        for poly,u,v in branches:
            for j in [0,1]:
                w=tuple(u[i]+v[i]-(j if i==2 else 0) for i in range(3))
                cell=clip(clip(poly,w),difference((Q(0),Q(0),Q(1)),w))
                stop+=2*area(clip(cell,difference(v,w)))
                cont=clip(cell,difference(w,v))
                if area(cont)>0:new.append((cont,v,w))
        expected=Q(1,2) if k==1 else Q(1,F[k-1]*F[k+1])-Q(1,F[k]*F[k+2])
        assert stop==expected,(k,stop,expected)
        branches=new
        tail=2*sum(area(p) for p,u,v in branches)
        assert tail==Q(1,F[k]*F[k+2])
        rows.append(dict(k=k,mass=str(stop),tail_after_k=str(tail),iid_mass=str(Q(2*k,factorial(k+1))-Q(2*(k+1),factorial(k+2)))))
    printed=[Q(1,2),Q(1,3),Q(1,10),Q(1,24),Q(1,65)]
    assert [Q(r['tail_after_k']) for r in rows[:5]]==printed
    assert Q(rows[1]['mass'])==Q(1,6)!=printed[1]
    alphas=sorted({Q(j,d) for d in range(1,13) for j in range(d+1)})
    for alpha in alphas:
        regions=permutation_regions(-1,2,alpha)
        straight=Q(1,4)-alpha/2+alpha*alpha/2
        others=Q(1,8)+alpha/4-alpha*alpha/4
        assert regions=={p:straight if p in ['123','321'] else others for p in regions},(alpha,regions)
        assert sum(regions.values())==1
    return dict(fibonacci_permutations={k:str(v) for k,v in fib.items()},fibonacci_runs=rows,printed_fibonacci_row=[str(x) for x in printed],table27_issue='Printed Fibonacci row gives tails P(L>k), whereas text/formula and iid row give masses P(L=k).',potency2_alpha_cases=len(alphas),scope='Exact rational polygon clipping; original three figures checked by their affine boundaries.')


def main():
    p=argparse.ArgumentParser();p.add_argument('--resume',action='store_true');args=p.parse_args()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else dict(scope='3.3.3-18–28, exact arithmetic',blocks={})
    for f in [partial_sums,rectangle_tests,descending_triples,continuous_tests,planar_tests]:
        if f.__name__ in data['blocks']:print('PRESERVED',f.__name__,flush=True);continue
        start=time.monotonic();print('START',f.__name__,flush=True)
        result=f();data['blocks'][f.__name__]=dict(result=result,elapsed_seconds=time.monotonic()-start)
        OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');print('PASS',f.__name__,flush=True)
    print('ALL BLOCKS PASSED',flush=True)


if __name__=='__main__':main()
