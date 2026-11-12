"""Reproducible workloads for TAOCP 2 exercise4.2.4-2.

Exact rational operations followed by nearest/even rounding; unbounded exponents.
Checkpoint per workload/radix; already completed blocks are preserved.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,time
from accuracy_model import Arithmetic
from float_model import power
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/benford-addition.json'
CONFIG={'formats':[[2,53],[10,16],[16,14],[64,9]],'horner_points':1001,'horner_degree':12,'gaussian_n':24,'rk_steps':2000,'ties':'even','exponent_range':'unbounded','normalization':'exact sum, with rounded result tabulated separately'}

def exponent(z,b,start=0):
    """Unrounded normalized exponent, with exact comparisons."""
    assert z
    e=start;t=power(b,e);z=abs(z)
    while z>=t:e+=1;t*=b
    while z<t/b:e-=1;t/=b
    return e

class Observed(Arithmetic):
 def __init__(self,b,p):
  super().__init__(b,p,'even');self.c=Counter();self.align=Counter();self.norm=Counter();self.rounded_norm=Counter();self.gaps=0;self.left=0
 def add(self,x,y):
  x,y=Q(x),Q(y);z=x+y;w=self.R(z);c=self.c;c['operations']+=1
  if not x or not y:
   c['zero_operand']+=1;self.align['over5']+=1
  else:
   c['nonzero_operands']+=1;c['same_sign' if x*y>0 else 'opposite_sign']+=1
   ex,ey=self.encode(x)[0],self.encode(y)[0];g=abs(ex-ey);self.gaps+=g
   self.align[str(g) if g<=5 else 'over5']+=1
  if not z:
   c['zero_result']+=1;self.norm['left>4']+=1;self.rounded_norm['left>4']+=1
  else:
   E=max(self.encode(v)[0] for v in (x,y) if v)
   ez=exponent(z,self.b,E);ew=self.encode(w)[0]
   for target,e in [(self.norm,ez),(self.rounded_norm,ew)]:
    s=E-e;assert s>=-1,(x,y,self.b,s)
    target['right1' if s==-1 else 'none' if s==0 else 'left'+str(s) if s<=4 else 'left>4']+=1
   s=E-ez;self.left+=max(0,s)
   if ew!=ez:c['rounding_changes_exponent']+=1
   if x and y:
    if x*y>0:assert s in (-1,0)
    else:assert s>=0
  return w
 def sub(self,x,y):return self.add(x,-y)
 def result(self):
  n=self.c['operations'];nz=n-self.c['zero_result']
  return {'counts':dict(self.c),'alignment_counts':dict(self.align),'exact_normalization_counts':dict(self.norm),'rounded_normalization_counts':dict(self.rounded_norm),
  'alignment_frequencies':{k:self.align[k]/n for k in ['0','1','2','3','4','5','over5']},
  'normalization_frequencies':{k:self.norm[k]/n for k in ['right1','none','left1','left2','left3','left4','left>4']},
  'mean_gap_given_nonzero_operands':self.gaps/self.c['nonzero_operands'],
  'mean_left_shifts_given_nonzero_result':self.left/nz}

def validate_classifier():
 count=0
 for b,p in [(2,3),(3,2),(10,1)]:
  A=Observed(b,p)
  vals=[Q(0)]+[s*Q(k)*power(b,e-p) for e in (-1,0,1) for k in range(b**(p-1),b**p) for s in (-1,1)]
  for x in vals:
   for y in vals:
    z=x+y;A.add(x,y)
    if z:
     # Independent finite catalogue of exact exponent intervals.
     candidates=[e for e in range(-10,11) if power(b,e-1)<=abs(z)<power(b,e)]
     assert len(candidates)==1 and exponent(z,b)==candidates[0]
    count+=1
 return count

def horner(A):
 coeff=[Q((-1)**k,k+1) for k in range(13)];q=[A.R(x) for x in coeff];error=Q(0)
 for i in range(1001):
  x=Q(19*(i-500),10000);xx=A.R(x);y=q[-1];true=coeff[-1]
  for c,d in zip(reversed(q[:-1]),reversed(coeff[:-1])):
   y=A.add(A.mul(y,xx),c);true=true*x+d
  error=max(error,abs(y-true))
 return {'max_absolute_value_error':float(error)}

def gaussian(A):
 n=24;exact=[[Q((17*i+23*j)%31-15,64)+(20 if i==j else 0) for j in range(n)] for i in range(n)]
 mat=[[A.R(v) for v in row] for row in exact];rhs=[A.R(sum(row)) for row in exact]
 for k in range(n):
  assert mat[k][k]
  for i in range(k+1,n):
   factor=A.div(mat[i][k],mat[k][k]);mat[i][k]=Q(0)
   for j in range(k+1,n):mat[i][j]=A.sub(mat[i][j],A.mul(factor,mat[k][j]))
   rhs[i]=A.sub(rhs[i],A.mul(factor,rhs[k]))
 sol=[Q(0)]*n
 for i in range(n-1,-1,-1):
  v=rhs[i]
  for j in range(i+1,n):v=A.sub(v,A.mul(mat[i][j],sol[j]))
  sol[i]=A.div(v,mat[i][i])
 return {'max_error_from_exact_solution_one':float(max(abs(v-1) for v in sol))}

def oscillator(A):
 h=A.R(Q(1,100));half=A.R(Q(1,2));sixth=A.R(Q(1,6));x=Q(1);v=Q(0)
 def inc(x,v):return A.mul(h,v),-A.mul(h,x)
 def finish(y,ks):
  k1,k2,k3,k4=ks
  s=A.add(A.add(A.add(k1,A.mul(2,k2)),A.mul(2,k3)),k4)
  return A.add(y,A.mul(sixth,s))
 for _ in range(2000):
  k1,l1=inc(x,v)
  k2,l2=inc(A.add(x,A.mul(half,k1)),A.add(v,A.mul(half,l1)))
  k3,l3=inc(A.add(x,A.mul(half,k2)),A.add(v,A.mul(half,l2)))
  k4,l4=inc(A.add(x,k3),A.add(v,l3))
  x,v=finish(x,(k1,k2,k3,k4)),finish(v,(l1,l2,l3,l4))
 return {'final_x':float(x),'final_v':float(v),'absolute_energy_defect':float(abs(x*x+v*v-1)),
 'note':'Energy defect includes RK4 discretization error; it is not a pure rounding error.'}

def main():
 data=json.loads(OUT.read_text()) if OUT.exists() else {'config':CONFIG,'blocks':{}}
 assert data['config']==CONFIG
 def save():OUT.write_text(json.dumps(data,indent=2)+'\n')
 if 'classifier_cases' not in data:
  data['classifier_cases']=validate_classifier();save();print('classifier',data['classifier_cases'],flush=True)
 for b,p in CONFIG['formats']:
  for name,run in [('horner',horner),('gaussian',gaussian),('oscillator',oscillator)]:
   key=f'{name}-b{b}-p{p}'
   if key in data['blocks']:continue
   A=Observed(b,p);start=time.monotonic();diagnostics=run(A);r=A.result()
   assert sum(r['alignment_counts'].values())==r['counts']['operations']
   assert sum(r['exact_normalization_counts'].values())==r['counts']['operations']
   assert sum(r['rounded_normalization_counts'].values())==r['counts']['operations']
   r.update(b=b,p=p,workload=name,elapsed_seconds=time.monotonic()-start,diagnostics=diagnostics);data['blocks'][key]=r;save()
   print(key,r['counts'],r['mean_gap_given_nonzero_operands'],r['normalization_frequencies'],flush=True)
 data['status']='completed';save()
if __name__=='__main__':main()
