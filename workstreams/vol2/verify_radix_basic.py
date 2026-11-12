#!/usr/bin/env python3
"""Exact checks for TAOCP 4.4 A/B and exercises1–5,7,8,10,19.

Independent integer/rational oracles accompany digit algorithms and literal
MIX instruction execution. Successful blocks are checkpoints, not rerun.
"""
from collections import Counter
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import argparse, json, random, time
from mix_float_machine import Machine, Word, word

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/radix-basic.json'
SOURCE = ROOT / 'sources/radix-basic.mix'


def encode(u, bases):
    ds = []
    for b in bases:
        u, r = divmod(u, b)
        ds.append(r)
    return ds + [u]


def decode(ds, bases):
    u = ds[-1]
    for b, d in zip(reversed(bases), reversed(ds[:-1])):
        u = u*b + d
    return u


def maddmul(ds, bases, multiplier, addend):
    carry = addend
    out = []
    for d, b in zip(ds[:-1], bases):
        carry, r = divmod(multiplier*d + carry, b)
        out.append(r)
    return out + [multiplier*ds[-1] + carry]


def mdivide(ds, bases, divisor):
    out = [0]*len(ds)
    out[-1], r = divmod(ds[-1], divisor)
    for j in range(len(bases)-1, -1, -1):
        out[j], r = divmod(r*bases[j] + ds[j], divisor)
        assert 0 <= out[j] < bases[j]
    return out, r


def mixed_block():
    src, dst = [60,60,24], [16,14,8,20]
    ds = encode(0, dst)
    trace = [ds[::-1]]
    for mul, add in [(1,3),(24,0),(1,9),(60,0),(1,12),(60,0),(1,37)]:
        ds = maddmul(ds,dst,mul,add)
        trace.append(ds[::-1])
    expected = [[0,0,0,0,0],[0,0,0,0,3],[0,0,0,4,8],
                [0,0,0,5,1],[0,2,5,9,12],[0,2,5,10,8],
                [8,3,1,0,0],[8,3,1,2,5]]
    assert trace == expected
    u = 3*86400 + 9*3600 + 12*60 + 37
    assert u == decode(ds,dst) == 292357
    q = [37,12,9,3]
    divtrace = [q[::-1]]
    remainders = []
    for d in dst:
        q,r = mdivide(q,src,d)
        divtrace.append(q[::-1]); remainders.append(r)
    assert divtrace == [[3,9,12,37],[0,5,4,32],[0,0,21,45],
                        [0,0,2,43],[0,0,0,8]]
    assert remainders + [decode(q,src)] == ds
    rng = random.Random(44012)
    for _ in range(2000):
        a = [rng.randrange(2,31) for _ in range(rng.randrange(1,9))]
        b = [rng.randrange(2,31) for _ in range(rng.randrange(1,9))]
        u = rng.randrange(1 << rng.randrange(1,100))
        digits = encode(u,a)
        got = encode(digits[-1],b)
        for radix,digit in zip(reversed(a),reversed(digits[:-1])):
            got = maddmul(got,b,radix,digit)
        assert decode(got,b) == u
        quot = digits; rem = []
        for radix in b:
            old = decode(quot,a)
            quot,r = mdivide(quot,a,radix)
            assert (decode(quot,a),r) == divmod(old,radix)
            rem.append(r)
        assert rem + [decode(quot,a)] == got
    return {'table1':trace,'table2':divtrace,'value':292357,
            'mixed_cases':2000}


def shortest(u, eps, B):
    original, tolerance = u, eps
    ds = [0]; M = 0
    while not (u < eps or u > 1-eps):
        M += 1
        t = u*B; digit = t.numerator // t.denominator
        ds.append(digit); u=t-digit; eps*=B
        assert M < 500
    up = u >= F(1,2)
    if up:
        assert M == 0 or ds[-1] < B-1
        ds[-1] += 1
    v = F(decode(ds[::-1],[B]*M), B**M)
    assert abs(v-original) < tolerance
    # Oracle: nearest lattice point at each shorter output length.
    for k in range(M):
        scaled = original*B**k
        lo = scaled.numerator//scaled.denominator
        assert min(abs(F(lo,B**k)-original),abs(F(lo+1,B**k)-original)) >= tolerance
    return M, ds, v


def fractions_block():
    cases = 0; ties = 0; zero_length = 0
    for b in range(2,17):
        for m in [1,2,3]:
            den = b**m
            nums = sorted(set([1,den-1,den//2] + list(range(1,min(den,30)))))
            for t in nums:
                if not 0 < t < den: continue
                u = F(t,den)
                for B in [2,3,8,10,16]:
                    for eps in [F(1,2*den),F(1,den),F(1,3),F(2,3)]:
                        M,ds,v = shortest(u,eps,B)
                        assert abs(v-u) < eps
                        zero_length += M == 0
                        ties += (u*B**M).denominator == 2
                        if eps == F(1,2*den):
                            nearest = (v*den + F(1,2)).numerator // (v*den + F(1,2)).denominator
                            assert nearest == t
                        # Method2b, exactly, in reverse digit order.
                        src = encode(t,[b]*m)[:-1]; x=F(0)
                        for d in src: x=(x+d)/b
                        assert x == u
                        # Fixed-output method2a versus direct integer quotient.
                        x=u; value=0
                        for _ in range(M+2):
                            x*=B; d=x.numerator//x.denominator
                            x-=d; value=value*B+d
                        assert value == (t*B**(M+2))//den
                        cases += 1
    # General termination condition, checked against gcd of exact denominators.
    termination=0
    def prime_set(n):
        out=set();d=2
        while d*d<=n:
            while n%d==0:out.add(d);n//=d
            d+=1
        if n>1:out.add(n)
        return out
    for b in range(2,51):
        for B in range(2,51):
            remaining=b
            while (g:=gcd(remaining,B))>1:remaining//=g
            assert (remaining==1) == (prime_set(b)<=prime_set(B))
            termination+=1
    return {'fraction_cases':cases,'tie_cases':ties,'zero_digit_answers':zero_length,
            'termination_base_pairs':termination}


def constants_block():
    choices=0; input_checks=0
    for bits in range(4,10):
        w=1<<bits
        for D in [10,100]:
            if D>=w:continue
            g=gcd(w,D)
            for c in range(w):
                good=True
                for u in range(D):
                    q=(w*u+c)//D
                    actual=D*q//w
                    input_checks+=1
                    if actual != u:good=False;break
                assert good == (c>=D-g),(w,D,c,g)
                choices+=1
    w=64**5; D=10; c=8
    example=[{'u':u,'q':(w*u+c)//D,'output':D*((w*u+c)//D)//w} for u in range(D)]
    assert all(x['u']==x['output'] for x in example)
    # Exercise7 with exact endpoint arithmetic, including u=w.
    bounds=0
    for w in range(1,80):
        for den in [1,2,3,5,10,17]:
            a=F(1,den)
            for h in [0,1,2,3]:
                x=a+F(h,4*w)
                for u in range(w+1):
                    au=a*u;ux=x*u
                    qa=au.numerator//au.denominator;qx=ux.numerator//ux.denominator
                    assert qx in [qa,qa+1]
                    if u<a*w:assert qx==qa
                    bounds+=1
    return {'constant_choices':choices,'input_checks':input_checks,
            'exercise5_counterexample':{'w':64**5,'D':10,'c':8,'rows':example},
            'exercise7_cases':bounds}


class RadixMachine(Machine):
    def __init__(self,beta=64,n=1,m=1,ceil_only=False,store_only=False):
        super().__init__(beta,source=SOURCE)
        self.symbols.update(U=1000,C=1001,D=1002,INPUT=1100,ANSWER=1200,N=n,M=m)
        self.external=set(range(1000,1003))|set(range(1100,1120))|set(range(1200,1220))
        self.writes=[];self.events=[]
        for a in self.external:self.memory[a]=word(0)
        self.memory[1001]=word(10**n);self.memory[1002]=word(10**n)
        if ceil_only:
            next(r for r in self.rows if r[0]=='E803')[3]='1UP'
            self.symbols['1UP']=1003;self.external.add(1003);self.memory[1003]=word((self.w+9)//10)
        if store_only:
            next(r for r in self.rows if r[0]=='F804')[3]='=1//10='
        self.max_steps=2000
    def constant(self,s):
        if s=='1//10':return self.w//10
        if s=='1//10+1':return self.w//10+1
        return super().constant(s)
    def store(self,addr,field,v):
        if addr>=len(self.rows):
            assert addr in self.external and field==(0,5),(addr,field)
            self.memory[addr]=v;self.writes.append(addr)
        else:super().store(addr,field,v)
    def observer(self,m,src):
        if src in ['E803','E804','E807','E812','F813']:
            self.events.append({'line':src,'A':self.reg['A'].val,'X':self.reg['X'].val,'U':self.memory[1000].val})
    def run(self,entry,u,n=1,c=None):
        self.memory[1000]=word(u)
        if c is not None:self.memory[1001]=word(c)
        self.ret=self.symbols[entry+'_END'];self.execute(entry)
        length=n if entry=='R4' else self.reg['1'].mag
        return [self.memory[1200+j].val for j in range(length)]


def mix_block():
    rng=random.Random(4408);counts=Counter();cex={};corrections=0
    for variant in ['original','ceil_only','store_only','both']:
        mm=RadixMachine(ceil_only=variant=='ceil_only',store_only=variant=='store_only')
        entry='E8FIX' if variant in ['store_only','both'] else 'E8'
        ds=mm.run(entry,10)
        cex[variant]={'digits_lsd_first':ds,'trace':mm.events,'cycles':mm.time}
        assert ds == {'original':[10],'ceil_only':[0,10],'store_only':[10],'both':[0,1]}[variant]
    for beta in [64,256]:
        w=beta**5
        sample=set(range(1000))|{w-1,w-2,w//2,w//10,w//10-1}
        sample.update(rng.randrange(w) for _ in range(250))
        for u in sorted(sample):
            want=[int(c) for c in str(u)[::-1]]
            for entry in ['R1','E8FIX']:
                mm=RadixMachine(beta)
                got=mm.run(entry,u)
                assert got==want,(beta,entry,u,got,want)
                assert not mm.ov and mm.halt is None
                assert mm.memory[1000].val==u
                if entry=='R1':assert mm.time==18*len(want)+4
                else:
                    retries=mm.visits['F810'];assert retries<=1
                    corrections+=retries
                    assert mm.time==35*len(want)+3+21*retries,(u,mm.time,len(want),retries)
                counts[entry]+=1
        n=1
        while 10**n<w:
            D=10**n; g=gcd(w,D)
            inputs=set(range(min(D,50)))|{D-1,D-2,D//2}
            inputs.update(rng.randrange(D) for _ in range(40))
            for u in inputs:
                for c in set([D,D-1,D-g,w-1]):
                    mm=RadixMachine(beta,n=n)
                    got=mm.run('R4',u,n,c)
                    assert got==[int(z) for z in f'{u:0{n}d}'[::-1]]
                    assert mm.time==16*n+19 and not mm.ov and mm.halt is None
                    counts['R4']+=1
            for u in [D,w-1]:
                mm=RadixMachine(beta,n=n);mm.run('R4',u,n)
                assert mm.halt==98;counts['R4_overflow']+=1
            n+=1
        for length in range(2,n):
            for _ in range(80):
                u=rng.randrange(10**length);ds=[int(x) for x in f'{u:0{length}d}'[::-1]]
                mm=RadixMachine(beta,m=length-1)
                for j,d in enumerate(ds):mm.memory[1100+j]=word(d)
                mm.ret=mm.symbols['R6_END'];mm.execute('R6')
                assert mm.reg['A'].val==u and not mm.ov
                assert mm.visits['R603']==length-1
                counts['R6']+=1
    return {'instruction_runs':dict(counts),'correction_paths':corrections,'exercise8_counterexamples':cex}


def pack(u):return int(str(u),16)


def bcd_block():
    rng=random.Random(441019);cases=0
    sample=list(range(10000))+[rng.randrange(10**rng.randrange(1,25)) for _ in range(2000)]
    for u in sample:
        digits=len(str(u));x=pack(u)
        h=(x+int('3'*digits,16)) & int('8'*digits,16)
        doubled=x+x+h-(h>>2)
        assert doubled==pack(2*u)
        half=x>>1;h=half & int('8'*digits,16)
        half-=(h>>2)+(h>>3)
        assert half==pack(u//2)
        cases+=1
    table=[0x369,0x69c,0x088,0x066,0x3cf,0x738]
    x=table[0];h=(x+0x333)&0x888
    assert [x,x+0x333,h,h-(h>>2),x+h-(h>>2),2*x+h-(h>>2)]==table
    masks=[0xf0f0f0f0,0xff00ff00,0xffff0000]
    packed=0
    sample=list(range(10000))+[10**8-1,0,10**7,99990000,90909090,10101010]
    sample += [rng.randrange(10**8) for _ in range(5000)]
    for u in sample:
        x=pack(u)
        for d,mask in zip([1,2,4],masks):
            selected=x&mask
            assert selected%(16**d)==0
            x=x-selected+(selected//16**d)*10**d
            assert 0<=x<2**32
        assert x==u;packed+=1
    return {'doubling_halving_cases':cases,'table1_hex':[hex(x) for x in table],
            'eight_digit_packed_cases':packed,'masks_hex':[hex(x) for x in masks]}


BLOCKS={'mixed':mixed_block,'fractions':fractions_block,'constants':constants_block,
        'mix':mix_block,'bcd':bcd_block}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--resume',action='store_true')
    parser.add_argument('--blocks',nargs='*',choices=list(BLOCKS));args=parser.parse_args()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'scope':'4.4 A/B and1–5,7,8,10,19','blocks':{}}
    for name in args.blocks or BLOCKS:
        if name in data['blocks']:continue
        t=time.monotonic();result=BLOCKS[name]()
        data['blocks'][name]={'status':'passed','seconds':time.monotonic()-t,'result':result}
        OUT.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'checkpoint':name,**data['blocks'][name]},ensure_ascii=False),flush=True)


if __name__=='__main__':main()
