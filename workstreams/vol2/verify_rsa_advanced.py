"""Exact checks of TAOCP 2 exercise 44 and both versions of exercise 47.

FLINT supplies short lattice bases; Python integers/Fractions independently
check transformation, determinant, Gram-Schmidt inequalities, and root bounds.
PARI proposes primality certificates; verify_ecpp independently checks them.
All completed checkpoints are reused. See notes/rsa-advanced.md.
"""
from pathlib import Path
from math import gcd, isqrt, prod
from fractions import Fraction as Q
import datetime
import json
import os
import random
import subprocess
import sys
import time
from flint import fmpz_mat
from verify_ecpp import Verifier

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/rsa-advanced.json'
GP='/tmp/knuth-vol2-or9kgh/pari-local/usr/bin/gp'


def save(path,data):
    tmp=path.with_suffix('.tmp')
    tmp.write_text(json.dumps(data,indent=2)+'\n')
    tmp.replace(path)


def determinant(A):
    A=[list(row) for row in A];n=len(A);prev=1;sign=1
    for k in range(n-1):
        if not A[k][k]:
            j=next(j for j in range(k+1,n) if A[j][k])
            A[k],A[j]=A[j],A[k];sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=A[i][j]*pivot-A[i][k]*A[k][j]
                assert num%prev==0
                A[i][j]=num//prev
            A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]


def gram_schmidt(rows):
    orth=[];norm=[];mus=[]
    for row in rows:
        z=list(map(Q,row));mu=[]
        for j,w in enumerate(orth):
            t=sum(Q(x)*y for x,y in zip(row,w))/norm[j]
            mu.append(t);z=[x-t*y for x,y in zip(z,w)]
        norm.append(sum(t*t for t in z));orth.append(z);mus.append(mu)
    for i in range(len(rows)):
        assert norm[i]>0
        assert all(abs(t)<=Q(51,100) for t in mus[i])
        if i:assert norm[i]+mus[i][i-1]**2*norm[i-1]>=Q(3,4)*norm[i-1]
    return norm


def peval(c,x):
    value=0
    for a in reversed(c):value=value*x+a
    return value


def lattice_checks():
    rng=random.Random(45444)
    bases=[2,3,5,7,11,13,17,19,23,29,31]
    cases=[]
    for d,mode in [(2,'zero'),(2,'upper'),(3,'negative'),(3,'generic'),
                   (4,'timestamp'),(4,'generic'),(4,'three_roots'),
                   (4,'nonunit_coefficients'),(5,'generic')]:
        k=d*(d-1)//2+1;n=d+k
        threshold_squared=n**n*2**(n*n)*d**(2*d)
        floor_threshold=isqrt(threshold_squared)
        target=floor_threshold+2
        if d==4:
            assert threshold_squared<10**54
            target=10**27+1
        bs=bases[1:k+1] if mode=='timestamp' else bases[:k]
        if mode=='nonunit_coefficients':bs=[6]+bases[2:k+1]
        moduli=[]
        for b in bs:
            m=b
            while m<=target:m*=b
            moduli.append(m)
        assert all(gcd(a,b)==1 for i,a in enumerate(moduli) for b in moduli[i+1:])
        m=min(moduli);M=prod(moduli)
        x={'zero':0,'upper':m-1,'negative':1-m}.get(mode,m//3+13)
        rows=[]
        for i,mi in enumerate(moduli):
            if mode=='timestamp':
                a=1<<(i+1);t=i+7;c=pow(a*x+t,3,mi)
                coeff=[(t**3-c)%mi,3*a*t*t%mi,3*a*a*t%mi,a**3%mi]
            elif mode=='three_roots':
                roots=[x,x+1,x+2]
                coeff=[-prod(roots),sum(roots[a]*roots[b] for a in range(3) for b in range(a+1,3)),-sum(roots),1]
                coeff=[v%mi for v in coeff]
            elif mode=='nonunit_coefficients' and i==0:
                # 2(X-x)^2+3(X-x): collectively primitive modulo6^e,
                # even though no nonconstant coefficient is a unit.
                x=6*(x//6)
                coeff=[(2*x*x-3*x)%mi,(3-4*x)%mi,2,0]
            else:
                coeff=[0]+[rng.randrange(mi) for _ in range(d-2)]+[1]
                coeff[0]=-peval(coeff,x)%mi
            assert peval(coeff,x)%mi==0 and gcd(*coeff,mi)==1
            rows.append(coeff)
        u=[(M//mi)*pow(M//mi,-1,mi)%M for mi in moduli]
        # A=dL clears the rational last diagonal of the printed matrix.
        A=[[0]*n for _ in range(n)]
        for j in range(d):A[j][j]=d*m**j*M
        for i in range(k):
            for j in range(d):A[d+i][j]=d*m**j*rows[i][j]*u[i]
            A[d+i][d+i]=M//moduli[i]
        det_expected=M**(n-1)*m**(k-1)*d**d
        assert determinant(A)==det_expected
        reduced,transform=fmpz_mat(A).lll(transform=True,delta=.99,eta=.51)
        R=[[int(reduced[i,j]) for j in range(n)] for i in range(n)]
        T=[[int(transform[i,j]) for j in range(n)] for i in range(n)]
        assert abs(determinant(T))==1
        assert all(sum(T[i][h]*A[h][j] for h in range(n))==R[i][j]
                   for i in range(n) for j in range(n))
        norms=gram_schmidt(R)
        assert prod(norms)==det_expected**2
        v=T[0];w=R[0]
        norm2=sum(t*t for t in w)
        assert norm2**n <= (n*2**n)**n*det_expected**2
        assert norm2<M*M
        coeff=[]
        for j in range(d):
            assert w[j]%(d*m**j)==0
            coeff.append(w[j]//(d*m**j))
        assert any(coeff) and peval(coeff,x)==0
        assert all(abs(w[j])<M for j in range(n))
        assert all(abs(v[d+i])<moduli[i] for i in range(k))
        assert all((coeff[j]-v[d+i]*rows[i][j])%moduli[i]==0
                   for i in range(k) for j in range(d))
        cases.append(dict(d=d,k=k,n=n,mode=mode,root=x,moduli=moduli,
                          input_polynomials=rows,threshold_floor=floor_threshold,
                          polynomial=coeff,transform_row=v,short_vector=w,
                          squared_norm=norm2,scaled_determinant=det_expected))
        print('lattice',d,mode,'passed',flush=True)
    return dict(cases=cases,exact_integer_transform_entries=sum(c['n']**2 for c in cases))


def modpower(a,e,n):
    result=1
    while e:
        if e&1:result=result*a%n
        a=a*a%n;e//=2
    return result


def integer_root_checks():
    """Recover every integer root using rational Sturm chains and bisection.

    The planted roots are used only after recovery to validate the output.
    Half-integer interval boundaries cannot lose an integer solution.
    """
    def trim(c):
        c=list(c)
        while c and c[-1]==0:c.pop()
        return c
    def divrem(a,b):
        a=trim(list(map(Q,a)));b=trim(list(map(Q,b)))
        quotient=[Q(0)]*max(0,len(a)-len(b)+1)
        while a and len(a)>=len(b):
            k=len(a)-len(b);v=a[-1]/b[-1];quotient[k]=v
            for j,t in enumerate(b):a[k+j]-=v*t
            a=trim(a)
        return trim(quotient),a
    def derivative(c):return [j*c[j] for j in range(1,len(c))]
    def roots(coeff,m):
        p=list(map(Q,trim(coeff)));a=p;b=derivative(p)
        while b:a,b=b,divrem(a,b)[1]
        q,rem=divrem(p,a);assert not rem
        chain=[q,derivative(q)]
        while chain[-1]:
            _,rem=divrem(chain[-2],chain[-1])
            chain.append([-v for v in rem])
        chain.pop()
        def variations(t):
            values=[peval(c,t) for c in chain]
            signs=[1 if y>0 else -1 for y in values if y]
            return sum(a!=b for a,b in zip(signs,signs[1:]))
        lo,hi=1-m,m-1
        stack=[(lo,hi,variations(Q(2*lo-1,2)),variations(Q(2*hi+1,2)))]
        found=[];visited=0
        while stack:
            lo,hi,left,right=stack.pop();visited+=1
            assert left>=right
            if left==right:continue
            if lo==hi:
                if peval(coeff,lo)==0:found.append(lo)
                continue
            mid=(lo+hi)//2;v=variations(Q(2*mid+1,2))
            stack.extend([(lo,mid,left,v),(mid+1,hi,v,right)])
        return sorted(found),visited
    prior=json.loads(OUT.read_text())['checks']['lattice']['result']['cases']
    rows=[]
    for c in prior:
        found,visited=roots(c['polynomial'],min(c['moduli']))
        assert c['root'] in found
        valid=[x for x in found if all(peval(a,x)%mi==0 for a,mi in
                                      zip(c['input_polynomials'],c['moduli']))]
        assert c['root'] in valid
        if c['mode']=='three_roots':assert valid==[c['root']+i for i in range(3)]
        rows.append(dict(d=c['d'],mode=c['mode'],polynomial_integer_roots=found,
                         valid_common_roots=valid,bisection_nodes=visited))
    # Repeated roots, half-integer roots, and no integer roots exercise endpoints.
    extra=[([0,0,1],3,[0]),([-1,2],3,[]),([1,0,1],3,[]),([-2,1,1],4,[-2,1])]
    for p,m,want in extra:assert roots(p,m)[0]==want
    return dict(cases=rows,extra_cases=len(extra),bisection_nodes=sum(r['bisection_nodes'] for r in rows))


def challenge_checks():
    inp=json.loads((ROOT/'sources/rsa47-inputs.json').read_text())
    old=inp['original'];N=old['N']
    factors=[int(p) for p,e in json.loads((ROOT/'sources/rsa47-factordb-original.json').read_text())['factors'] if e==1]
    assert len(factors)==3 and prod(factors)==N
    cp=ROOT/'results/rsa47-certificates.json'
    certs=json.loads(cp.read_text()) if cp.exists() else {}
    for p in factors:
        if str(p) in certs:continue
        code=f'default(nbthreads,1);print(primecert({p}));quit;\n'
        proc=subprocess.Popen([GP,'-fq','-s','134217728'],stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        print('prime certificate PID',proc.pid,'digits',len(str(p)),'limit60',flush=True)
        try:stdout,stderr=proc.communicate(code,timeout=60)
        except subprocess.TimeoutExpired:
            proc.kill();proc.communicate();raise
        assert proc.returncode==0,(proc.returncode,stderr)
        certs[str(p)]=json.loads(stdout.strip());save(cp,certs)
    v=Verifier()
    for p in factors:
        cert=certs[str(p)]
        if isinstance(cert,list):assert all(row[0]%2==1 for row in cert)
        v.verify(cert,p)
        assert p%3==2
    v.validate_small_certificates()
    phi=prod(p-1 for p in factors);d=pow(3,-1,phi)
    roots=[];chunks=[]
    for c in old['ciphertexts']:
        x=pow(c,d,N);assert x==modpower(c,d,N)
        crt=sum(pow(c,pow(3,-1,p-1),p)*(N//p)*pow(N//p,-1,p) for p in factors)%N
        assert crt==x and pow(x,3,N)==c==((x*x)%N*x)%N
        chunk=x.to_bytes((x.bit_length()+7)//8,'big')
        chunk.decode('ascii')
        roots.append(x);chunks.append(chunk.decode('ascii'))
    plain=''.join(chunks)
    assert 'His remarks (as reported)' in plain and 'Chesterton (1905)' in plain
    (ROOT/'results/rsa47-original-plaintext.txt').write_text(plain)
    new=inp['replacement'];NN=new['N']
    assert len(str(N))==211 and len(str(NN))==318
    assert all(0<=c<NN for c in new['ciphertexts'])
    assert gcd(N,NN)==1
    witness=next(a for a in range(2,101) if pow(a,NN-1,NN)!=1)
    residue=pow(witness,NN-1,NN)
    assert residue==modpower(witness,NN-1,NN)
    return dict(original=dict(N=N,factors=factors,roots=roots,chunk_lengths=list(map(len,chunks)),
                              plaintext=plain,elliptic_curve_links=v.links,
                              terminal_lucas_primes=len(v.small),decimal_digits=211,bits=N.bit_length()),
                replacement=dict(decimal_digits=318,bits=NN.bit_length(),composite_witness=witness,
                                 witness_residue=residue,factorization='not obtained; FactorDB C as of access',
                                 decryption='not obtained; research challenge',shared_factor_with_original=False))


def main():
    state=json.loads(OUT.read_text()) if OUT.exists() else dict(
        started_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        pid=os.getpid(),checks={})
    print('RSA advanced PID',os.getpid(),flush=True)
    state['status']='running';save(OUT,state)
    for name,fn in [('lattice',lattice_checks),('challenge',challenge_checks),
                    ('integer_roots',integer_root_checks)]:
        if name in state['checks']:
            print(name,'existing checkpoint',flush=True);continue
        start=time.monotonic();r=fn()
        state['checks'][name]=dict(status='passed',seconds=time.monotonic()-start,result=r)
        save(OUT,state);print(name,'PASSED',state['checks'][name]['seconds'],flush=True)
    state['status']='passed';save(OUT,state);print('ALL CHECKPOINTS PASSED',flush=True)


if __name__=='__main__':main()
