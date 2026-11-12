"""Every endpoint-pair combination, compared with exact interior probes."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from interval_model import Intervals,contains,valid,neg,key
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/intervals.json'


def endpoint_sweep(b,p):
    a=Intervals(b,p);ints=[I for I in product(a.ends,repeat=2) if valid(I)]
    fs=a.finite;positive=[x for x in fs if x>0];small=min(positive)/1000;big=max(positive)*1000
    probes=set(fs+[small,-small,big,-big]+[(x+y)/2 for x,y in zip(fs,fs[1:])]);probes=sorted(probes)
    ranges={I:(min(x for x in probes if contains(I,x)),max(x for x in probes if contains(I,x))) for I in ints}
    count=divisions=zero_rejections=checks=0
    for I,J in product(ints,repeat=2):
        for name,scalar in [('add',lambda x,y:x+y),('sub',lambda x,y:x-y),('mul',lambda x,y:x*y),('div',lambda x,y:x/y)]:
            if name=='div' and contains(J,0):
                try:a.div(I,J)
                except ZeroDivisionError:zero_rejections+=1
                else:raise AssertionError('zero divisor accepted')
                continue
            ans=getattr(a,name)(I,J)
            assert valid(ans),(name,b,p,I,J,ans)
            # Exact scalar operations use neither directed rounding nor endpoint rules.
            for x,y in product(ranges[I],ranges[J]):
                assert contains(ans,scalar(x,y)),(name,b,p,I,J,ans,x,y,scalar(x,y))
                checks+=1
            count+=1;divisions+=name=='div'
    zero=('-0','+0');allreals=('-inf','+inf')
    assert a.mul(zero,allreals)==zero
    assert a.div(zero,('+0','+inf'))==zero
    assert a.mul(('+0',Q(1)),('-inf','-0'))==('-inf','-0')
    return dict(intervals=len(ints),operations=count,scalar_extreme_checks=checks,defined_divisions=divisions,zero_divisor_rejections=zero_rejections,probe_values=list(map(str,probes)),scope='All endpoint pairs; exact finite interior/extreme probes. Unbounded-real soundness proved separately.')


def physical_intervals():
    Nlo=Q(60221407)*10**16;Nhi=Q(60221408)*10**16
    hlo=Q(66260701,10**41);hhi=Q(66260702,10**41)
    # Direct fixed-grid outward rounding; no gigantic format enumeration.
    lower_sum=(Nlo+hlo)//10**16
    upper_sum=-(-(Nhi+hhi)//10**16)
    lower_prod=(Nlo*hlo)//Q(1,10**17)
    upper_prod=-(-(Nhi*hhi)//Q(1,10**17))
    assert (lower_sum,upper_sum)==(60221407,60221409)
    assert (lower_prod,upper_prod)==(39903126,39903128)
    assert Nhi+hhi>Nhi
    return dict(sum_outward_fractions=[lower_sum,upper_sum],sum_exponent=24,printed_upper_fraction=60221408,exact_excess_above_printed_upper=str(hhi),product_outward_fractions=[lower_prod,upper_prod],product_exponent=-9,scope='2020 erratum interval arithmetic; not a claim that the printed interval misses the exact fixed SI constants.')


if __name__=='__main__':
    out=json.loads(OUT.read_text()) if OUT.exists() else {}
    def run(key,fn):
        if key not in out:
            out[key]=fn();OUT.write_text(json.dumps(out,indent=2)+'\n');print('PASS',key,flush=True)
    run('physical_intervals',physical_intervals)
    for b,p in [(2,2),(3,1)]:run(f'endpoint_b{b}_p{p}',lambda b=b,p=p:endpoint_sweep(b,p))
