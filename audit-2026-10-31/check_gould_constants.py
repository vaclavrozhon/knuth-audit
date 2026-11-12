"""Independent integral and generating-function checks for exercises 189-192."""
from pathlib import Path
import json
import mpmath as mp


def main():
    mp.mp.dps=60
    g=mp.quad(lambda x:mp.exp(-x)/(1+x),[0,1,4,16,64,mp.inf])
    probabilities=[]
    for k in range(1,13):
        by_x=mp.quad(lambda x:mp.exp(-x)*mp.log1p(x)**k,[0,1,4,16,64,mp.inf])/mp.factorial(k)
        by_t=mp.quad(lambda t:t**(k-1)*mp.exp(1-mp.exp(t)),[0,1,2,4,8,10])/mp.factorial(k-1)
        assert abs(by_x-by_t)<mp.mpf('1e-55')
        probabilities.append(by_x)
    assert abs(probabilities[0]-g)<mp.mpf('1e-55')
    # Exact signs and missing factors are proved in the notes, not inferred
    # from numerical integration. Quadrature only corroborates corrections.
    base_integral=mp.quad(lambda t:mp.exp(-mp.exp(t)),[0,1,2,4,8,10])
    assert abs(base_integral-g/mp.e)<mp.mpf('1e-55')
    assert abs(base_integral-g/3)>mp.mpf('.02')
    gamma_checks=[]
    for z in map(mp.mpf,['0','.25','.5','1','2','3']):
        integral=mp.quad(lambda x:mp.exp(-x)*(1+x)**z,[0,1,4,16,64,mp.inf])-1
        series=mp.fsum((-1)**k*z/((k+z)*mp.factorial(k)) for k in range(1,201))
        printed=mp.e*mp.gamma(1+z)-mp.e*series
        corrected=printed-mp.e
        assert abs(corrected-integral)<mp.mpf('1e-55')
        gamma_checks.append({'z':str(z),'G':mp.nstr(integral,30),'printed_minus_true':mp.nstr(printed-integral,30)})
    mean=mp.quad(lambda x:mp.exp(-x)*(1+x)*mp.log1p(x),[0,1,4,16,64,mp.inf])
    factorial_second=mp.quad(lambda x:mp.exp(-x)*(1+x)*mp.log1p(x)**2,[0,1,4,16,64,mp.inf])
    variance=factorial_second+mean-mean**2
    assert abs(mean-(1+g))<mp.mpf('1e-55')
    assert abs(variance-(2*probabilities[1]+g-g*g))<mp.mpf('1e-55')
    saddle=[]
    for n in (10,20,50,100,200,500,1000):
        xi=mp.lambertw(n);center=mp.exp(xi)-1;scale=mp.sqrt(n/(1+xi))
        peak=-center+n*mp.log(xi)
        def normalized(y):
            x=center+scale*y
            if x<=0:
                return mp.mpf(0)
            return mp.exp(-x+n*mp.log(mp.log1p(x))-peak)
        left=-center/scale
        cuts=[left]+[mp.mpf(v) for v in (-12,-6,-3,0,3,6,12,24) if v>left]+[mp.inf]
        ratio=mp.quad(normalized,cuts)/mp.sqrt(2*mp.pi)
        saddle.append({'n':n,'integral_over_asymptotic':mp.nstr(ratio,35)})
    report={'precision_digits':60,'probabilities_1_to_12':[mp.nstr(v,40) for v in probabilities],
            'two_integral_forms_checked':12,'base_integral':mp.nstr(base_integral,40),
            'g_over_3':mp.nstr(g/3,40),'mean':mp.nstr(mean,40),'variance':mp.nstr(variance,40),
            'gamma_series_checks':gamma_checks,'saddle_ratios':saddle,
            'F020':'R(0)=-g by the definition of rho, but the printed positive integral gives +g.',
            'F021':'Answer 189(c): g/3 should be g/e; the maximum in the next sentence needs the modulus of exp(-exp(u*z)), not exp(exp(u*z)).',
            'F022':'After answer 189(d), first integral needs (k-1)! instead of k!.',
            'F023':'Answer 191 gamma series is missing -e; at z=0 it gives e instead of 0.',
            'C006':'The published 2019 correction to answer 189(a) itself prints exp(exp(-x)*cos(y)); it should print exp(-exp(x)*cos(y)). Follow-up to an existing erratum, not counted as a new independent finding.',
            'limitation':'Numerical integrals corroborate analytic counterexamples and identities. The n=10..1000 saddle ratios do not prove the full asymptotic remainder.'}
    (Path(__file__).parent/'results/gould_constants.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
