"""The rectangle asymptotic constant in X262(a), p483."""
from pathlib import Path
import json,subprocess
import mpmath as mp

ROOT=Path(__file__).parent
mp.mp.dps=300


def main():
    pell=[1,2]
    for _ in range(2,17):pell.append(2*pell[-1]+pell[-2])
    results=[]
    for m in range(1,5):
        cs=[mp.cos(j*mp.pi/(2*m+1)) for j in range(1,m+1)]
        bs=[mp.sqrt(1+c*c) for c in cs]
        roots=[c+b for c,b in zip(cs,bs)]
        mu=mp.fprod(roots)
        denominator=mp.fprod(2*b for b in bs)
        assert abs(denominator**2-pell[2*m])<mp.mpf('1e-250')
        for n in [10,40,80,160]:
            got=json.loads(subprocess.check_output(['/tmp/knuth-aztec-zdd',str(2*m),str(n),'0'],text=True))
            count=int(got['solutions'])
            product=mp.fprod((r**(n+1)-(-1/r)**(n+1))/(2*b) for r,b in zip(roots,bs))
            assert int(mp.nint(product))==count
            ratio=mp.mpf(count)/mu**(n+1)
            expected=1/mp.sqrt(pell[2*m])
            if n==160:assert abs(ratio/expected-1)<mp.mpf('1e-23')
            results.append(dict(m=m,n=n,count=str(count),printed_a=pell[2*m],
                normalized_count=mp.nstr(ratio,45),correct_coefficient=mp.nstr(expected,45),
                ratio_to_printed_asymptotic=mp.nstr(ratio/pell[2*m],45)))
    out=dict(pell_numbers=pell,checks=results,
             corrected_asymptotic='a_(2m)^(-1/2) * mu_(2m)^(n+1)',
             minimal_counterexample='m=1: a2=5,mu2=phi, but R(2,n) has F_(n+1)~phi^(n+1)/sqrt(5) tilings.')
    (ROOT/'results/rectangle_asymptotic.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
