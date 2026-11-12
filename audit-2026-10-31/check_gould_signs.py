"""Recompute the finite residual sign pattern in answer 190.

Bell and Gould triangles use exact integers. The transcendental constant is
evaluated independently at 1000 and 1200 decimal digits; this is a numerical
stability check, not a certified interval proof of every sign.
"""
from pathlib import Path
from itertools import groupby
import json
import mpmath as mp


def main():
    bell=[1];gould=None;selected=[]
    for n in range(1,4101):
        new=[bell[-1]]
        for v in bell:
            new.append(new[-1]+v)
        bell=new
        if n==1:
            gould=[0]
        elif n==2:
            gould=[1,1]
        else:
            new=[0]*n;new[-1]=gould[0]
            for k in range(n-2,-1,-1):
                new[k]=gould[k]+new[k+1]
            gould=new
        if n>=4000:
            selected.append((n,bell[0],gould[0]))
    sequences=[];log_errors=[]
    for precision in (1000,1200):
        with mp.workdps(precision):
            g=mp.e*mp.e1(1)
            residuals=[mp.mpf(a)/b-g for _,b,a in selected]
            assert all(residuals)
            sequences.append(['+' if r>0 else '-' for r in residuals])
            log_errors.append([float(mp.log10(abs(r))) for r in residuals])
    assert sequences[0]==sequences[1]
    assert max(abs(a-b) for a,b in zip(*log_errors))<1e-10
    runs=[(sign,len(list(group))) for sign,group in groupby(sequences[1])]
    printed=[('+',2),('-',4),('+',4),('-',5),('+',4),('-',4),('+',5),('-',4),
             ('+',4),('-',5),('+',4),('-',4),('+',4),('-',5),('+',4),('-',4),
             ('+',5),('-',4),('+',4),('-',5),('+',4),('-',4),('+',4),('-',5)]
    assert sum(k for _,k in printed)==101
    assert runs==printed,(runs,printed)
    report={'range':[4000,4100],'precision_digits':[1000,1200],
            'runs':runs,'matches_printed_pattern':True,
            'log10_relative_residual_min':min(log_errors[1]),
            'log10_relative_residual_max':max(log_errors[1]),
            'scope':'Exact Bell/Gould integers and stable high-precision signs for the stated 101 values. No proof of the open asymptotic sign pattern.'}
    (Path(__file__).parent/'results/gould_signs.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
