"""Period lifting criterion and lagged-generator identities, 3.2.2-23,30--33."""
from itertools import product
from pathlib import Path
import json
import random
from verify_binary_polynomials import Quotient
from verify_primitive_criteria import power_x, cycle_length

ROOT=Path(__file__).resolve().parent


def convolution(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def exceptional(a):
    k=len(a);f=[-x for x in a[::-1]]+[1]
    opposite=[(-1)**j*x for j,x in enumerate(f)]
    lhs=[x+y for x,y in zip(convolution(f,f),convolution(opposite,opposite))]
    plus=[0]*(2*k+1);minus=plus.copy()
    for j,x in enumerate(f):
        plus[2*j]=2*x;minus[2*j]=2*(-1)**(k+j)*x
    return (all((x-y)%8==0 for x,y in zip(lhs,plus)),
            all((x-y)%8==0 for x,y in zip(lhs,minus)))


def main():
    factor_rows=json.loads((ROOT/'results/binary-period-factors.json').read_text())['small_exponent_rows']
    fs={row['exponent']:[q for q,e in row['factors']] for row in factor_rows}
    fs[1]=[]
    checks=0;states=0;exceptions=0
    for k in range(1,7):
        for a in product(range(4),repeat=k):
            mask=sum((x%2)<<(k-1-j) for j,x in enumerate(a))
            primitive=(mask==1 if k==1 else Quotient(k,mask).primitive(fs[k]))
            if not primitive:continue
            M=(1<<k)-1;badminus,badplus=exceptional(a)
            u=power_x(M,a,4)
            assert (u==(3,)+(0,)*(k-1))==badminus
            assert (u==(1,)+(0,)*(k-1))==badplus
            period,mu,visited=cycle_length(a,8);states+=visited
            assert mu==0 and (period==4*M)==(not badminus and not badplus)
            checks+=1;exceptions+=badminus or badplus
    print('lifting criterion',checks,'coefficient vectors,',states,'direct states',flush=True)

    trinomials=[]
    for k in range(3,13):
        for l in range(1,k):
            if not Quotient(k,(1<<l)|1,l).primitive(fs[k]):continue
            for middle,constant in product([-1,1],repeat=2):
                a=[0]*k;a[k-l-1]=-middle;a[k-1]=-constant
                assert exceptional(a)==(False,False)
                period,mu,visited=cycle_length(a,8)
                assert mu==0 and period==4*((1<<k)-1)
                trinomials.append(dict(k=k,l=l,middle=middle,constant=constant,period_mod_8=period))
    # Original addition and exercise 23 subtraction, at the actual degree 55.
    large=[]
    for a24 in [-1,1]:
        a=[0]*55;a[23]=a24;a[54]=1
        M=(1<<55)-1
        assert exceptional(a)==(False,False)
        assert power_x(4*M,a,8)==(1,)+(0,)*54
        assert power_x(2*M,a,8)!=(1,)+(0,)*54
        large.append(dict(coefficient_lag24=a24,period_mod8=4*M))

    # Coefficients of X_n as an integer linear form in X_0,...,X_54.
    forms=[tuple(int(i==j) for j in range(55)) for i in range(55)]
    for n in range(55,1501):
        forms.append(tuple(x+y for x,y in zip(forms[n-24],forms[n-55])))
    decimation_checks=0
    for n in range(55,501):
        assert forms[2*n]==tuple(2*a-b+c for a,b,c in zip(forms[2*(n-12)],forms[2*(n-24)],forms[2*(n-55)]))
        assert forms[3*n]==tuple(3*a-3*b+c+d for a,b,c,d in zip(forms[3*(n-8)],forms[3*(n-16)],forms[3*(n-24)],forms[3*(n-55)]))
        decimation_checks+=2
    printed500={2:792,5:1,6:17,9:715,12:36,13:1,16:364,19:210,23:105,
                26:462,30:16,33:1287,36:9,37:18,40:1001,43:120,44:1,47:455,50:462,54:120}
    printed165={0:1,7:3,14:1,31:3,38:4,45:1}
    assert {j:c for j,c in enumerate(forms[500]) if c}==printed500
    assert {j:c for j,c in enumerate(forms[165]) if c}==printed165
    a=[0]*55;a[23]=a[54]=1
    # An integer modulus larger than every coefficient preserves this positive result.
    assert power_x(500,a,1<<128)==forms[500]
    assert power_x(165,a,1<<128)==forms[165]
    g_checks=0
    for n in range(0,300):
        indices=list(range(n+30,n-1,-1))+list(range(n+54,n+30,-1))
        indices2=list(range(n+31,n,-1))+list(range(n+55,n+31,-1))
        g=[forms[i] for i in indices]
        shifted=[g[-1]]+g[:-1]
        shifted[31]=tuple(x+y for x,y in zip(shifted[31],g[-1]))
        assert shifted==[forms[i] for i in indices2]
        g_checks+=1

    rng=random.Random(32231);multiplicative_checks=0
    for e in [3,4,5,8,16,32,64]:
        m=1<<e;zmod=1<<(e-2)
        ys=[rng.randrange(2) for j in range(55)]
        zs=[rng.randrange(zmod) for j in range(55)];zs[0]|=1
        xs=[((-1)**y*pow(3,z,m))%m for y,z in zip(ys,zs)]
        assert any(x%8 in [3,5] for x in xs)
        for n in range(55,2055):
            ys.append((ys[n-24]+ys[n-55])%2)
            zs.append((zs[n-24]+zs[n-55])%zmod)
            xs.append(xs[n-24]*xs[n-55]%m)
            assert xs[n]==((-1)**ys[n]*pow(3,zs[n],m))%m
            assert (zs[n]%2==1)==(xs[n]%8 in [3,5])
            multiplicative_checks+=1
    result=dict(status='passed',lifting_coefficient_vectors=checks,lifting_direct_states=states,
                exceptional_vectors=exceptions,small_signed_trinomials=trinomials,
                degree55_mod8=large,decimation_linear_form_checks=decimation_checks,
                g_shift_linear_form_checks=g_checks,X500_coefficients=printed500,
                X165_coefficients=printed165,multiplicative_exponent_checks=multiplicative_checks)
    (ROOT/'results/lagged-identities.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ALL lagged identities passed;',len(trinomials),'signed primitive trinomials;',
          decimation_checks,'decimations;',multiplicative_checks,'multiplicative checks',flush=True)


if __name__=='__main__':main()
