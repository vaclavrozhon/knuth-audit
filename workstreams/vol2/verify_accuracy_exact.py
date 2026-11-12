"""Exact identities and counterexamples for 4.2.2 Theorems A--D and 11/12/20.

Theorem proofs are separate from these finite rational checks.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from accuracy_model import Arithmetic
from float_model import power
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/accuracy-exact.json'


def tails():
    cases=0
    for b,p in product(range(2,11),range(1,4)):
        a=Arithmetic(b,p)
        for x,e in product(range(b**(p-1),b**p),range(-1,p+3)):
            unit=power(b,e);rem=x%unit
            ts=[rem] if 2*rem<unit else [rem-unit] if 2*rem>unit else [rem,rem-unit]
            for t in ts:
                assert a.R(x-t)==x-t and a.R(t)==t,(b,p,x,e,t)
                cases+=1
    return dict(cases=cases,claim='Both tail and difference representable; stronger strict-width version proved in notes.')


def identity_format(b,p,tie):
    a=Arithmetic(b,p,tie);N=b**p;cases=large=failC=0;witness=None
    for U,V,d,sign in product(range(N//b,N),range(N//b,N),range(p+4),[-1,1]):
        u=Q(U);v=sign*V*power(b,-d)
        if abs(v)>u:continue
        w=a.add(u,v)
        up=a.sub(w,v);vp=a.sub(w,u);upp=a.sub(w,vp);vpp=a.sub(w,up)
        assert up+vpp==w and upp+vp==w,('A',b,p,tie,u,v,w)
        du=a.sub(u,up);dv=a.sub(v,vpp);res=a.add(du,dv)
        assert du==u-up and dv==v-vpp and res==du+dv,('B substeps',b,p,tie,u,v,w)
        assert w+res==u+v,('B',b,p,tie,u,v,w,res)
        gotC=w+a.add(a.sub(u,w),v)
        fails=gotC!=u+v
        # Exercise20: carry result rounded to exactly2 times the operand binade.
        predicted=v>0 and d==0 and w==2*N
        assert fails==predicted,('Linnainmaa',b,p,tie,u,v,w,fails,predicted)
        if b<=3:assert not fails,('C',b,p,tie,u,v,w)
        if fails:
            failC+=1
            if witness is None:witness=dict(u=str(u),v=str(v),rounded_sum=str(w),computed_reconstruction=str(gotC),exact_sum=str(u+v))
        cases+=1;large+=d>=p
    return dict(cases=cases,large_exponent_gap_cases=large,fast_sum_failures=failC,witness=witness)


def drift_format(b,p,tie):
    a=Arithmetic(b,p,tie);N=b**p;cases=0;failures=[]
    for U,V,d,sign in product(range(N//b,N),range(N//b,N),range(-2,p+3),[-1,1]):
        u=Q(U);v=sign*V*power(b,-d)
        h=lambda x:a.sub(a.add(x,v),v)
        h1=h(u);h2=h(h1)
        if h1!=h2:
            assert (b,p,tie)==(2,1,'odd'),('D unexpected',b,p,tie,u,v,h1,h2)
            failures.append(dict(u=str(u),v=str(v),h1=str(h1),h2=str(h2)))
        cases+=1
    return dict(cases=cases,failures=failures)


if __name__=='__main__':
    out=json.loads(OUT.read_text()) if OUT.exists() else {}
    def save(name,result):
        out[name]=result;OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('PASS',name,result.get('cases'),flush=True)
    if 'tails' not in out:save('tails',tails())
    for b,p in [(b,p) for b in range(2,11) for p in [1,2]]+[(2,3),(3,3)]:
        for tie in ['book']+(['away'] if b in [2,3,4] else []):
            key=f'ABC_b{b}_p{p}_{tie}'
            if key not in out:save(key,identity_format(b,p,tie))
    for b,p in [(b,p) for b in range(2,9) for p in [1,2]]:
        for tie in ['even','odd'] if b%2==0 else ['book']:
            key=f'D_b{b}_p{p}_{tie}'
            if key not in out:save(key,drift_format(b,p,tie))
