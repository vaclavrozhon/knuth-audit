#!/usr/bin/env python3
"""Exact constructions and independent checks for TAOCP4.6.3-38."""
from datetime import datetime,timezone
from itertools import combinations
from math import isqrt,prod
from pathlib import Path
import argparse,json,time
import mpmath as mp
import sympy as sp
from verify_powers_vector import yao

BASE=Path(__file__).resolve().parent
RESULT=BASE/'results/powers-squares.json'

def primes_to(n):
    sieve=bytearray(b'\1')*(n+1);sieve[:2]=b'\0\0'
    for p in range(2,isqrt(n)+1):
        if sieve[p]:sieve[p*p::p]=b'\0'*((n-p*p)//p+1)
    return [i for i,x in enumerate(sieve) if x]


def constructor_block():
    primes=[2,3,5,7,11,13];precomputed={};counts=[]
    for r in range(1,7):
        k=prod(primes[:r]);residues=sorted({a*a%k for a in range(k)})
        expected=2*prod((p+1)//2 for p in primes[1:r])
        assert len(residues)==expected
        # Direct residue enumeration is independent of the CRT count.
        prog,outs,_=yao(residues[1:]+[k],max(1,(k.bit_length()-1).bit_length()-1))
        precomputed[r]=(k,residues,prog)
        counts.append(dict(r=r,k=k,residues=expected,precomputation_steps=len(prog.pairs)))
    cases=0;steps=0;examples=[]
    for m in list(range(1,65))+[127,256,1024,4096]:
        choices=range(1,5) if m<=64 else [4,5,6]
        for r in choices:
            k,residues,prog=precomputed[r]
            if k>m*m and m>1:continue
            values=[v[0] for v in prog.values];pairs=prog.pairs[:];where={v:i for i,v in enumerate(values)}
            pre=len(pairs)
            def add(a,b):
                if a==0:return b
                if b==0:return a
                assert a in where and b in where
                c=a+b
                if c not in where:
                    pairs.append((where[a],where[b]));where[c]=len(values);values.append(c)
                return c
            q=m*m//k
            for a in range(2,q+1):add((a-1)*k,k)
            middle=len(pairs)
            assert middle-pre<=max(0,q-1)
            for a in range(1,m+1):
                d,t=divmod(a*a,k)
                assert t in residues
                assert add(d*k,t)==a*a
            assert len(pairs)-middle<=m
            for i,(a,b) in enumerate(pairs,1):assert a<i and b<i and values[i]==values[a]+values[b]
            assert all(a*a in where for a in range(1,m+1))
            assert len(pairs)<=pre+max(0,q-1)+m
            if m<=32:
                available={1}
                for a in sorted(x for x in values if x<=m*m)[1:]:
                    assert any(a-b in available for b in available)
                    available.add(a)
                assert all(a*a in available for a in range(1,m+1))
            cases+=1;steps+=len(pairs)
            if m>=1024:examples.append(dict(m=m,r=r,k=k,steps=len(pairs),precomputation=pre,multiples=q))
    return dict(residue_tables=counts,constructed_cases=cases,validated_additions=steps,examples=examples)


def graph_block():
    universe=[a for a in range(1,21) if isqrt(a)**2!=a]
    n=len(universe);adj=[];tau=[0]*41
    for a in range(1,41):
        for b in range(a,41,a):tau[b]+=1
    for i,a in enumerate(universe):
        adj.append(sum(1<<j for j,b in enumerate(universe) if i!=j and isqrt(a+b)**2==a+b))
    pairchecks=0
    for i,j in combinations(range(n),2):
        common=adj[i]&adj[j];assert common.bit_count()<=tau[abs(universe[i]-universe[j])]
        seen=set()
        for z in range(n):
            if common>>z&1:
                a=isqrt(universe[i]+universe[z]);b=isqrt(universe[j]+universe[z])
                assert (a-b)*(a+b)==universe[i]-universe[j]
                assert (a-b,a+b) not in seen;seen.add((a-b,a+b))
        pairchecks+=1
    T=max(tau);cases=0
    for mask in range(1<<n):
        selected=[i for i in range(n) if mask>>i&1];k=len(selected)
        deg=[(adj[i]&mask).bit_count() for i in selected];twice_edges=sum(deg)
        wedges=sum(d*(d-1)//2 for d in deg)
        assert wedges<=T*k*(k-1)//2
        # Cauchy-Schwarz, in integer form; yields the K_{2,T+1} edge bound.
        assert twice_edges*twice_edges<=k*(2*wedges+twice_edges)
        # Every common square neighbor is independently described by factors.
        cases+=1
    # A square of a prime3mod4 cannot be the sum of two positive squares.
    primes=[p for p in primes_to(1000) if p%4==3];nonsplit=0
    for p in primes:
        for a in range(1,p):
            b2=p*p-a*a;assert isqrt(b2)**2!=b2
        nonsplit+=1
    return dict(universe=universe,all_subsets=cases,common_neighbor_pairs=pairchecks,divisor_bound=T,prime_square_obstructions=nonsplit)


def parameters_block():
    mp.iv.dps=80;mp.mp.dps=80;ln2=mp.iv.ln(2);rows=[];required=set()
    for j in range(4,21):
        t=(2**j)*ln2;u=mp.iv.ln(t)
        variants={'printed':(1+ln2/(2*j))*t/u,
                  'natural_denominator_only':(1+ln2/(2*u))*t/u,
                  'corrected':(1+(1+ln2/2)/u)*t/u}
        selected={}
        for name,value in variants.items():
            lo=int(mp.mpf(value._mpi_[0]));hi=int(mp.mpf(value._mpi_[1]));assert lo==hi
            selected[name]=lo;required.add(lo)
        rows.append(dict(j=j,m_power_of_two=2**j,r=selected))
    primes=primes_to(1000000);assert len(primes)>max(required);k=1;table={}
    for i,p in enumerate(primes[:max(required)],1):
        k*=p
        if i in required:table[i]=k
    for row in rows:
        exponent=row['m_power_of_two'];m=1<<exponent;t=exponent*ln2;u=mp.iv.ln(t);details={}
        for name,r in row['r'].items():
            k=table[r];q=m*m//k
            normalized=(mp.iv.ln(k)-t)*u/t
            details[name]=dict(r=r,largest_prime=primes[r-1],primorial_bits=k.bit_length(),multiples_bits=q.bit_length(),normalized_logk_minus_logm=str(normalized))
            if name=='printed':assert k<m and q>m
        row['details']=details
    # Symbolic substitution in p_r=r(log r+log log r-1+...).
    x,a=sp.symbols('x a',positive=True)
    ratio=(1+a*x)*(1+x*sp.log(1+a*x)+x*sp.log(1+x*sp.log(x)+x*sp.log(1+a*x))-x)
    expansion=sp.series(ratio,x,0,2)
    assert sp.simplify(expansion.removeO()-1-(a-1)*x)==0
    return dict(interval_precision_decimal_digits=80,examples=rows,symbolic_expansion=str(expansion),
                printed_alpha='(ln(2))^2/2',printed_logk='log(m)+(alpha-1)*log(m)/log(log(m))+o(log(m)/log(log(m)))',
                conclusion='Printed parameter yields more than m multiples before the m square targets. Corrected asymptotic choice uses coefficient1+ln(2)/2 and natural-log denominator.')

BLOCKS={'constructor':constructor_block,'graph':graph_block,'parameters':parameters_block}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('block',choices=BLOCKS);arg=ap.parse_args()
    out=json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert arg.block not in out['blocks'],'A completed block requires a specific new reason to rerun.'
    start=time.perf_counter();data=BLOCKS[arg.block]()
    out['blocks'][arg.block]=dict(status='passed',seconds=time.perf_counter()-start,data=data,completed_at_utc=datetime.now(timezone.utc).isoformat())
    RESULT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(arg.block,'PASSED',out['blocks'][arg.block]['seconds'],flush=True)
