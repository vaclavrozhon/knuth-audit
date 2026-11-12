#!/usr/bin/env python3
"""Independent transition counts and finite averaging for TAOCP4.5.2-20--22."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json,sys,time
from verify_gcd_basic import binary

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/gcd-bins.json'


def odds(m): return range(1,2) if m==0 else range(2**m+1,2**(m+1),2)
def size(m): return 1 if m==0 else 2**(m-1)
def power(k): return F(2)**k


def table(m,n):
    assert m>=n>=0
    a=Counter()
    def add(key,p):
        assert p>=0,(m,n,key,p)
        if p:a[key]+=p
    if m==n==0:add('stop',F(1))
    elif n==0:
        for t in range(1,m):add((m-t,0),power(-t))
        add((0,0),power(1-m))
    elif m==n:
        for t in range(2,n):
            p=t*power(-t)-5*power(-t-1)+3*power(-2*t)
            add((n-t,n),p);add((n,n-t),p)
        p=n*power(1-n)-power(2-n)+power(2-2*n)
        add((0,n),p);add((n,0),p);add('stop',power(1-n))
    elif m==n+1:
        if n>1:add((n,n),F(1,8))
        for t in range(1,n-1):add((n-t,n),11*power(-t-3)-3*power(-2*t-1))
        if n>1:add((1,n),5*power(-n-1)-3*power(1-2*n))
        add((0,n),3*power(-n)-power(1-2*n))
    else:
        add((m-1,n),F(1,2)-3*power(-m+n-2)-(power(-m-1) if n==1 else 0))
        for t in range(2,n):add((m-t,n),power(-t)+3*power(-m+n-t-1))
        if n>1:add((m-n,n),power(-n)+power(-m))
        add((m-n-1,n),power(-n-1)+power(1-m))
        for t in range(2,m-n):add((m-n-t,n),power(-n-t))
        add((0,n),power(1-m))
    assert sum(a.values())==1,(m,n,a)
    return dict(a)


def ramp_sum(r,h,c):
    """Sum max(2^h*w-c,0) over odd w with floor(log2(w))=r."""
    lo=0 if r==0 else 2**(r-1);hi=2**r-1
    lo=max(lo,(c-2**h)//2**(h+1)+1)
    k=max(0,hi-lo+1)
    return k*(2**h*(lo+hi+1)-c)


def lattice(m,n):
    assert m>=n>=1
    M,N=size(m),size(n);total=M*N;a={}
    thresholds=[(M-2*N,1),(M-N,-1),(2*M-2*N,-1),(2*M-N,1)]
    for r in range(m):
        count=sum(sign*ramp_sum(r,h,c) for h in range(m+1) for c,sign in thresholds)
        assert count>=0
        if count:
            a[(r,n)]=F(count,total)
            if m==n:a[(n,r)]=F(count,total)
    if m==n:a['stop']=F(1,M)
    return a


def transitions():
    count=0;bins=0
    for m in range(11):
        for n in range(m+1):
            hist=Counter()
            for u in odds(m):
                for v in odds(n):
                    count+=1
                    if u==v:hist['stop']+=1;continue
                    d=abs(u-v);w=d//(d&-d);r=w.bit_length()-1
                    hist[(r,n) if u>v else (m,r)]+=1
            got={k:F(v,size(m)*size(n)) for k,v in hist.items()}
            assert got==table(m,n),(m,n,got,table(m,n))
            bins+=1
    big_bins=0
    for m in range(1,49):
        for n in range(1,m+1):
            assert lattice(m,n)==table(m,n),(m,n,lattice(m,n),table(m,n))
            big_bins+=1
    return dict(direct_pairs=count,direct_bins=bins,lattice_bins=big_bins,largest_bit_bin=48)


def fixed_operand():
    records=[];inputs=0
    for v in [1,3,5,7,11,31,63]:
        for m in [6,9,12]:
            parity_sum=0;C=D=0;max_round_error=0
            for u in odds(m):
                inputs+=1;x=u
                for _ in range(m):
                    parity_sum+=x%2;x=(x-v*(x%2))//2
                x=u;rounds=0
                while x>v:
                    x=(x-v*(x%2))//2;rounds+=1
                assert 1<=x<=v
                assert u<=2**rounds*(x+v)-v and 2**rounds*x<=u
                _,s,_=binary(u,v);C+=s['C'];D+=s['D']
                max_round_error=max(max_round_error,abs(rounds-m))
            assert parity_sum==size(m)*(m+1)//2
            records.append(dict(v=v,m=m,mean_C=str(F(C,size(m))),mean_D=str(F(D,size(m))),
                                parity_total=parity_sum,max_abs_rounds_minus_m=max_round_error))
    return dict(inputs=inputs,records=records)


def averaging():
    # Reuse the independently validated full-input census; do not repeat it.
    old=json.loads((ROOT/'results/gcd-basic.json').read_text())['statistics']['result']['exact_distributions']
    means={};odd_pairs=0;records=[]
    for m in range(8):
        for n in range(m+1):
            C=D=0
            for u in odds(m):
                for v in odds(n):
                    _,s,_=binary(u,v);C+=s['C'];D+=s['D'];odd_pairs+=1
            means[m,n]=(F(C,size(m)*size(n)),F(D,size(m)*size(n)))
    for row in old:
        N=row['N'];M=2**N-1;sums=[F(0),F(0)]
        for m in range(N):
            for n in range(m+1):
                weight=(N-m)*(N-n)*size(m)*size(n)*(1 if m==n else 2)
                for i in range(2):sums[i]+=weight*means[m,n][i]
        assert sums[0]==row['sums']['C']
        # Exact extra shifts needed to strip unequal initial powers of two.
        extra=2*(M*(M-N)-sum((2**(N-k)-1)**2 for k in range(1,N)))
        closed=F(4*M*M+(8-6*N)*M-6*N,3)
        assert extra==closed and sums[1]+extra==row['sums']['D']
        records.append(dict(N=N,pairs=M*M,C_sum=int(sums[0]),
                            odd_D_weighted_sum=int(sums[1]),initial_shifts=extra,
                            actual_D_sum=row['sums']['D']))
    assert records[1]['odd_D_weighted_sum']==4 and records[1]['actual_D_sum']==8
    # Exact finite geometric moments, checked through a separate generating function.
    import sympy as s
    z=s.symbols('z');f=1/(1-z);mom1=s.simplify(z*s.diff(f,z));mom2=s.simplify(z*s.diff(mom1,z))
    diagonal=mom2.subs(z,s.Rational(1,4))/4
    off=(mom1.subs(z,s.Rational(1,2))**2-mom2.subs(z,s.Rational(1,4)))/8
    assert diagonal==s.Rational(5,27) and off==s.Rational(11,27)
    return dict(odd_pairs=odd_pairs,records=records,leading_off_diagonal=str(off),leading_diagonal=str(diagonal),
                reused_census='results/gcd-basic.json statistics')


if __name__=='__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('transitions',transitions),('fixed_operand',fixed_operand),('averaging',averaging)]:
        if name in data:continue
        start=time.monotonic();value=fn()
        data[name]=dict(status='passed',seconds=time.monotonic()-start,result=value)
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,'passed',round(data[name]['seconds'],3),flush=True)
