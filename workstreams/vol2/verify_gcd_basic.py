#!/usr/bin/env python3
"""Exact checks supplementing the proofs for TAOCP 4.5.2, pp.333-343.

The transcribed MIX instructions and the arithmetic algorithms are independent
paths, compared with Python's gcd. Checkpoints prevent repeating passed work.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd, lcm
from pathlib import Path
import json, random, sys, time
from mix_float_machine import Machine, Word, word

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/gcd-basic.json'
SOURCE=ROOT/'sources/gcd-basic.mix'


def euclid(u,v):
    assert u>=0 and v>=0
    rows=[]
    while v:
        rows.append((u,v,u//v,u%v))
        u,v=v,u%v
    return u,rows


def binary(u,v):
    assert u>0 and v>0
    k=0
    while u%2==v%2==0:
        u//=2;v//=2;k+=1
    B=int(u%2==0);t=u if B else -v
    C=D=E=Fcount=0;rows=[]
    while True:
        halves=[]
        while t%2==0:
            assert t
            t//=2;D+=1;halves.append(t)
        E+=t>0
        if t>0:u=t
        else:v=-t
        assert u%2 and v%2
        C+=1;Fcount+=u>v
        rows.append((u,v,u-v,halves))
        t=u-v
        if not t:break
    assert E==Fcount+B
    stats=dict(A=k,B=B,C=C,D=D,E=E,F=Fcount)
    return u*2**k,stats,rows


def binary_time(s):return 9*s['A']+2*s['B']+6*s['C']+3*s['D']+s['E']+13


def ternary(u,v):
    assert u>0 and v>0
    k=0
    while u%3==v%3==0:
        u//=3;v//=3;k+=1
    while u%3==0:u//=3
    while v%3==0:v//=3
    rows=[]
    while u!=v:
        oldmax=max(u,v)
        t=abs(u-v) if (u-v)%3==0 else u+v
        values=[t];assert t%3==0
        while t%3==0:
            t//=3;values.append(t)
        assert 0<t<oldmax
        rows.append((u,v,values))
        if u>v:u=t
        else:v=t
    rows.append((u,v,[0]))
    return u*3**k,rows


def extended(u,v):
    assert u>=0 and v>=0
    a=(1,0,u);b=(0,1,v);rows=[]
    while b[2]:
        assert u*a[0]+v*a[1]==a[2]
        assert u*b[0]+v*b[1]==b[2]
        assert abs(a[0]*b[1]-a[1]*b[0])==1
        q=a[2]//b[2];rows.append((a,b,q))
        a,b=b,tuple(x-q*y for x,y in zip(a,b))
    assert a[2]==gcd(u,v) and u*a[0]+v*a[1]==a[2]
    assert u*b[0]+v*b[1]==0 and gcd(b[0],b[1])==1
    return a,b,rows


def arithmetic():
    rng=random.Random(45201);count=0
    cases=list(product(range(128),repeat=2))
    for bits in [32,64,256,1024,2048]:
        cases.extend((rng.getrandbits(bits),rng.getrandbits(bits)) for _ in range(100))
    for u,v in cases:
        g=gcd(u,v);a,rows=euclid(u,v);assert a==g
        extended(u,v)
        if u and v:
            b,s,br=binary(u,v);assert b==g
            assert s['C']<=max(u,v).bit_length()
            c,tr=ternary(u,v);assert c==g
            b2,s2,_=binary(v,u);assert s2['C']==s['C']
            assert s2['F']==s['C']-1-s['F']
        count+=1
    assert extended(40902,24140)[0]==(337,-571,34)
    assert extended(31408,2718)[0]==(2,-23,302)
    assert binary(31408,2718)[2][0][:2]==(1963,1359)
    return dict(pairs=count,examples={
        'euclid_40902_24140':euclid(40902,24140),
        'binary_40902_24140':binary(40902,24140),
        'ternary_40902_24140':ternary(40902,24140),
        'extended_40902_24140':extended(40902,24140),
        'extended_31408_2718':extended(31408,2718),
        'negative_lcm_witness':dict(u=1,v=2,terminal=extended(1,2)[:2],lcm=2)})


def machine(b,entry,u,v):
    m=Machine(b,source=SOURCE)
    m.memory[m.symbols['U']]=word(u)
    m.memory[m.symbols['V']]=word(v)
    for reg in m.reg:m.reg[reg]=Word(-1,b*b-1)
    m.ret=m.symbols[entry+'_END'];m.max_steps=10000
    m.execute(entry)
    assert m.halt is None and not m.ov
    return m


def binary_instructions():
    rng=random.Random(45200);count=0
    for b in [64,100]:
        W=b**5
        for _ in range(400):
            a,x=rng.randrange(W),rng.randrange(W)
            sa,sx=rng.choice([-1,1]),rng.choice([-1,1]);n=rng.randrange(81)
            for op in ['SLB','SRB']:
                m=Machine(b,source=SOURCE)
                m.rows=[['shift','TEST',op,str(n)]];m.symbols={'TEST':0};m.ret=1
                m.reg['A']=Word(sa,a);m.reg['X']=Word(sx,x)
                m.execute('TEST')
                raw=(a*W+x)*2**n%(W*W) if op=='SLB' else (a*W+x)//2**n
                assert m.reg['A']==Word(sa,raw//W) and m.reg['X']==Word(sx,raw%W)
                assert m.time==2
                count+=1
    return dict(instructions=count,byte_bases=[64,100],independent_signs=True)


def mix():
    rng=random.Random(45202);count=0;visits=set();maxima=[]
    for b in [64,100]:
        w=b**5
        cases=list(product(range(64),repeat=2))
        edge={0,1,2,3,w-2,w-1}
        for i in range(w.bit_length()):
            for d in [-1,0,1]:
                n=2**i+d
                if 0<=n<w:edge.add(n)
        # Edges paired with fixed contrasting magnitudes and common powers of 2.
        cases.extend(product(sorted(edge),[0,1,2,3,w//2,w-1]))
        cases.extend((rng.randrange(w),rng.randrange(w)) for _ in range(500))
        for u,v in cases:
            g=gcd(u,v);m=machine(b,'A',u,v)
            assert m.reg['A'].val==g,(b,u,v,m.reg)
            _,rows=euclid(v,u) # Program A begins with v mod u.
            assert m.visits['A05']==len(rows)
            assert m.time==19*len(rows)+6
            visits.update(m.trace);count+=1
            if u and v:
                m=machine(b,'B',u,v);_,s,_=binary(u,v)
                assert m.reg['A'].val==g,(b,u,v,m.reg)
                assert m.time==binary_time(s),(b,u,v,m.time,s)
                assert m.visits['B06']==s['A'] and m.visits['B12']==s['B']
                assert m.visits['B21']==s['C'] and m.visits['B13']==s['D']
                assert m.visits['B16']==s['E']
                visits.update(m.trace);count+=1
        for n in range(1,min(w.bit_length(),16)):
            u,v=(1,1) if n==1 else (2**n-2,2**n-1)
            m=machine(b,'B',u,v)
            assert m.time==(19 if n==1 else 13*n+8)
            maxima.append(dict(byte_base=b,N=n,u=u,v=v,time=m.time))
    return dict(machine_runs=count,visited_source_rows=sorted(visits),worst_witnesses=maxima)


def identities():
    count=0
    for u,v,w in product(range(21),repeat=3):
        assert gcd(u,v)*w==gcd(u*w,v*w)
        assert lcm(u,v)*w==lcm(u*w,v*w)
        assert u*v==gcd(u,v)*lcm(u,v)
        assert gcd(lcm(u,v),lcm(u,w))==lcm(u,gcd(v,w))
        assert lcm(gcd(u,v),gcd(u,w))==gcd(u,lcm(v,w))
        if u and v*w%u==0:assert gcd(u,v)*gcd(u,w)%u==0
        count+=1
    bijections=0
    for n in range(1,101):
        ds=[x for x in range(1,n*n+1) if n*n%x==0]
        pairs={(gcd(d,n),n*n//lcm(d,n)) for d in ds}
        divs=[x for x in range(1,n+1) if n%x==0]
        oracle={(u,v) for u,v in product(divs,repeat=2) if lcm(u,v)==n}
        assert len(pairs)==len(ds) and pairs==oracle
        bijections+=len(ds)
    return dict(triples=count,bijection_pairs=bijections)


def statistics():
    output=[]
    for n in range(1,9):
        M=2**n-1;sums=Counter();hist=Counter();maximum=0;witness=None
        for u,v in product(range(1,M+1),repeat=2):
            _,s,_=binary(u,v);sums.update(s);hist[s['A']]+=1
            t=binary_time(s)
            if t>maximum:maximum=t;witness=[u,v]
        den=M*M
        assert F(sums['A'],den)==F(1,3)-F(4,3*M)+F(n,den)
        assert F(sums['B'],den)==F(1,3)-F(1,3*M)
        assert 2*sums['E']==sums['C']-den+2*sums['B']
        assert maximum==(19 if n==1 else 13*n+8)
        assert hist==Counter({k:(2**(n-k)-1)**2-(2**(n-k-1)-1)**2 for k in range(n)})
        output.append(dict(N=n,pairs=den,sums=dict(sums),A_histogram=dict(hist),maximum_time=maximum,witness=witness))
    return dict(exact_distributions=output,limit_A_mean='1/3',limit_A_stddev='2/3')


def counterexamples():
    # Literal signed subtraction and ordinary max in the printed answer 5.
    u,v=1,7;rows=[]
    for _ in range(3):
        t=u-v if (u-v)%3==0 else u+v
        assert t
        while t%3==0:t//=3
        old=(u,v)
        if u>v:u=t
        else:v=t
        rows.append(dict(before=old,t=t,after=(u,v)))
    assert rows[0]['after']==(1,-2)
    assert rows[1]['before']==rows[1]['after']==rows[2]['after']==(1,-2)
    a,b,trace=extended(1,2)
    assert b[0]==-2 and b[0]*1==-2 and lcm(1,2)==2
    assert extended(0,0)[:2]==((1,0,0),(0,1,0))
    # Algorithm C, as stated for arbitrary integers and n>=1.
    xs=[-1];d=xs[-1];k=len(xs)-1
    while d!=1 and k>0:d=gcd(xs[k-1],d);k-=1
    assert d==-1 and gcd(*xs)==1
    return dict(ternary_literal_cycle=rows,extended_lcm=dict(u=1,v=2,a=a,b=b,trace=trace),
                singleton_fold=dict(inputs=xs,result=d,correct=1),binary_N1=dict(inputs=[1,1],time=machine(64,'B',1,1).time,printed_bound=21))


if __name__=='__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('binary_instructions',binary_instructions),('arithmetic',arithmetic),('mix',mix),('identities',identities),('statistics',statistics),('counterexamples',counterexamples)]:
        if name in data:continue
        start=time.monotonic();value=fn()
        data[name]=dict(status='passed',seconds=time.monotonic()-start,result=value)
        OUT.write_text(json.dumps(data,indent=2)+'\n')
        print(name, 'passed',round(data[name]['seconds'],3),flush=True)
