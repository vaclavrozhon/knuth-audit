"""Primitivity criteria, exercise 19 constants, and squarefree moduli."""
from hashlib import sha256
from itertools import product
from math import prod, lcm
from pathlib import Path
import json
import sympy
from verify_ecpp import Verifier

ROOT=Path(__file__).resolve().parent
# N=2^e, p=N-delta. First two columns of Table 4.5.4-2, p.408.
BINARY_EXPONENTS=list(range(15,49))+[59,60,63,64]
BINARY_DELTAS=[19,15,1,5,1,3,9,3,15,3,39,5,39,57,3,35,1,5,9,41,
               31,5,25,45,7,87,21,11,57,17,55,21,115,59,55,93,25,59]
DECIMAL_ROWS=[(6,17),(7,9),(8,11),(9,63),(10,33),(11,23),(12,11),(16,63)]


def multiply(u,v,a,p):
    k=len(a);out=[0]*(2*k-1)
    for i,x in enumerate(u):
        for j,y in enumerate(v):out[i+j]=(out[i+j]+x*y)%p
    for j in range(2*k-2,k-1,-1):
        c=out[j]
        for t,aa in enumerate(a,1):out[j-t]=(out[j-t]+c*aa)%p
    return tuple(out[:k])


def power_x(n,a,p):
    k=len(a);r=(1,)+(0,)*(k-1);x=(0,1)+(0,)*(k-2) if k>1 else (a[0]%p,)
    while n:
        if n&1:r=multiply(r,x,a,p)
        n>>=1
        if n:x=multiply(x,x,a,p)
    return r


def criterion(a,p,minus_factors,r_factors):
    k=len(a);norm=(-1)**(k-1)*a[-1]%p
    if norm==0 or pow(norm,p-1,p)!=1:return False
    if any(pow(norm,(p-1)//q,p)==1 for q in minus_factors):return False
    r=(p**k-1)//(p-1)
    if power_x(r,a,p)!=(norm,)+(0,)*(k-1):return False
    return all(any(power_x(r//q,a,p)[1:]) for q in r_factors)


def cycle_length(a,p):
    k=len(a);initial=(0,)*(k-1)+(1,);state=initial;seen={}
    while state not in seen:
        seen[state]=len(seen)
        state=state[1:]+(sum(x*y for x,y in zip(a,state[::-1]))%p,)
    return len(seen)-seen[state],seen[state],len(seen)


def matrix_product(u,v,p):
    return tuple(sum(u[2*i+t]*v[2*t+j] for t in range(2))%p for i in range(2) for j in range(2))


def matrix_power(n,a,p):
    r=(1,0,0,1);x=(0,1,a[1],a[0])
    while n:
        if n&1:r=matrix_product(r,x,p)
        n>>=1
        if n:x=matrix_product(x,x,p)
    return r


def factors(n):return [(int(q),int(e)) for q,e in sympy.factorint(n).items()]


def main():
    v=Verifier();counts=[];first={};states=0
    for p,kmax in [(2,8),(3,5),(5,4),(7,3),(11,2)]:
        for k in range(1,kmax+1):
            fs=factors(p-1);rs=factors((p**k-1)//(p-1));good=0
            for a in product(range(p),repeat=k):
                claimed=criterion(a,p,[q for q,e in fs],[q for q,e in rs])
                length,mu,visited=cycle_length(a,p);states+=visited
                actual=mu==0 and length==p**k-1
                assert claimed==actual,(p,k,a,claimed,length,mu)
                if claimed:good+=1;first.setdefault((p,k),a)
            fs_order=factors(p**k-1)
            phi=prod((q-1)*q**(e-1) for q,e in fs_order)
            assert good==phi//k
            counts.append(dict(p=p,k=k,primitive_polynomials=good))
    print('small criteria:',sum(p['p']**p['k'] for p in counts),'polynomials,',states,'orbit states',flush=True)

    assert len(BINARY_EXPONENTS)==len(BINARY_DELTAS)==38
    rows=[];composite_witnesses=[]
    targets=[(2,e,d) for e,d in zip(BINARY_EXPONENTS,BINARY_DELTAS)]+[(10,e,d) for e,d in DECIMAL_ROWS]
    for base,e,delta in targets:
        N=base**e;p=N-delta;v.prove_small(p)
        fm=factors(p-1);fp=factors(p+1)
        for q,exp in fm+fp:v.prove_small(q)
        # Certify that this really is the largest prime below N.
        for n in range(p+1,N):
            q=next(iter(sympy.factorint(n)))
            assert 1<q<n and n%q==0
            composite_witnesses.append(dict(n=n,divisor=int(q)))
        for attempt in range(10000):
            norm=2+int.from_bytes(sha256(f'norm-{p}-{attempt}'.encode()).digest(),'big')%(p-3)
            if all(pow(norm,(p-1)//q,p)!=1 for q,exp in fm):break
        else:raise AssertionError(('no primitive norm',p))
        for attempt in range(10000):
            a1=2+int.from_bytes(sha256(f'a1-{p}-{attempt}'.encode()).digest(),'big')%(p-3)
            a=(a1,(-norm)%p)
            if criterion(a,p,[q for q,exp in fm],[q for q,exp in fp]):break
        else:raise AssertionError(('no primitive quadratic',p))
        order=p*p-1
        assert matrix_power(order,a,p)==(1,0,0,1)
        all_factors=sorted({q for q,exp in fm+fp})
        witnesses=[]
        for q in all_factors:
            value=matrix_power(order//q,a,p)
            assert value!=(1,0,0,1)
            witnesses.append(dict(prime_divisor=q,matrix=list(value)))
        rows.append(dict(base=base,exponent=e,delta=delta,p=p,a1=a[0],a2=a[1],
                         factors_p_minus_1=fm,factors_p_plus_1=fp,matrix_order_witnesses=witnesses))
        print('quadratic constants',base,e,delta,'verified',flush=True)

    crt_rows=[]
    for ps in [(2,3),(2,5),(3,5),(2,3,5)]:
        m=prod(ps)
        for k in range(1,4):
            a=tuple(sum(first[(p,k)][j]*(m//p)*pow(m//p,-1,p) for p in ps)%m for j in range(k))
            length,mu,visited=cycle_length(a,m)
            expected=lcm(*(p**k-1 for p in ps))
            assert mu==0 and length==expected
            crt_rows.append(dict(modulus=m,degree=k,coefficients=a,period=length))
    v.validate_small_certificates()
    result=dict(status='passed',small_criteria=counts,small_orbit_states=states,
                exercise19=rows,largest_prime_composite_witnesses=composite_witnesses,
                small_lucas_certificates=[v.small[p] for p in sorted(v.small)],
                exercise22=crt_rows,
                scope='Exact period/criterion checks; no spectral-quality or statistical-optimality claim')
    (ROOT/'results/primitive-criteria.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ALL criteria,',len(rows),'quadratic constants,',len(crt_rows),'CRT examples passed',flush=True)


if __name__=='__main__':main()
