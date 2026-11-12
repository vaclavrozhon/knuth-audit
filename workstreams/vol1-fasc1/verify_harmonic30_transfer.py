"""Transfer ten existing MIX sums; only inspect the 65 changed tie positions.
No resummation of the harmonic terms or groups is performed.
"""
from pathlib import Path
import json
p=Path(__file__).parent
old=json.loads((p.parent/'vol1/results/rounded-harmonic.json').read_text())
rows=[]
for row in old['values']:
    n=row['n']; M=10**n
    def up(k): return (2*M+k)//(2*k)
    changes=[]
    for j in range(n+1):
        k=2*M//5**j
        left,mid,right=up(k-1),up(k),up(k+1)
        delta=int(left!=mid-1)+int(mid-1!=right)-int(left!=mid)-int(mid!=right)
        changes.append({'index':k,'old':mid,'new':mid-1,'group_count_change':delta})
    dg=sum(x['group_count_change'] for x in changes)
    assert dg==0
    scaled=row['scaled_sum']-(n+1)
    whole,frac=divmod(scaled,M)
    rows.append({'n':n,'scaled_ties_even_sum':scaled,'output':f'{whole}.{frac:0{n}d}',
                 'groups_after_first':row['groups_after_first']+dg,
                 'digits':len(str(scaled)),'tie_changes':changes})
g=sum(x['groups_after_first'] for x in rows);digits=sum(x['digits'] for x in rows)
out={'source':'workstreams/vol1/results/rounded-harmonic.json',
     'method':'Each of n+1 reciprocal half ties rounds downward to an even integer; inherited scaled sum minus n+1. Only changed adjacent-boundary indicators counted.',
     'rows':rows,'groups_after_first_total':g,'digits_total':digits,
     'memory_units':digits+10,'oops':139*g+66*digits+99*10+9,
     'timing_formula':'139 sum(groups_after_first) + 66 sum(decimal_digits) + 99*10 + 9; memory writes are digits plus ten newlines.'}
assert out['oops']==40659359 and out['memory_units']==82
(p/'results/harmonic30-transfer.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
print([x['output'] for x in rows])
