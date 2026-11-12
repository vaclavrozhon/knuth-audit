"""Exact orders and certificates for exercise 3.2.1.2-22.

The factorization was found with PARI, but its product and the order witnesses
are checked here. Large factor primality uses certificates checked separately
by verify_ecpp.py. Small decimal examples use recursive Lucas proofs.
"""
from math import gcd,lcm,prod
from pathlib import Path
import json
import subprocess
import sys
import sympy
from verify_carry_generators import prime_certificates

ROOT=Path(__file__).resolve().parent


def exact_order(a,m,fs):
    n=prod(p**e for p,e in fs)
    assert pow(a,n,m)==1
    assert all(pow(a,n//p,m)!=1 for p,e in fs)
    return n


def main():
    # Decimal values and factors printed on p.550.
    examples=[(9999998999,[(439,1),(22779041,1)],[219,11389520],2494304880),
              (9999999001,[(9999999001,1)],[4999999500],4999999500),
              (10000000999,[(10000000999,1)],[5000000499],5000000499),
              (10000001001,[(3,1),(17,1),(2687,1),(72973,1)],[1,16,2686,12162],130668528)]
    small_primes=set();rows=[]
    for m,fs,orders,expected in examples:
        assert prod(p**e for p,e in fs)==m
        assert lcm(*orders)==expected
        checks=[]
        for (p,e),order in zip(fs,orders):
            small_primes.add(p)
            of=[(int(q),int(k)) for q,k in sympy.factorint(order).items()]
            small_primes.update(q for q,k in of)
            exact_order(10,p**e,of)
            checks.append(dict(modulus=p**e,order=order,order_factors=of))
        rows.append(dict(modulus=m,factors=fs,period=expected,component_checks=checks))
    # The four examples specifically cited by answer 19.
    p=2**31-1;small_primes.add(p)
    pf=[(int(q),int(k)) for q,k in sympy.factorint(p-1).items()]
    for a in (314159269,62089911,16807,48271):exact_order(a,p,pf)
    small_primes.update(q for q,k in pf)
    certs=prime_certificates(small_primes)
    result=dict(status='passed',decimal_examples=rows,prime_certificates=certs,
                table_3_3_4_lines_17_to_20=dict(modulus=p,multipliers=[314159269,62089911,16807,48271],period=p-1,period_factors=pf))
    (ROOT/'results/lagged-periods-small.json').write_text(json.dumps(result,indent=2)+'\n')

    b=2**32-5;m=b**43-b**22+1
    # b, b-1, Phi_3(b), Phi_7(b), Phi_21(b).
    fs=[(b,22),(2,1),(5,1),(19,1),(22605091,1),
        (883,1),(46681,1),(447526613551,1),
        (43,1),(1152964457,1),(7192358279,1),(17603680453543143795603788392916017993,1),
        (421,1),(7057,1),(9829,1),(3650221,1),
        (369647370490794909627747628939678026804346693178224186677750022102445220940696162576134304437648517,1)]
    assert len(fs)==17 and len(str(max(p for p,e in fs)))==99
    assert prod(p**e for p,e in fs)==m-1
    assert b**22*(b-1)*sum(b**i for i in range(7))*(b**14+b**7+1)==m-1
    assert b**44>m
    assert pow(b,m-1,m)==1
    witnesses=[]
    for q,e in fs:
        residue=pow(b,(m-1)//q,m)
        assert gcd(residue-1,m)==1
        witnesses.append(dict(prime=q,residue=residue))
    out=ROOT/'results/marsaglia-zaman-factors.json'
    if out.exists():
        previous=json.loads(out.read_text())['factor_certificates']
        assert [r['prime'] for r in previous]==[p for p,e in fs]
    else:
        gp=str(Path(sys.argv[1]).resolve())
        previous=[]
        for q,e in fs:
            code=f'print(primecert({q}));quit;\n'
            run=subprocess.run([gp,'-fq','-s','134217728'],input=code,text=True,
                               capture_output=True,check=True,timeout=300)
            cert=json.loads(run.stdout.strip());assert cert
            previous.append(dict(prime=q,certificate=cert))
    data=dict(status='exact product and modular witnesses passed; factor certificates need verify_ecpp.py',
              base=b,modulus=m,period=m-1,factors_of_period=fs,
              distinct_prime_factors=len(fs),largest_factor_decimal_digits=99,
              order_witnesses=witnesses,factor_certificates=previous,
              pocklington_note='b^22 divides m-1 and b^44>m; the witness for q=b already proves m prime once b is certified.')
    out.write_text(json.dumps(data,indent=2)+'\n')
    print('Four decimal periods and four referenced multipliers passed; MZ product and all 17 order witnesses passed.')


if __name__=='__main__':main()
