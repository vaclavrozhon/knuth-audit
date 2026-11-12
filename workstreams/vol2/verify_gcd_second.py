#!/usr/bin/env python3
"""Double sums, residue expansions and endpoint checks for4.5.2-30."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,sys,time
import mpmath as mp
import sympy as s

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/gcd-second.json'


def residues():
    e=s.symbols('e');h0,h1,L,X=s.symbols('h0 h1 L X',nonzero=True)
    # Local expansions at s=-1 of h(s), pi/sin(pi*s), the dyadic
    # denominator, and x^-s. No floating numerical differentiation.
    product=(h0+h1*e)*(-1/e)*(1/(L*e)-s.Rational(1,2))*(1-e*X)
    residue=s.expand(product).coeff(e,-1)
    assert s.expand(residue-(h0*X/L+h0/2-h1/L))==0
    rows=[]
    for k in [1,2,3,5,10,20,40,80,160]:
        hat=-sum(F(comb(k-1,r),1-F(1,2**r)) for r in range(1,k))
        extra=-hat-(2**(k-1)-1)
        assert 0<=extra<=2*(F(3,2)**(k-1)-1)
        rows.append(dict(k=k,hat=str(hat),leading_term=str(-hat/F(2**(k+1)-1))))
    return dict(double_pole_residue=str(residue),endpoint_main_terms=rows,
                derivative_points='h prime at -1, for both a and b',
                endpoint_limit='kth term at x=1 is(-1)^k*(1/4+o(1))')


def numerical():
    mp.mp.dps=75;L=mp.log(2);ell=240;K=180;M=14
    twos=[mp.mpf(2)**j for j in range(1,ell+1)]
    cs=[1+1/t for t in twos];ds=[1+t for t in twos]
    weights=[1/t**2 for t in twos]
    a=lambda z:sum(w*mp.power(c,z-1) for c,w in zip(cs,weights))
    b=lambda z:sum(mp.power(d,z-1) for d in ds)
    aprime=lambda z:sum(w*mp.power(c,z-1)*mp.log(c) for c,w in zip(cs,weights))
    bprime=lambda z:sum(mp.power(d,z-1)*mp.log(d) for d in ds)
    azero,bzero=a(0),b(0);aminus,bminus=a(-1),b(-1)
    ap,bp=aprime(-1),bprime(-1)
    assert aprime(1)>ap>0 and bp>0
    apos=[];aneg=[];bneg=[];hat=[]
    for k in range(1,K+1):
        apos.append(a(k));aneg.append(a(-k));bneg.append(b(-k))
        hat.append(-sum(mp.mpf(comb(k-1,r))/(1-mp.power(2,-r)) for r in range(1,k)))
    omega=[2*mp.pi*m/L for m in range(1,M+1)]
    common=[2j*mp.pi/(L*mp.sinh(mp.pi*w)) for w in omega]
    av=[a(-1+1j*w) for w in omega];bv=[b(-1+1j*w) for w in omega]
    # binom(k-1-i*omega,k-1), updated without repeated Gamma calls.
    binoms=[[mp.mpc(1) for w in omega]]
    for k in range(1,K):
        binoms.append([v*(k-1j*w)/k for v,w in zip(binoms[-1],omega)])
    def direct(x):
        p=q=mp.mpf(0)
        for k in range(1,181):
            t=mp.mpf(2)**k
            p+=sum(1/(t*u*(1+u*(1+t*x))) for u in twos)
            q+=sum(1/(t*(1+u+t*x)) for u in twos)
        return p,q
    rows=[]
    for x in [mp.mpf(1)/7,mp.mpf(1)/3,mp.mpf(1)/2]:
        logx=mp.log(x,2);phase=[mp.exp(-1j*w*mp.log(x)) for w in omega]
        A=sum(mp.re(v*c*p) for v,c,p in zip(av,common,phase))
        B=sum(mp.re(v*c*p) for v,c,p in zip(bv,common,phase))
        pk=[sum(mp.re(v*c*p) for v,c,p in zip(row,common,phase)) for row in binoms]
        left1=azero+aminus*x*(logx+mp.mpf('.5'))-ap*x/L+x*A
        left2=bzero+bminus*x*(logx+mp.mpf('.5'))-bp*x/L+x*B
        for k in range(2,K+1):
            fac=mp.power(2,k-1)/(mp.power(2,k-1)-1)*(-x)**k
            left1-=fac*aneg[k-1];left2-=fac*bneg[k-1]
        right1=-sum(apos[k-1]*(-x)**k/(mp.power(2,k+1)-1) for k in range(1,K+1))
        right2=sum((-x)**k/(mp.power(2,k+1)-1)*(logx-hat[k-1]-mp.mpf('.5')-1/(mp.power(2,k+1)-1)+mp.harmonic(k-1)/L+pk[k-1]) for k in range(1,K+1))
        d1,d2=direct(x);i1,i2=direct(1/x)
        errors=[abs(v-w) for v,w in zip([left1,left2,right1,right2],[d1,d2,i1,i2])]
        assert max(errors)<mp.mpf('2e-54'),(x,errors)
        # A separately arranged application of the original operator to G1.
        f=lambda z:sum(1/(t*(1+t*z)) for t in twos)
        g1=lambda z:f(z)-f(1/z)
        op=sum((g1(x/(x+t))-g1(1/(1+t*x)))/t for t in twos[:180])
        g2=d1-i1+d2-i2
        assert abs(op-g2)<mp.mpf('2e-54'),(x,op-g2)
        rows.append(dict(x=mp.nstr(x,20),G2=mp.nstr(g2,40),expansion_errors=[mp.nstr(v,8) for v in errors],operator_error=mp.nstr(abs(op-g2),8)))
    # The endpoint series term is nonzero asymptotically, even after the
    # complete Fourier correction; no omitted-frequency sign assumption.
    endpoint=[]
    for k in [10,20,40,80,160]:
        P=sum(mp.re(v*c) for v,c in zip(binoms[k-1],common))
        term=(-1)**k/(mp.power(2,k+1)-1)*(-hat[k-1]-mp.mpf('.5')-1/(mp.power(2,k+1)-1)+mp.harmonic(k-1)/L+P)
        endpoint.append(dict(k=k,term=mp.nstr(term,30)))
    bound=sum(abs(c)*mp.sqrt(mp.sinh(mp.pi*w)/(mp.pi*w)) for c,w in zip(common,omega))
    return dict(rows=rows,endpoint=endpoint,uniform_periodic_bound_partial=mp.nstr(bound,30),
                a_prime_minus_one=mp.nstr(ap,35),a_prime_plus_one=mp.nstr(aprime(1),35),b_prime_minus_one=mp.nstr(bp,35),
                truncation=dict(dyadic_terms=ell,power_terms=K,Fourier_pairs=M),
                scope='75-digit floating checks; exact derivation and endpoint proof in notes/gcd-second.md.')


if __name__=='__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('residues',residues),('numerical',numerical)]:
        if name in data:continue
        start=time.monotonic();value=fn();data[name]=dict(status='passed',seconds=time.monotonic()-start,result=value)
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,'passed',round(data[name]['seconds'],3),flush=True)
