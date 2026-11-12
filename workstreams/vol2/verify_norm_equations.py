"""Exact checks for TAOCP 2, exercise 4.5.4-45.

The proofs and the distinction between the printed and repaired algorithm
are in notes/norm-equations.md. No floating point arithmetic is used.
Completed checkpoints are preserved. Trial division/root search are exact
small-instance oracles, not claims about polynomial-time implementations.
"""
from collections import Counter
from math import gcd, isqrt, prod
from pathlib import Path
import datetime
import json
import os
import random
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/norm-equations.json'


def norm(a, z):
    x, y = z
    return x*x-a*y*y


def mul(a, z, w, n):
    x, y = z
    u, v = w
    return ((x*u+a*y*v) % n, (x*v+y*u) % n)


def inv(a, z, n):
    q = pow(norm(a, z), -1, n)
    return (z[0]*q % n, -z[1]*q % n)


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def factor_small(n):
    ans = []
    for p in range(2, isqrt(n)+1):
        if n % p:
            continue
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        ans.append((p, e))
    if n > 1:
        ans.append((n, 1))
    return ans


def gauss(a, m, z):
    """Shortest (w,u) in <(m,0),(z,1)> for w^2+abs(a)u^2.

    Returns a reduced basis and its integer coordinates in the input basis.
    The separate exhaustive check below verifies minimality for small inputs.
    """
    A = abs(a)
    assert A and m
    def dot(v, w):
        return v[0]*w[0]+A*v[1]*w[1]
    b, c = (m, 0), (z, 1)
    B, C = (1, 0), (0, 1)
    steps = 0
    while True:
        if dot(c, c) < dot(b, b):
            b, c, B, C = c, b, C, B
        s, t = dot(b, b), dot(b, c)
        if 2*abs(t) <= s:
            break
        q = (2*t+s)//(2*s)
        c = tuple(c[i]-q*b[i] for i in range(2))
        C = tuple(C[i]-q*B[i] for i in range(2))
        steps += 1
        assert steps < 1000
    assert b == (m*B[0]+z*B[1], B[1])
    assert c == (m*C[0]+z*C[1], C[1])
    assert abs(B[0]*C[1]-B[1]*C[0]) == 1
    assert dot(b,b) <= dot(c,c) and 2*abs(dot(b,c)) <= dot(b,b)
    assert 3*dot(b,b)**2 <= 4*m*m*A
    return b, c, B, C, steps


def elementary_checks():
    identity = 0
    for a in range(-4, 5):
        for x in range(-2, 3):
            for y in range(-2, 3):
                for u in range(-2, 3):
                    for v in range(-2, 3):
                        X, Y = x*u+a*y*v, x*v+y*u
                        assert norm(a,(X,Y)) == norm(a,(x,y))*norm(a,(u,v))
                        identity += 1
    # All four coordinates 1, a=2: printed norm=-7, product=1.
    assert norm(2,(-1,2)) == -7 and norm(2,(3,2)) == 1
    restricted = Counter((u*u-3*v*v)%7 for u in range(1,7) for v in range(1,7))
    complete = Counter((u*u-3*v*v)%7 for u in range(7) for v in range(7))
    assert [restricted[b] for b in range(1,7)] == [4,4,8,4,8,8]
    assert [complete[b] for b in range(1,7)] == [8]*6
    fiber_instances = residue_pairs = bijection_checks = 0
    for n in range(3, 66, 2):
        fac = factor_small(n)
        for a in range(1,n):
            if gcd(a,n) != 1:
                continue
            fibers = [[] for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    fibers[(x*x-a*y*y)%n].append((x,y))
            residue_pairs += n*n
            expected = prod(p**(e-1)*(p-(1 if pow(a,(p-1)//2,p)==1 else -1))
                            for p,e in fac)
            for b in range(1,n):
                if gcd(b,n) != 1:
                    continue
                assert len(fibers[b]) == expected
                # Test the whole bijection, including its explicit inverse.
                anchor = fibers[b][0]
                image = {mul(a,anchor,z,n) for z in fibers[1]}
                assert image == set(fibers[b])
                for z in image:
                    assert mul(a,anchor,mul(a,inv(a,anchor,n),z,n),n) == z
                fiber_instances += 1
                bijection_checks += expected
    return dict(identity_cases=identity, fiber_instances=fiber_instances,
                residue_pairs=residue_pairs, bijection_checks=bijection_checks,
                sign_counterexample={'a':2,'pairs':[[1,1],[1,1]],
                                     'printed_norm':-7,'correct_norm':1},
                uniformity_counterexample={'n':7,'a':3,'b':1,
                    'nonzero_coordinate_counts':dict(sorted(restricted.items())),
                    'all_coordinate_counts':dict(sorted(complete.items()))})


def lattice_checks():
    cases = shortest_comparisons = max_steps = 0
    witnesses = []
    for a in range(-35,36):
        if not a:
            continue
        for s in range(1,37):
            for z in range(s):
                if (z*z-a)%s:
                    continue
                m = (z*z-a)//s
                if not m:
                    continue
                (w,u), c, B, C, steps = gauss(a,m,z)
                v = B[0]
                t = (w*w-a*u*u)//m
                assert w*w-a*u*u == m*t
                assert 3*t*t <= 4*abs(a)
                X, Y = s*u+z*v, v
                assert (X,Y) != (0,0) and X*X-a*Y*Y == s*t
                # Enumerate all vectors with norm at most the candidate norm.
                L = w*w+abs(a)*u*u
                for U in range(-isqrt(L//abs(a)),isqrt(L//abs(a))+1):
                    for W in range(-isqrt(L),isqrt(L)+1):
                        if (W-z*U)%m or (W,U)==(0,0):
                            continue
                        assert W*W+abs(a)*U*U >= L
                        shortest_comparisons += 1
                max_steps=max(max_steps,steps)
                cases += 1
                if (a,s,z)==(2,17,6):
                    assert L==2 and 3*L*L > 4*abs(a)
                    witnesses.append(dict(a=a,s=s,z=z,m=m,u=u,v=v,
                                          squared_length=L,t=t,X=X,Y=Y))
    assert len(witnesses)==1
    return dict(cases=cases,shortest_comparisons=shortest_comparisons,
                max_gauss_steps=max_steps,missing_factor_witness=witnesses[0])


class Solver:
    def __init__(self, seed):
        self.rng = random.Random(seed)
        self.stats = Counter()
        self.max_depth = 0

    def square_case(self,a,b,n,r):
        assert r*r%n == a%n
        h=pow(2,-1,n)
        return ((b+1)*h%n,(b-1)*h*pow(r,-1,n)%n)

    def split(self,a,b,n,d,depth):
        """Use one discovered divisor, without factoring either component."""
        assert 1<d<n and n%d==0
        self.stats['factor_splits']+=1
        support, rest, exponent = 1,n,0
        while (g:=gcd(rest,d))>1:
            support*=g
            rest//=g
            exponent+=1
        assert support*rest==n and gcd(support,rest)==1
        assert pow(d,exponent)%support==0
        x,y=self.solve(a,b,d,depth+1)
        modulus=d
        while modulus % support:
            assert (norm(a,(x,y))-b)%modulus==0
            residual=(b-norm(a,(x,y)))//modulus
            # A Bezout combination of the two derivatives works even when
            # neither derivative is invertible on the whole composite modulus.
            g,h,c0,c1,d0,d1=2*x,-2*a*y,1,0,0,1
            while h:
                q=g//h
                g,h=h,g-q*h
                c0,c1=c1,c0-q*c1
                d0,d1=d1,d0-q*d1
            if g<0:
                g,c0,d0=-g,-c0,-d0
            k=residual*pow(g,-1,modulus)%modulus
            x+=modulus*(k*c0%modulus)
            y+=modulus*(k*d0%modulus)
            modulus*=modulus
            x%=modulus; y%=modulus
            assert (norm(a,(x,y))-b)%modulus==0
            self.stats['hensel_doublings']+=1
        x%=support; y%=support
        if rest==1:
            return x,y
        X,Y=self.solve(a,b,rest,depth+1)
        def crt(x,X):
            return (x+support*((X-x)*pow(support,-1,rest)%rest))%n
        self.stats['crt_merges']+=1
        return crt(x,X),crt(y,Y)

    def solve(self,a,b,n,depth=0):
        self.max_depth=max(self.max_depth,depth)
        assert depth<50
        if n==1:
            return (0,0)
        assert n%2 and gcd(a*b,n)==1
        a=(a+n//2)%n-n//2
        b%=n
        if a>0 and (r:=isqrt(a))**2==a:
            self.stats['known_square']+=1
            return self.square_case(a,b,n,r)
        if a==-1:
            # Exact small-instance prime and sum-of-two-squares oracle.
            p=b
            while not (p%4==1 and prime(p)):
                p+=n
            for y in range(isqrt(p)+1):
                x=isqrt(p-y*y)
                if x*x+y*y==p:
                    self.stats['minus_one_base']+=1
                    return x%n,y%n
            raise AssertionError('prime 1 mod 4 lacked representation')
        for trial in range(10000):
            self.stats['random_pairs']+=1
            U,V=self.rng.randrange(n),self.rng.randrange(n)
            W=norm(a,(U,V))%n
            d=gcd(W,n)
            if 1<d<n:
                return self.split(a,b,n,d,depth)
            if d==n:
                d=gcd(V,n)
                if d==1:
                    self.stats['zero_norm_square']+=1
                    return self.square_case(a,b,n,U*pow(V,-1,n)%n)
                if 1<d<n:
                    return self.split(a,b,n,d,depth)
                d=gcd(U,n)
                if 1<d<n:
                    return self.split(a,b,n,d,depth)
                continue
            s=b*W%n
            if s==1:
                self.stats['unit_target']+=1
                return inv(a,(U,V),n)
            if not prime(s):
                continue
            roots=[z for z in range(s) if (z*z-a)%s==0]
            if not roots:
                continue
            z=roots[0]
            m=(z*z-a)//s
            d=gcd(m,n)
            if d==n:
                self.stats['m_zero_modulus']+=1
                return self.square_case(a,b,n,z)
            if d>1:
                return self.split(a,b,n,d,depth)
            (w,u),_,B,_,_=gauss(a,m,z)
            v=B[0]
            t=(w*w-a*u*u)//m
            alpha=(s*u+z*v,v)
            assert norm(a,alpha)==s*t and 3*t*t<=4*abs(a)
            assert gcd(gcd(alpha[0],alpha[1]),n)==1
            if t==0:
                d=gcd(alpha[1],n)
                if d>1:
                    return self.split(a,b,n,d,depth)
                self.stats['t_zero']+=1
                return self.square_case(a,b,n,alpha[0]*pow(alpha[1],-1,n)%n)
            d=gcd(t,n)
            if d>1:
                return self.split(a,b,n,d,depth)
            self.stats['norm_descents']+=1
            X,Y=self.solve(t,a,n,depth+1)
            d=gcd(Y,n)
            if d==n:
                self.stats['recursive_square']+=1
                return self.square_case(a,b,n,X)
            if d>1:
                return self.split(a,b,n,d,depth)
            iy=pow(Y,-1,n)
            beta=(X*iy%n,iy)
            assert norm(a,beta)%n==t%n
            delta=mul(a,alpha,inv(a,beta,n),n)
            ans=mul(a,delta,inv(a,(U,V),n),n)
            assert norm(a,ans)%n==b
            return ans
        raise AssertionError('finite test trial cap reached')


def solver_checks():
    solver=Solver(20261103)
    instances=0
    examples=[]
    for n in range(3,82,2):
        for a in range(1,n):
            if gcd(a,n)!=1:
                continue
            for b in range(1,n):
                if gcd(b,n)!=1:
                    continue
                x,y=solver.solve(a,b,n)
                assert 0<=x<n and 0<=y<n and (x*x-a*y*y-b)%n==0
                instances+=1
    # Force overlapping divisor supports to validate the lift/CRT path.
    for n,d in ((81,9),(225,15),(675,15),(945,9),(4725,15)):
        for a,b in ((2,1),(-1,2),(7,11),(13,17)):
            if gcd(a*b,n)!=1:
                continue
            x,y=solver.split(a,b,n,d,0)
            assert (x*x-a*y*y-b)%n==0
            examples.append(dict(n=n,divisor=d,a=a,b=b,x=x,y=y))
    return dict(exhaustive_instances=instances,stats=dict(solver.stats),
                max_call_depth=solver.max_depth,forced_factor_examples=examples,
                oracle_scope='Trial division and exhaustive roots only for finite validation; see proof for efficient replacements.')


def main():
    data=json.loads(OUT.read_text()) if OUT.exists() else {'status':'running','checks':{}}
    for name,f in [('elementary',elementary_checks),('lattice',lattice_checks),
                   ('solver',solver_checks)]:
        if data['checks'].get(name,{}).get('status')=='passed':
            print('skip',name,flush=True)
            continue
        start=time.monotonic()
        result=f()
        data['checks'][name]=dict(status='passed',seconds=time.monotonic()-start,**result)
        data['updated_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
        tmp=OUT.with_suffix('.tmp'); tmp.write_text(json.dumps(data,indent=2)+'\n');tmp.replace(OUT)
        print(name,data['checks'][name]['seconds'],'passed',flush=True)
    data['status']='passed'
    OUT.write_text(json.dumps(data,indent=2)+'\n')
    print('all three checkpoints passed; pid',os.getpid(),flush=True)


if __name__=='__main__':
    main()
