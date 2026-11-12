"""Exact checks of 4.2.2 basic laws, comparisons, and exercises 1--16/32.

Proofs are in notes/accuracy-basic.md. Successful blocks are checkpointed.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from accuracy_model import Arithmetic,relations
from float_model import power,value
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/accuracy-basic.json'


def examples():
    a=Arithmetic(10,8);out={}
    u,v,w=map(Q,['11111113','-11111111','7.5111111'])
    ans=[a.add(a.add(u,v),w),a.add(u,a.add(v,w))]
    assert ans==list(map(Q,['9.5111111','10']));out['nonassociative_add']=list(map(str,ans))
    u,v,w=map(Q,['20000','-6','6.0000003'])
    ans=[a.add(a.mul(u,v),a.mul(u,w)),a.mul(u,a.add(v,w))]
    assert ans==[Q('0.01'),Q('.006')];out['nondistributive']=list(map(str,ans))
    u,v,w=map(Q,['8.0000001','1.2500008','8.0000008'])
    ans=[a.mul(a.mul(u,v),w),a.mul(u,a.mul(v,w))]
    assert ans==list(map(Q,['80.000064','80.000057']));out['exercise3']=list(map(str,ans))
    ans=[a.div(9,9),a.mul(9,a.div(1,9))]
    assert ans==[1,Q('.99999999')];out['exercise5']=list(map(str,ans))
    a=Arithmetic(2,6);u=Q(33,64);v=Q(34,64)
    x=a.mul(a.add(u,v),a.add(u,v));y=2*a.add(a.mul(u,u),a.mul(v,v))
    assert x>y;out['exercise7']=dict(u=str(u),v=str(v),left=str(x),right=str(y))
    # Exercise8: apply the 1999 corrections, including exponent28 for zero.
    rows=[((1,31415927),(1,31416000)),((0,99997000),(1,10000039)),
          ((24,60221400),(27,60221)),((24,60221400),(31,6)),((24,60221400),(28,0))]
    got=[relations(u,v,10,8,Q(1,10000)) for u,v in rows]
    assert [r['essential'] for r in got]==[True,True,True,False,False]
    assert all(r['similar'] and not r['less'] and not r['greater'] for r in got)
    out['exercise8']=got
    u,v,w=(0,50),(1,5),(1,6)
    assert relations(u,v,10,2,Q(1,100))['essential']
    assert relations(v,w,10,2,Q(1,100))['essential']
    assert not relations(u,w,10,2,Q(2,100))['essential']
    out['exercise9']=dict(u=u,v=v,w=w,epsilon='1/100')
    # 4.2.2-10: truncate raw p fractional places BEFORE normalization.
    # u=8/9 < v=1, w=5/9; the raw products use different exponents.
    left=Q((Q(8,9)*Q(5,9)*9).__floor__(),9)
    right=3*Q((Q(1,3)*Q(5,9)*9).__floor__(),9)
    assert left==Q(4,9)>right==Q(1,3)
    out['exercise10']=dict(radix=3,precision=2,u='8/9',v='1',w='5/9',left=str(left),right=str(right))
    return out


def relative_bounds():
    count=equalities=0
    for b,p in product(range(2,11),range(1,4)):
        a=Arithmetic(b,p);eps=power(b,1-p)/2
        # Exact nodes, both sides of midpoints, and midpoint ties, including
        # crossing the upper power-of-b boundary. Reflection covers negatives.
        for k,t in product(range(b**(p-1),b**p),[Q(0),Q(1,3),Q(1,2),Q(2,3)]):
            x=(k+t)*power(b,-p);r=a.R(x);rho=abs(x-r)
            assert rho<=eps*min(x,r),(b,p,x,r)
            if rho==eps*min(x,r):equalities+=1
            assert rho/x<eps
            count+=1
    return dict(cases=count,equalities_in_2026_nonstrict_bound=equalities)


def zero_boundary():
    rows=[]
    for b in [2,3,10,64,100]:
        p=4;q=b//2;u=(0,0);v=(0,b**(p-1));eps=Q(1,b)
        rel=relations(u,v,b,p,eps,q)
        x,y=value(u,b,p,q),value(v,b,p,q)
        assert rel['essential'] and eps<1
        assert abs(x-y)>b*eps*abs(x)
        assert not relations(u,v,b,p,eps/2,q)['essential']
        rows.append(dict(b=b,p=p,q=q,u=u,v=v,epsilon=str(eps),difference=str(y)))
    return dict(finding='V2-C0083',counterexamples=rows,
                repair='For (36), require nonzero u,v, or replace epsilon<1 by epsilon<1/b.')


def reciprocal_and_divisibility():
    rows=[];ct=0
    for b,p in product(range(2,11),range(1,5)):
        a=Arithmetic(b,p);u=1-power(b,-p)
        r=a.div(1,a.div(1,u))
        if b+p>4:assert r!=u,(b,p,u,r)
        else:
            for f in range(b**(p-1),b**p):
                x=Q(f,b**p);assert a.div(1,a.div(1,x))==x
        rows.append(dict(b=b,p=p,u=str(u),double_reciprocal=str(r)))
    for b,p in [(b,p) for b in range(2,7) for p in [1,2,3]]:
        a=Arithmetic(b,p)
        for m,n in product(range(2*b**(p-1)+1),range(1,b**p)):
            r=a.div(m,n);assert (r.denominator==1)==(m%n==0),(b,p,m,n,r)
            ct+=1
    # Odd-radix ties are not prescribed by AlgorithmN. The b3,p1 exception
    # works for away/even ties but not odd ties; do not silently universalize.
    a=Arithmetic(3,1,'odd');u=Q(2,3)
    assert a.div(1,a.div(1,u))==1!=u
    return dict(reciprocals=rows,divisibility_cases=ct,
                odd_radix_caveat='b3,p1 double reciprocal depends on unresolved tie convention; odd ties send2/3 to1.')


def sum_constant_integer(x,n,p=8,unit_power=-7):
    """Positive decimal fixed-unit integer engine, independent of Arithmetic.R."""
    assert x.denominator and x*10**(-unit_power)==int(x*10**(-unit_power))
    inc=int(x*10**(-unit_power));s=0;grid=1;limit=10**p
    transitions=[]
    for k in range(1,n+1):
        raw=s+inc
        while raw>=limit:grid*=10;limit*=10
        z,r=divmod(raw,grid)
        if 2*r>grid or (2*r==grid and z%2):z+=1
        s=z*grid
        if s>=limit:grid*=10;limit*=10
        if not transitions or transitions[-1][1]!=grid:
            transitions.append([k,grid,str(Q(s)*power(10,unit_power))])
    return Q(s)*power(10,unit_power),transitions


def welford():
    a=Arithmetic(10,8);n=10**6;x=Q('1.1111111')
    s,transitions=sum_constant_integer(x,n)
    assert s==Q('1109099.1')
    expected={10:'11.111111',91:'101.11110',901:'1001.1102',9001:'10001.020',90009:'100000.91',900819:'1000000.0'}
    assert {k:v for k,grid,v in transitions if k in expected}=={k:str(Q(v)) for k,v in expected.items()}
    x2=a.mul(x,x);assert x2==Q('1.2345679')
    s2,trans2=sum_constant_integer(x2,n)
    assert s2==Q('1224782.1')
    variance=a.div(a.sub(a.mul(n,s2),a.mul(s,s)),a.mul(n,n-1))
    assert variance==Q('-.0053187053'),variance
    # Welford is exact for constant input: M1=x,S1=0, later differences0.
    m=a.add(0,a.div(a.sub(x,0),1));S=a.add(0,a.mul(a.sub(x,0),a.sub(x,m)))
    assert m==x and S==0
    for k in [2,3,1000000]:
        m=a.add(m,a.div(a.sub(x,m),k));S=a.add(S,a.mul(a.sub(x,m),a.sub(x,m)))
        assert m==x and S==0
    # Exhaustive representative finite checks of the inward midpoint update.
    count=0;midpoint_failures=[]
    for b,p in [(2,1),(2,3),(3,2),(4,2),(10,2)]:
        ar=Arithmetic(b,p);fs=sorted({b**(p-1),b**(p-1)+1,b**p//2,b**p-2,b**p-1})
        vals=sorted({Q(0)}|{sign*f*power(b,e-p) for f,e,sign in product(fs,[-2,0,2],[-1,1]) if b**(p-1)<=f<b**p})
        for u,v in product(vals,repeat=2):
            for k in [2,3,7,1000]:
                m=ar.add(u,ar.div(ar.sub(v,u),k))
                assert min(u,v)<=m<=max(u,v),(b,p,u,v,k,m)
                count+=1
            mid=ar.div(ar.add(u,v),2)
            if b==2:assert min(u,v)<=mid<=max(u,v)
            elif not min(u,v)<=mid<=max(u,v) and not any(r['b']==b for r in midpoint_failures):
                midpoint_failures.append(dict(b=b,p=p,u=str(u),v=str(v),midpoint=str(mid)))
    return dict(n=n,sum=str(s),sum_squares=str(s2),variance_formula14=str(variance),
                exponent_transitions=transitions,square_transitions=trans2,
                welford_constant_variance=0,inward_updates_checked=count,
                midpoint_counterexamples=midpoint_failures)


def round_even_formula():
    cases=0
    for x in [Q(i,16) for i in range(-320,321)]+[Q(i,2) for i in range(-50,51)]:
        k,r=divmod(x.numerator,x.denominator)
        target=k+(2*r>x.denominator or (2*r==x.denominator and k%2==1))
        for shift in range(-3,4):
            b=Q(1,4)+shift;z=x/2+b;t=x/2-b
            got=z.__floor__()+t.__ceil__();assert got==target
            cases+=1
    return dict(cases=cases,all_solutions='a=1/2, b mod1=1/4',proof='notes/accuracy-basic.md')


def ternary_midpoint_boundary():
    vals=sorted({Q(0)}|{sign*f*power(3,e) for sign,f,e in product([-1,1],[1,2],range(-4,5))})
    count=0
    for tie in ['away','even']:
        a=Arithmetic(3,1,tie)
        for u,v in product(vals,repeat=2):
            mid=a.div(a.add(u,v),2)
            assert min(u,v)<=mid<=max(u,v)
            count+=1
    a=Arithmetic(3,1,'odd');assert a.div(a.add(2,2),2)==1
    return dict(finding='V2-C0084',cases=count,radix=3,precision=1,
                rules_satisfying_midpoint_property=['away','even'],
                odd_tie_failure=dict(u=2,v=2,computed_midpoint=1))


if __name__=='__main__':
    out=json.loads(OUT.read_text()) if OUT.exists() else {}
    for name in ['examples','relative_bounds','zero_boundary','reciprocal_and_divisibility','welford','round_even_formula','ternary_midpoint_boundary']:
        if name in out:continue
        out[name]=globals()[name]();OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
        print('PASS',name,flush=True)
