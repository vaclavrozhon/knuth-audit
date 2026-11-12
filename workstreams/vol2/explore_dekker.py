"""Exploration used to discover the exact recursive-failure family.

Completed six300-input blocks are checkpointed; do not rerun without reason.
"""
import json,sys,random
from fractions import Fraction as Q
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from dekker_recursive import Recursive,val,flatten
out=[]
for p in [3,4,6,8,12,20]:
 r=Recursive(p);rng=random.Random(42390+p);best=None;headfail=None
 for i in range(300):
  x=Q(rng.randrange(2**(4*p-1),2**(4*p)),2**(4*p))
  y=Q(rng.randrange(2**(4*p-1),2**(4*p)),2**(4*p))*rng.choice([-1,1])
  a=r.encode(x,2);b=r.encode(y,2);assert val(a)==x and val(b)==y
  r.count=0;r.trace=[];c=r.add(a,b,2);assert r.count==64
  err=abs(val(c)-x-y)/(abs(x)+abs(y))
  if best is None or err>Q(best['normalized_error']):best={'p':p,'i':i,'x':str(x),'y':str(y),'a':flatten(a),'b':flatten(b),'answer':flatten(c),'normalized_error':str(err),'error_in_4p_units':float(err*2**(4*p)),'error_in_2p_units':float(err*2**(2*p)),'trace':r.trace}
  if headfail is None and r.trace[-1]['head_sum_residual_error']!='0':headfail=r.trace[-1]
 out.append({'p':p,'best':best,'headfail':headfail})
 (ROOT/'results/dekker-recursive-exploration.json').write_text(json.dumps(out,indent=2)+'\n')
 print(p,{k:v for k,v in best.items() if k!='trace'},'headfail',headfail,flush=True)
