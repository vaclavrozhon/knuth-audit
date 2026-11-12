"""Two short arithmetic witnesses; no queen enumeration or optimizer."""
from fractions import Fraction
import json
N20=[8,11,4,7,5,12,1,16,14,2,15,10,3,13,6,9]
LIMIT=[9,11,13,3,10,2,5,1,16,12,15,7,14,4,6,8]
def norm(q):return [(2*r-17)**2+(2*c-17)**2 for r,c in enumerate(q,1)]
def valid(q):
    assert sorted(q)==list(range(1,17))
    assert len({r+c for r,c in enumerate(q,1)})==len({r-c for r,c in enumerate(q,1)})==16
def verify():
    for q in [N20,LIMIT]:valid(q)
    a,b=[sum(Fraction(w,4)**10 for w in norm(q)) for q in [N20,LIMIT]]
    assert a==Fraction(130230066663839627189,64) and b==Fraction(130915446232517223025,64) and a<b
    assert [round(float(x*1024)/10**21,2) for x in [a,b]]==[2.08,2.09]
    assert sum(Fraction(w,4) for w in norm(LIMIT))==680==16*(16**2-1)//6
    return dict(correct_N20_costs=[str(a),str(b)],decimal_N20_costs=[float(a),float(b)],
        printed_scale_factor=1024,N2_constant_cost=680,source_distance='d²=((2r−17)²+(2c−17)²)/4',
        proves_cost_scale_error=True,proves_positive_integer_N2_exception=True,new_global_optimization=False)
if __name__=='__main__':print(json.dumps(verify(),indent=2))
