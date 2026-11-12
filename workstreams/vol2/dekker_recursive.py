"""Literal recursive interpretation of TAOCP4.2.3-9, with exact comparisons.

Level0 is binary rounding, level1 a pair, level2 a pair of pairs. This is
an investigation model, not an assumed correct quadruple-precision package.
"""
from fractions import Fraction as Q
from accuracy_model import Arithmetic


def val(x):return sum((val(a) for a in x),Q(0)) if isinstance(x,tuple) else x

def neg(x):return tuple(neg(a) for a in x) if isinstance(x,tuple) else -x

def flatten(x):return sum((flatten(a) for a in x),[]) if isinstance(x,tuple) else [str(x)]


class Recursive:
    def __init__(self,p,ties='even'):
        self.ar=Arithmetic(2,p,ties);self.p=p;self.count=0;self.trace=[]
    def encode(self,x,level):
        if level==0:return self.ar.R(x)
        h=self.encode(x,level-1);return h,self.encode(x-val(h),level-1)
    def add(self,x,y,level):
        if level==0:
            self.count+=1
            return self.ar.add(x,y)
        u,ut=x;v,vt=y
        if abs(val(u))<abs(val(v)):u,v,ut,vt=v,u,vt,ut
        low=level-1
        w=self.add(u,v,low)
        r=self.add(self.add(u,neg(w),low),v,low)
        s=self.add(self.add(r,vt,low),ut,low)
        z=self.add(w,s,low)
        zz=self.add(self.add(w,neg(z),low),s,low)
        self.trace.append({'level':level,'u':flatten(u),'ut':flatten(ut),'v':flatten(v),'vt':flatten(vt),'w':flatten(w),'r':flatten(r),'s':flatten(s),'z':flatten(z),'zz':flatten(zz),'head_sum_residual_error':str(val(w)+val(r)-val(u)-val(v)),'last_residual_error':str(val(z)+val(zz)-val(w)-val(s))})
        return z,zz
