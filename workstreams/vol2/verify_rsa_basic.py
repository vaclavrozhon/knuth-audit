"""Exact finite checks for TAOCP 2 pp.404–407 and exercises 32,34,35.

General proofs are in notes/rsa-basic.md. Exhaustive finite checks use
enumerated residues, integer roots, CRT, and Jacobi symbols, not sampling.
Completed checkpoints are resumable and are never recomputed implicitly.
"""
from pathlib import Path
from itertools import combinations
from math import gcd, isqrt, lcm, prod
from fractions import Fraction
import datetime
import json
import os
import time
from verify_primality_jacobi import jacobi

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/rsa-basic.json'


def primes(limit):
    return [n for n in range(2, limit+1)
            if all(n % d for d in range(2, isqrt(n)+1))]


def icbrt(n):
    lo, hi = 0, 1 << ((n.bit_length()+2)//3)
    while lo+1 < hi:
        mid = (lo+hi)//2
        if mid**3 <= n: lo = mid
        else: hi = mid
    assert lo**3 <= n < (lo+1)**3
    return lo


def crt(residues, moduli):
    N = prod(moduli)
    return sum(a*(N//m)*pow(N//m, -1, m)
               for a,m in zip(residues,moduli)) % N


def rsa_inverse_and_broadcast():
    pairs = list(combinations([p for p in primes(100) if p > 3 and p%3 == 2], 2))
    count = 0
    for p,q in pairs:
        N = p*q; d = pow(3, -1, (p-1)*(q-1))
        encrypted = set()
        for x in range(N):
            c = pow(x,3,N); encrypted.add(c)
            z = pow(c,d,N)
            assert z == x
            assert z == crt([pow(c,pow(3,-1,p-1),p),
                             pow(c,pow(3,-1,q-1),q)], [p,q])
            count += 1
        assert len(encrypted) == N
    moduli = [5*11,17*23,29*41]
    for x in range(min(moduli)):
        c = crt([pow(x,3,n) for n in moduli],moduli)
        assert c == x**3 and icbrt(c) == x
    assert 65537 in primes(65537)
    def cost(e): return e.bit_length()-1 + e.bit_count()-1
    assert cost(65537) == 17 and cost(3) == 2
    return dict(rsa_moduli=len(pairs), all_residue_roundtrips=count,
                broadcast_moduli=moduli,broadcast_messages=min(moduli),
                binary_power_multiplications={'3':2,'65537':17})


def order_probabilities():
    pairs = list(combinations([p for p in primes(43) if p > 2], 2))
    instances = residues = ladders = 0
    for p,q in pairs:
        N=p*q
        for m in range(1,65):
            roots = splits = 0
            for x in range(N):
                value=pow(x,m,N)
                roots += value == 1
                splits += 1 < gcd(value-1,N) < N
            a,b=gcd(m,p-1),gcd(m,q-1)
            assert roots == a*b
            assert splits == a*(q-b) + b*(p-a)
            P,Q=Fraction(a,p),Fraction(b,q)
            assert Fraction(splits,N) == P+Q-2*P*Q
            if P>Fraction(1,2) and Q>Fraction(1,2):
                assert m%lcm(p-1,q-1) == 0
            instances+=1; residues+=N
        m=lcm(p-1,q-1); r=m; k=0
        while r%2 == 0: r//=2; k+=1
        success=units=0
        for x in range(N):
            if gcd(x,N)!=1: continue
            units+=1; y=pow(x,r,N)
            for j in range(k):
                z=y*y%N
                if z==1:
                    success += 1 < gcd(y-1,N) < N
                    break
                y=z
        def v2(n): return (n & -n).bit_length()-1
        a,b=sorted([v2(p-1),v2(q-1)])
        expected_failure=Fraction(4**a+2,3*2**(a+b))
        assert Fraction(units-success,units)==expected_failure<=Fraction(1,2)
        ladders+=units
    p,q,p1,q1,m=23,47,11,23,22
    N=p*q; actual=sum(pow(x,m,N)==1 for x in range(N))
    assert actual==44 and m%(p1*q1)!=0
    assert Fraction(actual,N)>Fraction(1,p1*q1)
    return dict(order_instances=instances, enumerated_residues=residues,
                unit_ladders=ladders,
                C0166=dict(p=p,q=q,p1=p1,q1=q1,m=m,N=N,
                           root_count=actual,actual_probability=f'{actual}/{N}',
                           claimed_upper_bound=f'1/{p1*q1}'))


def padding():
    pairs=list(combinations([p for p in primes(100) if p>3 and p%3==2],2))
    messages=representatives=leaking=original_endpoint_failures=0
    endpoint_example=None
    for p,q in pairs:
        N=p*q; M=icbrt(N); H=M**3-M**2
        assert M>=2 and M**3<N
        for x in range(H):
            messages+=1
            # The published 2004 upper endpoint correction is included.
            old_z=[x] if x>=M else [x+y*M for y in range(M*M-M,M*M)]
            for z in old_z:
                assert 0<=z<N
                assert (z%M if z>=H else z)==x
            leaking += x>=M and x**3<N
            # Minimal additional correction: reserve z=M^3 for x=M.
            new_z=[M**3] if x==M else old_z
            for z in new_z:
                assert 0<=z<N and z**3>=N
                decoded=M if z==M**3 else (z%M if z>=H else z)
                assert decoded==x
                assert icbrt(pow(z,3,N))**3 != pow(z,3,N)
                representatives+=1
        # The original inclusive y=M^2 may overflow N, as the known erratum says.
        for x in range(M):
            z=x+M**3; plain=z%N
            decoded=plain%M if plain>=H else plain
            if decoded!=x:
                original_endpoint_failures+=1
                if endpoint_example is None:
                    endpoint_example=dict(N=N,p=p,q=q,M=M,x=x,y=M*M,z=z,decoded=decoded)
    assert leaking==len(pairs)
    assert original_endpoint_failures>0
    return dict(moduli=len(pairs),messages=messages,corrected_representatives=representatives,
                unpadded_boundary_leaks=leaking,
                C0167=dict(N=55,p=5,q=11,M=3,message=3,ciphertext=27),
                known_2004_endpoint_error=dict(failing_messages=original_endpoint_failures,
                                               example=endpoint_example))


def williams():
    ps=[p for p in primes(200) if p%8==3]
    qs=[q for q in primes(200) if q%8==7]
    moduli=roots_checked=encodings=zero_symbol_choices=false_inputs=valid_false=0
    original_failure=None
    for p in ps:
        for q in qs:
            N=p*q; f=(pow(p,q-1,N)-pow(q,p-1,N))%N
            assert f%p==p-1 and f%q==1
            assert jacobi(-1,N)==1 and jacobi(2,N)==jacobi(f,N)==-1
            roots={}
            for x in range(N):
                roots.setdefault(x*x%N,[]).append(x)
                j=jacobi(x,N)
                assert jacobi(-x,N)==j and jacobi(2*x,N)==-j
                assert jacobi(f*x,N)==-j
                roots_checked+=1
            for c,rs in roots.items():
                x=rs[0]
                assert set(rs)=={x,(-x)%N,f*x%N,(-f*x)%N}
                selected=[y for y in rs if y%2==0 and jacobi(y,N)>=0]
                assert len(selected)==1
            valid_unit_cipher=set()
            for x in range((N-5)//8+1):
                choices=[z for z in [4*x+2,8*x+4] if jacobi(z,N)>=0]
                assert choices
                if all(jacobi(z,N)==0 for z in choices):
                    zero_symbol_choices+=len(choices)
                    if original_failure is None:
                        original_failure=dict(p=p,q=q,N=N,x=x,choices=choices)
                for z in choices:
                    assert 0<z<N
                    c=z*z%N
                    y=next(y for y in roots[c] if y%2==0 and jacobi(y,N)>=0)
                    assert y==z
                    decoded=y//4 if y%4==2 else y//8
                    assert decoded==x
                    if gcd(z,N)==1:valid_unit_cipher.add(c)
                    encodings+=1
            phi=(p-1)*(q-1)
            assert 8*len(valid_unit_cipher)==phi+4
            for t in range(N):
                if jacobi(t,N)!=-1:continue
                c=t*t%N
                y=next(y for y in roots[c] if y%2==0 and jacobi(y,N)>=0)
                decoded=y//4 if y%4==2 else y//8
                possible=[z for z in [4*decoded+2,8*decoded,8*decoded+4]
                          if 0<=z<N and z*z%N==c]
                assert y in possible
                assert any(1<gcd(z-t,N)<N for z in possible)
                false_inputs+=1
                valid_false+=c in valid_unit_cipher
            moduli+=1
    assert original_failure is not None and 2*valid_false>false_inputs
    return dict(moduli=moduli,square_root_inputs=roots_checked,
                corrected_encodings=encodings,zero_symbol_choices=zero_symbol_choices,
                false_unit_inputs=false_inputs,false_inputs_with_valid_ciphertext=valid_false,
                known_2004_zero_symbol_error=original_failure)


def padding_randomized():
    """A uniform correction that randomizes every small message, including M.

    The earlier padding checkpoint checked a special-case replacement at M.
    This stronger version gives every x<ceil(cuberoot(N)) the same number of
    random padding choices; successful earlier checkpoints are retained.
    """
    moduli=messages=representatives=0
    for p,q in combinations([p for p in primes(100) if p>3 and p%3==2],2):
        N=p*q; B=icbrt(N)+1; J=N//B; H=(J-B)*B
        assert N>=28 and B<=H<N and H>=N-B*B-B+1
        for x in range(H):
            zs=[x] if x>=B else [x+y*B for y in range(J-B,J)]
            assert len(zs)==(1 if x>=B else B)
            for z in zs:
                assert B<=z<N and z**3>=N
                decoded=z%B if z>=H else z
                assert decoded==x
                representatives+=1
            messages+=1
        moduli+=1
    return dict(moduli=moduli,messages=messages,representatives=representatives,
                formula='B=ceil(cuberoot(N));J=floor(N/B);H=(J-B)B;0<=x<H;'
                        'if x<B use z=x+yB with J-B<=y<J;otherwise z=x;'
                        'decode z>=H by z mod B')


def main():
    state=json.loads(OUT.read_text()) if OUT.exists() else dict(
        started_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        pid=os.getpid(),status='running',checks={})
    print('RSA validator PID',os.getpid(),flush=True)
    checks=[('rsa',rsa_inverse_and_broadcast),('orders',order_probabilities),
            ('padding',padding),('williams',williams),('padding_randomized',padding_randomized)]
    state.update(status='running',expected_checks=[name for name,fn in checks])
    tmp=OUT.with_suffix('.json.tmp');tmp.write_text(json.dumps(state,indent=2)+'\n');tmp.replace(OUT)
    for name,fn in checks:
        if name in state['checks']:
            print(name,'existing passed checkpoint',flush=True);continue
        start=time.monotonic(); result=fn()
        state['checks'][name]=dict(status='passed',seconds=time.monotonic()-start,result=result)
        tmp=OUT.with_suffix('.json.tmp');tmp.write_text(json.dumps(state,indent=2)+'\n');tmp.replace(OUT)
        print(name,state['checks'][name],flush=True)
    state['status']='passed'
    tmp=OUT.with_suffix('.json.tmp');tmp.write_text(json.dumps(state,indent=2)+'\n');tmp.replace(OUT)
    print('ALL FIVE RSA CHECKPOINTS PASSED',flush=True)


if __name__=='__main__':main()
