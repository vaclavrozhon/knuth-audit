"""Exact feasible queenon + Arb interval certificate for Backtrack exercise 15.

Inputs are the published Nobel--Agrawal--Boyd witnesses, not a new optimizer.
Run with python-flint, numpy, scipy. No large sparse constraint matrix is built.
The Simkin variational/enumeration theorem is an explicitly imported theorem.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
import sys
import time
import numpy as np
import flint
from flint import arb, fmpq, ctx

ROOT = Path(__file__).resolve().parent
SRC = ROOT/'sources/queens/n-queens/src'
OUT = ROOT/'results/queens_constant'
OUT.mkdir(exist_ok=True)
ctx.prec = 128


def stamp():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact_float(x):
    a,b = float(x).as_integer_ratio()
    return arb(fmpq(a,b))


def imported(name):
    spec=importlib.util.spec_from_file_location(name,SRC/'problem_formulations'/f'{name}.py')
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def lower_transpose(v,n):
    """Independent explicit dual coefficient for each triangle; small checks only."""
    row=np.r_[0.,v[:n-1]]; col=v[n-1:2*n-1]
    anti=v[2*n-1:4*n-1]; diag=v[4*n-1:6*n-1]
    r,c=np.indices((n,n)); base=row[:,None]+col[None,:]
    W=base+anti[r+c]+diag[n-1+c-r]
    N=base+anti[r+c]+diag[n+c-r]
    E=base+anti[r+c+1]+diag[n+c-r]
    S=base+anti[r+c+1]+diag[n-1+c-r]
    return np.concatenate([W.ravel(),N.ravel(),E.ravel(),S.ravel(),anti,diag])


def project_pair(P,Q,D):
    """Exact affine projection: rows of each matrix n, pair's columns 2n.

    Input arrays are integers over D. Output denominator is 2*n*n*D.
    Row deficits R,T and pair-column deficits C give
      Y_P = 2*n*n*P + 2*n*R_i + n*C_j - sum(C).
    Formula for Y_Q replaces R with T. All operations here are int64, with
    an a-priori size bound checked below before arithmetic.
    """
    n=P.shape[0]
    assert n<=1024 and D<=2**30 and np.max(np.abs(P))<2*D and np.max(np.abs(Q))<2*D
    R=n*D-P.sum(axis=1); T=n*D-Q.sum(axis=1)
    C=2*n*D-(P+Q).sum(axis=0); total=C.sum()
    Y=2*n*n*P+2*n*R[:,None]+n*C[None,:]-total
    Z=2*n*n*Q+2*n*T[:,None]+n*C[None,:]-total
    den=2*n*n*D
    # Cell arithmetic is bounded by 2^54 under the preconditions; also bound sums.
    assert all(int(np.abs(z).max())*n<2**63 for z in [Y,Z,Y+Z])
    assert np.all(Y.sum(axis=1)==n*den)
    assert np.all(Z.sum(axis=1)==n*den)
    assert np.all((Y+Z).sum(axis=0)==2*n*den)
    return Y,Z,den


def diagonal_slacks(N,E,S,W,den):
    n=N.shape[0]; d=2*n*den
    def diagonal_sum(X,anti):
        assert int(np.abs(X).max())*n<2**63
        X=np.fliplr(X) if anti else X
        return np.array([np.diag(X,n-k).sum() for k in range(1,2*n)],dtype=np.int64)
    return (d-diagonal_sum(N+W,True),d-diagonal_sum(S+E,True),
            d-diagonal_sum(N+E,False),d-diagonal_sum(S+W,False)),d


def g(x):
    return arb(0) if x==0 else x*x.log()


def integral_g(s,t):
    """Integral_0^1 g((1-y)s+yt)dy by its exact antiderivative."""
    if s==t:
        return g(s)
    def H(x):
        return arb(0) if x==0 else (2*x*x*x.log()-x*x)/4
    return (H(t)-H(s))/(t-s)


def selfcheck():
    lower,upper=imported('lower_bound'),imported('xqueenons')
    rng=np.random.default_rng(20261101)
    for n in range(1,7):
        v=rng.normal(size=6*n-1)
        A,b=lower.construct_A(n)
        assert np.max(np.abs(lower_transpose(v,n)-A.T@v))<2e-14
        # Independent projection and diagonal indexing vs the published matrix.
        D=2**20
        P,Q=(np.rint(rng.uniform(.8,1.2,(n,n))*D).astype(np.int64) for _ in range(2))
        N,S,den=project_pair(P,Q,D)
        E,W=N.T.copy(),S.T.copy()
        slacks,sden=diagonal_slacks(N,E,S,W,den)
        tail=np.column_stack(slacks[:2]).ravel().tolist()+np.column_stack(slacks[2:]).ravel().tolist()
        x=np.r_[N.ravel()/den,E.ravel()/den,S.ravel()/den,W.ravel()/den,np.array(tail)/sden]
        A,b=upper.construct_A(n)
        assert np.max(np.abs(A@x-b))<2e-14
        # Uniform queenon has negative Q-entropy exactly 2, including zero endpoints.
        den=1;N=E=S=W=np.ones((n,n),dtype=np.int64)
        slacks,sden=diagonal_slacks(N,E,S,W,den)
        NW,SE,NE,SW=[[arb(fmpq(int(t),sden)) for t in a] for a in slacks]
        value=arb(3)
        for left,right in [([arb(1)]+SE,NW+[arb(1)]),([arb(1)]+SW,NE+[arb(1)])]:
            value+=sum((integral_g(s,t) for s,t in zip(left,right)),arb(0))/n
        assert value.contains(2),value
    return dict(sizes=list(range(1,7)),dual_coefficients='match sparse published matrix',
                rational_projection='all linear constraints exact; diagonal indexing matches source',
                uniform_queenon_objective='contains exactly 2 for each size')


def lower_certificate(v,n,meta):
    vals=[exact_float(x) for x in v]
    rows=[arb(0)]+vals[:n-1]; cols=vals[n-1:2*n-1]
    anti=vals[2*n-1:4*n-1]; diag=vals[4*n-1:6*n-1]
    er=[x.exp() for x in rows];ec=[x.exp() for x in cols]
    ea=[x.exp() for x in anti];ed=[x.exp() for x in diag]
    aa=[x+y for x,y in zip(ea,ea[1:])];dd=[x+y for x,y in zip(ed,ed[1:])]
    total=arb(0)
    # Four triangle exponential terms factor as (a_k+a_{k+1})(d_l+d_{l+1}).
    for r in range(n):
        subtotal=arb(0)
        for c in range(n):
            subtotal+=ec[c]*aa[r+c]*dd[n-1+c-r]
        total+=er[r]*subtotal
        if (r+1)%128==0:
            print('lower rows',r+1,n,flush=True)
    exp_sum=arb(-1).exp()*(total+sum(ea,arb(0))+sum(ed,arb(0)))
    value=sum(vals,arb(0))/n-exp_sum+4*arb(n).log()+2*arb(2).log()+3
    assert value.is_finite()
    meta['lower']=dict(n=n,dual_dimension=len(v),interval=value.str(35),
        formula='v^T b - sum exp(A^T v - 1) + 4 log n + 2 log 2 + 3',
        inputs='all binary64 dual entries interpreted as exact dyadic rationals')
    return value


def upper_certificate(x,n,meta):
    D=2**30
    # Rounding selects an initial rational grid; its feasibility is not assumed.
    raw=[np.rint(z*D).astype(np.int64) for z in x[:4*n*n].reshape((4,n,n))]
    N,S,den=project_pair(raw[0],raw[2],D)
    Et,Wt,den2=project_pair(raw[1].T,raw[3].T,D)
    E,W=Et.T.copy(),Wt.T.copy();assert den2==den
    grids=[N,E,S,W]
    assert all(np.min(z)>0 for z in grids)
    slacks,sden=diagonal_slacks(*grids,den)
    assert all(np.min(z)>=0 for z in slacks)
    # All row/column equalities and all diagonal inequalities hold as integers.
    h=hashlib.sha256()
    for z in grids:h.update(z.astype('<i8').tobytes())
    unique,counts=np.unique(np.concatenate([z.ravel() for z in grids]),return_counts=True)
    entropy=arb(0)
    for i,(number,count) in enumerate(zip(unique,counts)):
        a=arb(fmpq(int(number),den))
        entropy+=int(count)*g(a)
        if (i+1)%100000==0:print('upper unique densities',i+1,len(unique),flush=True)
    value=3+entropy/(4*n*n)
    NW,SE,NE,SW=[[arb(fmpq(int(t),sden)) for t in a] for a in slacks]
    for left,right in [([arb(1)]+SE,NW+[arb(1)]),([arb(1)]+SW,NE+[arb(1)])]:
        value+=sum((integral_g(s,t) for s,t in zip(left,right)),arb(0))/n
    assert value.is_finite()
    # The original implementation is only a floating-point crosscheck, not the certificate.
    original=imported('xqueenons').construct_objective_fxn_derivs(n)[0](x)
    meta['upper']=dict(n=n,interval=value.str(35),original_float_objective=float(original),
        rational_density_denominator=den,rational_slack_denominator=sden,
        rounded_grid_bits=30,exact_constraint_checks='all pass',
        min_density_numerator=min(int(z.min()) for z in grids),
        min_slack_numerator=min(int(z.min()) for z in slacks),
        maximum_change_from_published_density=float(max(np.max(np.abs(z/den-w)) for z,w in zip(grids,x[:4*n*n].reshape((4,n,n))))),
        unique_density_values=len(unique),rational_grid_sha256=h.hexdigest())
    return value


def main():
    started=time.time()
    meta=dict(started_at_utc=stamp(),pid=os.getpid(),command=[sys.executable,*sys.argv],
        status='running',precision_bits=ctx.prec,python_flint=flint.__version__,
        log='results/queens_constant/certificate.log',time_limit_seconds=7200,
        scope='Independent exact-feasibility and interval numerical certification; Simkin enumeration and variational theorem imported.')
    paths=[SRC/'witnesses/L_2048.npz',SRC/'witnesses/U_1024.npz']
    meta['source_sha256']={str(p.relative_to(ROOT)):sha(p) for p in paths}
    meta['script_sha256']=sha(__file__)
    (OUT/'certificate-run.json').write_text(json.dumps(meta,indent=2)+'\n')
    try:
        meta['selfcheck']=selfcheck()
        if '--selfcheck' in sys.argv:
            meta['status']='selfcheck_pass'
            print(json.dumps(meta['selfcheck'],indent=2));return
        lower=lower_certificate(np.load(paths[0])['v'],2048,meta)
        (OUT/'certificate-run.json').write_text(json.dumps(meta,indent=2)+'\n')
        upper=upper_certificate(np.load(paths[1])['x'],1024,meta)
        lo=arb(fmpq(1944000752,10**9));hi=arb(fmpq(1944001082,10**9))
        assert lower>lo and upper<hi, (lower,upper)
        sigma_lo=(1-hi).exp();sigma_hi=(1-lo).exp()
        assert sigma_lo>arb(fmpq(3890675,10**7))
        assert sigma_hi<arb(fmpq(3890685,10**7))
        meta.update(status='pass',alpha_rational_interval=['1.944000752','1.944001082'],
            sigma_lower_endpoint=sigma_lo.str(35),sigma_upper_endpoint=sigma_hi.str(35),
            six_decimal_rounding='0.389068',finished_at_utc=stamp(),elapsed_seconds=time.time()-started)
    except Exception as error:
        meta.update(status='failed',error=repr(error),finished_at_utc=stamp())
        raise
    finally:
        (OUT/'certificate-run.json').write_text(json.dumps(meta,indent=2)+'\n')
    print(json.dumps(meta,indent=2),flush=True)


if __name__=='__main__':main()
