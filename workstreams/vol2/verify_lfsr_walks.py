"""Exact finite-state, linear-form, and generating-function checks for31–35."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from math import comb
from pathlib import Path
import json
import sys
import numpy as np
import mpmath as mp

ROOT=Path(__file__).resolve().parent
DEST=ROOT/'results/lfsr-walks.json'


def convolution(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c


def forms(k,l,length):
    a=[1<<i for i in range(k)]
    for i in range(k,length):a.append(a[i-l]^a[i-k])
    return a[:length]


def component_polynomials(k,l,length):
    fs=forms(k,l,length);parent=list(range(k))
    def find(i):
        while parent[i]!=i:parent[i]=parent[parent[i]];i=parent[i]
        return i
    for f in fs:
        bits=[i for i in range(k) if f>>i&1]
        for i in bits[1:]:parent[find(i)]=find(bits[0])
    groups={}
    for i in range(k):groups.setdefault(find(i),[]).append(i)
    out=[]
    for indices in groups.values():
        groupmask=sum(1<<i for i in indices)
        selected=[f for f in fs if f&groupmask]
        assert all(f&groupmask==f for f in selected)
        assert len(indices)<=16
        local=[sum(((f>>i)&1)<<j for j,i in enumerate(indices)) for f in selected]
        hist=Counter(sum((f&s).bit_count()%2 for f in local) for s in range(1<<len(indices)))
        out.append(dict(inputs=len(indices),outputs=len(local),coefficients=[hist[j] for j in range(max(hist)+1)]))
    return out


def distribution(k,l):
    m=k-2*l
    return convolution([comb(m,a) for a in range(m+1)],
                       [comb(l,b//2)*3**(b//2) if b%2==0 else 0 for b in range(2*l+1)])


def short_walks():
    cases=words=0
    for k in range(3,11):
        for l in range(1,(k+1)//2):
            if k<=2*l:continue
            hist=Counter()
            # Direct recurrence over actual bits, independent of polynomial model.
            for seed in range(1<<k):
                y=[seed>>j&1 for j in range(k)]
                for j in range(k,k+l):y.append(y[j-l]^y[j-k])
                hist[sum(y)]+=1;words+=1
            poly=distribution(k,l)
            assert [hist[j] for j in range(len(poly))]==poly
            assert sum(hist.values())==1<<k;cases+=1
    poly=distribution(55,24);right=sum(poly[40:]);assert right==18509401282464000
    p=Q(right,2**55-1)
    distinct={};bylength={}
    for length in range(79,104):
        comps=component_polynomials(55,24,length)
        for c in comps:distinct[tuple(c['coefficients'])]=c
        if length in (79,86,87,94,101,103):bylength[str(length)]=comps
    expected=[[1,0,3],[1,0,2,4,1],[1,0,2,5,5,10,8,1],
              [1,0,2,7,7,15,25,29,28,13,1]]
    assert all(tuple(v) in distinct for v in expected)
    return dict(small_models=cases,initial_states=words,right79_numerator=right,
                right79_probability=str(p),right79_decimal=str(mp.mpf(p.numerator)/p.denominator),
                component_factors=list(distinct.values()),selected_decompositions=bylength,
                auxiliary_counterexample33=dict(printed_coefficient=str(Q(sum(poly[:40]),2**55)),
                                                actual_including_zero=str(Q(right,2**55))))


def period_bits(k,mask):
    state=1;initial=state;bits=[]
    for _ in range((1<<k)-1):
        bits.append(state&1)
        bit=(state&mask).bit_count()%2
        state=(state>>1)|(bit<<(k-1))
        if state==initial:return bits
    return bits if state==initial else []


def all_moments():
    rows=[];models=checks=0
    for k in range(2,9):
        N=(1<<k)-1
        for mask in range(1,1<<k,2):
            bits=period_bits(k,mask)
            if len(bits)!=N:continue
            y=bits+bits[:k]
            tails=[sum(y[i+j]<<(j-1) for j in range(1,k)) for i in range(N)]
            # Count equal projected states, the B definition in the exercise.
            ends=[0]*N
            seen={}
            for j in range(1,N):
                ends[j]=seen.get(tails[j],0)
                seen[tails[j]]=ends[j]+1
            z=2*np.array(bits,dtype=np.int64)-1;s=np.zeros(N,dtype=np.int64)
            B=0;paircount=0
            for m in range(1,N+1):
                s+=np.roll(z,-(m-1))
                paircount+=ends[m-1];B+=paircount
                # B_m weights a pair ending at j by m-j; add new pairs with weight1.
                a=int(s.sum());b=int((s*s).sum());c=int((s*s*s).sum())
                assert a==m
                assert b==m*N-m*(m-1)
                assert c==m**3-6*B*(N+1)
                checks+=1
            models+=1;rows.append(dict(k=k,mask=mask,period=N))
    # Large55-bit B: projected-state model and independent linear-form equality.
    fs=forms(55,24,165);bits=[int(bool(f&1)) for f in fs]
    tails=[sum(bits[i+j]<<(j-1) for j in range(1,55)) for i in range(111)]
    pairs=[(i,j) for j in range(1,111) for i in range(1,j) if tails[i]==tails[j]]
    algebra=[(i,j) for j in range(1,111) for i in range(1,j) if fs[0]^fs[i]^fs[j]==0]
    # Dual forms need not equal field powers; a zero recurrence is phase-independent.
    assert pairs==algebra==[(31,55),(62,110)]
    B=sum(79-j for i,j in pairs if j<79);assert B==24
    return dict(primitive_recurrences=models,window_moment_checks=checks,rows=rows,
                lag55_pairs_through110=pairs,B79=B,
                third79=str(Q(79**3-6*24*2**55,2**55-1)),
                printed_third_moment_counterexample=dict(k=2,m=1,N=3,actual='1/3',printed='1'))


def curve():
    k=11;mask=1|(1<<9);bits=period_bits(k,mask);N=len(bits);assert N==2047
    z=2*np.array(bits,dtype=np.int64)-1;s=np.zeros(N,dtype=np.int64);rows=[]
    for m in range(1,N+1):
        s+=np.roll(z,-(m-1))
        rows.append(dict(m=m,right=int((s>0).sum()),tie=int((s==0).sum())))
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,ax=plt.subplots(figsize=(10,3.2))
    odd=[r for r in rows if r['m']%2]
    ax.plot([r['m'] for r in odd],[r['right']/N for r in odd],lw=.7)
    ax.axhline(.5,color='gray',lw=.6);ax.set(xlabel='Walk length (odd lengths shown)',ylabel='Probability of more ones',xlim=(0,N),ylim=(.3,.7))
    fig.tight_layout();fig.savefig(ROOT/'results/lfsr-walk-curve.svg');fig.savefig(ROOT/'results/lfsr-walk-curve.png',dpi=160);plt.close(fig)
    svg=ROOT/'results/lfsr-walk-curve.svg'
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    return dict(k=k,lag=2,period=N,at445=rows[444],rows=rows,
                scope='Exact all starting phases; plot uses odd lengths to avoid tie-parity oscillations.')


def counterexample32():
    e=Q(1,10);values=[-1-2*e*e,e-2*e*e,1-2*e];probs=[Q(1,2)-e,e,Q(1,2)]
    assert sum(x*p for x,p in zip(values,probs))==0
    positive=sum(p for x,p in zip(values,probs) if x>0)
    double=sum(p*q for x,p in zip(values,probs) for y,q in zip(values,probs) if x+y>0)
    assert positive==Q(3,5) and double==Q(9,25)
    a,b=2,3;vs=[-b,a];ps=[Q(a,a+b),Q(b,a+b)]
    assert sum(x*p for x,p in zip(vs,ps))==0
    assert sum(p*q for x,p in zip(vs,ps) for y,q in zip(vs,ps) if x+y>0)==Q(9,25)
    return dict(original_epsilon=str(e),original_values=list(map(str,values)),
                one_round_positive=str(positive),two_round_positive=str(double),
                corrected2005_values=vs,corrected2005_probabilities=list(map(str,ps)))


def asymptotic33():
    rows=[]
    for k in (20,50,100,200,500,1000):
        for l in sorted({1,k//5,(k-1)//2}):
            m=k-2*l;L=k+l
            choose=[comb(m,a) for a in range(m+1)];prefix=[0]
            for c in choose:prefix.append(prefix[-1]+c)
            numerator=tie=0
            for b in range(l+1):
                weight=comb(l,b)*3**b;threshold=L//2-2*b
                numerator+=weight*((1<<m)-prefix[min(m+1,max(0,threshold+1))])
                if L%2==0 and 0<=L//2-2*b<=m:tie+=weight*choose[L//2-2*b]
            p=mp.mpf(2*numerator+tie)/(2*(2**k-1))
            estimate=mp.mpf('.5')+l/(mp.sqrt(2*mp.pi)*L**mp.mpf('1.5'))
            rows.append(dict(k=k,l=l,L=L,probability_with_half_ties=mp.nstr(p,25),
                             leading_formula=mp.nstr(estimate,25),
                             remainder_times_L_to_3_over2=mp.nstr((p-estimate)*L**mp.mpf('1.5'),12),
                             tie_probability=mp.nstr(mp.mpf(tie)/(2**k-1),25)))
    return dict(rows=rows,scope='Exact binomial integer sums; uniform asymptotic proof is in the note. No primitivity assumed for these uniform-seed models.')


def auxiliary():
    poly=distribution(55,24);poly[0]-=1;N=2**55-1
    moments=[Q(sum(count*(2*j-79)**r for j,count in enumerate(poly)),N) for r in (1,2,3)]
    assert moments==[Q(79,N),Q(79*N-79*78,N),Q(79**3-144*(N+1),N)]
    p=distribution(4,1)
    assert Q(sum(p[:3]),16)==Q(7,16) and Q(sum(p[3:]),16)==Q(9,16)
    import sympy as S
    x,a,b=S.symbols('x a b')
    g=a*S.log((1+S.exp(x))/2)+b*S.log((1+3*S.exp(2*x))/4)-(a+3*b-1)*x/2
    assert S.simplify(S.diff(g,x).subs(x,0))==S.Rational(1,2)
    t=S.Symbol('t',real=True);integrals=[]
    for k in range(4):
        v=(-1)**k*S.integrate(S.exp(-t*t/2)*t**(2*k),(t,-S.oo,S.oo))/(2*S.pi)
        expected=(-1)**k*S.factorial2(2*k-1)/S.sqrt(2*S.pi)
        assert S.simplify(v-expected)==0
        integrals.append(str(v))
    return dict(moments79_from_weight_polynomial=list(map(str,moments)),
                coefficient33_counterexample=dict(k=4,l=1,printed_lower_tail='7/16',desired_upper_tail='9/16'),
                g_linear_coefficient='1/2',normalized_gaussian_integrals=integrals)


def main():
    mp.mp.dps=60
    out=json.loads(DEST.read_text()) if '--resume' in sys.argv and DEST.exists() else {}
    for name,fn in [('short',short_walks),('moments',all_moments),('curve',curve),
                    ('counterexample32',counterexample32),('asymptotic33',asymptotic33),('auxiliary',auxiliary)]:
        if name in out:continue
        print('START',name,flush=True);out[name]=fn();DEST.write_text(json.dumps(out,indent=2)+'\n');print('PASS',name,flush=True)
    print('ALL BLOCKS COMPLETE',flush=True)


if __name__=='__main__':main()
