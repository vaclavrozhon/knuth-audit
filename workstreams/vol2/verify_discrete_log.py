"""Exact arithmetic for TAOCP 2 exercise 4.5.4-46.

Own row-lattice algorithm uses Bezout identities over integers. Validation
uses enumerated finite subgroups, exhaustive power tables, and direct
certificates. No factorization of p-1 is needed by the index-calculus code.
"""
from itertools import product
from math import gcd, isqrt, prod, comb
from pathlib import Path
import datetime
import json
import os
import random
import time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/discrete-log.json'


def primes(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,isqrt(p)+1))]


def egcd(a,b):
    x,y,X,Y=1,0,0,1
    while b:
        q=a//b
        a,b=b,a-q*b
        x,X=X,x-q*X
        y,Y=Y,y-q*Y
    return (a,x,y) if a>0 else (-a,-x,-y)


class RowLattice:
    """Upper triangular basis of M Z^d plus all inserted relation rows."""
    def __init__(self,M,d):
        self.M,self.d=M,d
        self.B=[[M*int(i==j) for j in range(d)] for i in range(d)]
        self.C=[[] for _ in range(d)]
        self.rows=[]
        self.nonunit_gcd_steps=0

    def index(self):
        return prod(self.B[j][j] for j in range(self.d))

    def contains(self,v):
        v=list(v)
        for j in range(self.d):
            q,r=divmod(v[j],self.B[j][j])
            if r:
                return False
            v=[v[k]-q*self.B[j][k] for k in range(self.d)]
        return not any(v)

    def insert(self,v):
        v=list(v); self.rows.append(v[:])
        for c in self.C:
            c.append(0)
        c=[0]*(len(self.rows)-1)+[1]
        for j in range(self.d):
            if not v[j]:
                continue
            old=self.B[j][:]; oldc=self.C[j][:]
            pivot,w=old[j],v[j]
            g,x,y=egcd(pivot,w)
            assert x*pivot+y*w==g
            self.nonunit_gcd_steps += gcd(pivot,self.M)>1 and gcd(w,self.M)>1
            self.B[j]=[x*old[k]+y*v[k] for k in range(self.d)]
            self.C[j]=[(x*oldc[k]+y*c[k])%self.M for k in range(len(c))]
            v=[-(w//g)*old[k]+(pivot//g)*v[k] for k in range(self.d)]
            c=[(-(w//g)*oldc[k]+(pivot//g)*c[k])%self.M for k in range(len(c))]
            assert v[j]==0
        assert not any(v)
        # Reduce entries above the diagonal without modular division.
        for j in range(1,self.d):
            for i in range(j):
                q=self.B[i][j]//self.B[j][j]
                self.B[i]=[x-q*y for x,y in zip(self.B[i],self.B[j])]
                self.C[i]=[(x-q*y)%self.M for x,y in zip(self.C[i],self.C[j])]
        assert all(self.B[j][j]>0 and self.M%self.B[j][j]==0 for j in range(self.d))

    def certificate(self):
        count=0
        for j in range(self.d):
            for k in range(self.d):
                assert sum(c*r[k] for c,r in zip(self.C[j],self.rows))%self.M == self.B[j][k]%self.M
                count+=1
        return count


def lattice_check():
    rng=random.Random(461973)
    insertions=memberships=cert_entries=0
    for M in range(2,10):
        for d in range(1,4):
            universe=list(product(range(M),repeat=d))
            for case in range(8):
                L=RowLattice(M,d); H={(0,)*d}
                for _ in range(6):
                    v=[rng.randrange(-M,M+1) for _ in range(d)]
                    before=L.index(); contained=L.contains(v)
                    L.insert(v)
                    H={tuple((h[j]+k*v[j])%M for j in range(d)) for h in H for k in range(M)}
                    assert L.index()*len(H)==M**d
                    assert (L.index()==before)==contained
                    cert_entries+=L.certificate()
                    for w in universe:
                        assert L.contains(w)==(w in H)
                        memberships+=1
                    insertions+=1
    L=RowLattice(6,2)
    rows=[[2,0],[3,0],[0,2],[0,3]]
    for v in rows:
        L.insert(v)
    assert L.index()==1 and L.B==[[1,0],[0,1]]
    assert L.nonunit_gcd_steps>0
    L.certificate()
    return dict(insertions=insertions,membership_comparisons=memberships,
                certificate_entries=cert_entries,nonunit_example=dict(M=6,rows=rows,
                     coefficients=L.C,basis=L.B,nonunit_gcd_steps=L.nonunit_gcd_steps))


def smooth(v,base):
    e=[]
    for q in base:
        k=0
        while v%q==0:
            v//=q; k+=1
        e.append(k)
    return e if v==1 else None


def escape_check():
    functionals=pairs=bound_checks=0
    for p in primes(47):
        if p==2:
            continue
        M=p-1
        for B in (2,3,5):
            if B>M:
                continue
            base=primes(B); d=len(base)
            S={v:smooth(v,base) for v in range(1,p)}
            S={v:e for v,e in S.items() if e is not None}
            T={v:e for v,e in S.items() if v<=M//B}
            k=0
            while B**(k+1)<=M//B:
                k+=1
            assert len(T)>=comb(d,k) if k<=d else True
            bound_checks+=1
            for q in primes(M):
                if M%q:
                    continue
                for ell in product(range(q),repeat=d):
                    if not any(ell):
                        continue
                    j=next(j for j in range(d) if ell[j])
                    outside=sum(sum(x*y for x,y in zip(ell,e))%q!=0 for e in S.values())
                    assert 2*outside>=len(T)
                    for v,e in T.items():
                        f=S[v*base[j]]
                        assert all(f[k]-e[k]==int(k==j) for k in range(d))
                        assert (sum(x*y for x,y in zip(ell,e))%q or
                                sum(x*y for x,y in zip(ell,f))%q)
                        pairs+=1
                    functionals+=1
    return dict(functionals=functionals,pair_checks=pairs,smooth_count_bounds=bound_checks)


def power_table(a,p):
    r=1; out={}
    for n in range(p-1):
        out[r]=n; r=r*a%p
    return out


def precompute(p,a,B,rng):
    M=p-1; base=primes(B); L=RowLattice(M,len(base))
    exponents=[]; trials=0; changes=0
    while L.index()>1:
        r=rng.randrange(M); v=pow(a,r,p); trials+=1
        e=smooth(v,base)
        if e is None:
            continue
        old=L.index(); L.insert(e); exponents.append(r)
        assert old%L.index()==0
        changes+=L.index()<old
        assert trials<100000
    assert L.B==[[int(i==j) for j in range(len(base))] for i in range(len(base))]
    entries=L.certificate()
    logs=[sum(c*r for c,r in zip(row,exponents))%M for row in L.C]
    for q,n in zip(base,logs):
        assert pow(a,n,p)==q
    for r,e in zip(exponents,L.rows):
        # Ordinary integer product validates the full smooth factorization.
        assert prod(q**k for q,k in zip(base,e))==pow(a,r,p)
    return dict(p=p,a=a,B=B,base=base,logs=logs,relations=L.rows,
                relation_exponents=exponents,coefficients=L.C,trials=trials,
                index_decreases=changes,certificate_entries=entries,
                nonunit_gcd_steps=L.nonunit_gcd_steps)


def logarithms_check():
    rng=random.Random(2026110346)
    cases=[]; targets=target_trials=0
    selected=[]
    for p in primes(251):
        if p==2:
            continue
        roots=[]
        for a in range(2,p):
            table=power_table(a,p)
            if len(table)==p-1:
                roots.append(a)
                if len(roots)==2:
                    break
        selected.extend((p,a,min(11,p-1)) for a in roots)
    for p in (1009,10007,65537):
        a=next(a for a in range(2,p) if len(power_table(a,p))==p-1)
        selected.append((p,a,31))
    for p,a,B in selected:
        data=precompute(p,a,B,rng)
        table=power_table(a,p)
        bs=list(range(1,p)) if p<=1009 else [1,p-1]+[rng.randrange(1,p) for _ in range(128)]
        for b in bs:
            while True:
                r=rng.randrange(p-1)
                e=smooth(b*pow(a,r,p)%p,data['base'])
                target_trials+=1
                if e is not None:
                    break
            n=(sum(ei*ni for ei,ni in zip(e,data['logs']))-r)%(p-1)
            assert n==table[b] and pow(a,n,p)==b
            book_representative=n or p-1
            assert 1<=book_representative<p and pow(a,book_representative,p)==b
            targets+=1
        cases.append(data)
        print('logarithms',p,a,'relations',len(data['relations']),flush=True)
    assert pow(3,2,7)==2 and pow(3,1,7)!=2
    # Known 1998 correction of the final modulus, separate from C0173.
    assert 2*pow(3,5,7)%7==3 and (2+5)%6==1 and (2+5)%7!=1
    return dict(cases=cases,targets=targets,target_trials=target_trials,
                reconstruction_counterexample=dict(p=7,a=3,base=[2],r=2,e=1,c=1,
                     printed_log=1,correct_log=2),
                known_modulus_counterexample=dict(p=7,a=3,b=2,n=2,r=5,smooth_value=3))


def main():
    data=json.loads(OUT.read_text()) if OUT.exists() else {'status':'running','checks':{}}
    for name,f in [('integer_lattice',lattice_check),('escape',escape_check),
                   ('logarithms',logarithms_check)]:
        if data['checks'].get(name,{}).get('status')=='passed':
            print('skip',name,flush=True);continue
        start=time.monotonic();result=f()
        data['checks'][name]=dict(status='passed',seconds=time.monotonic()-start,**result)
        data['updated_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
        tmp=OUT.with_suffix('.tmp');tmp.write_text(json.dumps(data,indent=2)+'\n');tmp.replace(OUT)
        print(name,data['checks'][name]['seconds'],'passed',flush=True)
    data['status']='passed';OUT.write_text(json.dumps(data,indent=2)+'\n')
    print('all three checkpoints passed; pid',os.getpid(),flush=True)


if __name__=='__main__':
    main()
