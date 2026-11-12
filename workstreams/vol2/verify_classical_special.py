#!/usr/bin/env python3
"""Exact and interval checks for TAOCP4.3.1-36,37,41; resume completed blocks."""
from collections import Counter
from decimal import Decimal, localcontext
from math import gcd,isqrt
from pathlib import Path
import argparse,json,random,time
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/classical-special.json'


def quad_sign(a,b):
    """Sign of a+b*sqrt(5), for integer coefficients."""
    if not b:return (a>0)-(a<0)
    if not a:return (b>0)-(b<0)
    if a>0 and b>0:return 1
    if a<0 and b<0:return -1
    d=a*a-5*b*b
    return ((d>0)-(d<0))*(1 if a>0 else -1)


def logphi_interval(p):
    # Fixed point; the only large divisions are by small positive integers.
    q=p+(p+1).bit_length()+10;S=1<<q
    sqrt_floor=isqrt(5*S*S) # Supplies the GIVEN approximation of phi.
    xlo,xhi=sqrt_floor,sqrt_floor+1
    lo=hi=0;k=0
    while True:
        k+=1;xlo//=5;xhi=(xhi+4)//5
        d=2*k-1;lo+=xlo//d;hi+=(xhi+d-1)//d
        tail=(xhi+4*(2*k+1)-1)//(4*(2*k+1))
        upper=hi+tail
        if upper-lo<=1<<(q-p):break
    with localcontext() as c:
        c.prec=int(q*.302)+40
        actual=((Decimal(1)+Decimal(5).sqrt())/2).ln()
        assert Decimal(lo)/S<actual<Decimal(upper)/S
    return {'bits':p,'working_bits':q,'terms':k,'lower_numerator':str(lo),'upper_numerator':str(upper),'denominator_power_of_two':q,'width_ticks':upper-lo}


def log_block():
    cases=steps=0;max_delay=0;sample=[]
    for n in list(range(1,129))+[256,512,1024]:
        D=1<<(2*n);threshold=1<<n
        # All values are pairs (a,b) meaning (a+b sqrt(5))/D.
        for eps_units in [-1,0,1]:
            prev=(D,0);curr=(-D//2+eps_units,D//2)
            true_prev=(D,0);true_curr=(-D//2,D//2)
            fprev,f=0,1;k=1;K=None
            while True:
                if K is None and quad_sign(true_curr[0]-threshold,true_curr[1])<0:K=k
                assert curr[1]==true_curr[1]
                err=curr[0]-true_curr[0]
                assert err==(-1)**(k+1)*f*eps_units
                assert abs(err)<=1<<(n+1)
                steps+=1
                if quad_sign(curr[0]-threshold,curr[1])<0:break
                prev,curr=curr,(prev[0]-curr[0],prev[1]-curr[1])
                true_prev,true_curr=true_curr,(true_prev[0]-true_curr[0],true_prev[1]-true_curr[1])
                fprev,f=f,fprev+f;k+=1
            if K is not None:max_delay=max(max_delay,k-K)
            cases+=1
            if n in [1,2,128,1024]:sample.append({'n':n,'eps_units':eps_units,'stop':k,'error_numerator':str(err),'denominator_bits':2*n})
    intervals=[logphi_interval(p) for p in [1,2,4,8,16,32,64,128,256,512,1024,2048]]
    return {'power_runs':cases,'power_steps':steps,'max_delay_beyond_exact_threshold':max_delay,'samples':sample,'certified_log_intervals':intervals}


def ds(x,b,n):return [(x//b**i)%b for i in range(n)]


def d3(h,l,z,a,c,b):
    q,r=divmod(h*b+l,a);trace=[q]
    while q>=b or q*c>b*r+z:
        q-=1;r+=a;trace.append(q)
        if r>=b:break
    assert 0<=q<b
    return q,trace


def virtual_division(U,V,b,m,n):
    bits=b.bit_length()-1;assert b==1<<bits
    vs=ds(V,b,n);e=bits-vs[-1].bit_length();d=1<<e
    def digit(v,i):return v[i] if 0<=i<len(v) else 0
    def shifted(v,i):
        return ((digit(v,i)<<e)&(b-1)) | (digit(v,i-1)>>(bits-e) if e else 0)
    a,c=shifted(vs,n-1),shifted(vs,n-2)
    normalV=d*V;assert (a,c)==(normalV//b**(n-1),normalV//b**(n-2)%b)
    R=U;normalR=d*U;Q=0;stats=Counter();traces=[]
    for j in range(m,-1,-1):
        us=ds(R,b,m+n+1)
        top=[shifted(us,i) for i in [j+n,j+n-1,j+n-2]]
        physical=[normalR//b**i%b for i in [j+n,j+n-1,j+n-2]]
        assert top==physical
        q,trace=d3(*top,a,c,b);p,ptrace=d3(*physical,a,c,b);assert trace==ptrace
        raw=R//b**j-q*V;physical_raw=normalR//b**j-p*normalV
        assert (raw<0)==(physical_raw<0)
        addback=raw<0
        if addback:q-=1;p-=1;raw+=V;physical_raw+=normalV;stats['addbacks']+=1
        assert 0<=raw<V and 0<=physical_raw<normalV
        R=raw*b**j+R%b**j
        normalR=physical_raw*b**j+normalR%b**j
        assert normalR==d*R
        Q+=q*b**j;stats['iterations']+=1;stats['d3_decrements']+=len(trace)-1
        traces.append([j,trace,addback])
    assert (Q,R)==divmod(U,V)
    stats['no_shift' if e==0 else 'shifted']+=1
    return Q,R,stats,traces


def virtual_block():
    stats=Counter();cases=0;rng=random.Random(43137)
    for b in [2,4]:
        for n in [2,3]:
            for m in [0,1]:
                for V in range(b**(n-1),b**n):
                    for U in range(b**(m+n)):
                        _,_,s,_=virtual_division(U,V,b,m,n);stats.update(s);cases+=1
    for _ in range(4000):
        b=1<<rng.choice([1,2,3,4,8,16]);n=rng.randrange(2,9);m=rng.randrange(7)
        U=rng.randrange(b**(m+n));V=rng.randrange(b**(n-1),b**n)
        _,_,s,_=virtual_division(U,V,b,m,n);stats.update(s)
    assert stats['addbacks'] and stats['no_shift'] and stats['shifted']
    return {'complete_inputs':cases,'larger_inputs':4000,'counts':dict(stats),'scope':'Every trial digit including D3 decrements and D6 borrow agrees with fully shifted reference; independent final divmod.'}


def reduction(U,w,b,m,n):
    s=-1 if U<0 else 1;t=abs(U);inv=pow(w,-1,b)
    assert t<b**(m+n) and w<b**n
    for k in range(m):
        x=(t%b)*inv%b
        assert (t-x*w)%b==0
        t=(t-x*w)//b
        assert -w<t<b**(m+n-k-1)
    t*=s
    assert abs(t)<b**n and (b**m*t-U)%w==0
    return t


def bmult(U,V,w,b,n):
    sign=(-1 if U<0 else 1)*(-1 if V<0 else 1);u,v=abs(U),abs(V)
    assert u<w and v<w and w<b**n
    inv=pow(w,-1,b);t=prefix=0;stats=Counter()
    for k in range(n):
        uk=u//b**k%b;prefix+=uk*b**k
        t+=uk*v;x=(t%b)*inv%b
        assert (t-x*w)%b==0
        t=(t-x*w)//b
        assert -w<t<=v and (v>0 or t==0)
        assert (b**(k+1)*t-prefix*v)%w==0
        if t<0:stats['negative_states']+=1
    t*=sign
    assert abs(t)<w and (b**n*t-U*V)%w==0
    assert t%w==(U*V*pow(b**n,-1,w))%w
    return t,stats


def inverse2(w,bits):
    assert w%2;x=1;p=1
    while p<bits:
        p=min(2*p,bits);x=x*(2-w*x)%(1<<p)
        assert w*x%(1<<p)==1
    assert x==pow(w,-1,1<<bits)
    return x


def montgomery_block():
    rng=random.Random(43141);cases=0;stats=Counter();reductions=0
    for b in range(2,11):
        for w in range(1,41):
            if gcd(b,w)!=1:continue
            n=1
            while w>=b**n:n+=1
            for u in range(-w+1,w):
                for v in range(-w+1,w):
                    t,s=bmult(u,v,w,b,n);stats.update(s);cases+=1
            for m in range(4):
                bound=b**(m+n)
                for U in [0,1,bound-1,-1,1-bound,rng.randrange(-bound+1,bound)]:
                    reduction(U,w,b,m,n);reductions+=1
    conversions=0
    for _ in range(1000):
        b=rng.choice([2,3,4,7,10,16,256]);n=rng.randrange(1,14)
        w=rng.randrange(1,b**n)
        if gcd(b,w)!=1:continue
        u,v=rng.randrange(w),rng.randrange(w);a=pow(b,2*n,w)
        ru,_=bmult(u,a,w,b,n);rv,_=bmult(v,a,w,b,n)
        t,_=bmult(ru,rv,w,b,n);result,_=bmult(t,1%w,w,b,n)
        assert result%w==u*v%w and ru%w==b**n*u%w
        conversions+=1
    inverses=0
    for bits in range(1,257):
        for _ in range(5):inverse2(rng.getrandbits(bits)|1,bits);inverses+=1
    # Literal mixed-sign reading with Euclidean remainders; contextual caveat only.
    t=0;trace=[t]
    for k in range(3):
        t+=((6>>k)&1)*(-6);t=(t-(t%2)*7)//2;trace.append(t)
    assert trace==[0,0,-3,-8]
    return {'signed_products':cases,'reductions':reductions,'conversion_chains':conversions,'newton_inverses':inverses,'counts':dict(stats),'literal_mixed_sign_trace':trace,'signed_scope':'Multiply magnitudes then attach product sign, as in the section signed-magnitude convention; literal mixed-sign Euclidean-remainder reading is not asserted correct.'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');a=ap.parse_args()
    if OUT.exists() and not a.resume:raise SystemExit('Use --resume')
    data=json.loads(OUT.read_text()) if OUT.exists() else {'scope':'4.3.1-36/37/41','blocks':{}}
    for name,fn in [('logphi36',log_block),('virtual37',virtual_block),('montgomery41',montgomery_block)]:
        if name in data['blocks']:continue
        start=time.monotonic();r=fn();r['elapsed_seconds']=time.monotonic()-start;data['blocks'][name]=r
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,'PASS',flush=True)
    print('ALL CHECKPOINTS COMPLETE',flush=True)
if __name__=='__main__':main()
