"""Exact absorption equations and independent constants for 2.2.2-13/14."""
from pathlib import Path
import json,time
import sympy as s
import mpmath as mp

def absorption(m,p):
    states=[(x,y) for x in range(m) for y in range(m-x)]
    loc={v:i for i,v in enumerate(states)};n=len(states)
    A=s.eye(n);R=s.zeros(n,m+1);q=(1-p)/2;d=p/2
    for i,(x,y) in enumerate(states):
        for dest,prob in [((x+1,y),q),((x,y+1),q),((max(x-1,0),y),d),((x,max(y-1,0)),d)]:
            if sum(dest)==m:R[i,dest[0]]+=prob
            else:A[i,loc[dest]]-=prob
    v=(A.inv(method='DM')*R)[0,:]
    assert s.simplify(sum(v)-1)==0
    return [s.factor(x) for x in v]

def main():
    start=time.monotonic();p=s.symbols('p');v=absorption(4,p);den=16-12*p+4*p*p
    expected=[1/den,s.Rational(1,4),(6-6*p+2*p*p)/den,s.Rational(1,4),1/den]
    assert all(s.cancel(a-b)==0 for a,b in zip(v,expected))
    cases=[]
    for m in range(1,9):
        for pval in [s.Rational(0),s.Rational(1,3),s.Rational(1,2),s.Rational(2,3)]:
            row=absorption(m,pval)
            assert row==list(reversed(row)) and all(x>=0 for x in row)
            e=sum(row[k]*max(k,m-k) for k in range(m+1))
            cases.append({'m':m,'p':str(pval),'expected_max':str(e)})
    for m in range(1,101):
        e=sum(s.Rational(1 if k in [0,m] else 2,2*m)*max(k,m-k) for k in range(m+1))
        assert e==s.Rational(3*m,4)+s.Rational(m%2,4*m)
    mp.mp.dps=70
    a=mp.mpf('.5')+sum(4*mp.sin(n*mp.pi/2)/(n*n*mp.pi**2*mp.sinh(n*mp.pi/2)) for n in range(1,101))
    b=1-sum(8/(n*n*mp.pi**2*mp.cosh(n*mp.pi/2)) for n in range(1,101,2))
    assert abs(a-b)<mp.mpf('1e-65')
    coefficients=[]
    for n in range(2,6):
        phi=lambda z:mp.exp(-z*z/2)/mp.sqrt(2*mp.pi)
        Phi=lambda z:(1+mp.erf(z/mp.sqrt(2)))/2
        value=mp.sqrt(n)*(n-1)*mp.quad(lambda z:phi(z)**2*Phi(z)**(n-2),[-mp.inf,0,mp.inf])
        orthant={2:mp.mpf(1),3:mp.mpf('.5'),4:mp.atan(mp.sqrt(2))/mp.pi,5:mp.mpf(1)/8+3*mp.atan(1/mp.sqrt(8))/(4*mp.pi)}[n]
        closed=(n-1)*mp.sqrt(n)*orthant/(2*mp.sqrt(mp.pi))
        assert abs(value-closed)<mp.mpf('1e-60')
        coefficients.append({'n':n,'c_n':mp.nstr(value,40)})
    result={'symbolic_m4':[str(x) for x in v],'exact_cases':cases,'fixed_m_limit_checked_through':100,'critical_alpha_book':mp.nstr(a,60),'critical_alpha_square':mp.nstr(b,60),'alpha_numerical_note':'Finite series match independently derived square boundary-value expression; an analytic equivalence is not inferred from numeric matching.','multinomial_constants':coefficients,'elapsed_seconds':time.monotonic()-start}
    (Path(__file__).parent/'results/sequential-probability.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='exact_cases'},indent=2))
if __name__=='__main__':main()
