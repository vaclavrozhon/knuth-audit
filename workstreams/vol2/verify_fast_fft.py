#!/usr/bin/env python3
"""4.3.3C: literal FFT passes, exact cyclotomic oracle, fixed-point arithmetic.
No floating point is used in the correctness or interval certificates.
"""
from pathlib import Path
from math import isqrt
from itertools import product
import json,random,time
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/fast-fft.json'

def reverse(x,k):
    y=0
    for _ in range(k):y=2*y+(x&1);x>>=1
    return y

def raw_passes(values,k,operation):
    """Passes 0..k in the book's actual storage order; no hidden permutation."""
    a=values[:];states=[a]
    for j in range(1,k+1):
        stride=1<<(k-j);z=[None]*(1<<k)
        for h in range(1<<j):
            power=reverse(h,j)*stride
            for t in range(stride):
                i=(h>>1)*2*stride+t
                z[h*stride+t]=operation(a[i],a[i+stride],power)
        a=z;states.append(a)
    return states

def ordinary(raw,k):return [raw[reverse(s,k)] for s in range(1<<k)]

class Cyclotomic:
    """Z[z]/(z^(K/2)+1), where z is a primitive K-th root for K a power of 2."""
    def __init__(self,k):self.k=k;self.K=1<<k;self.d=self.K//2;self.zero=(0,)*self.d
    def integer(self,x):return (x,)+(0,)*(self.d-1)
    def add(self,a,b):return tuple(x+y for x,y in zip(a,b))
    def shift(self,a,p):
        p%=self.K;c=[0]*self.d
        for i,x in enumerate(a):
            q,r=divmod(i+p,self.d);c[r]+=x*(-1 if q%2 else 1)
        return tuple(c)
    def mul(self,a,b):
        c=[0]*self.d
        for i,x in enumerate(a):
            for j,y in enumerate(b):
                if i+j<self.d:c[i+j]+=x*y
                else:c[i+j-self.d]-=x*y
        return tuple(c)
    def direct(self,a,q=1):
        return [tuple(sum(self.shift(a[t],q*s*t)[j] for t in range(self.K))
                      for j in range(self.d)) for s in range(self.K)]
    def passes(self,a,q=1):
        return raw_passes(a,self.k,lambda b,c,p:self.add(b,self.shift(c,q*p)))

def algebra():
    rng=random.Random(43338);cases=0;pass_cells=0;qcases=0
    for k in range(1,6):
        R=Cyclotomic(k);K=R.K
        inputs=[[rng.randrange(-10,11) for _ in range(K)] for _ in range(8)]
        if k<=3:inputs += [list(x)+(K//2)*[0] for x in product(range(2),repeat=K//2)]
        for u in inputs:
            a=[R.integer(x) for x in u];states=R.passes(a);direct=R.direct(a)
            assert ordinary(states[-1],k)==direct
            for j,state in enumerate(states):
                stride=1<<(k-j)
                for h in range(1<<j):
                    A=reverse(h,j)
                    for t in range(stride):
                        want=R.zero
                        for T in range(1<<j):want=R.add(want,R.shift(a[T*stride+t],stride*A*T))
                        assert state[h*stride+t]==want;pass_cells+=1
            for q in [-3,-2,-1,0,2,3]:
                got=ordinary(R.passes(a,q)[-1],k)
                assert got==[direct[(q*s)%K] for s in range(K)];qcases+=1
            v=[rng.randrange(8) for _ in range(K)];vh=ordinary(R.passes([R.integer(x) for x in v])[-1],k)
            wh=[R.mul(x,y) for x,y in zip(direct,vh)]
            w2=ordinary(R.passes(wh)[-1],k)
            conv=[sum(u[i]*v[(r-i)%K] for i in range(K)) for r in range(K)]
            assert w2==[R.integer(K*conv[(-s)%K]) for s in range(K)];cases+=1
    # Exercise 8: raw inverse FFT after raw forward FFT is not identity.
    R=Cyclotomic(2);u=[R.integer(x) for x in [0,1,0,0]]
    wrong=R.passes(R.passes(u)[-1],q=-1)[-1]
    assert wrong==[(0,0),(2,2),(2,0),(0,-2)]
    assert wrong!=[tuple(4*x for x in z) for z in u]
    return dict(cases=cases,pass_formula_cells=pass_cells,powered_root_cases=qcases,seed=43338,
                ex8_four_times_wrong_output=[list(x) for x in wrong],
                ex8_correct_input=[0,1,0,0])

def table1():
    R=Cyclotomic(3)
    def expression(a=0,i=0,w=0,wb=0):return (a,w,i,-wb)
    u=[2,13,4,0,0,0,0,0];v=[5,2,9,0,0,0,0,0]
    uh=ordinary(R.passes([R.integer(x) for x in u])[-1],3)
    vh=ordinary(R.passes([R.integer(x) for x in v])[-1],3)
    wantu=[expression(19),expression(2,4,13),expression(-2,13),expression(2,-4,0,-13),expression(-7),expression(2,4,-13),expression(-2,-13),expression(2,-4,0,13)]
    wantv=[expression(16),expression(5,9,2),expression(-4,2),expression(5,-9,0,-2),expression(12),expression(5,9,-2),expression(-4,-2),expression(5,-9,0,2)]
    wantw=[expression(304),expression(-26,64,69,-125),expression(-18,-56),expression(-26,-64,125,-69),expression(-84),expression(-26,64,-69,125),expression(-18,56),expression(-26,-64,-125,69)]
    wh=[R.mul(x,y) for x,y in zip(uh,vh)]
    assert uh==wantu and vh==wantv and wh==wantw
    second=ordinary(R.passes(wh)[-1],3)
    assert second==[R.integer(x) for x in [80,0,0,0,288,1000,512,552]]
    W=[10,69,64,125,36,0,0,0];assert sum(x<<(4*i) for i,x in enumerate(W))==1234*2341
    return dict(all_40_table_cells_exact=True,coefficient_oracle=W,answer=1234*2341,
                errata_scales=dict(u_hat=128,v_hat=128),note='2015 v-column correction is 2^7, not 2^16: original erratum image read.')

def truncdiv(x,B):return x//B if x>=0 else -((-x)//B)
def cmul(a,b,B):return (truncdiv(a[0]*b[0]-a[1]*b[1],B),truncdiv(a[0]*b[1]+a[1]*b[0],B))
def norm2(z):return z[0]*z[0]+z[1]*z[1]
def ceildiv(a,b):return (a+b-1)//b
def ceilsqrt(a):
    q=isqrt(a);return q+(q*q<a)

def certified_roots(k,m):
    """Interval evaluation of (46); exact rational endpoints and integer sqrt.
    Each returned coordinate is the certified floor of the true coordinate*2^m.
    Extra precision also prevents reuse of a rounded x as an exact denominator.
    """
    guard=16;B=1<<m
    while True:
        S=1<<(m+guard);scale=1<<guard;roots={1:(-B,0),2:(0,B)}
        xl=xu=0;yl=yu=S;ok=True
        for r in range(2,k):
            nxl=isqrt(S*(S+xl)//2);nxu=ceilsqrt(S*(S+xu)//2)
            nyl=yl*S//(2*nxu);nyu=ceildiv(yu*S,2*nxl)
            xl,xu,yl,yu=nxl,nxu,nyl,nyu
            if xl//scale!=xu//scale or yl//scale!=yu//scale:ok=False;break
            roots[r+1]=(xl//scale,yl//scale)
            assert norm2(roots[r+1])<=B*B
        if ok:return roots,guard
        guard*=2;assert guard<=1024

def fixed_transform(a,k,powers,m):
    B=1<<m;maxnorm=0
    def operation(b,c,p):
        nonlocal maxnorm
        w=powers[p]
        z=(truncdiv(B*b[0]+w[0]*c[0]-w[1]*c[1],B),
           truncdiv(B*b[1]+w[0]*c[1]+w[1]*c[0],B))
        nn=norm2(z);assert nn<B*B;maxnorm=max(maxnorm,nn)
        return z
    raw=raw_passes(a,k,operation)[-1]
    return ordinary(raw,k),maxnorm

def fixed_multiply(u,v,k,l,m,verify=True):
    K=1<<k;B=1<<m;mask=(1<<l)-1
    assert u.bit_length()<=K*l//2 and v.bit_length()<=K*l//2 and m>=k+l
    roots,guard=certified_roots(k,m);powers=[(B,0)]
    for j in range(1,K):
        bit=j&-j;t=bit.bit_length()-1
        powers.append(cmul(powers[j-bit],roots[k-t],B));assert norm2(powers[-1])<=B*B
    U=[(u>>(l*i))&mask for i in range(K)];V=[(v>>(l*i))&mask for i in range(K)]
    shift=m-k-l
    uh,m1=fixed_transform([(x<<shift,0) for x in U],k,powers,m)
    vh,m2=fixed_transform([(x<<shift,0) for x in V],k,powers,m)
    wh=[cmul(x,y,B) for x,y in zip(uh,vh)]
    w2,m3=fixed_transform(wh,k,powers,m)
    # Exact division by K is combined with final scaling; no extra truncation.
    W=[]
    for r in range(K):
        numerator=w2[(-r)%K][0]*(1<<(k+2*l))
        W.append((2*numerator+B)//(2*B))
    w=sum(x<<(l*i) for i,x in enumerate(W))
    if verify:
        assert w==u*v
        # A separate coefficient convolution verifies every recovered integer.
        expected=[sum(U[i]*V[r-i] for i in range(max(0,r-K//2+1),min(r,K//2-1)+1)) for r in range(K)]
        assert W==expected
    return w,dict(root_guard_bits=guard,max_norm_squared=[m1,m2,m3],scale_squared=B*B)

def fixed_tests():
    rng=random.Random(43349);rows=[];cases=0
    for k in [7,8,9,10,11,12]:
        for l in [1,k]:
            n=(1<<k)*l//2;m=4*k+2*l;mask=(1<<n)-1
            pairs=[(0,mask),(mask,mask),(1<<(n-1),1<<(n-1))]
            pairs += [(rng.getrandbits(n),rng.getrandbits(n)) for _ in range(2)]
            max_ratio=0;guard=0
            for u,v in pairs:
                _,s=fixed_multiply(u,v,k,l,m);cases+=1
                max_ratio=max(max_ratio,max(s['max_norm_squared'])/s['scale_squared']);guard=max(guard,s['root_guard_bits'])
            rows.append(dict(k=k,l=l,m=m,n=n,cases=len(pairs),root_guard_bits=guard,max_norm_squared_ratio_display=max_ratio))
    for k,l,m,u,v in [(3,4,24,1234,2341),(11,8,60,rng.getrandbits(8192),rng.getrandbits(8192))]:
        _,s=fixed_multiply(u,v,k,l,m);cases+=1;rows.append(dict(k=k,l=l,m=m,n=max(u.bit_length(),v.bit_length()),cases=1,**s))
    wrong,_=fixed_multiply(1234,2341,3,4,7,verify=False)
    assert wrong!=1234*2341
    # Exact squared sufficient-precision criterion, including corrected m=144.
    for k,l,m in [(11,8,60),(15,15,90),(27,27,144)]:
        assert (1<<(2*m))>=k*k*(1<<(6*k+4*l+7))
    return dict(seed=43349,cases=cases,rows=rows,insufficient_precision_example=dict(k=3,l=4,m=7,got=wrong,expected=1234*2341),
                note='All correctness and interval tests exact; displayed norm ratios alone use floating point.')

def main():
    d=json.loads(OUT.read_text()) if OUT.exists() else {}
    for name,fn in [('algebra',algebra),('table1',table1),('fixed_point',fixed_tests)]:
        if name in d:continue
        start=time.monotonic();r=fn();r['seconds']=round(time.monotonic()-start,3)
        d[name]=r;OUT.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'block':name,**r}),flush=True)
if __name__=='__main__':main()
