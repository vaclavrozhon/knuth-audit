"""Rigorous fixed-point powers for queen_power_threshold.cpp."""
from pathlib import Path
from math import isqrt
import json,hashlib
ROOT=Path(__file__).parent;OUT=ROOT/'results/queen_costs'
C=2**56
values=sorted({(2*r-15)**2+(2*c-15)**2 for r in range(16) for c in range(16)})
weights=[]
for v in values:
    for n in range(160):
        for w in values:
            # Only w<=v is ever used: v is the largest uncancelled norm.
            weights.append(isqrt((C*C*w**n)//v**n) if w<=v and n>=21 else 0)
p=OUT/'power-intervals.txt';p.write_text(str(len(values))+'\n'+' '.join(map(str,values))+'\n'+' '.join(map(str,weights))+'\n')
(OUT/'power-intervals.json').write_text(json.dumps(dict(scale=C,norm_values=values,entries=len(weights),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),formula='floor(2^56*(w/v)^(N/2)) = isqrt(floor(2^112*w^N/v^N))',rounding_error_per_solution_less_than=16),indent=2)+'\n')
print(len(weights),'exact integer interval endpoints generated.')
