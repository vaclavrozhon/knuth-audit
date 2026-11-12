from pathlib import Path
import json,re
R=Path(__file__).parent/'results/usa_partitions';graph=json.loads((R/'graph.json').read_text());E=graph['edges'];report=[]
for name in ['n48-k6','n48-k8','n49-k7']:
    d=json.loads((R/(name+'.json')).read_text());dp=json.loads((R/(name+'-dp.json')).read_text());states=d['states'];index={s:i for i,s in enumerate(states)};edges=E+([['DC','MD'],['DC','VA']] if d['n']==49 else []);models={}
    for block in re.split(r'(?m)^(?=\d+: \(total cost)',(R/(name+'-cost.out')).read_text()):
        if not block.strip():continue
        lines=block.splitlines();c=int(re.search(r'\$(\d+)',lines[0]).group(1));groups=[]
        for line in lines[1:]:
            group=set(line.split('(')[0].split());assert len(group)==d['k'];groups.append(group)
            seen={next(iter(group))}
            while True:
                new=seen|{b for a,b in edges if a in seen and b in group}|{a for a,b in edges if b in seen and a in group}
                if new==seen:break
                seen=new
            assert seen==group
        assert set.union(*groups)==set(states) and sum(map(len,groups))==len(states)
        price=sum(sum((a in g)!=(b in g) for a,b in edges) for g in groups);assert price==c
        key=tuple(sorted(tuple(sorted(g)) for g in groups));assert key not in models;models[key]=c
    best=min(models.values());assert best==dp['minimum_cost'] and sum(v==best for v in models.values())==dp['optimal_count']
    masks=[d['rows'][i]['mask'] for i in dp['witness_rows']];assert sum(masks)==(1<<d['n'])-1 and sum(d['rows'][i]['cost'] for i in dp['witness_rows'])==best
    native=R/(name+'-count.log')
    if native.exists():assert int(re.search(r'Altogether (\d+) solutions',native.read_text()).group(1))==dp['count']
    assert dp['count']=={'n48-k6':4536539,'n48-k8':4177616,'n49-k7':4517463}[name]
    report.append(dict(case=name,**dp,accepted_models=len(models),native_count_complete=native.exists()))
d=json.loads((R/'n48-k6.json').read_text());expected=[set('MT TX WY CO NM'.split())|{s} for s in ['ID','UT','AZ']]+[set('MT TX ID UT CO OK'.split()),set('MT TX SD MO IA OK'.split()),set('MT TX SD MO NE AR'.split())];assert {frozenset(x) for x in d['mt_tx']}=={frozenset(x) for x in expected};assert sorted(d['chain_residual_components'])==[11,31] and d['maine_options']==25
# Exercise242: independent integer partition feasibility.
checks=0
for L in range(1,16):
 for U in range(L+1,21):
  can=[True]+[False]*200
  for i in range(1,201):
   can[i]=any(can[i-j] for j in range(L,min(U,i+1)));assert can[i]==(i>=L*((i+U-2)//(U-1)));checks+=1
(R/'verified.json').write_text(json.dumps(dict(cases=report,interval_checks=checks,exercise240_six_options_correct=True),indent=2)+'\n');print('All model certificates and counts agree; interval checks',checks)
