"""Exact finite models for TAOCP2 4.5.4-43; proofs are in notes/bbs.md.

Checks are structural/certificate checks, not empirical proofs of cryptographic
hardness. The recovery experiment supplies the true initial branch and a perfect
oracle; it does not enumerate the exponentially-in-precision guess family.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd, isqrt, ceil, log, exp
from collections import Counter
import json, time, argparse, random
ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/bbs.json'


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))


def legendre(x, p):
    v = pow(x, (p-1)//2, p)
    return -1 if v == p-1 else v


def chi(x, p, q):
    a, b = legendre(x, p), legendre(x, q)
    return a if a == b and a else 0


def qrroot(y, p, q):
    a, b = pow(y, (p+1)//4, p), pow(y, (q+1)//4, q)
    return a+p*((b-a)*pow(p, -1, q) % q)


def nearest_grid(x, width):
    return (2*(x//(2*width))+1)*width


def structure():
    rows=[]; identities=0
    for r in range(4,13):
        for p in range(3, 1+isqrt(2**(r-1)),4):
            if not (2**(r-2)<p*p<2**(r-1) and prime(p)): continue
            for q in range(3, 2+isqrt(2**(r+1)),4):
                m=p*q
                if not (2**r<q*q<2**(r+1) and 2**(r-1)<m<2**r and prime(q)):continue
                Q={x*x%m for x in range(m)};roots={x*x%m:x for x in Q}
                assert len(roots)==len(Q)==(p+1)*(q+1)//4
                multiplicities=Counter(x*x%m for x in range(m))
                for y in Q:
                    assert qrroot(y,p,q)==roots[y]
                    assert multiplicities[y]==(1 if y%p==0 else 2)*(1 if y%q==0 else 2)
                U=sorted(y for y in Q if gcd(y,m)==1)
                for s in list(dict.fromkeys(U[:3]+U[-3:])):
                    for v in range(m):
                        tau=v*s%m;half=v*pow(2,-1,m)%m
                        assert half*s%m==(tau+m*(tau&1))//2
                        assert chi(4*v%m,p,q)==chi(v,p,q)
                        if tau:
                            assert ((-v*s%m)&1)+(tau&1)==1
                        if gcd(v,m)==1 and chi(v,p,q):
                            z=chi(v,p,q)*v*s%m
                            assert z==qrroot(v*v*s*s%m,p,q)
                        identities+=1
                rows.append(dict(r=r,p=p,q=q,m=m,squares=len(Q)))
    # Full pairwise image, compared with determinant's CRT invertibility.
    pair_rows=[];m=209
    for delta in [1,2,10,11,19]:
        image=Counter((a%m,(a+delta*b)%m) for a in range(m) for b in range(m))
        d=gcd(delta,m)
        assert len(image)==m*m//d and set(image.values())=={d}
        pair_rows.append(dict(difference=delta,gcd=d,image_size=len(image),fiber=d))
    return dict(modules=rows,algebra_identities=identities,pairwise_images=pair_rows)


def counterexamples():
    p,q=11,19;m=p*q;Q=sorted({x*x%m for x in range(m)});root={x*x%m:x for x in Q}
    units=[x for x in Q if gcd(x,m)==1];nonunits=[x for x in Q if gcd(x,m)>1]
    S=set(nonunits+units[:16]);G=lambda y:(root[y]&1)^(y not in S)
    uniform=F(len(S),len(Q));weighted=F(sum(G(pow(x,4,m))==((x*x%m)&1) for x in range(m)),m)
    assert uniform==F(31,60) and weighted==F(93,209)
    eps=F(1,60);n=ceil(F(1,2)*eps**-2*log(4));upper=exp(-2*n*float(F(1,2)-weighted)**2)
    assert n==2496 and upper<3e-7
    a,b,j=1,2,-6;eps=F(1,2);alpha=F(1,128);beta=F(5,512);bp=beta/2
    u=(a+(j+pow(2,-1,m))*b)%m
    assert u==199 and chi(u,p,q)==1
    assert abs(F(a,m)-alpha)<eps/64 and abs(F(b,m)-beta)<eps**3/64
    exact=(a+j*b+b//2)//m;good=(alpha+j*beta+bp)//1;bad=(alpha*j*beta+bp)//1
    assert exact==good==-1 and bad==0
    assert eps*m/16<u<(1-eps/16)*m
    z_old=[];z_fixed=[]
    for u in range(1,m):
        if gcd(u,m)>1:continue
        c=chi(u,p,q);edge=F(u,m)<eps/16 or F(u,m)>1-eps/16;g=root[u*u%m]&1
        z_old.append(-1 if c and (edge or g!=(u&1)) else abs(c))
        z_fixed.append(-1 if c and (edge or g!=((c*u%m)&1)) else abs(c))
    assert F(sum(z_old),len(z_old))==F(-2,45)
    assert F(sum(z_fixed),len(z_fixed))==F(37,90)
    stage_sum=F(4,9)*sum(F(1,min(8,2**t)) for t in range(8))
    assert stage_sum==F(19,18)>F(8,9)
    # Conservative repaired constants, exact over a grid of r and dyadic eta.
    checked=0
    for r in range(4,257):
        for e in range(3,11):
            eta=F(1,2**e);nmax=64*r*eta**-2;B=4096*r*eta**-2
            assert nmax<B
            assert 4/B<eta/1024
            assert eta/4096+eta/128+eta**3/8192+eta/1024<eta/64
            assert sum(F(1,32*min(r,2**t)) for t in range(r))<F(3,32)
            checked+=1
    return dict(m=m,good_inputs=sorted(S),success_uniform=str(uniform),success_sampling=str(weighted),
                samples=n,probability_correct_upper_bound=upper,
                floor=dict(a=a,b=b,j=j,u=199,alpha=str(alpha),beta=str(beta),beta_next=str(bp),
                           exact=int(exact),correct=int(good),printed=int(bad)),
                Z_mean_printed='-2/45',Z_mean_corrected='37/90',stage_sum_r8=str(stage_sum),
                repaired_constant_checks=checked,
                hint_zero_case=dict(m=m,y=0,v=1,lambda_sum=0))


def recovery():
    p,q=383,787;assert prime(p) and prime(q) and p%4==q%4==3
    m=p*q;r=m.bit_length();eps=F(1,2);rng=random.Random(4300182)
    roots_checked=0;votes=0;dominance=0;traces=[]
    for case in range(12):
        x=rng.randrange(1,m)
        while legendre(x,p)*legendre(x,q)!=-1:x=rng.randrange(1,m)
        y=x*x%m;s=qrroot(y,p,q);assert s*s%m==y
        a=rng.randrange(1,m);b=rng.randrange(1,m)
        while gcd(a*b,m)>1:a=rng.randrange(1,m);b=rng.randrange(1,m)
        A=a*s%m;B=b*s%m
        alpha=nearest_grid(F(A,m),eps/64);beta=nearest_grid(F(B,m),eps**3/64)
        la,lb=A&1,B&1;ai,bi=a,b
        all_right=True
        for t in range(r):
            n=4*min(r,2**t)*eps**-2;n=int(n);assert n<p
            an=(alpha+la)/2;bn=(beta+lb)/2
            ain=ai*pow(2,-1,m)%m;bin_=bi*pow(2,-1,m)%m
            trueA=ai*s%m;trueB=bi*s%m;trueAn=ain*s%m;trueBn=bin_*s%m
            decisions=[]
            # First recover the next bit of b, then of a.
            for kind in ['u','v']:
                total=0;target=trueBn&1 if kind=='u' else trueAn&1
                for j in range(-n//2,n//2):
                    u=(ai+j*bi+bin_)%m if kind=='u' else (ain+j*bin_)%m
                    c=chi(u,p,q);tau=u*s%m
                    if not c:continue
                    canonical=qrroot(u*u*y%m,p,q);assert canonical==c*tau%m
                    g=canonical&1
                    f=(alpha+j*beta+bn)//1 if kind=='u' else (an+j*bn)//1
                    base=la+j*lb if kind=='u' else j*decisions[0]
                    guess=(g+base+f)%2;Y=(2*guess-1)*c;total+=Y
                    exactsum=trueA+j*trueB+trueBn if kind=='u' else trueAn+j*trueBn
                    assert (exactsum//m)&1==((tau&1)+(trueA&1)+j*(trueB&1)+target)%2 if kind=='u' else (exactsum//m)&1==((tau&1)+(trueAn&1)+j*(trueBn&1))%2
                    edge=F(tau,m)<eps/16 or F(tau,m)>1-eps/16
                    z=-1 if edge else 1
                    if all_right:assert z <= (2*target-1)*Y
                    dominance+=int(all_right);votes+=1
                guessed=int(total>=0);decisions.append(guessed)
                if guessed!=target:all_right=False
            lb,la=decisions;alpha,beta=an,bn;ai,bi=ain,bin_
            if not all_right:break
        if all_right:
            recovered=(2**r*pow(b,-1,m)*int(beta*m+F(1,2)))%m
            assert recovered==s
            d=gcd(x-recovered,m);assert d in [p,q]
            roots_checked+=1
        traces.append(dict(x=x,a=a,b=b,success=all_right,stages=t+1))
    assert roots_checked==12
    return dict(modulus=m,p=p,q=q,true_initial_branch=True,oracle='perfect canonical-root bit',
                successful_roots=roots_checked,votes=votes,pointwise_dominance_checks=dominance,traces=traces,
                limitation='Algebraic recovery tests with supplied correct branch, not full branch enumeration or proof of success rate.')


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--resume',action='store_true');args=parser.parse_args()
    data=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {'blocks':{}}
    for name,fn in [('structure',structure),('counterexamples',counterexamples),('recovery',recovery)]:
        if data['blocks'].get(name,{}).get('status')=='passed':continue
        start=time.perf_counter();result=fn();data['blocks'][name]=dict(status='passed',seconds=time.perf_counter()-start,result=result)
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,'passed',data['blocks'][name]['seconds'],flush=True)
    data['status']='passed';OUT.write_text(json.dumps(data,indent=2)+'\n')

if __name__=='__main__':main()
