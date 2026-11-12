"""Exact checks for spectral exercises16--21 and24; checkpointed blocks."""
import argparse
from fractions import Fraction as Q
from itertools import product
import json
from math import gcd,isqrt,prod
from pathlib import Path
import time
import sympy as sp
from spectral import dot,round_ratio
from spectral_independent import shortest_basis,lcg_basis,recurrence_basis

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/spectral-extensions.json'


def l1(v):return sum(abs(x) for x in v)
def plane_score(v):return l1(v)-int(min(v)<0<max(v))


def reduce_dual(U,V,s,score):
    t=len(U);last=t-1;j=0
    while True:
        for i in range(t):
            if i==j:continue
            d,n=dot(V[i],V[j]),dot(V[j],V[j])
            if 2*abs(d)<=n:continue
            q=round_ratio(d,n);old=dot(V[i],V[i])
            V[i]=[x-q*y for x,y in zip(V[i],V[j])]
            U[j]=[x+q*y for x,y in zip(U[j],U[i])]
            assert dot(V[i],V[i])<old
            s=min(s,score(U[j]));last=j
        j=(j+1)%t
        if j==last:return s


def l1_s(a,m,T):
    U,V=[[m]],[[1]];s=m;r=1;values={}
    for t in range(2,T+1):
        r=r*a%m
        for row in U:row.append(0)
        for row in V:row.append(0)
        U.append([-r]+[0]*(t-2)+[1]);V.append([0]*(t-1)+[m])
        for i in range(t-1):
            q=round_ratio(V[i][0]*r,m)
            V[i][-1]=V[i][0]*r-q*m
            U[-1]=[x+q*y for x,y in zip(U[-1],U[i])]
        s=min(s,l1(U[-1]));s=reduce_dual(U,V,s,l1)
        assert sp.Matrix(U)*sp.Matrix(V).T==m*sp.eye(t)
        z=[max(map(abs,row))*s//m for row in V]
        for x in product(*(range(-b,b+1) for b in z)):
            if not any(x):continue
            v=[sum(x[i]*U[i][j] for i in range(t)) for j in range(t)]
            s=min(s,plane_score(v))
        values[t]=dict(count=s,z=z)
    return values


def direct_l1(a,m,t,bound):
    best=bound;mixed=False;found=False;tail=[0]*(t-1)
    def visit(j,n,residue):
        nonlocal best,mixed,found
        if j==t-1:
            radius=best-n;base=-residue%m
            for k in range(-((radius+base)//m),(radius-base)//m+1):
                x=base+k*m;length=n+abs(x)
                if not length:continue
                v=[x]+tail[:];both=min(v)<0<max(v)
                if length<best:best,mixed,found=length,both,True
                elif length==best:mixed|=both;found=True
            return
        for x in range(-(best-n),best-n+1):
            if n+abs(x)>best:continue
            tail[j]=x;visit(j+1,n+abs(x),(residue+x*pow(a,j+1,m))%m)
    visit(0,0,0)
    assert found
    return best-int(mixed)


def norm_one():
    models=dimensions=0;largest_z=0
    for m in range(2,65):
        for a in range(1,m):
            if gcd(a,m)!=1:continue
            values=l1_s(a,m,5)
            for t,d in values.items():
                assert d['count']==direct_l1(a,m,t,d['count']+1),(a,m,t,d)
                dimensions+=1;largest_z=max(largest_z,*d['z'])
            models+=1
    U=sp.Matrix([[1,-1],[0,2]]);V=U.inv().T;X=sp.Matrix([[4,3]]);Y=X*U
    assert list(Y)==[4,2] and l1(list(Y*U))==4 and V.row(1)==sp.Matrix([[Q(1,2),Q(1,2)]])
    assert abs(X[1])>l1(list(Y*U))*max(map(abs,V.row(1)))
    return dict(models=models,dimensions=dimensions,largest_z=largest_z,
                false_fy_example=dict(U=[[1,-1],[0,2]],V=[['1','0'],['1/2','1/2']],X=[4,3],Y=[4,2],printed_rhs='2',left_side=3),
                scope='Corrected L1 adaptation, S4 and S5 update the changed row. Exact independent original-coordinate L1 census. Bound s suffices for STRICT improvement even though score=L1-delta.')


def ties_loop(mode):
    V=[[1,-1,0],[0,1,-1],[1,1,1]];j=0;last=2;seen={};steps=[]
    for iteration in range(100):
        key=(j,tuple(map(tuple,V)))
        if key in seen:return dict(cycle_start=seen[key],cycle_length=iteration-seen[key],steps=steps)
        seen[key]=iteration
        for i in range(3):
            if i==j:continue
            d,n=dot(V[i],V[j]),dot(V[j],V[j])
            allowed=2*abs(d)>n or (2*abs(d)==n and (mode=='symmetric' or d>0))
            if not allowed:continue
            q=((1 if d>0 else -1)*round_ratio(abs(d),n)) if mode=='symmetric' else round_ratio(d,n)
            old=dot(V[i],V[i]);V[i]=[x-q*y for x,y in zip(V[i],V[j])]
            assert dot(V[i],V[i])<=old
            last=j;steps.append(dict(j=j,i=i,q=q,V=[v[:] for v in V]))
        j=(j+1)%3
        if j==last:return dict(terminated=True,iterations=iteration+1,steps=steps)
    raise AssertionError('unexpected long tie sequence')


def reduction_examples():
    cases=[]
    for m in [4,7,64,1000]:
        y=(1-m)//3
        V=[[y+m*(i==j) for j in range(3)] for i in range(3)]
        U=[[-y+(i==j) for j in range(3)] for i in range(3)]
        assert sp.Matrix(U)*sp.Matrix(V).T==m*sp.eye(3)
        assert all(sum(row)%m==0 for row in U)
        assert dot(V[0],V[1])==(1-m*m)//3
        assert dot(V[0],V[0])==(2*m*m+1)//3
        assert dot(U[0],U[0])==(m*m+2)//3
        assert all(2*abs(dot(V[i],V[j]))<=dot(V[j],V[j]) for i in range(3) for j in range(3) if i!=j)
        s=dot(U[0],U[0]);z=[isqrt(dot(row,row)*s//(m*m)) for row in V]
        for i in [1,2]:
            q=round_ratio(dot(U[i],U[0]),dot(U[0],U[0]));assert q==1
            U[i]=[x-q*w for x,w in zip(U[i],U[0])]
            V[0]=[x+q*w for x,w in zip(V[0],V[i])]
        assert U[1]==[-1,1,0] and U[2]==[-1,0,1] and V[0]==[1,1,1]
        cases.append(dict(m=m,old_squared=s,z=z,half_box=(prod(2*b+1 for b in z)-1)//2,transformed_U=U,transformed_V=V))
    positive=ties_loop('positive');symmetric=ties_loop('symmetric')
    assert positive['terminated'] and 'cycle_length' in symmetric
    table=json.loads((ROOT/'results/spectral-table.json').read_text())
    row=table['rows']['3']['dimensions']['6'];vectors=[v for v in row['independent']['vectors'] if v[0] and v[-1]]
    assert row['squared']==4 and len(vectors)==4
    return dict(worst_case=cases,positive_ties=positive,symmetric_ties=symmetric,
                multiple_minima=dict(a=2**18+1,m=2**35,t=6,squared=4,vectors=vectors),
                scope='Exact matrix identities; cubic box growth, sign error in off-diagonal V product; positive tie termination versus symmetric cycle; two non-boundary minimizer pairs in table row3.')


def orbit(a,c,m,x):
    result=[];first=x
    while not result or x!=first:
        result.append(x);x=(a*x+c)%m
        assert len(result)<=m
    return result


def shorter_periods():
    models=point_checks=0
    for e in range(3,7):
        m=2**e
        for a in range(1,m):
            if a%8 not in [3,5]:continue
            for seed in [1,3,5,7]:
                states=orbit(a,0,m,seed);assert len(states)==m//4
                divisor=4 if a%8==5 else 2
                assert gcd(m,*[x-seed for x in states])==divisor
                for t in [2,3]:
                    points=[tuple(x*pow(a,j,m)%m for j in range(t)) for x in states]
                    first=points[0]
                    for u in product(range(-2,3),repeat=t):
                        phases={sum(x*y for x,y in zip(u,p))%m for p in points}
                        congruence=sum(u[j]*pow(a,j,m) for j in range(t))%(m//divisor)==0
                        assert (len(phases)==1)==congruence
                        point_checks+=1
                if a%8==5:
                    r=seed%4;M=m//4;c=((a-1)//4)*r
                    mapped={(x-r)//4 for x in states}
                    assert mapped==set(range(M))
                    for x in states:
                        y=(x-r)//4
                        assert ((a*x%m)-r)//4==(a*y+c)%M
                models+=1
    counter=shortest_basis(lcg_basis(3,8,2))
    false=shortest_basis(lcg_basis(3,4,2))
    assert counter['squared']==8 and false['squared']==2
    table=json.loads((ROOT/'results/spectral-table.json').read_text())
    randu=[]
    for t,d in table['rows']['12']['dimensions'].items():
        t=int(t);w=d['independent']['vectors'][0]
        assert sum(w[j]*pow(65539,j,2**30) for j in range(t))%2**30==0
        randu.append(dict(t=t,squared=d['squared'],witness=w))
    details=json.loads((ROOT/'results/spectral-details.json').read_text())
    for case in details['examples']['randu']:
        t=case['t'];w=case['independent']['vectors'][0]
        assert sum(w[j]*pow(65539,j,2**30) for j in range(t))%2**30==0
        randu.append(dict(t=t,squared=116,witness=w))
    return dict(models=models,normal_checks=point_checks,
                counterexample=dict(original_m=16,a=3,seed=1,orbit=[1,3,9,11],points=[[1,3],[3,9],[9,11],[11,1]],correct=counter,printed_modulus_result=false),
                randu_unchanged=randu,
                scope='Full actual orbits; affine phase condition checked directly. a5mod8 uses m/4, a3mod8 uses m/2. RANDU unchanged by nested-lattice lower bound and explicit witnesses valid modulo2^30.')


def batched():
    models=0
    for e in range(1,7):
        m=2**e;d=gcd(4,m)
        for a in range(1,m,4):
            for c in [1,3]:
                for seed in range(min(4,m)):
                    states=orbit(a,c%m,m,seed);assert len(states)==m
                    selected=states[::4]
                    assert len(selected)==m//d and set(selected)==set(range(seed%d,m,d))
                    for x in selected:
                        y=(a*x+c)%m;z=(a*y+c)%m;w=(a*z+c)%m
                        k=(x-seed)//d
                        z0=(a*(a*seed+c)+c)%m;w0=(a*z0+c)%m
                        assert (z-z0-d*k*a*a)%m==0 and (w-w0-d*k*a*a*a)%m==0
                    models+=1
    return dict(models=models,scope='Correct lattice vector gcd(4,m)*(1,a^2,a^3)/m. Printed4 is valid for e>=2; e1 needs2. General offset checked directly.')


def second_order_s(a,b,p,T):
    U=[[p,0],[0,p]];V=[[1,0],[0,1]];R=[[1,0],[0,1]];s=p*p;out={2:s}
    for t in range(3,T+1):
        R=[[row[1]%p,(b*row[0]+a*row[1])%p] for row in R]
        f,g=R[0][1],R[1][1]
        for row in U:row.append(0)
        for row in V:row.append(0)
        U.append([-f,-g]+[0]*(t-3)+[1]);V.append([0]*(t-1)+[p])
        for i in range(t-1):
            v=V[i][0]*f+V[i][1]*g;q=round_ratio(v,p)
            V[i][-1]=v-q*p;U[-1]=[x+q*y for x,y in zip(U[-1],U[i])]
        s=min(s,dot(U[-1],U[-1]));s=reduce_dual(U,V,s,lambda x:dot(x,x))
        assert sp.Matrix(U)*sp.Matrix(V).T==p*sp.eye(t)
        z=[isqrt(dot(v,v)*s//(p*p)) for v in V]
        for x in product(*(range(-b,b+1) for b in z)):
            if not any(x):continue
            v=[sum(x[i]*U[i][j] for i in range(t)) for j in range(t)]
            s=min(s,dot(v,v))
        out[t]=s
    return out


def second_order():
    models=dimensions=0
    for p in [2,3,5,7,11]:
        for a in range(p):
            for b in range(1,p):
                states=[];x,y=0,1
                while not states or (x,y)!=(0,1):
                    states.append((x,y));x,y=y,(a*y+b*x)%p
                    assert len(states)<p*p
                if len(states)!=p*p-1:continue
                values=second_order_s(a,b,p,5)
                for t,s in values.items():
                    d=shortest_basis(recurrence_basis(a,b,p,t))
                    assert d['squared']==s,(p,a,b,t,s,d)
                    # A spanning set of initial states, including zero,
                    # verifies the two modular constraints independently.
                    for u in d['vectors']:
                        for initial in [(1,0),(0,1)]:
                            xs=list(initial)
                            while len(xs)<t:xs.append((a*xs[-1]+b*xs[-2])%p)
                            assert dot(u,xs)%p==0
                    dimensions+=1
                models+=1
    return dict(models=models,dimensions=dimensions,scope='All primitive second-order recurrences for p2,3,5,7,11; literal S4-prime with recurrence matrix versus independent LLL/sphere; coordinate-spanning states validate dual constraints.')


def output_and_boundary():
    # Exercise17 changes only S9, which is never reached for t=2.
    # Record an independently enumerated target output for that dimension.
    d=shortest_basis(lcg_basis(2,5,2))
    exact=sorted([list(v) for v in product(range(-2,3),repeat=2)
                  if dot(v,v)==5 and (v[0]+2*v[1])%5==0])
    assert d['squared']==5 and sorted(d['vectors'])==exact and len(exact)==4
    # For m=2 the stride-four sample consists of one point modulo Z^3.
    states=orbit(1,1,2,0)
    point=[states[j%2] for j in [0,2,3]]
    printed=sp.Matrix([[2,2,2],[0,1,0],[0,0,1]])
    correct=sp.Matrix([[1,1,1],[0,1,0],[0,0,1]])
    assert point==[0,0,1] and printed.det()==2 and correct.det()==1
    return dict(two_dimensional=dict(a=2,m=5,squared=5,vectors=exact,
                control_flow='S1--S3 compute nu2; S4 exits at T=2 or increments t. S9 is not reached at t=2.'),
                period_two=dict(m=2,a=1,c=1,seed=0,point_numerator=point,
                    point_denominator=2,printed_determinant=2,correct_determinant=1))


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    r=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}
    for key,fun in [('norm_one',norm_one),('reduction_examples',reduction_examples),('shorter_periods',shorter_periods),('batched',batched),('second_order',second_order),('output_and_boundary',output_and_boundary)]:
        if key in r:continue
        start=time.monotonic();r[key]=fun();r[key]['seconds']=time.monotonic()-start
        OUT.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(key,'complete',r[key]['seconds'],flush=True)
