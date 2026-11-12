"""Exact checks for 4.2.2-22/27/29/31; general proofs live in the notes.

Checkpointed per block; successful results are not recomputed on resume.
"""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
import json
from accuracy_model import Arithmetic
from float_model import power
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/accuracy-iterations.json'


def nearest(x,tie):
    k,r=divmod(x.numerator,x.denominator)
    return k+int(2*r>x.denominator or (2*r==x.denominator and
        (tie=='up' or (tie=='even' and k%2) or (tie=='odd' and not k%2))))


def reciprocal_integer():
    count=0
    for K,m,tie in product([Q(k,d) for d in [1,2,3] for k in range(1,161)],range(1,65),['up','down','even','odd']):
        n=nearest(K/m,tie)
        if not n:continue
        l=nearest(K/n,tie)
        if not l:continue
        r=nearest(K/l,tie)
        assert r==n,(K,m,tie,n,l,r)
        if m*m<=K:assert l==m,(K,m,tie,n,l)
        count+=1
    return dict(cases=count,K='1..160 divided by1,2,3',m='1..64',ties=['up','down','even','odd'])


def format_checks(b,p,tie):
    a=Arithmetic(b,p,tie);N=b**p;B=N//b;mul=rec=0
    for u,v in product(range(B,N),repeat=2):
        xs=[Q(u)]
        for k in range(6):xs.append(a.mul(xs[-1],v) if k%2==0 else a.div(xs[-1],v))
        assert xs[2]==xs[4]==xs[6] and xs[3]==xs[5],(b,p,tie,u,v,xs)
        mul+=1
    for m,e,sign in product(range(B,N),range(-2,4),[-1,1]):
        u=sign*m*power(b,e-p)
        a1=a.div(1,u);a2=a.div(1,a1);a3=a.div(1,a2)
        assert a3==a1,(b,p,tie,u,a1,a2,a3)
        rec+=1
    return dict(multiplication_pairs=mul,reciprocal_cases=rec)


def decimal_witness():
    a=Arithmetic(10,2);xs=[Q(19)]
    for k in range(6):xs.append(a.mul(xs[-1],55) if k%2==0 else a.div(xs[-1],55))
    assert xs==[19,1000,18,990,18,990,18]
    return dict(sequence=list(map(str,xs)),largest_changing_subscript=1)


def binary_concave():
    # R((2**e)**(99/100))=2**k is equivalent to the exact comparisons
    # (3/4)**100*2**(100*k) <= 2**(99*e) < (3/4)**100*2**(100*(k+1)).
    # None of the cases is a midpoint; no transcendental numerics are needed.
    def rounded_power_exponent(e,num,den):
        t=power(2,num*e);c=Q(3,4)**den
        k=(num*e)//den
        while t<c*power(2,den*k):k-=1
        while t>=c*power(2,den*(k+1)):k+=1
        assert c*power(2,den*k)<t<c*power(2,den*(k+1))
        return k
    es={e:rounded_power_exponent(rounded_power_exponent(e,99,100),100,99) for e in range(42,59)}
    assert all(t==e-1 for e,t in es.items()),es
    return dict(exponents=es,witness_orbit_exponents=[44,43,42,41],method='Exact integer/rational 100th/99th power comparisons; no floating logarithms.')


def pell_example():
    pm2,pm1,qm2,qm1=0,1,1,0;convs=[]
    for n in range(40):
        a=1 if n==0 or n%2==1 else 2
        p=a*pm1+pm2;q=a*qm1+qm2
        assert 3*q*q-p*p==2-3*(n%2)
        convs.append(dict(n=n,p=p,q=q,residual=2*p*p+9*q**4-p**4))
        pm2,pm1,qm2,qm1=pm1,p,qm1,q
    x=408855776;y=708158977
    assert (convs[31]['q'],convs[31]['p'])==(x,y)
    assert 2*y*y+9*x**4-y**4==1
    a=Arithmetic(2,53,'even');X=Q(x);Y=Q(y)
    # Explicit straight-line orders; host binary64 is an independent check.
    X2=a.mul(X,X);Y2=a.mul(Y,Y);X4=a.mul(X2,X2);Y4=a.mul(Y2,Y2)
    direct=a.sub(a.add(a.mul(2,Y2),a.mul(9,X4)),Y4)
    alternate=a.add(a.mul(2,Y2),a.mul(a.sub(a.mul(3,X2),Y2),a.add(a.mul(3,X2),Y2)))
    xf=float(x);yf=float(y);x2=xf*xf;y2=yf*yf
    assert Q((2*y2+9*(x2*x2))-(y2*y2))==direct
    assert Q(2*y2+(3*x2-y2)*(3*x2+y2))==alternate
    assert direct==-36893488147419103232 and alternate==1002978273411373056
    assert all(c['residual']==1 for c in convs if c['n']%2)
    return dict(convergents=convs,binary53=dict(direct=str(direct),alternate=str(alternate),exact='1'),operation_order='Squares, then products, then additions/subtraction; all separately rounded, no FMA.')


if __name__=='__main__':
    out=json.loads(OUT.read_text()) if OUT.exists() else {}
    def run(key,fn):
        if key in out:return
        out[key]=fn();OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('PASS',key,flush=True)
    run('reciprocal_integer',reciprocal_integer)
    for b,p in [(b,p) for b in range(2,9) for p in [1,2]]+[(2,3),(2,4),(3,3)]:
        for tie in ['book','even','odd']:
            run(f'format_b{b}_p{p}_{tie}',lambda b=b,p=p,tie=tie:format_checks(b,p,tie))
    run('decimal_witness',decimal_witness)
    run('binary_concave',binary_concave)
    run('pell_example',pell_example)
