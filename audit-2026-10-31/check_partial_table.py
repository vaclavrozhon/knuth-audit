"""Compare all 27 printed entries of answer363(e) with the definition."""
from pathlib import Path
import json
from check_surveys import stable_and_constrained

columns=[(0,0),(0,1),(0,None),(1,0),(1,1),(1,None),(None,0),(None,1),(None,None)]
printed=[['0','q1q2','0','q1q3','q1q2q3','q1q2p3','0','q1p2q3','q1p2p3'],
         ['q2q3','q1q2q3','q1q2p3','q1q2q3','q1q2q3','q1q2p3','q1p2q3','q1p2q3','q1p2p3'],
         ['0','p1q2q3','p1q2p3','p1q2q3','p1q2q3','p1q2p3','p1p2q3','p1p2q3','p1p2p3']]
checks=0
for row,x1 in enumerate([0,1,None]):
    for col,(x2,x3) in enumerate(columns):
        assignment=(x1,x2,x3);valid,constrained=stable_and_constrained(assignment,[(1,2,3)])
        if not valid:value='0'
        else:value=''.join(('p' if x is None else 'q')+str(i) for i,x in enumerate(assignment,1) if x is None or i not in constrained) or '1'
        assert value==printed[row][col],(assignment,value,printed[row][col]);checks+=1
result=dict(table_entries=checks,all_match=True,source='Volume4B page619; author PS page255')
Path('results/partial_table.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
