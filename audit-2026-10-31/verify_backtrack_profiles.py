"""Compare archived profiles with printed values and an independent permutation oracle."""
from pathlib import Path
from itertools import permutations
import json

R = Path(__file__).resolve().parent / 'results/backtrack_basics'
data = json.loads((R/'profiles.json').read_text())
small = json.loads((R/'verified.json').read_text())
Q = [1,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596,2279184,14772512]
H = [1,1,1,3,7,23,83,405,2113,12657,82297,596483,4698655,40071743,367854835]
P16 = [1,16,210,2236,19688,141812,838816,3998456,15324708,46358876,
       108478966,193892860,260303408,253897632,171158018,72002088,14772512]
for item in data:
    expected = Q if item['kind']=='queens' else H
    assert item['profile'][-1] == expected[item['n']]
    if item['kind']=='queens' and 1 <= item['n'] <= 12:
        assert item['profile'] == small['queens'][item['n']-1]['profile']
    if item['kind']=='queens' and item['n']==16:
        assert item['profile']==P16 and sum(P16)==1141190303
bee_oracle = []
for n in range(11):
    count = sum(len({v-i for i,v in enumerate(p)}) == n for p in permutations(range(n)))
    assert count == H[n]
    bee_oracle.append(count)
result = dict(status='pass', queen_counts=Q, bee_counts=H, queen16_profile=P16,
              queen16_nodes=sum(P16), bee_permutation_oracle=bee_oracle,
              independent_small_checks='B* and permutation enumeration in verified.json')
(R/'profiles-verified.json').write_text(json.dumps(result,indent=2)+'\n')
print('All profiles and counts agree; independent bee permutations through n=10.')
