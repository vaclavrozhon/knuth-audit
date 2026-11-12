"""Independent symbolic checks of Kahan's error recurrence and calculator example."""
from fractions import Fraction as Q
from pathlib import Path
from decimal import Decimal,localcontext
import json
import sympy as S
from accuracy_model import Arithmetic
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/accuracy-compensation.json'


def kahan():
    f,g,x,eta,sigma,gamma,delta=S.symbols('f g x eta sigma gamma delta')
    y=(x-g)*(1+eta);s=(f+g+y)*(1+sigma)
    c=((s-f-g)*(1+gamma)-y)*(1+delta)
    z=S.expand(s-c)
    A=1-gamma*sigma-delta*sigma-gamma*delta*sigma
    B=gamma-eta+gamma*delta+gamma*eta+gamma*delta*eta+gamma*eta*sigma+delta*eta*sigma+gamma*delta*eta*sigma
    C=sigma*(1+gamma)*(1+delta)
    D=-(1+delta)*(gamma+gamma*eta+eta*sigma+gamma*eta*sigma)
    F=(1+eta)*(1-gamma-gamma*delta-gamma*sigma-delta*sigma-gamma*delta*sigma)
    G=(1+delta)*(1+eta)*(gamma+sigma+gamma*sigma)
    assert S.expand(z-A*f-B*g-F*x)==0
    assert S.expand(c-C*f-D*g-G*x)==0
    # Independently expand successive direct original operations, retaining degrees0..2.
    t=S.symbols('t');fn=gn=0;degrees=[]
    for k in range(1,9):
        es,ss,gs,ds=S.symbols(f'e{k} s{k} g{k} d{k}')
        et,st,gt,dt=[v*t for v in [es,ss,gs,ds]]
        yy=((1 if k==1 else 0)-gn)*(1+et)
        sn=(fn+gn+yy)*(1+st)
        cn=((sn-fn-gn)*(1+gt)-yy)*(1+dt)
        def trunc(v):
            p=S.Poly(v,t);return S.expand(sum(p.nth(j)*t**j for j in range(3)))
        fn,gn=trunc(sn-cn),trunc(cn)
        second=S.expand(fn).coeff(t,2)
        count=len(S.Add.make_args(second))
        assert count==(4 if k==1 else 4*k+2)
        degrees.append(dict(n=k,quadratic_monomials=count,quadratic_polynomial=str(second)))
    return dict(matrix=list(map(str,[A,B,C,D])),injection=list(map(str,[F,G])),quadratic_counts=degrees,claim='Printed4n differs from4n+2 for n>=2; asymptotic result unaffected.')


def approximation(x,digits=32):
    with localcontext() as c:
        c.prec=digits
        return str(Decimal(x.numerator)/Decimal(x.denominator))


def calculator():
    y=S.symbols('y');h=-Q(37,20)*y**2-Q(69,20)*y**4
    series=S.Poly(S.expand(sum(S.binomial(107,k+1)*h**k for k in range(4))),y)
    expected=[Q(107),-Q('10491.35'),Q('659749.9625'),-Q('30141386.26625')]
    assert [series.nth(2*k) for k in range(4)]==expected
    rows=[]
    for precision in [8,10,12]:
        a=Arithmetic(10,precision)
        for exponent in [3,4,5,6]:
            y=Q(1,10**exponent);Y2=a.mul(y,y)
            ztrue=(Q(1,3)-y*y)*(3+Q(69,20)*y*y)
            z=a.mul(a.sub(a.div(1,3),Y2),a.add(3,a.mul(Q(69,20),Y2)))
            ref=(1-ztrue**107)/(1-ztrue)
            # Compare exact final-power rounding with separately rounded repeated squares.
            correctly_rounded_power=a.R(z**107)
            acc=Q(1);cur=z;n=107
            while n:
                if n&1:acc=a.mul(acc,cur)
                n//=2
                if n:cur=a.mul(cur,cur)
            den=a.sub(1,z)
            quotient=None if den==0 else a.div(a.sub(1,correctly_rounded_power),den)
            squared=None if den==0 else a.div(a.sub(1,acc),den)
            horner=Q(1)
            for _ in range(106):horner=a.add(a.mul(horner,z),1)
            exact_at_z=sum(z**k for k in range(107))
            rows.append(dict(precision=precision,y=str(y),rounded_argument=str(z),exact_argument=str(ztrue),reference=approximation(ref),quotient=None if quotient is None else str(quotient),squared_power_quotient=None if squared is None else str(squared),horner=str(horner),argument_error=approximation(exact_at_z-ref),quotient_arithmetic_error=None if quotient is None else approximation(quotient-exact_at_z),horner_arithmetic_error=approximation(horner-exact_at_z)))
    return dict(series=list(map(str,expected)),rows=rows,scope='Controlled exact decimal emulations, not observations from physical calculators. Display decimals approximate; all operations/errors computed as Fractions.')


if __name__=='__main__':
    out=json.loads(OUT.read_text()) if OUT.exists() else {}
    for key,fn in [('kahan',kahan),('calculator',calculator)]:
        if key not in out:
            out[key]=fn();OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('PASS',key,flush=True)
