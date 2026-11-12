"""Exact models and certificates for 3.2.1.1 exercises 12--14 after errata."""
from itertools import product
from math import gcd,prod,isqrt
from pathlib import Path
import json
import random
import sympy

ROOT=Path(__file__).resolve().parent


def word(digits,b):
    result=0
    for x in digits:
        result=result*b+x
    return result


def encode(past,carry,coeff,b):
    m=sum(a*b**(i+1) for i,a in enumerate(coeff))-1
    s=carry
    for j,a in enumerate(coeff,1):
        s+=a*word(past[:j],b)
    return s*(1 if m>0 else -1)


def transition(past,carry,coeff,b):
    total=sum(a*x for a,x in zip(coeff,past))+carry
    cn,x=divmod(total,b)
    return (x,)+past[:-1],cn


def prime_certificates(targets):
    cert={2:dict(prime=2)}
    def build(p):
        if p in cert:return
        factors=[(int(q),int(e)) for q,e in sympy.factorint(p-1).items()]
        assert prod(q**e for q,e in factors)==p-1
        for q,_ in factors:build(q)
        for g in range(2,10000):
            if pow(g,p-1,p)==1 and all(gcd(pow(g,(p-1)//q,p)-1,p)==1 for q,_ in factors):
                cert[p]=dict(prime=p,witness=g,factors=factors)
                return
        raise AssertionError(('No prime certificate',p))
    for p in targets:build(p)
    proved={2}
    for p in sorted(cert):
        if p==2:continue
        fs=cert[p]['factors'];g=cert[p]['witness']
        assert all(q in proved and e>=1 for q,e in fs)
        assert prod(q**e for q,e in fs)==p-1
        assert pow(g,p-1,p)==1
        assert all(gcd(pow(g,(p-1)//q,p)-1,p)==1 for q,_ in fs)
        proved.add(p)
    return [cert[p] for p in sorted(cert)]


def main():
    general=carry_bounds=borrow=decimal=wheel=0
    for b in range(2,6):
        for k in range(1,4):
            for coeff in product(range(-2,3),repeat=k):
                lo=sum(min(a,0) for a in coeff);hi=sum(max(a,0) for a in coeff)
                m=sum(a*b**(i+1) for i,a in enumerate(coeff))-1
                M=abs(m);inverse=pow(b,-1,M)
                for past in product(range(b),repeat=k):
                    for c in range(lo,hi):
                        new,cn=transition(past,c,coeff,b)
                        assert lo<=cn<hi
                        carry_bounds+=1
                        X=encode(past,c,coeff,b)
                        if not 0<=X<M:continue
                        Y=encode(new,cn,coeff,b)
                        assert b*Y==X+M*new[0]
                        assert 0<=Y<M and Y==inverse*X%M
                        general+=1
    # Both subtract-with-borrow variants, including larger lags.
    for b in range(2,6):
        for k in range(2,6):
            for ell in range(1,k):
                for sign in [-1,1]:
                    coeff=[0]*k;coeff[-1]=-sign;coeff[ell-1]=sign
                    M=b**k-b**ell+sign;inverse=pow(b,-1,M)
                    for past in product(range(b),repeat=k):
                        for bn in [0,1]:
                            X=word(past,b)-word(past[:ell],b)+sign*bn
                            if not 0<=X<M:continue
                            new,cn=transition(past,-bn,coeff,b)
                            Y=word(new,b)-word(new[:ell],b)-sign*cn
                            assert cn in [-1,0]
                            assert b*Y==X+M*new[0]
                            assert Y==inverse*X%M
                            borrow+=1
    rng=random.Random(3211142026)
    for sign,a in [(-1,999999900),(1,8999999101)]:
        M=10**10-10**3+sign
        assert 10*a%M==1
        coeff=[0]*10;coeff[2]=sign;coeff[9]=-sign
        past=(0,)*9+(1,);c=0
        digits={-i:past[i-1] for i in range(1,11)};cs={0:0};states={0:1}
        for n in range(504):
            past,c=transition(past,c,coeff,10)
            digits[n]=past[0];cs[n+1]=c
            states[n+1]=encode(past,c,coeff,10)
            assert states[n+1]==pow(a,n+1,M)
        for n in range(500):
            high=word([digits[n-j] for j in range(1,8)],10)
            low=word([digits[n+2],digits[n+1],digits[n]],10)
            future=high*1000-sign*low+sign*1000*(-cs[n+3])
            assert future==states[n]
            # Independent long division versus the backward digit sequence.
            U=states[n]
            for h in range(1,21):
                digit,U=divmod(10*U,M)
                j=n-h
                previous=pow(a,j,M);following=pow(a,j+1,M)
                assert digit==(10*following-previous)//M
            decimal+=1
        if sign==-1:
            # Pencil-and-paper rotation/folding and inverse rotation.
            xs={0,1,M-1,M-2,999999900,*[rng.randrange(M) for _ in range(10000)]}
            for X in xs:
                d=X//10**9;T=(10*X)%10**10+d*(10**3+1)
                while T>=10**10:
                    hi,lo=divmod(T,10**10);T=lo+hi*(10**3+1)
                assert T%M==10*X%M
                q,r=divmod(X,10)
                inverse_rotation=q+r*10**9-r*100
                assert 0<=inverse_rotation<M and inverse_rotation==a*X%M
                wheel+=1
    b=2**31;d=65430;M=d*b*b+b-1;order=(M-1)//2
    fs=[(int(q),int(e)) for q,e in sympy.factorint(order).items()]
    certificates=prime_certificates([M,*[q for q,e in fs]])
    assert prod(q**e for q,e in fs)==order
    assert pow(b,order,M)==1
    residues=[dict(prime=q,residue=pow(b,order//q,M)) for q,e in fs]
    assert all(x['residue']!=1 for x in residues)
    # Exact witnesses for the short dual vectors discussed in the note.
    a=pow(b,-1,M)
    assert (1-b*a)%M==0 and (d+a-a*a)%M==0
    q=isqrt(M)
    assert q//2>b+1
    result=dict(status='all assertions passed',general_states=general,
                carry_bound_states=carry_bounds,borrow_states=borrow,
                decimal_states=decimal,wheel_inputs=wheel,
                example=dict(base=b,modulus=M,order=order,order_factors=fs,
                             proper_divisor_residues=residues,
                             spectral_v2_squared=b*b+1,spectral_v3_squared=d*d+2,
                             comparison_multiplier=q,comparison_v2_lower_bound=f'{q}/2'),
                prime_certificates=certificates)
    (ROOT/'results/carry-generators.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='prime_certificates'},indent=2))


if __name__=='__main__':
    main()
