"""Independent exact oracles for 3.2.1.1 text and exercises 1--11."""
from math import gcd, isqrt
from pathlib import Path
import json
import random
import sympy

ROOT=Path(__file__).resolve().parent


class Mix:
    """Numeric part of signed-magnitude MIX; +/-0 both compare as zero."""
    def __init__(self,w,ov=False):
        self.w=w; self.a=0; self.x=0; self.ov=ov

    def add(self,v):
        total=self.a+v
        if abs(total)>=self.w:
            self.ov=True
        self.a=(-1 if total<0 else 1)*(abs(total)%self.w)

    def mul(self,v):
        total=self.a*v; hi,lo=divmod(abs(total),self.w)
        sign=-1 if total<0 else 1
        self.a=sign*hi; self.x=sign*lo

    def slax5(self):
        self.a=(-1 if self.a<0 else 1)*abs(self.x); self.x=0

    def jnov(self):
        jump=not self.ov; self.ov=False
        return jump


def schrage(a,x,m):
    if a==0:
        return 0
    q,r=divmod(m,a); h=x//q
    u=q*h; v=a*(x-u); z=r*h
    assert all(0<=y<m for y in [u,v,z]),(a,x,m,u,v,z)
    return (v-z) % m


def main():
    counts=dict(mix_word=0,mix_plus=0,mix_skip=0,mix_minus=0,mix_sum_difference=0,
                montgomery=0,small_schrage=0,lucky_counts=0,decompositions=0,
                concrete_large=0)
    for w in [8,16,32,64]:
        for a in range(w):
            for x in range(w):
                # Text program (2), with overflow initially off.
                p=Mix(w);p.a=-x;p.mul(a);p.add(-p.x)
                if p.a<0:
                    p.add(2);p.add(w-1)
                expected=a*x%(w+1)
                assert p.a==expected%w and p.ov==(expected==w)
                counts['mix_plus']+=1
                # Variant which skips the unrepresentable state w.
                p=Mix(w);p.a=-x
                for runs in range(2):
                    p.mul(a);p.add(-p.x)
                    if p.a>=0:
                        break
                    p.add(2)
                    if p.a>0:
                        continue
                    p.add(w-1)
                    break
                else:
                    raise AssertionError('Skip variant failed to return')
                if expected==w:
                    expected=a*w%(w+1)
                assert p.a==expected and not p.ov
                counts['mix_skip']+=1
                # Answer 8, including the equivalent encodings 0 and w-1.
                p=Mix(w,True);p.ov=False;p.a=x;p.mul(a);p.add(p.x)
                if not p.jnov():
                    p.add(1)
                assert p.a%(w-1)==a*x%(w-1) and not p.ov
                counts['mix_minus']+=1
                for c in range(w):
                    p=Mix(w);p.a=a;p.mul(x);p.slax5();p.add(c)
                    assert p.a==(a*x+c)%w and p.x==0
                    # Answer 2's JNOV-return / JMP-back clears either flag.
                    if not p.jnov():
                        assert p.jnov()
                    assert not p.ov
                    if gcd(a,w)==1:
                        cp=pow(a,-1,w)*c%w
                        q=Mix(w);q.a=x;q.add(cp);q.mul(a)
                        assert q.x==(a*x+c)%w
                    counts['mix_word']+=1
        for m in range(1,w):
            for x in range(m):
                for y in range(m):
                    p=Mix(w);p.a=x;p.add(-y)
                    if p.a<0:p.add(m)
                    assert p.a==(x-y)%m and not p.ov
                    p=Mix(w);p.a=x;p.add(-m);p.add(y)
                    if p.a<0:p.add(m)
                    assert p.a==(x+y)%m and not p.ov
                    counts['mix_sum_difference']+=1
            if gcd(m,w)==1:
                for a in range(1,m):
                    ap=a*w%m;mp=pow(m,-1,w)
                    for x in range(m):
                        z,y=divmod(ap*x,w);t=mp*y%w;u=m*t//w
                        answer=z-u+(m if z<u else 0)
                        assert answer==a*x%m
                        counts['montgomery']+=1
    # Necessity/sufficiency of r<=q and the exact count in answer 10.
    for m in range(1,2001):
        lucky=0
        for a in range(1,m):
            q,r=divmod(m,a)
            safe=r*((m-1)//q)<m
            assert safe==(r<=q)
            lucky+=safe
            if m<=64 and safe:
                for x in range(m):
                    assert schrage(a,x,m)==a*x%m
                    counts['small_schrage']+=1
        t=isqrt(m);divisors=sum(m%d==0 for d in range(1,t+1))
        tau=2*divisors-(t*t==m)
        expected=2*t+tau//2-(m<=t*t+t)-1
        assert expected==lucky,(m,expected,lucky)
        counts['lucky_counts']+=1
        # The trivial a^2<=m case also avoids small-m decomposition issues.
        for a in range(1,m//2+1):
            if a*a<=m:
                continue
            ap=isqrt(m-1); app=(a+ap-1)//ap; appp=ap*app-a
            assert ap*app-appp==a
            assert 0<=appp<ap and ap*ap<m and app*app<m
            counts['decompositions']+=1
    m=2**31-1;a=62089911
    lucky=lambda t:t==0 or m%t<=m//t
    divisors=sympy.divisors(m-1)
    triples=[(int(d),int((a+d-1)//d),int(d*((a+d-1)//d)-a))
             for d in divisors if lucky((a+d-1)//d) and lucky(d*((a+d-1)//d)-a)]
    pairs=[(int(d),int(a//d)) for d in sympy.divisors(a)
           if d<=a//d and lucky(d) and lucky(a//d)]
    assert len(divisors)==192 and len(triples)==86
    assert len(sympy.divisors(a))==24 and len(pairs)==5
    assert 3641*17053-62==a
    rng=random.Random(32112026)
    xs={0,1,m-1,m-2,*[rng.randrange(m) for _ in range(20000)]}
    for d in [125929,589806,34636833,2432031,30540]:
        for h in [1,2,m//d-1,m//d]:
            xs.update(v for v in [h*d-1,h*d,h*d+1] if 0<=v<m)
    for x in sorted(xs):
        assert (schrage(3641,schrage(17053,x,m),m)-schrage(62,x,m))%m==a*x%m
        assert schrage(70317,schrage(883,x,m),m)==a*x%m
        assert schrage(883,schrage(70317,x,m),m)==a*x%m
        counts['concrete_large']+=1
    result=dict(status='all assertions passed',checks=counts,
                example=dict(m=m,a=a,lucky_divisors=len(triples),factorizations=pairs),
                scope='Text programs and exercises 1--11; mathematical proofs supply general bounds.')
    (ROOT/'results/modulus-arithmetic.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
