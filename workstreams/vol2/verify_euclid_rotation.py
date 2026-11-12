#!/usr/bin/env python3
"""Exact quadratic first-hit recursion versus direct orbit iteration."""
from fractions import Fraction as F
from functools import cmp_to_key
from math import isqrt
from pathlib import Path
from verify_euclid_quadratic import Q
import argparse,json,os,time
ROOT=Path(__file__).resolve().parent
DEST=ROOT/'results/euclid-rotation.json'

def sign(x):
    a,b=x.a,x.b
    if not b:return (a>0)-(a<0)
    if not a:return (b>0)-(b<0)
    if (a>0)==(b>0):return 1 if a>0 else -1
    t=a*a-x.D*b*b
    assert t
    return ((t>0)-(t<0))*(1 if a>0 else -1)

def le(x,y):return sign(x-y)<=0
def lt(x,y):return sign(x-y)<0
def ceiling(x):return -(-x).floor()
def frac(x):return x-x.floor()

def first_hit(alpha,beta,gamma,left=True,trace=None):
    # left=True: [beta,gamma); left=False: (beta,gamma].
    assert le(Q(0,0,alpha.D),beta) and lt(beta,gamma) and le(gamma,Q(1,0,alpha.D))
    inv=alpha.inv();ratio=beta*inv
    k=ceiling(ratio) if left else ratio.floor()+1
    p=alpha*k
    if (lt(p,gamma) if left else le(p,gamma)):
        return k
    b=-(gamma*inv)+k;c=-(beta*inv)+k
    m=first_hit(frac(inv),b,c,not left,trace)
    assert m>=1
    n=k-1+ceiling(inv*m)
    assert (alpha*n).floor()==m
    if trace is not None:trace.append((n,m))
    return n

def book(alpha,beta,gamma):
    inv=alpha.inv();k=ceiling(beta*inv)
    if lt(alpha*k,gamma):return k
    return k-1+ceiling(inv*book(frac(inv),-(gamma*inv)+k,-(beta*inv)+k))

def orbit(alpha,limit):
    out=[];x=Q(0,0,alpha.D)
    for n in range(limit):
        out.append(x);x=x+alpha
        if sign(x-1)>=0:x=x-1
    return out

def oracle(seq,beta,gamma,left):
    for n,x in enumerate(seq):
        if (le(beta,x) and lt(x,gamma)) if left else (lt(beta,x) and le(x,gamma)):
            return n
    raise AssertionError('Oracle range too short; never evidence of no hit')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    out=json.loads(DEST.read_text()) if args.resume and DEST.exists() else {};print('pid',os.getpid(),flush=True)
    def save(k,x):out[k]=x;DEST.write_text(json.dumps(out,indent=2)+'\n');print(k,json.dumps(x),flush=True)
    if 'counterexample' not in out:
        a=Q(-1,1,2);b=a*F(1,2);g=a
        assert book(a,b,g)==0 and first_hit(a,b,g)==3
        seq=orbit(a,4);assert oracle(seq,b,g,True)==3
        count=0
        for j in range(-10,11):
            a=Q(-1+F(j,1000),1,2);b=a*F(1,2)
            assert book(a,b,a)==0 and first_hit(a,b,a)==3
            assert oracle(orbit(a,4),b,a,True)==3;count+=1
        save('counterexample',dict(alpha='sqrt(2)-1',beta='alpha/2',gamma='alpha',book=0,correct=3,family=count))
    if 'comparisons' not in out:
        start=time.monotonic();count=raw_fail=transitions=max_n=max_depth=0
        for D in (2,3,5,6,7,10,13,17):
            root=Q(-isqrt(D),1,D)
            for alpha in (root,root*F(1,2)):
                seq=orbit(alpha,4096);grid=[Q(F(j,12),0,D) for j in range(13)]
                points=sorted(seq[:25],key=cmp_to_key(lambda x,y:sign(x-y)))
                intervals=[(v[i],v[j]) for v in (grid,points) for i in range(len(v)) for j in range(i+1,len(v))]
                for beta,gamma in intervals:
                    for left in (True,False):
                        trace=[];got=first_hit(alpha,beta,gamma,left,trace)
                        want=oracle(seq,beta,gamma,left)
                        assert got==want,(D,alpha,beta,gamma,left,got,want)
                        assert all(n>m for n,m in trace)
                        transitions+=len(trace);max_depth=max(max_depth,len(trace));max_n=max(max_n,got);count+=1
                    if book(alpha,beta,gamma)!=first_hit(alpha,beta,gamma):raw_fail+=1
        save('comparisons',dict(cases=count,original_failures=raw_fail,recursive_transitions=transitions,max_index=max_n,max_depth=max_depth,quadratic_rotations=16,seconds=time.monotonic()-start))
    if 'thin_intervals' not in out:
        start=time.monotonic();a=Q(-1,1,2);seq=orbit(a,20000);ct=0;max_depth=0
        for target in (100,1000,4096,9999):
            eps=Q(F(1,10**9),0,2);beta=seq[target]-eps;gamma=seq[target]+eps
            for left in (True,False):
                trace=[];got=first_hit(a,beta,gamma,left,trace);want=oracle(seq,beta,gamma,left)
                assert got==want==target;ct+=1;max_depth=max(max_depth,len(trace))
        save('thin_intervals',dict(cases=ct,max_depth=max_depth,seconds=time.monotonic()-start))
    out['status']='passed';out['final_pid']=os.getpid();out['scope']='Exact quadratic-field comparisons by rational squares; independent orbit uses repeated addition and one subtraction, without recursive formula. General proof covers arbitrary irrational alpha and real endpoints.';DEST.write_text(json.dumps(out,indent=2)+'\n');print('passed',flush=True)
if __name__=='__main__':main()
