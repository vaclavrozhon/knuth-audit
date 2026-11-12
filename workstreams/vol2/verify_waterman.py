"""Waterman's multiplier construction: Gaussian factors versus direct squares.

All factorizations are multiplied back and their primes checked by trial
division. Spectral candidates are checked by S and independent sphere search.
"""
import argparse
from functools import lru_cache
from itertools import product
import json
from math import gcd,isqrt
from pathlib import Path
import time
import mpmath as mp
import sympy as sp
from spectral import spectral_s
from spectral_independent import shortest_basis,lcg_basis

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/waterman.json'
mp.mp.dps=60


def mul(z,w):
    return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]


def power(z,e):
    r=(1,0)
    for _ in range(e):r=mul(r,z)
    return r


@lru_cache(None)
def prime_squares(p):
    assert p%4==1 and all(p%d for d in range(2,isqrt(p)+1))
    n=2
    while pow(n,(p-1)//2,p)!=p-1:n+=1
    root=pow(n,(p-1)//4,p);assert root*root%p==p-1
    z,w=(p,0),(root,1)
    while w!=(0,0):
        norm=w[0]**2+w[1]**2
        real=z[0]*w[0]+z[1]*w[1]
        imag=z[1]*w[0]-z[0]*w[1]
        q=((2*real+norm)//(2*norm),(2*imag+norm)//(2*norm))
        v=mul(q,w);r=z[0]-v[0],z[1]-v[1]
        assert r[0]**2+r[1]**2<norm
        z,w=w,r
    assert z[0]**2+z[1]**2==p
    x,y=map(abs,z)
    if x%2==0:x,y=y,x
    return x,y


def representations(N):
    factors={int(p):int(e) for p,e in sp.factorint(N).items()}
    assert __import__('math').prod(p**e for p,e in factors.items())==N
    for p in factors:assert all(p%d for d in range(2,isqrt(p)+1))
    predicted=set()
    if all(p%4==1 for p in factors):
        entries=list(factors.items())
        for signs in product([-1,1],repeat=max(0,len(entries)-1)):
            z=(1,0)
            for (p,e),sign in zip(entries,(1,*signs)):
                u,v=prime_squares(p);z=mul(z,power((u,sign*v),e))
            x,y=map(abs,z)
            if x%2:x,y=y,x
            predicted.add((x,y))
        assert len(predicted)==2**(len(entries)-1)
    direct=set()
    for x in range(0,isqrt(N)+1,2):
        y=isqrt(N-x*x)
        if y*y+x*x==N and gcd(x,y)==1:direct.add((x,y))
    assert predicted==direct,(N,factors,predicted,direct)
    return factors,sorted(predicted)


def main(resume):
    r=json.loads(OUT.read_text()) if resume and OUT.exists() else {'construction':[],'spectral':{}}
    if not r['construction']:
        start=time.monotonic();m=2**32;top=isqrt(m*m//3)
        assert 3*top*top<m*m<3*(top+1)**2 and top==2479700524
        N=top-(top-1)%4;count=0
        while count<16:
            factors,reps=representations(N)
            multipliers=[(x+y)*pow(y-x,-1,m)%m for x,y in reps]
            assert all(a%4==1 for a in multipliers)
            r['construction'].append(dict(N=N,factors=factors,representations=reps,multipliers=multipliers))
            count+=len(reps);N-=4
        assert count==16 and r['construction'][-1]['N']==2479700521-68
        first=r['construction'][0]
        assert set(map(tuple,first['representations']))=={(4364,49605),(26364,42245),(38640,31411),(11960,48339)}
        assert set(first['multipliers'])=={2974037721,2254986297,4246248609,956772177}
        eight=next(d for d in r['construction'] if d['N']==2479700521-8)
        assert eight['representations']==[(45088,21137)] and eight['multipliers']==[3825140801]
        factors,reps=representations(5773502689)
        assert factors=={53:1,108934013:1} and set(reps)=={(67008,35825),(75820,4983)}
        assert 5773502691==isqrt(10**20//3)
        # The two conjugate products are checked directly, independently of
        # the Gaussian gcd algorithm's choice of units/conjugates.
        assert mul((7,2),(2203,10202))==(-4983,75820)
        assert mul((7,2),(2203,-10202))==(35825,-67008)
        decimal=(75820-4983)*pow(-4983-75820,-1,10**10)%10**10
        assert decimal==4160984121
        r['decimal_example']=dict(N=5773502689,factors=factors,representations=reps,a=decimal)
        r['construction_seconds']=time.monotonic()-start
        OUT.write_text(json.dumps(r,indent=2)+'\n');print('construction',count,'multipliers',flush=True)
    table=json.loads((ROOT/'results/spectral-table.json').read_text())
    for d in r['construction']:
        for a in d['multipliers']:
            key=str(a)
            if key in r['spectral']:continue
            if a==1566083941:
                data=table['rows']['14'];sq=[data['dimensions'][str(t)]['squared'] for t in range(2,7)]
                certificates='results/spectral-table.json row14'
            else:
                book=spectral_s(a,2**32,6);independent={}
                for t in range(2,7):
                    independent[t]=shortest_basis(lcg_basis(a,2**32,t))
                    assert independent[t]['squared']==book['values'][t]['squared']
                sq=[book['values'][t]['squared'] for t in range(2,7)]
                certificates=independent
            merits=[mp.pi**(mp.mpf(t)/2)*mp.mpf(s)**(mp.mpf(t)/2)/(mp.gamma(1+mp.mpf(t)/2)*2**32)
                    for t,s in zip(range(2,7),sq)]
            r['spectral'][key]=dict(squared=sq,merits=[mp.nstr(x,45) for x in merits],
                min_merit=mp.nstr(min(merits),45),certificates=certificates)
            OUT.write_text(json.dumps(r,indent=2)+'\n');print('spectral',a,sq,flush=True)
    best=max(r['spectral'],key=lambda a:mp.mpf(r['spectral'][a]['min_merit']))
    r['best_by_min_merit']=int(best)
    r['best_by_mu2']=int(max(r['spectral'],key=lambda a:r['spectral'][a]['squared'][0]))
    assert r['best_by_mu2']==1566083941
    r['selection_note']='The source does not define best among16. Its selected1566083941 maximizes mu2, but not min(mu2,...,mu6); no candidate Pareto-dominates it. No error claimed from this ambiguity.'
    r['scope']='First16 primitive square representations below2^32/sqrt3; Gaussian factors versus direct enumeration; S versus independent sphere minima. Best means largest min(mu2,...,mu6), explicitly chosen here.'
    r['complete']=True;OUT.write_text(json.dumps(r,indent=2)+'\n')
    print('best_by_min_merit',best,flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    main(args.resume)
