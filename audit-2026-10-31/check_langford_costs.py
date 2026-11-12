"""Langford226--229: exact identities, lex extrema, DLX5 and HiGHS optima."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
import json,subprocess,time
import numpy as np
from scipy.sparse import csc_matrix
from scipy.optimize import milp,Bounds,LinearConstraint
ROOT=Path(__file__).parent;OUT=ROOT/'results/langford_costs';OUT.mkdir(exist_ok=True)

def pairings(n,descending=False,first=False):
    seq=[0]*(2*n);order=list(range(1,n+1));order=order[::-1] if descending else order
    def rec(used):
        if used==(1<<n)-1:yield tuple(seq);return
        pos=seq.index(0)
        for i in order:
            if used>>(i-1)&1 or pos+i+1>=2*n or seq[pos+i+1]:continue
            seq[pos]=seq[pos+i+1]=i
            yield from rec(used|(1<<(i-1)))
            seq[pos]=seq[pos+i+1]=0
    return rec(0)

def costs(a):return [sum((j+1)*x for j,x in enumerate(a)),sum((j+1)**2*x for j,x in enumerate(a)),sum((j+1)*x*x for j,x in enumerate(a))]

def basics():
    results=[]
    for n in [3,4,7,8,11]:
        allp=list(pairings(n));hist=Counter()
        for a in allp:
            s1,s2,S=costs(a);r1,r2,R=costs(a[::-1]);j=[a.index(k)+1 for k in range(1,n+1)]
            assert s1+r1==(2*n+1)*n*(n+1)
            assert 3*(S+R)==(2*n+1)**2*n*(n+1)
            assert s2-(2*n+1)*s1==r2-(2*n+1)*r1
            assert 4*sum(j)==(3*n-1)*n
            assert 6*sum(x*x for x in j)==2*(4*n*n-1)*n-3*s1
            hist[s1,s2]+=1
        if n==7:
            assert hist[444,4440]==4 and hist[448,4424]==6
            assert sum(v for (a,b),v in hist.items() if a==444 or b==4440)==4
            assert sum(v for (a,b),v in hist.items() if a==448 or b==4424)==6
        results.append(dict(n=n,solutions=len(allp)))
    lexmin=next(pairings(16));lexmax=next(pairings(16,True))
    expected_min=[1,2,1,3,2,4,8,3,12,13,4,10,14,15,16,8,9,6,11,5,7,12,10,13,6,5,9,14,7,15,11,16]
    expected_max=[16,14,15,9,6,13,5,7,12,10,11,6,5,9,8,7,14,16,15,13,10,12,11,8,4,1,3,1,2,4,3,2]
    assert list(lexmin)==expected_min and tuple(lexmax)>tuple(expected_max)
    assert costs(lexmin)==[5240,119192,60324] and costs(expected_max)==[3708,68880,37552]
    (OUT/'basics.json').write_text(json.dumps(dict(small=results,lexmin=lexmin,lexmax=lexmax,lexmin_costs=costs(lexmin),lexmax_costs=costs(lexmax),printed_lexmax=expected_max,printed_costs=costs(expected_max)),indent=2)+'\n')
    print('Reversal identities and lex minimum agree; printed lex maximum is not maximal.',flush=True)

def problem(which,n=16):
    rows=[];weights=[]
    for i in range(1,n+1):
        for j in range(1,2*n-i):
            k=j+i+1;rows.append((i,j,k));weights.append([i*(j+k),i*(j*j+k*k),i*i*(j+k)][which])
    return rows,weights

def original(which):
    name=['sum1','sum2','squared_values'][which];rows,weights=problem(which);K=12017 if which<2 else 2
    header=' '.join([f'n{i}' for i in range(1,17)]+[f's{i}' for i in range(1,33)])
    data=header+'\n'+'\n'.join(f'n{i} s{j} s{k} |{w}' for (i,j,k),w in zip(rows,weights))+'\n'
    (OUT/(name+'.xcc')).write_text(data);start=time.monotonic()
    p=subprocess.run(['/tmp/knuth-dlx5',f'k{K}','v17','m1','d0'],input=data,text=True,capture_output=True,timeout=1800)
    (OUT/(name+'.out')).write_text(p.stdout);(OUT/(name+'.log')).write_text(p.stderr)
    (OUT/(name+'-run.json')).write_text(json.dumps(dict(seconds=time.monotonic()-start,returncode=p.returncode,k=K),indent=2)+'\n')
    assert 'The optimum cost' in p.stderr and 'TIMEOUT' not in p.stderr
    print(name,p.stderr[-450:],flush=True)

def integer_program(which):
    name=['sum1','sum2','squared_values'][which];rows,weights=problem(which);rr=[];cc=[]
    for col,(i,j,k) in enumerate(rows):
        rr.extend([i-1,16+j-1,16+k-1]);cc.extend([col]*3)
    A=csc_matrix((np.ones(len(rr)),(rr,cc)),shape=(48,len(rows)))
    start=time.monotonic();res=milp(np.array(weights,dtype=float),integrality=np.ones(len(rows)),bounds=Bounds(0,1),constraints=LinearConstraint(A,np.ones(48),np.ones(48)),options={'time_limit':900,'mip_rel_gap':0.0})
    model=None;objective=None
    if res.x is not None:
        chosen=np.rint(res.x).astype(int);assert np.max(np.abs(res.x-chosen))<1e-5 and np.all(A@chosen==1)
        model=[0]*32
        for (i,j,k),v in zip(rows,chosen):
            if v:model[j-1]=model[k-1]=i
        objective=int(np.dot(weights,chosen));assert costs(model)[which]==objective
    report=dict(status=int(res.status),message=res.message,objective=objective,model=model,dual_bound=float(res.mip_dual_bound) if hasattr(res,'mip_dual_bound') else None,gap=float(res.mip_gap) if hasattr(res,'mip_gap') else None,seconds=time.monotonic()-start)
    (OUT/(name+'-milp.json')).write_text(json.dumps(report,indent=2)+'\n');print(name,'MILP',report,flush=True)

if __name__=='__main__':
    basics()
    with ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(original,range(3)))
    for i in range(3):integer_program(i)
