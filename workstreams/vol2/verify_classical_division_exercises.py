#!/usr/bin/env python3
"""New exercise-specific checks, preserving the completed mathematical D census."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import argparse,json,random,time
import sympy as s
from verify_division import algorithm_d
from verify_classical_basic import ClassicalMachine,value
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/classical-division-exercises.json'


def estimates():
    rng=random.Random(4311724);count=0;triggers=Counter()
    for _ in range(30000):
        b=rng.randrange(2,101);n=rng.randrange(2,9)
        v=rng.randrange(b**(n-1),b**n);u=rng.randrange(b*v)
        a=v//b**(n-1);c=v//b**(n-2)%b;top=u//b**(n-1);z=u//b**(n-2)%b
        q,r=divmod(u,v);h=rng.randrange(b);rh=top-h*a
        if a>=b//2 and u//b**n==a:
            assert q in (b-2,b-1);triggers['17']+=1
        assert top//(a+1)<=q
        if h*c>b*rh+z:
            assert q<h;triggers['19']+=1
        else:
            assert q>=h-1;triggers['20_one_sided']+=1
            if h>=q:
                assert q in (h,h-1);triggers['20_upper_estimate']+=1
                if h!=q and a>=b//2:
                    assert r*b>=(b-2)*v;triggers['21']+=1
        count+=1
    b,n,u,v,h=10,2,100,50,1
    a=v//b;c=v%b;rh=u//b-h*a;q,r=divmod(u,v)
    assert a>=b//2 and h<b and h*c<=b*rh+u%b
    assert q not in (h,h-1) and r*b<(b-2)*v
    witness={'b':b,'n':n,'u':u,'v':v,'qhat':h,'q':q,'rhat':rh,'remainder':r,'second_digit_test':[h*c,b*rh+u%b],'bound21':str(F(b-2,b)*v)}
    examples=[]
    for b,U,V,n,m in [(10,4100,588,3,1),(2**16,int('7fff800100000000',16),int('800080020005',16),3,1)]:
        stats=Counter();q,r=algorithm_d(U,V,b,n,m,stats)
        assert stats['add_back']>0
        examples.append({'b':b,'U':U,'V':V,'q':q,'r':r,'stats':dict(stats)})
    # Telescope Benford probabilities symbolically; no Monte Carlo.
    benford=[]
    for b in [2,3,4,5,10,16,2**32]:
        k=b//2
        assert all(b//(a+1)==1 for a in [k,b-1])
        if k>1:assert b//k>=2
        benford.append({'b':b,'minimum_leading_digit':k,'probability':'log_b('+str(F(b,k))+')'})
    return {'sampled_cases':count,'trigger_counts':dict(triggers),'missing_upper_bound_witness':witness,'published_add_back_examples':examples,'Benford':benford}


def svoboda_one(v,b,n):
    x=F(v,b**n);a=v//b**(n-1)
    if 2*a<b:x*= (b+1)//(a+1)
    assert F(1,2)<=x<1+F(1,b)
    seq=[x];count=0
    while x<1:
        a=(b*x).__floor__();factor=b*(b+1)//(a+1)
        new=x+F(b*(b-a)//(a+1),b)*x
        assert new==F(factor,b)*x
        x=new;seq.append(x);count+=1
        assert x<1+F(1,b) and count<=3
        if count==1:assert x>=1-F(3,2*b)
    assert x.__floor__()==1 and (b*x).__floor__()%b==0
    return count,seq


def svoboda():
    counts=Counter();first={};total=0
    for b in range(2,31):
        for n in range(1,4):
            for v in range(b**(n-1),b**n):
                k,seq=svoboda_one(v,b,n);counts[k]+=1;total+=1
                first.setdefault(k,{'b':b,'n':n,'v':v,'sequence':list(map(str,seq))})
    rng=random.Random(43128)
    for _ in range(2000):
        b=rng.randrange(2,1001);n=rng.randrange(1,20);v=rng.randrange(b**(n-1),b**n)
        svoboda_one(v,b,n)
    b,a,t=s.symbols('b a t',positive=True)
    f=a*(b+1-a)/(b*(a+1));g=a*(b*(b+1)-a)/(b*b*(a+1))
    assert s.simplify(s.diff(f,a,2)+2*(b+2)/(b*(a+1)**3))==0
    assert s.simplify(s.diff(g,a,2)+2*(b*b+b+1)/(b*b*(a+1)**3))==0
    assert s.simplify(g.subs(a,(b-1)/2)-(1-s.Rational(3,2)/b)-(3*b-1)/(2*b*b*(b+1)))==0
    assert s.simplify(g.subs(a,b-1)-(1-s.Rational(3,2)/b)-(b*b+2*b-2)/(2*b**3))==0
    assert s.simplify((1-s.Rational(3,2)/b)*(1+1/b)**2-1-(b*b-4*b-3)/(2*b**3))==0
    return {'exhaustive_cases':total,'iteration_counts':dict(counts),'first_examples':first,'larger_cases':2000,'symbolic_identities':5}


def aliases_AS():
    rng=random.Random(431030);count=0
    for beta in [64,100,256]:
        B=beta**5
        for n in range(1,9):
            for k in range(20):
                u=[rng.randrange(B) for _ in range(n)];v=[rng.randrange(B) for _ in range(n)]
                if k==0:u=[0]*n;v=[0]*n
                if k==1:u=[B-1]*n;v=[B-1]*n
                for entry in ['A','S']:
                    uu,vv=(v,u) if entry=='S' and value(u,B)<value(v,B) else (u,v)
                    expected=value(uu,B)+value(vv,B) if entry=='A' else value(uu,B)-value(vv,B)
                    for name in ['U','V']:
                        mm=ClassicalMachine(beta,n)
                        mm.symbols['W']=mm.symbols[name]
                        mm.put('U',uu+[0]);mm.put('V',vv+[0])
                        mm.ret=mm.symbols[entry+'_END'];mm.execute(entry)
                        out=[mm.memory[mm.symbols['W']+j].val for j in range(n+(entry=='A'))]
                        assert value(out,B)==expected and all(0<=x<B for x in out);count+=1
    return {'cases':count,'scope':'Programs A/S with W=U or W=V, source operands loaded before store'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resume',action='store_true');args=ap.parse_args()
    if OUT.exists() and not args.resume:raise SystemExit('Use --resume')
    data=json.loads(OUT.read_text()) if OUT.exists() else {'scope':'4.3.1-17--30 supplementary mathematics','blocks':{}}
    for name,fn in [('estimates',estimates),('Svoboda',svoboda),('AS_aliases',aliases_AS)]:
        if name in data['blocks']:continue
        t=time.monotonic();r=fn();r['elapsed_seconds']=time.monotonic()-t;data['blocks'][name]=r
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,'PASS',flush=True)
    print('ALL CHECKPOINTS COMPLETE',flush=True)
if __name__=='__main__':main()
