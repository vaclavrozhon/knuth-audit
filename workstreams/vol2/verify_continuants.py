"""Independent Euclidean validation and moment checks for exercise3.3.4-31.

Run continuant_census.cpp first for (3,2000000) and (2,1048576).
--input-dir names its raw witness arrays; after validation compressed arrays
are retained in results/. --resume preserves each completed block.
"""
import argparse
import array
from fractions import Fraction as Q
import gzip
import hashlib
from itertools import product
import json
from math import gcd,isqrt
from pathlib import Path
import sys
import time
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/continuants.json'


def cf(m, a):
    digits = []
    while a:
        d, r = divmod(m, a)
        digits.append(d)
        m, a = a, r
    return digits


def allowed(digits, bound, canonical):
    if max(digits) <= bound:
        return True
    return (not canonical and
            max(digits[:-1] + [digits[-1]-1, 1]) <= bound)


def census(bound, limit, input_dir):
    log = (ROOT / f'results/continuants-{bound}.log').read_text()
    marker = f'COMPLETE alphabet {bound} limit {limit} '
    assert marker in log
    details = {}
    arrays = {}
    for convention in ['any', 'canonical']:
        name = f'continuants-{bound}.{convention}.u32'
        raw_path = input_dir / name if input_dir else None
        saved = ROOT / 'results' / (name + '.gz')
        raw = raw_path.read_bytes() if raw_path and raw_path.exists() else gzip.decompress(saved.read_bytes())
        assert len(raw) == 4*(limit+1)
        values = array.array('I'); values.frombytes(raw)
        if sys.byteorder != 'little': values.byteswap()
        assert values.itemsize == 4
        checked = 0
        for m in range(2, limit+1):
            a = values[m]
            if not a: continue
            assert 0 < a < m and gcd(a, m) == 1, (bound, convention, m, a)
            assert allowed(cf(m, a), bound, convention == 'canonical'), (bound, convention, m, a)
            checked += 1
        # Independently enumerate all reduced fractions for small moduli.
        for m in range(2, 501):
            possible = any(allowed(cf(m, a), bound, convention == 'canonical')
                           for a in range(1, m) if gcd(a, m) == 1)
            assert possible == bool(values[m]), (bound, convention, m)
        info = dict(witnesses_checked=checked, raw_sha256=hashlib.sha256(raw).hexdigest(),
                    compressed_array='results/' + saved.name, direct_moduli=499)
        if bound == 3:
            missing = [m for m in range(2, limit+1) if not values[m]]
            minima = []
            for m in missing:
                best = None
                for a in range(1, m):
                    if gcd(a, m) != 1: continue
                    digits = cf(m, a)
                    score = max(digits)
                    if convention == 'any':
                        alt = digits[:-1]+[digits[-1]-1, 1]
                        if max(alt) < score: score, digits = max(alt), alt
                    if best is None or score < best[0]: best = (score, a, digits)
                assert best[0] > bound
                minima.append(dict(m=m, bound=best[0], numerator=best[1], digits=best[2]))
            info.update(missing=missing, exact_minima_for_missing=minima)
            fours = [x['m'] for x in minima if x['bound'] == 4]
            assert fours[-4:] == ([2052, 2370, 5052, 6234] if convention == 'any'
                                 else [2370, 3618, 5052, 6234])
            assert [x['m'] for x in minima if x['bound'] == 5] == ([54, 150] if convention == 'any' else [6, 54, 150])
        else:
            # Blocks (j*2^14,(j+1)*2^14]; m=1 via the word (1).
            counts = [sum(bool(values[m]) for m in range(max(2, j*16384+1), (j+1)*16384+1))
                      + (j == 0) for j in range(64)]
            info.update(block_counts=counts, block_size=16384,
                        min_density=str(Q(min(counts),16384)),
                        max_density=str(Q(max(counts),16384)))
        saved.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
        details[convention] = info
        arrays[convention] = values
    assert all(not arrays['canonical'][m] or arrays['any'][m] for m in range(2,limit+1))
    return dict(alphabet=bound, limit=limit, conventions=details,
                method='Complete forward-word census; all positive witnesses independently validated by Euclidean division, small negative cases by all reduced fractions.')


def moments():
    x = sp.Symbol('x'); result = []
    bounds = {3: (Q(251527723,10**8), Q(251527724,10**8)),
              2: (Q(204032869,10**8), Q(204032870,10**8))}
    for alphabet in (2,3):
        mu=Q(alphabet+1,2); second=Q((alphabet+1)*(2*alphabet+1),6)
        M=sp.Matrix([[second,2*mu,1],[mu,1,0],[1,0,0]])
        polynomial=sp.Poly(M.charpoly(x).as_expr(),x)
        state=sp.Matrix([1,0,0]); mean_prev=Q(0); mean=Q(1)
        counts=0
        for n in range(1,9):
            mean_prev,mean=mean,mu*mean+mean_prev
            state=M*state
            vals=[]
            for word in product(range(1,alphabet+1),repeat=n):
                k0,k1=0,1
                for d in word:k0,k1=k1,d*k1+k0
                vals.append(k1)
            assert Q(sum(vals),len(vals))==mean
            assert Q(sum(v*v for v in vals),len(vals))==state[0]
            if alphabet==2:assert mean==Q(4,5)*2**n+Q(1,5)*Q(-2)**(-n)
            counts+=len(vals)
        low,high=bounds[alphabet]
        assert polynomial.eval(low*low)<0<polynomial.eval(high*high)
        assert polynomial.count_roots(low*low,sp.oo)==1
        assert min(M**2)>0
        # Mean's largest characteristic root is below the SD base.
        # y^2-mu*y-1 > 0 for y=low beyond its positive root.
        assert low*low-mu*low-1>0
        result.append(dict(alphabet=alphabet,mean_digit=str(mu),second_moment_digit=str(second),
                      second_moment_matrix=str(M),characteristic_polynomial=str(polynomial.as_expr()),
                      sd_exponential_base_interval=[str(low),str(high)],
                      finite_words_checked=counts,checked_lengths=list(range(1,9))))
    return dict(cases=result,scope='Exact first and second moments, rational root isolation. The five-decimal nearest rounding of the alphabet3 base is2.51528; the book prints2.51527.')


def powers(exponent):
    from verify_spectral_details import bounded_quotients
    r=bounded_quotients(2**exponent,residue=0,modulus=1)
    r['canonical_solutions_exist']=bool(r['solutions'])
    if not r['solutions']:
        r['noncanonical']=bounded_any(r['m'])
        assert r['noncanonical']['solutions']
        a=r['noncanonical']['solutions'][0]
        digits=cf(r['m'],a)
        r['witness_digits']=digits[:-1]+[digits[-1]-1,1]
        r['witness_numerator']=a
    else:
        r['witness_digits']=cf(r['m'],r['solutions'][0])
        r['witness_numerator']=r['solutions'][0]
    for a in r['solutions']:
        assert a%2==1 and max(cf(r['m'],a))<=2
    r['exponent']=exponent
    assert max(r['witness_digits'])<=2
    return r


def bounded_any(m):
    """Prefix/suffix Diophantine census, including terminal1 words.

    Every word crosses sqrt(m) at a unique prefix denominator P.
    Write m=P*R+Q*S, where Q is the preceding denominator and R,S
    are the denominator/numerator of the tail. Empty and single1
    tails are handled explicitly; all remaining tails have R>S>=1.
    """
    threshold=isqrt(m); solutions=set();prefixes=trials=0
    stack=[(1,0,0,1)]
    while stack:
        P,Q0,A,B=stack.pop()
        if P<=threshold:
            for d in (1,2):stack.append((d*P+Q0,P,d*A+B,A))
            continue
        prefixes+=1
        if P==m and 0<A<m:solutions.add(A)
        if P+Q0==m and 0<A+B<m:solutions.add(A+B)
        low=(m+Q0+P+Q0-1)//(P+Q0);high=(m-Q0)//P
        r0=(m*pow(P,-1,Q0))%Q0 if Q0>1 else 0
        for k in range(-((-(low-r0))//Q0),(high-r0)//Q0+1):
            R=r0+k*Q0;S=(m-P*R)//Q0;trials+=1
            assert P*R+Q0*S==m and 1<=S<R
            if gcd(R,S)==1 and allowed(cf(R,S),2,False):solutions.add(A*R+B*S)
    for a in solutions:assert gcd(a,m)==1 and allowed(cf(m,a),2,False)
    return dict(solutions=sorted(solutions),prefixes=prefixes,suffix_trials=trials)


def alternative_split():
    for m in range(2,501):
        direct=[a for a in range(1,m) if gcd(a,m)==1 and allowed(cf(m,a),2,False)]
        assert bounded_any(m)['solutions']==direct,m
    return dict(exhaustive_small_moduli=499,scope='Independent all-numerator comparison validates terminal1 prefix/suffix handling.')


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true')
    ap.add_argument('--input-dir',type=Path)
    args=ap.parse_args()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}
    blocks=[('census3',lambda:census(3,2000000,args.input_dir)),
            ('census2',lambda:census(2,1048576,args.input_dir)),('moments',moments),
            ('alternative_split',alternative_split)]
    blocks += [(f'power{e}',lambda e=e:powers(e)) for e in range(25,36)]
    for key,fn in blocks:
        if key in data:continue
        start=time.monotonic();data[key]=fn();data[key]['seconds']=time.monotonic()-start
        OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
        print(key,'completed',data[key]['seconds'],flush=True)
