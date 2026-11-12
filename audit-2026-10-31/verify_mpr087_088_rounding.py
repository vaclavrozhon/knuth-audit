"""Exact rational certificates for the four printed MPR87–88 decimals.
No path enumeration, simulation, or prior verifier is run.
"""
from fractions import Fraction as Q
from datetime import datetime, timezone
from pathlib import Path
import json, os, time

def atan_interval(x, terms):
    s=sum(((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(terms)),Q(0))
    nxt=(-1)**terms*x**(2*terms+1)/Q(2*terms+1)
    return min(s,s+nxt),max(s,s+nxt)

def log_interval(z, terms):
    s=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(terms)),Q(0))
    tail=2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
    return s,s+tail

def pair(x):
    return {"lower":str(x[0]),"upper":str(x[1]),"decimal_display":[float(x[0]),float(x[1])]}

def main():
    start=time.perf_counter()
    a=atan_interval(Q(1,5),12);b=atan_interval(Q(1,239),4)
    pi=(16*a[0]-4*b[1],16*a[1]-4*b[0])
    ln2=log_interval(Q(1,3),20);ln3=log_interval(Q(1,2),30)
    sqrt3=(Q(1732050807568877,10**15),Q(1732050807568878,10**15))
    assert sqrt3[0]**2<3<sqrt3[1]**2
    hit=(pi[0]/(3*sqrt3[1]),pi[1]/(3*sqrt3[0]))
    values={"MPR87":(pi[0]/4-ln2[1]/2,pi[1]/4-ln2[0]/2),
            "MPR88a":ln2,
            "MPR88b":(ln3[0]-hit[1],ln3[1]-hit[0]),
            "MPR88_atom_2_over_3":(2*hit[0]-ln3[1],2*hit[1]-ln3[0])}
    targets={"MPR87":439,"MPR88a":693,"MPR88b":494,"MPR88_atom_2_over_3":111}
    for name,x in values.items():
        assert Q(2*targets[name]-1,2000)<x[0]<=x[1]<Q(2*targets[name]+1,2000)
    result={"executed_at_utc":datetime.now(timezone.utc).isoformat(),"nice":os.getpriority(os.PRIO_PROCESS,0),
            "purpose":"Only exact rounding certificates for four printed decimal approximations",
            "constants":{"pi":pair(pi),"ln2":pair(ln2),"ln3":pair(ln3),"sqrt3":pair(sqrt3)},
            "values":{k:pair(v)for k,v in values.items()},"printed_thousandths":targets,
            "all_roundings_correct":True,"elapsed_seconds":time.perf_counter()-start,
            "path_enumerations":0,"simulations":0,"old_runs_repeated":0}
    assert result["nice"]>=15
    out=Path(__file__).parent/"results/sequential/mpr-087-088-rounding.json"
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:result[k]for k in ["executed_at_utc","nice","all_roundings_correct","elapsed_seconds"]}))
if __name__=="__main__":main()
