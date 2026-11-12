#!/usr/bin/env python3
"""Exact construction and independent checks for TAOCP 4.1-32."""
from pathlib import Path
import json
from bisect import bisect_left

ROOT = Path(__file__).resolve().parent
TARGET = ROOT / 'results/ruzsa-digits.json'


def digits(n, base):
    out = []
    while n:
        n, r = divmod(n, base)
        out.append(r)
    return out or [0]


def good(n, base, bound):
    return max(digits(n, base)) <= bound


def ternary_from_binary(n):
    return sum(d * 3**k for k,d in enumerate(digits(n,2)))


def ternary_ceiling(x):
    ds = digits(x, 3) + [0]
    bad = [j for j,d in enumerate(ds) if d == 2]
    if not bad:
        return x
    j = max(bad)
    k = j+1
    while ds[k] != 0:
        k += 1
    ds[k] = 1
    for j in range(k):
        ds[j] = 0
    return sum(d*3**j for j,d in enumerate(ds))


def repair_state(n):
    ds = digits(n, 5)
    bad = [j for j,d in enumerate(ds) if d > 2]
    if not bad:
        return None
    j = max(bad)
    i = j+1
    while i < len(ds) and ds[i] == 2:
        i += 1
    assert i < len(ds) and ds[i] < 2
    return i, ds[i], n % 5**i


def step(n):
    assert good(n,3,1)
    state = repair_state(n)
    if state is None:
        return n, 'done'
    i, b, tail = state
    power, rest = 1,n
    while rest % 3 == 0:
        rest //= 3
        power *= 3
    gap = (power+1)//2
    if tail >= gap:
        out = n-gap
        case = 'subtract'
    else:
        x = 5**i-tail
        u = ternary_ceiling(x)
        assert x <= u < 2*x
        assert u < power
        assert 0 <= u-x < (5**i-1)//2
        out = n+u
        case = 'add'
    assert good(out,3,1)
    assert out >= n-tail
    next_state = repair_state(out)
    if next_state is not None:
        i2,b2,_ = next_state
        assert (i2, 2-b2, out) < (i, 2-b, n)
    return out,case


def valuation_factorial(n,p):
    answer=0
    while n:
        n//=p
        answer+=n
    return answer


def main():
    out=json.loads(TARGET.read_text()) if TARGET.exists() else {}
    if out.get('status') == 'passed':
        raise SystemExit('Refusing to repeat successful checks.')
    def save(): TARGET.write_text(json.dumps(out,indent=2)+'\n')
    if 'gap_checks' not in out:
        vals=[ternary_from_binary(n) for n in range(1 << 15)]
        for x in range(1,100001):
            u=ternary_ceiling(x)
            assert u==vals[bisect_left(vals,x)]
            assert x<=u<2*x
        out['gap_checks']=100000
        save();print('PASS ternary ceiling and multiplicative gaps',flush=True)
    if 'local_steps' not in out:
        cases={'add':0,'subtract':0,'done':0}
        for mask in range(1,1 << 14):
            n=ternary_from_binary(mask)
            if digits(n,5)[-1] != 1:
                continue
            _,case=step(n)
            cases[case]+=1
        out['local_steps']=cases
        save();print('PASS all local steps',cases,flush=True)
    examples=out.setdefault('constructed',[])
    done={e['exponent'] for e in examples}
    for exponent in range(1,41):
        start=3**exponent
        ds=digits(start,5)
        if ds[-1] != 1 or exponent in done:
            continue
        n=start;count=0;cases={'add':0,'subtract':0};floor=5**(len(ds)-1)
        while not good(n,5,2):
            n,case=step(n);count+=1;cases[case]+=1
            assert n>=floor
            assert count<1000000,('computational cap',exponent)
        assert good(n,3,1)
        examples.append({'exponent':exponent,'start':start,'result':n,'lower_bound':floor,
                         'steps':count,'cases':cases,'ternary':''.join(map(str,digits(n,3)[::-1])),
                         'quinary':''.join(map(str,digits(n,5)[::-1]))})
        save();print('PASS construction',exponent,count,n,flush=True)
    if 'oeis' not in out:
        rows=[]
        for line in (ROOT/'sources/oeis-A129508-bfile-excerpt.txt').read_text().splitlines():
            if line.strip() and not line.startswith('#'):
                rows.append(tuple(map(int,line.split())))
        assert all(j==i+1 for i,(j,n) in enumerate(rows))
        vals=[n for _,n in rows]
        assert vals==sorted(set(vals))
        for n in vals:
            assert good(n,3,1) and good(n,5,2)
            for p in [3,5]:
                assert valuation_factorial(2*n,p)-2*valuation_factorial(n,p)==0
        bound=20011
        # Full generation in the two bases, independent of the repair algorithm.
        a={ternary_from_binary(i) for i in range(1 << 13)}
        a={n for n in a if n<=bound}
        assert 3**13>bound
        b={0}
        power=1
        while power<=bound:
            b={n+d*power for n in b for d in range(3) if n+d*power<=bound}
            power*=5
        intersection=sorted(a & b)
        assert intersection==[n for n in vals if n<=bound]
        out['oeis']={'listed_checked':len(vals),'full_intersection_bound':bound,
                     'full_intersection_count':len(intersection)}
        save();print('PASS OEIS and independent full intersection',out['oeis'],flush=True)
    out['status']='passed';save()


if __name__=='__main__':main()
