"""One bounded new check of the previously unproved reversed Sigma2 maximum."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib,os,warnings
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import csc_matrix,vstack

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/cost226_229/reversed-sigma2-bounded.json'
assert not OUT.exists()
start=time.monotonic();n=16
rows=[(i,j,j+i+1) for i in range(1,n+1) for j in range(1,2*n-i)]
weights=np.array([i*(j*j+k*k) for i,j,k in rows],dtype=float)
rr=[];cc=[]
for c,(i,j,k) in enumerate(rows):rr.extend([i-1,n+j-1,n+k-1]);cc.extend([c]*3)
A=csc_matrix((np.ones(len(rr)),(rr,cc)),shape=(3*n,len(rows)))
bound=68880-2*33*3708+33*33*16*17
assert bound==120360
AA=vstack([A,csc_matrix(weights.reshape(1,-1))],format='csc')
with warnings.catch_warnings():
    warnings.simplefilter('ignore',RuntimeWarning)
    res=milp(np.zeros(len(rows)),integrality=np.ones(len(rows)),bounds=Bounds(0,1),
        constraints=LinearConstraint(AA,np.r_[np.ones(3*n),bound+1],np.r_[np.ones(3*n),np.inf]),
        options={'time_limit':20.0,'mip_rel_gap':0.0,'threads':1})
model=None;value=None
if res.x is not None:
    bits=np.rint(res.x).astype(int);assert np.max(np.abs(res.x-bits))<1e-5 and np.all(A@bits==1)
    model=[0]*(2*n)
    for b,(i,j,k) in zip(bits,rows):
        if b:assert not model[j-1] and not model[k-1];model[j-1]=model[k-1]=i
    value=sum((j+1)**2*v for j,v in enumerate(model));assert value>bound
report=dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),nice=os.nice(0),
    seconds=time.monotonic()-start,limit_seconds=20,threads=1,status=int(res.status),message=res.message,strict_target=bound+1,
    counterexample=model,exact_counterexample_cost=value,numerical_infeasibility_is_exact_certificate=False,old_censuses_repeated=0)
OUT.write_text(json.dumps(report,indent=2)+'\n');print(report)
