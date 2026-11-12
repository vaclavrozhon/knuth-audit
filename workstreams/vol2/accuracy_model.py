"""Exact, unbounded-exponent arithmetic for the audit of TAOCP 2, 4.2.2.

Only rational inputs/outputs. No host floating point rounding. The validated
4.2.1 normalization model is used after positioning the exact input fraction.
Odd-radix ties default to away from zero; alternative tie rules are explicit.
"""
from fractions import Fraction as Q
from functools import lru_cache
from float_model import normalize, power, value


class Arithmetic:
    def __init__(self, b, p, ties='book'):
        self.b, self.p, self.ties = b, p, ties

    @lru_cache(maxsize=65536)
    def encode(self, x):
        x=Q(x)
        if not x:return (0,0)
        f=x;e=0;b=self.b;p=self.p
        while abs(f)>=1:f/=b;e+=1
        while abs(f)<Q(1,b):f*=b;e-=1
        if self.ties=='book':return normalize(e,f,b,p)[0]
        z=abs(f)*b**p;k,r=divmod(z.numerator,z.denominator)
        if 2*r>z.denominator or (2*r==z.denominator and
            (self.ties=='away' or (self.ties=='even' and k%2) or
             (self.ties=='odd' and not k%2))):k+=1
        if k==b**p:k//=b;e+=1
        return e, k if x>0 else -k

    def R(self, x):return value(self.encode(Q(x)),self.b,self.p)
    def add(self,x,y):return self.R(x+y)
    def sub(self,x,y):return self.R(x-y)
    def mul(self,x,y):return self.R(x*y)
    def div(self,x,y):return self.R(Q(x)/y)


def relations(u,v,b,p,epsilon,q=0):
    x,y=value(u,b,p,q),value(v,b,p,q)
    small=min(power(b,u[0]-q),power(b,v[0]-q))
    big=max(power(b,u[0]-q),power(b,v[0]-q))
    return dict(less=y-x>epsilon*big,similar=abs(x-y)<=epsilon*big,
                greater=x-y>epsilon*big,essential=abs(x-y)<=epsilon*small)
