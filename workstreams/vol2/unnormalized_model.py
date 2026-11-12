"""Exact unnormalized models for4.2.2.

The default preserves the specified number of leading zeros after rounding.
Alternative before_rounding documents the ambiguity of carry handling.
Zero products use(49) with its0 branch; this is an explicit convention.
"""
from fractions import Fraction as Q
from accuracy_model import Arithmetic
from float_model import power


class Unnormalized:
    def __init__(self,b,p,after_rounding=True):
        self.b,self.p,self.after_rounding=b,p,after_rounding
    def val(self,u):return Q(u[1])*power(self.b,u[0]-self.p)
    def leading(self,u):
        F=abs(u[1]);l=0
        while l<self.p and F<self.b**(self.p-l-1):l+=1
        return l
    def delta(self,u):return power(self.b,u[0]-self.p)/2
    def fixed(self,x,e):
        b,p=self.b,self.p
        z=x/power(b,e-p);sgn=-1 if z<0 else 1
        k,r=divmod(abs(z.numerator),z.denominator)
        # AlgorithmN's recommended tie choice, odd bases choose away.
        if 2*r>z.denominator or (2*r==z.denominator and
            (b%2 or (k+b//2)%2==0)):k+=1
        if k>=b**p:
            assert k==b**p;k//=b;e+=1
        return e,sgn*k
    def add(self,u,v):
        e=max(u[0],v[0]);x=self.val(u)+self.val(v)
        if abs(x)>=power(self.b,e):e+=1
        return self.fixed(x,e)
    def mul(self,u,v):return self._product(u,v,False)
    def div(self,u,v):return self._product(u,v,True)
    def _product(self,u,v,division):
        lu,lv=self.leading(u),self.leading(v);L=max(lu,lv)
        if division and not v[1]:raise ZeroDivisionError
        if not u[1] or not v[1]:
            e=u[0]-v[0]-lu+lv+L if division else u[0]+v[0]-min(lu,lv)
            return e,0
        x=self.val(u)/self.val(v) if division else self.val(u)*self.val(v)
        if self.after_rounding:
            e,F=Arithmetic(self.b,self.p-L).encode(x)
            return e+L,F
        e=0;f=abs(x)
        while f>=1:f/=self.b;e+=1
        while f<Q(1,self.b):f*=self.b;e-=1
        return self.fixed(x,e+L)
