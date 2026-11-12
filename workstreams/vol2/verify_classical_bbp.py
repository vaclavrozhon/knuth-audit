#!/usr/bin/env python3
"""Exact interval bit extraction and algebra for TAOCP 4.3.1-39.
Independent oracle: fixed-point alternating Machin arctangent series.
The bit extractor never constructs 2**n; the oracle intentionally may.
"""
from pathlib import Path
import json, random, sys, time
import sympy as s

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/classical-bbp.json'
results=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
def checkpoint(name, value):
    results[name]=value
    OUT.write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
    print(name, json.dumps(value,ensure_ascii=False),flush=True)

def identities():
    z=s.symbols('z',real=True); rt=s.sqrt(2); I=s.I
    A=s.log((1+z)/(1-z))/8
    B=s.log((1+rt*z+z*z)/(1-rt*z+z*z))/(8*rt)
    C=s.atan(z)/4; D=s.atan(rt*z/(1-z*z))/(4*rt)
    for a,f in [(1,A+B+C+D),(5,A-B+C-D),(3,A-B-C+D),(7,A+B-C-D)]:
        assert s.simplify(s.diff(f,z)-z**(a-1)/(1-z**8))==0
        assert f.subs(z,0)==0
    # Formal real symbols: ln2,ln3,ln5,ln(1+sqrt2),atan(1/sqrt2),atan(1/3),pi.
    L2,L3,L5,H,T,W,P=s.symbols('L2 L3 L5 H T W P',real=True)
    logs=[-H-L2/2,-L2/2-I*P/4,(L3-L2)/2-I*T,(L5-L2)/2-I*W,
          H-L2/2,(L5-L2)/2+I*W,(L3-L2)/2+I*T,-L2/2+I*P/4]
    q=(1+I)/rt
    roots=[s.expand_complex(q**r).simplify() for r in range(8)]
    S=[s.expand(-2**s.Rational(j,2)*sum(roots[(-j*r)%8]*logs[r] for r in range(8))/8)
       for j in range(1,9)]
    one=s.Rational
    rows=[([4,0,0,-2,-1,-1,0,0],P),
          ([0,1,0,one(1,2),0,one(1,4),0,one(1,8)],L2),
          ([0,2,0,0,0,one(1,2),0,0],L3),
          ([0,2,0,2,0,one(1,2),0,0],L5),
          ([1,0,one(1,2),0,one(1,4),0,one(1,8),0],rt*H),
          ([1,0,-one(1,2),0,one(1,4),0,-one(1,8),0],rt*T),
          ([1,-1,0,-one(1,2),-one(1,4),0,0,0],W),
          ([8,-8,-4,-8,-2,-2,1,0],0)]
    for co,target in rows: assert s.expand(sum(c*x for c,x in zip(co,S))-target)==0
    coef=[s.simplify(-sum(rows[0][0][j-1]*2**s.Rational(j,2)*roots[(-j*r)%8]
                         for j in range(1,9))/8) for r in range(8)]
    assert coef==[2,-2+2*I,0,0,2,0,0,-2-2*I]
    printed=2*logs[0]-2*(2-2*I)*logs[1]+2*logs[4]+(2+2*I)*logs[7]
    assert s.expand(printed-(P/2-L2)*(1+3*I))==0
    # Independent rational integral decomposition for the BBP identity.
    integrand=(4-2*z**3-z**4-z**5)/(1-z**8/16)
    # Derivatives of elementary primitives provide a second proof via Euler's series.
    euler_integrand=4*(2+2*z+z*z)/(4+z**4)
    zero_integrand=4*((1-z)/(2-2*z+z*z)-z/(2-z*z))
    assert s.cancel(integrand-euler_integrand-zero_integrand)==0
    return {'odd_generating_functions':4,'S_identities':len(rows),
            'root_filter_coefficients':[str(x) for x in coef],
            'printed_expression':'(pi/2-ln(2))*(1+3i)',
            'corrected_expression':'pi','independent_integral_decomposition':True}

def ceildiv(a,b): return -(-a//b)
def scaled_term(num,den,shift):
    if shift>=0: num<<=shift
    else: den<<=-shift
    return num//den,ceildiv(num,den)

def sj_interval(n,j,m):
    """Enclose 2**(n-1) S_j minus an integer; units 2**(-m)."""
    stop=(n+3)//4
    lo=hi=0
    for k in range(stop):
        den=8*k+j
        a=pow(2,n-1-4*k,den)
        l,h=scaled_term(a,den,m); lo+=l; hi+=h
    # Include enough tail terms that the remaining scaled tail is <1.
    # Extra terms bound tail roundoff explicitly; no floating-point decisions.
    count=(m+3)//4+2
    for k in range(stop,stop+count):
        l,h=scaled_term(1,8*k+j,m+n-1-4*k); lo+=l; hi+=h
    k=stop+count
    # Remaining denominators only grow; sum of the geometric majorant.
    _,tail=scaled_term(16,15*(8*k+j),m+n-1-4*k)
    hi+=tail
    return lo,hi

def bbp_bit(n,initial=None):
    assert n>=1
    m=max(4,2*n.bit_length()) if initial is None else initial
    attempts=0
    while True:
        attempts+=1
        vals=[sj_interval(n,j,m) for j in (1,4,5,6)]
        lo=4*vals[0][0]-2*vals[1][1]-vals[2][1]-vals[3][1]
        hi=4*vals[0][1]-2*vals[1][0]-vals[2][0]-vals[3][0]
        lower=(2*lo)//(1<<m); upper=(2*hi)//(1<<m)
        if lower==upper: return lower%2,m,attempts,hi-lo
        m=max(m+4,2*m)

def atan_oracle(q,p):
    """Enclose atan(1/q), scaled by 2**p, using alternating remainders."""
    scale=1<<p; power=q; k=0; lo=hi=0
    while True:
        den=(2*k+1)*power
        l,h=scale//den,ceildiv(scale,den)
        if k%2: lo-=h;hi-=l
        else: lo+=l;hi+=h
        k+=1;power*=q*q
        den=(2*k+1)*power
        if den>scale:
            tail=ceildiv(scale,den)
            if k%2: lo-=tail
            else: hi+=tail
            return lo,hi,k

def oracle_bits(positions):
    p=max(positions)+64
    a,b,ka=atan_oracle(5,p);c,d,kc=atan_oracle(239,p)
    lo,hi=16*a-4*d,16*b-4*c
    out={}
    for n in positions:
        l=lo>>(p-n);h=hi>>(p-n)
        assert l==h,('oracle ambiguous',n)
        out[n]=l%2
    return out,{'precision':p,'atan5_terms':ka,'atan239_terms':kc,'interval_width_ticks':hi-lo}

def bits():
    rng=random.Random(43139)
    positions=sorted(set(range(1,513))|{1000,1024,4096,8192,10000}|
                     {rng.randrange(513,6001) for _ in range(150)})
    oracle,info=oracle_bits(positions)
    out=[]
    for n in positions:
        bit,m,tries,width=bbp_bit(n)
        assert bit==oracle[n],(n,bit,oracle[n])
        out.append({'n':n,'bit':bit,'m':m,'attempts':tries,'width_ticks':width})
    forced=[]
    for n in range(1,65):
        bit,m,tries,width=bbp_bit(n,initial=2)
        assert bit==oracle[n]
        forced.append({'n':n,'m':m,'attempts':tries})
    assert max(row['attempts'] for row in forced)>1
    return {'ordinary_cases':len(out),'max_n':max(positions),'oracle':info,
            'max_m':max(row['m'] for row in out),
            'adaptive_cases':sum(row['attempts']>1 for row in out),
            'forced_low_precision_cases':len(forced),'forced':forced,'cases':out}

if __name__=='__main__':
    for name,fun in [('identities',identities),('bits',bits)]:
        if name not in results:
            t=time.monotonic(); value=fun();value['elapsed_seconds']=time.monotonic()-t
            checkpoint(name,value)
    print('ALL CHECKPOINTS PASSED',flush=True)
