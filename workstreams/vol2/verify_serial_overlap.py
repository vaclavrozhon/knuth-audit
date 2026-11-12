"""Exact independent checks for TAOCP 3.3.2 H, exercises 15,16,23,24."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import prod
from pathlib import Path
import json
import sys
import sympy as s

ROOT = Path(__file__).resolve().parent
DEST = ROOT/'results/serial-overlap.json'


def words(d,t):
    return list(product(range(d),repeat=t))


def counts(u,t):
    n = len(u)
    return Counter(tuple(u[(i+j)%n] for j in range(t)) for i in range(n))


def maximum_checks():
    cases = 0
    for n in range(1,9):
        for u in product(range(3),repeat=n):
            z = list(u)
            for t in range(2,n+1):
                for j in range(n-t+1):
                    z[j] = max(z[j],z[j+1])
                assert z[:n-t+1] == [max(u[j:j+t]) for j in range(n-t+1)]
                cases += 1
    # Covariance of overlapping maxima threshold indicators, p=x^t=1/2.
    import mpmath as mp
    mp.mp.dps = 40
    inflation = []
    for t in [1,2,3,4,8,16,32]:
        x = mp.power(2,-mp.mpf(1)/t)
        factor = 1+8*sum(x**(t+k)-mp.mpf(1)/4 for k in range(1,t))
        inflation.append(dict(t=t,two_bin_variance_factor=str(factor)))
    return dict(in_place_transformations=cases,overlap_inflation=inflation)


def mixing_checks():
    periods = [u for n in range(1,6) for u in product(range(2),repeat=n)]
    cases = strict = 0
    for u in periods:
        for v in periods:
            for t in range(1,5):
                pu = counts(u,t)
                pv = counts(v,t)
                direct = Counter()
                for i in range(len(u)):
                    for r in range(len(v)):
                        direct[tuple((u[(i+j)%len(u)]+v[(i+r+j)%len(v)])%2
                                     for j in range(t))] += 1
                convolution = Counter()
                for a,na in pu.items():
                    for b,nb in pv.items():
                        convolution[tuple((x+y)%2 for x,y in zip(a,b))] += na*nb
                assert direct == convolution
                prior = sum((Q(pu[a],len(u))-Q(1,2**t))**2 for a in words(2,t))
                after = sum((Q(direct[a],len(u)*len(v))-Q(1,2**t))**2 for a in words(2,t))
                assert after <= prior
                strict += after < prior
                cases += 1
    return dict(period_pair_cases=cases,strict_contractions=strict)


def prob(a,p):
    return prod((p[x] for x in a),start=s.S.One)


def joint(a,b,k,p):
    """Place two words on an integer line, solve shared positions directly."""
    assignments = dict(enumerate(a))
    for j,y in enumerate(b,k):
        if j in assignments and assignments[j] != y:
            return s.S.Zero
        assignments[j] = y
    return prod(p[y] for y in assignments.values())


def kernel(a,b,p):
    return 1/prob(a,p) if a == b else s.S.Zero


def suffix(a,n):
    return a[-n:] if n else ()


def overlap(a,b,k,p):
    t = len(a)
    if k <= 0:
        return kernel(a[:t+k],suffix(b,t+k),p)-1
    return kernel(suffix(a,t-k),b[:t-k],p)-1


def matrices(p,t):
    d = len(p)
    ww = words(d,t)
    pp = [prob(a,p) for a in ww]
    c = s.Matrix(len(ww),len(ww),lambda i,j:
                 sum(joint(ww[i],ww[j],k,p)-pp[i]*pp[j] for k in range(1-t,t)))
    bar = s.Matrix(len(ww),len(ww),lambda i,j:
                   kernel(ww[i],ww[j],p)-kernel(ww[i][:-1],ww[j][:-1],p))
    transform = s.Matrix(len(ww),len(ww),lambda i,j:
                         int(i==j)-p[ww[i][-1]]*int(ww[i][:-1]==ww[j][:-1]))
    h = s.Matrix(len(ww),len(ww),lambda i,j:
                 prob(ww[i][:-1],p)*(p[ww[i][-1]]*int(i==j)-p[ww[i][-1]]*p[ww[j][-1]])
                 if ww[i][:-1]==ww[j][:-1] else 0)
    return ww,pp,c,bar,transform,h


def covariance_checks():
    rows = []
    models = [(s.Rational(1,2),)*2,(s.Rational(1,3),s.Rational(2,3)),
              (s.Rational(1,3),)*3,(s.Rational(1,6),s.Rational(1,3),s.Rational(1,2))]
    for p in models:
        for t in range(1,6 if len(p)==2 else 4):
            ww,pp,c,bar,l,h = matrices(p,t)
            assert c*bar*c == c,(p,t)
            rank = len(p)**t-len(p)**(t-1)
            assert c.rank() == rank
            assert l*c*l.T == h
            diag = s.diag(*[1/x for x in pp])
            assert l.T*diag*l == bar
            assert h*diag*h == h
            for k in range(1-t,t):
                for i,a in enumerate(ww):
                    for j,b in enumerate(ww):
                        assert joint(a,b,k,p)-pp[i]*pp[j] == pp[i]*pp[j]*overlap(a,b,k,p)
            if t==5 and len(p)==2:
                a,b = (0,1,1,0,1),(1,0,1,0,1)
                example = p[0]**4*p[1]**6*(1/(p[0]*p[1])+1/(p[0]*p[1]**2)+1/p[1]-9)
                assert c[ww.index(a),ww.index(b)] == example
            rows.append(dict(p=list(map(str,p)),t=t,rank=rank,
                             covariance_identity=True,innovation_covariance=True))
    return rows


def cyclic_checks():
    cases = 0
    rows = []
    specs = [(2,t,n) for t in range(1,5) for n in range(max(3,2*t-1),min(9,2*t+2)+1)]
    specs += [(3,t,n) for t in range(1,4) for n in range(max(3,2*t-1),min(7,2*t+1)+1)]
    for d,t,n in specs:
        weights = list(range(1,d+1))
        denom = sum(weights)**n
        p = tuple(s.Rational(w,sum(weights)) for w in weights)
        ww,pp,c,bar,l,h = matrices(p,t)
        index = {a:i for i,a in enumerate(ww)}
        first = [0]*len(ww)
        second = [[0]*len(ww) for _ in ww]
        for u in product(range(d),repeat=n):
            ns = counts(u,t)
            short = counts(u,t-1)
            weight = prod(weights[x] for x in u)
            active = [(index[a],v) for a,v in ns.items()]
            for i,x in active:
                first[i] += weight*x
                for j,y in active:
                    second[i][j] += weight*x*y
            original = sum(ns[a]**2/pp[i] for i,a in enumerate(ww))
            original -= sum(value**2/prob(a,p) for a,value in short.items())
            residual = sum((ns[a]-p[a[-1]]*short[a[:-1]])**2/pp[i]
                           for i,a in enumerate(ww))
            assert original == residual
            cases += 1
        assert first == [denom*n*x for x in pp]
        exact = s.Matrix(len(ww),len(ww),lambda i,j:
                         s.Rational(second[i][j],denom)-n*n*pp[i]*pp[j])
        assert exact == n*c
        rows.append(dict(d=d,t=t,n=n,words=d**n))
    return dict(sequences=cases,models=rows)


def telescoping_checks():
    rows = []
    for d,t in [(2,1),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3)]:
        p = tuple(s.Rational(w,d*(d+1)//2) for w in range(1,d+1))
        ww,pp,c,bar,l,h = matrices(p,t)
        tt = {k:s.Matrix(len(ww),len(ww),lambda i,j:overlap(ww[i],ww[j],k,p))
              for k in range(1-t,t)}
        kh = {k:tt[k]*h for k in tt}
        total = s.zeros(len(ww))
        for k in tt:
            for ell in tt:
                got = kh[k]*tt[ell]
                if k>0 or ell<0:
                    assert got.is_zero_matrix
                else:
                    width = min(t+k,t-ell)
                    def corrected(a,b):
                        aa = suffix(a,width-k)
                        bb = suffix(b,width+ell)
                        return kernel(aa[:width],bb[:width],p)-kernel(aa[:width-1],bb[:width-1],p)
                    want = s.Matrix(len(ww),len(ww),lambda i,j:corrected(ww[i],ww[j]))
                    assert got == want,(d,t,k,ell)
                total += got
        assert total == sum((tt[k] for k in tt),s.zeros(len(ww)))
        rows.append(dict(d=d,t=t,lag_pairs=(2*t-1)**2,entries=len(ww)**2))
    return rows


def main():
    out = json.loads(DEST.read_text()) if '--resume' in sys.argv and DEST.exists() else {}
    for name,fn in [('maximum',maximum_checks),('mixing',mixing_checks),
                    ('covariances',covariance_checks),('cyclic',cyclic_checks),
                    ('telescoping',telescoping_checks)]:
        if name in out:
            continue
        print('START',name,flush=True)
        out[name] = fn()
        DEST.write_text(json.dumps(out,indent=2)+'\n')
        print('PASS',name,flush=True)
    print('ALL BLOCKS COMPLETE',flush=True)


if __name__ == '__main__':
    main()
