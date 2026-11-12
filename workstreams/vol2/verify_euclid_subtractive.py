#!/usr/bin/env python3
"""New weighted checks for TAOCP4.5.3-35; reuses completed33 cache."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from math import gcd,prod
import json,os,sys,time
from flint import arb,ctx
from verify_euclid_discrete import cf,steps,divisors,phi,mu,factors
from verify_euclid_heilbronn import continuant

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/euclid-subtractive.json'

def pfrac(n):return F(phi(n),n)
def except_p(a,b):return prod((F(p-1,p) for p in factors(a) if b%p),start=F(1))

def subtract(m,n):
    count=0
    while m!=n:
        if m>n:m-=n
        else:n-=m
        count+=1
    return count

def weighted_representations():
    cache=json.loads((ROOT/'results/euclid-heilbronn-representations.json').read_text())
    checks=0;newcuts=0;groups=0;absent=0;truncated=0;boundary=0
    for n in range(1,cache['max_n']+1):
        # Strict quadruples were independently enumerated for33 and are reused.
        reps={tuple(t) for t in cache['strict'][str(n)]}
        for m in range(n//2+1,n):
            d=gcd(m,n);reps.add((m//d,d,(n-m)//d,d))
        recovered={}
        for m in range(1,(n+1)//2):
            a=cf(m,n);d=gcd(m,n);weight=0
            for cut in range(1,len(a)):
                left,right=a[:cut],a[cut:]
                t=(continuant(left),d*continuant(right),continuant(left[:-1]),d*continuant(right[1:]))
                assert t not in recovered
                recovered[t]=a[cut-1];weight+=a[cut-1];newcuts+=1
            tail=a[:-1]+[a[-1]-1]
            t=(continuant(tail),d,continuant(tail[:-1]),d)
            assert t not in recovered
            recovered[t]=a[-1]-1;weight+=a[-1]-1;newcuts+=1
            assert weight==sum(a)-1
        assert set(recovered)==reps
        for t,w in recovered.items():
            x,xp,y,yp=t
            assert w==x//y
            assert n==x*xp+y*yp and x>y>0 and xp>=yp>0 and gcd(x,y)==1
            checks+=1
        w=sum(recovered.values())
        total=sum(sum(cf(m,n)) for m in range(1,n))
        direct=sum(subtract(m,n) for m in range(1,n+1))
        assert total==2*(w+n//2)
        assert direct==2*w+1-n%2==total-(n-1)
        grouped=Counter((y,xp) for x,xp,y,yp in reps if 2*y*xp<n)
        exact=F(0);transformed=F(0)
        for t in reps:
            x,xp,y,yp=t
            if 2*xp*y<n:
                exact+=F(n,xp*y);truncated+=1
                assert 0<F(n,xp*y)-x//y<2
            else:assert x//y==1;boundary+=1
        for y in range(1,n):
            d=gcd(y,n);m=n//d;j=y//d
            for xp in range(1,(n-1)//(2*y)+1):
                if gcd(y,xp)!=d:
                    assert grouped[y,xp]==0;absent+=1;continue
                assert xp%d==0
                k=xp//d
                expected=d*except_p(d,j)
                assert expected.denominator==1 and grouped[y,xp]==expected
                transformed+=F(m,j*k)*except_p(d,j);groups+=1
        assert exact==transformed
        # Independently sum the divisor/j/k expression S5.
        expression=F(0)
        for d in divisors(n):
            m=n//d
            for j in range(1,(n-1)//(2*d*d)+1):
                if gcd(j,m)!=1:continue
                hj=sum((F(1,k) for k in range(1,(n-1)//(2*d*d*j)+1) if gcd(k,j)==1),start=F(0))
                expression+=F(m,j)*except_p(d,j)*hj
        assert expression==exact
    return {'max_n':cache['max_n'],'weighted_quadruples':checks,'weighted_cuts':newcuts,
            'nonempty_fixed_y_xprime_groups':groups,'excluded_gcd_groups':absent,
            'truncated_representations':truncated,'discarded_weight_one_representations':boundary,
            'direct_subtraction_pairs':sum(range(1,cache['max_n']+1)),
            'identities':'S2,S3,S4; exact rational transformed sum before S5 approximation'}

def multiplicative_identities():
    count=0
    for n in range(1,4097):
        lhs=sum((F(n,d)*pfrac(d)*pfrac(n//d) for d in divisors(n)),start=F(0))
        rhs=n*prod((1-F(1,p*p) for p in factors(n)),start=F(1))
        assert lhs==rhs;count+=1
    local=0
    for d in range(1,65):
        for j in range(1,129):
            assert except_p(d,j)*pfrac(j)==pfrac(d)*except_p(j,d)
            assert except_p(j,d)==sum((F(mu(r),r) for r in divisors(j) if gcd(r,d)==1),start=F(0))
            local+=1
    return {'prime_factor_cancellation_inputs':count,'local_euler_and_mobius_inputs':local}

def harmonic_bound():
    ctx.dps=80
    rows=[];count=0
    js=list(range(1,129))+[210,2310,30030,510510,9699690]
    xs=[F(1),F(3,2),F(2),F(5,2),F(7),F(51,2),F(257),F(1001)]
    for j in js:
        c=2+sum((arb(p).log()/(p-1) for p in factors(j)),start=arb(0))
        for x in xs:
            h=sum((F(1,k) for k in range(1,(x.numerator-1)//x.denominator+1) if gcd(k,j)==1),start=F(0))
            if x==1:assert h==0;count+=1;continue
            pj=pfrac(j)
            error=arb(h.numerator)/h.denominator-arb(pj.numerator)/pj.denominator*(arb(x.numerator)/x.denominator).log()
            assert error>0 and error<c,(j,x,error,c)
            count+=1
            if j>128 and x==1001:rows.append({'j':j,'x':'1001','error':str(error),'upper_bound':str(c)})
    return {'inputs':count,'precision_decimal':80,'inequality':'0 <= H_j(x)-P(j)ln(x) <= 2+sum_{p|j}ln(p)/(p-1)','large_primorial_examples':rows}

def normalization_examples():
    # These are new archived observations, not a proof of the conjecture.
    ctx.dps=80;rows=[]
    for n in [101,1009,10007]:
        assert factors(n)=={n:1}
        quotients=sum(sum(cf(m,n)) for m in range(1,n))
        tsum=sum(steps(m,n) for m in range(n))
        tn=arb(tsum)/n;l=arb(2).log();pi=arb.pi()
        rhs=pi**2/(24*l*l)*(tn+arb(1)/2-18*l*l/(pi*pi))**2
        rhs+=6/(pi*pi)*(arb(3)/n-arb(1)/(n*n))*arb(n).log()**2-arb('2.542875')
        assert rhs>0 and rhs<n
        rows.append({'n_prime':n,'quotient_total':quotients,'division_total':tsum,
                     'printed_main_expression':str(rhs),'quotient_total_divided_by_n':str(F(quotients,n)),
                     'average_subtractions_to_equality':str(F(quotients-(n-1),n)),
                     'proof_note':'General contradiction uses total>=n while expression=O(log(n)^2) along primes.'})
    return {'rows':rows,'conjecture_status':'Normalized version not proved; exact intended stopping convention not established.'}

def main():
    print('PID',os.getpid(),flush=True)
    out=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {'scope':'4.5.3-35 and normalization findingC0134','checkpoints':{}}
    for key,fn in [('weighted_representations',weighted_representations),('multiplicative_identities',multiplicative_identities),('harmonic_bound',harmonic_bound),('normalization_examples',normalization_examples)]:
        if key in out['checkpoints']:print('SKIP',key,flush=True);continue
        start=time.monotonic();out['checkpoints'][key]=fn();OUT.write_text(json.dumps(out,indent=2)+'\n')
        print('PASS',key,round(time.monotonic()-start,3),flush=True)
    print('ALL SUBTRACTIVE CHECKPOINTS PASSED',flush=True)

if __name__=='__main__':main()
