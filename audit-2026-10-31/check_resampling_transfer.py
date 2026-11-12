"""Independent two-state transfer calculation for Algorithm M's Case 2."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as s

z=s.Symbol('z');K=s.QQ.frac_field(z);Z=K.from_sympy(z)
T=[[K.one/2,K.one/2],[(4+Z)/(2*(4-Z)),Z/(2*(4-Z))]]
row=[K.one/2,K.one/2];previous=[K.one,K.one]
base=json.loads(Path('results/resampling.json').read_text())
moments={r['n']:r for r in base['moment_rows'] if r['case']==2}
means=[Q(0),Q(0)];factorial_seconds=[Q(0),Q(0)]
for n in range(1,41):
    if n>1:
        row=[sum(row[i]*T[i][j] for i in range(2)) for j in range(2)]
        G=(2*previous[-1]+previous[-2])/(4-Z);previous.append(G)
        mean=(1+2*means[-1]+means[-2])/3;means.append(mean)
        second=(2*mean+2*factorial_seconds[-1]+factorial_seconds[-2])/3;factorial_seconds.append(second)
    else:G=K.one
    assert sum(row)==G
    expected=Q(n-1,4)+Q(1,16)*(1-Q(-1,3)**(n-1))
    assert means[n]==expected
    if n in moments:
        assert means[n]==Q(moments[n]['mean'])
        assert factorial_seconds[n]+means[n]-means[n]**2==Q(moments[n]['variance'])
    if n==7:assert G==K.from_sympy((1088-400*z+42*z*z-z**3)/(4-z)**6)
result=dict(transfer_sizes_checked=40,independent_moment_sizes_checked=9,
            transfer_matrix=[['1/2','1/2'],['(4+z)/(2(4-z))','z/(2(4-z))']],
            pgf_recurrence='(4-z)G_n=2G_(n-1)+G_(n-2); G_0=G_1=1',
            mean='(n-1)/4 + (1-(-1/3)^(n-1))/16')
Path('results/resampling_transfer.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
