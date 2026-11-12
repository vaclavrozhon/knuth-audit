#!/usr/bin/env python3
"""Independent finite-grid and integer-count checks for TAOCP 4.5.1,12--14."""
from fractions import Fraction as F
from bisect import bisect_left
from math import gcd
from pathlib import Path
import itertools
import json
import random
import sys
import time

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'sources'))
from slash_arithmetic import (SlashFormat, as_pair, positive_rectangle,
                              integer_rectangle, format_count, pack_binary,
                              unpack_binary, pack_hex, unpack_hex)
OUT = ROOT / 'results/rational-slash.json'


def grid(fmt):
    # Independent full enumeration; never used for large formats.
    cap = 1 << fmt.size
    return sorted({F(u, a) for a in range(1, cap)
                   for u in range(-cap + 1, cap)
                   if fmt.fits((u, a)) and gcd(u, a) == 1})


def grid_round(x, values):
    j = bisect_left(values, x)
    if j < len(values) and values[j] == x:
        return as_pair(x), (as_pair(x), as_pair(x))
    lo = as_pair(values[j-1]) if j else (-1, 0)
    hi = as_pair(values[j]) if j < len(values) else (1, 0)
    threshold = F(lo[0]+hi[0], lo[1]+hi[1])
    if x < threshold:
        result = lo
    elif x > threshold:
        result = hi
    else:
        result = sorted([lo, hi], key=lambda t: (t[1], t[0]))[0]
    return result, (lo, hi)


def rounding():
    count = 0
    rows = []
    formats = [SlashFormat(size=q) for q in range(1, 11)]
    formats += [SlashFormat('fixed', p) for p in range(2, 7)]
    for fmt in formats:
        values = grid(fmt)
        pairs = [(-1, 0)] + [as_pair(x) for x in values] + [(1, 0)]
        probes = list(values)
        for lo, hi in zip(pairs, pairs[1:]):
            m = F(lo[0]+hi[0], lo[1]+hi[1])
            probes.extend([m,
                (F(*lo)+m)/2 if lo[1] else m-1,
                (F(*hi)+m)/2 if hi[1] else m+1])
        for x in probes:
            want, bracket = grid_round(x, values)
            assert fmt.bracket(x) == bracket, (fmt.kind, fmt.size, x)
            assert fmt.round(x) == want, (fmt.kind, fmt.size, x, want)
            count += 1
        rows.append([fmt.kind, fmt.size, len(values), len(probes)])
    fmt = SlashFormat('fixed', 8)
    values = grid(fmt)
    xs = [F(314,159), F(1300,1113), F(377,120), F(1,256), F(-1,256)]
    want = [(79,40),(7,6),(22,7),(0,1),(0,1)]
    for x, y in zip(xs, want):
        assert fmt.round(x) == y == grid_round(x, values)[0]
    assert F(314,159)+F(1300,1113) == F(22,7)
    rng = random.Random(45112)
    certificates = 0
    for q in [27,58]:
        fmt = SlashFormat(size=q)
        for _ in range(1000):
            x = F(rng.randrange(-2**100,2**100),rng.randrange(1,2**100))
            e = rng.randrange(-70,71)
            x *= F(2**max(0,e),2**max(0,-e))
            lo, hi = fmt.bracket(x)
            for y in (lo,hi):
                assert fmt.fits(y) and gcd(*y)==1
            if lo == hi:
                assert F(*lo)==x
            else:
                assert not lo[1] or F(*lo)<x
                assert not hi[1] or x<F(*hi)
                assert hi[0]*lo[1]-lo[0]*hi[1]==1
                assert not fmt.fits((lo[0]+hi[0],lo[1]+hi[1]))
            certificates += 1
    return {'grid_cases':count, 'grid_rows':rows, 'p8_example':want,
            'large_bracket_certificates':certificates}


def endpoints():
    rows = []
    for q in range(1,59):
        fmt = SlashFormat(size=q)
        bound = 1 << (q-1)
        assert fmt.fits((bound-1,1)) and not fmt.fits((bound,1))
        assert fmt.round(F(bound)) == (1,0)
        zpos = fmt.round(F(1,bound))
        zneg = fmt.round(F(-1,bound))
        if q >= 3:
            assert zpos == zneg == (0,1)
        rows.append([q,zneg,zpos])
    assert SlashFormat(size=1).round(F(1)) == (1,0)
    assert SlashFormat(size=1).round(F(-1)) == (-1,0)
    assert SlashFormat(size=2).round(F(-1,2)) == (-1,1)
    return {'q_range':[1,58], 'zero_boundary_rows':rows,
            'C0115':'q=1 endpoints round to infinities; q=2 negative tie to -1'}


def counts():
    positives = 0
    for a,b in itertools.combinations(range(10),2):
        for c,d in itertools.combinations(range(10),2):
            direct = sum(gcd(u,v)==1 for u in range(a+1,b+1) for v in range(c+1,d+1))
            assert positive_rectangle(a,b,c,d)==direct
            positives += 1
    signed = 0
    for a,b in itertools.combinations(range(-5,6),2):
        for c,d in itertools.combinations(range(-5,6),2):
            direct = sum(gcd(u,v)==1 for u in range(a+1,b+1) for v in range(c+1,d+1))
            assert integer_rectangle(a,b,c,d)==direct, (a,b,c,d,direct)
            signed += 1
    small = []
    for q in range(1,11):
        n = len(grid(SlashFormat(size=q)))
        assert format_count(2,q)==n
        small.append([2,q,n])
    for q in [1,2,3]:
        pairs={(u,a) for du in range(1,q) for u in range(16**(du-1),16**du)
               for a in range(1,16**(q-du)) if gcd(u,a)==1}
        n=2*len(pairs)+1
        assert format_count(16,q)==n
        small.append([16,q,n])
    binary=format_count(2,27);hexa=format_count(16,7)
    assert binary==2140040119 and hexa==1830986459
    # The literal printed cutoff min(M2,N2)=1 wrongly includes (0,2).
    assert integer_rectangle(-1,1,0,2)==3
    literal=(1-(-1))*(2-0)
    assert literal==4
    return {'positive_rectangles':positives,'signed_rectangles':signed,
            'small_formats':small,'binary32_count':binary,'hex32_count':hexa,
            'C0116':{'bounds':[-1,1,0,2],'literal':literal,'correct':3}}


def encodings():
    rows=[]
    for q in range(2,11):
        accepted=[]
        for w in range(1 << (q+q.bit_length())):
            try:x=unpack_binary(w,q)
            except ValueError:continue
            assert pack_binary(x,q)==w
            accepted.append(x)
        assert len(set(accepted))==len(accepted)==format_count(2,q)+2
        rows.append(['binary',q,len(accepted)])
    for q in [1,2,3]:
        accepted=[]
        for w in range(1 << (4*q+q.bit_length()+1)):
            try:x=unpack_hex(w,q)
            except ValueError:continue
            assert pack_hex(x,q)==w
            accepted.append(x)
        assert len(set(accepted))==len(accepted)==format_count(16,q)+2
        rows.append(['hex',q,len(accepted)])
    rng=random.Random(45113);large=0
    for q in [27,58]:
        for _ in range(2000):
            d=rng.randrange(1,q+1)
            a=rng.randrange(1 << (d-1),1 << d)
            u=rng.randrange(-(1 << (q-d))+1,1 << (q-d))
            x=as_pair(F(u,a));w=pack_binary(x,q)
            assert unpack_binary(w,q)==x and w.bit_length() <= (32 if q==27 else 64)
            large+=1
        for x in [(1,0),(-1,0),(0,1)]:assert unpack_binary(pack_binary(x,q),q)==x
    for _ in range(2000):
        d=rng.randrange(1,8)
        a=rng.randrange(16**(d-1),16**d)
        u=rng.randrange(-16**(7-d)+1,16**(7-d))
        x=as_pair(F(u,a));w=pack_hex(x)
        assert unpack_hex(w)==x and w.bit_length()<=32
        large+=1
    return {'exhaustive_code_rows':rows,'large_roundtrips':large}


if __name__ == '__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('rounding',rounding),('endpoints',endpoints),('counts',counts),('encodings',encodings)]:
        if name in data:continue
        start=time.monotonic();value=fn()
        data[name]={'status':'passed','seconds':time.monotonic()-start,'result':value}
        OUT.write_text(json.dumps(data,indent=2)+'\n')
        print(name,json.dumps(data[name]),flush=True)
