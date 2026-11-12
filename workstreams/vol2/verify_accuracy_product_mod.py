"""Exact Dekker/Veltkamp operations and the complete modulo-floor criterion."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
import json,random
from accuracy_model import Arithmetic
from float_model import power
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/accuracy-product-mod.json'


def dekker(p):
    a=Arithmetic(2,p);N=2**p;s=(p+1)//2;H=2**(s-1);c=2**s+1
    assert a.R(c)==c
    def split(u):
        up=a.mul(u,c);hi=a.add(a.sub(u,up),up);lo=a.sub(u,hi)
        assert hi+lo==u and N//2<=hi<=N and hi%(2**s)==0 and abs(lo)<=H
        return hi,lo
    if p<=7:pairs=list(product(range(N//2,N),repeat=2))
    else:
        rng=random.Random(4222100+p)
        end=[N//2,N//2+1,N//2+H-1,N-H,N-2,N-1]
        pairs=list(product(end,repeat=2))+[(rng.randrange(N//2,N),rng.randrange(N//2,N)) for _ in range(1000)]
    maxfirst=0;small=[]
    for u,v in pairs:
        uh,ul=split(Q(u));vh,vl=split(Q(v))
        prods=[uh*vh,uh*vl,ul*vh,ul*vl]
        assert all(a.R(z)==z for z in prods)
        w=a.mul(u,v);r=prods[0]-w
        assert a.sub(prods[0],w)==r
        maxfirst=max(maxfirst,abs(r))
        for z in prods[1:]:
            nextr=r+z;assert a.add(r,z)==nextr,(p,u,v,r,z,nextr);r=nextr
        assert w+r==u*v and a.R(r)==r
        if p<=3:small.append(dict(u=u,v=v,uh=str(uh),ul=str(ul),vh=str(vh),vl=str(vl),w=str(w),first_subtraction=str(prods[0]-w),residual=str(r)))
    return dict(cases=len(pairs),exhaustive=p<=7,maximum_first_difference=str(maxfirst),small_precision_cases=small)


def modulo(b,p):
    h=power(b,-p);book=Arithmetic(b,p);even=Arithmetic(b,p,'even')
    cases=fail=0;witness=None
    for m,e,sgn in product(range(b**(p-1),b**p),range(-3,p+2),[-1,1]):
        u=sgn*m*power(b,e-p);flo=u//1;frac=u-flo
        got=book.sub(u,book.R(frac))
        predicted=b%4==0 and -1<u<0 and u%(2*h)==3*h/2
        assert (got!=flo)==predicted,(b,p,u,got,flo,predicted)
        assert even.sub(u,even.R(frac))==flo,(b,p,u,'even')
        cases+=1
        if got!=flo:
            fail+=1
            if witness is None:witness=dict(u=str(u),rounded_fraction=str(book.R(frac)),computed_floor=str(got),true_floor=str(flo))
    return dict(cases=cases,book_rule_failures=fail,witness=witness)


if __name__=='__main__':
    out=json.loads(OUT.read_text()) if OUT.exists() else {}
    def run(key,fn):
        if key not in out:
            out[key]=fn();OUT.write_text(json.dumps(out,indent=2)+'\n');print('PASS',key,out[key]['cases'],flush=True)
    for p in range(2,10):run(f'dekker_p{p}',lambda p=p:dekker(p))
    for b,p in product(range(2,11),range(1,4)):run(f'mod_b{b}_p{p}',lambda b=b,p=p:modulo(b,p))
