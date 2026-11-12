"""Independent polynomial/recurrence checks for TAOCP2 §3.6 code.

Original typeset code and 2002 replacements are distinguished. Compiled
current author sources stay byte-for-byte unchanged in sources/.
"""
from pathlib import Path
import argparse, ctypes, json, subprocess
from fractions import Fraction

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/summary-generators.json'
K, L, T = 100, 37, 70
Q = (1 << K) - 1
F = (1 << K) | (1 << L) | 1


def mul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1; a <<= 1
        if a >> K: a ^= F
    return r


def power(e):
    a, r = 2, 1
    while e:
        if e & 1: r = mul(r, a)
        a = mul(a, a); e >>= 1
    return r


def exponent(s):
    # Read the seed from least to most significant, after a leading 1.
    e = 1
    while s:
        e = 2*e + s % 2; s //= 2
    return e << (T-1)


def poly(state):
    return sum((v & 1) << ((i+L) % K) for i, v in enumerate(state))


def direct(state, n, bits=30, sign=-1):
    """Unsplit recurrence, independent of ran_array's buffer management."""
    m = 1 << bits
    values = list(state)
    for j in range(K, n+K): values.append((values[j-K]+sign*values[j-L]) % m)
    return values[:n], values[n:n+K]


def block(state, n, bits=30, sign=-1):
    m = 1 << bits
    aa = list(state)
    for j in range(K, n): aa.append((aa[j-K]+sign*aa[j-L]) % m)
    out = [0]*K
    for i in range(L): out[i]=(aa[n+i-K]+sign*aa[n+i-L]) % m
    for i in range(L, K): out[i]=(aa[n+i-K]+sign*out[i-L]) % m
    return aa, out


def start(seed, bits=30, version='original', sign=-1):
    """Integer lift of original or revised code, including floating variants."""
    m = 1 << bits
    x = [0]*(2*K-1)
    ss = ((seed+2) & (m-2)) if sign == -1 else 2*(seed+2)
    for j in range(K):
        x[j] = ss
        ss *= 2
        if ss >= m: ss -= m-2
    x[1] += 1
    s, t = seed & ((1 << 30)-1), T-1
    while t:
        for j in range(K-1, 0, -1):
            x[2*j] = x[j]
            if version == 'revised': x[2*j-1] = 0
        if version == 'original':
            for j in range(2*K-2, K-L, -2): x[2*K-1-j] = x[j] & (m-2)
        for j in range(2*K-2, K-1, -1):
            if version == 'revised' or x[j] & 1:
                x[j-(K-L)] = (x[j-(K-L)] + sign*x[j]) % m
                x[j-K] = (x[j-K] + sign*x[j]) % m
        if s & 1:
            for j in range(K, 0, -1): x[j] = x[j-1]
            x[0] = x[K]
            if version == 'revised' or x[K] & 1: x[L] = (x[L]+sign*x[K]) % m
        if s: s >>= 1
        else: t -= 1
    state = x[L:K]+x[:L]
    if version == 'revised':
        for j in range(10): _, state = direct(state, 2*K-1, bits, sign)
    assert all(0 <= z < m for z in state)
    return state


def fortran_start(seed, version):
    """One-based transcription of answer10; permitted original seed range."""
    m=1 << 30; x=[0]*(2*K)
    sseed=seed % m; ss=sseed-sseed % 2+2
    for j in range(1,K+1):
        x[j]=ss; ss+=ss
        if ss >= m: ss=ss-m+2
    x[2]+=1; ss=sseed; t=T-1
    def subtract(a,b):
        d=a-b
        return d+m if d<0 else d
    while True:
        for j in range(K,1,-1):
            x[j+j-1]=x[j]
            if version=='revised':x[j+j-2]=0
        if version=='original':
            for j in range(2*K-1,K-L,-2):x[2*K-1-j+2]=x[j]-x[j]%2
        for j in range(2*K-1,K,-1):
            if version=='revised' or x[j]%2==1:
                x[j-(K-L)]=subtract(x[j-(K-L)],x[j])
                x[j-K]=subtract(x[j-K],x[j])
        if ss%2==1:
            for j in range(K,0,-1):x[j+1]=x[j]
            x[1]=x[K+1]
            if version=='revised' or x[K+1]%2==1:x[L+1]=subtract(x[L+1],x[K+1])
        if ss:ss//=2
        else:t-=1
        if t<=0:break
    out=x[L+1:K+1]+x[1:L+1]
    if version=='revised':
        for _ in range(10):_,out=direct(out,199)
    return out


def polynomial_checks():
    seeds=list(range(128))+[310952,12509,(1<<29),(1<<30)-3]
    cases=0
    witnesses={}
    for version in ['original','revised']:
        offset=1990 if version=='revised' else 0
        for s in seeds:
            a=start(s,version=version)
            expected=power((exponent(s)-offset) % Q)
            assert poly(a)==expected, (version,s)
            assert fortran_start(s,version)==a
            if s==0:witnesses[version]={'polynomial_hex':hex(expected),'first_word':a[0]}
            for n in [100,101,136,137,199,200,1009]:
                seq, end=direct(a,n)
                assert block(a,n)==(seq,end)
                assert poly(end)==mul(expected,power((-n)%Q))
                cases+=1
    # Counterexample to replacing modular distance by ordinary distance.
    s,sp,n,np=0,1<<29,(1<<99)-1,0
    assert (exponent(s)-n-exponent(sp)+np)%Q==0
    assert abs(n-np)<abs(exponent(s)-exponent(sp))
    assert power((exponent(s)-n)%Q)==power(exponent(sp))
    # All small exact analogues of the exponent spacing, not sampled seeds.
    spacing=0
    for e in range(1,11):
        for t in range(2,8):
            k=t+e
            q=(1<<k)-1
            hs=[]
            for s in range(1<<e):
                a=1; v=s
                while v:a=2*a+v%2;v//=2
                hs.append(a << (t-1))
            assert len(set(hs))==len(hs)
            v=sorted(hs)
            assert min([b-a for a,b in zip(v,v[1:])]+[q-v[-1]+v[0]])==(1<<t)-1
            assert set([hs.index(v[-1]),hs.index(v[0])])=={0,(1<<e)-1}
            spacing+=1
    return dict(seed_versions=len(seeds)*2,one_based_fortran_states=len(seeds)*2,
        recurrence_polynomial_cases=cases,exhaustive_spacing_parameter_sets=spacing,
        seed0=witnesses,modular_distance_witness={'s':0,'s_prime':1<<29,'n':(1<<99)-1,'n_prime':0,'ordinary_h_distance':1<<99})


def compiled_checks(tmp):
    results=[]
    for floating in [False,True]:
        name='knuth-rng-double.c' if floating else 'knuth-rng.c'
        so=tmp/(name+'.so')
        subprocess.run(['cc','-std=c99','-O2','-shared','-fPIC','-Dmain=knuth_reference_main',str(ROOT/'sources'/name),'-o',str(so)],check=True)
        lib=ctypes.CDLL(str(so)); typ=ctypes.c_double if floating else ctypes.c_long
        init=lib.ranf_start if floating else lib.ran_start
        arr=lib.ranf_array if floating else lib.ran_array
        init.argtypes=[ctypes.c_long];arr.argtypes=[ctypes.POINTER(typ),ctypes.c_int]
        state=(typ*K).in_dll(lib,'ran_u' if floating else 'ran_x')
        bits,sign=(52,1) if floating else (30,-1)
        scale=1<<bits if floating else 1
        trials=words=0
        for seed in [0,1,2,3,12509,310952,(1<<29),(1<<30)-3]:
            init(seed);ref=start(seed,bits,'revised',sign)
            assert [int(z*scale) for z in state]==ref
            for n in [100,101,137,199,1009,2009]:
                buf=(typ*n)();arr(buf,n);expected,ref=direct(ref,n,bits,sign)
                assert [int(z*scale) for z in buf]==expected
                assert [int(z*scale) for z in state]==ref
                words+=n+K;trials+=1
        rudimentary=[]
        for count,n in [(2009,1009),(1009,2009)]:
            init(310952);buf=(typ*n)()
            for _ in range(count):arr(buf,n)
            rudimentary.append(format(state[0],'.20f') if floating else state[0])
        assert rudimentary==(['0.36410514377569680455']*2 if floating else [995235265]*2)
        results.append(dict(floating=floating,compiled_source=name,block_calls=trials,exact_word_comparisons=words,rudimentary=rudimentary))
    # Original/reference checkpoints use an unsplit integer recurrence.
    original=[]
    for bits,sign,seed,expected in [(30,-1,310952,461390032),(15,-1,12509,9387),(52,1,310952,'0.27452626307394156768')]:
        state=start(seed,bits,'original',sign)
        _,end=direct(state,1009*2009,bits,sign)
        got=format(end[0]/(1<<bits),'.20f') if sign==1 else end[0]
        assert got==expected,(bits,got,expected)
        original.append(dict(bits=bits,seed=seed,output=got,method='integer recurrence'))
    state=start(12509,15,'revised');_,end=direct(state,1009*2009,15)
    assert end[0]==24130
    return dict(current=results,original=original,revised_15bit=24130)


def wrapper_checks(tmp):
    # Include verbatim current source with a renamed main, and export its macro.
    records=[]
    for floating in [False,True]:
        stem='knuth-rng-double.c' if floating else 'knuth-rng.c'
        prefix='ranf' if floating else 'ran';ctype='double' if floating else 'long'
        harness=tmp/(stem+'-wrapper.c');so=tmp/(stem+'-wrapper.so')
        harness.write_text('#define main original_main\n#include "'+str(ROOT/'sources'/stem)+'"\n'+ctype+' audit_next(void) { return '+prefix+'_arr_next(); }\n')
        subprocess.run(['cc','-std=c99','-O2','-shared','-fPIC',str(harness),'-o',str(so)],check=True)
        lib=ctypes.CDLL(str(so));nxt=lib.audit_next;nxt.restype=ctypes.c_double if floating else ctypes.c_long
        init=getattr(lib,prefix+'_start');init.argtypes=[ctypes.c_long]
        bits,sign=(52,1) if floating else (30,-1);scale=(1<<bits) if floating else 1
        checks=0
        # Default initialization, then explicit reseeding after partial buffers.
        for seed,call_init in [(314159,False),(0,True),(310952,True),(0,True)]:
            if call_init:init(seed)
            state=start(seed,bits,'revised',sign);expected=[]
            for _ in range(4):
                arr,state=direct(state,1009,bits,sign);expected.extend(arr[:100])
            for v in expected[:313]:assert int(nxt()*scale)==v;checks+=1
        records.append(dict(floating=floating,checked_outputs=checks))
    return records


def lcg_checks():
    constants=[]
    for a,m in [(48271,2147483647),(40692,2147483399),(157,32363),(146,31727),(142,31657)]:
        q,r=divmod(m,a);assert r<q
        candidates={1,m-1,q-1,q,q+1}
        for j in range(a+1):
            for d in [-1,0,1]:
                x=j*q+d
                if 0<x<m:candidates.add(x)
        for x in candidates:
            y=a*(x%q)-r*(x//q)
            assert -m<y<m
            assert (y+m if y<0 else y)==a*x%m
        constants.append(dict(a=a,m=m,q=q,r=r,division_boundary_cases=len(candidates)))
    assert pow(48271,1000000,2147483647)==1263606197
    # The printed 'evaluate one power modulo (a-1)m, then divide' identity.
    identities=0
    for m in range(2,25):
        for a in range(2,12):
            for c in range(4):
                for seed in [0,m-1]:
                    x=seed
                    for n in range(13):
                        y=(pow(a,n,(a-1)*m)*(seed*(a-1)+c)-c)%((a-1)*m)
                        assert y%(a-1)==0 and y//(a-1)==x
                        x=(a*x+c)%m;identities+=1
    return dict(schrage_constants=constants,affine_power_identities=identities,millionth=1263606197)


def errata_compile_check(tmp):
    source=ROOT/'repro_errata_ranf.c'
    result=subprocess.run(['cc','-std=c99','-fsyntax-only',str(source)],capture_output=True,text=True)
    assert result.returncode!=0 and 'undeclared' in result.stderr and 'x' in result.stderr
    (ROOT/'results/errata-ranf-compile.log').write_text(result.stderr)
    exe=tmp/'errata-ranf-repaired'
    subprocess.run(['cc','-std=c99','-O2','-DAUDIT_REPAIR',str(source),'-o',str(exe)],check=True)
    run=subprocess.run([str(exe)],capture_output=True,text=True,check=True)
    assert run.stdout.splitlines()==['0.36410514377569680455']*2
    return dict(unrepaired_compiler_returncode=result.returncode,diagnostic='results/errata-ranf-compile.log',repair='Add int x[KK+KK-1] declaration',repaired_outputs=run.stdout.splitlines())


def small_prime_checks():
    from math import isqrt,lcm
    rows=[]
    for a,m in [(157,32363),(146,31727),(142,31657)]:
        assert all(m%d for d in range(2,isqrt(m)+1))
        n=m-1; p=2; factors=[]
        while p*p<=n:
            if n%p==0:
                factors.append(p)
                while n%p==0:n//=p
            p+=1
        if n>1:factors.append(n)
        residues=[pow(a,(m-1)//q,m) for q in factors]
        assert pow(a,m-1,m)==1 and all(x!=1 for x in residues)
        rows.append(dict(a=a,m=m,prime_divisors=factors,residues=residues))
    return dict(rows=rows,combined_state_period=lcm(32362,31726,31656))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');ap.add_argument('--tmp',required=True);args=ap.parse_args()
    tmp=Path(args.tmp);assert tmp.is_dir()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}
    tasks=[('polynomial',polynomial_checks),('compiled',lambda:compiled_checks(tmp)),('wrapper',lambda:wrapper_checks(tmp)),('lcg',lcg_checks),('errata_compile',lambda:errata_compile_check(tmp)),('small_primes',small_prime_checks)]
    for name,fn in tasks:
        if name in data:continue
        data[name]=fn();OUT.write_text(json.dumps(data,indent=2)+'\n');print('PASS',name,flush=True)
    print('ALL',len(tasks),'blocks passed',flush=True)
if __name__=='__main__':main()
