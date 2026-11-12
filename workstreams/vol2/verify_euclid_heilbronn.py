#!/usr/bin/env python3
"""Exact representation and uniform-bound checks for TAOCP4.5.3-33/34."""
from pathlib import Path
from fractions import Fraction as F
from math import gcd,isqrt
import json,os,sys,time
from verify_euclid_discrete import cf,steps,divisors,phi,mu,factors

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/euclid-heilbronn.json'
MAX=128

def continuant(a):
    p,q=0,1
    for x in a:p,q=q,x*q+p
    return q

def all_representations():
    strict={};relaxed={};unrestricted={};checks=0;cuts=0;boundary=0
    for n in range(1,MAX+1):
        rs=set();rr=set();gs=set()
        for x in range(2,n):
            for y in range(1,x):
                for xp in range(1,(n-1)//x+1):
                    remainder=n-x*xp
                    if remainder%y:continue
                    yp=remainder//y
                    if not 0<yp<=xp:continue
                    item=(x,xp,y,yp)
                    if yp<xp:gs.add(item)
                    if gcd(x,y)!=1:continue
                    rr.add(item)
                    if yp<xp:rs.add(item)
        assert len(rr)-len(rs)==(n-1)//2
        boundary+=len(rr)-len(rs)
        recovered=set()
        for m in range(1,n//2+1):
            a=cf(m,n);d=gcd(m,n)
            for cut in range(1,len(a)):
                left,right=a[:cut],a[cut:]
                item=(continuant(left),d*continuant(right),continuant(left[:-1]),d*continuant(right[1:]))
                assert item not in recovered
                recovered.add(item);cuts+=1
        assert recovered==rs
        ceiling_count=0
        for y in range(1,(n-1)//2+1):
            for t in range(1,y+1):
                if gcd(t,y)!=1:continue
                tp=1 if y==1 else (n*pow(t,-1,y)-1)%y+1
                ratio=(F(n,y+t)-tp)/y
                ceiling_count+=-((-ratio.numerator)//ratio.denominator)
        assert ceiling_count==len(rr)
        assert sum(steps(m,n) for m in range(n))==(5*n-3)//2+2*len(rs)
        for x,xp,y,yp in rr:
            t=(x-1)%y+1
            assert xp*(y+t)<n and (xp*t-n)%y==0
            recovered_x=t+y*((n-t*xp-1)//(xp*y))
            assert recovered_x==x
            checks+=1
        strict[n]=rs;relaxed[n]=rr;unrestricted[n]=gs
    cache={'max_n':MAX,'strict':{str(n):[list(t) for t in sorted(v)] for n,v in strict.items()},'unrestricted_counts':{str(n):len(v) for n,v in unrestricted.items()}}
    (ROOT/'results/euclid-heilbronn-representations.json').write_text(json.dumps(cache)+'\n')
    return {'max_n':MAX,'relaxed_representations':checks,'strict_cuts':cuts,'boundary_representations':boundary,'all_parts_33':True}

def uniform_counts():
    data=json.loads((ROOT/'results/euclid-heilbronn-representations.json').read_text())
    reps={int(n):v for n,v in data['strict'].items()};gs={int(n):v for n,v in data['unrestricted_counts'].items()}
    hs={n:len(v) for n,v in reps.items()}
    def hd2(n,d):return sum(2*int(x*d<xp)+int(x*d==xp) for x,xp,y,yp in reps[n])
    count_checks=0;ties=0;largest=F(0);worst=None
    inner=[F(0)]
    for y in range(1,isqrt(MAX)+1):
        inner.append(inner[-1]+sum(F(1,y*(y+t)) for t in range(1,y+1) if gcd(t,y)==1))
    for n in range(1,MAX+1):
        assert gs[n]==sum(hs[n//d] for d in divisors(n))
        assert hs[n]==sum(mu(d)*gs[n//d] for d in divisors(n))
        assert gs[n]==sum(hd2(n//d,d) for d in divisors(n))
        for d in range(1,n+2):
            ylimit=isqrt((n-1)//d)
            exact=F(hd2(n,d),2);main=n*inner[ylimit]
            ratio=abs(exact-main)/n
            assert ratio<=4
            if ratio>largest:largest=ratio;worst=[n,d]
            ties+=sum(x*d==xp for x,xp,y,yp in reps[n]);count_checks+=1
    return {'uniform_count_checks':count_checks,'tie_cases':ties,'absolute_error_bound_checked':'4*n, proved independently in notes','largest_error_over_n':str(largest),'worst_n_d':worst,'all_parts_34a':True}

def divisor_identities():
    s={};k={};harm=[F(0)]
    for n in range(1,1025):harm.append(harm[-1]+F(1,n))
    sigma=lambda n:sum(F(1,d) for d in divisors(n))
    for y in range(1,513):
        s[y]=sum(F(y,y+t) for t in range(1,y+1) if gcd(t,y)==1)
        k[y]=y*(harm[2*y]-harm[y])
        assert sum(s[d] for d in divisors(y))==k[y]
        assert sum(mu(y//d)*k[d] for d in divisors(y))==s[y]
        lhs=sum(F(phi(j),j*j) for j in range(1,y+1))
        rhs=sum(F(mu(d),d*d)*harm[y//d] for d in range(1,y+1))
        assert lhs==rhs
    for n in range(1,1025):
        pairs=[(c,d) for c in divisors(n) for d in divisors(n//c)]
        assert sum(F(mu(d),c*d) for c,d in pairs)==1
        assert sum(F(1,c*d) for c,d in pairs)<=sigma(n)**2
        for p in factors(n):
            assert sum(F(mu(d)*factors(c*d).get(p,0),c*d) for c,d in pairs)==0
            lhs=sum(F(mu(d)*factors(c).get(p,0),c*d) for c,d in pairs)
            rhs=sum(F(1,p**j) for j in range(1,factors(n)[p]+1))
            assert lhs==rhs
    return {'harmonic_and_mobius_inputs':512,'final_convolution_inputs':1024,'logarithms':'exact rational coefficient of each ln(p)'}

def main():
    print('PID',os.getpid(),flush=True)
    out=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {'scope':'4.5.3-33/34; general proofs in notes/euclid-heilbronn.md','checkpoints':{}}
    for key,fn in [('representations',all_representations),('uniform_counts',uniform_counts),('divisor_identities',divisor_identities)]:
        if key in out['checkpoints']:print('SKIP',key,flush=True);continue
        start=time.monotonic();out['checkpoints'][key]=fn();OUT.write_text(json.dumps(out,indent=2)+'\n')
        print('PASS',key,round(time.monotonic()-start,3),flush=True)
    print('ALL HEILBRONN CHECKPOINTS PASSED',flush=True)

if __name__=='__main__':main()
