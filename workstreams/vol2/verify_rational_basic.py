#!/usr/bin/env python3
"""Exact, independent checks for TAOCP 4.5.1, text and exercises 1--9,11."""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json,random,sys,time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/rational-basic.json'

def norm(a,b):
    if not b:raise ZeroDivisionError
    g=gcd(a,b)*(1 if b>0 else -1)
    return a//g,b//g

def mul(x,y):
    u,a=x;v,b=y;d=gcd(u,b);e=gcd(a,v)
    return (u//d)*(v//e),(a//e)*(b//d)

def divide(x,y):
    u,a=x;v,b=y
    if not v:raise ZeroDivisionError
    d=gcd(u,v);e=gcd(a,b)
    return (u//d)*(b//e)*(1 if v>0 else -1),abs((a//e)*(v//d))

def add(x,y,s=1):
    u,a=x;v,b=y;d=gcd(a,b)
    t=u*(b//d)+s*v*(a//d);e=gcd(t,d)
    return (t//e,(a//d)*(b//e)),(d,t,e)

def check(x,y):
    u,a=x;v,b=y;xx=F(u,a);yy=F(v,b)
    assert (u*b<a*v)==(xx<yy)
    assert gcd(u*v,a*b)==gcd(u,b)*gcd(a,v)
    z=mul(x,y);assert z==( (xx*yy).numerator,(xx*yy).denominator )
    for sign in [-1,1]:
        z,(d,t,e)=add(x,y,sign);q=xx+sign*yy
        assert z==(q.numerator,q.denominator)
        assert gcd(u*b+sign*v*a,a*b)==d*e
        assert gcd(t,d)==gcd(t%d,d)
    if v:
        z=divide(x,y);q=xx/yy;assert z==(q.numerator,q.denominator)
    else:
        try:divide(x,y)
        except ZeroDivisionError:pass
        else:raise AssertionError('zero divisor')

def arithmetic():
    vals=sorted({norm(u,a) for a in range(1,16) for u in range(-16,17)})
    count=0
    for x in vals:
        for y in vals:check(x,y);count+=1
    rng=random.Random(451)
    for _ in range(1000):
        check(norm(rng.randrange(-2**512,2**512),rng.randrange(1,2**512)),
              norm(rng.randrange(-2**512,2**512),rng.randrange(1,2**512)))
    assert add((7,66),(17,12))==((67,44),(6,201,3))
    assert add((17,120),(-27,70))==((-41,168),(10,-205,5))
    return {'small_pairs':count,'large_pairs':1000,'large_operand_bits':512,
            'text_example':[67,44],'exercise5':[-41,168]}

def maximum():
    rows=[];pairs=0
    for N in range(2,17):
        vals=[(u,a) for a in range(1,N) for u in range(N) if gcd(u,a)==1]
        best=-1;witness=None
        for x in vals:
            for y in vals:
                t=add(x,y)[1][1];pairs+=1
                if t>best:best=t;witness=[x,y]
        want=2 if N==2 else (N-1)**2+(N-2)**2
        assert best==want,(N,best,witness)
        rows.append({'N':N,'maximum':best,'witness':witness})
    assert rows[0]['maximum']!=1
    return {'pairs':pairs,'rows':rows,'C0113':'N=2 requires maximum2, not1'}

def fingerprints():
    cases=0;max_per_n=[]
    for n in range(1,9):
        seen={};ct=0
        for a in range(1,2**n):
            for u in range(-a,a+1):
                x=F(u,a);finger=(2**(2*n)*u)//a
                if finger in seen:assert seen[finger]==x
                else:seen[finger]=x
                ct+=1
        cases+=ct;max_per_n.append([n,len(seen)])
    assert (128//13)==(128//14) and F(1,13)!=F(1,14)
    return {'cases':cases,'distinct_by_n':max_per_n,'short_fingerprint_collision':[9,9]}

def qnorm(a,b,c):
    if not c:raise ZeroDivisionError
    g=gcd(gcd(a,b),c)*(1 if c>0 else -1)
    return a//g,b//g,c//g

def qmul(x,y):
    a,b,c=x;d,e,f=y
    return qnorm(a*d+5*b*e,a*e+b*d,c*f)

def qdiv(x,y):
    a,b,c=x;d,e,f=y
    if d==e==0:raise ZeroDivisionError
    return qnorm((a*d-5*b*e)*f,(b*d-a*e)*f,c*(d*d-5*e*e))

def quadratic():
    rng=random.Random(45111);count=0
    for _ in range(4000):
        x=qnorm(rng.randrange(-10000,10001),rng.randrange(-10000,10001),rng.randrange(1,10001))
        y=qnorm(rng.randrange(-10000,10001),rng.randrange(-10000,10001),rng.randrange(1,10001))
        if y[:2]==(0,0):continue
        z=qdiv(x,y);assert qmul(z,y)==x
        # Independent coefficient oracle over the rational basis (1,sqrt(5)).
        a,b,c=x;d,e,f=y;den=F(d*d-5*e*e,f*f)
        A=(F(a,c)*F(d,f)-5*F(b,c)*F(e,f))/den
        B=(F(b,c)*F(d,f)-F(a,c)*F(e,f))/den
        assert (F(z[0],z[2]),F(z[1],z[2]))==(A,B)
        count+=1
    assert qdiv((1,0,1),(1,1,1))==(-1,1,4)
    return {'exact_divisions':count,'example_inverse_1_plus_sqrt5':[-1,1,4]}

def extended_op(op,x,y):
    # Explicit dispatch is part of this extension, before the finite routines.
    undef=(0,0);zero=(0,1)
    if x==undef or y==undef:return undef
    a,b=x;c,d=y
    sx=1 if a>0 else -1 if a<0 else 0
    sy=1 if c>0 else -1 if c<0 else 0
    if op=='-':return extended_op('+',x,(-c,d))
    if op=='+':
        if not b and not d:return x if sx==sy else undef
        if not b:return x
        if not d:return y
        return add(x,y)[0]
    if op=='*':
        if not b or not d:return (sx*sy,0) if sx*sy else undef
        return mul(x,y)
    if op=='/':
        if (not b and not d) or (not a and not c):return undef
        if not c:return (sx,0)
        if not b:return (sx*sy,0)
        if not d:return zero
        return divide(x,y)
    raise ValueError(op)

def extended():
    import math
    vals=[(-1,0),(-2,1),(0,1),(2,1),(1,0),(0,0)];count=0
    def val(x):
        a,b=x
        return a/b if b else math.copysign(math.inf,a) if a else math.nan
    for x in vals:
        for y in vals:
            a,b=val(x),val(y)
            for op in ['+','-','*','/']:
                if op=='+':want=a+b
                elif op=='-':want=a-b
                elif op=='*':want=a*b
                elif b==0:want=math.copysign(math.inf,a) if a!=0 and not math.isnan(a) else math.nan
                else:want=a/b
                got=val(extended_op(op,x,y))
                assert (math.isnan(want) and math.isnan(got)) or got==want,(op,x,y,got,want)
                count+=1
    assert extended_op('/',(1,1),(0,1))==(1,0)
    try:divide((1,1),(0,1))
    except ZeroDivisionError:pass
    else:raise AssertionError('literal finite algorithm unexpectedly extended')
    return {'operation_cases':count,'literal_finite_division_by_zero':'raises; special dispatch required'}

if __name__=='__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('arithmetic',arithmetic),('maximum',maximum),('fingerprints',fingerprints),('quadratic',quadratic),('extended',extended)]:
        if name in data:continue
        t=time.monotonic();v=fn();data[name]={'status':'passed','seconds':time.monotonic()-t,'result':v}
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,json.dumps(data[name]),flush=True)
