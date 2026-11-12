"""Exact checks for TAOCP 3.2.2-34--37; two proof-typography counterexamples."""
from itertools import combinations, product
from math import gcd, isqrt
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent


def primes_to(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,isqrt(p)+1))]


def factors(n):
    return [p for p in primes_to(n) if n%p==0]


def poly_power(n,a,c,p):
    # Pair (constant, x coefficient), with x^2=c*x+a.
    def mul(v,w):
        return ((v[0]*w[0]+a*v[1]*w[1])%p,
                (v[0]*w[1]+v[1]*w[0]+c*v[1]*w[1])%p)
    r,b=(1,0),(0,1)
    while n:
        if n&1:r=mul(r,b)
        b=mul(b,b);n//=2
    return r


def projective_next(x,a,c,p):
    if x is None:return c
    if x==0:return None
    return (a*pow(x,-1,p)+c)%p


def orbit(a,c,m,projective=True):
    x=0 if projective else 1
    seen={};seq=[]
    while x not in seen:
        seen[x]=len(seq);seq.append(x)
        x=projective_next(x,a,c,m) if projective else (a*pow(x,-1,m)+c)%m
    return seq,seen[x]


def matmul(v,w,m):
    return tuple(tuple(sum(v[i][k]*w[k][j] for k in range(2))%m
                       for j in range(2)) for i in range(2))


def determinant(a,p):
    a=[list(row) for row in a];det=1;n=len(a)
    for j in range(n):
        i=next((i for i in range(j,n) if a[i][j]%p),None)
        if i is None:return 0
        if i!=j:a[i],a[j]=a[j],a[i];det=-det
        pivot=a[j][j]%p;det=det*pivot%p
        inverse=pow(pivot,-1,p)
        for i in range(j+1,n):
            t=a[i][j]*inverse%p
            for k in range(j+1,n):a[i][k]=(a[i][k]-t*a[j][k])%p
    return det%p


def main():
    parameter_cases=states=matrix_checks=0;rows=[];full={}
    for p in primes_to(101):
        selected=[]
        for a,c in product(range(1,p),range(p)):
            u=poly_power(p+1,a,c,p)
            criterion=(u[0]!=0 and u[1]==0 and
                       all(poly_power((p+1)//q,a,c,p)[1] for q in factors(p+1)))
            seq,mu=orbit(a,c,p)
            assert mu==0
            assert criterion==(len(seq)==p+1)
            parameter_cases+=1;states+=len(seq)
            if criterion:
                assert all((x*x-c*x-a)%p for x in range(p))
                selected.append((a,c))
            if p<=13:
                # Matrix formula and quotient-ring formula versus direct iteration.
                q=[0,1]
                for n in range(1,p+2):q.append((c*q[n]+a*q[n-1])%p)
                t=((1,0),(0,1));M=((0,1),(a,c))
                xs=list(range(p))+[None]
                for n in range(1,p+2):
                    t=matmul(t,M,p)
                    assert t==((a*q[n-1]%p,q[n]),(a*q[n]%p,q[n+1]))
                    assert poly_power(n,a,c,p)==(a*q[n-1]%p,q[n])
                    for j,x0 in enumerate(list(range(p))+[None]):
                        xs[j]=projective_next(xs[j],a,c,p)
                        numerator=(q[n+1] if x0 is None else q[n+1]*x0+a*q[n])%p
                        denominator=(q[n] if x0 is None else q[n]*x0+a*q[n-1])%p
                        assert numerator or denominator
                        value=numerator*pow(denominator,-1,p)%p if denominator else None
                        assert value==xs[j];matrix_checks+=1
        # a=0 cannot pass condition(i), even before checking invertibility.
        assert all(poly_power(p+1,0,c,p)[0]==0 for c in range(p))
        phi=sum(gcd(j,p+1)==1 for j in range(1,p+2))
        assert len(selected)==(p-1)*phi//2
        rows.append(dict(p=p,full_period_pairs=len(selected),formula=(p-1)*phi//2))
        if p<=13:full[p]=selected
    print('Prime parameters:',parameter_cases,'orbit states:',states,'matrix comparisons:',matrix_checks,flush=True)
    (ROOT/'results/inversive-prime-partial.json').write_text(json.dumps(dict(rows=rows,parameter_cases=parameter_cases,states=states,matrix_checks=matrix_checks),indent=2)+'\n')

    odd_cases=odd_states=0;power_rows=[]
    for e in range(3,9):
        m=1<<e;case_count=0
        for a in range(1,m,4):
            for c in range(2,m,4):
                seq,mu=orbit(a,c,m,False)
                assert mu==0 and len(seq)==m//2 and set(seq)==set(range(1,m,2))
                odd_states+=len(seq);odd_cases+=1;case_count+=1
        power_rows.append(dict(e=e,parameters=case_count,period=m//2))
    # Check necessity in the entire class preserving the odd residues,
    # including noninvertible even a, whose orbits can have a transient.
    boundary_cases=0
    for e in range(3,7):
        m=1<<e
        for a in range(m):
            for c in range(1-a%2,m,2):
                seq,mu=orbit(a,c,m,False)
                assert (mu==0 and len(seq)==m//2)==(a%4==1 and c%4==2)
                if a%2 and not(a%4==1 and c%4==2):
                    assert ((a*pow((a+c)%8,-1,8)+c)%8)==1
                boundary_cases+=1
    identity_checks=0
    for a,c in product([-7,-3,1,5,9],[-6,-2,2,6,10]):
        q=[0,1]
        for n in range(1,1025):q.append(c*q[n]+a*q[n-1])
        for n in range(1,513):
            assert q[2*n]==q[n]*(q[n+1]+a*q[n-1])
            assert q[2*n-1]==a*q[n-1]**2+q[n]**2
            assert q[2*n+1]-a*q[2*n-1]==(q[n+1]-a*q[n-1])*(q[n+1]+a*q[n-1])
            identity_checks+=3
        for ell in range(10):
            n=1<<ell
            assert q[n]%(1<<(ell+1))==1<<ell
            assert (q[n+1]-a*q[n-1])%(1<<(ell+2))==1<<(ell+1)
            den=q[n]+a*q[n-1];num=q[n+1]+a*q[n]
            assert (den-num)%(1<<(ell+2))==1<<(ell+1)
    assert (5-1)==4 and (2-0)*(2+2)==8
    print('Powers of two:',odd_cases,'full-period parameters,',odd_states,'states;',boundary_cases,'boundary cases',flush=True)

    plane_parameters=lag_cases=determinants=rational_checks=0
    for p,parameters in full.items():
        for a,c in parameters:
            seq,mu=orbit(a,c,p);assert mu==0
            q=[0,1]
            for n in range(1,p+1):q.append((c*q[n]+a*q[n-1])%p)
            poles=[]
            for b in range(1,p+1):
                assert q[b]!=0
                inv=pow(q[b],-1,p)
                u=a*q[b-1]*inv%p
                t=(a-a*q[b+1]*q[b-1]*inv**2)%p
                assert t==(-pow(-a,b,p)*inv**2)%p and t
                pole=-u%p;poles.append(pole)
                index=seq.index(pole)
                assert seq[(index+b)%(p+1)] is None
                for n,x in enumerate(seq):
                    y=seq[(n+b)%(p+1)]
                    if x is None or y is None:continue
                    assert y==(q[b+1]*inv+t*pow((x+u)%p,-1,p))%p
                    rational_checks+=1
            assert len(set(poles))==p
            plane_parameters+=1
            for d in range(1,min(3,p)+1):
                for rest in combinations(range(1,p+1),d-1):
                    lags=(0,)+rest
                    points=[tuple(seq[(n+b)%(p+1)] for b in lags) for n in range(p+1)]
                    points=[v for v in points if None not in v]
                    assert len(points)==p+1-d and len(set(points))==len(points)
                    for selected in combinations(points,d+1):
                        assert determinant([(1,)+v for v in selected],p)!=0
                        determinants+=1
                    lag_cases+=1
    # In the 2005-corrected answer37, the remaining printed positive pole
    # should be negative. p7,a1,c1,b2=2 gives F^2(x)=2-1/(x+1).
    seq,mu=orbit(1,1,7);assert seq==[0,None,1,2,5,4,3,6]
    assert seq[(seq.index(6)+2)%8] is None
    assert seq[(seq.index(1)+2)%8]==5
    print('Hyperplanes:',determinants,'nonzero determinants;',rational_checks,'rational identities',flush=True)
    out=dict(status='all_checks_passed',prime_parameter_cases=parameter_cases,
             prime_orbit_states=states,matrix_checks=matrix_checks,prime_counts=rows,
             power_two_parameters=odd_cases,power_two_states=odd_states,power_two_rows=power_rows,
             parity_preserving_boundary_cases=boundary_cases,doubling_identity_checks=identity_checks,
             plane_parameters=plane_parameters,lag_cases=lag_cases,nonzero_determinants=determinants,
             rational_identity_checks=rational_checks,
             C0013=dict(a=1,c=2,n=1,q=[0,1,2,5],printed_left=4,printed_right=8,
                        correction='q_(n+1)+a*q_(n-1) in both consecutive places'),
             C0014=dict(p=7,a=1,c=1,b=2,u=1,t=6,actual_pole=6,printed_evaluation_point=1,
                        F_squared_at_1=5,correction='Evaluate at x=-u_j after the 2005 denominator correction'),
             scope='Exhaustive finite checks support general proofs. No statistical quality guarantee follows solely from period.')
    (ROOT/'results/inversive.json').write_text(json.dumps(out,indent=2)+'\n')
    print('ALL checks passed',flush=True)


if __name__=='__main__':main()
