"""Integer formulas independent of MIX instruction execution; b radix, eight digits.

A value is (biased exponent, nonnegative fraction integer, sign). The sign of
its low storage word is immaterial. Normalized zero has exponent and integer0.
"""
from fractions import Fraction


def power(b,e):return Fraction(b**e) if e>=0 else Fraction(1,b**-e)

def value(b,u):
    e,F,s=u
    return s*F*power(b,e-b*b//2-8) if F else Fraction(0)

def normalize(b,n,places,e,sign=1):
    if not n:return (0,0,sign),None
    assert n>0
    # n/b**places, with exponent e, is the unnormalized magnitude.
    while n>=b**places:places+=1;e+=1
    while n<b**(places-1):n*=b;e-=1
    if places>8:F=n//b**(places-8)
    else:F=n*b**(8-places)
    assert b**7<=F<b**8
    return (e,F,sign),10 if e<0 else 20 if e>=b*b else None

def model(b,u,v,op,improved=False):
    eu,U,su=u;ev,V,sv=v
    if op=='DFSUB':sv=-sv;op='DFADD'
    if op=='DFADD':
        if (ev,V)>(eu,U):eu,ev,U,V,su,sv=ev,eu,V,U,sv,su
        d=eu-ev;extra=int(improved)
        # Saturate huge shifts without constructing enormous denominators.
        aligned=0 if d>10 else V*b**extra//b**d
        n=U*b**extra+su*sv*aligned
        assert n>=0
        return normalize(b,n,8+extra,eu,su)
    W=b**5;Um,Ul=U//b**3,(U%b**3)*b*b;Vm,Vl=V//b**3,(V%b**3)*b*b
    if op=='DFMUL':
        p=10 if improved else 9
        n=Um*Vm//b**(10-p)+Um*Vl//b**(15-p)+Vm*Ul//b**(15-p)
        return normalize(b,n,p,eu+ev-b*b//2,su*sv)
    assert op=='DFDIV'
    if not V:return None,30
    a_num=U;a_den=b**4*Vm
    q10=a_num*b**10//a_den
    q5=a_num*b**5//a_den
    r5=Vl*b**5//(b*Vm)
    n=q10-q5*r5//b**4
    return normalize(b,n,10,eu-ev+b*b//2+1,su*sv)
