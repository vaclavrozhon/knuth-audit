"""Check the new proof partition/invariants, not just the previously tested identity."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import product
from collections import Counter
import json
from accuracy_model import Arithmetic
from float_model import power
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/accuracy-drift-proof.json'


def check(b,p,tie):
    a=Arithmetic(b,p,tie);N=b**p;B=N//b
    fs=sorted({B,min(B+1,N-1),(B+N)//2,N-2,N-1}-{0})
    fs=[F for F in fs if B<=F<N];counts=Counter();examples={}
    for U,V,d,sgn in product(fs,fs,range(-1,p+3),[-1,1]):
        u=Q(U);v=sgn*V*power(b,-d);w=a.add(u,v);z=a.sub(w,v);w2=a.add(z,v);z2=a.sub(w2,v)
        if z==u:branch='fixed'
        elif abs(v)>=u:branch='v_dominant'
        else:
            assert not (v<0 and abs(v)>=u/2)
            assert B/Q(b)<=w<=2*N
            r=w-u-v;x=w-v
            if w>=N:
                branch='coarse';assert v>0 and abs(r)<=Q(b,2) and B<=x<=N-1+Q(b,2)
                assert B<=z<=N and z.denominator==1
                if z==N:assert w2==w
                elif w2!=w:
                    assert w==N and z-x==Q(-1,2) and w2==N-1 and B<z<N and z%2==1
            elif w>=B and x>=B:
                branch='same';assert abs(r)==Q(1,2) and z-u==2*r
                if w>B:assert w2==w
                else:assert r==Q(-1,2) and w2==B-Q(1,2) and w2-v==z
            elif w>=B:
                branch='back_lower';assert u==B and v>0 and r<0
                j=w-B;t=v-j;k=(B-z)*b;delta=k/Q(b)-t
                assert j.denominator==1 and k.denominator==1 and 1<=k<=b//2 and abs(delta)<=Q(1,2*b)
                if w>B:assert w2==w
                elif w2!=w:
                    assert delta==Q(1,2*b) and w2==B-Q(1,b) and k%2==1
                    if z==B/Q(b):assert b==2 and p==1 and v==Q(1,4)
            else:
                branch='fine';assert v<0 and abs(v)<u/2 and abs(r)<=Q(1,2*b)
                assert u==B and r==Q(-1,2*b) and z==B-Q(1,b)
                k=(B-w)*b;assert k.denominator==1 and k%2==1
                if w>B/Q(b):assert w2==w
                else:assert b==2 and p==1 and v==Q(-1,4) and w2==Q(1,4)
        exception=(b,p,tie)==(2,1,'odd') and v==u/4
        assert (z2!=z)==exception
        counts[branch]+=1
        examples.setdefault(branch,list(map(str,[u,v,w,z,w2,z2])))
    return dict(cases=sum(counts.values()),branches=counts,examples=examples)


if __name__=='__main__':
    out=json.loads(OUT.read_text()) if OUT.exists() else {}
    for b,p in product(range(2,11),[1,2]):
        for tie in ['even','odd'] if b%2==0 else ['book']:
            key=f'b{b}_p{p}_{tie}'
            if key not in out:
                out[key]=check(b,p,tie);OUT.write_text(json.dumps(out,indent=2)+'\n');print('PASS',key,flush=True)
