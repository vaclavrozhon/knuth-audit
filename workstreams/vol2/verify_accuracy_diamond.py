"""Exact rational checks of Diamond's identity AND the new secant/gap proof.

The general proof is in notes/accuracy-diamond.md. This finite family is only
an implementation cross-check; no floating point evaluations of f or g occur.
"""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from pathlib import Path
import json
from accuracy_model import Arithmetic
from float_model import power
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/accuracy-diamond.json'


def gaps(ar,x):
    if not x:return Q(0),Q(0)
    e,m=ar.encode(abs(x)); step=power(ar.b,e-ar.p)
    left=step/ar.b if m==ar.b**(ar.p-1) else step
    return (left,step) if x>0 else (step,left)


def lemma(ar,a,c,u,v,f,g):
    assert a<c and u<v and a and v
    L,_=gaps(ar,a);M,_=gaps(ar,c);T,_=gaps(ar,v)
    D=c-a;E=v-u;alpha=g(u);beta=g(v);fa=f(a)
    assert alpha<a<beta
    assert a-alpha<=L/2 and beta-a>=D-M/2>0
    assert E>=T and fa>=v-T/2
    slopes=[(2*E-T)/L,(fa-u)/(a-alpha),(v-fa)/(beta-a),T/(2*D-M)]
    assert slopes[0]<=slopes[1]<slopes[2]<=slopes[3]
    assert 2*D-M<L
    _,right=gaps(ar,a)
    assert 2*D-M>=right and L>right and a<0
    e,m=ar.encode(-a);assert m==ar.b**(ar.p-1)
    return list(map(str,[a,c,u,v]+slopes))


def orbit(ar,A,C,K,x):
    if x==C:return None
    side=1 if x>C else -1
    f=lambda t:A-K/(t-C)
    g=lambda t:C+K/(A-t)
    xs=[x];ys=[];roundings=[]
    for _ in range(3):
        if not side*(xs[-1]-C)>0:return None
        fx=f(xs[-1]);y=ar.R(fx)
        # Range on this branch: y<A for x>C, and y>A for x<C.
        if not -side*(y-A)>0:return None
        gy=g(y);z=ar.R(gy)
        assert g(fx)==xs[-1] and f(gy)==y
        roundings.extend([(fx,y),(gy,z)])
        ys.append(y);xs.append(z)
    for t,z in roundings:
        lo,hi=gaps(ar,z);assert z-lo/2<=t<=z+hi/2
    assert (xs[0]<=xs[1]<=xs[2]<=xs[3] or xs[0]>=xs[1]>=xs[2]>=xs[3])
    if ar.b**ar.p>=3:assert xs[3]==xs[2],(ar.b,ar.p,ar.ties,A,C,K,x,xs,ys)
    count=0;examples=[]
    direction=1 if xs[1]>=xs[0] else -1
    xx=[direction*t for t in xs];yy=[direction*t for t in ys]
    ff=lambda t:direction*f(direction*t)
    gg=lambda t:direction*g(direction*t)
    curvature=-side*direction
    for k in [1,2]:
        if curvature>0:
            a,c,u,v=xx[k],xx[k+1],yy[k-1],yy[k];fun,inv=ff,gg
        else:
            a,c,u,v=yy[k-1],yy[k],xx[k-1],xx[k];fun,inv=gg,ff
        if a<c and u<v:
            examples.append(lemma(ar,a,c,u,v,fun,inv));count+=1
    return xs,ys,count,examples,curvature,direction


def check(b,p,tie):
    ar=Arithmetic(b,p,tie);B=b**(p-1);N=b**p
    starts=sorted({Q(0)}|{sgn*m*power(b,e) for sgn,m,e in product([-1,1],range(B,N),range(-2,2))})
    # All starts in the declared four bins; the parameter family is finite.
    params=list(product([Q(-b),Q(0),Q(b)],[Q(-b),Q(0),Q(b)],[Q(1),Q(7,2)]))
    params += [(Q(115),Q(97),Q(35)),(Q(-115),Q(-97),Q(35))]
    counts=Counter();examples={}
    for A,C,K in params:
        for x in starts:
            r=orbit(ar,A,C,K,x)
            if r is None:counts['outside_domain']+=1;continue
            xs,ys,n,lemmas,curv,direction=r;counts['valid']+=1;counts['lemma_applications']+=n
            counts['two_changes']+=xs[2]!=xs[1]
            counts['three_changes']+=xs[3]!=xs[2]
            counts['zero_start']+=x==0
            counts['zero_last']+=xs[-1]==0
            for lm in lemmas:examples.setdefault(f'curvature{curv}_direction{direction}',lm)
            if xs[3]!=xs[2]:examples.setdefault('bp2_exception',dict(params=list(map(str,[A,C,K])),xs=list(map(str,xs)),ys=list(map(str,ys))))
    return dict(counts=counts,proof_examples=examples,parameters=len(params),starts=len(starts))


if __name__=='__main__':
    out=json.loads(OUT.read_text()) if OUT.exists() else {}
    formats=[(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2),(5,1),(10,1),(10,2)]
    for b,p in formats:
        for tie in ['book','even','odd','away']:
            key=f'b{b}_p{p}_{tie}'
            if key not in out:
                out[key]=check(b,p,tie);OUT.write_text(json.dumps(out,indent=2)+'\n');print('PASS',key,out[key]['counts'],flush=True)
    if 'decimal_example' not in out:
        ar=Arithmetic(10,2);r=orbit(ar,Q(115),Q(97),Q(35),Q(110));assert r[0]==[110,100,99,99]
        out['decimal_example']=dict(xs=list(map(str,r[0])),ys=list(map(str,r[1])),lemma=r[3]);OUT.write_text(json.dumps(out,indent=2)+'\n');print('PASS decimal_example',flush=True)
