"""Exact independent enumerations/recurrence/Lambert coefficients; no asymptotic fit proof."""
from pathlib import Path
from collections import Counter
from math import comb,sqrt,pi
import json,sys
sys.set_int_max_str_digits(0)
from tree_shapes import shapes,stack_height
B=Path(__file__).resolve().parent

def lambert(n):
    d=[0]*(n+2)
    for j in range(1,n+2):
        for k in range(j,n+2,j):d[k]+=1
    cc=[1]
    for k in range(1,n+2):cc.append(cc[-1]*(2*n-k+1)//k)
    def c(k):return cc[k] if 0<=k<len(cc) else 0
    catalan=cc[n]//(n+1)
    total=sum(d[j]*(c(n+1-j)-2*c(n-j)+c(n-1-j)) for j in range(1,n+2))-catalan
    return total,catalan

N=30
g=[[1]+[0]*N]
for k in range(1,N+1):
    row=[1]
    for n in range(1,N+1):row.append(sum(g[-1][i]*row[n-1-i] for i in range(n)))
    g.append(row)
for n in range(1,N+1):
    sn,cn=lambert(n)
    assert sn==sum(cn-g[k][n] for k in range(n))
    assert g[n][n]==cn
    if n<=8:
        counts=Counter(stack_height(t) for t in shapes(n))
        for k in range(n+1):assert g[k][n]==sum(c for h,c in counts.items() if h<=k)
        assert sn==sum(h*c for h,c in counts.items())
rows=[]
for n in [10,100,1000,10000]:
    sn,cn=lambert(n);value=sn/cn
    original=sqrt(pi*n)-1.5+11/24*sqrt(pi/n)
    erratum=sqrt(pi*n)-1.5-13/24*sqrt(pi/n)+1/(2*n)
    rows.append({'n':n,'exact_numerator':str(sn),'exact_denominator':str(cn),'mean':value,'original_expansion':original,'erratum_expansion':erratum,'normalized_coefficient':(value-sqrt(pi*n)+1.5)*sqrt(n/pi),'original_error_times_n_3_over_2':(value-original)*n**1.5})
out={'enumerated_n_le':8,'recurrence_vs_lambert_n_le':N,'rows':rows}
(B/'results/height.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({**out,'rows':[{k:v for k,v in r.items() if not k.startswith('exact_')} for r in rows]},indent=2))
