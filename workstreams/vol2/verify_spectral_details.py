"""Additional exact checks for spectral examples, bounds and construction.

Checkpointed blocks; --resume only runs missing blocks. The main table's
shortest-vector computations are reused, not repeated.
"""
import argparse
from fractions import Fraction as Q
from itertools import product
import json
from math import gcd,isqrt
from pathlib import Path
import time
import ast
import subprocess
import shutil
import mpmath as mp
import sympy as sp
from spectral import spectral_s,dot
from spectral_independent import shortest_basis,lcg_basis,reduced_box_minimum
from verify_spectral_table import rounded_interval

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/spectral-details.json'
mp.mp.dps=90;mp.iv.dps=90
PARI=shutil.which('gp') or '/tmp/knuth-vol2-or9kgh/pari-local/usr/bin/gp'


def endpoints(x):
    def convert(v):
        sign,mantissa,exponent,_=v
        return Q((-1)**sign*mantissa)*Q(2)**exponent
    return tuple(map(convert,x._mpi_))


def certify_round(x,printed):
    lo,hi=endpoints(x);a,b=rounded_interval(printed)
    assert a<lo<=hi<b,(printed,str(x))
    return dict(printed=printed,enclosure=[str(lo),str(hi)])


def table_intervals():
    table=json.loads((ROOT/'results/spectral-table.json').read_text())
    assert table['complete']
    proofs=[]
    for line,row in table['rows'].items():
        m=mp.iv.mpf(row['m'])
        for t,d in row['dimensions'].items():
            t=int(t);s=mp.iv.mpf(d['squared'])
            lg=mp.iv.log(s)/(2*mp.iv.log(2))
            merit=mp.iv.pi**(mp.iv.mpf(t)/2)*s**(mp.iv.mpf(t)/2)/(mp.iv.gamma(1+mp.iv.mpf(t)/2)*m)
            proofs.append(dict(line=int(line),dimension=t,
                lg=certify_round(lg,d['corrected_lg']),merit=certify_round(merit,d['printed_merit'])))
    gammas=[mp.iv.sqrt(mp.iv.mpf(4)/3),mp.iv.mpf(2)**(mp.iv.mpf(1)/3),mp.iv.sqrt(2),
            mp.iv.mpf(2)**(mp.iv.mpf(3)/5),(mp.iv.mpf(64)/3)**(mp.iv.mpf(1)/6)]
    bounds=[]
    for t,g,printed in zip(range(2,7),gammas,['3.63','5.92','9.87','14.89','23.87']):
        bounds.append(certify_round(mp.iv.pi**(mp.iv.mpf(t)/2)*g**(mp.iv.mpf(t)/2)/mp.iv.gamma(1+mp.iv.mpf(t)/2),printed))
    return dict(table_checks=len(proofs)*2,table=proofs,upper_bounds=bounds,
                scope='Outward90-decimal interval arithmetic, exact rational endpoints; original row25 lg corrected by1998 erratum. Squared entries use exact integers in main table file.')


def examples():
    table=json.loads((ROOT/'results/spectral-table.json').read_text())
    r=table['rows']['6']['S'];trace=r['trace']
    assert r['values']['2']['euclidean_steps']==6
    initial=next(x for x in trace if x['step']=='S4')
    assert initial['U']==[[-67654,-226,0],[-44190611,191,0],[5793866,33,1]]
    assert initial['V']==[[-191,-44190611,2564918569],[-226,67654,1307181134],[0,0,10**10]]
    steps=[x for x in trace if x['step']=='S5' and x['t']==3]
    expected=[(1,[None,1,4]),(2,[-2,None,0]),(3,[0,3,None]),(1,[None,-10,-1]),
              (2,[-1,None,-6]),(3,[-1,0,None]),(1,[None,0,2]),(2,[0,None,-1]),
              (3,[3,4,None]),(1,[None,0,0]),(2,[-5,None,0]),(3,[1,0,None]),
              (1,[None,-3,-1]),(2,[0,None,0]),(3,[0,0,None])]
    assert [(x['j'],x['q']) for x in steps]==expected
    U=[row[:] for row in initial['U']];V=[row[:] for row in initial['V']]
    for i,q in [(1,1),(2,4)]:
        V[i]=[x-q*y for x,y in zip(V[i],V[0])]
        U[0]=[x+q*y for x,y in zip(U[0],U[i])]
    assert U==[[-21082801,97,4],[-44190611,191,0],[5793866,33,1]]
    assert V==[[-191,-44190611,2564918569],[-35,44258265,-1257737435],[764,176762444,-259674276]]
    final=r['values']['3']
    assert final['U']==[[-1479,616,-2777],[-3022,104,918],[-227,-983,-130]]
    assert final['V']==[[-888874,601246,-2994234],[-2809871,438109,1593689],[-854296,-9749816,-1707736]]
    assert final['z']==[0,0,1]
    decimal=[certify_round(mp.iv.sqrt(4577114792),'67654.37748'),
             certify_round(mp.iv.sqrt(1034718),'1017.21089')]
    a,m,t=464680339,2**29,5
    anomaly=spectral_s(a,m,t)['values'][t]
    anomaly_independent=shortest_basis(lcg_basis(a,m,t))
    assert anomaly['squared']==anomaly_independent['squared']<anomaly['search_start_squared']
    randu=[]
    gp=PARI
    for t in [7,8,9]:
        B=lcg_basis(65539,2**29,t)
        independent=shortest_basis(B)
        G=[[dot(x,y) for y in B] for x in B]
        matrix='['+';'.join(','.join(map(str,row)) for row in G)+']'
        code='default(realprecision,100);default(nbthreads,1);r=qfminim('+matrix+',,,2);print([r[1],r[2]]);for(i=1,matsize(r[3])[2],print(Vec(r[3][,i])))\n'
        raw=subprocess.run([gp,'-fq'],input=code,text=True,capture_output=True,check=True,timeout=120)
        assert not raw.stderr,raw.stderr
        lines=raw.stdout.strip().splitlines();count,best=ast.literal_eval(lines[0])
        vectors=[]
        for line in lines[1:]:
            x=ast.literal_eval(line)
            v=[sum(x[i]*B[i][j] for i in range(t)) for j in range(t)]
            assert dot(v,v)==best
            vectors.extend([v,[-z for z in v]])
        assert independent['squared']==best==116
        assert count==len(vectors) and independent['vectors']==sorted(vectors)
        randu.append(dict(t=t,independent=independent,pari_output=raw.stdout,
                          pari_version='2.15.4',pari_flag=2,pari_decimal_precision=100))
    mu9=certify_round(mp.iv.mpf(32)/945*mp.iv.pi**4*mp.iv.mpf(116)**(mp.iv.mpf(9)/2)/2**29,'11.98')
    ex8=mp.iv.mpf(4)/3*mp.iv.mpf('1e-4')/mp.iv.sqrt(mp.iv.pi)
    return dict(worked_example_steps=len(steps),worked_example_decimals=decimal,
                anomaly=dict(a=a,m=m,t=5,book=anomaly,independent=anomaly_independent),
                randu=randu,mu9=mu9,exercise8_bound=str(ex8),
                scope='All displayed intermediate matrices and15 reductions on104; rare1982 search improvement; RANDU t7..9 rational sphere versus PARI qfminim flag2, all witnesses validated exactly; exercise8 numerical upper bound.')


def cf(m,a):
    qs=[]
    while a:q=m//a;qs.append(q);m,a=a,m-q*a
    return qs


def bounded_quotients(m,residue=1,modulus=20):
    """Complete prefix/suffix search with quotients1,2 and fixed denominator.

    Split after the first continuant P>sqrt(m). Its predecessor Q<=sqrt(m).
    The suffix continuants R,S satisfy P*R+Q*S=m and 0<=S<R, so only a
    few R in a residue class modulo Q are possible for each prefix.
    """
    threshold=isqrt(m);solutions=set();prefixes=trials=0
    stack=[(1,0,0,1,())]
    while stack:
        P,Q0,A,B,word=stack.pop()
        if P<=threshold:
            for q in [1,2]:stack.append((q*P+Q0,P,q*A+B,A,word+(q,)))
            continue
        prefixes+=1
        # Empty suffix, only relevant for small m.
        if P==m and word[-1]==2 and 0<A<m and A%modulus==residue:
            solutions.add(A)
        low=(m+Q0+P+Q0-1)//(P+Q0)  # S<R, integer S>=1
        high=(m-Q0)//P
        r0=(m*pow(P,-1,Q0))%Q0 if Q0>1 else 0
        for k in range(-((-(low-r0))//Q0),(high-r0)//Q0+1):
            R=r0+k*Q0;S=(m-P*R)//Q0;trials+=1
            assert P*R+Q0*S==m and 1<=S<R
            if gcd(R,S)!=1:continue
            num=A*R+B*S
            if num%modulus!=residue:continue
            tail=cf(R,S)
            if max(tail)>2:continue
            assert gcd(num,m)==1 and cf(m,num)==list(word)+tail
            solutions.add(num)
    return dict(m=m,solutions=sorted(solutions),prefixes=prefixes,suffix_trials=trials,
                residue=residue,modulus=modulus)


def quotient_claim():
    small=0
    for m in range(2,251):
        r=bounded_quotients(m,residue=0,modulus=1)
        direct=[a for a in range(1,m) if gcd(a,m)==1 and max(cf(m,a))<=2]
        assert r['solutions']==direct,(m,r,direct)
        small+=1
    large=bounded_quotients(10**10)
    assert large['solutions']==[]
    qs=cf(10**10,4219755981)
    assert max(qs)==3 and qs.count(3)==1
    return dict(small_moduli=small,large=large,row8_quotients=qs,
                scope='Complete exact prefix/suffix census, not a random search; all canonical finite continued fractions end with quotient>=2.')


def errata_and_periods():
    a,m=2650845021,2**32
    book=spectral_s(a,m,6);certificates={};printed=[4938969760,2646962,68342,8778,1506]
    merits=[]
    for t,expected,score in zip(range(2,7),printed,['3.61','4.20','5.37','8.85','4.11']):
        certificates[t]=shortest_basis(lcg_basis(a,m,t))
        assert certificates[t]['squared']==book['values'][t]['squared']==expected
        merit=mp.iv.pi**(mp.iv.mpf(t)/2)*mp.iv.mpf(expected)**(mp.iv.mpf(t)/2)/(mp.iv.gamma(1+mp.iv.mpf(t)/2)*m)
        merits.append(certify_round(merit,score))
    p1,p2=2**31-1,2**31-249
    orders=[]
    for p,a in [(p1,48271),(p2,40692)]:
        assert all(p%d for d in range(2,isqrt(p)+1))
        factors={int(q):int(e) for q,e in sp.factorint(p-1).items()}
        assert __import__('math').prod(q**e for q,e in factors.items())==p-1
        assert all(all(q%d for d in range(2,isqrt(q)+1)) for q in factors)
        powers={q:pow(a,(p-1)//q,p) for q in factors}
        assert all(x!=1 for x in powers.values()) and pow(a,p-1,p)==1
        orders.append(dict(a=a,p=p,order=p-1,factors=factors,witness_powers=powers))
    crt=1431853894371298687
    assert crt%p1==48271 and crt%p2==40692 and gcd(p1-1,p2-1)==62
    period=(p1-1)*(p2-1)//62
    p=p1;a,b=271828183,-314159269
    discriminant=(a*a+4*b)%p
    assert pow(discriminant,(p-1)//2,p)==p-1
    def mul(z,w):
        u,v=z;r,s=w
        return ((u*r+b*v*s)%p,(u*s+v*r+a*v*s)%p)
    def power(n):
        z=(0,1);r=(1,0)
        while n:
            if n&1:r=mul(r,z)
            z=mul(z,z);n//=2
        return r
    order=p*p-1;factors={int(q):int(e) for q,e in sp.factorint(order).items()}
    assert __import__('math').prod(q**e for q,e in factors.items())==order
    assert all(all(q%d for d in range(2,isqrt(q)+1)) for q in factors)
    witnesses={q:power(order//q) for q in factors}
    assert power(order)==(1,0) and all(z!=(1,0) for z in witnesses.values())
    return dict(killingbeck=dict(a=2650845021,m=m,squared=printed,certificates=certificates,merits=merits),
                combined=dict(orders=orders,crt_multiplier=crt,period=period),
                second_order=dict(p=p,a=a,b=b,discriminant=discriminant,order=order,factors=factors,witnesses=witnesses),
                scope='Numerical2004 erratum and exact periods/CRT in38,39. Exhaustive historical search over2^30 multipliers not repeated; no independent global optimality claim.')


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true')
    ap.add_argument('--pari',default=PARI,help='Path to a PARI/GP executable')
    args=ap.parse_args();PARI=args.pari
    r=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}
    for key,fun in [('table_intervals',table_intervals),('examples',examples),('quotient_claim',quotient_claim),('errata_and_periods',errata_and_periods)]:
        if key in r:continue
        start=time.monotonic();r[key]=fun();r[key]['seconds']=time.monotonic()-start
        OUT.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
        print(key,'completed',r[key]['seconds'],flush=True)
