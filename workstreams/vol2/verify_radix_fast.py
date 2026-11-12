#!/usr/bin/env python3
"""Exact checks of 4.4-14 and a finite-state linear array for 4.4-16."""
from pathlib import Path
import argparse,json,random,time,sys

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/radix-fast.json'
sys.set_int_max_str_digits(0)


def input_dc(ds):
    if len(ds)==1:return ds[0],10
    k=len(ds)//2;high,p=input_dc(ds[:-k]);low,q=input_dc(ds[-k:])
    return high*q+low,p*q


def output_dc(u,n,powers):
    assert 0<=u<powers[n]
    if n==1:return [u]
    k=n//2;q,r=divmod(u,powers[k])
    return output_dc(q,n-k,powers)+output_dc(r,k,powers)


def divide_conquer_block():
    rng=random.Random(4414);cases=0;maxdigits=0
    for n in list(range(1,81))+[127,128,129,255,256,257,511,512,513,1024,2048,4096,8192]:
        trials=12 if n<=80 else 3
        powers={1:10}
        def power(k):
            if k not in powers:
                a=k//2;powers[k]=power(a)*power(k-a)
            return powers[k]
        power(n)
        for i in range(trials):
            ds=[0]*n if i==0 else [9]*n if i==1 else [rng.randrange(10) for _ in range(n)]
            v,p=input_dc(ds);text=''.join(map(str,ds))
            assert p==10**n and v==int(text)
            assert output_dc(v,n,powers)==ds
            cases+=1;maxdigits=max(maxdigits,n)
    return {'bidirectional_cases':cases,'max_decimal_digits':maxdigits}


def local_step(r,done,right_in,left_in,right_boundary,pending_done):
    """Only local state and the two incoming nearest-neighbour symbols."""
    right_out=None;left_out=left_in;new_done=done;next_pending=False
    if pending_done:
        assert left_in is None;left_out='DONE'
    if isinstance(right_in,int):
        assert not done and right_in in range(10)
        q,r=divmod(10*r+right_in,2);right_out=q
    elif right_in=='END':
        assert not done and left_in is None and not pending_done
        left_out=r;new_done=True
        if right_boundary:next_pending=True
        else:right_out='END'
    else:assert right_in is None
    return r,new_done,right_out,left_out,next_pending


def array_convert(ds):
    n=len(ds);L=4*n
    remainders=[0]*L;done=[False]*L;pending=[False]*L
    right=[None]*L;left=[None]*L
    result=[];times=[];digit_visits=0
    for t in range(n+2*L):
        right[0]=ds[t] if t<n else 'END' if t==n else None
        new_right=[None]*L;new_left=[None]*L
        for j in range(L):
            if isinstance(right[j],int):digit_visits+=1
            r,d,ro,lo,p=local_step(remainders[j],done[j],right[j],left[j],j==L-1,pending[j])
            remainders[j],done[j],pending[j]=r,d,p
            if j<L-1:new_right[j+1]=ro
            if j:new_left[j-1]=lo
            elif isinstance(lo,int):result.append(lo);times.append(t)
            elif lo=='DONE':
                assert t==n+2*L-1 and len(result)==L
            else:assert lo is None
        right,left=new_right,new_left
    assert all(done) and not any(pending)
    assert len(result)==L and times==list(range(n,n+2*L,2))
    assert result==remainders and digit_visits==n*L
    return result,n+2*L,digit_visits


def array_block():
    # All twenty arithmetic transitions of the finite transducer.
    for r in range(2):
        for d in range(10):
            rr,done,q,left,p=local_step(r,False,d,None,False,False)
            assert 10*r+d==2*q+rr and q in range(10) and rr in range(2)
    inputs=[list(map(int,str(u))) for u in range(1001)]
    rng=random.Random(4416)
    for n in [1,2,3,4,8,16,32,64,128,256]:
        inputs += [[0]*n,[9]*n,[1]+[0]*(n-1)]
        inputs += [[rng.randrange(10) for _ in range(n)] for _ in range(3)]
    cases=0;maxdigits=0;maxticks=0;totalvisits=0
    for ds in inputs:
        out,ticks,visits=array_convert(ds)
        v=int(''.join(map(str,ds)))
        assert sum(d<<j for j,d in enumerate(out))==v
        assert out==[(v>>j)&1 for j in range(4*len(ds))]
        assert ticks==9*len(ds)
        cases+=1;maxdigits=max(maxdigits,len(ds));maxticks=max(maxticks,ticks);totalvisits+=visits
    return {'cases':cases,'max_decimal_digits':maxdigits,'max_ticks':maxticks,
            'total_local_digit_transitions':totalvisits,'arithmetic_transition_table_cases':20}


def main():
    p=argparse.ArgumentParser();p.add_argument('--resume',action='store_true');args=p.parse_args()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'scope':'4.4-14,16','blocks':{}}
    for name,fun in [('divide_conquer',divide_conquer_block),('array',array_block)]:
        if name in data['blocks']:continue
        t=time.monotonic();got=fun();data['blocks'][name]={'status':'passed','seconds':time.monotonic()-t,'result':got}
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps({'checkpoint':name,**data['blocks'][name]}),flush=True)


if __name__=='__main__':main()
