#!/usr/bin/env python3
"""4.3.1-40: exact low digits and certified approximate high digits."""
from pathlib import Path
from collections import Counter
from fractions import Fraction
import argparse,json,random,time
from verify_classical_special import d3
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/classical-exact.json'


def ndigits(x,b):
    assert x>0
    n=0
    while x:n+=1;x//=b
    return n


def mul_digit(x,q,b,n):
    """Exactly n one-word products and the usual multiply-add carry loop."""
    assert 0<=q<b and x<b**n
    out=[];carry=0
    for _ in range(n):
        x,a=divmod(x,b);t=a*q+carry;carry,z=divmod(t,b);out.append(z)
    out.append(carry);ans=0
    for z in reversed(out):ans=ans*b+z
    return ans


def short_divrem(R,D,b,stats):
    """R/D bounded by b+1; normalized D, one ordinary digit after a shift."""
    n=ndigits(D,b);assert D//b**(n-1)>=b//2
    high=0
    if R>=b*D:R-=b*D;high=b;stats['redundant_digits']+=1
    assert 0<=R<b*D
    if n==1:q,r=divmod(R,D);stats['word_divisions']+=1
    else:
        q,tr=d3(R//b**n,R//b**(n-1)%b,R//b**(n-2)%b,D//b**(n-1),D//b**(n-2)%b,b)
        stats['word_divisions']+=1;stats['estimate_products']+=len(tr)
        r=R-mul_digit(D,q,b,n);stats['high_products']+=n
        if r<0:q-=1;r+=D;stats['addbacks']+=1
    assert 0<=r<D and R==q*D+r
    q+=high;assert q<=b+1
    return q,r


def low_digits(U,V,b,k):
    assert b&(b-1)==0 and V>0
    s=(V&-V).bit_length()-1
    assert U%(1<<s)==0
    a=(U>>s)%(b**k);v=V>>s;inv=pow(v,-1,b)
    Q=0;count=0
    for j in range(k):
        mod=b**(k-j);q=(a%b)*inv%b;Q+=q*b**j;count+=1
        if j<k-1:
            product=mul_digit(v%mod,q,b,k-j);count+=k-j
            a=(a-product)%mod;assert a%b==0;a//=b
    assert Q==(U//V)%(b**k)
    assert count== (k*(k+3)//2-1 if k else 0)
    return Q,count,s


def hybrid(U,V,b,n):
    assert b**(n-1)<=V<b**n and U<b**(2*n) and U%V==0
    k=n//2
    low,lowproducts,s=low_digits(U,V,b,k)
    bits=b.bit_length()-1;shift=bits-(V//b**(n-1)).bit_length();d=1<<shift
    A=d*U;B=d*V;assert b**n//2<=B<b**n
    g=0
    while True:
        L=n-k+g
        if b**g>4*(b+(b+1)*L):break
        g+=1
    # Prefix at fixed precision L: all later divisors just drop one low word.
    R=A*b**L//b**(2*n);D=B*b**L//b**n
    Z=0;stats=Counter()
    for j in range(L):
        assert D==B*b**(L-j)//b**n and D>0
        q,R=short_divrem(R,D,b,stats);Z=Z*b+q;D//=b
    # y=Z/b^(L-1), approximate Q=b^n*y; join with exact low residue.
    exp=n-L+1
    if exp>=0:num=Z*b**exp-low;den=b**k
    else:num=Z-low*b**(-exp);den=b**(k-exp)
    high=(2*num+den)//(2*den);Q=high*b**k+low
    assert Q==U//V and Q*V==U
    approx=Fraction(Z*b**n,b**(L-1))
    bound=Fraction(2*(b+(b+1)*L)*b**n,b**L)
    assert abs(approx-Q)<bound<Fraction(b**k,2)
    stats['low_products']=lowproducts
    return Q,{'n':n,'b':b,'k':k,'g':g,'L':L,'removed_low_bits':s,'counts':dict(stats),'principal_products':lowproducts+stats['high_products'],'relative_to_D':(lowproducts+stats['high_products'])/(n*(n+1))}


def complete_block():
    counts=Counter();cases=0;maxg=0
    for b,ns in [(2,range(2,8)),(4,range(2,4))]:
        for n in ns:
            for V in range(b**(n-1),b**n):
                for Q in range((b**(2*n)-1)//V+1):
                    U=V*Q;q,r=hybrid(U,V,b,n);counts.update(r['counts']);cases+=1;maxg=max(maxg,r['g'])
    return {'complete_inputs':cases,'counts':dict(counts),'max_guard':maxg}


def large_block():
    rng=random.Random(43140);counts=Counter();samples=[]
    for _ in range(800):
        b=1<<rng.choice([1,2,4,8,16,32]);n=rng.randrange(2,65)
        V=rng.randrange(b**(n-1),b**n);Q=rng.randrange((b**(2*n)-1)//V+1)
        q,r=hybrid(V*Q,V,b,n);counts.update(r['counts'])
    for n in [16,32,64,128,256,512]:
        b=2**32;V=rng.randrange(b**(n-1),b**n);Q=rng.randrange(b**n)
        q,r=hybrid(V*Q,V,b,n);samples.append(r)
    return {'larger_inputs':800,'counts':dict(counts),'cost_samples':samples}


def witness_block():
    b=2;n=4;U=165;V=15;inv=pow(V,-1,b);w0=U*inv%b
    printed_u=U-w0*V;printed_w1=inv*(printed_u%b)%b
    corrected_u=printed_u//b;corrected_w1=inv*(corrected_u%b)%b
    assert ndigits(U,b)==2*n and ndigits(V,b)==n and ndigits(U//V,b)==n
    assert U%V==0 and printed_w1!=((U//V)//b)%b==corrected_w1
    q,meta=hybrid(U,V,b,n)
    return {'b':b,'n':n,'U':U,'V':V,'Q':q,'w0':w0,'printed_u_prime':printed_u,'printed_w1':printed_w1,'corrected_u_prime':corrected_u,'corrected_w1':corrected_w1,'low_digits':low_digits(U,V,b,n//2)[0]}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');a=ap.parse_args()
    if OUT.exists() and not a.resume:raise SystemExit('Use --resume')
    data=json.loads(OUT.read_text()) if OUT.exists() else {'scope':'4.3.1-40; power-of-two radix; certified guard and exact merge','blocks':{}}
    for name,fn in [('complete',complete_block),('large',large_block),('missing_shift',witness_block)]:
        if name in data['blocks']:continue
        start=time.monotonic();r=fn();r['elapsed_seconds']=time.monotonic()-start;data['blocks'][name]=r
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,'PASS',flush=True)
    print('ALL CHECKPOINTS COMPLETE',flush=True)
if __name__=='__main__':main()
