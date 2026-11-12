"""Independent integer/rational IEEE rounding checks and finite trajectory replay.

Every stored edge probe is checked with exact Fraction arithmetic. Binary32
trajectories use a dictionary, independently of the C++ Brent detector.
Large binary64 cycles are replayed with Python binary64 arithmetic, checking
entry minimality, period minimality, and the saved hash. This is not a
complete floating-point state census.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import struct
import time
import sympy

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/logistic-float-validation.json'

def two(e):
    return Q(1<<e) if e>=0 else Q(1,1<<-e)

def decode(bits,width):
    p,bias=(23,127) if width==32 else (52,1023)
    exponent=(bits>>p)&((1<<(width-p-1))-1)
    fraction=bits&((1<<p)-1)
    assert bits>>(width-1)==0
    if exponent:
        return Q((1<<p)+fraction)*two(exponent-bias-p)
    return Q(fraction)*two(1-bias-p)

def rnd(x,width):
    assert x>=0
    if not x:return Q(0)
    p,bias=(23,127) if width==32 else (52,1023)
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<two(e):e-=1
    shift=max(e,1-bias)-p
    a=x/two(shift)
    q,r=divmod(a.numerator,a.denominator)
    q+=2*r>a.denominator or (2*r==a.denominator and q%2==1)
    return q*two(shift)

def exact_step(x,width,expression):
    if expression==0:return rnd(rnd(4*x,width)*rnd(1-x,width),width)
    return rnd(4*rnd(x-rnd(x*x,width),width),width)

def encode(x,width):
    return int.from_bytes(struct.pack('>f' if width==32 else '>d',float(x)),'big')

def hardware_step(x,expression):
    return (4*x)*(1-x) if expression==0 else 4*(x-x*x)

def replay(row):
    width=int(row['format'][6:]);expr=row['expression'];seed=row['seed_bits']
    probes=0
    for x,y in row['edge_probes']:
        assert exact_step(decode(x,width),width,expr)==decode(y,width)
        probes+=1
    rec=dict(format=row['format'],expression=expr,seed_bits=seed,exact_edge_probes=probes)
    if width==32:
        visited={};bits=seed;sequence=[]
        while bits not in visited:
            visited[bits]=len(sequence);sequence.append(bits)
            bits=encode(exact_step(decode(bits,width),width,expr),width)
            assert len(sequence)<100000
        mu=visited[bits];period=len(sequence)-mu
        assert row['cycle_found'] and mu==row['transient'] and period==row['period']
        assert sequence[mu]==row['entry_bits']
        h=14695981039346656037
        for b in sequence[mu:]:h=((h^b)*1099511628211)&((1<<64)-1)
        assert h==row['cycle_hash_fnv64']
        rec.update(exact_trajectory_states=len(sequence),period=period,transient=mu)
    elif row['cycle_found']:
        mu=row['transient'];period=row['period'];x=float(decode(seed,width));previous=None
        for _ in range(mu):previous=x;x=hardware_step(x,expr)
        entry=x;assert encode(entry,width)==row['entry_bits']
        check_at={period//int(p) for p in sympy.factorint(period)}
        h=14695981039346656037
        for j in range(period):
            if j in check_at:assert x!=entry
            h=((h^encode(x,width))*1099511628211)&((1<<64)-1)
            predecessor=x;x=hardware_step(x,expr)
        assert x==entry and h==row['cycle_hash_fnv64']
        if mu:assert previous!=predecessor
        rec.update(binary64_replayed_states=mu+period,period=period,transient=mu)
    else:
        rec['scope']='Detection cap reached; no period or global nonperiodicity claim.'
    return rec

rows=[json.loads(line) for line in (ROOT/'results/logistic-float.jsonl').read_text().splitlines()]
assert len(rows)==40
result=json.loads(OUT.read_text()) if OUT.exists() else []
for row in rows[len(result):]:
    before=time.monotonic();r=replay(row);r['elapsed_seconds']=time.monotonic()-before
    result.append(r);OUT.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',r['format'],r['expression'],r['seed_bits'],r.get('period'),flush=True)
