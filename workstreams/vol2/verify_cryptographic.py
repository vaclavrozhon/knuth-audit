"""Exact checks for TAOCP 3.5F, separate from the general proofs."""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as F
from math import gcd,ceil
import argparse,json
P=Path(__file__).resolve().parent;OUT=P/'results/cryptographic.json'
p=argparse.ArgumentParser();p.add_argument('--resume',action='store_true');args=p.parse_args()
r=json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}
def save():OUT.write_text(json.dumps(r,indent=2)+'\n')
def parity(x):return x.bit_count()&1
if 'hybrids' not in r:
 cases=0
 for N in range(1,4):
  L=1<<N
  for table in range(1<<L):
   A=lambda w:(table>>w)&1
   for word in range(L):
    for k in range(N):
     tail=N-k;prefix=(word>>tail)<<tail
     pk=F(sum(A(prefix|z) for z in range(1<<tail)),1<<tail)
     tail1=tail-1;prefix1=(word>>tail1)<<tail1
     pk1=F(sum(A(prefix1|z) for z in range(1<<tail1)),1<<tail1)
     nextbit=(word>>tail1)&1
     successes=sum((A(prefix|z)^((z>>tail1)&1)^1)==nextbit for z in range(1<<tail))
     assert F(successes,1<<tail)==F(1,2)+pk1-pk
     cases+=1
 # P2 as printed pads the target bit with0 and uses the success test.
 # N=1, S={1}, A(w)=w: F0=C and T0(0)=C xor0 xorC=0.
 wrong=[c^0^c for c in (0,1)];fixed=[c^c^1 for c in (0,1)]
 assert wrong==[0,0] and fixed==[1,1]
 # Zero-variance counterexample to the non-strict tail inequality.
 assert F(1)>F(1,2)
 r['hybrids']=dict(point_source_identities=cases,N_range=[1,3],P2_counterexample=dict(N=1,source=['1'],test='A(B)=B',printed_outputs=wrong,repaired_outputs=fixed),chebyshev_counterexample=dict(n=1,X1=0,variance=0,t=2,tail_probability=1,claimed_upper_bound='1/2'))
 save();print('PASS hybrid identity and boundary counterexamples',cases,flush=True)
if 'walsh' not in r:
 vals=[]
 for z in product((0,1),repeat=4):vals.append(int(z[0]!=z[1] and z[2]+z[3]<2))
 spectrum={format(x,'04b'):sum((-1)**(vals[z]^parity(x&z)) for z in range(16)) for x in range(16)}
 assert spectrum['1100']==12
 assert {x for x,s in spectrum.items() if s==4}=={'0000','0011','1101','1110'}
 assert all(s<=0 for x,s in spectrum.items() if x not in {'1100','0000','0011','1101','1110'})
 r['walsh']=dict(spectrum_numerator_over16=spectrum,known_erratum='1997-11-30:0001 to0011')
 save();print('PASS printed Walsh example after known erratum',flush=True)
if 'linear_amplification' not in r:
 def fwht(a):
  a=list(a);h=1
  while h<len(a):
   for i in range(0,len(a),2*h):
    for j in range(i,i+h):u,v=a[j],a[j+h];a[j]=u+v;a[j+h]=u-v
   h*=2
  return a
 configurations=[(2,k) for k in range(1,6)]+[(3,2)]
 rows=[];direct_checks=0;pair_checks=0;total_matrices=0
 for R,k in configurations:
  L=1<<R;K=1<<k;n=K-1;matrix_count=1<<(R*k)
  # Explicitly verify pairwise independence by complete matrix enumeration.
  pairs={}
  if k<=3:
   pairs={(c,d):Counter() for c in range(1,K) for d in range(c+1,K)}
  for table in range(1<<L):
   G=lambda z:(table>>z)&1
   sn=[sum((-1)**(G(z)^parity(x&z)) for z in range(L)) for x in range(L)]
   positive=[x for x in range(L) if sn[x]>0]
   failures=Counter();all_list_failures=Counter()
   for matrix in range(matrix_count):
    B=[(matrix>>(j*R))&(L-1) for j in range(k)]
    cb=[0]*K
    for c in range(1,K):
     low=c&-c;cb[c]=cb[c^low]^B[low.bit_length()-1]
    if table==0:
     total_matrices+=1
     for c,d in pairs:pairs[c,d][cb[c],cb[d]]+=1
    transforms=[]
    for i in range(R):
     values=[0]+[(-1)**G(cb[c]^(1<<i)) for c in range(1,K)]
     h=fwht(values);assert all(v&1 for v in h)
     if k<=3:
      for b in range(K):
       assert h[b]==sum((-1)**(parity(b&c)^G(cb[c]^(1<<i))) for c in range(1,K));direct_checks+=1
     transforms.append(h)
    outputs=[sum((transforms[i][b]<0)<<i for i in range(R)) for b in range(K)]
    for x in positive:
     bx=sum(parity(x&B[j])<<j for j in range(k))
     failures[x]+=outputs[bx]!=x
     all_list_failures[x]+=x not in outputs
   for x in positive:
    s=F(sn[x],L);bound=F(R)*(1-s*s)/(n*s*s)
    assert F(failures[x],matrix_count)<=bound
    assert all_list_failures[x]<=failures[x]
    if K>ceil(F(2*R,s*s)):assert 2*all_list_failures[x]<=matrix_count
   rows.append(dict(R=R,k=k,truth_table=table,positive_coefficients={str(x):str(F(sn[x],L)) for x in positive},designated_failures=dict(failures),list_failures=dict(all_list_failures),matrices=matrix_count))
  for c,d in pairs:
   assert len(pairs[c,d])==L*L and set(pairs[c,d].values())=={matrix_count//(L*L)};pair_checks+=1
 r['linear_amplification']=dict(configurations=configurations,truth_tables=len(rows),matrices_per_table_total=total_matrices,direct_transform_entries=direct_checks,pairwise_distributions=pair_checks,rows=rows)
 save();print('PASS AlgorithmL exact distributions',len(rows),direct_checks,pair_checks,flush=True)
if 'blum_squares' not in r:
 from sympy import primerange
 rows=[];roots_checked=0
 for R in range(3,13):
  primes=list(primerange(3,1<<((R+2)//2+1)))
  for p in primes:
   if p%4!=3 or not (2**(R-2)<p*p<2**(R-1)):continue
   for q in primes:
    if q%4!=3 or not (2**R<q*q<2**(R+1)):continue
    M=p*q;assert 2**(R-1)<M<2**R
    units=[x for x in range(1,M) if gcd(x,M)==1]
    roots={}
    for x in units:roots.setdefault(x*x%M,[]).append(x)
    QR=set(roots);assert len(QR)==(p-1)*(q-1)//4
    assert {x*x%M for x in QR}==QR
    for y,rs in roots.items():
     assert len(rs)==4
     qr=[x for x in rs if x in QR];assert len(qr)==1
     for chosen in rs:
      good=[x0 for x0 in rs if gcd(chosen-x0,M) in (p,q)]
      assert len(good)==2
      for x0 in good:assert gcd(chosen-x0,M)*gcd(chosen+x0,M)==M
      roots_checked+=1
    rows.append(dict(R=R,p=p,q=q,M=M,units=len(units),quadratic_residues=len(QR)))
 r['blum_squares']=dict(moduli=len(rows),chosen_roots_checked=roots_checked,rows=rows,note='Uniformity conditional on a fixedM; this does not equate uniformM with uniform triples over allM.')
 save();print('PASS Blum square permutations and factor recovery',len(rows),roots_checked,flush=True)
if 'numeric_examples' not in r:
 import mpmath as mp
 mp.mp.dps=90
 year=F(3652425,10000)*24*60*60*10**6;assert year==31556952000000
 def estimate(N,R):
  exponent=mp.root(R,4)*mp.log(R)**mp.mpf('.75')
  factor=mp.exp(exponent)/int(year)
  test=(mp.exp(exponent)/(100000*mp.mpf(N)**2*R**2)-mp.mpf(N)*R**2)/int(year)
  return dict(N=N,R=R,factoring_MIP_years=mp.nstr(factor,65),test_MIP_years=mp.nstr(test,65))
 rows=[estimate(1000,50000),estimate(10**10,200000),estimate(10**13,333333)]
 assert mp.mpf('1.5e25')<=mp.mpf(rows[0]['factoring_MIP_years'])<mp.mpf('2.5e25')
 assert mp.mpf(rows[0]['test_MIP_years'])>70000
 assert abs(mp.mpf(rows[1]['test_MIP_years'])/mp.mpf('7.486e10')-1)<mp.mpf('.0001')
 assert abs(mp.mpf(rows[2]['test_MIP_years'])/mp.mpf('535e12')-1)<mp.mpf('.001')
 r['numeric_examples']=dict(instructions_per_MIP_year=int(year),rows=rows,known_erratum='2005-09-20:53.5 to535 teraMIP-years',scope='Conditional historical arithmetic, not a verified factoring lower bound.')
 save();print('PASS conditional numeric estimates after known errata',flush=True)
