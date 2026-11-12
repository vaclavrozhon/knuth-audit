"""Independent reconstruction of the apparent sign reversal in figure4 data."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
import mpmath as mp
from reproduce_general_test_figures import PARAMS,stream,transformed_maxima
from verify_ks import statistics,sup_at_knots,probability,mm
ROOT=Path(__file__).resolve().parent
mp.mp.dps=70

def affine_power(x,a,c,m,n):
    aa,cc=1,0
    while n:
        if n&1:aa,cc=(a*aa)%m,(a*cc+c)%m
        a,c=(a*a)%m,((a+1)*c)%m;n>>=1
    return (aa*x+cc)%m

def main():
    out=[]
    for name in ['B','F']:
        x,a,c,m=PARAMS[name];raw=stream(PARAMS[name],1001)
        assert all(y==affine_power(x,a,c,m,j) for j,y in enumerate(raw))
        if name=='F':assert all(y==(x+j*(2**18*x+1)+comb(j,2)*2**18)%m for j,y in enumerate(raw))
        for offset in [0,1]:
            data=transformed_maxima(raw[offset:offset+1000],m,5)
            assert statistics(data)==sup_at_knots(data)
            groups=[data[j:j+10] for j in range(0,200,10)]
            values=[]
            for g in groups:
                d=statistics(g);assert d==sup_at_knots(g)
                values.append(d[1])
            cdf=[probability(10,10*d,False) for d in values]
            assert all(p==probability(10,10*d) for d,p in zip(values,cdf))
            result=statistics(cdf);assert result==sup_at_knots(cdf)
            out.append(dict(generator=name,offset=offset,outer_based_on_KS10minus=[mp.nstr(mm(z)*mp.sqrt(20),30) for z in result],inner_minus_unscaled=[str(d) for d in values],transformed_maxima=[str(d) for d in data]))
            print(name,offset,out[-1]['outer_based_on_KS10minus'],flush=True)
            (ROOT/'results/ks-figure-signs.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
