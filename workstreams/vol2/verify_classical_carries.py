#!/usr/bin/env python3
"""Carry PGFs, column carry asymptotics42, complement example and rounding43."""
from collections import Counter
from fractions import Fraction as F
from itertools import product,permutations
from math import comb,factorial
from pathlib import Path
import argparse,json,random,time
import sympy as s
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/classical-carries.json'


def pgf():
    b,z,t=s.symbols('b z t');den=b-(1+b)*(1+z)*t/2+z*t*t;G=(b-z*t)/den
    first=-t/den+t*(b-z*t)*(b+1-2*t)/(2*den**2)
    second=-t*t*(b+1-2*t)/den**2+t*t*(b-z*t)*(b+1-2*t)**2/(2*den**3)
    partial1=t/2*(1/(1-t)**2-1/((b-1)*(1-t))+1/((b-1)*(b-t)))
    partial2=t*t/2*(1/(1-t)**3-1/((b-1)**2*(1-t))+1/((b-1)**2*(b-t))+1/((b-1)*(b-t)**2))
    assert s.factor(s.diff(G,z)-first)==0
    assert s.factor(s.diff(G,z,2)-second)==0
    assert s.factor(first.subs(z,1)-partial1)==0
    assert s.factor(second.subs(z,1)-partial2)==0
    assert s.factor(G.subs(z,1)-1/(1-t))==0
    # Distinct from the earlier mean-only checks: exact joint distributions
    # of total carries and final carry, including their second moments.
    results=[]
    for B,n in [(2,6),(3,3),(4,3),(5,2),(7,2),(10,2)]:
        hist=Counter()
        for U,V in product(range(B**n),repeat=2):
            x,y=U,V;c=K=0
            for _ in range(n):
                x,a=divmod(x,B);y,d=divmod(y,B);c=(a+d+c)//B;K+=c
            hist[K,c]+=1
        dp={(0,0):1}
        for _ in range(n):
            new=Counter()
            for (K,c),count in dp.items():
                for a,d in product(range(B),repeat=2):
                    e=(a+d+c)//B;new[K+e,e]+=count
            dp=new
        assert hist==dp
        total=B**(2*n);mean=sum(F(k*v,total) for (k,c),v in hist.items())
        var=sum(F(k*k*v,total) for (k,c),v in hist.items())-mean**2
        mu=F(1,2)*(n-F(1,B-1)*(1-F(1,B**n)))
        variance=F(1,4)*(n+F(2*n,B-1)-F(2*B+1,(B-1)**2)+F(2*B+2,(B-1)**2*B**n)-F(1,(B-1)**2*B**(2*n)))
        assert mean==mu and var==variance
        # Coefficients of the rational GF by its second-order recurrence.
        polys=[s.Integer(1),(B+1+(B-1)*z)/(2*B)]
        for j in range(2,n+1):polys.append(s.expand((B+1)*(1+z)*polys[-1]/(2*B)-z*polys[-2]/B))
        expected=sum(s.Rational(v,total)*z**k for (k,c),v in hist.items())
        assert s.expand(polys[n]-expected)==0
        results.append({'b':B,'n':n,'pairs':total,'mean':str(mean),'variance':str(var),'joint_histogram':{str(key):v for key,v in sorted(hist.items())}})
    return {'symbolic_identities':5,'joint_distributions':results}


def stirling1(m,k):
    row=[1]
    for j in range(1,m+1):row=[(j-1)*(row[k] if k<len(row) else 0)+(row[k-1] if k else 0) for k in range(j+1)]
    return row[k]


def column():
    cases=[];total=0
    for N in [2,3,4,5,8]:
        for m in range(1,6):
            h=Counter(sum(xs)//N for xs in product(range(N),repeat=m));total+=N**m
            for k in range(m):
                count=sum((-1)**r*comb(m+1,r)*comb(N*(k+1-r)+m-1,m) for r in range(k+1))
                exact=sum(F(stirling1(m,m-j),factorial(m)*N**j)*sum((-1)**r*comb(m+1,r)*(k+1-r)**(m-j) for r in range(k+1)) for j in range(m+1))
                assert count==h[k] and exact==F(count,N**m)
            cases.append({'N':N,'m':m,'counts':dict(h)})
    euler=[]
    for m in range(1,9):
        h=Counter(sum(p[i]<p[i+1] for i in range(m-1)) for p in permutations(range(m)))
        for k in range(m):assert h[k]==sum((-1)**r*comb(m+1,r)*(k+1-r)**m for r in range(k+1))
        euler.append({'m':m,'ascent_counts':dict(h)})
    return {'complete_tuples':total,'distributions':cases,'Eulerian_permutation_checks':euler,'corrected_sign':'(-1)^r, published erratum2024'}


def complements_rounding():
    top=int('11011111',2);low1=int('1111110',2);low0=int('1101011',2)
    example=(top-256)*128**2+low1*128+low0
    assert example==-2**21+int('1011111',2)*2**14+low1*2**7+low0==-524437
    rng=random.Random(431276)
    for _ in range(5000):
        bits=rng.randrange(2,65);B=2**bits;M=B-1
        x,y=rng.randrange(B),rng.randrange(B)
        signed=lambda z:z if z<B//2 else z-B
        assert (x+y)%B==(signed(x)+signed(y))%B
        end=(x+y)%B+(x+y)//B
        assert 0<=end<=M and end%M==(x+y)%M
    for u,v in product(range(256),repeat=2):
        p=u*v;t=p+128;w=(t+t//256)//256
        q,r=divmod(p,255);assert w==q+(r>=128)
        assert w==(257*t)//65536 and t+t//256<65536
    return {'complement_example':example,'bit_pattern_pairs':5000,'gray_product_pairs':65536,'maximum_gray_intermediate':65025+128+(65025+128)//256}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    if OUT.exists() and not args.resume:raise SystemExit('Use --resume')
    data=json.loads(OUT.read_text()) if OUT.exists() else {'scope':'4.3.1 pp.276-278 and42/43','blocks':{}}
    for name,fn in [('PGF',pgf),('column42',column),('complement43',complements_rounding)]:
        if name in data['blocks']:continue
        t=time.monotonic();r=fn();r['elapsed_seconds']=time.monotonic()-t;data['blocks'][name]=r
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,'PASS',flush=True)
    print('ALL CHECKPOINTS COMPLETE',flush=True)
if __name__=='__main__':main()
