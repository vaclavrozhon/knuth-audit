"""Independent capacity-token model versus literal memory execution, C0034."""
from pathlib import Path
import json
from check_sequential_allocation import Stacks

def pair_cap(c,i):
    # All stacks empty before/after a push-pop pair.
    overflow=c[i]==0
    if overflow:
        right=next((j for j in range(i+1,len(c)) if c[j]),None)
        donor=right if right is not None else max(j for j in range(i) if c[j])
        c[donor]-=1;c[i]+=1
    return overflow

rows=[];family=[];checks=0
for n in range(2,65):
    caps=[0]*(n-1)+[n];a=Stacks(caps.copy());b=Stacks([1]*n)
    for lower in range(n-1):
        for i in range(n-2,lower-1,-1):
            expected=pair_cap(caps,i)
            assert a.push(i,(lower,i))==expected==True
            assert b.push(i,(lower,i))==False
            assert [a.b[j+1]-a.b[j] for j in range(n)]==caps
            a.pop(i);b.pop(i);checks+=1
            if n==4:rows.append({'pair':'I'+str(i+1)+' D'+str(i+1),'capacities0':caps.copy(),'overflows0':a.overflows,'overflows1':b.overflows})
    assert a.overflows==n*(n-1)//2 and b.overflows==0
    assert caps==[1]*n
    family.append({'n':n,'memory':n,'overflows0':a.overflows,'overflows1':b.overflows})
r={'checks':checks,'n4_pairs':rows,'family':family,'small_counterexample':'First five n=4 pairs suffice; omit the last pop for a nine-operation counterexample.','proof':'notes/sequential-overflow-bound.md'}
(Path(__file__).parent/'results/sequential-overflow-bound.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'checked_pairs':checks,'n4_pairs':rows,'range_n':[2,64]},indent=2))
