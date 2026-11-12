"""Independent orbit enumeration versus number-theoretic claims, 3.2.1.2.

Small orbits are enumerated directly, without using any period formulas.
Large table entries use exact modular-order certificates and already proved
prime factors from modulus-table.json. No statistical quality is asserted.
"""
from functools import lru_cache
from itertools import product
from math import gcd, lcm, prod
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent


@lru_cache(None)
def factors(n):
    result=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:result.append((p,e))
        p+=1
    if n>1:result.append((n,1))
    return tuple(result)


def orbit(m,a,c,x):
    seen={};values=[]
    while x not in seen:
        seen[x]=len(values);values.append(x);x=(a*x+c)%m
    return seen[x],len(values)-seen[x],values


def order(a,m):
    assert gcd(a,m)==1
    return orbit(m,a,0,1%m)[1]


def lambda_pp(p,e):
    return 2**max(0,e-2) if p==2 and e>=3 else (p-1)*p**(e-1)


def carmichael(m):
    return lcm(*(lambda_pp(p,e) for p,e in factors(m)))


def full_criterion(m,a,c):
    return gcd(c,m)==1 and all((a-1)%p==0 for p,_ in factors(m)) and (m%4!=0 or (a-1)%4==0)


def geometric_period(a,p,e):
    m=p**e
    if a%p==0:return 1
    if p==2 and e>=2 and a%4==3:
        return 2 if a%m==m-1 else 2*order(a,m)
    if a%p==1:return m
    return order(a,m)


def predicted_period(m,a,c,x):
    A=((a-1)*x+c)%m
    reduced=m//gcd(A,m)
    return lcm(*(geometric_period(a,p,e) for p,e in factors(reduced)))


def primitive_criterion(a,p,e):
    if p==2:
        if e==1:return a%2==1
        if e==2:return a%4==3
        if e==3:return a%8 in (3,5,7)
        return a%8 in (3,5)
    base=a%p!=0 and all(pow(a,(p-1)//q,p)!=1 for q,_ in factors(p-1))
    return base and (e==1 or pow(a,p-1,p*p)!=1)


def main():
    counts=dict(orbits=0,crt=0,primitive_prime_power=0,order_lcm=0,
                binary_conjugacy=0,half_period=0,gcd_identity=0,
                polynomial_root_bound=0)
    max_tails=[]
    for m in range(1,33):
        maxtail=0
        for a,c,x in product(range(m),repeat=3):
            mu,lam,values=orbit(m,a,c,x)
            assert (lam==m)==full_criterion(m,a,c),(m,a,c,x,mu,lam)
            assert lam==predicted_period(m,a,c,x),(m,a,c,x,mu,lam)
            components=[orbit(p**e,a%(p**e),c%(p**e),x%(p**e))[:2] for p,e in factors(m)]
            assert mu==max((u for u,_ in components),default=0)
            assert lam==lcm(*(v for _,v in components))
            counts['orbits']+=1;counts['crt']+=1;maxtail=max(mu,maxtail)
            if c==0:assert carmichael(m)%lam==0
        bound=max((e for _,e in factors(m)),default=0)
        assert maxtail==bound
        max_tails.append([m,maxtail])
    for m in range(2,241):
        unit_orders={a:order(a,m) for a in range(1,m) if gcd(a,m)==1}
        assert max(unit_orders.values())==carmichael(m)
        phi=len(unit_orders);fs=factors(m)
        cyclic=m in (2,4) or (len(fs)==1 and fs[0][0]!=2) or (len(fs)==2 and fs[0]==(2,1))
        assert (carmichael(m)==phi)==cyclic
        if len(fs)==1:
            p,e=fs[0]
            for a in range(m):
                assert primitive_criterion(a,p,e)==(a in unit_orders and unit_orders[a]==carmichael(m))
                counts['primitive_prime_power']+=1
        if m<=60:
            for a,r in unit_orders.items():
                for b,s in unit_orders.items():
                    f1=dict(factors(r));f2=dict(factors(s));k1=k2=1
                    for p in f1.keys()|f2.keys():
                        u=f1.get(p,0);v=f2.get(p,0)
                        if u<v:k1*=p**u
                        else:k2*=p**v
                    z=pow(a,k1,m)*pow(b,k2,m)%m
                    assert order(z,m)==lcm(r,s)
                    counts['order_lcm']+=1
    for e in range(1,9):
        m=2**e;h=m//2
        for a in range(m):
            for c in range(1,m,2):
                if not full_criterion(m,a,c):continue
                _,_,v=orbit(m,a,c,0)
                assert all(v[n+h]==(v[n]+h)%m for n in range(h))
                counts['half_period']+=h
                s=order(a,m);assert gcd(v[s%m],m)==s
                counts['gcd_identity']+=1
        if e>=4:
            for a in range(m):
                if a%8 not in (3,5):continue
                c=(a-1)//4 if a%8==5 else (a+1)//4
                for y in range(m//4):
                    if a%8==5:
                        assert (a*(4*y+1)%m-1)//4==(a*y+c)%(m//4)
                    else:
                        for parity in (1,-1):
                            x=parity*(4*y+1)%m
                            yn=(((-parity)*(a*x%m))%m-1)//4
                            assert yn==((1-4*c)*y-c)%(m//4)
                    counts['binary_conjugacy']+=1
    for m in range(2,101):
        for a in range(m):
            for c in range(m):
                if not full_criterion(m,a,c):continue
                _,_,v=orbit(m,a,c,0);s=order(a,m)
                assert gcd(v[s%m],m)==s
                counts['gcd_identity']+=1
    for p in (2,3,5,7):
        for n in range(5):
            for coeff in product(range(p),repeat=n):
                def evaluate(x):
                    v=1
                    for c in coeff:v=(v*x+c)%p
                    return v
                assert sum(evaluate(x)==0 for x in range(p))<=n
                counts['polynomial_root_bound']+=1
    # Theorem D and exercises 17--18: no long orbit enumeration necessary.
    listed=[3,11,13,19,21,27,29,37,53,59,61,67,69,77,83,91,
            109,117,123,131,133,139,141,147,163,171,173,179,181,187,189,197]
    calculated=[a for a in range(200) if a%8 in (3,5) and a%5!=0 and pow(a,4,25)!=1]
    assert calculated==listed
    both=[a for a in listed if primitive_criterion(a,5,2)]
    assert both==[3,13,27,37,53,67,77,83,117,123,133,147,163,173,187,197]
    for e in (5,6,9,16):
        m=10**e;lam=5*10**(e-2)
        for a in range(200):
            exact=pow(a,lam,m)==1 and all(pow(a,lam//q,m)!=1 for q in (2,5))
            assert exact==(a in listed)
    # Full table for exercise 19: certify a multiplier of maximum order.
    table=json.loads((ROOT/'results/modulus-table.json').read_text())
    certs={c['prime']:c for c in table['prime_certificates']}
    rows=[]
    for row in table['table_rows']:
        m=row['value'];fs=row['factors']
        lam=lcm(*((p-1)*p**(e-1) for p,e in fs)) # all tabulated moduli are odd
        prime_divisors=set()
        for p,e in fs:
            prime_divisors.update(q for q,_ in certs[p]['factors_of_previous'])
            if e>1:prime_divisors.add(p)
        # All these primes have recursive certificates in the input artifact.
        assert all(q in certs for q in prime_divisors)
        found=[]
        for a in range(2,100000):
            if pow(a,lam,m)==1 and all(pow(a,lam//q,m)!=1 for q in prime_divisors):
                found.append(a)
                if len(found)==3:break
        assert len(found)==3
        assert prod(q**e for q,e in fs)==m
        rows.append(dict(base=row['base'],exponent=row['exponent'],sign=row['sign'],
                         modulus=m,maximum_order=lam,multipliers=found,
                         order_prime_divisors=sorted(prime_divisors),
                         scope='Maximum period with a coprime seed; statistical quality not asserted.'))
    result=dict(status='passed',counts=counts,max_tails=max_tails,theorem_d=calculated,
                primitive_at_both_prime_powers=both,table_entries=len(rows),table=rows)
    (ROOT/'results/multiplier-periods.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('max_tails','table')},indent=2))


if __name__=='__main__':main()
