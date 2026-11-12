"""TAOCP 3.3.2 I: collision recurrence, certified CDFs, floating sentinel."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import sys
import time

ROOT=Path(__file__).resolve().parent
DEST=ROOT/'results/collision-test.json'


def exact_recurrence(m,n):
    a=[Q(0)]*(n+1);a[1]=Q(1)
    for i in range(1,n):
        for j in range(i+1,0,-1):
            a[j]=Q(j,m)*a[j]+(1+Q(1,m)-Q(j,m))*a[j-1]
    return a


def small_checks():
    cases=0;rows=[]
    for m in range(1,7):
        for n in range(1,8):
            hist=Counter(len(set(u)) for u in product(range(m),repeat=n))
            a=exact_recurrence(m,n)
            assert a==[Q(hist[j],m**n) for j in range(n+1)]
            assert sum(a)==1
            mean=sum((n-j)*a[j] for j in range(n+1))
            assert mean==n-m+m*(1-Q(1,m))**n
            cases+=m**n;rows.append(dict(m=m,n=n,sequences=m**n))
    return dict(sequences=cases,models=rows)


def algorithm_s_float(m,n,cutoff=1e-20):
    a=[0.0]*(n+1);a[1]=1.0;j0=j1=1;maxwidth=0;pruned=0.0
    for _ in range(n-1):
        j1+=1
        for j in range(j1,j0-1,-1):
            a[j]=(j/m)*a[j]+((1+1/m)-(j/m))*a[j-1]
            if a[j]<cutoff:
                pruned+=a[j];a[j]=0.0
                if j==j1:j1-=1
                elif j==j0:j0+=1
        maxwidth=max(maxwidth,j1-j0)
    thresholds=[.01,.05,.25,.50,.75,.95,.99,1.00]
    cumulative=0.0;t=0;out=[];trace=[]
    for j in range(j0,j1+1):
        cumulative+=a[j]
        if cumulative>thresholds[t]:
            out.append(dict(collisions=n-j-1,cdf=1-cumulative))
            while cumulative>thresholds[t]:
                t+=1
                if t==len(thresholds):
                    return dict(m=m,n=n,output=out,status='sentinel_overrun',
                                sum=cumulative,support=[j0,j1],maximum_width=maxwidth)
            if t==len(thresholds)-1:
                break
    return dict(m=m,n=n,output=out,status='completed' if t==7 else 'exhausted_support',
                sum=sum(a),support=[j0,j1],maximum_width=maxwidth,pruned_mass=pruned)


def rounded_binary64(x):
    """Exact rational round-to-nearest-even for nonzero normal binary64 values."""
    if not x:return Q(0)
    sign=-1 if x<0 else 1;x=abs(x)
    e=x.numerator.bit_length()-x.denominator.bit_length()
    def pow2(e):return Q(2**e) if e>=0 else Q(1,2**(-e))
    if x<pow2(e):e-=1
    step=pow2(e-52);y=x/step;k,r=divmod(y.numerator,y.denominator)
    if 2*r>y.denominator or (2*r==y.denominator and k%2):k+=1
    return sign*k*step


def sentinel_check():
    r=rounded_binary64
    tenth=r(Q(1,10));two_tenths=r(Q(2,10))
    occupied2=r(r(1+tenth)-two_tenths)
    total=r(tenth+occupied2)
    assert total==1+Q(1,2**52)
    assert Q.from_float((1+1/10)-2/10)==occupied2
    assert Q.from_float(1/10+((1+1/10)-2/10))==total
    actual=algorithm_s_float(10,2)
    assert actual['status']=='sentinel_overrun'
    assert actual['output'][-1]['cdf']==-2**-52
    return dict(implementation=actual,exact_rounded_tenth=str(tenth),
                exact_rounded_two_occupied=str(occupied2),
                exact_rounded_sum=str(total),rounding='binary64, nearest even, each printed operation')


def sparse_sentinel_check():
    """Additional sparse model; retain the already completed m=10 check."""
    m=10018;r=rounded_binary64
    one=r(Q(1,m));two=r(r(1+one)-r(Q(2,m)));total=r(one+two)
    assert total==1+Q(1,2**52)
    assert Q.from_float((1+1/m)-2/m)==two
    actual=algorithm_s_float(m,2)
    assert actual['status']=='sentinel_overrun'
    assert actual['output'][-1]['cdf']==-2**-52
    return dict(implementation=actual,exact_one_occupied=str(one),
                exact_two_occupied=str(two),exact_sum=str(total),
                ratio_m_over_n=m//2,rounding='binary64, nearest even, each printed operation')


def certified_table():
    m=2**20;n=2**14;cutpoints=[101,108,119,126,134,145,153]
    cap=max(cutpoints);precision=160;scale=1<<precision
    a=[scale]+[0]*cap
    for i in range(1,n):
        a=[((m-i+c)*a[c]+((i-c+1)*a[c-1] if c else 0))//m
           for c in range(cap+1)]
    # Nonnegative substochastic recurrence in collision count. Rounding each
    # of cap+1 cells down loses at most (cap+1)/scale in l1 per step.
    error=Q((n-1)*(cap+1),scale)
    rows=[]
    printed=['.009','.043','.244','.476','.742','.946','.989']
    for c,display in zip(cutpoints,printed):
        lo=Q(sum(a[:c+1]),scale);hi=lo+error
        assert Q(display)-Q(1,2000)<lo<=hi<Q(display)+Q(1,2000)
        rows.append(dict(c=c,lower=str(lo),upper=str(hi),decimal=float(lo),printed=display))
    direct=algorithm_s_float(m,n)
    assert direct['status']=='completed'
    ordered=list(reversed(direct['output']))
    assert [row['collisions'] for row in ordered]==cutpoints
    for row,cert in zip(ordered,rows):assert abs(row['cdf']-cert['decimal'])<1e-9
    # Alternating binomial sum for expected collisions; n/m<1 makes terms
    # decrease, so adjacent partial sums enclose the exact mean.
    term=Q(n*(n-1),2*m);partial=term
    for k in range(3,11):
        term=-term*Q(n-k+1,k*m);partial+=term
    nxt=-term*Q(n-10,11*m)
    bounds=sorted([partial,partial+nxt])
    assert Q(127325,1000)<bounds[0]<bounds[1]<Q(127335,1000)
    return dict(m=m,n=n,precision_bits=precision,total_rounding_bound=str(error),
                cdfs=rows,algorithm_s=direct,mean_interval=list(map(str,bounds)),
                mean_decimal=float(partial))


def width_experiment(table):
    rows=[]
    for n in [256,1024,4096,16384,65536]:
        if n==16384:
            result=table['algorithm_s']
        else:
            result=algorithm_s_float(64*n,n)
        rows.append({key:result[key] for key in ['n','m','support','maximum_width','status','sum']})
    return dict(cutoff='1e-20',ratio_m_over_n=64,rows=rows,
                limitation='Finite precision regime only; not an asymptotic proof for fixed cutoff as n tends to infinity.')


def main():
    out=json.loads(DEST.read_text()) if '--resume' in sys.argv and DEST.exists() else {}
    for name,fn in [('small',small_checks),('sentinel',sentinel_check),('table',certified_table),
                    ('width',lambda:width_experiment(out['table'])),
                    ('sparse_sentinel',sparse_sentinel_check)]:
        if name in out:continue
        print('START',name,flush=True);out[name]=fn()
        DEST.write_text(json.dumps(out,indent=2)+'\n');print('PASS',name,flush=True)
    print('ALL BLOCKS COMPLETE',flush=True)


if __name__=='__main__':main()
