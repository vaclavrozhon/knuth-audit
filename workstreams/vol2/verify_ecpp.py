"""Independent exact verification of PARI ECPP certificates.

Only Python integer arithmetic is used for elliptic-curve operations.
Terminal primes below 2^64 are proved by recursive Lucas certificates;
SymPy factors p-1 to propose certificates, not to accept primality.
See notes/lagged-periods.md for the mathematical criterion and scope.
"""
from math import gcd,isqrt,prod
from pathlib import Path
import json
import sympy

ROOT=Path(__file__).resolve().parent


def add(P,Q,a,n):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u:
        if (y+v)%n==0:return None
        assert y==v
        numerator=3*x*x+a;denominator=2*y
    else:
        numerator=v-y;denominator=u-x
    assert gcd(denominator,n)==1,('nonunit denominator',n)
    slope=numerator*pow(denominator,-1,n)%n
    xx=(slope*slope-x-u)%n
    return xx,(slope*(x-xx)-y)%n


def multiply(k,P,a,n):
    result=None
    while k:
        if k&1:result=add(result,P,a,n)
        k>>=1
        if k:P=add(P,P,a,n)
    return result


class Verifier:
    def __init__(self):
        self.small={2:dict(prime=2)}
        self.links=0

    def prove_small(self,n):
        assert 1<n<2**64
        if n in self.small:return
        fs=[(int(p),int(e)) for p,e in sympy.factorint(n-1).items()]
        assert prod(p**e for p,e in fs)==n-1
        for p,e in fs:
            assert e>0 and p<n
            self.prove_small(p)
        for a in range(2,10000):
            if pow(a,n-1,n)==1 and all(gcd(pow(a,(n-1)//p,n)-1,n)==1 for p,e in fs):
                self.small[n]=dict(prime=n,witness=a,factors=fs)
                return
        raise AssertionError(('No terminal Lucas certificate',n))

    def verify(self,cert,target):
        if isinstance(cert,int):
            assert target==cert;self.prove_small(cert);return
        assert cert and cert[0][0]==target
        next_prime=None
        for N,t,s,a,P in reversed(cert):
            assert N>3 and t*t<4*N and s>0
            m=N+1-t;assert m%s==0
            q=m//s;assert q<N
            if next_prime is None:self.prove_small(q)
            else:assert q==next_prime
            # A slightly stronger, wholly integer sufficient lower bound.
            floor_fourth=isqrt(isqrt(N))
            ceil_fourth=floor_fourth+(floor_fourth**4<N)
            assert q>(ceil_fourth+1)**2
            x,y=P;assert 0<=x<N and 0<=y<N
            b=(y*y-x*x*x-a*x)%N
            assert gcd(4*a*a*a+27*b*b,N)==1
            # S has affine coordinates modulo every prime divisor of N.
            S=multiply(s,tuple(P),a,N);assert S is not None
            assert multiply(q,S,a,N) is None
            next_prime=N;self.links+=1

    def validate_small_certificates(self):
        proved={2}
        for n in sorted(self.small):
            if n==2:continue
            c=self.small[n];a=c['witness'];fs=c['factors']
            assert all(p in proved and e>0 for p,e in fs)
            assert prod(p**e for p,e in fs)==n-1
            assert pow(a,n-1,n)==1
            assert all(gcd(pow(a,(n-1)//p,n)-1,n)==1 for p,e in fs)
            proved.add(n)


def main():
    from certify_lagged_primes import targets
    v=Verifier();checked=[]
    for target in targets():
        path=ROOT/'results/lagged-prime-certificates'/f'{target["id"]}.json'
        row=json.loads(path.read_text());assert row['target']==target
        v.verify(row['certificate'],target['value'])
        checked.append(target['id']);print(target['id'], 'verified',flush=True)
    extra=ROOT/'results/marsaglia-zaman-factors.json'
    if extra.exists():
        for row in json.loads(extra.read_text())['factor_certificates']:
            v.verify(row['certificate'],row['prime'])
    v.validate_small_certificates()
    result=dict(status='passed',targets=checked,elliptic_curve_links=v.links,
                small_lucas_certificates=[v.small[p] for p in sorted(v.small)],
                method='Exact affine group operations, invertibility checks, Hasse bound; recursive Lucas terminal proofs')
    (ROOT/'results/lagged-primes-validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print('ALL',len(checked),'targets verified;',v.links,'ECPP links;',len(v.small),'small prime certificates')


if __name__=='__main__':main()
