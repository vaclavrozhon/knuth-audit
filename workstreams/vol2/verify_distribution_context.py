"""Exact finite illustration of the cited rejection/LCG interaction.

This enumerates all possible adjacent pairs, not a claim about the published
2^31-1 table or about one particular stream consuming nonoverlapping pairs.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

m=1024;a=33;c=1
cdf=lambda x:6*x*x-8*x*x*x+3*x*x*x*x
accepted=[]
for x in range(m):
    y=(a*x+c)%m
    accept=4*y*m*m < 27*x*(m-x)**2
    assert accept == (Q(y,m) < Q(27,4)*Q(x,m)*(1-Q(x,m))**2)
    if accept:accepted.append(x)
n=len(accepted)
dplus=max((Q(i+1,n)-cdf(Q(x,m)),x) for i,x in enumerate(accepted))
dminus=max((cdf(Q(x,m))-Q(i,n),x) for i,x in enumerate(accepted))
bounds=[0]+accepted+[m]
gap=max((cdf(Q(v,m))-cdf(Q(u,m)),u,v) for u,v in zip(bounds,bounds[1:]))
result={'modulus':m,'multiplier':a,'increment':c,'pairs_checked':m,
 'accepted':n,'target_cdf':'6x^2-8x^3+3x^4',
 'one_sided_dplus':str(dplus[0]),'one_sided_dminus':str(dminus[0]),
 'interval_discrepancy':str(dplus[0]+dminus[0]),
 'interval_discrepancy_decimal':float(dplus[0]+dminus[0]),
 'largest_empty_target_mass':str(gap[0]),'gap_numerators':[gap[1],gap[2]],
 'scope':'All adjacent pairs, exactly as the small illustration in the primary preprint; no simulation of its large table.'}
Path(__file__).resolve().with_name('results').joinpath('distribution-context.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
