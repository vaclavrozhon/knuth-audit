#!/usr/bin/env python3
"""Containment checks and experiments for outward slash intervals."""
from fractions import Fraction as F
from pathlib import Path
import json
import math
import random
import sys
import time

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'sources'))
from slash_arithmetic import SlashFormat
from slash_intervals import Interval
OUT=ROOT/'results/rational-intervals.json'


def containment():
    rng=random.Random(45116);cases=divisions=0
    for q in [4,8,27,58]:
        fmt=SlashFormat(size=q)
        for _ in range(500):
            a,b=sorted(F(rng.randrange(-1000,1001),rng.randrange(1,1001)) for _ in range(2))
            c,d=sorted(F(rng.randrange(-1000,1001),rng.randrange(1,1001)) for _ in range(2))
            X,Y=Interval(fmt,a,b),Interval(fmt,c,d)
            assert X.contains(a) and X.contains(b) and Y.contains(c) and Y.contains(d)
            for op,oracle in [(lambda:X+Y,lambda x,y:x+y),(lambda:X-Y,lambda x,y:x-y),
                              (lambda:X*Y,lambda x,y:x*y)]:
                z=op()
                for x in (a,(a+b)/2,b):
                    for y in (c,(c+d)/2,d):assert z.contains(oracle(x,y))
                cases+=1
            z=X/Y
            for x in (a,(a+b)/2,b):
                for y in (c,(c+d)/2,d):
                    if y:assert z.contains(x/y);divisions+=1
            if Y.lo<=0<=Y.hi:assert z.domain_issue
    fmt=SlashFormat(size=8)
    whole=Interval(fmt,-math.inf,math.inf)
    assert (whole*0).lo==(whole*0).hi==0
    assert (1/Interval(fmt,-1,1)).domain_issue
    assert (1/Interval(fmt,0)).domain_issue
    assert (Interval(fmt,1,math.inf)*Interval(fmt,-math.inf,-2)).contains(-10000)
    return {'interval_operations':cases,'nonzero_division_samples':divisions,
            'unbounded_and_zero_divisor_checks':4}


def experiments():
    fmt=SlashFormat(size=4);x=F(1,10)
    point=fmt.round(x);assert point==(0,1)
    enclosure=Interval(fmt,x);assert enclosure.contains(x)
    assert enclosure.lo==0 and enclosure.hi==F(1,7)
    rows=[]
    for q in [8,27,58]:
        fmt=SlashFormat(size=q);total=Interval(fmt,0);exact=F(0)
        for n in range(1,101):
            total=total+Interval(fmt,1)/n;exact+=F(1,n)
            assert total.contains(exact)
        # Determinant from the authors' 1988 response, attached 1979 example.
        a,b,c=F(10,13),F(20,17),F(1,13)
        d,e,f=F(11,19),F(7,11),F(77,95)
        g,h,i=F(69,91),F(4,17),F(56,65)
        exactdet=((a*e)*i+(d*h)*c+(g*b)*f)-((g*e)*c+(d*b)*i+(a*h)*f)
        assert exactdet==F(5,13)
        A,B,C,D,E,G,H,I,J=[Interval(fmt,t) for t in (a,b,c,d,e,f,g,h,i)]
        determinant=((A*E)*J+(D*I)*C+(H*B)*G)-((H*E)*C+(D*B)*J+(A*I)*G)
        assert determinant.contains(exactdet)
        dependency=Interval(fmt,F(1,3),F(1,2))
        difference=dependency-dependency
        assert difference.contains(0) and difference.width()>0
        rows.append({'q':q,'harmonic100':total.record(),'determinant':determinant.record(),
                     'dependency_x_minus_x':difference.record()})
    return {'mediant_endpoint_failure':{'exact':'1/10','point_pair':list(point),
                                       'outward':enclosure.record()},'rows':rows,
            'harmonic_exact':str(exact),'determinant_exact':'5/13'}


if __name__=='__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('containment',containment),('experiments',experiments)]:
        if name in data:continue
        start=time.monotonic();v=fn();data[name]={'status':'passed','seconds':time.monotonic()-start,'result':v}
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,json.dumps(data[name]),flush=True)
