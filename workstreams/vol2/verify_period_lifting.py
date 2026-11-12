"""Exact finite checks for TAOCP 3.2.2-8--12; proofs are in the notes."""
from itertools import product
from math import gcd
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent


def prime_divisors(n):
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0:n//=p
        p+=1
    if n>1:out.append(n)
    return out


def quadratic_criterion(d,a,c,m,ps):
    return (gcd(c,m)==1
            and all(d%p==0 and (a-1)%p==0 for p in ps if p!=2)
            and (m%4!=0 or (d%2==0 and (d-a+1)%4==0))
            and (m%2!=0 or (d-a+1)%2==0)
            and (m%9!=0 or (d-3*c)%9!=0))


def scalar_cycle(d,a,c,m):
    seen={};x=0
    while x not in seen:
        seen[x]=len(seen);x=(d*x*x+a*x+c)%m
    return seen[x],len(seen)-seen[x]


def quadratic():
    cases=full=0
    for m in range(1,49):
        ps=prime_divisors(m)
        for d,a,c in product(range(m),repeat=3):
            predicted=quadratic_criterion(d,a,c,m,ps)
            mu,lam=scalar_cycle(d,a,c,m)
            assert (lam==m)==predicted,(m,d,a,c,mu,lam,predicted)
            full+=predicted;cases+=1
    base_identities=0
    for p in (2,3,5,7):
        m=p*p
        for d,a,c in product(range(m),repeat=3):
            if not quadratic_criterion(d,a,c,m,[p]):continue
            for seed in range(m):
                x=seed
                for _ in range(p):x=(d*x*x+a*x+c)%m
                increment=2 if p==2 else (3*c-d if p==3 else p*c)
                assert x==(seed+increment)%m
                base_identities+=1
    # The exceptional condition modulo 9 is necessary.
    assert scalar_cycle(3,1,1,9)==(0,3)
    coveyou_states=0
    for e in range(2,17):
        m=2**e;small=m//4
        x=2;seen=set()
        for _ in range(small):
            assert x not in seen and x%4==2;seen.add(x)
            y=(x-2)//4
            following=x*(x+1)%m
            assert following==4*((4*y*y+5*y+1)%small)+2
            x=following;coveyou_states+=1
        assert x==2
    return dict(all_coefficient_cases=cases,full_period_cases=full,
                base_prime_square_identities=base_identities,
                coveyou_states=coveyou_states)


def recurrence_cycle(coeff,initial,m):
    state=tuple(x%m for x in initial);seen={};values=[]
    while state not in seen:
        seen[state]=len(values);values.append(state[0])
        v=sum(a*x for a,x in zip(coeff,state[::-1]))%m
        state=state[1:]+(v,)
    mu=seen[state]
    return mu,len(values)-mu,values


def A_initial(coeff):
    k=len(coeff);values=[1]
    for n in range(1,k):
        values.append(sum(coeff[j-1]*values[n-j] for j in range(1,n+1)))
    return values


def trim(poly,p):
    a=[v%p for v in poly]
    while a and a[-1]==0:a.pop()
    return a


def remainder(a,b,p):
    a=trim(a,p);b=trim(b,p)
    while len(a)>=len(b) and a:
        shift=len(a)-len(b);c=a[-1]*pow(b[-1],-1,p)%p
        for j,v in enumerate(b):a[j+shift]=(a[j+shift]-c*v)%p
        a=trim(a,p)
    return a


def coprime(a,b,p):
    a,b=trim(a,p),trim(b,p)
    while b:a,b=b,remainder(a,b,p)
    return len(a)==1


def numerator(coeff,initial):
    return [initial[n]-sum(coeff[j-1]*initial[n-j] for j in range(1,n+1))
            for n in range(len(coeff))]


def multiply(a,b,m):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]=(out[i+j]+x*y)%m
    return out


def linear_lifting():
    periods=polynomial_identities=numerator_tests=0
    for k in (1,2,3):
        for coeff in product(range(-2,3),repeat=k):
            initial=A_initial(coeff);f=[1]+[-a for a in coeff]
            for p in (2,3,5):
                lengths=[]
                for e in range(1,5):
                    m=p**e;mu,lam,values=recurrence_cycle(coeff,initial,m)
                    lengths.append(lam);periods+=1
                    # Independent finite polynomial certificate: f*H=1-z^lam.
                    H=[(values[n]-(values[n-lam] if n>=lam else 0))%m
                       for n in range(mu+lam)]
                    lhs=multiply(f,H,m)
                    rhs=[0]*max(len(lhs),lam+1)
                    rhs[0]=1;rhs[lam]=(rhs[lam]-1)%m
                    assert trim(lhs,m)==trim(rhs,m)
                    polynomial_identities+=1
                    for seed in ([0]*(k-1)+[1],list(range(1,k+1))):
                        g=numerator(coeff,seed)
                        _,other,_=recurrence_cycle(coeff,seed,m)
                        assert lam%other==0
                        if coprime(f,g,p):assert other==lam
                        numerator_tests+=1
                for i in range(len(lengths)-1):
                    assert lengths[i+1] in (lengths[i],p*lengths[i])
                    if p**(i+1)>2 and lengths[i+1]!=lengths[i]:
                        assert all(lengths[j]==lengths[i]*p**(j-i)
                                   for j in range(i,len(lengths)))
    exceptional=[recurrence_cycle((4,-1),(1,4),m)[1] for m in (2,4,8)]
    assert exceptional==[2,4,4]
    flat=[recurrence_cycle((1,-1),(1,1),2**e)[1] for e in range(2,17)]
    assert flat==[6]*15
    return dict(A_periods=periods,polynomial_certificates=polynomial_identities,
                numerator_sequences=numerator_tests,excluded_base_case=exceptional,
                nonterminating_search_periods=flat)


def fibonacci():
    cases=0
    for e in range(1,7):
        m=2**e
        for a,b in product(range(m),repeat=2):
            if a%2==b%2==0:continue
            mu,lam,_=recurrence_cycle((1,1),(a,b),m)
            assert mu==0 and lam==3*2**(e-1)
            assert (b*b-a*b-a*a)%2==1
            cases+=1
    identities=0
    # Fast doubling, independent of the orbit code.
    def fib(n,mod):
        if not n:return 0,1
        a,b=fib(n//2,mod)
        c=a*(2*b-a)%mod;d=(a*a+b*b)%mod
        return (d,(c+d)%mod) if n%2 else (c,d)
    for e in range(2,101):
        assert fib(3*2**(e-1),2**(e+1))==(0,2**e+1)
        identities+=1
    return dict(initial_pairs=cases,doubling_identities=identities)


def affine_second_order():
    maps=states=cycles=0
    maxima={}
    for m in (2,4,8,16):
        largest=0
        for a,b,c in product(range(m),repeat=3):
            finished=set()
            for initial in range(m*m):
                if initial in finished:continue
                route={};x=initial
                while x not in finished and x not in route:
                    route[x]=len(route);u,v=divmod(x,m)
                    x=v*m+(a*v+b*u+c)%m
                if x in route:
                    length=len(route)-route[x]
                    assert length<=2*m
                    largest=max(largest,length);cycles+=1
                finished.update(route)
            states+=m*m;maps+=1
        maxima[m]=largest
        assert largest==2*m
        x=y=0
        orbit=[]
        for _ in range(2*m):
            orbit.append((x,y));x,y=y,(x+1)%m
        assert (x,y)==(0,0) and len(set(orbit))==2*m
    return dict(coefficient_maps=maps,states=states,cycles=cycles,maxima=maxima)


def main():
    result=dict(status='in_progress')
    for name,fn in [('quadratic',quadratic),('linear_lifting',linear_lifting),
                    ('fibonacci',fibonacci),('affine_second_order',affine_second_order)]:
        result[name]=fn();print(name,result[name],flush=True)
        (ROOT/'results/period-lifting-partial.json').write_text(json.dumps(result,indent=2)+'\n')
    result['status']='passed'
    (ROOT/'results/period-lifting.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
