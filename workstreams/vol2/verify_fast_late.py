#!/usr/bin/env python3
"""4.3.3-16/17/18: chirp identity, binary recurrence, literal storage layout.
Numerical labels and snapshots serve only independent validation.
The memory multiplier reads/writes bits; Python call frames model control.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,random,time
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/fast-late.json'

def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def power(a,n):
    if n<0:
        d=a[0]*a[0]+a[1]*a[1];a=(a[0]/d,-a[1]/d);n=-n
    out=(F(1),F(0))
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n>>=1
    return out

def chirp_tests():
    rng=random.Random(43316);cases=0;cells=0;zero=(F(0),F(0))
    roots=[(F(1),F(1)),(F(2),F(0)),(F(1,2),F(-1,3)),(F(0),F(1))]
    for K in list(range(1,13))+[15,17,23]:
        N=1
        while N<=2*K:N*=2
        for rho in roots:
            omega=mul(rho,rho)
            u=[(F(rng.randrange(-3,4)),F(rng.randrange(-3,4))) for _ in range(K)]
            a=[mul(power(rho,-t*t),u[t]) for t in range(K)]+[zero]*(N-K)
            b=[power(rho,(2*K-2-t)**2) for t in range(N)]
            for s in range(K):
                r=2*K-2-s
                cyc=zero;linear=zero;direct=zero
                for j in range(N):cyc=add(cyc,mul(a[j],b[(r-j)%N]))
                for j in range(r+1):linear=add(linear,mul(a[j],b[r-j]))
                for t in range(K):direct=add(direct,mul(power(omega,s*t),u[t]))
                assert cyc==linear and mul(power(rho,-s*s),cyc)==direct
                cells+=1
            cases+=1
    return dict(cases=cases,DFT_cells=cells,max_K=23,seed=43316,
                scope='Exact Gaussian-rational chirp and cyclic-aliasing check; FFT convolution theorem checked separately.')

@lru_cache(None)
def Kcount(n):
    if n==1:return 1
    if n%2==0:return 3*Kcount(n//2)
    return 2*Kcount(n//2+1)+Kcount(n//2)

@lru_cache(None)
def Rcount(n):
    if n==1:return 2
    if n%2==0:return 2*Rcount(n//2)+Kcount(n//2)
    return Rcount(n//2)+2*Kcount(n//2+1)

@lru_cache(None)
def space(n):
    if n==1:return 0
    return space((n+1)//2)+(n%2)

def recurrence_tests():
    limit=100000
    for n in range(1,limit+1):
        exponents=[i for i in range(n.bit_length()-1,-1,-1) if n>>i&1]
        e=exponents[0];t=len(exponents)
        explicit=3**e+sum(3**x*2**(e-x-j+3) for j,x in enumerate(exponents[1:],2))
        assert Kcount(n)==explicit and explicit%2==1
        assert Kcount(n+1)-Kcount(n)==2**(e-t+2)
        assert 2*Rcount(n)==Kcount(n)+Kcount(n+1)
        assert space(n)==e-exponents[-1]-t+2-(t==1)
        if n>1:assert space(n-1)<=space(n)+1
    # Formal coefficients, with K_0=0; no divergent series is evaluated.
    for d in range(10001):
        left=(Kcount(d-1) if d>=2 else 0)+(d==2)
        right=sum(c*Kcount((d-shift)//2) for shift,c in [(0,2),(1,3),(2,1)]
                  if d-shift>=2 and (d-shift)%2==0)
        assert left==right
    return dict(recurrence_values=limit,formal_coefficients=10001,
                first_K=[Kcount(n) for n in range(1,17)],first_S=[space(n) for n in range(1,17)])

class Memory:
    def __init__(self,u,v,N):
        self.N=N;self.cap=3*N+space(N)
        self.a=[(u>>i)&1 for i in range(N)]+[(v>>i)&1 for i in range(N)]+[1]*self.cap
        self.leaves=0;self.negative=0;self.max_written=-1;self.frames=[]
    def write(self,p,b):
        assert b in (0,1)
        base,size=self.frames[-1]
        assert base<=p<base+size and p>=2*self.N
        self.a[p]=b;self.max_written=max(self.max_written,p-2*self.N)
    def integer(self,p,n):return sum(self.a[p+i]<<i for i in range(n))
    def copy(self,src,dst,n):
        for i in (range(n-1,-1,-1) if dst>src else range(n)):self.write(dst+i,self.a[src+i])
    def subtract_abs(self,p,pn,q,qn,dst,n):
        sign=0
        for i in range(n-1,-1,-1):
            x=self.a[p+i] if i<pn else 0;y=self.a[q+i] if i<qn else 0
            if x!=y:sign=1 if x>y else -1;break
        if sign<0:p,q,pn,qn=q,p,qn,pn
        borrow=0
        for i in range(n):
            z=(self.a[p+i] if i<pn else 0)-(self.a[q+i] if i<qn else 0)-borrow
            borrow=int(z<0);self.write(dst+i,z+2*borrow)
        assert borrow==0
        return sign
    def negate(self,p,n):
        carry=1
        for i in range(n):
            z=1-self.a[p+i]+carry;self.write(p+i,z&1);carry=z>>1
    def plus(self,src,srcn,dst,dstn):
        carry=0
        for i in range(dstn):
            z=self.a[dst+i]+(self.a[src+i] if i<srcn else 0)+carry
            self.write(dst+i,z&1);carry=z>>1
        # Overflow is discarded modulo the destination span.
    def multiply(self,up,vp,N,base):
        size=3*N+space(N);assert base+size<=len(self.a)
        assert up+N<=base or up>=base+size
        assert vp+N<=base or vp>=base+size
        want=self.integer(up,N)*self.integer(vp,N)
        before=self.a[:base]+self.a[base+size:]
        self.frames.append((base,size))
        if N==1:
            self.write(base,self.a[up]*self.a[vp]);self.write(base+1,0);self.leaves+=1
        else:
            n=(N+1)//2;e=2*n-N;sn=space(n);high=n-e
            a=self.subtract_abs(up,n,up+n,high,base,n)
            b=self.subtract_abs(vp,n,vp+n,high,base+n,n)
            self.multiply(base,base+n,n,base+2*n)
            top=base+3*n+sn;length=3*n-2*e
            self.copy(base+2*n,top,2*n)
            self.multiply(up+n,vp+n,high,base)
            for i in range(2*n,length):self.write(top+i,0)
            # The initial top span is |(U0-U1)(V0-V1)|.
            if a*b>=0:self.negate(top,length)
            self.plus(base,2*high,top,length)
            self.plus(base,2*high,top+n,length-n)
            # Independent signed mathematical value; implementation above uses bits.
            U0=self.integer(up,n);U1=self.integer(up+n,high)
            V0=self.integer(vp,n);V1=self.integer(vp+n,high)
            signed=((1<<n)+1)*U1*V1-(U0-U1)*(V0-V1)
            assert self.integer(top,length)==signed%(1<<length)
            self.negative+=signed<0
            self.multiply(up,vp,n,base)
            out=base+2*n+sn
            for i in range(n):self.write(out+i,0)
            self.plus(base,2*n,out,2*N)
            self.plus(base,2*n,out+n,2*N-n)
            assert self.integer(out,2*N)==want
            self.copy(out,base,2*N)
        assert self.integer(base,2*N)==want
        assert self.a[:base]+self.a[base+size:]==before
        self.frames.pop()

def memory_tests():
    rng=random.Random(43318);cases=0;negative=0;maxN=0;rows=[]
    for N in range(1,7):
        for u in range(1<<N):
            for v in range(1<<N):
                a=Memory(u,v,N);a.multiply(0,N,N,2*N)
                assert a.integer(2*N,2*N)==u*v and a.leaves==Kcount(N)
                cases+=1;negative+=a.negative
    for N in [7,8,9,15,16,17,31,32,33,63,64,65,127,128,129,257]:
        mask=(1<<N)-1
        pairs=[(mask,mask),(0,mask),(1<<(N-1),1<<(N-1)),((1<<((N+1)//2))-1,)*2]
        pairs += [(rng.getrandbits(N),rng.getrandbits(N)) for _ in range(5)]
        for u,v in pairs:
            a=Memory(u,v,N);a.multiply(0,N,N,2*N)
            assert a.leaves==Kcount(N) and a.max_written<a.cap
            cases+=1;negative+=a.negative
        maxN=max(maxN,N);rows.append(dict(N=N,capacity=3*N+space(N),leaves=Kcount(N)))
    return dict(cases=cases,exhaustive_N_max=6,large_cases=144,max_N=maxN,
                negative_intermediates=negative,seed=43318,rows=rows,
                scope='Bitwise arithmetic data array and preservation checks; control frames and oracle snapshots not counted as data storage.')

def main():
    d=json.loads(OUT.read_text()) if OUT.exists() else {}
    for name,fn in [('chirp',chirp_tests),('recurrence',recurrence_tests),('memory',memory_tests)]:
        if name in d:continue
        start=time.monotonic();r=fn();r['seconds']=round(time.monotonic()-start,3)
        d[name]=r;OUT.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'block':name,**r}),flush=True)
if __name__=='__main__':main()
