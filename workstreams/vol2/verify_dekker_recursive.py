"""Verify and expose the general failure family proved in dekker-recursive.md."""
from fractions import Fraction as Q
from pathlib import Path
import json
from dekker_recursive import Recursive,val,flatten
ROOT=Path(__file__).resolve().parent
out=[]
for p in [2,3,4,5,8,12,20,24,53,64,113]:
    e=Q(1,2**p);a=e*e/4
    for ties in ['even','odd','away']:
        r=Recursive(p,ties)
        u=((Q(2),a),(Q(0),Q(0)));v=((Q(1),e),(Q(0),Q(0)))
        # Four-word representations of exactly representable4p-bit inputs.
        assert val(r.encode(val(u),2))==val(u) and val(r.encode(val(v),2))==val(v)
        assert 2*p+4<=4*p
        for pair in [u[0],v[0]]:
            h,t=pair
            assert abs(t)<=abs(h)*e
            assert abs(t)<=abs(h+t)*e/(1+e) # Dekker's stronger definition7.2.
        ans=r.add(u,v,2)
        assert ans==((Q(3),e),(Q(0),Q(0))) and r.count==64
        assert val(ans)-val(u)-val(v)==-a
        assert r.trace[-1]['head_sum_residual_error']==str(-a)
        # Rounding comparisons behind the symbolic proof; all strict.
        assert a<e*e and a<e*e/2 and e<2*e
        assert r.ar.R(e+a)==e and r.ar.R(a-e)==-e
        assert r.ar.R(3+e)==3
        d=r.ar.R(-1-e);assert d in [-Q(1),-1-2*e]
        two_pair_trace=r.trace
        r.count=0;r.trace=[]
        can=r.add((Q(1),e),(-Q(1),a),1)
        assert val(can)==e and r.count==8
        out.append({'p':p,'ties':ties,'epsilon':str(e),'a':str(a),'u':flatten(u),'v':flatten(v),'answer':flatten(ans),'absolute_error':str(-a),'error_in_4p_units':str(a*2**(4*p)),'scalar_operations':64,'cancellation_answer':flatten(can),'cancellation_relative_error':str(a/(e+a)),'trace':two_pair_trace})
(ROOT/'results/dekker-recursive-family.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(out),'exact family instances; symbolic proof in notes/dekker-recursive.md')
