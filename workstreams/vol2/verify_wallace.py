"""TAOCP 3.4.1-31: exact proofs/certificates and independent-pool experiment.

The possible error is in the printed angle construction, not orthogonality.
The experiment uses two regeneration passes, 682 outputs from the X half,
all printed permutations, and the positive square root of the printed scale.
"""
from pathlib import Path
from fractions import Fraction as Q
import json
import math
import sys
import time
import mpmath as mp
import numpy as np
import sympy as s

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/wallace.json'
mp.mp.dps=70

def theory():
    c,t,x,y=s.symbols('c t x y',real=True)
    xp=c*x+t*y;yp=-t*x+c*y
    assert s.expand(xp**2+yp**2-(c*c+t*t)*(x*x+y*y))==0
    # Characteristic roots: monotonicity of positive inverse-power sum is
    # proved in the note; these rational endpoints certify the numbers.
    roots=[]
    funcs=[lambda z:(z**-24+z**-55)/mp.sqrt(2)-1,
           lambda z:mp.mpf(3)/5*z**-24+mp.mpf(4)/5*z**-55-1]
    for i,f in enumerate(funcs):
        lo=mp.mpf(1);hi=mp.mpf('1.1')
        for _ in range(220):
            mid=(lo+hi)/2
            if f(mid)>0:lo=mid
            else:hi=mid
        denominator=10**30;a=Q(int(mp.floor(lo*denominator)),denominator);b=a+Q(1,denominator)
        g=(lambda z:(z**31+1)**2-2*z**110) if i==0 else (lambda z:3*z**31+4-5*z**55)
        assert g(a)>0 and g(b)<0
        roots.append(dict(lower=str(a),upper=str(b),decimal=mp.nstr((lo+hi)/2,45)))
    d=2048;n=1024;m=682
    error2=Q(1,d+2)+Q(8*d+1,d*(2*d-1))
    assert error2<Q(1,400)
    # sqrt(3)>1.732 and pi<22/7 give a rational strict lower bound.
    lower_sbar=3*(Q(1732,1000)-1)/Q(22,7)
    assert lower_sbar**2*Q(m,n)>Q(8,25)
    sbar=3*(mp.sqrt(3)-1)/mp.pi
    covariance=-mp.mpf(m)/n*sbar**2
    variance=1-Q(1,d*(d+2))
    # Exact chi-square approximation moments under ideal N(0,1) input.
    # T=(Y+sqrt(2d-1))^2/2: E T=d, Var T=2d-1/2.
    assert Q(1+2*d-1,2)==d
    assert Q(2+4*(2*d-1),4)==2*d-Q(1,2)
    return dict(root_brackets=roots,d=d,n=n,m=m,angle_acceptance='1/3',
                mean_sine=mp.nstr(sbar,50),unscaled_lag2_covariance=mp.nstr(covariance,50),
                scaled_block_variance=str(variance),mean_square_scaling_error_bound=str(error2),
                scaled_lag2_covariance_strict_upper_bound='-11/50',
                correction='An independent random sign on sine makes the mean rotation matrix zero; not a proof of full RNG quality.')

def permutations():
    # All affine permutations through modulus32, tested independently by inversion.
    count=0;entries=0
    for n in [2,4,8,16,32]:
        for a in range(1,n,2):
            inv=pow(a,-1,n)
            for b in range(n):
                perm=[(a*j+b)%n for j in range(n)]
                assert sorted(perm)==list(range(n))
                for j,k in enumerate(perm):assert (inv*(k-b))%n==j;entries+=1
                count+=1
    # Mean of every indexed image equals the complete mean for each odd a.
    for n in [2,4,8,16,32,64,1024]:
        for a in range(1,n,2):
            for j in [0,n//2,n-1]:
                assert sum((a*j+b)%n for b in range(n))==n*(n-1)//2
    # Symbolic Gaussian fourth moment used for the scaled covariance bound:
    # direction on d-sphere has E e_i^2 e_j^2=1/[d(d+2)] for i!=j.
    d=s.symbols('d',positive=True)
    variance=(2*d-1)/(2*d)+1/(2*(d+2))
    assert s.simplify(variance-(1-1/(d*(d+2))))==0
    return dict(affine_permutations=count,inverse_entries=entries,
                averaged_offsets_moduli=[2,4,8,16,32,64,1024])

def angles(rng,batch):
    co=[];si=[];candidates=0
    while len(co)<batch:
        uv=rng.random((max(16,2*(batch-len(co))),2));candidates+=len(uv)
        u,v=uv[:,0],uv[:,1];rr=u*u+v*v
        good=(rr>0)&(rr<=1)
        u,v,rr=u[good],v[good],rr[good]
        c=(u*u-v*v)/rr;t=2*u*v/rr
        good=(np.abs(c)>=.5)&(t>=.5)
        co.extend(c[good]);si.extend(t[good])
    return np.array(co[:batch]),np.array(si[:batch]),candidates

def experiment():
    rng=np.random.Generator(np.random.PCG64(0x34131C58))
    n=1024;d=2*n;m=682;batch=256;trials=32768
    products=[[],[]];rawproducts=[[],[]];squares=[[],[]];means=[[],[]]
    max_norm_error=0.;max_mean_invariant_error=0.
    for base in range(0,trials,batch):
        pool=rng.standard_normal((batch,d));norm=np.sum(pool*pool,axis=1)
        pool2=pool.copy()
        initial=pool[:,:m].sum(axis=1)/math.sqrt(m)
        scale=np.abs(pool[:,-1]+math.sqrt(2*d-1))/np.sqrt(2*norm)
        initial_scaled=scale*initial
        old_invariant=pool[:,:n].sum(axis=1)**2+pool[:,n:].sum(axis=1)**2
        for _ in range(2):
            c,t,_=angles(rng,batch)
            a=2*rng.integers(0,n//2,batch)+1;b=rng.integers(0,n,batch)
            cc=2*rng.integers(0,n//2,batch)+1;dd=rng.integers(0,n,batch)
            ix=(a[:,None]*np.arange(n)+b[:,None])%n
            iy=(cc[:,None]*np.arange(n)+dd[:,None])%n+n
            rows=np.arange(batch)[:,None]
            x=pool[rows,ix];y=pool[rows,iy]
            pool=np.concatenate((c[:,None]*x+t[:,None]*y,-t[:,None]*x+c[:,None]*y),axis=1)
            sign=2*rng.integers(0,2,batch)-1;tt=t*sign
            x=pool2[rows,ix];y=pool2[rows,iy]
            pool2=np.concatenate((c[:,None]*x+tt[:,None]*y,-tt[:,None]*x+c[:,None]*y),axis=1)
        for variant,p in enumerate([pool,pool2]):
            end=p[:,:m].sum(axis=1)/math.sqrt(m)
            # S is the original invariant, as specified by the book.
            scale=np.abs(p[:,-1]+math.sqrt(2*d-1))/np.sqrt(2*norm)
            scaled=scale*end
            products[variant].extend(initial_scaled*scaled)
            rawproducts[variant].extend(initial*end)
            squares[variant].extend(scaled**2)
            means[variant].extend(scaled)
            max_norm_error=max(max_norm_error,float(np.max(np.abs(np.sum(p*p,axis=1)/norm-1))))
            invariant=p[:,:n].sum(axis=1)**2+p[:,n:].sum(axis=1)**2
            max_mean_invariant_error=max(max_mean_invariant_error,float(np.max(np.abs(invariant-old_invariant)/(1+old_invariant))))
    assert max_norm_error<1e-13 and max_mean_invariant_error<1e-11
    variants=[]
    for i in range(2):
        a=np.array(products[i]);b=np.array(rawproducts[i])
        variants.append(dict(random_sine_sign=bool(i),mean=float(np.mean(means[i])),
                             second_moment=float(np.mean(squares[i])),
                             scaled_product_mean=float(np.mean(a)),scaled_product_standard_error=float(np.std(a,ddof=1)/math.sqrt(trials)),
                             unscaled_product_mean=float(np.mean(b)),unscaled_product_standard_error=float(np.std(b,ddof=1)/math.sqrt(trials))))
    # Descriptive empirical experiment; no tail probability or global RNG certification.
    return dict(seed_hex='0x34131C58',generator='numpy.PCG64',numpy_version=np.__version__,
                independent_initial_pools=trials,pool_size=d,outputs_per_pass=m,passes=2,
                variants=variants,max_norm_relative_error=max_norm_error,
                max_block_mean_invariant_relative_error=max_mean_invariant_error)

def exact_two_pass():
    # Finite angle law: cos=+/-3/5, sin=4/5. All affine index choices,
    # both angles, and every ordered pair of passes, with integer matrices.
    checks=0;rows=[]
    for n in [2,4]:
        matrices=[]
        for a in range(1,n,2):
            for b in range(n):
                for c in range(1,n,2):
                    for d in range(n):
                        for cosine in [-3,3]:
                            mat=np.zeros((2*n,2*n),dtype=np.int64)
                            for j in range(n):
                                x=(a*j+b)%n;y=(c*j+d)%n+n
                                mat[j,x]=cosine;mat[j,y]=4
                                mat[j+n,x]=-4;mat[j+n,y]=cosine
                            assert np.array_equal(mat@mat.T,25*np.eye(2*n,dtype=np.int64))
                            matrices.append(mat)
        for m in range(1,n+1):
            u=np.array([int(j<m) for j in range(2*n)],dtype=np.int64)
            total=0
            for a in matrices:
                for b in matrices:
                    total+=int(u@b@a@u);checks+=1
            got=Q(total,25*len(matrices)**2*m)
            assert got==-Q(16*m,25*n)
            rows.append(dict(n=n,m=m,matrices=len(matrices),covariance=str(got)))
    return dict(ordered_two_pass_checks=checks,rows=rows)


result=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
for name,fn in [('theory',theory),('permutations',permutations),('experiment',experiment),('exact_two_pass',exact_two_pass)]:
    if name in result:continue
    before=time.monotonic();r=fn();r['elapsed_seconds']=time.monotonic()-before;result[name]=r
    OUT.write_text(json.dumps(result,indent=2)+'\n');print('PASS',name,flush=True)
