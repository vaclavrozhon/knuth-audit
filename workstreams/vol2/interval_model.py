"""Directed interval arithmetic, including signed-zero and infinity endpoints.

Only finite nonzero Fractions or the four strings -inf,-0,+0,+inf are endpoints.
The actual value0 is between-0 and+0 and is not itself an endpoint.
"""
from fractions import Fraction as Q
from bisect import bisect_left,bisect_right
from itertools import product
from float_model import power


def key(x):
    if isinstance(x,str):return {'-inf':(-2,0),'-0':(0,0),'+0':(2,0),'+inf':(4,0)}[x]
    return (-1,x) if x<0 else (3,x) if x>0 else (1,Q(0))


def neg(x):return {'-inf':'+inf','+inf':'-inf','-0':'+0','+0':'-0'}[x] if isinstance(x,str) else -x

def sign(x):return (-1 if x.startswith('-') else 1) if isinstance(x,str) else (-1 if x<0 else 1)

def z(x):return isinstance(x,str) and x.endswith('0')

def inf(x):return isinstance(x,str) and x.endswith('inf')

def contains(I,x):return key(I[0])<=key(Q(x))<=key(I[1])

def valid(I):return key(I[0])<key(I[1]) or (I[0]==I[1] and not isinstance(I[0],str) and I[0]!=0)


class Intervals:
    def __init__(self,b,p,emin=-1,emax=1):
        self.b,self.p=b,p
        positives=sorted({Q(F)*power(b,e-p) for e in range(emin,emax+1) for F in range(b**(p-1),b**p)})
        self.finite=sorted([-v for v in positives]+[Q(0)]+positives)
        self.ends=sorted([v for v in self.finite if v]+['-inf','-0','+0','+inf'],key=key)
    def rounded(self,x,up):
        x=Q(x)
        if not x:return '+0' if up else '-0'
        i=bisect_left(self.finite,x) if up else bisect_right(self.finite,x)-1
        if i<0:return '-inf'
        if i>=len(self.finite):return '+inf'
        ans=self.finite[i]
        return ('+0' if x>0 else '-0') if ans==0 else ans
    def upper_add(self,x,y):
        if z(x) and z(y):return '+0' if x==y=='+0' else '-0'
        if z(x):return y
        if z(y):return x
        assert x!='-inf' and y!='-inf'
        if inf(x) or inf(y):return '+inf'
        return self.rounded(x+y,True)
    def lower_add(self,x,y):return neg(self.upper_add(neg(x),neg(y)))
    def upper_mul(self,x,y):
        sg='+' if sign(x)*sign(y)>0 else '-'
        if z(x) or z(y):return sg+'0'
        if inf(x) or inf(y):return sg+'inf'
        return self.rounded(x*y,True)
    def lower_mul(self,x,y):return neg(self.upper_mul(neg(x),y))
    def upper_div(self,x,y):
        sg='+' if sign(x)*sign(y)>0 else '-'
        if z(x) or inf(y):return sg+'0'
        if inf(x) or z(y):return sg+'inf'
        return self.rounded(x/y,True)
    def lower_div(self,x,y):return neg(self.upper_div(neg(x),y))
    def add(self,I,J):return self.lower_add(I[0],J[0]),self.upper_add(I[1],J[1])
    def sub(self,I,J):return self.add(I,(neg(J[1]),neg(J[0])))
    def corner(self,I,J,low,up):
        pairs=list(product(I,J))
        return min((low(x,y) for x,y in pairs),key=key),max((up(x,y) for x,y in pairs),key=key)
    def mul(self,I,J):return self.corner(I,J,self.lower_mul,self.upper_mul)
    def div(self,I,J):
        if contains(J,0):raise ZeroDivisionError
        return self.corner(I,J,self.lower_div,self.upper_div)
