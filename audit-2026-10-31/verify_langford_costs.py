from pathlib import Path
from collections import Counter
import re,json
from check_langford_costs import costs
R=Path(__file__).parent/'results/langford_costs';report=[];optima=[]
for which,name in enumerate(['sum1','sum2','squared_values']):
    text=(R/(name+'.out')).read_text();models={};seen=0
    for block in re.split(r'(?m)^(?=\d+: \(total cost)',text):
        if not block.strip():continue
        lines=block.splitlines();price=int(re.search(r'\$(\d+)',lines[0]).group(1));a=[0]*32;used=set()
        for line in lines[1:]:
            toks=line.split('(')[0].split();i=int(next(t[1:] for t in toks if t[0]=='n'));j,k=sorted(int(t[1:]) for t in toks if t[0]=='s')
            assert k-j==i+1 and i not in used and not a[j-1] and not a[k-1]
            used.add(i);a[j-1]=a[k-1]=i
        assert len(used)==16 and costs(a)[which]==price
        assert tuple(a) not in models;models[tuple(a)]=price;seen+=1
    best=min(models.values());opt={a for a,v in models.items() if v==best};optima.append(opt)
    expected=[3708,68880,37552][which];assert best==expected and len(opt)==[12016,12016,1][which]
    ip=json.loads((R/(name+'-milp.json')).read_text());assert ip['status']==0 and ip['objective']==best
    report.append(dict(kind=name,accepted_models=seen,optimum=best,optimal_models=len(opt),next_cost=min(v for v in models.values() if v>best)))
assert optima[0]==optima[1]
assert next(iter(optima[2]))==tuple(json.loads((R/'basics.json').read_text())['printed_lexmax'])
(R/'verified.json').write_text(json.dumps(dict(results=report,first_two_optimal_sets_identical=True),indent=2)+'\n')
print(report)
