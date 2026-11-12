#!/usr/bin/env python3
"""Independent root counts and exhaustive small-field best approximations."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import json
import random
import time
from verify_polynomial_division import add,mul,scale,divide,trim,degree

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/sturm-cf.json'


def sturm(a):
    derivative=[i*a[i] for i in range(1,len(a))]
    seq=[a,derivative]
    while seq[-1]:
        r=divide(seq[-2],seq[-1])[1]
        if not r:break
        seq.append(scale(r,-1))
    assert len(seq[-1])==1
    return seq


def signs_at(seq,x):
    if x in ['-inf','inf']:
        return [(1 if a[-1]>0 else -1)*(-1 if x=='-inf' and len(a)%2==0 else 1) for a in seq]
    vals=[]
    for a in seq:
        v=F(0)
        for c in reversed(a):v=v*x+c
        vals.append((v>0)-(v<0))
    return vals


def variations(signs):
    s=[x for x in signs if x]
    return sum(a!=b for a,b in zip(s,s[1:]))


def root_block():
    rng=random.Random(2026110410);intervals=0;all_real=0;simultaneous=False
    for case in range(100):
        roots=sorted(rng.sample(range(-8,9),rng.randrange(0,9)))
        quadratics=rng.sample(range(1,10),rng.randrange(0,4))
        if case==0:roots=[-1,0,1];quadratics=[]
        if not roots and not quadratics:roots=[0]
        a=[rng.choice([-2,1,3])]
        for r in roots:a=mul(a,[-r,1])
        for c in quadratics:a=mul(a,[c,0,1])
        seq=sturm(a)
        if not quadratics:
            assert [len(x)-1 for x in seq]==list(range(len(a)-1,-1,-1))
            all_real+=1
        points=sorted(set([F(i,2) for i in range(-18,19)]+list(map(F,roots))))
        records=[]
        for x in points:
            signs=signs_at(seq,x)
            assert not any(a==b==0 for a,b in zip(signs,signs[1:]))
            for i in range(1,len(signs)-1):
                if signs[i]==0:assert signs[i-1]==-signs[i+1]
            simultaneous |= signs.count(0)>1
            records.append(variations(signs))
        for i,a0 in enumerate(points):
            for j in range(i,len(points)):
                assert records[i]-records[j]==sum(a0<r<=points[j] for r in roots)
                intervals+=1
        assert variations(signs_at(seq,'-inf'))-variations(signs_at(seq,'inf'))==len(roots)
    assert simultaneous
    return {'polynomials':100,'intervals_including_endpoints':intervals,
            'all_real_sequences':all_real,'simultaneous_nonadjacent_zeros':simultaneous}


def cf(u,v,p):
    a,b=u,v;pm,qm=[1],[];P,Q=[[]],[[1]];R=[scale(v,-1,p)]
    while b:
        quotient,remainder=divide(a,b,p)
        pn=add(mul(quotient,P[-1],p),pm,p)
        qn=add(mul(quotient,Q[-1],p),qm,p)
        pm,qm=P[-1],Q[-1]
        P.append(pn);Q.append(qn)
        R.append(add(mul(pn,u,p),scale(mul(qn,v,p),-1,p),p))
        a,b=b,remainder
    for n in range(1,len(P)):
        determinant=add(mul(P[n-1],Q[n],p),scale(mul(P[n],Q[n-1],p),-1,p),p)
        assert determinant==[(-1)**n%p]
        assert degree(R[n-1])+degree(Q[n])==degree(u)
        assert degree(Q[n-1])<degree(Q[n])
    return P,Q,R,a


def monics(p,n):
    for a in product(range(p),repeat=n):yield list(a)+[1]


def best_block():
    pairs=strong=weak=kronecker=nonconstant=0
    for modulus,max_m in [(2,4),(3,3)]:
        for m in range(1,max_m+1):
            for n0 in range(0,m):
                for u in monics(modulus,m):
                    for v in monics(modulus,n0):
                        P,Q,R,g=cf(u,v,modulus);pairs+=1;cache={}
                        def oracle(q):
                            key=tuple(q)
                            if key not in cache:
                                pp,rr=divide(mul(q,v,modulus),u,modulus)
                                cache[key]=(pp,scale(rr,-1,modulus))
                            return cache[key]
                        for n in range(1,len(P)):
                            en=int(degree(Q[n]));previous=degree(R[n-1]);older=degree(u) if n==1 else degree(R[n-2])
                            for values in product(range(modulus),repeat=en):
                                q=trim(values,modulus);pp,rr=oracle(q)
                                if degree(rr)<older:
                                    c,rem=divide(q,Q[n-1],modulus)
                                    assert not rem and pp==mul(c,P[n-1],modulus)
                                    weak+=1;nonconstant+=degree(c)>0
                                    if degree(rr)<=previous:
                                        assert degree(c)<=0;strong+=1
                        if len(g)==1:
                            best={}
                            for values in product(range(modulus),repeat=m):
                                q=trim(values,modulus)
                                if not q:continue
                                pp,rr=oracle(q);d=degree(rr)
                                if d<0 or d>n0:continue
                                eq=int(degree(q));entry=best.setdefault(int(d),[eq,[]])
                                if eq<entry[0]:entry[:]=[eq,[]]
                                if eq==entry[0]:entry[1].append((pp,q))
                            for d,(eq,solutions) in best.items():
                                for pp,q in solutions:
                                    assert any(mul(pp,Q[j],modulus)==mul(q,P[j],modulus) for j in range(len(P)))
                                    kronecker+=1
    return {'input_pairs':pairs,'strong_witnesses':strong,'weaker_polynomial_multiple_witnesses':weak,
            'nonconstant_multipliers_in_weaker_theorem':nonconstant,'minimal_degree_kronecker_witnesses':kronecker}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'blocks':{}}
    for name,fn in [('roots',root_block),('best_approximations',best_block)]:
        if name in data['blocks']:print('REUSE',name,flush=True);continue
        start=time.perf_counter();r=fn();r['seconds']=time.perf_counter()-start;data['blocks'][name]=r
        OUT.write_text(json.dumps(data,indent=2)+'\n');print('PASS',name,r,flush=True)
    data['status']='passed';OUT.write_text(json.dumps(data,indent=2)+'\n')


if __name__=='__main__':main()
