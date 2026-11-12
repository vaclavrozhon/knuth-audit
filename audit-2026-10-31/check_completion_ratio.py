#!/usr/bin/env python3
"""Exact mixed-radix verification for DLX28 and progress-report formula27."""
from datetime import datetime, timezone
from fractions import Fraction as F
from itertools import product
import json
import math

from dlx1_audit_tools import ROOT, sha


def ratio(cs,ts):
    result=F(0);denominator=1
    for c,t in zip(cs,ts):
        assert 1<=c<=t
        denominator*=t;result+=F(c-1,denominator)
    return result+F(1,2*denominator)


def integer_formula(cs,ts):
    k=0
    for c,t in zip(cs,ts):k=k*t+c-1
    return F(2*k+1,2*math.prod(ts))


def main():
    count=0;vectors=0
    for depth in range(1,6):
        for ts in product(range(1,5),repeat=depth):
            values=set();half=0
            for cs in product(*(range(1,t+1) for t in ts)):
                rho=ratio(cs,ts)
                assert rho==integer_formula(cs,ts)
                assert 0<rho<1 and rho.denominator%2==0
                assert rho not in values;values.add(rho)
                complement=tuple(t+1-c for c,t in zip(cs,ts))
                assert rho+ratio(complement,ts)==1
                condition=all(t==2*c-1 for c,t in zip(cs,ts))
                assert (rho==F(1,2))==condition
                half+=condition;count+=1
            assert len(values)==math.prod(ts)
            assert half==int(all(t%2==1 for t in ts))
            vectors+=1
    approximation=[]
    for ell in range(30):
        actual=ratio([2]*(ell+1),[4]*(ell+1))
        expected=F(1,3)+F(1,24*4**ell)
        assert actual==expected
        approximation.append(dict(ell=ell,numerator=actual.numerator,denominator=actual.denominator))
    result=dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
                source_sha256=sha(__file__),fixed_radix_vectors=vectors,exact_cases=count,
                approximation_cases=approximation,
                scope='General mixed-radix proof covers arbitrary finite positive radices; '
                      'finite exact verification supplements that proof. No claim about the accuracy of the runtime heuristic.')
    path=ROOT/'results/completion_ratio.json';path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='approximation_cases'},indent=2))


if __name__=='__main__':main()
