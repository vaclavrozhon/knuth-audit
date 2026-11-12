"""New exact checks for TAOCP 4.6.2 D, 28--31 and 37.

Checkpointed blocks do not rerun previous audit blocks. Independent comparisons
use trial division, root membership, polynomial CRT residues, permutation cycle
enumeration, and exact combinatorial counts. Timings are correctness checks.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product, combinations, permutations
from math import comb, factorial
from pathlib import Path
import argparse
import datetime
import json
import os
import time

import sympy as sp
from verify_berlekamp import Field

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / 'results/equal-degree.json'
STATS = Counter()


def monics(p, n):
    return [tuple(a)+(1,) for a in product(range(p), repeat=n)]


def catalog(p, n):
    f = Field(p)
    out = {}
    for d in range(1, n+1):
        out[d] = [u for u in monics(p, d)
                  if all(f.rem(u, v) for e in range(1, d//2+1) for v in out[e])]
    return out


def factors(u, f, cats):
    out = []
    for d in sorted(cats):
        for q in cats[d]:
            while len(u) >= len(q) and not f.rem(u, q):
                out.append(q)
                u = f.div(u, q)[0]
    assert u == (1,)
    return out


def prod(f, polys):
    u = (1,)
    for q in polys:
        u = f.mul(u, q)
    return u


def ddf(u, f):
    v, w, d, answer = u, (0, 1), 0, {}
    while d+1 <= (len(v)-1)//2:
        assert f.rem(w, v) == f.power((0, 1), f.p**d, v)
        d += 1
        w = f.power(w, f.p, v)
        g = f.gcd(f.sub(w, (0, 1)), v)
        if g != (1,):
            answer[d] = g
            v = f.div(v, g)[0]
            w = f.rem(w, v)
        STATS['ddf_stages'] += 1
    if v != (1,):
        assert len(v)-1 not in answer
        answer[len(v)-1] = v
    return answer


def distinct():
    for p, maxn in [(2, 8), (3, 6), (5, 4)]:
        f, cats = Field(p), catalog(p, maxn)
        for n in range(1, maxn+1):
            for u in monics(p, n):
                qs = factors(u, f, cats)
                if len(set(qs)) != len(qs):
                    continue
                expected = {d:prod(f, [q for q in qs if len(q)-1 == d])
                            for d in {len(q)-1 for q in qs}}
                assert ddf(u, f) == expected
                STATS['squarefree_ddf_inputs'] += 1
    # Printed table p448, 1 means the whole irreducible; 0 means unit gcd.
    rows = [((1,2,0,1),[0,0,0]), ((2,2,0,1),[1,1,1]),
            ((2,0,1,1),[1,1,0]), ((2,1,1,1),[1,0,1]),
            ((1,2,1,1),[0,1,1]), ((1,0,2,1),[0,1,0]),
            ((1,1,2,1),[0,0,1]), ((2,2,2,1),[1,0,0])]
    f, cats = Field(3), catalog(3, 3)
    assert set(q for q, _ in rows) == set(cats[3])
    for q, signs in rows:
        for s, bit in enumerate(signs):
            g = f.gcd(q, f.sub(f.power((s, 1), 13, q), (1,)))
            assert g == (q if bit else (1,))
            STATS['printed_cubic_entries'] += 1
    return {'printed_cubic_rows':rows}


def split():
    for p, d in [(3,1),(3,2),(3,3),(5,1),(5,2)]:
        f, qs = Field(p), catalog(p, d)[d]
        groups = list(combinations(qs[:5], 2))
        if len(qs) > 2:
            groups += [tuple(qs[:3]), tuple(qs)]
        for group in dict.fromkeys(groups):
            g = prod(f, group)
            success = 0
            count = p**(2*d)
            for coeff in product(range(p), repeat=2*d):
                t = f.poly(coeff)
                h = f.power(t, (p**d-1)//2, g)
                a = f.gcd(g, t)
                b = f.gcd(g, f.add(h, (1,)))
                c = f.gcd(g, f.sub(h, (1,)))
                assert f.mul(f.mul(a,b),c) == g
                c_factors = [q for q in group
                             if f.power(f.rem(t,q), (p**d-1)//2, q) == (1,)]
                assert c == prod(f, c_factors)
                success += c not in [(1,),g]
                STATS['split_polynomials'] += 1
            assert F(success,count) >= F(1,2)-F(1,2*p**(2*d))
            if len(group)==2:
                assert F(success,count) == F(1,2)-F(1,2*p**(2*d))
            STATS['split_distributions'] += 1
    # The first line on p687 has q1 instead of q2 in the second residue.
    f=Field(3);q1=(1,0,1);q2=(2,1,1);t=(2,1,2,1);g=f.mul(q1,q2)
    t1,t2=f.rem(t,q1),f.rem(t,q2)
    assert t1==() and t2==(0,1)
    assert f.power(t2,4,q1)==(1,) and f.power(t2,4,q2)==(2,)
    assert f.gcd(g,f.sub(f.power(t,4,g),(1,)))==(1,)
    # Exact one-bit probabilities and repeated independent trials.
    biases=[]
    for p in [3,5,7,11]:
        theta=F(p-1,2*p)
        for r in range(2,6):
            counts=Counter(sum(int(a and pow(a,(p-1)//2,p)==1) for a in vec)
                           for vec in product(range(p),repeat=r))
            for k, count in counts.items():
                assert F(count,p**r)==comb(r,k)*theta**k*(1-theta)**(r-k)
            assert 1-F(counts[0]+counts[r],p**r)>=F(4,9)
            STATS['berlekamp_split_distributions']+=1
        biases.append({'p':p,'one_bit_probability':str(theta),
                       'two_factor_split_probability':str(2*theta*(1-theta)),
                       'two_factor_mean_trials':str(1/(2*theta*(1-theta)))})
    return {'biased_coin_examples':biases,'wrong_modulus_counterexample':
            {'p':3,'q1':q1,'q2':q2,'t':t,'true_gcd':[1]}}


def trace_value(t,d,f,g):
    v=f.rem(t,g)
    for _ in range(d-1):
        v=f.rem(f.add(t,f.power(v,f.p,g)),g)
    return v


def trace():
    for p, maxd in [(2,6),(3,3),(5,2)]:
        f=Field(p);cats=catalog(p,maxd)
        for d in range(1,maxd+1):
            for q in cats[d]:
                counts=Counter()
                for a in product(range(p),repeat=d):
                    t=f.poly(a);v=trace_value(t,d,f,q)
                    assert len(v)<=1
                    direct=()
                    for i in range(d):direct=f.add(direct,f.power(t,p**i,q))
                    assert v==direct
                    counts[v]+=1
                    STATS['field_trace_values']+=1
                assert set(counts.values())=={p**(d-1)} and len(counts)==p
    f=Field(2);cats=catalog(2,6)
    for d, qs in cats.items():
        for q1,q2 in combinations(qs,2):
            g=f.mul(q1,q2)
            choices=[]
            for j in range(1,2*d,2):
                t=(0,)*j+(1,)
                h=f.gcd(g,trace_value(t,d,f,g))
                if h not in [(1,),g]:choices.append(j)
            assert choices
            STATS['cohen_distinguished_pairs']+=1
        if len(qs)>=2 and d<=4:
            g=f.mul(qs[0],qs[1]);good=0
            for coeff in product(range(2),repeat=2*d):
                h=f.gcd(g,trace_value(f.poly(coeff),d,f,g))
                good+=h not in [(1,),g]
                STATS['binary_split_polynomials']+=1
            assert good==2**(2*d-1)
    return {}


def irred_count(p,d):
    return sum(int(sp.mobius(c))*p**(d//c) for c in sp.divisors(d))//d


def lucky_coeffs(p,n):
    c=[F(1)]+[F(0)]*n
    for d in range(1,n+1):
        b=F(irred_count(p,d),p**d) if p else F(1,d)
        for j in range(n,d-1,-1):c[j]+=b*c[j-d]
    return c


def partition_vectors(n):
    def rec(left,d,ds):
        if left==0:yield tuple(ds);return
        for j in range(d,left+1):yield from rec(left-j,j,ds+[j])
    return rec(n,1,[])


def counts():
    printed_limit=['1','1/2','5/6','7/12','37/60','79/120','173/280','101/168','127/210','1033/1680']
    printed_binary=['1','1/4','1/2','7/16','7/16','7/16','27/64','111/256','109/256','109/256']
    assert list(map(str,lucky_coeffs(None,10)[1:]))==printed_limit
    assert list(map(str,lucky_coeffs(2,10)[1:]))==printed_binary
    for p,maxn in [(2,8),(3,6),(5,4)]:
        f=Field(p);cats=catalog(p,maxn)
        for n in range(1,maxn+1):
            dist=Counter()
            for u in monics(p,n):
                ds=tuple(sorted(len(q)-1 for q in factors(u,f,cats)))
                dist[ds]+=1
                STATS['degree_pattern_polynomials']+=1
            for ds in partition_vectors(n):
                ks=Counter(ds);c=1
                for j,k in ks.items():c*=comb(irred_count(p,j)+k-1,k)
                assert dist[ds]==c
                STATS['degree_patterns']+=1
            lucky=sum(count for ds,count in dist.items() if len(ds)==len(set(ds)))
            assert F(lucky,p**n)==lucky_coeffs(p,n)[n]
            STATS['lucky_distributions']+=1
    for n in range(1,9):
        dist=Counter()
        for perm in permutations(range(n)):
            unseen=set(range(n));ds=[]
            while unseen:
                i=next(iter(unseen));length=0
                while i in unseen:
                    unseen.remove(i);length+=1;i=perm[i]
                ds.append(length)
            dist[tuple(sorted(ds))]+=1
            STATS['permutations']+=1
        for ds,count in dist.items():
            denom=1
            for j,k in Counter(ds).items():denom*=j**k*factorial(k)
            assert F(count,factorial(n))==F(1,denom)
    n31=[]
    for p,maxd in [(3,5),(5,3),(7,2)]:
        f=Field(p);cats=catalog(p,maxd)
        for d in range(1,maxd+1):
            qs=cats[d]
            signatures=[[f.power((t,1),(p**d-1)//2,q) for t in range(p)] for q in qs]
            first=[sum(s[t]==(1,) for s in signatures) for t in range(p)]
            second=[sum(s[t1]==s[t2] for s in signatures) for t1,t2 in combinations(range(p),2)]
            formula=F(sum((3+(-1)**c)*int(sp.mobius(c))*(p**(d//c)-1)
                          for c in sp.divisors(d)),4*d)
            assert set(first)=={formula}
            if d>1:assert set(second)=={formula}
            else:assert set(second)=={formula-1}
            if d>1 and d%2:assert 2*formula==len(qs)
            n31.append({'p':p,'d':d,'count_i':first[0],'count_ii':second[0]})
            STATS['exercise31_fields']+=1
    return {'printed_lucky_limit':printed_limit,'printed_lucky_binary':printed_binary,
            'exercise31_counts':n31,'exercise37_counterexample':
            {'p':2,'degrees':[1,1],'true_probability':'3/4','printed_probability':'1/2'}}


def constants():
    import mpmath as mp
    mp.mp.dps=80
    p,N=2,4096
    log_partial=mp.mpf(0)
    for d in range(1,N+1):
        b=mp.mpf(irred_count(p,d))/mp.mpf(p)**d
        log_partial+=mp.log1p(b)-mp.mpf(1)/d
    # Analytic tail enclosure; numerical rounding allowance is far larger
    # than accumulated 80-digit rounding for these 4096 bounded operations.
    tail=mp.mpf(1)/(2*N)+2*mp.power(p,-mp.mpf(N+1)/2)/((N+1)*(1-mp.sqrt(mp.mpf(1)/p)))
    lo=mp.exp(log_partial-tail)-mp.mpf('1e-60')
    hi=mp.exp(log_partial)+mp.mpf('1e-60')
    assert mp.mpf('.3965') < lo < hi < mp.mpf('.3975')
    STATS['constant_product_terms']=N
    return {'c2_lower':mp.nstr(lo,40),'c2_upper':mp.nstr(hi,40),
            'tail_log_bound':mp.nstr(tail,40),'e_minus_gamma':mp.nstr(mp.exp(-mp.euler),40),
            'scope':'Analytic tail bound with 80-digit numerical evaluation; not interval-library certified rounding.'}


def main():
    p=argparse.ArgumentParser();p.add_argument('block',choices=['distinct','split','trace','counts','constants']);a=p.parse_args()
    data=json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert a.block not in data['blocks'], 'Do not repeat successful checkpoints'
    started=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic()
    extra=globals()[a.block]()
    data['blocks'][a.block]=dict(status='passed',started_at_utc=started,pid=os.getpid(),elapsed_seconds=time.monotonic()-t,stats=dict(STATS),**extra)
    RESULT.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data['blocks'][a.block]))


if __name__=='__main__':main()
