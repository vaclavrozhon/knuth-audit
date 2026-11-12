"""Certified restricted partitions and birthday probabilities via pole residues.

The proof of the two explicit error bounds is in notes/partition-certificate.md.
No floating arithmetic is used for the certificates or rounding decisions.
"""
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial, comb, lcm
from pathlib import Path
import json
import sys
import sympy as S
from verify_birthday_spacings import numerator, partition_counts, stirling

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
DEST=ROOT/'results/birthday-table.json'


def ceilq(q):return -((-q.numerator)//q.denominator)


def decimal(q,digits=24):
    with localcontext() as ctx:
        ctx.prec=digits
        return str(Decimal(q.numerator)/Decimal(q.denominator))


class PartitionPolynomial:
    def __init__(self,n,terms=24):
        self.n=n;self.N=n*(n+1)//2
        self.terms=min(terms,(n-1)//2+1)
        f=[Q(1)];logs=[Q(0)]
        for k in range(1,self.terms):
            power=sum(j**(2*k) for j in range(1,n+1))
            B=Q(S.bernoulli(2*k))
            logs.append(-B*power/Q(2*k*factorial(2*k)))
            f.append(sum(j*logs[j]*f[k-j] for j in range(1,k+1))/k)
        assert all((-1)**k*c>0 for k,c in enumerate(f))
        D=lcm(*(q.denominator for q in f));self.divisor=D*2**(n-1)
        self.coeffs=[int(D*b)*(factorial(n-1)//factorial(n-1-2*k))*2**(2*k)
                     for k,b in enumerate(f)]
        self.factor=factorial(n)*factorial(n-1)

    @lru_cache(maxsize=None)
    def scaled(self,m):
        """Approximation of n!(n-1)! times p_n(m)."""
        A=2*m+self.N;v=self.coeffs[0]
        for c in self.coeffs[1:]:v=v*A*A+c
        v*=A**(self.n-1-2*(self.terms-1))
        return Q(v,self.divisor)

    def error(self,lo,hi):
        n=self.n
        assert lo>=4*n*n
        a=Q(2*lo+self.N,2);radius=8*n/a
        assert n*radius/2<=1
        E=Q(n*(n+1)*(2*n+1),6)*radius**2/(24*(1-n*n*radius**2/24))
        assert E<=Q(1,2)
        if self.terms==(n-1)//2+1:
            tail=0
        else:
            tail=ceilq(2*Q(2*hi+self.N,2)**(n-1)/64**self.terms)
        other=0
        for d in range(2,n+1):
            p=n//d
            B=Q(2**n*3**(d+2*p+1),d**(2*p)*factorial(p))*Q(hi,p)**(p-1)
            other+=d*ceilq(B)
        other*=self.factor
        return dict(total=tail+other,truncated_tail=tail,other_roots=other,
                    radius=str(radius),log_product_bound=str(E))


def principal_part(n,m):
    """Independent expansion about z=1 in powers of 1-z (small n only)."""
    series=[Q(1)]+[Q(0)]*(n-1)
    for j in range(1,n+1):
        den=[Q((-1)**h*comb(j,h+1),j) for h in range(min(j,n))]
        inv=[Q(1)]
        for k in range(1,n):inv.append(-sum(den[h]*inv[k-h] for h in range(1,min(k+1,len(den)))))
        series=[sum(series[h]*inv[k-h] for h in range(k+1)) for k in range(n)]
    return sum(series[h]*comb(m+n-h-1,n-h-1) for h in range(n))/factorial(n)


def small_checks():
    rows=[]
    for n in range(2,21):
        model=PartitionPolynomial(n)
        lo=4*n*n;hi=5*n*n+17;dp=partition_counts(n,hi)
        # Use a complete polynomial: only other roots contribute to error.
        # The sine bound is irrelevant when no coefficient tail is truncated.
        other=0
        for d in range(2,n+1):
            p=n//d
            other+=d*ceilq(Q(2**n*3**(d+2*p+1),d**(2*p)*factorial(p))*Q(hi,p)**(p-1))
        for m in (lo,lo+1,lo+17,hi):
            estimate=model.scaled(m)/model.factor
            assert estimate==principal_part(n,m)
            assert abs(estimate-dp[m])<=other
            rows.append(dict(n=n,m=m,difference=str(estimate-dp[m])))
    return dict(models=len(rows),maximum_n=20,rows=rows)


def asymptotic_coefficients():
    x,alpha=S.symbols('x alpha');n=1/x;m=n**3/alpha
    center=m+n*(n+1)/4
    s2=n*(n+1)*(2*n+1)/6
    s4=n*(n+1)*(2*n+1)*(3*n*n+3*n-1)/30
    logpref=S.series((n-1)*S.log(1+alpha*(x+x*x)/4)-alpha/4,x,0,3).removeO()
    pref=S.series(S.exp(logpref),x,0,3).removeO()
    correction=1-s2*(n-1)*(n-2)/(24*center**2)
    correction+=(s2*s2/S.Integer(1152)+s4/S.Integer(2880))*(n-1)*(n-2)*(n-3)*(n-4)/center**4
    obtained=S.expand(S.series(pref*S.series(correction,x,0,3).removeO(),x,0,3).removeO())
    book=1-S.Rational(13,288)*alpha**2*x+(169*alpha**4+2016*alpha**3-1728*alpha**2-41472*alpha)*x*x/165888
    assert S.expand(obtained-book)==0
    q=book.subs(alpha,-alpha)
    return dict(p=str(S.collect(obtained,x)),q=str(S.collect(q,x)),
                normalization='n!(n-1)! p_n(n^3/alpha) / ((n^3/alpha)^(n-1) exp(alpha/4))',
                remainder_proof='notes/partition-certificate.md')


def table():
    n=512;m=2**25;out=[];models={};bounds={}
    for j in (509,510,511,512):
        model=PartitionPolynomial(j);models[j]=model
        bounds[j]=model.error(m-model.N,m)
        print('CERTIFIED MODEL',j,flush=True)
    def positive(j,r):
        model=models[j];num=numerator(j,r)
        value=sum(c*model.scaled(m-e) for e,c in num.items())
        error=sum(abs(c) for c in num.values())*bounds[j]['total']
        return value,error
    probabilities=[]
    for r in range(3):
        value=Q(0);error=Q(0);parts=[]
        for s in range(r+2):
            j=n-s;v,e=positive(j,r+1-s if s else r)
            weight=stirling(n,j);value+=weight*v;error+=weight*e
            parts.append(dict(zero_spacings=s,contribution=decimal(weight*v/m**(n-1)),
                              error=decimal(weight*e/m**(n-1))))
        value/=m**(n-1);error/=m**(n-1);probabilities.append((value,error))
        out.append(dict(r=r,decimal=decimal(value),lower=str(value-error),upper=str(value+error),
                        error=decimal(error),zero_spacing_contributions=parts))
        print('PROBABILITY',r,decimal(value),'ERROR',decimal(error),flush=True)
    rest=1-sum(v for v,e in probabilities);resterror=sum(e for v,e in probabilities)
    out.append(dict(r='>=3',decimal=decimal(rest),lower=str(rest-resterror),upper=str(rest+resterror),error=decimal(resterror)))
    printed=['.368801577','.369035243','.183471182','.078691997']
    for row,s in zip(out,printed):
        row['printed']=s
        row['printed_rounding_agrees']=Q(s)-Q(1,2*10**9)<Q(row['lower'])<=Q(row['upper'])<Q(s)+Q(1,2*10**9)
    model=models[n];q=model.scaled(m-model.N)/model.factor
    err=Q(bounds[n]['total'],model.factor);scale=10**1514
    normalized=q/scale;normalized_error=err/scale
    quoted=Q('7.080693469590264094')
    # The book prints a prefix followed by dots, not an explicit rounding rule.
    prefix_agrees=quoted<=normalized-normalized_error<normalized+normalized_error<quoted+Q(1,10**18)
    cert=dict(m=m,n=n,terms=24,probabilities=out,
              q=dict(exponent10=1514,decimal=decimal(normalized,35),lower=str(normalized-normalized_error),
                     upper=str(normalized+normalized_error),printed_prefix_agrees=prefix_agrees),
              method='Exact rational truncated principal part; positive-coefficient tail and all other roots bounded separately.',
              model_error_summaries={str(j):{k:(decimal(Q(v,m**(j-1))) if isinstance(v,int) else v)
                                           for k,v in bounds[j].items()} for j in models})
    return cert


def auxiliary_identities():
    z,t=S.symbols('z t');g=-1+z/(1-z)
    rows=[]
    # n=m=1; start with the exact rational first Euler derivative.
    for j in range(1,7):
        if j>1:g=S.cancel(z*S.diff(g,z))
        actual=S.series(g.subs(z,S.exp(-t)),t,0,4).removeO().expand()
        printed=-int(j==1)+S.factorial(j)/t**j
        repaired=-int(j==1)+S.factorial(j-1)/t**j
        correction=sum(S.ff(l,j)*S.bernoulli(l)*(-1)**l*t**(l-j)/(l*S.factorial(l))
                       for l in range(j,j+4))
        printed+=(-1)**j*correction;repaired-=(-1)**j*correction
        assert S.expand(actual-repaired)==0
        assert S.expand(actual-printed)!=0
        rows.append(dict(j=j,actual=str(actual),printed=str(S.expand(printed))))
    reciprocal=[]
    for n in range(1,11):
        D=S.prod(1-z**k for k in range(1,n+1))
        assert S.cancel(1/D.subs(z,1/z)-(-1)**n*z**(n*(n+1)//2)/D)==0
        reciprocal.append(n)
    for m in range(1,50):
        pnegative=Q(-m,2)+Q(3,4)+Q((-1)**m,4)
        qpositive=(m-1)//2
        assert qpositive==-pnegative
    return dict(euler_derivatives=rows,
                bernoulli_convention='B1=+1/2, including the global2021 change and page569 substitutions',
                c3_leading='c3 = 1/(3 sqrt(n)) + O(n^(-9/2)) for m=n^3/alpha, fixed positive alpha; see proof note',
                reciprocal_generating_functions=reciprocal,
                reciprocity_counterexample=dict(n=2,m=3,q='1',p_quasipolynomial_at_negative_m='-1'))


def printed_approximation():
    n=512;m=2**25;alpha=Q(4)
    bracket=1-13*alpha**2/(288*n)+(169*alpha**4-2016*alpha**3-1728*alpha**2+41472*alpha)/(165888*n*n)
    prefactor=Q(m**(n-1),factorial(n)*factorial(n-1)*10**1514)*bracket
    upper=sum(Q((-1)**j,factorial(j)) for j in range(81))
    lower=upper-Q(1,factorial(81))
    lo=prefactor*lower;hi=prefactor*upper;quoted=Q('7.080693501')
    assert quoted-Q(1,2*10**9)<lo<hi<quoted+Q(1,2*10**9)
    return dict(exponent10=1514,decimal=decimal((lo+hi)/2),lower=str(lo),upper=str(hi),
                printed='7.080693501',printed_rounding_agrees=True,
                distinction='This certifies evaluation of the printed three-term asymptotic approximation, not its error relative to exact q.')


def main():
    out=json.loads(DEST.read_text()) if '--resume' in sys.argv and DEST.exists() else {}
    for name,fn in [('small',small_checks),('asymptotic',asymptotic_coefficients),('table',table),
                    ('auxiliary',auxiliary_identities),('printed_approximation',printed_approximation)]:
        if name in out:continue
        print('START',name,flush=True);out[name]=fn()
        DEST.write_text(json.dumps(out,indent=2)+'\n');print('PASS',name,flush=True)
    print('ALL BLOCKS COMPLETE',flush=True)


if __name__=='__main__':main()
