"""Outward-rounded slash intervals for TAOCP 4.5.1-16.

Finite endpoints are exact Fraction values. Infinities mark unbounded sides.
A zero-containing divisor returns the whole line with an explicit domain flag.
"""
from fractions import Fraction as F
import math


def value(pair):
    u,a=pair
    return F(u,a) if a else math.copysign(math.inf,u)


def finite_or_infinite(x):
    if isinstance(x,float) and math.isinf(x):return x
    return F(x)


class Interval:
    def __init__(self,fmt,lo,hi=None,domain_issue=False):
        lo=finite_or_infinite(lo)
        hi=lo if hi is None else finite_or_infinite(hi)
        if lo>hi or lo==math.inf or hi==-math.inf:
            raise ValueError('interval must contain a finite point')
        self.format=fmt
        self.lo=lo if lo==-math.inf else value(fmt.bracket(lo)[0])
        self.hi=hi if hi==math.inf else value(fmt.bracket(hi)[1])
        self.domain_issue=domain_issue

    def coerce(self,y):
        if isinstance(y,Interval):
            if y.format is not self.format:raise ValueError('different formats')
            return y
        return Interval(self.format,y)

    def __add__(self,y):
        y=self.coerce(y)
        return Interval(self.format,self.lo+y.lo,self.hi+y.hi,
                        self.domain_issue or y.domain_issue)

    def __neg__(self):
        return Interval(self.format,-self.hi,-self.lo,self.domain_issue)

    def __sub__(self,y):return self+-self.coerce(y)
    def __radd__(self,y):return self+y
    def __rsub__(self,y):return self.coerce(y)-self

    def __mul__(self,y):
        y=self.coerce(y)
        def product(a,b):
            # Limit convention for multiplying sets of finite real values.
            return F(0) if a==0 or b==0 else a*b
        corners=[product(a,b) for a in (self.lo,self.hi) for b in (y.lo,y.hi)]
        return Interval(self.format,min(corners),max(corners),
                        self.domain_issue or y.domain_issue)

    def __rmul__(self,y):return self*y

    def __truediv__(self,y):
        y=self.coerce(y)
        if y.lo<=0<=y.hi:
            return Interval(self.format,-math.inf,math.inf,True)
        def reciprocal(a):return F(0) if a in (-math.inf,math.inf) else 1/a
        inverse=Interval(self.format,reciprocal(y.hi),reciprocal(y.lo),y.domain_issue)
        return self*inverse

    def __rtruediv__(self,y):return self.coerce(y)/self
    def contains(self,x):return self.lo<=x<=self.hi
    def width(self):return self.hi-self.lo
    def record(self):
        return {'lo':str(self.lo),'hi':str(self.hi),'width':str(self.width()),
                'domain_issue':self.domain_issue}
